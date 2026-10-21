---
title: Codex CLI
sidebar: false
prev: false
next: false
---

# Codex CLI

<ToolMeta id="codex" />

`codex` 是 OpenAI 官方终端编码 Agent，消耗 ChatGPT 订阅额度而非 API 余额。**适合在云电脑上修改代码、运行脚本、生成图片与审查图片。**

## 前置条件

- **系统需安装 Node.js 与 npm。**
- 拥有 ChatGPT 账号，个人账号需在安全设置中开启设备码登录，企业工作区需管理员开启。

## 安装

```bash
npm install -g @openai/codex@latest
```

## 登录与授权

**在云电脑上运行 `codex login --device-auth` 进行设备码登录。** 打开终端显示的授权链接并输入对应的一次性码即可完成验证。

```bash
codex login --device-auth
```

## 验证

```bash
codex login status
cd /tmp && codex exec --skip-git-repo-check "只回复 OK" </dev/null
```

## 常见坑与解决

### codex exec 卡在等待标准输入

**非交互调用时必须在命令末尾追加 `</dev/null`。** 否则程序会提示 `Reading additional input from stdin` 并持续等待。

### 默认沙箱只读或在非 git 目录报错

**写入文件需添加 `-s workspace-write -C 目标目录` 参数。** 若不在 git 仓库中运行需添加 `--skip-git-repo-check`。

### 多台机器共用凭据导致 401 报错

**每台机器必须各自执行 `codex login --device-auth` 独立登录。** 共用登录文件会导致令牌刷新互相挤掉。

### 生图生成两张或找不到存储路径

**提示词中需写明只生成一张并要求复制到当前目录。** 内置生图默认保存在 `~/.codex/generated_images` 路径下。

## 来源

- [OpenAI Codex CLI 官方文档](https://developers.openai.com/codex/cli)
- [openai/codex 官方仓库](https://github.com/openai/codex)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
