---
title: Fixed Egress Proxy (SSH Tunnel)
sidebar: false
prev: false
next: false
---

# Fixed Egress Proxy (SSH Tunnel)

<ToolMeta id="egress-proxy" />

A fixed egress proxy uses SSH dynamic port forwarding to set up a local SOCKS5 proxy, suitable for keeping a stable egress IP when the Bot **accesses geo-restricted services**.

## Prompt for the Bot

Copy the entire text below and send it to your Grok Bot. It will automatically install and verify it on the cloud computer, and will pause to wait for your action when login or key configuration is required.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于 SSH 隧道的固定出口代理（https://man.openbsd.org/ssh），以后访问受地域限制的服务用它。需要填服务器地址和私钥时请提醒我自己填。
````

</div>

## What You Need to Do Yourself

- Prepare an overseas server that supports SSH key login.
- Follow the prompts to write the login private key and connection information into a private file yourself.

## Sources

- [OpenSSH ssh manual (-D dynamic forwarding)](https://man.openbsd.org/ssh)

> This page is an unofficial community compilation and is not affiliated with the tool vendor or xAI. Commands are subject to the official documentation.

[← Back to Directory](/tools/)
