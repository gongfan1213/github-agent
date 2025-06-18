"""
主程序入口文件
功能：初始化并启动 GitHub Sentinel 的所有组件
- 加载配置
- 初始化 GitHub 客户端
- 设置通知系统
- 创建报告生成器
- 初始化订阅管理器
- 启动调度器
"""

from config import Config
from scheduler import Scheduler
from github_client import GitHubClient
from notifier import Notifier
from report_generator import ReportGenerator
from subscription_manager import SubscriptionManager

def main():
    config = Config()
    github_client = GitHubClient(config.github_token)
    notifier = Notifier(config.notification_settings)
    report_generator = ReportGenerator()
    subscription_manager = SubscriptionManager(config.subscriptions_file)
    
    scheduler = Scheduler(
        github_client=github_client,
        notifier=notifier,
        report_generator=report_generator,
        subscription_manager=subscription_manager,
        interval=config.update_interval
    )
    
    scheduler.start()

if __name__ == "__main__":
    main()
