---
title: Claude Code
sidebar: false
prev: false
next: false
---

# Claude Code

<ToolMeta id="claude-code" />

`claude` 是 Anthropic 官方终端编码 Agent。**适合用于阅读代码库、多文件协同修改以及在终端执行命令。**

## 前置条件

- **系统需为 Ubuntu 20.04+ 或 Debian 10+，且内存大于 4GB。**
- 所在地区需在 Anthropic 支持范围内。
- 拥有 Claude 订阅或 Anthropic Console 账号。
- 若使用 npm 安装需具备 Node.js 18+ 环境。

## 安装

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

## 登录与授权

**在项目目录下运行 claude 并按终端提示完成登录。** 后续非交互执行可直接使用 `claude -p`。

```bash
claude
```

## 验证

```bash
claude --version
```

## 常见坑与解决

### 安装后提示 command not found

**重新打开终端，或将 ~/.local/bin 手动添加进 PATH 环境变量。** 安装目录未生效会导致找不到命令。

### 安装报错 syntax error 或 403

**排查网络连接与所在地区是否受限。** 这类报错通常由网络或地区限制导致，可参考官方 Troubleshoot installation 文档。

## 来源

- [Claude Code 官方安装文档](https://code.claude.com/docs/en/setup)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
