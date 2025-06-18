# Slack 通知配置指南

## 概述
本文档详细说明了如何配置 GitHub Sentinel 的 Slack 通知功能。通过配置 Slack Webhook，您可以将 GitHub 仓库的更新通知直接发送到指定的 Slack 频道。

## 配置步骤

### 1. 创建 Slack 应用
1. 访问 [Slack API 网站](https://api.slack.com/apps)
2. 点击 "Create New App"
3. 选择 "From scratch"
4. 输入应用名称并选择工作区

### 2. 设置 Webhook
1. 在应用设置页面，选择 "Incoming Webhooks"
2. 开启 "Activate Incoming Webhooks"
3. 点击 "Add New Webhook to Workspace"
4. 选择要发送通知的频道
5. 复制生成的 Webhook URL

### 3. 配置 config.json
将复制的 Webhook URL 替换到 `config.json` 中的 `"slack_webhook_url"` 字段：
```json
{
    "notification_settings": {
        "slack_webhook_url": "你的_slack_webhook_地址"
    }
}
```

## 注意事项
1. Webhook URL 是敏感信息，请勿分享给他人
2. 如果不使用 Slack 通知功能，可以：
   - 删除 `"slack_webhook_url"` 这一行
   - 或者保持原样，程序会忽略这个设置
3. 确保选择的 Slack 频道有适当的权限设置

## 故障排除
如果通知没有正常发送，请检查：
1. Webhook URL 是否正确
2. Slack 应用是否已正确安装到工作区
3. 选择的频道是否存在且有权限
4. 网络连接是否正常 


在 Slack 上找到 **传入 Webhook（Incoming Webhook）** 的步骤如下，适用于向 Slack 频道或私信（DM）发送自动消息或通知：

---

### **步骤 1：进入 Slack 管理后台**
1. 打开 Slack 网页版或桌面客户端，登录你的工作区（Workspace）。
2. 点击左上角工作区名称 → **「设置和管理」** → **「管理应用」**（Manage apps）。

   > **注意**：如果你不是工作区管理员，可能需要联系管理员开启权限。

---

### **步骤 2：搜索并添加「Incoming Webhook」**
1. 在 **「应用目录」**（App Directory）中搜索 **`Incoming Webhook`**。
2. 点击 **「添加」**（Add to Slack）。

---

### **步骤 3：配置 Webhook**
1. **选择发送频道**  
   - 选择 Webhook 消息要发送到的频道（如 `#general`）或用户私信（DM）。
   - 点击 **「允许」**（Allow）授权。

2. **获取 Webhook URL**  
   - 添加成功后，系统会生成一个唯一的 **Webhook URL**（格式如 `https://hooks.slack.com/services/TXXXXXX/BXXXXXX/XXXXXXXX`）。
   - **复制此 URL**，它将用于发送消息到 Slack。

   > **⚠️ 安全提示**：此 URL 是私密的，不要泄露给未授权人员。

---

### **步骤 4：测试 Webhook（可选）**
使用 `curl` 或代码发送测试消息：
```bash
curl -X POST -H 'Content-type: application/json' \
--data '{"text":"Hello from Webhook!"}' \
https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```
如果成功，你的 Slack 频道会收到消息。

---

### **步骤 5：自定义消息格式（高级）**
Webhook 支持富文本（Rich Text）、按钮、附件等。参考 Slack 的 [Message Formatting](https://api.slack.com/reference/messaging/payload) 文档，例如：
```json
{
  "text": "New Task Alert",
  "attachments": [
    {
      "title": "Task #123",
      "text": "Fix the login page bug",
      "color": "#36a64f",
      "actions": [
        {
          "type": "button",
          "text": "View Details",
          "url": "https://example.com/task/123"
        }
      ]
    }
  ]
}
```

---

### **常见问题**
1. **找不到「Incoming Webhook」？**  
   - 确保你有 **工作区管理员权限**，或联系管理员启用该应用。
   - 某些免费版 Slack 可能限制部分功能。

2. **Webhook 失效？**  
   - 检查 URL 是否被重置（可在 **「管理应用」** → **「Incoming Webhooks」** 中重新获取）。

3. **如何限制发送频率？**  
   - Slack 默认限制高频请求（约 1 条/秒），如需更高频率需申请企业版。

---

### **替代方案**
如果不想用 Webhook，还可以：
- 使用 **Slack API**（`chat.postMessage`）发送消息（需 OAuth 令牌）。
- 通过 **Zapier** 或 **Make（Integromat）** 无代码集成其他工具到 Slack。

如需进一步帮助，可参考 [Slack 官方文档](https://api.slack.com/messaging/webhooks)。