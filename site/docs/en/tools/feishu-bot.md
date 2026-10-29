---
title: Feishu Bot Persistent Connection
sidebar: false
prev: false
next: false
---

# Feishu Bot Persistent Connection

<ToolMeta id="feishu-bot" />

A persistent connection messaging solution based on the official Feishu Python SDK, suitable for implementing event listening and group chat bot collaboration on a **Cloud Computer** without requiring a public IP.

## Prompt for the Bot

Copy the entire content below and send it to your Grok Bot. It will automatically install and verify everything on the Cloud Computer, pausing to wait for your action if login or key configuration is required.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于飞书 Python SDK（https://github.com/larksuite/oapi-sdk-python）的长连接机器人，以后接收群聊事件和派发任务用它。需要填密钥时请提醒我自己填。
````

</div>

## What You Need to Do

- Create an internal enterprise app on the Feishu Open Platform and enable persistent connection and bot features.
- Fill in the app's App ID and App Secret yourself when prompted.

## Sources

- [Official Feishu Python SDK (larksuite/oapi-sdk-python)](https://github.com/larksuite/oapi-sdk-python)
- [Feishu Open Platform](https://open.feishu.cn/)

> This page is an unofficial community compilation and is not affiliated with the tool's vendor or xAI. Refer to official documentation for commands.

[← Back to Directory](/tools/)
