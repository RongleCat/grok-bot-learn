---
title: 飞书机器人长连接
sidebar: false
prev: false
next: false
---

# 飞书机器人长连接

<ToolMeta id="feishu-bot" />

基于飞书官方 Python SDK 的长连接消息方案，适合在无需公网 IP 的 **云电脑** 上实现事件监听与群聊机器人协作。

结论是：适合在无公网IP的云电脑上，基于长连接实现飞书事件监听与群聊协作。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于飞书 Python SDK（https://github.com/larksuite/oapi-sdk-python）的长连接机器人，以后接收群聊事件和派发任务用它。需要填密钥时请提醒我自己填。
````

</div>

## 需要你自己做的事

- 在飞书开放平台创建企业自建应用并开启长连接与机器人功能。
- 根据提示自行填入应用的 App ID 与 App Secret。

## 来源

- [飞书官方 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [飞书开放平台](https://open.feishu.cn/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
