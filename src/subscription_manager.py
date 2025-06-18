"""
订阅管理器模块
功能：负责管理 GitHub 仓库的订阅信息
- 读取订阅配置文件
- 管理订阅的仓库列表
- 处理订阅数据的持久化
- 提供订阅信息的访问接口
"""

import json
import os

class SubscriptionManager:
    def __init__(self, subscriptions_file):
        self.subscriptions_file = subscriptions_file
    
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
