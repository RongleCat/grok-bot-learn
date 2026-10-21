---
title: GitHub CLI（gh）
sidebar: false
prev: false
next: false
---

# GitHub CLI（gh）

<ToolMeta id="gh" />

GitHub 官方命令行工具，适合让 Bot 在**云电脑**上无缝克隆私有仓库、推送代码、创建 PR 并管理 Actions。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你现在的目标是在云电脑上安装 GitHub CLI（gh），完成网页登录授权并配置 git 凭证。

1. 请在终端执行参考安装命令：
sudo apt-get install -y gh

2. 登录与授权处理要求：
执行参考登录命令：
gh auth login
在交互选项中选择 GitHub.com、HTTPS 以及通过浏览器登录。当终端输出一次性设备代码和验证链接时立即停下，把代码和链接原样发给我，由我在浏览器打开输入代码完成授权。严禁向我索要密码或 Token，不要打印敏感凭据。
授权完成后，在终端执行参考命令使 git 使用 gh 凭证：
gh auth setup-git

3. 安装完成标准：
在终端执行参考验证命令：
gh --version
gh auth status
预期结果：gh --version 正常输出版本号，gh auth status 显示当前登录账号状态正常。

4. 常见坑及处理办法：
- 若推送修改 .github/workflows 的提交，必须补齐工作流权限，可执行 gh auth refresh -s workflow 刷新。
- 在共用云电脑上提交代码时，使用 git -c user.name=... -c user.email=... commit 单独指定作者，避免修改全局配置。
- 提交前检查 .gitignore，严防将密钥、日志或构建文件推送到公开仓库。

5. 完成后请用几句话汇报 gh 的安装版本以及 auth status 的登录检测结果。
````

</div>

## 需要你自己做的事

- 准备 GitHub 账号
- 在浏览器打开授权链接并输入命令行给出的一次性代码
- 如需修改工作流提交按需授权 workflow 权限

## 来源

- [GitHub CLI Linux 安装文档](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 官方手册](https://cli.github.com/manual/gh_auth_login)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
