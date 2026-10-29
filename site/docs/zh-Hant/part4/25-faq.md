# 第 25 章 常見問題與排錯

遇到報錯或卡頓，**千萬別盲目重灌或重置**，這會沖掉剛寫好的環境和臨時指令碼。

1. **先看服務狀態**。
2. 再排查是本地網路、外掛授權、雲端環境還是每週額度的問題。


![常見問題與排錯](/info/25-faq.png)

## Grok Bot 登入與繫結賬號出問題怎麼辦？ {#登入與身份驗證}

**個人使用者透過設定頁面或專用連結關聯授權，企業席位直接用 Grok 登入，若綁錯需找人工客服，遇迴圈跳回可清 Cookie 用無痕模式認證。**

### 賬號與訂閱限制
Grok Bot 依託 Cursor 執行，與 Grok 手機端付費牆及每週額度限制（Weekly SuperGrok Limit）無關。

個人版支援 SuperGrok 與 Plus、Heavy 版本，以及 X Premium+；SuperGrok Lite 與 Grok Enterprise 無法關聯個人賬戶，企業席位由管理員統一分配。

**賬戶郵箱註冊後無法修改，關聯 Cursor 是一次性永久繫結**。綁錯賬號無法自行轉移，必須聯絡人工客服處理。

### 繫結與登入步驟
1. 個人繫結：開啟 [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) 或在客戶端進入 **設定** > **用量和計費**，在 **管理方案** 下點選 **透過 Grok 獲取訪問許可權**（僅在能提升當前用量層級時顯示）。
2. 企業席位：擁有 Grok Business 席位無需在方案頁手動繫結，完全退出後在登入頁點選 **Sign in with Grok** 即可。
3. 服務確認：遇到異常先訪問 [status.cursor.com](https://status.cursor.com) 檢視 **Grok Bot** 實時狀態，操作要求詳見[登入 Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in)。

   **服務故障時等待官方修復，切勿重灌應用或重置電腦**。

### 故障排查與驗收
客戶端版本過舊會引發協議不匹配；突發認證故障建議靜置 30 到 60 分鐘再試。**驗收標準是賬號郵箱、訂閱歸屬與客戶端登入狀態一一對應**。

| 故障現象 | 正確處置路徑 | 嚴禁操作 |
| :--- | :--- | :--- |
| 迴圈跳回登入頁 | 清理 `cursor.com` 與 `x.ai` 的 Cookie，用桌面端無痕模式認證 | 連續解除安裝重灌客戶端 |
| 找不到關聯入口 | 確認當前賬號層級低於待繫結方案，未達上限 | 註冊新賬號重複購買 |
| 提示 Model provider is overloaded | 複製報錯的 Request ID，等待 2 分鐘重新傳送 | 立即點選 Reset 重置電腦 |
| 提示郵箱需變更 | 重新註冊賬號並遷移資產 | 嘗試在設定中強改繫結郵箱 |

向 Bot 傳送提示詞確認登入狀態。
```text
请检查当前运行环境的网络连通性与 Cursor 身份验证状态，汇报当前登录的用户环境标识，但不要输出任何敏感 Token。
```

## Grok Bot 連不上雲端電腦該如何恢復？ {#雲端電腦與環境恢復}

**遇到斷連可先等兩分鐘重試或徹底重啟應用，卡死時點 Recover 存現場重建，而會覆蓋快照丟失未同步修改的 Reset 只能作最後兜底手段。**

![雲端電腦與環境恢復](/info/25-faq-s2.png)

所有 Bot 共享同一臺雲端電腦。**對話記錄獨立存在資料庫**，崩潰清空都不丟。

提示 Reconnecting、Couldn't Reach Grok Bot's Computer 或 Bot failed to respond 時：
1. 等 1 到 2 分鐘點 Retry。
2. 徹底退出應用。Mac 按 `Cmd+Q`，Win/Linux 退出托盤，別隻關視窗。
3. 進設定 > 計算機點更新。備份未完或 Bot 工作時切勿中斷。
4. 卡住點 Recover。
5. **Reset 是最後手段**。快照覆蓋會丟未同步修改。詳見[Grok Bot 電腦](https://cursor.com/cn/help/grok-bot/computer-recovery)。

|操作|現場儲存|環境影響|場景|
|---|---|---|---|
|Retry|原樣保留|無影響|網路抖動|
|Update|等備份完|全留軟體；整機清自裝包|官方補丁|
|Recover|存現場建機|移除自裝應用與環境|卡死損壞|
|Reset|快照覆蓋|丟未同步修改|連不上兜底|

**電腦狀態變綠顯示已連線**、終端正常且配置完整就算修好。

- 遇到 SSO 登入，點卡片上的 Take over 手動驗證，搞定點 I'm done。
- 金鑰與網路：在設定 > General > Security Key 開 Use hardware security keys 插 YubiKey；遇驗證碼在設定 > 計算機勾“透過此計算機路由流量”。
- 本地執行：在設定 > 計算機開“在此計算機上執行”（跑命令先確認）。詳見[Grok Bot 設定](https://cursor.com/cn/docs/grok-bot/settings)。
- 磁碟告警：報 Computer is low on disk space 時點 Go to Disk Saver，**必須人工確認才刪**。

```text
请检查当前云端计算机根目录与工作目录的磁盘占用情况，找出体积超过 200MB 的文件与缓存目录，列出清单供我确认，不要擅自执行任何删除命令。
```

## Grok Bot 自動化例程不觸發該怎麼排錯？ {#例程管理與自動化排錯}

**例程無動靜先確認狀態非暫停並校對時區與 Test 測試，Webhook 需帶鑑權金鑰且 200 僅代表入隊，Slack 觸發必須限定頻道白名單與過濾詞。**

![例程管理與自動化排錯](/info/25-faq-s3.png)

例程在雲端自動跑，關機也生效，支援定時、Webhook 與 Slack 推送。

1. **查狀態與時區**：Details 確認非 **Paused**（手機看 **Active**）；在“設定 > Bot > Timezone”手動選時區，跨國別用 Auto-detect。
2. **定時觸發時機**：只等下個週期（09:05 設 09:00 明早跑），即時測邏輯點 **Test**。
3. **校驗 Webhook**：POST 帶 `Authorization: Bearer <key>`。**200 僅代表入隊**，結果去聊天視窗看；非 200 為金鑰錯或暫停。
4. **收窄 Slack 觸發**：**必須限頻道與過濾詞**，防閒聊幾小時燒光配額。詳見[例程](https://cursor.com/cn/help/grok-bot/routines)。

手機端“執行歷史”查 **Running**、**Succeeded**、**Failed**；顯示 **No runs yet** 為未觸發。

| 故障 | 原因 | 修復 |
|---|---|---|
| 無動靜 | Paused/未到點/時區偏差 | 查 Active，點 Test，校對 Timezone |
| 401/403 | 漏 Token/金鑰重置/例程已刪 | 重新複製 header 覆蓋配置 |
| Slack 無回應 | 舊訊息/頻道或詞未命中 | 只認新訊息，核對頻道白名單與短語 |
| 配額消耗快 | 間隔過短/大群無過濾詞 | 暫停例程，拉長間隔，限定運維頻道 |

建立與修正自動化例程提示詞：
```text
请修改名为“工单同步”的例程：仅在 #ops-alert 频道出现包含“[P0-Error]”文字的新消息时才触发，忽略其他日常聊天，并列出更新后的 When to run 描述。
```

## 用量異常與配額控制

![用量異常與配額控制](/info/25-faq-s4.png)

Grok Bot 配額按周重置。基礎額度用完會中斷回覆，**這屬於正常的配額熔斷**。一次性試用額度跑複雜任務耗盡後無法恢復。

### 操作與防坑
1. 恢復額度：等每週重新整理，或在 **設定** > **用量和計費** 開按需用量，也可升訂閱。
2. 設定封頂：客戶端或網頁 [cursor.com/dashboard](https://cursor.com/dashboard) 設限。**在跑任務不強切，扣費微超幾個百分點屬正常。**
3. 額度對齊：外部賬號不疊加取高者（Pro 對應 SuperGrok/X Premium+，Pro+ 對應 SuperGrok Plus，Ultra 對應 SuperGrok Heavy）。
4. 移動端退訂：多端共享訂閱。商店付款需在 Apple ID 或 Google Play 退，官方不直退，見[方案和計費](https://cursor.com/cn/help/grok-bot/plans)。

### 驗收標準
| 場景 | 操作 | 邊界與坑點 |
| :--- | :--- | :--- |
| 防超額 | 客戶端或控制檯設月度限額 | **封頂拒新請求，在跑任務跑完才停** |
| 查用量 | Bot 內部設定查實時剩餘 | 外部 Grok 看板不互通 |
| 試用清零 | 排查大工程掃描或重構 | 一次性耗盡不恢復 |

```text
请列出你当前账号下所有处于活跃状态的例程，评估它们各自的执行频率与触发条件，指出哪一个例程最容易引发高额用量消耗。
```

## 群聊、協作與輔助 Bot 治理

輔助 Bot 會進側邊欄並彈通知，改檔案或連外網會觸發 **Auto-review** 審批。

### 操作與審批
1. 降噪隱藏：桌面端右鍵選 Hide from sidebar 或發指令關通知；手機端進配置關通知。
2. 恢復誤藏：桌面在 **隱藏的機器人** 選 Show in sidebar，手機選 Unhide。**嚴禁為找 Bot 去點雲端 Recover 或 Reset。**
3. 審批與白名單：高頻操作點 **始終允許**（存入 設定 > Bot > 自定義規則）；衝突先詢問，顯示“由管理員強制要求”的不可跳過。

   規範見 [Grok Bot 操作指南](https://cursor.com/cn/help/grok-bot/how-to)。

### 驗收標準
側邊欄無雜亂 Bot，日常高頻**免打擾自動透過**。

|場景|超時|表現|對策|
|---|---|---|---|
|前臺人工|永久等待|持續掛起|核對後允許或拒絕|
|後臺/Webhook|約 10 分鐘|變 Expired 取消|配“始終允許”或開通知|
|管理員強制|視場景|無法跳過|必須人工授權|

```text
请梳理我们在此会话中频繁执行的文件读取与构建指令，为它们生成一组最小权限的安全规则建议，以便我添加到 Auto-review 的自定义白名单中。
```

## 外掛與外部應用連線

### 授權排錯
**Added 只表示已安裝，不等於已登入**。卡片沒彈去側邊欄手動驗證。**授權須在 10 分鐘內完成**，超時點 Reopen；持續報錯點 Remove 刪掉重灌。

| 狀態 | 處理 |
| :-- | :-- |
| **Added / Needs auth** | 點「驗證身份」去瀏覽器登入 |
| **Connected 報錯** | 傳送帶外掛名的指令重新整理會話 |
| **Disabled by team admin** | 找團隊管理員解禁 |

### 多賬號與驗收
1. **多賬號**：在「連線應用」> 外掛 > Accounts 點 **Add Another Account**（手機端點 Authorize new account）並打標籤。對話指明標籤呼叫；無按鈕則僅支援單賬號。
2. **驗收**：**狀態顯示綠色 Connected 且標籤清晰**，發指令能一次準確呼叫。

詳見[連線應用](https://cursor.com/cn/help/grok-bot/connect-apps.md)。

```text
请刷新当前已连接的插件列表，使用带有“工作”标签的账户连接，读取最近更新的 3 个页面，确认授权是否正常。
```

## 賬號登出與資料清理

Grok Bot 共用 Cursor 賬號，**刪號不可逆**，無法單獨保留 Cursor。換電腦用直接退出登入或解除安裝就行。

### 終端登出步驟
登出前務必取消自動續費，避免賬單糾紛。
1. 手機端（iOS/Android）：點頭像進“設定” > 賬戶資訊 >“刪除賬戶”，網頁驗證中鍵入“**刪除**”兩字確認。
2. 桌面與網頁端：**客戶端無法直接登出**。登入 [cursor.com/dashboard](https://cursor.com/dashboard) >“設定” >“更多” >“刪除賬戶”確認。
3. 企業或團隊席位：個人無法獨立登出，必須聯絡管理員解綁或提工單。條款見[刪除你的 Grok Bot 賬戶](https://cursor.com/cn/help/grok-bot/delete-account)。

### 資產清理與避坑
| 資產與訂閱 | 處置結果 | 必做處理 |
| :--- | :--- | :--- |
| 雲端對話與環境 | **30 天內**物理擦除，快照銷燬 | 提前匯出程式碼和對話，下載檔案 |
| 本地檔案 | 完好無損 | 無需處理 |
| 商店與 X 獨立訂閱 | **不會自動取消** | 需去 Apple、Google 或 x.ai 手動退訂 |

## 獲取官方支援與工單規範

### 怎麼做
本地排查沒用時，發郵件到 **hi@cursor.com**。**別隻發“我的 Bot 壞了”這類模糊描述**，郵件裡帶齊這六項。

1. 賬號憑證：註冊郵箱。
2. 執行環境：平臺與客戶端版本號。從賬戶選單 > 支援 > 關於，點 Copy version info 複製。
3. 準備執行的操作：說明故障前想跑什麼任務。
4. 真實報錯憑據：完整錯誤彈窗、控制檯報錯或計費截圖。
5. 排查記錄：寫明做過哪些排查，避免客服給重複建議。
6. Request ID：右鍵報錯訊息或懸停點 More message actions 選 Copy request ID。若沒有該項，必須附原始報錯文字與全屏截圖。

Linux 若彈 Update required 且自動更新失敗，按發行版在終端執行更新指令：
- Debian / Ubuntu：`sudo apt update && sudo apt install --only-upgrade grok-bot`
- Fedora / RPM 系列：`sudo dnf upgrade --refresh grok-bot`

::: details 怎麼做
```text
收件人：hi@cursor.com
主题：【Grok Bot 故障申报】云端电脑持续重连且 Recover 失败 - [你的账号邮箱]

支持团队：
我的账号遇到了云端电脑无法连通的故障，无法正常执行任务，以下是详细环境与排查信息：

1. 账号邮箱：developer@example.com
2. 版本信息：Version 1.2.4 (Channel: stable, OS: Darwin x64 23.4.0)
3. 故障发生场景：我尝试让 Bot 运行自动化部署脚本，终端在拉取镜像时中断。
4. 核心报错信息：界面持续提示“Couldn't Reach Grok Bot's Computer”，伴随“Bot failed to respond”。
5. 已尝试的排错操作：
   - 已彻底 Quit 应用并重启；
   - 尝试在“设置 > 计算机”执行 Update，提示备份未就绪；
   - 尝试点击 Recover，重试一次后依然在进度条处卡住报错；
   - 查看 status.cursor.com 确认官方各项服务状态正常。
6. 请求 ID (Request ID)：req_98af7c32e01b44d7a1
7. 附件：包含当前报错卡片截图及“设置 > 计算机”面板状态截图。

请协助在后台检查该实例的宿主节点状态，谢谢。
```
:::

### 做到什麼程度算好
**發信後能收到自動回執，且技術無需二次追問即可調出日誌**。詳細規範見[獲取幫助](https://cursor.com/cn/help/grok-bot/get-help.md)。

## 典型故障排錯案例

### 案例一：雲端電腦 Reconnecting 迴圈
報 Couldn't Reach Grok Bot's Computer 時，**千萬別先點破壞性的 Reset**。
1. 訪問 [status.cursor.com](https://status.cursor.com) 確認服務正常，按 `Cmd+Q` 重啟應用。
2. 進設定 > 計算機，若提示未及時暫停，等約 5 分鐘讓後臺超時。
3. 待 Recover 電腦亮起後點選恢復並重跑安裝指令碼，**保全歷史指令碼與登入態**。

### 案例二：Slack 觸發器用量雪崩
因監聽 3000 多人的 `#general` 全量閒聊，每週用量在 24 小時內歸零。
1. **先在支出面板設死按需月度限額**，防止信用卡扣費。
2. 將例程切為 Paused 止血。
3. 規則收窄為“僅在 `#bot-help` 且被 `@Grok` 時觸發”。
4. 點 Test 單次驗證後再恢復上線。

### 案例三：Notion 認證失效與接管登入
Notion 報 Action needed 且 Okta SSO 攔截時，**必須用 Take over 在內建瀏覽器閉環認證**。
1. 見 Needs auth 提示後，點選卡片中的 Take over 接管。
2. 在雲端內建瀏覽器輸工號過二次驗證，點 I'm done。
3. 在 Accounts 點 Add Another Account 授權個人空間，**打上“個人庫”標籤防憑證衝突**。

## 容易踩的坑

1. 丟聊天別點 Reset，會抹掉程式碼。找回先**退出重啟**，核對 Cursor 賬號或看隱藏機器人。
2. 14:05 設 14:00 例程次日才跑，測邏輯點 **Test**。
3. Slack 大群無觸發詞監聽，打招呼會**燒光整週額度**。
4. 刪 App 仍會扣費，退訂去 **Apple ID 或 Google Play** 訂閱中心取消。
5. Updating 時點 Reset 會**損壞檔案系統**，只能找人工。
6. 外掛 Added 需確認 **Connected**；顯示 Needs auth 需瀏覽器授權。
7. 更新、Recover 或 Reset 清空 `node_modules` 與 `.venv`，依賴寫進**初始化指令碼**。
8. 審批卡片 **10 分鐘後 Expired 終止**，記得開通知或設“始終允許”。

## 做完怎麼驗收

- 查 [status.cursor.com](https://status.cursor.com) 無故障且郵箱正確。
- 進設定 > 計算機看綠燈，給 Bot 發基礎 Linux 命令測回包。
- 例程保持啟用，核對 When to run 時區，點 Test 跑通。
- 進設定 > 用量與計費，**必須設定按需用量月度限額**防天價賬單。
- 連線應用顯 Connected，寫操作能彈 Auto-review 且手機有推送。
- 工單隻留 Request ID 和 Copy version info，**切勿洩露 Bearer Token 請求頭**。

## 延伸閱讀

- 相關章節：[第 5 章 共享雲電腦：檔案、瀏覽器與接管](/part1/05-computer)
- 相關章節：[第 10 章 額度與成本：讓一週用量撐滿一週](/part1/10-usage)
- [Grok Bot 常見問題官方解答](https://cursor.com/cn/help/grok-bot/faqs)
- [Grok Bot 操作與排錯指南](https://cursor.com/cn/help/grok-bot/how-to)
- [Grok Bot 電腦環境管理與災難恢復](https://cursor.com/cn/help/grok-bot/computer-recovery)
- [自動化例程與觸發器詳細配置](https://cursor.com/cn/help/grok-bot/routines)
- [賬號體系與登出說明](https://cursor.com/cn/help/grok-bot/delete-account)
- [支援團隊聯絡與工單規範](https://cursor.com/cn/help/grok-bot/get-help)
- [Grok Bot 系統全域性設定參考](https://cursor.com/cn/docs/grok-bot/settings)
