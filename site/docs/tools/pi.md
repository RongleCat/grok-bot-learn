---
title: Pi Coding Agent
sidebar: false
prev: false
next: false
---

# Pi Coding Agent

<ToolMeta id="pi" />

`pi` 是由 Earendil Works 维护的极简终端编码 Agent，默认仅提供 `read`、`write`、`edit`、`bash` 四个基础工具。**支持通过扩展、技能、Pi 包以及 TypeScript SDK 进行高度自定义。**

## 前置条件

- **系统需运行在 Node.js 22.19 或更新版本。**
- 可使用官方安装脚本或带 `--ignore-scripts` 的 npm 全局安装。

## 安装

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

## 登录与授权

**在项目目录运行 pi 并输入 `/login` 选择服务商以连接订阅或 API Key。** 也可以预先在环境中设置服务商的 API Key 环境变量。

```bash
pi
```

## 常见坑与解决

### 安装后无法运行或停留在旧版本 0.73.1

**旧包 @mariozechner/pi-coding-agent 已弃用，请迁移至 @earendil-works。** 老用户使用 `pi update` 可能需要连续执行两次。

### 第三方 Pi 包存在安全隐患

**安装第三方 Pi 包前务必先查看源码。** Pi 包具备执行扩展代码的权限。

### npm 安装后启动报错

**检查并升级系统的 Node.js 版本至 22.19 及以上。** 系统 Node.js 低于该版本将无法运行。

## 来源

- [Pi 官网](https://pi.dev)
- [earendil-works/pi 官方仓库](https://github.com/earendil-works/pi)
- [Pi 迁移公告](https://pi.dev/news/2026/5/7/pi-has-a-new-home)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
