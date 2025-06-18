"""
配置管理模块
功能：负责加载和管理应用程序的配置信息
- 从 config.json 文件读取配置
- 管理 GitHub Token
- 管理通知设置
- 管理订阅文件路径
- 管理更新间隔时间
"""

import json

class Config:
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.github_token = config.get('github_token')
            self.notification_settings = config.get('notification_settings')
            self.subscriptions_file = config.get('subscriptions_file')
            self.update_interval = config.get('update_interval', 24 * 60 * 60)  # Default to 24 hours
