---
title: MCP Connectors
sidebar: false
prev: false
next: false
---

# MCP Connectors

<ToolMeta id="mcp-connectors" />

MCP Connectors establish an interaction channel between external services and the model, making them ideal for enabling the Bot to **directly call external tools and cloud data** to accomplish complex collaboration.

The conclusion is: this tool is used solely to allow the Bot to directly call external tools and cloud data for complex collaboration.

## Prompt to Send to the Bot

Copy the entire text below and send it to your Grok Bot. It will automatically install and verify it on the cloud computer, pausing to wait for your action if it encounters a login or API key configuration.

<div class="tool-prompt">

````text
帮我在你的云电脑上接入 MCP 连接器（https://docs.x.ai/grok/connectors），以后调用外部工具和同步云端数据用它。需要第三方授权时把链接发给我，需要填密钥时请提醒我自己填。
````

</div>

## What You Need to Do

- Visit the connector control page in your browser and prepare the account to connect.
- Enter the address or authorization key of the target service yourself as prompted.

## Sources

- [Grok Official Documentation: Connectors](https://docs.x.ai/grok/connectors)

> This page is an unofficial community compilation and is not affiliated with the tool vendor or xAI. Official documentation prevails for commands.

[← Back to Directory](/tools/)
