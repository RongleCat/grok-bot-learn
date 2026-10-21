---
title: yt-dlp
sidebar: false
prev: false
next: false
---

# yt-dlp

<ToolMeta id="yt-dlp" />

`yt-dlp` 是支持上千个站点的开源命令行音视频下载器。**适合让 Bot 下载视频原片或抽取独立音频以供转写工具处理。**

## 前置条件

- **系统需安装 Python 3.10+。**
- 音视频合并与转码需预先安装 `ffmpeg`。

## 安装

```bash
python3 -m venv ~/.venvs/ytdlp
~/.venvs/ytdlp/bin/pip install -U "yt-dlp[default]"
```

## 登录与授权

**不需要登录。** 遇到需校验或登录的站点可通过 `--cookies` 参数传入本地导出的 cookie 文件，严禁外传该文件。

## 验证

```bash
~/.venvs/ytdlp/bin/yt-dlp --version
```

## 常见坑与解决

### 下载后无法合并音视频文件

**在系统中安装 ffmpeg 工具。** 缺少该依赖时程序仅能下载单路流而无法完成合并转码。

### 目标站点调整导致解析下载失败

**执行 `yt-dlp -U` 命令更新至最新版本。** 站点结构调整常导致旧版本解析规则失效，且注意仅下载有权使用的内容。

## 来源

- [yt-dlp 官方仓库](https://github.com/yt-dlp/yt-dlp)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
