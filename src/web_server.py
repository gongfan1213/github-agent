from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from config import Config
from llm import LLM
from report_generator import ReportGenerator
from datetime import datetime, timedelta
import requests
from hacker_news_client import HackerNewsClient
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('http_proxy', None)
os.environ.pop('HTTPS_PROXY', None)
os.environ.pop('https_proxy', None)
app = Flask(__name__)

for k in ['HTTP_PROXY', 'http_proxy', 'HTTPS_PROXY', 'https_proxy']:
    if k in os.environ:
        del os.environ[k]
# 配置 LLM 客户端（使用配置文件中的值）
class CustomConfig(Config):
    def __init__(self):
        super().__init__()
        self.llm_model_type = 'openai'
        self.openai_model_name = 'gpt-3.5-turbo'  # 可根据实际模型名调整
        self.ollama_api_url = os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api/chat')
        self.openai_api_key = os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY_HERE')

# 初始化 LLM
config = CustomConfig()
llm_client = OpenAI(
    base_url=os.getenv('OPENAI_BASE_URL', 'YOUR_OPENAI_BASE_URL_HERE'),
    api_key=os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY_HERE')
)
llm = LLM(config)

# 假设有 prompts/github_openai_prompt.txt
report_types = ["github", "hacker_news_hours_topic", "hacker_news_daily_report"]
report_generator = ReportGenerator(llm, report_types)

@app.route('/')
def index():
    return render_template('index.html', report_types=report_types)

@app.route('/api/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    report_type = data.get('report_type')
    markdown_content = data.get('markdown_content', '')
    # 选择 prompt
    system_prompt = report_generator.prompts.get(report_type)
    if not system_prompt:
        return jsonify({'error': 'Prompt not found for this report type.'}), 400
    # 调用 LLM 生成报告
    try:
        result = llm.generate_report(system_prompt, markdown_content)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/statistics', methods=['POST'])
def statistics():
    data = request.json
    repo_url = data.get('repo_url')
    if not repo_url:
        return jsonify({'error': '缺少 repo_url'}), 400
    try:
        parts = repo_url.rstrip('.git').split('/')
        owner, repo = parts[-2], parts[-1]
    except Exception:
        return jsonify({'error': 'repo_url 格式错误'}), 400
    from datetime import datetime, timedelta
    since = (datetime.utcnow() - timedelta(days=30)).isoformat() + 'Z'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    base = f'https://api.github.com/repos/{owner}/{repo}'
    # 拉取数据
    issues = requests.get(f'{base}/issues?since={since}&state=all', headers=headers, proxies={}).json()
    prs = requests.get(f'{base}/pulls?state=all', headers=headers, proxies={}).json()
    commits = requests.get(f'{base}/commits?since={since}', headers=headers, proxies={}).json()
    contributors = requests.get(f'{base}/contributors', headers=headers, proxies={}).json()
    # 只取前3条，进一步防止内容过长
    issues_sample = issues[:3] if isinstance(issues, list) else issues
    prs_sample = prs[:3] if isinstance(prs, list) else prs
    commits_sample = commits[:3] if isinstance(commits, list) else commits
    contributors_sample = contributors[:3] if isinstance(contributors, list) else contributors

    def safe_llm_summary(title, items):
        try:
            return llm.generate_report(
                f"请用一句话总结以下GitHub仓库的{title}（只需提炼主要特征/趋势/亮点）：\n{items}", ""
            )
        except Exception as e:
            return f"{title}总结失败: {e}"

    issues_summary = safe_llm_summary("issues", issues_sample)
    prs_summary = safe_llm_summary("PRs", prs_sample)
    commits_summary = safe_llm_summary("commits", commits_sample)
    contributors_summary = safe_llm_summary("贡献者", contributors_sample)

    final_prompt = f"""
请根据以下各部分的简要总结，生成一个结构紧凑、信息量大的智能报告，分为如下小节：
1. 活跃趋势分析
2. 主要贡献者及分工
3. 高频/典型问题
4. PR 合并率与特征
5. 代码提交方向
6. 异常与亮点

issues总结: {issues_summary}
PRs总结: {prs_summary}
commits总结: {commits_summary}
贡献者总结: {contributors_summary}
"""
    try:
        llm_summary = llm.generate_report("你是一个专业的GitHub仓库分析师，请用中文总结以下内容：" + final_prompt, "")
    except Exception as e:
        llm_summary = f"LLM 总结失败: {e}"
    return jsonify({
        'issues': issues,
        'prs': prs,
        'commits': commits,
        'contributors': contributors,
        'commits_url': f'{repo_url.rstrip(".git")}/commits',
        'llm_summary': llm_summary
    })

@app.route('/api/hn_statistics', methods=['GET'])
def hn_statistics():
    # 实例化客户端
    hn_client = HackerNewsClient()
    news = hn_client.fetch_top_stories()
    # 只保留有详细字段的新闻
    news = [n for n in news if n.get('title') and n.get('score') is not None and n.get('by') and n.get('descendants') is not None]
    news_sample = news[:3] if isinstance(news, list) else news
    # 活跃用户（取前3条新闻的作者）
    users_sample = []
    for n in news_sample:
        if 'by' in n:
            users_sample.append({'id': n['by']})
    if not users_sample:
        users_sample = [{'id': '未知'}]
    # 组装精简内容，防止token超限
    def news_brief(news_list):
        return [f"标题:{n['title']} 分数:{n['score']} 作者:{n['by']} 评论数:{n['descendants']}" for n in news_list]
    news_brief_list = news_brief(news_sample)
    users_brief_list = [u['id'] for u in users_sample]
    # 1. 热门话题趋势
    try:
        llm_hot_topics = llm.generate_report(
            f"你是Hacker News分析师，请用中文详细总结以下新闻的热门话题趋势，内容丰富、结构紧凑：\n{news_brief_list}", ""
        )
    except Exception as e:
        llm_hot_topics = f"热门话题趋势总结失败: {e}"
    # 2. 主要活跃用户及其特征
    try:
        llm_active_users = llm.generate_report(
            f"你是Hacker News分析师，请用中文详细总结以下活跃用户的主要特征和分工，内容丰富、结构紧凑：\n{users_brief_list}", ""
        )
    except Exception as e:
        llm_active_users = f"主要活跃用户总结失败: {e}"
    # 3. 评论与讨论亮点
    try:
        llm_comments = llm.generate_report(
            f"你是Hacker News分析师，请用中文详细总结以下新闻的评论与讨论亮点，内容丰富、结构紧凑：\n{news_brief_list}", ""
        )
    except Exception as e:
        llm_comments = f"评论与讨论亮点总结失败: {e}"
    # 4. 异常与创新内容
    try:
        llm_innovations = llm.generate_report(
            f"你是Hacker News分析师，请用中文详细总结以下新闻和用户中的异常与创新内容，内容丰富、结构紧凑：\n新闻：{news_brief_list}\n用户：{users_brief_list}", ""
        )
    except Exception as e:
        llm_innovations = f"异常与创新内容总结失败: {e}"
    return jsonify({
        'news': news_sample,
        'users': users_sample,
        'llm_hot_topics': llm_hot_topics,
        'llm_active_users': llm_active_users,
        'llm_comments': llm_comments,
        'llm_innovations': llm_innovations
    })

if __name__ == '__main__':
    print("Flask server is starting on http://localhost:8888 ...")
    app.run(debug=True, port=8888)