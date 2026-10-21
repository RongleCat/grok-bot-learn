---
title: X API 发帖（OAuth 1.0a PIN）
sidebar: false
prev: false
next: false
---

# X API 发帖（OAuth 1.0a PIN）

<ToolMeta id="x-api" />

基于 OAuth 1.0a PIN 授权的 X 官方接口调用方案，适合让 Bot 在**云电脑**上安全执行发帖、传图与删帖任务。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你现在的目标是在云电脑上通过 OAuth 1.0a PIN 模式完成 X API 授权与发帖能力验证。

1. 参考请求流程：
素材未提供预置 shell 命令，严禁编造素材之外的命令。请严格按照以下原生步骤实现授权与调用：
- 第一步：使用 OAuth 1.0a HMAC-SHA1 签名向 POST https://api.x.com/oauth/request_token 发送请求，携带参数 oauth_callback=oob 获取临时令牌。
- 第二步：拼装授权网址 https://api.x.com/oauth/authorize?oauth_token=返回的令牌 并原样发给我。
- 第三步：收到我发回的 PIN 后，携带 oauth_verifier=PIN 向 POST https://api.x.com/oauth/access_token 请求获取 oauth_token 与 oauth_token_secret 并妥善保存。
- 第四步：调用 GET https://api.x.com/2/users/me 核对账号信息。
- 第五步：调用 POST https://api.x.com/2/tweets 发送推文，正文格式为 {"text":"..."}（若有配图先上传媒体获取 media_id 放入 media.media_ids）。

2. 凭证与授权处理要求：
开始前请停下，请我将 X 开发者后台生成的 Consumer Key 和 Consumer Secret 填入本地私密文件，不要让我贴进聊天，严禁打印密钥。第二步获取临时令牌后必须停下，把授权链接原样发给我，等待我在浏览器登录并把页面显示的 PIN 发回，不得自行伪造 PIN。

3. 安装完成标准：
调用 GET https://api.x.com/2/users/me 预期能正确返回当前授权用户的账号信息；调用 POST https://api.x.com/2/tweets 预期成功发布一条测试推文并返回推文 ID。

4. 常见坑及处理办法：
- 控制台直接生成的 OAuth 2.0 Access Token 有效期仅 2 小时，发帖必须使用 OAuth 1.0a。
- 在开发者后台修改 App 权限后，旧令牌不会自动生效，必须重新走一遍 PIN 授权流程，否则发帖报 403。
- 若请求报 401，多为签名算法错误或四个字段不完整，重新执行 PIN 流程获取完整凭据。
- X API 按调用计费，正文含链接的推文费用更高，以控制台实时价格为准。

5. 完成后请用几句话汇报账号核验结果及测试推文的发布结果。
````

</div>

## 需要你自己做的事

- 在 X 开发者平台创建 App 并开启 Read and write 权限
- 将 Consumer Key 与 Consumer Secret 存入本地私密文件
- 在浏览器打开授权链接并把页面显示的 PIN 码发给 Bot

## 来源

- [X 官方文档：PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
