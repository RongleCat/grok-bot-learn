---
title: Pi Coding Agent
sidebar: false
prev: false
next: false
---

# Pi Coding Agent

<ToolMeta id="pi" />

极简且高度可扩展的终端编码 Agent，适合 **通过扩展、技能与提示模板深度定制** 专属开发工作流。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你需要在云电脑上安装、配置并验证 Pi Coding Agent。请按以下步骤执行：

1. 目标：完成 Pi Coding Agent 的安装与基础配置，连接模型服务商并验证运行状态。
2. 安装与升级参考命令：
- 官方脚本安装：curl -fsSL https://pi.dev/install.sh | sh
- npm 安装：npm install -g --ignore-scripts @earendil-works/pi-coding-agent
- 升级命令：pi update
- 登录：在项目目录运行 pi，并在交互界面内输入 /login
3. 登录与授权：在项目目录运行 pi 并输入 /login 连接订阅或配置服务商 API Key；也可预先配置服务商环境变量。遇到需要填写密钥的步骤时请停下，请我将密钥填入本地私密文件或设置环境变量，不要让我把密钥贴进聊天，不要打印密钥。
4. 验证命令与预期结果：安装完成后在项目目录启动 pi，预期能正常进入会话界面且自带 read、write、edit、bash 四项工具；后续升级可运行 pi update。
5. 常见坑及处理：
- 旧包 @mariozechner/pi-coding-agent 已弃用并停在 0.73.1，必须安装 @earendil-works/pi-coding-agent，旧用户升级可能需执行两次 pi update。
- 系统 Node.js 需为 22.19 或更新版本，若使用 npm 方式需先自行升级 Node（官方脚本可顺带安装 Node）。
- Pi 包可以执行扩展代码，安装任何第三方包前必须先查看源码。
6. 汇报结果：完成后用几句话汇报 Pi 的安装方式、版本信息与服务商配置结果。
````

</div>

## 需要你自己做的事

- 准备模型服务商的 API Key 或订阅账号
- 根据提示将 API Key 写入本地私密文件或配置为环境变量
- 若通过 npm 安装需确保 Node.js 版本达到 22.19 及以上

## 来源

- [Pi 官网](https://pi.dev)
- [earendil-works/pi 官方仓库](https://github.com/earendil-works/pi)
- [Pi 迁移公告](https://pi.dev/news/2026/5/7/pi-has-a-new-home)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
