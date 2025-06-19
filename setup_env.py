#!/usr/bin/env python3
"""
环境变量设置脚本
帮助用户安全地配置敏感信息
"""

import os
import json
from pathlib import Path

def create_env_file():
    """创建 .env 文件模板"""
    env_content = """# GitHub Hacker News 智能体环境变量配置
# 请将以下占位符替换为你的实际值

# GitHub 配置
GITHUB_TOKEN=your_github_token_here

# OpenAI 配置
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=your_openai_base_url_here

# Ollama 配置（可选）
OLLAMA_API_URL=http://localhost:11434/api/chat

# 通知配置（可选）
EMAIL_ADDRESS=your_email_here
SLACK_WEBHOOK_URL=your_slack_webhook_url_here
"""
    
    env_file = Path('.env')
    if env_file.exists():
        print("⚠️  .env 文件已存在，跳过创建")
        return
    
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ 已创建 .env 文件模板")
    print("📝 请编辑 .env 文件，填入你的实际配置值")

def create_config_from_env():
    """从环境变量创建 config.json"""
    config = {
        "github_token": os.getenv('GITHUB_TOKEN', 'YOUR_GITHUB_TOKEN_HERE'),
        "llm_model_type": "openai",
        "openai_api_key": os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY_HERE'),
        "openai_base_url": os.getenv('OPENAI_BASE_URL', 'YOUR_OPENAI_BASE_URL_HERE'),
        "notification_settings": {
            "email": os.getenv('EMAIL_ADDRESS', 'YOUR_EMAIL_HERE'),
            "slack_webhook_url": os.getenv('SLACK_WEBHOOK_URL', 'YOUR_SLACK_WEBHOOK_URL_HERE')
        },
        "github": {
            "subscriptions_file": "subscriptions.json"
        },
        "llm": {
            "model_type": "openai",
            "openai_model_name": "gpt-4",
            "ollama_model_name": "llama3",
            "ollama_api_url": os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api/chat')
        },
        "update_interval": 86400
    }
    
    config_file = Path('config.json')
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    print("✅ 已从环境变量创建 config.json")

def check_security():
    """检查安全配置"""
    print("\n🔒 安全检查:")
    
    # 检查 .env 文件是否在 .gitignore 中
    gitignore_file = Path('.gitignore')
    if gitignore_file.exists():
        with open(gitignore_file, 'r', encoding='utf-8') as f:
            gitignore_content = f.read()
        
        if '.env' in gitignore_content:
            print("✅ .env 文件已在 .gitignore 中")
        else:
            print("⚠️  .env 文件未在 .gitignore 中，建议添加")
    
    # 检查 config.json 是否在 .gitignore 中
    if gitignore_file.exists():
        with open(gitignore_file, 'r', encoding='utf-8') as f:
            gitignore_content = f.read()
        
        if 'config.json' in gitignore_content:
            print("✅ config.json 文件已在 .gitignore 中")
        else:
            print("⚠️  config.json 文件未在 .gitignore 中，建议添加")

def main():
    print("🚀 GitHub Hacker News 智能体环境配置工具")
    print("=" * 50)
    
    while True:
        print("\n请选择操作:")
        print("1. 创建 .env 文件模板")
        print("2. 从环境变量创建 config.json")
        print("3. 安全检查")
        print("4. 退出")
        
        choice = input("\n请输入选项 (1-4): ").strip()
        
        if choice == '1':
            create_env_file()
        elif choice == '2':
            create_config_from_env()
        elif choice == '3':
            check_security()
        elif choice == '4':
            print("👋 再见！")
            break
        else:
            print("❌ 无效选项，请重新选择")

if __name__ == '__main__':
    main() 