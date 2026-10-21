---
title: 固定出口代理（SSH 隧道）
sidebar: false
prev: false
next: false
---

# 固定出口代理（SSH 隧道）

<ToolMeta id="egress-proxy" />

固定出口代理利用 SSH 动态端口转发搭建本地 SOCKS5 代理，适合让 Bot 在**访问受地域限制的服务**时保持稳定的出口 IP。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
请你在云电脑中建立 SSH 动态转发隧道并配置 SOCKS5 出口代理环境变量。

1. 目标：开通基于 SSH 的固定出口 SOCKS5 代理隧道并配置网络代理环境。
2. 参考命令：
- 启动后台隧道：ssh -fN -o ServerAliveInterval=30 -D 127.0.0.1:1081 user@your-vps
- 配置代理环境变量：export HTTPS_PROXY=socks5h://127.0.0.1:1081 ALL_PROXY=socks5h://127.0.0.1:1081 NO_PROXY=localhost,127.0.0.1
3. 密钥与授权原则：遇到登录、授权、填密钥等只能我来做的步骤时（如连接 VPS 所需的 SSH 凭证），请先停下，请我将私钥填入本地私密文件并把权限设为 600，不要让我把私钥贴进聊天，不要打印密钥。
4. 常见坑及处理办法：
- 代理协议必须使用 socks5h 而不是 socks5，以确保 DNS 解析同步走代理。
- 隧道可能因空闲断开，命令中需保留 -o ServerAliveInterval=30 保持心跳；也可以为特定工具编写包装脚本，在调用前检查隧道并在必要时拉起，同时支持环境变量开关绕过代理。
- SSH 私钥必须存放在本地私密目录且权限设为 600。
- 仅代理需要的工具，切勿开启全局代理，避免影响其他正常网络连接。
5. 安装完成标准：执行验证命令 curl --proxy socks5h://127.0.0.1:1081 https://ifconfig.me，预期结果为返回你所连接的海外 VPS 实际出口 IP 地址。
6. 执行完成后，用几句话向我汇报配置与验证结果。
````

</div>

## 需要你自己做的事

- 准备一台受目标服务支持且可通过 SSH 密钥登录的海外 VPS
- 将 VPS 的 SSH 登录私钥存放在云电脑私密文件并设权限为 600
- 将命令中的 user@your-vps 替换为真实的 VPS 用户名及 IP

## 来源

- [OpenSSH ssh 手册（-D 动态转发）](https://man.openbsd.org/ssh)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
