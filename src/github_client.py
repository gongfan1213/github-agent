"""
GitHub API 客户端模块
功能：负责与 GitHub API 进行交互
- 使用 GitHub Token 进行身份验证
- 获取订阅仓库的更新信息
- 处理 API 请求和响应
- 管理 API 请求头信息
"""

import requests

class GitHubClient:
    def __init__(self, token):
        self.token = token
    
    def fetch_updates(self, subscriptions):
        headers = {
            'Authorization': f'token {self.token}'
        }
        updates = {}
        for repo in subscriptions:
            response = requests.get(f'https://api.github.com/repos/{repo}/events', headers=headers)
            if response.status_code == 200:
                updates[repo] = response.json()
        return updates
