import sys
import os
from datetime import datetime, timedelta
import requests
import json
import base64

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.report_generator import ReportGenerator

def fetch_github_events(token, repo):
    """获取仓库的最近事件"""
    try:
        # 确保 token 是有效的字符串
        if not isinstance(token, str):
            print(f"警告: {repo} 的 token 格式无效")
            return []
            
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        url = f'https://api.github.com/repos/{repo}/events'
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"警告: 获取 {repo} 的事件失败，状态码: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"错误: 获取 {repo} 的事件时发生错误: {str(e)}")
        return []

def main():
    try:
        # 读取配置文件
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 读取订阅列表
        with open('subscriptions.json', 'r', encoding='utf-8') as f:
            subscriptions = json.load(f)
        
        # 创建报告生成器实例
        report_generator = ReportGenerator()
        
        # 获取所有仓库的更新
        updates = {}
        for repo in subscriptions['repositories']:
            print(f"正在获取 {repo} 的更新...")
            events = fetch_github_events(config['github_token'], repo)
            if events:
                updates[repo] = events
                print(f"成功获取 {repo} 的 {len(events)} 个事件")
            else:
                print(f"未获取到 {repo} 的更新")
        
        if not updates:
            print("警告: 没有获取到任何仓库的更新")
            return
        
        # 生成报告
        report = report_generator.generate_report(updates)
        
        # 创建reports目录（如果不存在）
        reports_dir = "reports"
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        
        # 生成报告文件名（使用当前时间）
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"report_{timestamp}.txt"
        report_path = os.path.join(reports_dir, report_filename)
        
        # 保存报告到文件
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)
        
        # 打印报告
        print("\n" + "="*50)
        print("GitHub AI 仓库更新报告")
        print("="*50 + "\n")
        print(report)
        print("\n" + "="*50)
        print(f"\n报告已保存到：{report_path}")
        
    except FileNotFoundError as e:
        print(f"错误: 找不到配置文件: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"错误: 配置文件格式无效: {str(e)}")
    except Exception as e:
        print(f"错误: 程序执行过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main() 