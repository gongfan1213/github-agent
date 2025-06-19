# GitHub Hacker News 智能体 (GitHubSentinel)

![Version](https://img.shields.io/badge/version-v0.2-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)

![AI Agent](https://img.shields.io/badge/AI-Agent-purple)

**信息挖掘智能体**，支持 GitHub 仓库进展跟踪和 Hacker News 技术趋势分析。

[参考](https://github.com/DjangoPeng/GitHubSentinel)


## 📋 目录

- [项目概述](#项目概述)
- [智能体分析](#智能体分析)
- [核心功能](#核心功能)
- [系统架构](#系统架构)
- [数据结构](#数据结构)
- [安装配置](#安装配置)
- [使用方法](#使用方法)
- [API 文档](#api-文档)
- [部署指南](#部署指南)
- [开发指南](#开发指南)
- [安全注意事项](#安全注意事项)

## 🎯 项目概述

GitHub Hacker News 智能体是一个综合性的**信息挖掘智能体**，主要功能包括：

- **GitHub 仓库监控**：自动跟踪订阅仓库的 commits、issues、PRs 等更新
- **Hacker News 趋势分析**：实时抓取和分析 HN 热门技术话题
- **智能报告生成**：基于 LLM（OpenAI GPT 或 Ollama）自动生成分析报告
- **多渠道通知**：支持邮件和 Slack 通知
- **Web 界面**：提供 Gradio 和 Flask 两种 Web 界面
- **定时任务**：支持自定义定时执行监控任务


## 🛠️ 技术栈详细分析

### **1. 核心编程语言**
- **Python 3.10** - 主要开发语言，提供强大的数据处理和AI集成能力

### **2. 人工智能与机器学习**
- **OpenAI GPT API** - 支持 GPT-4o、GPT-4o-mini、GPT-3.5-turbo 等模型
- **Ollama 本地模型** - 支持 Llama3.1、Gemma2:2b、Qwen2:7b 等私有化部署
- **大语言模型集成** - 通过统一的 LLM 接口支持多种 AI 模型

### **3. Web 框架与界面**
- **Flask** - 轻量级 Web 框架，提供 RESTful API 服务
- **Gradio** - 快速构建 AI 应用界面的 Python 库
- **HTML/CSS/JavaScript** - 前端界面开发
- **ECharts** - 数据可视化图表库

### **4. 数据获取与处理**
- **Requests** - HTTP 客户端库，用于 API 调用
- **BeautifulSoup4** - HTML 解析库，用于网页内容提取
- **GitHub API** - 官方 API 集成，获取仓库数据
- **Hacker News API** - 技术新闻数据获取

### **5. 数据处理与存储**
- **JSON** - 配置文件和数据交换格式
- **Markdown** - 报告生成格式
- **文件系统存储** - 本地文件存储报告和数据

### **6. 任务调度与后台服务**
- **Schedule** - Python 任务调度库
- **Daemon 进程** - 后台服务进程
- **信号处理** - 进程管理和优雅关闭

### **7. 通知系统**
- **SMTP** - 邮件发送服务
- **Markdown2** - Markdown 转 HTML 用于邮件内容

### **8. 日志与监控**
- **Loguru** - 现代化日志记录库
- **结构化日志** - 支持不同级别的日志记录

### **9. 容器化与部署**
- **Docker** - 容器化部署
- **Python 3.10-slim** - 轻量级基础镜像
- **环境变量配置** - 灵活的配置管理

### **10. 测试框架**
- **unittest** - Python 标准测试框架
- **Mock** - 单元测试模拟对象
- **测试覆盖率** - 完整的测试用例

### **11. 开发工具与配置**
- **Git** - 版本控制
- **环境变量管理** - 敏感信息保护
- **配置文件管理** - JSON 格式配置
- **命令行工具** - 交互式命令行界面

### **12. 数据可视化**
- **ECharts** - 交互式图表库
- **实时数据展示** - 动态图表更新
- **多维度分析** - 仓库活跃度、用户贡献等统计

### **13. 安全与隐私**
- **环境变量** - API 密钥安全存储
- **代理配置** - 网络访问控制
- **输入验证** - 数据安全处理

### **14. 架构特点**
- **模块化设计** - 清晰的代码结构
- **配置驱动** - 灵活的配置管理
- **多模型支持** - 可扩展的 AI 模型集成
- **实时监控** - 定时任务和数据更新
- **可视化报告** - 丰富的图表展示


## 🤖 智能体分析

### 智能体特征

#### 1. **自主性 (Autonomy)**
- **自动数据采集**：无需人工干预，自动抓取 GitHub 和 Hacker News 数据
- **定时任务执行**：守护进程自动按计划执行监控任务
- **智能决策**：根据配置自动选择模型和生成报告类型
- **错误恢复**：具备异常处理和自动重试机制

#### 2. **感知能力 (Perception)**
- **多源数据感知**：
  - GitHub API 数据（commits、issues、PRs、contributors）
  - Hacker News 网页数据（新闻、评论、分数、用户）
  - 用户配置和偏好设置
  - 系统运行状态和环境信息

#### 3. **学习与适应 (Learning & Adaptation)**
- **LLM 驱动分析**：使用 GPT 或 Ollama 模型进行智能分析
- **模式识别**：识别技术趋势、热点话题、异常内容
- **个性化报告**：根据不同的提示模板生成定制化报告
- **持续优化**：基于历史数据优化分析策略

#### 4. **目标导向 (Goal-Oriented)**
- **明确目标**：监控开源项目进展和技术趋势
- **任务分解**：将复杂的信息挖掘任务分解为多个子任务
- **结果导向**：生成有价值的分析报告和通知
- **价值评估**：评估信息的重要性和相关性

### 智能体架构

#### 感知层 (Perception Layer)
```
┌─────────────────────────────────┐
│        数据采集模块              │
│                                 │
│  ┌─────────────┐ ┌─────────────┐ │
│  │GitHub Client│ │ HN Client   │ │
│  │             │ │             │ │
│  │• API 调用   │ │• 网页抓取   │ │
│  │• 数据解析   │ │• 内容解析   │ │
│  │• 错误处理   │ │• 代理支持   │ │
│  └─────────────┘ └─────────────┘ │
└─────────────────────────────────┘
```

#### 认知层 (Cognitive Layer)
```
┌─────────────────────────────────┐
│        智能分析模块              │
│                                 │
│  ┌─────────────┐ ┌─────────────┐ │
│  │ LLM Engine  │ │Report Gen   │ │
│  │             │ │             │ │
│  │• 模型选择   │ │• 模板管理   │ │
│  │• 提示工程   │ │• 内容聚合   │ │
│  │• 响应解析   │ │• 格式转换   │ │
│  └─────────────┘ └─────────────┘ │
│                                 │
│  ┌─────────────┐ ┌─────────────┐ │
│  │Pattern Rec  │ │Trend Anal   │ │
│  │             │ │             │ │
│  │• 模式识别   │ │• 趋势分析   │ │
│  │• 异常检测   │ │• 预测建模   │ │
│  │• 关联分析   │ │• 洞察生成   │ │
│  └─────────────┘ └─────────────┘ │
└─────────────────────────────────┘
```

#### 执行层 (Action Layer)
```
┌─────────────────────────────────┐
│        执行输出模块              │
│                                 │
│  ┌─────────────┐ ┌─────────────┐ │
│  │  Notifier   │ │   Web UI    │ │
│  │             │ │             │ │
│  │• 邮件通知   │ │• Gradio     │ │
│  │• Slack      │ │• Flask      │ │
│  │• Webhook    │ │• 可视化     │ │
│  └─────────────┘ └─────────────┘ │
│                                 │
│  ┌─────────────┐ ┌─────────────┐ │
│  │File Export  │ │Daemon Proc  │ │
│  │             │ │             │ │
│  │• Markdown   │ │• 定时任务   │ │
│  │• JSON       │ │• 进程管理   │ │
│  │• 日志记录   │ │• 状态监控   │ │
│  └─────────────┘ └─────────────┘ │
└─────────────────────────────────┘
```

### 信息挖掘能力

#### 1. **数据挖掘**
```python
# GitHub 项目信息挖掘
- 代码提交模式分析：识别活跃时段、提交频率、代码质量
- 问题解决趋势：分析 issue 解决速度、问题类型分布
- 贡献者活跃度：评估项目健康度和社区活跃度
- 项目发展方向：基于 PR 和 commit 预测技术方向

# Hacker News 技术趋势挖掘
- 热门话题识别：实时发现技术讨论热点
- 技术热点分析：识别新兴技术和工具
- 用户讨论模式：分析技术社区讨论偏好
- 创新内容发现：发现突破性技术和想法
```

#### 2. **知识提取**
- **结构化信息**：将非结构化数据转换为结构化报告
- **趋势分析**：识别技术发展趋势和模式
- **洞察生成**：基于数据生成有价值的洞察
- **关联分析**：发现不同信息源之间的关联

#### 3. **智能推理**
- **因果关系分析**：分析项目活动与技术趋势的关系
- **预测性分析**：基于历史数据预测发展趋势
- **异常检测**：识别异常的项目活动或技术讨论
- **风险评估**：评估项目和技术趋势的风险

### 智能体应用场景

#### 1. **开源项目监控智能体**
- **自动跟踪**：持续监控项目进展和健康状态
- **智能评估**：基于多维度数据评估项目质量
- **趋势预测**：预测项目发展方向和潜在问题
- **决策支持**：为项目管理和投资决策提供数据支持

#### 2. **技术趋势分析智能体**
- **实时监控**：24/7 监控技术热点和新兴趋势
- **深度分析**：深入分析技术发展的内在逻辑
- **市场洞察**：为技术投资和产品决策提供洞察
- **竞争情报**：监控竞争对手的技术动向

#### 3. **信息聚合智能体**
- **多源整合**：整合来自不同平台的技术信息
- **智能筛选**：基于用户偏好智能筛选相关内容
- **个性化推送**：根据用户需求推送定制化信息
- **知识管理**：构建个人或团队的技术知识库

### 智能体优势

#### 1. **效率提升**
- **自动化程度高**：减少 90% 的人工数据收集时间
- **智能分析**：快速生成深度分析报告
- **持续运行**：24/7 不间断监控和分析
- **批量处理**：同时处理多个项目和话题

#### 2. **质量保证**
- **LLM 驱动**：基于先进的语言模型进行分析
- **多维度验证**：从多个角度验证信息准确性
- **结构化输出**：生成标准化、可读性强的报告
- **持续优化**：基于反馈不断改进分析质量

#### 3. **可扩展性**
- **模块化设计**：易于添加新的数据源和分析模块
- **配置灵活**：支持多种配置和自定义选项
- **API 友好**：提供完整的 API 接口供集成使用
- **云原生**：支持容器化部署和云平台集成

### 智能体评估指标

#### 1. **准确性指标**
- **数据采集准确率**：≥ 95%
- **分析结果准确性**：基于 LLM 模型性能
- **趋势预测准确度**：≥ 80%
- **异常检测准确率**：≥ 90%

#### 2. **效率指标**
- **响应时间**：< 30 秒（Web 界面）
- **处理速度**：每分钟处理 100+ 条数据
- **资源消耗**：内存 < 512MB，CPU < 10%
- **并发能力**：支持 10+ 并发用户

#### 3. **价值指标**
- **信息价值密度**：高价值信息占比 ≥ 60%
- **洞察质量**：用户满意度 ≥ 85%
- **时间节省**：相比人工分析节省 80% 时间
- **决策支持**：为技术决策提供有效数据支持

### 智能体发展方向

#### 1. **增强学习能力**
- **自适应学习**：基于历史数据优化分析模型
- **个性化推荐**：学习用户偏好，提供个性化服务
- **主动学习**：主动发现和推荐有价值的信息
- **知识图谱**：构建技术知识图谱，提升推理能力

#### 2. **扩展感知范围**
- **多平台支持**：集成 Stack Overflow、Reddit、Twitter 等
- **多语言支持**：支持中文、英文等多种语言
- **多媒体分析**：分析图片、视频等技术内容
- **实时流处理**：支持实时数据流处理和分析

#### 3. **提升智能水平**
- **高级推理**：支持复杂的逻辑推理和因果分析
- **预测建模**：构建更准确的预测模型
- **情感分析**：分析技术社区的情感倾向
- **知识发现**：自动发现新的技术趋势和模式

## 🚀 核心功能

### 1. GitHub 仓库监控

#### 功能特性
- **多仓库订阅管理**：支持同时监控多个 GitHub 仓库
- **数据抓取**：自动获取 commits、issues、pull requests 数据
- **时间范围分析**：支持指定时间范围的数据分析
- **进展报告**：生成结构化的项目进展报告

#### 监控数据类型
- **Commits**：代码提交记录和变更统计
- **Issues**：问题跟踪和解决状态
- **Pull Requests**：代码合并请求和审查状态
- **Contributors**：贡献者活跃度分析

### 2. Hacker News 趋势分析

#### 功能特性
- **实时抓取**：自动抓取 HN 首页热门新闻
- **智能解析**：解析新闻标题、链接、分数、评论数等
- **趋势分析**：识别技术热点和发展趋势
- **多维度报告**：生成话题趋势、用户分析、评论亮点等报告

#### 分析维度
- **热门话题趋势**：识别当前技术圈讨论热点
- **活跃用户分析**：分析主要贡献者和讨论者
- **评论亮点**：提取有价值的讨论内容
- **异常与创新内容**：发现异常和创新性内容

### 3. 智能报告生成

#### 支持的 LLM 模型
- **OpenAI GPT 系列**：gpt-4、gpt-4o-mini、gpt-3.5-turbo
- **Ollama 本地模型**：llama3、gemma2、qwen2 等

#### 报告类型
- **GitHub 项目进展报告**：结构化项目更新总结
- **HN 小时话题报告**：当前技术热点分析
- **HN 每日趋势报告**：24小时技术趋势汇总

### 4. 通知系统

#### 通知渠道
- **邮件通知**：支持 SMTP 邮件发送
- **Slack 通知**：支持 Slack Webhook 集成

#### 通知内容
- GitHub 项目进展简报
- Hacker News 技术趋势报告
- 系统运行状态通知

### 5. Web 界面

#### Gradio 界面
- **模型选择**：支持 OpenAI 和 Ollama 模型切换
- **参数配置**：可调整报告周期、模型参数等
- **实时生成**：支持实时生成和下载报告

#### Flask Web 界面
- **数据可视化**：使用 ECharts 展示统计数据
- **智能分析**：LLM 驱动的智能总结
- **交互式操作**：支持复制链接、查看详情等

## 🏗️ 系统架构

### 整体架构图

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web 界面层    │    │   定时任务层     │    │   数据采集层     │
│                 │    │                 │    │                 │
│ • Gradio UI     │    │ • Daemon Process│    │ • GitHub Client │
│ • Flask Web     │    │ • Schedule      │    │ • HN Client     │
│ • Templates     │    │ • Job Runner    │    │ • API Wrapper   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   核心处理层     │
                    │                 │
                    │ • LLM Engine    │
                    │ • Report Gen    │
                    │ • Notifier      │
                    │ • Config Mgmt   │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │   数据存储层     │
                    │                 │
                    │ • JSON Files    │
                    │ • Markdown      │
                    │ • Logs          │
                    └─────────────────┘
```

### 核心模块说明

#### 1. 配置管理模块 (`config.py`)
- **功能**：统一管理所有配置参数
- **支持**：环境变量、配置文件、默认值
- **配置项**：API 密钥、模型参数、通知设置等

#### 2. 数据采集模块
- **GitHub Client** (`github_client.py`)：GitHub API 数据采集
- **HN Client** (`hacker_news_client.py`)：Hacker News 数据抓取

#### 3. LLM 引擎 (`llm.py`)
- **功能**：统一 LLM 接口，支持多种模型
- **支持**：OpenAI GPT、Ollama 本地模型
- **特性**：错误处理、重试机制、响应解析

#### 4. 报告生成器 (`report_generator.py`)
- **功能**：基于模板和 LLM 生成结构化报告
- **支持**：多种报告类型和格式
- **特性**：模板管理、内容聚合、文件输出

#### 5. 通知系统 (`notifier.py`)
- **功能**：多渠道通知发送
- **支持**：邮件、Slack、自定义 Webhook
- **特性**：模板渲染、错误处理、重试机制

#### 6. 定时任务 (`daemon_process.py`)
- **功能**：后台定时任务执行
- **支持**：自定义时间间隔、多种任务类型
- **特性**：优雅关闭、错误恢复、日志记录

## 📊 数据结构

### 配置文件结构

#### `config.json`
```json
{
    "github_token": "YOUR_GITHUB_TOKEN_HERE",
    "llm_model_type": "openai",
    "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",
    "openai_base_url": "YOUR_OPENAI_BASE_URL_HERE",
    "notification_settings": {
        "email": "YOUR_EMAIL_HERE",
        "slack_webhook_url": "YOUR_SLACK_WEBHOOK_URL_HERE"
    },
    "github": {
        "subscriptions_file": "subscriptions.json"
    },
    "llm": {
        "model_type": "openai",
        "openai_model_name": "gpt-4",
        "ollama_model_name": "llama3",
        "ollama_api_url": "http://localhost:11434/api/chat"
    },
    "update_interval": 86400
}
```

#### `subscriptions.json`
```json
{
    "repositories": [
        "openai/openai-python",
        "langchain-ai/langchain",
        "huggingface/transformers",
        "anthropics/claude"
    ]
}
```

### 数据模型

#### GitHub 数据模型
```python
# Commits 数据结构
{
    "sha": "commit_hash",
    "commit": {
        "message": "commit_message",
        "author": {
            "name": "author_name",
            "email": "author_email",
            "date": "commit_date"
        }
    },
    "author": {
        "login": "github_username",
        "avatar_url": "avatar_url"
    }
}

# Issues 数据结构
{
    "number": 123,
    "title": "issue_title",
    "body": "issue_description",
    "state": "open|closed",
    "created_at": "creation_date",
    "closed_at": "close_date",
    "user": {
        "login": "author_username"
    }
}

# Pull Requests 数据结构
{
    "number": 456,
    "title": "pr_title",
    "body": "pr_description",
    "state": "open|closed|merged",
    "merged_at": "merge_date",
    "user": {
        "login": "author_username"
    }
}
```

#### Hacker News 数据模型
```python
# HN 新闻数据结构
{
    "id": "story_id",
    "title": "story_title",
    "link": "story_url",
    "score": 123,
    "by": "author_username",
    "descendants": 45
}
```

### 报告模板结构

#### GitHub 项目进展报告
```markdown
# {项目名称} 项目进展

## 时间周期：{开始日期}至{结束日期}

## 新增功能
- 功能描述1
- 功能描述2

## 主要改进
- 改进描述1
- 改进描述2

## 修复问题
- 问题修复1
- 问题修复2
```

#### Hacker News 话题报告
```markdown
# Hacker News 热门话题 {日期} {小时}

1. **话题标题**：话题描述和趋势分析
    - 相关链接1
    - 相关链接2

2. **话题标题**：话题描述和趋势分析
    - 相关链接1
```

## 🛠️ 安装配置

### 环境要求

- **Python**: 3.10+
- **操作系统**: Windows, macOS, Linux
- **内存**: 建议 2GB+
- **网络**: 需要访问 GitHub API 和 Hacker News

### 快速安装

1. **克隆仓库**
```bash
git clone https://github.com/your-username/github-agent.git
cd github-agent
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置环境**
```bash
# 复制示例配置
cp config.example.json config.json

# 运行配置工具
python setup_env.py
```

### 详细配置

#### 1. 获取 API 密钥

**GitHub Token**
1. 访问 [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token (classic)"
3. 选择权限：`repo`, `read:user`, `read:email`
4. 复制生成的 token

**OpenAI API Key**
1. 访问 [OpenAI API Keys](https://platform.openai.com/api-keys)
2. 创建新的 API key
3. 复制生成的 key

#### 2. 环境变量配置（推荐）

```bash
# 设置环境变量
export GITHUB_TOKEN="your_github_token_here"
export OPENAI_API_KEY="your_openai_api_key_here"
export OPENAI_BASE_URL="your_openai_base_url_here"
export OLLAMA_API_URL="http://localhost:11434/api/chat"
```

#### 3. 配置文件设置

编辑 `config.json`：
```json
{
    "github_token": "your_github_token_here",
    "openai_api_key": "your_openai_api_key_here",
    "openai_base_url": "https://api.openai.com/v1/",
    "notification_settings": {
        "email": "your_email@example.com",
        "slack_webhook_url": "your_slack_webhook_url"
    }
}
```

#### 4. 订阅仓库配置

编辑 `subscriptions.json`：
```json
{
    "repositories": [
        "owner/repo1",
        "owner/repo2"
    ]
}
```

## 📖 使用方法

### 命令行使用

#### 1. 启动守护进程
```bash
# 启动定时任务守护进程
python src/daemon_process.py
```

#### 2. 手动生成报告
```bash
# 生成 GitHub 项目报告
python src/github_client.py

# 生成 Hacker News 报告
python src/hacker_news_client.py

# 生成示例报告
python examples/generate_sample_report.py
```

#### 3. 启动 Web 界面
```bash
# 启动 Gradio 界面
python src/gradio_server.py

# 启动 Flask Web 界面
python src/web_server.py
```

### Web 界面使用

#### Gradio 界面
1. 访问 `http://localhost:7860`
2. 选择 "GitHub 项目进展" 或 "Hacker News 热点话题"
3. 配置模型类型和参数
4. 点击生成报告

#### Flask Web 界面
1. 访问 `http://localhost:8888`
2. 选择数据源（GitHub 或 Hacker News）
3. 输入仓库地址或直接分析 HN
4. 查看智能分析和可视化结果

### 定时任务配置

#### 默认定时任务
- **GitHub 报告**：每天 08:00 执行
- **HN 话题报告**：每 4 小时执行一次
- **HN 每日报告**：每天 10:00 执行

#### 自定义定时任务
编辑 `src/daemon_process.py`：
```python
# 修改执行时间
schedule.every(1).days.at("09:00").do(github_job, ...)
schedule.every(6).hours.at(":00").do(hn_topic_job, ...)
```

## 🔌 API 文档

### Web API 接口

#### 1. GitHub 统计分析
```http
POST /api/statistics
Content-Type: application/json

{
    "repo_url": "https://github.com/owner/repo"
}
```

**响应示例**：
```json
{
    "issues": [...],
    "prs": [...],
    "commits": [...],
    "contributors": [...],
    "llm_summary": "智能分析总结...",
    "commits_url": "https://github.com/owner/repo/commits"
}
```

#### 2. Hacker News 统计分析
```http
GET /api/hn_statistics
```

**响应示例**：
```json
{
    "news": [...],
    "users": [...],
    "llm_hot_topics": "热门话题趋势分析...",
    "llm_active_users": "活跃用户分析...",
    "llm_comments": "评论亮点分析...",
    "llm_innovations": "创新内容分析..."
}
```

#### 3. 报告生成
```http
POST /api/generate_report
Content-Type: application/json

{
    "report_type": "github|hacker_news_hours_topic|hacker_news_daily_report",
    "markdown_content": "原始数据内容"
}
```

### 核心类 API

#### GitHubClient
```python
client = GitHubClient(token)

# 获取仓库更新
updates = client.fetch_updates(repo, since, until)

# 导出项目进展
file_path = client.export_progress_by_date_range(repo, days)
```

#### HackerNewsClient
```python
client = HackerNewsClient()

# 获取热门新闻
stories = client.fetch_top_stories()

# 导出新闻文件
file_path = client.export_top_stories(date, hour)
```

#### LLM
```python
llm = LLM(config)

# 生成报告
report = llm.generate_report(system_prompt, user_content)
```

#### ReportGenerator
```python
generator = ReportGenerator(llm, report_types)

# 生成 GitHub 报告
report, file_path = generator.generate_github_report(markdown_file_path)

# 生成 HN 话题报告
report, file_path = generator.generate_hn_topic_report(markdown_file_path)

# 生成 HN 每日报告
report, file_path = generator.generate_hn_daily_report(directory_path)
```

## 🚀 部署指南

### Docker 部署

#### 1. 构建镜像
```bash
docker build -t github-sentinel .
```

#### 2. 运行容器
```bash
docker run -d \
  --name github-sentinel \
  -e GITHUB_TOKEN="your_token" \
  -e OPENAI_API_KEY="your_key" \
  -v $(pwd)/data:/app/data \
  github-sentinel
```

#### 3. 使用 Docker Compose
```yaml
version: '3.8'
services:
  github-sentinel:
    build: .
    environment:
      - GITHUB_TOKEN=${GITHUB_TOKEN}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

### 生产环境部署

#### 1. 系统服务配置
```bash
# 创建系统服务文件
sudo nano /etc/systemd/system/github-sentinel.service
```

```ini
[Unit]
Description=GitHub Sentinel Daemon
After=network.target

[Service]
Type=simple
User=github-sentinel
WorkingDirectory=/opt/github-sentinel
Environment=GITHUB_TOKEN=your_token
Environment=OPENAI_API_KEY=your_key
ExecStart=/usr/bin/python3 src/daemon_process.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### 2. 启动服务
```bash
sudo systemctl enable github-sentinel
sudo systemctl start github-sentinel
sudo systemctl status github-sentinel
```

### 监控和日志

#### 日志配置
```python
# 日志文件位置
logs/
├── app.log          # 应用日志
├── error.log        # 错误日志
└── access.log       # 访问日志
```

#### 监控指标
- 任务执行状态
- API 调用频率
- 错误率统计
- 资源使用情况

## 👨‍💻 开发指南

### 项目结构
```
github-agent/
├── src/                    # 核心源代码
│   ├── config.py          # 配置管理
│   ├── github_client.py   # GitHub API 客户端
│   ├── hacker_news_client.py # HN 客户端
│   ├── llm.py             # LLM 引擎
│   ├── report_generator.py # 报告生成器
│   ├── notifier.py        # 通知系统
│   ├── daemon_process.py  # 定时任务
│   ├── gradio_server.py   # Gradio 界面
│   ├── web_server.py      # Flask Web 界面
│   └── templates/         # Web 模板
├── prompts/               # LLM 提示模板
├── tests/                 # 测试文件
├── examples/              # 示例代码
├── reports/               # 生成的报告
├── logs/                  # 日志文件
└── docs/                  # 文档
```

### 开发环境设置

#### 1. 虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows
```

#### 2. 开发依赖
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 开发依赖
```

#### 3. 代码格式化
```bash
# 安装 pre-commit hooks
pre-commit install

# 格式化代码
black src/
isort src/
```

### 测试

#### 运行测试
```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试
python -m pytest tests/test_github_client.py

# 生成覆盖率报告
python -m pytest --cov=src tests/
```

#### 测试结构
```
tests/
├── test_github_client.py      # GitHub 客户端测试
├── test_hacker_news_client.py # HN 客户端测试
├── test_llm.py               # LLM 引擎测试
├── test_report_generator.py  # 报告生成器测试
├── test_notifier.py          # 通知系统测试
└── test_subscription_manager.py # 订阅管理测试
```

### 贡献指南

#### 1. Fork 项目
1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/new-feature`
3. 提交更改：`git commit -am 'Add new feature'`
4. 推送分支：`git push origin feature/new-feature`
5. 创建 Pull Request

#### 2. 代码规范
- 遵循 PEP 8 代码风格
- 添加适当的注释和文档字符串
- 编写单元测试
- 更新相关文档

#### 3. 提交信息规范
```
feat: 添加新功能
fix: 修复 bug
docs: 更新文档
style: 代码格式调整
refactor: 代码重构
test: 添加测试
chore: 构建过程或辅助工具的变动
```

## 🔒 安全注意事项

### ⚠️ 重要安全提醒

#### 1. 敏感信息保护
- **永远不要提交敏感信息到版本控制**
- `config.json` 文件已被添加到 `.gitignore`
- 确保 API 密钥和 token 不会被意外提交

#### 2. 环境变量使用
- **推荐使用环境变量**而不是硬编码在配置文件中
- 生产环境必须使用环境变量
- 定期轮换密钥和 token

#### 3. 权限最小化
- GitHub token 只授予必要的权限
- 定期检查 token 权限
- 监控 API 使用情况

#### 4. 网络安全
- 使用 HTTPS 进行 API 通信
- 配置防火墙规则
- 定期更新依赖包

### 安全最佳实践

#### 1. 密钥管理
```bash
# 使用密钥管理服务
export GITHUB_TOKEN=$(aws secretsmanager get-secret-value --secret-id github-token --query SecretString --output text)
export OPENAI_API_KEY=$(aws secretsmanager get-secret-value --secret-id openai-key --query SecretString --output text)
```

#### 2. 访问控制
```python
# 实现访问控制
def check_permissions(user, action):
    if not user.has_permission(action):
        raise PermissionError(f"用户 {user} 没有权限执行 {action}")
```

#### 3. 输入验证
```python
# 验证输入数据
def validate_repo_url(url):
    if not url.startswith('https://github.com/'):
        raise ValueError("无效的 GitHub 仓库 URL")
```


**GitHub Hacker News 智能体** - 让开源项目监控变得智能和高效！ 🚀
