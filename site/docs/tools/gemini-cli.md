---
title: Gemini CLI
sidebar: false
prev: false
next: false
---

# Gemini CLI

<ToolMeta id="gemini-cli" />

`gemini` 是 Google 开源的终端 AI Agent。**适合付费档或 Google Cloud 项目用户在终端执行 AI 交互任务。**

## 前置条件

- **系统需安装 Node.js 20+。**
- 需拥有付费档或 Google Cloud 项目账号，免费档与 Google One 用户请直接使用 `agy`。

## 安装

```bash
npm install -g @google/gemini-cli
```

## 登录与授权

**使用前需配置 Google Cloud 项目或付费凭证。** 也可以不安装直接通过 `npx` 命令运行。

```bash
gemini
```

## 验证

```bash
gemini --version
```

## 常见坑与解决

### 安装失败提示版本不兼容

**先将系统的 Node.js 升级至 20 或更高版本。** Node.js 版本过低会导致安装流程中断。

### 请求被拒提示所在地区不受支持

**配置固定出口代理后再发起请求。** 地区不在 Gemini Code Assist 支持范围会被拦截，可接入固定出口代理转发流量。

## 来源

- [Gemini CLI 官方安装文档](https://geminicli.com/docs/get-started/installation/)
- [google-gemini/gemini-cli 官方仓库](https://github.com/google-gemini/gemini-cli)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
