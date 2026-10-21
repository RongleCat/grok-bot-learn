---
title: 固定出口代理（SSH 隧道）
sidebar: false
prev: false
next: false
---

# 固定出口代理（SSH 隧道）

<ToolMeta id="egress-proxy" />

利用 OpenSSH 的动态端口转发在本地建立 SOCKS5 代理。**适合让特定命令行工具的流量经由受支持的海外 VPS 出口，解决地区限制拦截。**

## 前置条件

- **需拥有一台处于受支持地区的海外 VPS。**
- 可使用 SSH 密钥免密登录 VPS，私钥权限需设为 `600`。

## 安装

```bash
ssh -fN -o ServerAliveInterval=30 -D 127.0.0.1:1081 user@your-vps
```

## 登录与授权

**基于本地 SSH 密钥进行服务器连接认证。** 私钥需放置于本地私密目录，严禁对外泄露。

```bash
export HTTPS_PROXY=socks5h://127.0.0.1:1081 ALL_PROXY=socks5h://127.0.0.1:1081 NO_PROXY=localhost,127.0.0.1
```

## 验证

```bash
curl --proxy socks5h://127.0.0.1:1081 https://ifconfig.me
```

## 常见坑与解决

### DNS 泄漏导致仍被目标服务识别地域

**代理协议必须使用 `socks5h://127.0.0.1:1081` 而非 `socks5`。** 采用 `socks5h` 能确保域名解析一并走代理转发。

### SSH 隧道连接静默中断

**连接命令中添加 -o ServerAliveInterval=30 参数保持心跳。** 并在包装脚本中执行命令前先校验隧道连通性。

### 全局代理影响其他本地服务

**仅对指定工具设置代理环境变量而不要开启全局代理。** 可编写包装脚本并在运行真实程序前临时导出 `HTTPS_PROXY` 与 `ALL_PROXY`。

## 来源

- [OpenSSH ssh 手册（-D 动态转发）](https://man.openbsd.org/ssh)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
