# GitHub Hacker News智能体
# v0.2

![image](https://github.com/user-attachments/assets/b785e2ee-e7c6-4d31-82a7-239bcc91266f)

![image](https://github.com/user-attachments/assets/6cfaebe5-897a-495e-8227-cf8bc068b412)


![image](https://github.com/user-attachments/assets/b3650038-ae3e-41b4-aff8-99dfdd3476cc)


这是一个用于监控 GitHub 仓库更新的工具，支持邮件和 Slack 通知。

## 功能特点

- 监控多个 GitHub 仓库的更新
- 支持邮件通知
- 支持 Slack 通知
- 可配置的更新检查间隔
- 自动生成更新报告

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/你的用户名/github-agent.git
cd github-agent
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置

1. 复制示例配置文件：
```bash
cp config.example.json config.json
```

2. 编辑 `config.json`：
- 设置你的 GitHub 令牌
- 配置通知设置（邮箱和/或 Slack webhook）
- 根据需要调整更新间隔

3. 编辑 `subscriptions.json`：
- 添加你想要监控的 GitHub 仓库

## 使用方法

运行主程序：
```bash
python src/main.py
```

## 注意事项

- 请确保 `config.json` 和 `subscriptions.json` 文件不会被提交到版本控制系统
- 定期更新 GitHub 令牌以确保安全
- 建议使用虚拟环境运行程序

## 许可证

MIT
