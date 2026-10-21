---
title: X API 发帖（OAuth 1.0a PIN）
sidebar: false
prev: false
next: false
---

# X API 发帖（OAuth 1.0a PIN）

<ToolMeta id="x-api" />

直接调用 X 官方开发者 API 进行发帖、传图与删帖。**适合让 Bot 在云电脑上实现自动化定时发帖，仅检索讨论建议直接用 Grok 搜索。**

## 前置条件

- **需拥有 X 开发者账号并在控制台创建 App。**
- App 权限需设定为 `Read and write`（若需私信加 `Direct message`）。
- 获取 `Consumer Key` 与 `Consumer Secret` 并存放于本地私密文件。

## 登录与授权

**采用 OAuth 1.0a PIN 授权机制获取持久凭证。** 避免使用控制台生成的 2 小时易过期 OAuth 2.0 访问令牌。

## 操作步骤

1. 使用 OAuth 1.0a HMAC-SHA1 签名向 POST https://api.x.com/oauth/request_token 发起请求并携带参数 `oauth_callback=oob`。
2. 在浏览器中打开 https://api.x.com/oauth/authorize?oauth_token= 拼接返回令牌的地址，登录待发帖账号并授权。
3. 在授权成功页面获取显示的 PIN 码。
4. 携带 `oauth_verifier=PIN` 向 POST https://api.x.com/oauth/access_token 发起请求，保存返回的 `oauth_token` 与 `oauth_token_secret`。
5. 请求 GET https://api.x.com/2/users/me 核对当前绑定的账号信息。
6. 向 POST https://api.x.com/2/tweets 发送 JSON 正文 `{"text":"..."}` 发帖，配图需先上传媒体获取 `media_id` 填入 `media.media_ids`。

## 常见坑与解决

### 修改应用权限后发帖报错 403

**修改 App 权限后必须重新走一遍 PIN 授权流程。** 旧令牌不会自动同步新权限。

### 接口请求返回 401 未授权

**重新执行 PIN 授权并确认四个凭证与签名完整无误。** 401 通常由签名错误或凭据字段缺失导致。

### 发帖计费超出预期

**注意 X API 按调用计费且正文带链接推文更贵。** 具体费用以开发者控制台实时价格为准。

## 来源

- [X 官方文档：PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
