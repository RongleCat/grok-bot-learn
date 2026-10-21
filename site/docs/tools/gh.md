---
title: GitHub CLI（gh）
sidebar: false
prev: false
next: false
---

# GitHub CLI（gh）

<ToolMeta id="gh" />

GitHub 官方命令行工具，适合让 Bot 在 **云电脑** 上克隆私有仓库、推送代码、创建 PR 并管理 Actions。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上安装 GitHub CLI（https://github.com/cli/cli/blob/trunk/docs/install_linux.md），以后管理代码仓库、推送分支和提交 PR 用它。需要登录或授权时停下来把链接发给我由我完成。
````

</div>

## 需要你自己做的事

- 准备 GitHub 账号。
- 在浏览器打开授权链接并输入对应的一次性验证码。

## 来源

- [GitHub CLI Linux 安装文档](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 官方手册](https://cli.github.com/manual/gh_auth_login)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
