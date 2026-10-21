---
title: Codex CLI
sidebar: false
prev: false
next: false
---

# Codex CLI

<ToolMeta id="codex" />

OpenAI 官方终端编码 Agent，适合 **代码修改、脚本运行与生图审图**，可直接使用 ChatGPT 订阅额度。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你需要在云电脑上安装、配置并验证 Codex CLI。请按以下步骤执行：

1. 目标：使用 ChatGPT 订阅额度完成 Codex CLI 的全局安装与设备码授权，并通过非交互执行验证。
2. 安装与登录参考命令：
- 安装：npm install -g @openai/codex@latest
- 登录：codex login --device-auth
- 登录状态检查：codex login status
3. 登录与授权：运行 codex login --device-auth 启动设备码登录。遇到终端输出授权链接与一次性码时立刻停下，将链接与验证码原样发给我，由我在浏览器完成确认。不要让我把密钥贴进聊天，不要打印密钥。
4. 验证命令与预期结果：
- 运行 codex login status，预期显示已成功登录。
- 运行 cd /tmp && codex exec --skip-git-repo-check "只回复 OK" </dev/null，预期输出 OK。
5. 常见坑及处理：
- 非交互调用 codex exec 时必须在末尾加上 </dev/null，否则会一直等待标准输入。
- 默认沙箱为只读，若需修改文件需添加 -s workspace-write -C 目标目录；在非 git 仓库执行需加 --skip-git-repo-check。
- 严禁多台机器共用同一份登录文件，令牌刷新会互相挤掉导致 401 报错，每台机器必须各自运行 codex login --device-auth。
- 生图结果默认保存在 ~/.codex/generated_images，如需生图请在提示词中要求复制到当前目录且明确只生成一张。
6. 汇报结果：完成后用几句话汇报登录状态与验证执行情况。
````

</div>

## 需要你自己做的事

- 准备 ChatGPT 账号并开启设备码登录（企业工作区需管理员开启）
- 在浏览器打开 Bot 发送的设备码链接并完成确认
- 确保云电脑具备 Node.js 与 npm 环境

## 来源

- [OpenAI Codex CLI 官方文档](https://developers.openai.com/codex/cli)
- [openai/codex 官方仓库](https://github.com/openai/codex)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
