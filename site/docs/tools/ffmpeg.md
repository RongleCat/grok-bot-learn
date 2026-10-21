---
title: FFmpeg
sidebar: false
prev: false
next: false
---

# FFmpeg

<ToolMeta id="ffmpeg" />

`ffmpeg` 是一套开源音视频多媒体处理工具。**适合用于音视频转码、画面压缩、指定时间截帧、抽取音频、字幕烧录与视频拼接。**

## 前置条件

- **Debian 或 Ubuntu 系统需具备 sudo 权限以通过 apt 安装。**
- 烧录中文字幕前需确保已安装中文字体。

## 安装

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

## 登录与授权

**不需要登录。**

## 验证

```bash
ffmpeg -version
```

## 常见坑与解决

### 系统重置后命令失效

**将 apt 安装命令写入工作目录的初始化恢复脚本中。** 云电脑环境重置可能会清空系统包。

### 烧录中文字幕时文字显示为方块

**在系统环境中安装中文字体包。** 缺少对应字库会导致字符无法正确渲染。

### 处理大文件长时间阻塞终端

**将转码任务放入后台执行并将输出重定向至日志文件。** 耗时较长的操作避免在前台阻塞进程。

## 来源

- [FFmpeg 官方下载页](https://ffmpeg.org/download.html)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
