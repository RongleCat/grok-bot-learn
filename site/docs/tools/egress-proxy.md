---
title: 固定出口代理（SSH 隧道）
sidebar: false
prev: false
next: false
---

# 固定出口代理（SSH 隧道）

<ToolMeta id="egress-proxy" />

固定出口代理利用 SSH 动态端口转发搭建本地 SOCKS5 代理，适合让 Bot 在 **访问受地域限制的服务** 时保持稳定的出口 IP。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于 SSH 隧道的固定出口代理（https://man.openbsd.org/ssh），以后访问受地域限制的服务用它。需要填服务器地址和私钥时请提醒我自己填。
````

</div>

## 需要你自己做的事

- 准备一台支持 SSH 密钥登录的境外服务器。
- 根据提示自行将登录私钥与连接信息写入私密文件。

## 来源

- [OpenSSH ssh 手册（-D 动态转发）](https://man.openbsd.org/ssh)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
