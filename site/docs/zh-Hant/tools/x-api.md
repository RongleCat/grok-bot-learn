---
title: X API 發帖（OAuth 1.0a PIN）
sidebar: false
prev: false
next: false
---

# X API 發帖（OAuth 1.0a PIN）

<ToolMeta id="x-api" />

基於 OAuth 1.0a PIN 授權的 X 官方介面呼叫方案，適合讓 Bot 在 **雲電腦** 上安全執行發帖、傳圖與刪帖任務。

結論是：該工具僅用於讓 Bot 在雲電腦中發帖、傳圖與刪帖。

## 發給 Bot 的提示詞

複製下方整段內容傳送給你的 Grok Bot，它會在雲電腦上自動安裝並驗證，遇到登入或配置金鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上配置 X API 发帖（https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth），以后发帖、传图和管理推文用它。需要填密钥时请提醒我自己填，需要登录授权时把链接发给我。
````

</div>

## 需要你自己做的事

- 在 X 開發者平臺建立應用並開通讀寫許可權。
- 開啟授權連結並在收到頁面 PIN 碼後傳送給 Bot。

## 來源

- [X 官方文件：PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)
