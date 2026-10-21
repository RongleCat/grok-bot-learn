---
title: Antigravity CLI（agy）
sidebar: false
prev: false
next: false
---

# Antigravity CLI（agy）

<ToolMeta id="agy" />

`agy` 是 Google 官方终端 Agent，支持通过 `--model` 指定模型与 `-p` 开展非交互输出。**它能直接读取视频文件，适合视频理解、长文写作与代码修改。**

## 前置条件

- **系统需运行在 Linux 环境且满足 glibc&gt;=2.28。**
- 需拥有 Google 账号。

## 安装

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

## 登录与授权

**首次运行 agy 时选择 Google OAuth。** 远程机器上会打印授权链接，在本地浏览器打开授权后将验证码粘回终端，随后完成主题、服务条款与目录信任确认。

```bash
agy
```

## 验证

```bash
agy --version
agy -p "只回复 OK"
```

## 常见坑与解决

### 提示 `agy: command not found`

**在终端执行 `export PATH="$HOME/.local/bin:$PATH"` 并重新打开终端。** 安装器默认将二进制文件放置在 `~/.local/bin`。

### 提示所在地区不受支持或拒绝请求

**配置固定出口代理让 agy 流量走海外 VPS。** 运行前将 `HTTPS_PROXY` 与 `ALL_PROXY` 设置为 `socks5h` 地址，或编写同名包装脚本自动开隧道。

### 非交互调用卡住或报错

**先在交互模式下完成首次登录与当前目录信任。** Bot 自身的 shell 无法在非交互模式下回答交互提问。

## 来源

- [Antigravity 官方文档：快速开始](https://antigravity.google/docs/getting-started/)
- [Antigravity CLI 官方仓库](https://github.com/google-antigravity/antigravity-cli)
- [Antigravity CLI 故障排查](https://antigravity.google/docs/cli/troubleshooting/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
