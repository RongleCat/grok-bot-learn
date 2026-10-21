---
title: Playwright
sidebar: false
prev: false
next: false
---

# Playwright

<ToolMeta id="playwright" />

Playwright 是微软开源的自动化库，适合让 Bot 执行**批量网页截图与渲染抓取**，无需手动耗费浏览器交互额度。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
请你在云电脑中为 Python 环境安装 Playwright 并下载 Chromium。

1. 目标：完成 Playwright 及其依赖环境的安装与可用性验证。
2. 参考命令：
- 创建虚拟环境：python3 -m venv ~/.venvs/pw
- 安装 Playwright：~/.venvs/pw/bin/pip install playwright
- 安装依赖与 Chromium：~/.venvs/pw/bin/python -m playwright install --with-deps chromium
3. 密钥与授权原则：遇到登录、授权、填密钥等只能我来做的步骤时，请先停下，把授权链接或验证码原样发给我，或请我把密钥填进本地私密文件，不要让我把密钥贴进聊天，不要打印密钥。
4. 常见坑及处理办法：
- Debian 系统的 Python 存在 PEP 668 保护，直接使用全局 pip install 会报 externally-managed-environment 错误，必须在上述 venv 虚拟环境中安装。
- 命令中的 --with-deps 会调用 sudo 安装系统依赖，如果当前环境没有 root 权限导致失败，请去掉 --with-deps 重试。
- 仅安装 chromium 浏览器，节省云电脑磁盘空间。
5. 安装完成标准：执行验证命令 ~/.venvs/pw/bin/python -m playwright --version，预期结果为正常打印版本号。
6. 执行完成后，用几句话向我汇报安装与验证结果。
````

</div>

## 需要你自己做的事

- 确认云电脑具备 Python 3 环境
- 若缺少 root 权限需配合确认依赖安装状态

## 来源

- [Playwright Python 官方文档](https://playwright.dev/python/docs/intro)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
