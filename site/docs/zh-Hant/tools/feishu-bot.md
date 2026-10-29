---
title: 飛書機器人長連線
sidebar: false
prev: false
next: false
---

# 飛書機器人長連線

<ToolMeta id="feishu-bot" />

基於飛書官方 Python SDK 的長連線訊息方案，適合在無需公網 IP 的 **雲電腦** 上實現事件監聽與群聊機器人協作。

## 發給 Bot 的提示詞

複製下方整段內容傳送給你的 Grok Bot，它會在雲電腦上自動安裝並驗證，遇到登入或配置金鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于飞书 Python SDK（https://github.com/larksuite/oapi-sdk-python）的长连接机器人，以后接收群聊事件和派发任务用它。需要填密钥时请提醒我自己填。
````

</div>

## 需要你自己做的事

- 在飛書開放平臺建立企業自建應用並開啟長連線與機器人功能。
- 根據提示自行填入應用的 App ID 與 App Secret。

## 來源

- [飛書官方 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [飛書開放平臺](https://open.feishu.cn/)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)
