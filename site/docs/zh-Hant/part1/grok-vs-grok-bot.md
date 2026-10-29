# Grok 和 Grok Bot 有什麼區別

**Grok 是對話助手，Grok Bot 是在雲電腦上替你幹活的常駐 AI 同事。**
Grok 負責你問我答，關閉網頁或 App 對話即結束；Grok Bot 則在獨立雲電腦裡常駐，關掉客戶端後臺任務依然照跑。
兩者都來自 xAI（現名 SpaceXSI），但在互動形態與應用定位上完全不同。

## Grok 和 Grok Bot 的核心區別是什麼？

**核心區別在於 Grok 只動嘴給建議，而 Grok Bot 會在雲電腦裡實際動手操作。**
Grok 是純粹的對話助手，你問一句它答一句；Grok Bot 則是 2026 年 8 月 11 日由 xAI 和 Cursor 推出的常駐 AI 同事，目前仍是 Beta。
想要建立整體概念，可以先閱讀[第 1 章 Grok Bot 是什麼](/part1/01-what-is)。

| 維度 | Grok | Grok Bot |
| --- | --- | --- |
| 是什麼 | xAI 的 AI 對話助手 | 一組常駐的 AI 同事（AI teammates），目前處於 Beta |
| 在哪用 | grok.com 網頁、iOS 和 Android App、X 裡的 Grok 標籤頁 | macOS、Windows、Linux 桌面端，iPhone、iPad、Android 移動端 |
| 怎麼幹活 | 你問一句它答一句，支援文字、語音、上傳檔案分析、生圖生影片等 | 用打字或語音發訊息交代任務，在帶瀏覽器、檔案系統和終端的常駐雲電腦上跨應用幹活，需批准時才找你 |
| 關掉後還跑不跑 | 不跑，用完關掉網頁或 App 對話就結束 | 照樣跑，合上筆記本、關掉 App，後臺任務和例程繼續跑 |
| 能不能操作網站和軟體 | 不能，不替你在別的網站和軟體裡動手幹活 | 能，登入常用網站和應用把活幹完，敏感步驟由人點 Take over 接管 |
| 需要哪檔訂閱 | 免費可試用，訂閱提高額度；包含在 The X Subscription 免費檔、Plus 檔及以上 | 包含在 The X Subscription 的 Premium、Super、Ultra；Plus 不含 |
| 適合的事 | 即時問答、查報錯、寫一段文字、生圖生影片、看 X 最新動態 | 流程固定、高頻重複、跨多網站或軟體的活（如巡檢官網、每週對賬、彙總晨報、復現 Issue） |

**同一賬號的所有 Bot 共用一臺雲電腦，共享檔案、瀏覽器登入態和應用登入。**
每個 Bot 雖然有自己的螢幕，但官方提醒不要把不同 Bot 當成安全隔離，具體執行機制見[第 5 章 共享雲電腦](/part1/05-computer)。
若需配置環境，可以參考[第 3 章 安裝登入與第一個 Bot](/part1/03-install)。

## 什麼時候用 Grok，什麼時候用 Grok Bot？

**幾秒內能給結果的即時問答用 Grok，需要跨軟體、定時跑或多步執行的重複事務用 Grok Bot。**

**適合用 Grok 的場景，集中在即時問答與單次內容生成。**
比如查報錯、寫一段文字、生圖生影片（影片最長 15 秒），或者實時聯網搜尋網頁和 X 的最新動態。
這類任務幾秒鐘就能搞定，不用動用雲電腦。

**適合用 Grok Bot 的場景，主要是流程固定、高頻重複且跨多個網站或軟體的繁雜工作。**
典型任務包括定期巡檢官網出摘要、每週對賬、每天彙總晨報、讀 Issue 復現缺陷等。
這類工作必須能由人核驗結果，高危動作（發信、付款、刪除）會停下來等待批准，遇上輸密碼、兩步驗證、驗證碼或付款時可以點 Take over 人工接管。

一次跑通的流程還能存成技能，並設成例程定時自動跑，多個 Bot 也可以在群聊裡協作交接。
**需要留意的是，高頻輪詢和影片處理等任務會迅速消耗每週額度。**
關於額度規劃和消耗細節，建議提前檢視[第 10 章 額度與成本](/part1/10-usage)。

## 用 Grok Bot 需要買哪檔訂閱？

**使用 Grok Bot 至少需要每月 30 美元的 Premium 方案，8 美元的 Plus 檔並不包含 Grok Bot。**

自 2026 年 10 月起，官方推出了 The X Subscription 統一訂閱方案，把 Grok、Grok Bot、Cursor 和 X Premium 整合在一起。
該訂閱分為五檔：Free（$0）、Plus（$8/月）、Premium（$30/月）、Super（$100/月）與 Ultra（$200/月）。

**Grok 在免費檔和 Plus 檔就能使用，而 Grok Bot 僅對 Premium、Super、Ultra 開放。**
付費檔每週提供一個共享額度池，由 Grok、Grok Bot 以及 Cursor 裡的 Grok 模型共同使用。

**老使用者也可以直接使用 Grok Bot。**
擁有老的 Cursor 付費個人版、Cursor 團隊版，或者關聯了 SuperGrok、SuperGrok Plus、SuperGrok Heavy 的賬號，都能直接使用 Grok Bot。
更詳細的訂閱權益，可以查閱[第 2 章 方案與訂閱](/part1/02-plans)。

## 延伸閱讀

本站章節：
- [第 1 章 Grok Bot 是什麼](/part1/01-what-is)
- [第 2 章 方案與訂閱](/part1/02-plans)
- [第 3 章 安裝登入與第一個 Bot](/part1/03-install)
- [第 5 章 共享雲電腦](/part1/05-computer)
- [第 10 章 額度與成本](/part1/10-usage)

官方頁面：
- [Grok 官方頁面](https://x.ai/grok)
- [Grok Bot 釋出公告](https://x.ai/news/introducing-grok-bot)
- [Grok Bot 官方概覽文件](https://docs.x.ai/grok-bot/overview)
- [The X Subscription 訂閱文件](https://docs.x.ai/x-subscription/grok-bot)
