---
title: Cursor CLI
sidebar: false
prev: false
next: false
---

# Cursor CLI

<ToolMeta id="cursor-cli" />

`agent` 是 Cursor 官方命令行 Agent。**适合在云电脑上执行小范围代码修改，从而节省 Bot 自身的决策额度。**

## 前置条件

- **需拥有 Cursor 账号。**

## 安装

```bash
curl https://cursor.com/install -fsS | bash
```

## 登录与授权

**在云电脑上设置 `NO_OPEN_BROWSER=1` 后执行 agent login 获取授权链接。** 在本地浏览器中打开链接完成登录，脚本或 CI 环境可直接配置 `CURSOR_API_KEY` 环境变量。

```bash
NO_OPEN_BROWSER=1 agent login
agent status
```

## 验证

```bash
agent --version
agent -p "只回复 OK" --trust --output-format text </dev/null
```

## 常见坑与解决

### 非交互运行时命令卡住等待

**非交互调用时命令末尾必须追加 `</dev/null`。** 同时无人值守时必须携带 `--trust` 参数以跳过工作区信任确认。

### 随手添加 `--model` 导致配置变动

**避免随意添加 `--model` 参数。** 该参数会直接修改你在账号中设定的默认模型。

### 找不到 agent 命令或连接失败

**将 ~/.local/bin 加进 PATH，并在网络中放行 *.cursor.sh 与 *.cursorapi.com。** 确保命令路径生效且域名未被防火墙拦截。

## 来源

- [Cursor CLI 官方安装文档](https://cursor.com/docs/cli/installation)
- [Cursor CLI 官方认证文档](https://cursor.com/docs/cli/reference/authentication)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
