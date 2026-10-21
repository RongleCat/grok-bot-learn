---
title: Claude Code
sidebar: false
prev: false
next: false
---

# Claude Code

<ToolMeta id="claude-code" />

Anthropic 官方终端编码 Agent，适合 **代码库阅读、多文件修改与命令执行**，支持后台自动更新。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你需要在云电脑上安装、配置并验证 Claude Code。请按以下步骤执行：

1. 目标：在云电脑上安装 Anthropic 官方 Claude Code 并完成授权与版本验证。
2. 安装与登录参考命令：
- 原生安装（推荐）：curl -fsSL https://claude.ai/install.sh | bash
- npm 方式（Node 18+，切勿使用 sudo）：npm install -g @anthropic-ai/claude-code
- 登录：在项目目录下运行 claude
3. 登录与授权：在项目目录执行 claude 启动登录。若终端提示登录链接或授权流程，请立刻停下，将授权链接原样发给我，由我在浏览器中完成授权。不要让我把密钥贴进聊天，不要打印密钥。
4. 验证命令与预期结果：运行 claude --version，预期输出当前安装的版本号；后续非交互调用使用 claude -p。
5. 常见坑及处理：
- 若安装后提示 command not found，说明安装目录未进 PATH，请将 ~/.local/bin 加入 PATH 或重开终端。
- 若安装命令报 syntax error near unexpected token '<' 或 403 错误，通常为网络或支持地区问题，需核对网络与地区设置。
- 确保系统为 Ubuntu 20.04+ 或 Debian 10+ 且内存保持在 4GB 以上。
6. 汇报结果：完成后用几句话汇报 Claude Code 的安装版本与就绪状态。
````

</div>

## 需要你自己做的事

- 准备 Claude 订阅或 Anthropic Console 账号
- 在浏览器打开 Bot 发送的授权链接完成认证
- 确保云电脑系统满足 Ubuntu 20.04 或 Debian 10 以上且内存不少于 4GB

## 来源

- [Claude Code 官方安装文档](https://code.claude.com/docs/en/setup)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
