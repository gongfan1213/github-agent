from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from config import Config
from llm import LLM
from report_generator import ReportGenerator
from datetime import datetime, timedelta
import requests
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
    summary_prompt = f"""
请对以下 GitHub 仓库的近一个月数据进行简要总结，分为如下小节：
1. 活跃趋势分析
2. 主要贡献者及分工
3. 高频/典型问题
4. PR 合并率与特征
5. 代码提交方向
6. 异常与亮点
每一小节用简短小标题，内容紧凑。

issues:
{issues_sample}
prs:
{prs_sample}
commits:
{commits_sample}
contributors:
{contributors_sample}
"""
    # 用 LLM 生成总结
    try:
        llm_summary = llm.generate_report("你是一个专业的GitHub仓库分析师，请用中文总结以下内容：" + summary_prompt, "")
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

if __name__ == '__main__':
    print("Flask server is starting on http://localhost:8888 ...")
    app.run(debug=True, port=8888)