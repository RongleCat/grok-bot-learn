---
title: yt-dlp
sidebar: false
prev: false
next: false
---

# yt-dlp

<ToolMeta id="yt-dlp" />

yt-dlp 是支持上千个站点的命令行音视频下载工具，适合让 Bot **批量下载视频或抽取音频**以供后续转写处理。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
请你在云电脑中为 Python 环境安装最新版 yt-dlp。

1. 目标：在专属虚拟环境中安装 yt-dlp[default] 并验证可用性。
2. 参考命令：
- 创建虚拟环境：python3 -m venv ~/.venvs/ytdlp
- 安装工具：~/.venvs/ytdlp/bin/pip install -U "yt-dlp[default]"
3. 密钥与授权原则：遇到登录、授权、填密钥等只能我来做的步骤时，请先停下，把授权链接或验证码原样发给我，或请我把密钥填进本地私密文件，不要让我把密钥贴进聊天，不要打印密钥。
4. 常见坑及处理办法：
- 若环境未安装 ffmpeg，则只能下载单路音视频流，无法执行流合并与转码操作。
- 部分站点需要登录或校验，后续使用时可通过 --cookies 传入我导出的 cookie 文件，cookie 文件包含敏感信息切勿外传。
- 站点改版导致下载失败时，可先执行 yt-dlp -U 尝试更新。
- 严格遵守版权规范，只下载有权使用的内容。
5. 安装完成标准：执行验证命令 ~/.venvs/ytdlp/bin/yt-dlp --version，预期结果为正常输出 yt-dlp 的版本号。
6. 执行完成后，用几句话向我汇报安装与验证结果。
````

</div>

## 需要你自己做的事

- 准备需要下载的目标媒体链接
- 若目标站点需登录鉴权，提前导出 cookie 文件备用

## 来源

- [yt-dlp 官方仓库](https://github.com/yt-dlp/yt-dlp)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
