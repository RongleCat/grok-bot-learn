---
title: X API Posting (OAuth 1.0a PIN)
sidebar: false
prev: false
next: false
---

# X API Posting (OAuth 1.0a PIN)

<ToolMeta id="x-api" />

An official X API integration solution based on OAuth 1.0a PIN authorization, suitable for allowing the Bot to securely execute posting, image uploading, and post deletion tasks on a **cloud computer**.

The conclusion is: This tool is only used to allow the Bot to post, upload images, and delete posts on a cloud computer.

## Prompt to Send to the Bot

Copy the entire content below and send it to your Grok Bot. It will automatically install and verify it on the cloud computer, pausing to wait for your action when login or key configuration is required.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置 X API 发帖（https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth），以后发帖、传图和管理推文用它。需要填密钥时请提醒我自己填，需要登录授权时把链接发给我。
````

</div>

## What You Need to Do Yourself

- Create an application on the X Developer Platform and enable read and write permissions.
- Open the authorization link and send the PIN code from the page to the Bot.

## Sources

- [X Official Documentation: PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> This page is an unofficial community compilation and has no affiliation with the tool vendor or xAI. Commands are subject to official documentation.

[← Back to Directory](/tools/)
