# GitHub Token 获取指南

## 1. 访问 GitHub 设置

1. 登录您的 GitHub 账号
2. 点击右上角的头像
3. 在下拉菜单中选择 "Settings"（设置）

## 2. 进入开发者设置

1. 在左侧菜单栏中滚动到底部
2. 点击 "Developer settings"（开发者设置）
3. 在新页面中点击 "Personal access tokens"（个人访问令牌）
4. 选择 "Tokens (classic)" 或 "Fine-grained tokens"

## 3. 生成新的 Token

### 使用 Fine-grained tokens（推荐）

1. 点击 "Generate new token"（生成新令牌）
2. 选择 "Generate new token (classic)"
3. 填写 Token 信息：
   - Note（备注）：填写用途，如 "GitHub Agent"
   - Expiration（有效期）：选择合适的时间，建议 30 天或更长
   - Select scopes（选择权限）：
     - `repo`（仓库访问权限）
     - `read:org`（读取组织信息）
     - `read:user`（读取用户信息）

### 使用 Classic tokens

1. 点击 "Generate new token"（生成新令牌）
2. 选择 "Generate new token (classic)"
3. 填写 Token 信息：
   - Note（备注）：填写用途，如 "GitHub Agent"
   - Expiration（有效期）：选择合适的时间
   - Select scopes（选择权限）：
     - `repo`（完整仓库访问权限）
     - `read:org`（读取组织信息）
     - `read:user`（读取用户信息）

## 4. 保存 Token

1. 点击页面底部的 "Generate token"（生成令牌）按钮
2. **重要：立即复制生成的 Token**
   - Token 只会显示一次
   - 如果忘记复制，需要重新生成

## 5. 配置到项目中

1. 打开项目的 `config.json` 文件
2. 将 Token 填入 `github_token` 字段：
```json
{
    "github_token": "你的_github_令牌",
    ...
}
```

## 注意事项

1. **安全性**
   - 永远不要分享您的 Token
   - 不要将 Token 提交到代码仓库
   - 定期更新 Token
   - 使用最小权限原则

2. **Token 格式**
   - 使用纯 ASCII 字符
   - 避免使用特殊字符
   - 确保没有多余的空格

3. **权限范围**
   - 只授予必要的权限
   - 定期检查权限设置
   - 及时撤销不需要的权限

4. **有效期管理**
   - 设置合适的有效期
   - 在过期前更新 Token
   - 记录 Token 的过期时间

## 常见问题

1. **Token 不工作**
   - 检查 Token 是否过期
   - 验证权限设置是否正确
   - 确认 Token 格式是否正确

2. **权限不足**
   - 检查是否选择了正确的权限范围
   - 确认账号是否有足够的权限
   - 联系仓库管理员获取必要权限

3. **Token 泄露**
   - 立即在 GitHub 设置中撤销 Token
   - 生成新的 Token
   - 更新所有使用该 Token 的配置

## 最佳实践

1. **环境变量**
   - 考虑使用环境变量存储 Token
   - 避免在配置文件中硬编码
   - 使用 `.env` 文件管理敏感信息

2. **Token 轮换**
   - 定期更换 Token
   - 使用多个 Token 分散风险
   - 记录 Token 的使用情况

3. **监控和审计**
   - 定期检查 Token 使用情况
   - 监控异常访问
   - 记录 Token 相关操作 