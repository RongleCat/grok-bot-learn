---
title: 固定出口代理（SSH 隧道）
sidebar: false
prev: false
next: false
---

# 固定出口代理（SSH 隧道）

<ToolMeta id="egress-proxy" />

固定出口代理利用 SSH 動態埠轉發搭建本地 SOCKS5 代理，適合讓 Bot 在 **訪問受地域限制的服務** 時保持穩定的出口 IP。

## 發給 Bot 的提示詞

複製下方整段內容傳送給你的 Grok Bot，它會在雲電腦上自動安裝並驗證，遇到登入或配置金鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于 SSH 隧道的固定出口代理（https://man.openbsd.org/ssh），以后访问受地域限制的服务用它。需要填服务器地址和私钥时请提醒我自己填。
````

</div>

## 需要你自己做的事

- 準備一臺支援 SSH 金鑰登入的境外伺服器。
- 根據提示自行將登入私鑰與連線資訊寫入私密檔案。

## 來源

- [OpenSSH ssh 手冊（-D 動態轉發）](https://man.openbsd.org/ssh)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)
