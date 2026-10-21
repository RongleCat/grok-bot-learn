---
title: muse2api
sidebar: false
prev: false
next: false
---

# muse2api

<ToolMeta id="muse2api" />

`muse2api` 是通过无头浏览器驱动 muse.ai 网页端的开源项目，默认运行在 `18610` 端口。**适合让 Bot 本地调用其兼容接口，消耗网页端免费额度进行生图、生视频与对话。**

## 前置条件

- **环境需为 Debian 或 Ubuntu 且安装有 Chromium 与 Python 3.10+，或具备 Docker 环境。**
- 需拥有 muse.ai 账号。

## 安装

```bash
git clone https://github.com/czg86389-hub/muse2api.git
cd muse2api
cp .env.example .env
docker compose up -d
```

## 登录与授权

**在云电脑浏览器中登录 muse.ai 后，利用自带的 Chrome 扩展导入登录态。** 在扩展中填入服务地址与 `MUSE2API_KEY` 点击读取导入，会话约 48 小时自动续期。

## 验证

```bash
curl -s http://127.0.0.1:18610/v1/chat/completions -H "Authorization: Bearer $MUSE2API_KEY" -H "Content-Type: application/json" -d '{"model":"muse-spark","messages":[{"role":"user","content":"只回复 OK"}]}'
```

## 常见坑与解决

### 导入时提示缺少核心 cookie `hatch_vml`

**在同一浏览器打开 `https://muse.ai/api/session` 并刷新 muse.ai 页面后重试。** 这样即可补全所需会话凭据。

### 视频生成时长设置无效

**接口参数必须使用 `duration` 而非 `seconds`。** 传 `seconds` 会被忽略并默认设定为 6 秒，且需轮询 `/v1/videos/{task_id}` 获取异步结果。

### 接口偶发报错或未生成媒体

**此情况属于临时错误，执行退避重试即可。** 另外项目基于逆向网页端，密钥只保存在 `.env` 中且不要盲目在线升级。

## 来源

- [muse2api 项目仓库（czg86389-hub）](https://github.com/czg86389-hub/muse2api)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
