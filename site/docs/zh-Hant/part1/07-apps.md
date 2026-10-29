# 第 7 章 連線應用：外掛、郵箱與 Secrets

接入工具記住**先跑通介面，再掛聯結器**。第三方金鑰別往聊天框貼，**存進 Secrets 只寫儲存**防洩露。

- 外掛裝太多會撐大上下文頻繁報錯；原生 X 檢索免外掛就能呼叫。
- 專屬郵箱沒收件箱介面也不彈窗，自動群發會卡在審批卡片。
- 企業環境注意 Zoom 報錯、Google Workspace 攔截與機房 IP 風控。


![連線應用：外掛、郵箱與 Secrets](/info/07-apps.png)

## 接入順序：先跑通介面，再掛聯結器

### 接入步驟
1. 介面操作：**日常事務先在內建瀏覽器跑通**。
2. 官方聯結器：穩定後接 Connect Apps 外掛。
3. 專用指令碼：高頻大吞吐最後調 API 或 CLI。

### 避坑與限制
- 全裝會佔上下文並引發呼叫幻覺。
- **同賬號 Bot 共享雲電腦、瀏覽器與 `/workspace`**，建新 Bot 無法隔離憑據。

### 驗收標準
**靠最小外掛集準確完成任務**，上下文無冗餘工具宣告與誤觸發。

