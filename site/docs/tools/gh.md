---
title: GitHub CLI（gh）
sidebar: false
prev: false
next: false
---

# GitHub CLI（gh）

<ToolMeta id="gh" />

`gh` 是 GitHub 官方命令行工具。**适合让 Bot 在云电脑上克隆私有仓库、推送代码、创建 PR 以及审查 Actions 任务。**

## 前置条件

- **系统需预先安装 git。**
- 参考官方 Linux 文档添加 apt 源后安装 `gh`。

## 安装

```bash
sudo apt-get install -y gh
```

## 登录与授权

**运行 `gh auth login` 选择 GitHub.com、HTTPS 并通过浏览器设备码授权。** 随后运行 `gh auth setup-git` 将凭据绑定到 git 操作。

```bash
gh auth login
gh auth setup-git
```

## 验证

```bash
gh --version
gh auth status
```

## 常见坑与解决

### 推送包含工作流的提交失败

**执行 `gh auth refresh -s workflow` 为当前令牌补全权限。** 修改 `.github/workflows` 必须具备 workflow 权限。

### 共用机器污染全局 git 作者配置

**提交代码时使用 git -c user.name=... -c user.email=... commit 临时指定作者。** 这样可避免覆盖全局凭据。

### 敏感凭据与文件泄露

**在推送前仔细检查 .gitignore 文件配置。** 杜绝将私密密钥、日志与构建产物推送到远程仓库。

## 来源

- [GitHub CLI Linux 安装文档](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 官方手册](https://cli.github.com/manual/gh_auth_login)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
