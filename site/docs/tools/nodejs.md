---
title: Node.js 与 npm
sidebar: false
prev: false
next: false
---

# Node.js 与 npm

<ToolMeta id="nodejs" />

`Node.js` 与 `npm` 是多种前端及终端命令行工具的运行时基础。**用于支撑各类 Agent 工具的全局安装与环境执行。**

## 前置条件

- **根据不同工具需求安装对应版本，如 Gemini CLI 需 20+，Pi 需 22.19+。**
- 推荐使用 `nvm` 在用户目录下管理与安装最新版本。

## 安装

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash
source ~/.bashrc
nvm install 22
```

## 登录与授权

**不需要登录。**

## 验证

```bash
node -v
npm -v
```

## 常见坑与解决

### 全局安装包报 `EACCES` 权限错误

**改用 nvm 管理环境或设置 `npm config set prefix ~/.local` 并将 ~/.local/bin 加入 PATH。** 切勿使用 sudo 执行 npm 全局安装。

### 多版本共存时执行版本不一致

**在终端执行 node -v 和 which node 确认当前调用的具体路径。** 确保使用的版本满足工具依赖要求。

## 来源

- [nvm 官方仓库](https://github.com/nvm-sh/nvm)
- [Node.js 官网](https://nodejs.org/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
