"""
报告生成器模块
功能：负责生成仓库更新报告
- 处理仓库更新数据
- 格式化报告内容
- 生成可读性强的报告文本
- 支持多种报告格式
"""

from datetime import datetime

class ReportGenerator:
    def __init__(self):
        """初始化报告生成器"""
        pass

    def generate_report(self, updates):
        """
        生成仓库更新报告
        
        参数:
            updates (dict): 仓库更新数据
            
        返回:
            str: 格式化的报告文本
        """
        if not updates:
            return "没有新的更新"
            
        report = []
        report.append("=" * 50)
        report.append("GitHub 仓库更新报告")
        report.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 50 + "\n")
        
        for repo, events in updates.items():
            report.append(repo)
            report.append("-" * 50)
            
            for event in events:
                event_type = event.get("type", "未知事件")
                created_at = event.get("created_at", "")
                if created_at:
                    created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                    created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
                
                report.append(f"更新时间：{created_at}")
                report.append(f"事件类型：{event_type}")
                
                # 处理不同类型的事件
                if event_type == "PushEvent":
                    commits = event.get("payload", {}).get("commits", [])
                    if commits:
                        report.append("提交信息：")
                        for commit in commits:
                            message = commit.get("message", "")
                            author = commit.get("author", {}).get("name", "未知作者")
                            report.append(f"    - {message} ({author})")
                
                elif event_type == "PullRequestEvent":
                    pr = event.get("payload", {}).get("pull_request", {})
                    if pr:
                        title = pr.get("title", "")
                        user = pr.get("user", {}).get("login", "未知用户")
                        report.append(f"PR标题：{title}")
                        report.append(f"提交者：{user}")
                
                elif event_type == "IssuesEvent":
                    issue = event.get("payload", {}).get("issue", {})
                    if issue:
                        title = issue.get("title", "")
                        user = issue.get("user", {}).get("login", "未知用户")
                        report.append(f"Issue标题：{title}")
                        report.append(f"提交者：{user}")
                
                else:
                    report.append("未知事件类型")
                
                report.append("")  # 添加空行分隔不同事件
            
            report.append("")  # 添加空行分隔不同仓库
        
        return "\n".join(report)
