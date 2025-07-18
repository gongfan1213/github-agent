# GitHub Sentinel v1.0.0 功能说明

## 核心功能

### 1. 配置管理
- 支持从 `config.json` 读取配置信息
- 管理 GitHub Token 认证
- 配置通知系统（邮件、Slack）
- 设置更新检查间隔时间
- 管理订阅文件路径

### 2. GitHub 仓库监控
- 支持多个仓库同时监控
- 通过 GitHub API 获取仓库更新
- 使用 Token 进行身份验证
- 获取仓库事件信息
- 支持自定义更新检查频率

### 3. 通知系统
- 支持多种通知方式
  - 邮件通知
  - Slack 通知
- 可配置通知内容格式
- 支持自定义通知设置

### 4. 报告生成
- 生成仓库更新报告
- 格式化报告内容
- 支持多种报告格式
- 包含详细的更新信息

### 5. 订阅管理
- 管理 GitHub 仓库订阅
- 支持订阅配置的持久化
- 提供订阅信息的访问接口
- 灵活的订阅管理机制

### 6. 调度系统
- 定时执行更新检查
- 自动触发通知
- 可配置执行间隔
- 支持后台运行

## 技术特点

1. **模块化设计**
   - 清晰的代码结构
   - 独立的组件设计
   - 易于扩展和维护

2. **配置灵活**
   - 支持外部配置文件
   - 可自定义各项参数
   - 易于调整和修改

3. **错误处理**
   - 完善的异常处理机制
   - 日志记录功能
   - 运行状态监控

4. **安全性**
   - 安全的 Token 管理
   - 配置信息保护
   - 安全的 API 调用

## 使用说明

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **配置设置**
   - 编辑 `config.json` 文件
   - 设置 GitHub Token
   - 配置通知方式
   - 设置更新间隔

3. **运行程序**
   ```bash
   python src/main.py
   ```

## 注意事项

1. 首次使用需要配置 GitHub Token
2. 确保网络连接正常
3. 正确设置通知配置
4. 定期检查日志信息

## 后续计划

1. 添加更多通知方式
2. 优化报告格式
3. 增加更多自定义选项
4. 提供 Web 界面
5. 添加更多监控指标 