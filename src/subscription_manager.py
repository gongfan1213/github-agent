"""
订阅管理器模块
功能：负责管理 GitHub 仓库的订阅信息
- 读取订阅配置文件
- 管理订阅的仓库列表
- 处理订阅数据的持久化
- 提供订阅信息的访问接口
"""

import json
<<<<<<< HEAD
=======
import os
>>>>>>> 8c45dafbfc62b94f62cc53c7c041c34e2d2d0173

class SubscriptionManager:
    def __init__(self, subscriptions_file):
        self.subscriptions_file = subscriptions_file
<<<<<<< HEAD
        self.subscriptions = self.load_subscriptions()
    
    def load_subscriptions(self):
        with open(self.subscriptions_file, 'r') as f:
            return json.load(f)
    
    def save_subscriptions(self):
        with open(self.subscriptions_file, 'w') as f:
            json.dump(self.subscriptions, f, indent=4)
    
    def get_subscriptions(self):
        return self.subscriptions
    
    def add_subscription(self, repo):
        if repo not in self.subscriptions:
            self.subscriptions.append(repo)
            self.save_subscriptions()
    
    def remove_subscription(self, repo):
        if repo in self.subscriptions:
            self.subscriptions.remove(repo)
            self.save_subscriptions()

=======
    
    def get_subscriptions(self):
        try:
            if not os.path.exists(self.subscriptions_file):
                # 如果文件不存在，创建默认配置
                default_config = {"repositories": []}
                with open(self.subscriptions_file, 'w') as f:
                    json.dump(default_config, f, indent=4)
                return default_config["repositories"]
            
            with open(self.subscriptions_file, 'r') as f:
                config = json.load(f)
                return config.get("repositories", [])
        except json.JSONDecodeError:
            print(f"错误：{self.subscriptions_file} 文件格式不正确")
            return []
        except Exception as e:
            print(f"读取订阅文件时发生错误：{str(e)}")
            return []
>>>>>>> 8c45dafbfc62b94f62cc53c7c041c34e2d2d0173