[《4.5 聯結器、Skill、模板與對外入口》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
[《Grok Bot Masterclass｜Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)

## 外掛連線：從商店授權到企業許可權穿透

![外掛連線：從商店授權到企業許可權穿透](/info/07-apps-s2.png)

外掛綁在個人賬戶且全域性生效，**許可權受限於第三方平臺，無法提權**。

| 外掛 | 支援操作 | 限制與避坑 |
|:---|:---|:---|
| **Google Calendar** | 讀寫日程、查空閒與回邀請 | 無法改 Meet 等候室；Zoom 需手動填連結 |
| **Google Drive** | 檢索與讀取檔案 | 改表格需配 Sheets；無法改分享名單 |
| **Google Sheets** | 修改有許可權單元格 | 只讀檔案不可改；檢索由 Drive 處理 |
| **Slack** | 頻道發訊息 | 進不去未加入的私有與禁言頻道；非拉群 Bot |
| **Gmail** | 搜讀發郵件、加標籤 | 僅限單郵箱，個人與企業郵箱不可同綁 |

詳見[連線應用](https://cursor.com/cn/help/grok-bot/connect-apps.md)。

1. 桌面端點側邊欄/聊天卡片「連線」，移動端點頭像選「連線應用」。
2. 搜外掛點「新增」（Add）並在瀏覽器登入授權。
3. 確認進入「已安裝」（Installed）；中斷點「重新連線」重試。

企業 Google 遇攔截換瀏覽器無效，**認證名為「Grok」**。

管理員需在 Google Admin console 經 Security > Access and data control > API controls > App access control > Manage third-party app access 新增「Grok」（或填 Client ID）設為 Trusted。

提示「已被團隊管理員禁用」聯絡 Cursor 管理員後臺開啟。

**在「已安裝」列表無黃色警告，且能正常讀資料、未觸發 OAuth 失敗即成功。**

## Bot 專屬郵箱：認領、收發規則與人閘審批

![Bot 專屬郵箱：認領、收發規則與人閘審批](/info/07-apps-s3.png)

Grok Bot 專屬郵箱（`yourname@mail.grokbot.com`）**歸屬個人賬戶**。私聊與 Routines 可用，不可在 Slack 串或他人會話呼叫，無團隊共享地址。

規則詳見文件[為你的 Bot 設定電子郵箱地址](https://cursor.com/cn/help/grok-bot/agent-email.md)。

### 使用限制與安全

| 專案 | 規則與限制 |
|---|---|
| 地址屬性 | 唯一且永久生效，**無法重新命名或刪除**，登出賬號也不釋放 |
| 發信配額 | 單封最多 50 人；附件最多 10 個（單個 ≤10MB，總量 ≤25MB，禁 `.exe`） |
| 首次外聯 | 限 1 位收件人且正文必帶退訂連結；退信或被標垃圾直接停用 |
| 收信安全 | **無獨立收件箱與通知**，1 分鐘後可查；內容只讀，不執行指令 |

### 認領與配置

團隊須管理員在後臺（`cursor.com/dashboard/bot`）開啟「Agent Email」，個人可直接用。地址限小寫字母、數字及 `.-_`，首尾須為字母數字，最長 64 字元且避開保留詞。

1. 認領地址：側邊欄進「Connect apps」>「Email」建立，或傳送 `claim your email` 及命令：
```text
  给自己申请一个电子邮件地址
  ```
2. 查詢收信：對話中直接檢索：
```text
今天你的收件箱里收到了什么？帮我找出过去一周收到的所有费用账单与回执。
```
3. 配置例程：建 Routine 監聽發件人（支援 `*@example.com`，不支援按主題篩選）：
```text
收到来自 billing@example.com 的电子邮件时，总结其中的账单金额与截止日期，并将摘要整理后发送给我。
```
4. 人閘審批：**系統嚴禁無人值守靜默外發**。Bot 只生成草稿卡片，人工點選「Send」後才真正投遞。

### 驗收標準

外部發測試信後等待 1 分鐘，讓 Bot 查詢並起草回覆。**螢幕彈出待審批卡片且點選前保持掛起**即為成功。

## 安全機密資訊：Secrets 的只寫機制與團隊隔離

![安全機密資訊：Secrets 的只寫機制與團隊隔離](/info/07-apps-s4.png)

**敏感憑證絕不能發在對話方塊、寫進 Shell 配置或錄入「Teach a task」。** 輸入框儲存後變空白是進入了保護狀態。

雲電腦執行 `Recover` 或 `Reset` 不會丟失憑證，詳見[安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets.md)。

### 提交與更新

1. 聊天提交：Bot 索取憑據時彈出安全卡片，輸入框顯示掩碼，點「Save securely」，顯示「Saved」即完成。
2. 團隊 Bot：在設定的「Secrets」點「Add secret」，填名稱（如 `GITHUB_TOKEN`）、描述與金鑰後點「Save secret」。**更新點「Replace」與「Replace value」，系統不支援找回舊值。**
3. 網頁填入：若提示 `Could not fill into the page`，**走 Takeover flow 手動接管登入**，切忌在對話方塊發賬號密碼。

### 驗收標準

- **面板僅顯示名稱與描述，金鑰值完全隱藏。**
- 對話中要明文 Bot 讀不到，但 CLI 或請求鑑權正常透過。

## X 平臺原生檢索：免外掛呼叫社交動態

Grok Bot 在 v0.70.2（2026-10-08）整合了 X 只讀檢索。**它直接走 The X Subscription 統一用量，不用裝第三方外掛，也不用配 API Token**。

1. **直接發自然語言指令**：支援全網搜帖、抓取公開推文正文，也能查賬號發帖與被 @ 記錄，或統計特定話題 7 天互動趨勢。

```text
检索 X 平台账号 @xai 最近 24 小时发布的所有推文。按时间倒序整理每条推文的核心内容、发布时间、点赞数、转推数，并附带原帖链接。
```

```text
检索 X 平台上关于 #AIagents 话题过去 7 天的热门讨论。筛选互动量最高的前 5 条推文，提取核心观点，并汇总该话题本周的讨论热度变化趋势。
```

2. **驗收標準**：**結果要包含釋出時間、互動數字與推文原鏈**，全程沒有聯結器安裝提示，也沒有抓取截斷。

功能梳理見[《4.5 聯結器、Skill、模板與對外入口》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)。

## 安裝開源 Skill 與 CLI 工具：打通本地與終端能力

### 資源邊界

| 作用域 | 包含資源與配置 |
| :--- | :--- |
| **全域性共享** | 所有 Bot 共享已裝 Skill、官方聯結器、共用記憶與 `/workspace` 目錄 |
| **獨立持有** | 各 Bot 獨立持有專屬工作指令、獨立記憶片段與定時例程（Routines） |

體系結構梳理參見[《4.5 聯結器、Skill、模板與對外入口》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)與[《Grok Bot Masterclass｜Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)。

### 核心操作步驟

1. 開啟本地網路流量中繼。雲電腦使用機房 IP，訪問 GitHub 等外部站點容易被攔截。

   在桌面端 Settings -> Computer 勾選「流量經過本地裝置」（Route traffic through this computer），借本機網路中繼，客戶端與雲端需同步更新。
2. 安裝開源 Skill。在對話方塊直接傳送倉庫地址讓 Bot 部署。如需 Access Token，等系統提示後透過安全卡片提交，**嚴禁將 Token 直接貼上在對話方塊中**。

```text
帮我安装这个开源 Skill：https://github.com/example/custom-data-skill
阅读仓库内的说明文档，将其注册为我的可用技能，并告诉我它支持的触发指令与所需参数。
```

3. 獨立登入 Codex CLI。先在網頁端「賬戶安全與登入」開啟「裝置程式碼登入」（Device code login）。在雲端終端執行登入命令，獲取裝置驗證碼並用本機瀏覽器驗證。

   **絕對不要把本機登入憑證複製到雲電腦 `/workspace`**，否則共用快取會導致 Token 重新整理衝突、兩端頻繁掉線。
4. CLI 代理下放重型任務。大批次程式碼格式化或轉碼等機械任務，直接寫成 Shell 指令碼交給雲電腦 CLI 執行。配合「Wake on Done」機制接收完成通知，避免 Bot 長時間佔用高額度推理會話。

### 做到什麼程度算好

- 在雲電腦終端執行 `codex --version` 正常輸出版本資訊，**且本機終端日常使用不會被頂替掉線**。
- 向 Bot 傳送測試任務，能按流程在 `/workspace` 目錄下生成符合交付標準的結構化檔案。

## 容易踩的坑

### 外掛與企業許可權
- Zoom 授權報 4700 屬官方重定向缺陷，客戶端內無法修復。
- Gmail 僅支援單賬號繫結，換綁必須先斷開當前郵箱再重授。
- Google 許可權審批**必須搜「Grok」，不能搜「Cursor」**，換瀏覽器沒用。

### 專屬郵箱與外發審批
- `mail.grokbot.com` 無介面與推送，查信需問 Bot 或建例程；例程僅按發件人和域名監聽（需過 SPF/DKIM），不能按主題篩選。
- 底層設有強行人閘，提示詞無法跳過，發信必須在草稿**手動點選「Send」**。

### 安全與網路環境
- Teach a task 錄屏長達 10 分鐘且無 Secrets 掩碼，別輸入密碼或展示 API Key。
- 所有 Bot 共用儲存與登入態，**機密檔案別丟在 `/workspace`**。
- 拷本地 Token 會互相踢掉線，終端必須走裝置碼獨立授權。
- 外部站點封機房 IP 報錯，去 Computer 頁面**開啟「流量經過本地裝置」**。

## 做完怎麼驗收

1. 側邊欄確認 Drive 和 Sheets 正常。讓 Bot 找 Q3_Report 並用 Sheets 讀表格 A1 到 B10，**能讀出且不報許可權錯**。
2. 用個人郵箱髮帶數字程式碼郵件到 `yourname@mail.grokbot.com`，等 2 分鐘讓 Bot 查收；讓它起草回信，**核對程式碼並點 Send 發出草稿卡片**。
3. 讓 Bot 列印 `GITHUB_TOKEN`，**必須拒絕明文或只給掩碼**；再跑測試命令能過鑑權，確認 Token 未洩漏。
4. 搜 `@xai` 24 小時前兩條高贊推文，**原連結可點且沒調第三方外掛**。
5. 終端跑 `codex --version` 報版本；本地併發**不衝突踢線**；開「流量經過本地裝置」能開啟機房敏感頁。

## 延伸閱讀

### 官方文件與支援頁面

- [連線應用](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- [為你的 Bot 設定電子郵箱地址](https://cursor.com/cn/help/grok-bot/agent-email.md)
- [安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets.md)
- [Grok Bot 電腦](https://cursor.com/cn/help/grok-bot/computer-recovery.md)
- [例程](https://cursor.com/cn/help/grok-bot/routines.md)
- [團隊 Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- [面向 Teams 和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams.md)

### 社群實戰資料

- 《4.5 聯結器、Skill、模板與對外入口》：[飛書知識庫文件](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
- 《Grok Bot Masterclass｜Avi Chawla》：[飛書知識庫文件](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)
