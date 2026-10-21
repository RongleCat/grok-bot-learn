---
title: Gemini CLI
sidebar: false
prev: false
next: false
---

# Gemini CLI

<ToolMeta id="gemini-cli" />

Google 开源的终端 AI Agent，适合 **付费用户与 Google Cloud 项目用户** 进行终端交互与开发协作。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你需要在云电脑上安装、配置并验证 Gemini CLI。请按以下步骤执行：

1. 目标：完成 Gemini CLI 的安装与认证，供付费或 Google Cloud 项目账号调用。
2. 安装与登录参考命令：
- 全局安装：npm install -g @google/gemini-cli
- 免安装运行方式：npx
- 登录：gemini
3. 登录与授权：运行 gemini 触发登录流程。遇到终端打印的授权链接时请先停下，原样发给我，由我在浏览器完成认证。不要让我把密钥贴进聊天，不要打印密钥。
4. 验证命令与预期结果：运行 gemini --version，预期成功输出版本号。
5. 常见坑及处理：
- 免费档与 Google One 用户已被 Antigravity CLI 取代，此类用户请直接使用 agy；本工具仅供付费或 Google Cloud 项目用户使用。
- 系统必须运行 Node.js 20+，版本过低会导致安装失败，需先升级 Node。
- 若地区不在 Gemini Code Assist 支持范围会被拒绝请求，可参考固定出口代理解决。
6. 汇报结果：完成后用几句话汇报 Node 版本、Gemini CLI 安装版本及可用状态。
````

</div>

## 需要你自己做的事

- 准备付费 Google 账号或 Google Cloud 项目账号
- 在浏览器打开 Bot 发送的授权链接完成认证
- 确保云电脑已安装 Node.js 20 及以上版本

## 来源

- [Gemini CLI 官方安装文档](https://geminicli.com/docs/get-started/installation/)
- [google-gemini/gemini-cli 官方仓库](https://github.com/google-gemini/gemini-cli)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
