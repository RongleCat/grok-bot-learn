---
title: Node.js 与 npm
sidebar: false
prev: false
next: false
---

# Node.js 与 npm

<ToolMeta id="nodejs" />

Node.js 与 npm 是前端及各类 AI CLI 的执行基础，适合为 Bot 提供**现代命令行工具的运行环境**。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
请你在云电脑的用户目录下通过 nvm 安装 Node.js 22 和 npm。

1. 目标：安装 nvm 并使用其安装 Node.js 22。
2. 参考命令：
- 下载安装 nvm：curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash
- 重载环境配置：source ~/.bashrc
- 安装 Node.js 22：nvm install 22
3. 密钥与授权原则：遇到登录、授权、填密钥等只能我来做的步骤时，请先停下，把授权链接或验证码原样发给我，或请我把密钥填进本地私密文件，不要让我把密钥贴进聊天，不要打印密钥。
4. 常见坑及处理办法：
- 执行 npm install -g 若报 EACCES 权限错误，切勿使用 sudo，改用 nvm 环境或使用 npm config set prefix ~/.local 并把 ~/.local/bin 加进 PATH。
- 若环境中存在多个 Node 版本，使用 node -v 和 which node 确认当前使用的版本与路径。
- 安装后若未找到命令，确认已执行 source ~/.bashrc。
5. 安装完成标准：分别执行验证命令 node -v 和 npm -v，预期结果为正常输出 Node.js 的 22.x 版本号以及 npm 版本号。
6. 执行完成后，用几句话向我汇报安装与验证结果。
````

</div>

## 需要你自己做的事

- 无需准备外部账号或密钥

## 来源

- [nvm 官方仓库](https://github.com/nvm-sh/nvm)
- [Node.js 官网](https://nodejs.org/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
