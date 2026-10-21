---
title: Antigravity CLI（agy）
sidebar: false
prev: false
next: false
---

# Antigravity CLI（agy）

<ToolMeta id="agy" />

Google 官方终端 Agent，适合 **视频理解、长文写作与代码修改**，支持直接读取视频文件。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你需要在云电脑上安装、配置并验证 Antigravity CLI（agy）。请按以下步骤执行：

1. 目标：完成 Antigravity CLI 的安装与环境配置，通过 Google OAuth 授权并验证可用性。
2. 安装参考命令：运行 curl -fsSL https://antigravity.google/cli/install.sh | bash 完成安装。
3. 登录与授权：在终端运行 agy。遇到 Google OAuth 登录时，终端会打印授权链接，请立刻停下，把授权链接原样发给我。等我在浏览器完成授权后，我会把验证码发给你，你再粘回终端继续。随后完成主题、服务条款与当前目录信任确认。不要让我把密钥或敏感信息发进聊天，不要在日志中打印密钥。
4. 验证命令与预期结果：运行 agy --version，预期输出版本号；运行 agy -p "只回复 OK"，预期正常返回 OK。
5. 常见坑及处理：
- 若提示 agy: command not found，说明二进制在 ~/.local/bin 且未加入环境变量，执行 export PATH="$HOME/.local/bin:$PATH" 后重开终端。
- 若云电脑出口 IP 变动导致 Google 报地区不支持或拒绝请求，需设置固定出口代理，例如设置 HTTPS_PROXY/ALL_PROXY 为 socks5h 地址，或编写同名包装脚本代理运行。
- 非交互调用无法响应交互提问，必须先在交互模式下完成首次登录与目录信任。
6. 汇报结果：完成后用几句话汇报 agy 版本、代理及非交互测试结果。
````

</div>

## 需要你自己做的事

- 准备 Google 账号
- 点击 Bot 发送的授权链接完成验证并将验证码发回终端
- 网络受限时准备固定出口代理

## 来源

- [Antigravity 官方文档：快速开始](https://antigravity.google/docs/getting-started/)
- [Antigravity CLI 官方仓库](https://github.com/google-antigravity/antigravity-cli)
- [Antigravity CLI 故障排查](https://antigravity.google/docs/cli/troubleshooting/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
