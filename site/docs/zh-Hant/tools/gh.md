---
title: GitHub CLI（gh）
sidebar: false
prev: false
next: false
---

# GitHub CLI（gh）

<ToolMeta id="gh" />

GitHub 官方命令列工具，適合讓 Bot 在 **雲電腦** 上克隆私有倉庫、推送程式碼、建立 PR 並管理 Actions。

結論是：該工具僅用於讓 Bot 在雲電腦克隆 GitHub 私有倉庫、推送程式碼、建立 PR 並管理 Actions。

## 發給 Bot 的提示詞

複製下方整段內容傳送給你的 Grok Bot，它會在雲電腦上自動安裝並驗證，遇到登入或配置金鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
帮我在你的云电脑上安装 GitHub CLI（https://github.com/cli/cli/blob/trunk/docs/install_linux.md），以后管理代码仓库、推送分支和提交 PR 用它。需要登录或授权时停下来把链接发给我由我完成。
````

</div>

## 需要你自己做的事

- 準備 GitHub 賬號。
- 在瀏覽器開啟授權連結並輸入對應的一次性驗證碼。

## 來源

- [GitHub CLI Linux 安裝文件](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 官方手冊](https://cli.github.com/manual/gh_auth_login)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)
