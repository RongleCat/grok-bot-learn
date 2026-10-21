---
title: Cursor CLI
sidebar: false
prev: false
next: false
---

# Cursor CLI

<ToolMeta id="cursor-cli" />

Cursor 官方命令行 Agent，适合 **在云电脑执行小范围代码修改**，将 Bot 额度留给全局决策。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你需要在云电脑上安装、配置并验证 Cursor CLI。请按以下步骤执行：

1. 目标：完成 Cursor CLI 的安装与认证，支持在云电脑上进行非交互代码修改。
2. 安装与登录参考命令：
- 安装：curl https://cursor.com/install -fsS | bash
- 登录：NO_OPEN_BROWSER=1 agent login
- 状态查询：agent status
3. 登录与授权：在终端运行 NO_OPEN_BROWSER=1 agent login 触发登录。终端打印授权链接时立刻停下，把链接原样发给我，由我在浏览器打开登录。若使用 CURSOR_API_KEY 环境变量，请让我填入本地私密文件或环境变量，不要让我把密钥贴进聊天，不要打印密钥。
4. 验证命令与预期结果：
- 运行 agent --version，预期输出版本号。
- 在项目目录运行 agent -p "只回复 OK" --trust --output-format text </dev/null，预期输出 OK。
5. 常见坑及处理：
- 非交互调用时必须追加 </dev/null，避免卡在等待标准输入。
- 无人值守执行必须加上 --trust，否则会卡在目录信任提问。
- 绝不要随手加 --model，否则会修改账号内配置的默认模型。
- 若提示找不到命令，将 ~/.local/bin 加入 PATH；若连不上服务器，放行 *.cursor.sh 与 *.cursorapi.com。
6. 汇报结果：完成后用几句话汇报版本号、登录状态以及非交互测试执行结果。
````

</div>

## 需要你自己做的事

- 准备 Cursor 账号或 CURSOR_API_KEY
- 在浏览器打开 Bot 发送的授权链接完成登录
- 确保云电脑网络放行 *.cursor.sh 与 *.cursorapi.com 域名

## 来源

- [Cursor CLI 官方安装文档](https://cursor.com/docs/cli/installation)
- [Cursor CLI 官方认证文档](https://cursor.com/docs/cli/reference/authentication)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
