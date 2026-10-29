# 第 20 章 可靠的自動化：定時、Webhook 與事件觸發

Routine 每天醒幾十次只回“今日無變化”，額度照扣。**任務缺乏規範極易靜默出錯**。
- 時區偏差（早 9 點跑在凌晨 3 點）
- 週期誤判（預設工作日導致週末漏網）
- 缺少兜底（報錯順著空資料亂改線上）

**兩段式架構配 Linux cron 能砍掉 80% 以上空轉**。寫入邊界合同與安全人閘，打通快捷指令和 X 事件流，自動化才能穩定省錢。


![可靠的自動化：定時、Webhook 與事件觸發](/info/20-automation.png)

## 觸發器選型：到點交付還是等待變化

![觸發器選型：到點交付還是等待變化](/info/20-automation-s1.png)

先分清是到點交差還是等新資料。**Bot 與 Grok、Cursor 共享每週額度池**，高頻輪詢幾天就耗盡。

### 訂閱與配額限制

The X Subscription（2026-10-12）中 Plus 無 Bot，支援檔為 Premium（$30/月或$300/年，4x）、Super（$100/月或$1000/年，15x）、Ultra（$200/月或$2000/年，50x）。

單 Bot 限 50 個 Routine，記錄留 20 次，**定時最短間隔 5 分鐘**。

### 觸發方式與選型

- 定時例程：到點無論有無資料均計費，適合固定日報。
- Webhook：平時零消耗，**僅限帶 Bearer 金鑰的 POST 請求**。
- 第三方事件（GitHub、Slack 等）：有事件才喚醒，繁忙頻道易刷爆額度。
- X 互動（回覆 @bot）：無法解析影片帖，同時 @grok 與 @bot 不觸發。

**等新資料才處理，一律改用 Webhook 或第三方事件。**

## 例程設計模板：寫合同而不是寫頭銜

提示詞只寫頭銜容易跑崩，**生產例程必須寫明執行合同**。

出處見 [《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)，需備齊四要素，涵蓋資料來源、輸出格式，以及缺失報錯與人工審批策略。

### 編寫合同與配置例程

1. **把約束輸入輸出的合同發給 Bot 並讓它記住**；共享 Bot 則寫入詳情 About 的 Description。
```text
负责范围：监控指定数据源并生成标准化 Markdown 摘要。
允许读取的数据源：工作区目录下的 data/incoming/ 文件夹及指定公开 RSS 链接。
输出格式规范：必须输出包含“标题、核心要点（最多3条）、影响评估、原始链接”的 Markdown 结构，存入 docs/daily/ 目录。
数据异常策略：若数据源无更新或文件为空，仅在工作区追加一行日志“[时间戳] NO_NEW_DATA”，严禁编造或推测新闻内容，严禁在聊天窗口发送刷屏提示。
权限边界：只读外部内容与本地写入。禁止调用外部发帖、转账、发送邮件或删除文件操作。
```
2. 聊天中把工作流存為含自檢邏輯的 Skill，直接發指令建定時例程。
```text
每个工作日上午 8:30，运行“晨间资讯归档”Skill。如果数据源没有更新，记录日志后保持沉默。
```
3. 在 Details 的“例程”列表用開關切換 Pause 或 Resume。

   點進面板可改 Instruction、When to run、Webhook，底部支援 Pause/Resume、Test、Edit 與 Delete routine（垃圾桶圖示）。

### 上線前幹跑測試

例程在雲端虛擬機器跑真實操作，**所有 Bot 預設共用底層執行環境且無沙箱隔離**，失控會改動真實檔案。開啟前先在聊天中發指令幹跑驗證。
```text
针对即将上线的例程“晨间资讯归档”，进行一次干跑验证：
1. 复述你理解的执行触发条件与完整业务流程。
2. 列出本次执行涉及读写操作的路径，以及可能产生风险的 3 个最高风险步骤。
3. 说明如果源文件损坏或格式错误，你的具体兜底动作。
现在不要执行任何实际写文件和网络请求操作，仅输出分析报告。
```

### 鎖死安全人閘

前往 Settings 的 Custom Rules（或 Auto-review），**對不可逆動作強制設為手動審批**。

| 攔截指令 | 動作範圍 |
|---|---|
| `send` / `post` | 外發訊息、郵件或社媒 |
| `buy` / `transfer` | 支付與轉賬介面 |
| `delete` / `permissions` | 檔案資料庫刪除、許可權變更 |

指令觸發後系統會彈出審批卡停住執行，持續等待人工確認，絕不自動外發。

## Webhook 接入：移動端與外部流水線打通

出處：[《Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)

### 憑證與狀態

例程選“當 Webhook 被觸發時”，**必須點 Save 才會生成地址、金鑰與 Header**。v0.68.1 若卡片看不全 URL，**讓 Bot 在聊天發連結**複製，金鑰勿發公開群。

**返回 200 僅代表雲端已啟動，不代表執行完畢**。結果去聊天視窗看；非 200 檢查例程是否 Paused 與金鑰。

### 快捷指令

帶分享面板（瀏覽器等）：
1. 勾選“在共享表單中顯示”，接收連結與文字。
2. 用“獲取 URL 內容”發 POST，請求頭填 `Authorization: Bearer <key>`，JSON 體加 `content` 填快捷指令輸入。

```text
接收端 Bot 的配套 Instruction 模板：
收到 Webhook 传入的 JSON 数据后，提取 content 字段中的链接。
如果是普通网页，抓取正文，提炼核心结论与知识点。
整理完成后，以 Markdown 格式追加写入知识库目录下的 inbox.md，包含收录时间、原文链接、核心观点与分类标签。
处理完毕后在聊天中输出一句话确认回执。
```

無分享面板（微信等）：
1. 用“請求文字”接“執行快捷指令”轉發。
2. 繫結 iPhone 15 Pro 操作按鈕或主螢幕，複製後彈窗提交。

**大檔案不能直接塞請求體**。音影片和圖片先傳網盤換公網 URL 再發給 Bot。

## 增量判斷避免空跑：兩段式檢查架構

![增量判斷避免空跑：兩段式檢查架構](/info/20-automation-s4.png)

巡檢每次都跑大模型太費額度，**直接拆成兩段**。

1. 用 Linux 自帶 cron 做機械巡檢。
2. **資料變了**再調 Webhook 叫醒 Bot 處理。

出處：[《Grok Bot 額度再省一點：定時任務極限最佳化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。

### 1. 解耦原理：鬧鐘與大腦分工

Grok Bot 背後是常開的 Linux 雲電腦。

1. **機械檢查**：用 cron 跑指令碼對比資料。期間**絕對不要呼叫任何大模型**，幾秒退出不耗用量。
2. **增量喚醒**：有變動發 POST 到本機 Webhook，喚醒 Bot 分析總結。

把 6 個例程中的等待類改完，耗時約 23 分鐘，每週少 8 到 10 次空轉，延遲從一天降到半小時內。

### 2. 虛擬機器落地配置步驟

1. 在 Bot 上新增一條“增量處理中心”例程，觸發選 Webhook，**儲存好 Webhook URL 和 Bearer 金鑰**。
2. 開啟終端，在工作區建指令碼 `check_update.sh`：

::: details 2. 虛擬機器落地配置步驟
```bash
   #!/bin/bash
   # 监测目标 API 或页面是否有增量变化，纯机械对比，严禁调用 LLM

   TARGET_URL="https://api.example.com/v1/feed"
   STATE_FILE="/home/user/workspace/last_state.hash"
   WEBHOOK_URL="https://your-bot-webhook-url.com/api/v1/run"
   WEBHOOK_KEY="Bearer YOUR_SECRET_KEY"

   # 获取最新数据的哈希值或时间戳
   CURRENT_HASH=$(curl -s "$TARGET_URL" | md5sum | awk '{print $1}')

   if [ ! -f "$STATE_FILE" ]; then
       echo "$CURRENT_HASH" > "$STATE_FILE"
       exit 0
   fi

   OLD_HASH=$(cat "$STATE_FILE")

   # 比对是否有变化
   if [ "$CURRENT_HASH" != "$OLD_HASH" ]; then
       echo "检测到数据更新，正在唤醒 Bot..."
       echo "$CURRENT_HASH" > "$STATE_FILE"
       
       # 叫醒 Bot 进行智能分析
       curl -X POST "$WEBHOOK_URL" \
            -H "Authorization: $WEBHOOK_KEY" \
            -H "Content-Type: application/json" \
            -d '{"event": "data_changed", "source": "feed_monitor"}'
   else
       # 无变化，保持沉默，零额度消耗
       echo "无新变化，退出。"
   fi
   ```
:::

3. 終端安裝並啟動 cron 服務：

```bash
   sudo apt-get update && sudo apt-get install -y cron
   sudo service cron start
   ```

跑 `crontab -e` 設定時（工作日早 9 點到晚 7 點，每 30 分鐘檢查一次）：

```cron
   */30 9-19 * * 1-5 /bin/bash /home/user/workspace/check_update.sh >> /home/user/workspace/cron_check.log 2>&1
   ```

- **客戶端點“更新電腦”會重置系統**：工作區指令碼雖在，但 `apt-get` 裝的 cron 會被抹掉，更新後必須重灌並啟動一次。
- **指令碼別調大模型 API**：只做輕量檢測，把判斷交給模型省不下成本，開銷全轉去 API 計費了。

## 第三方事件與 X 平臺聯動

### Slack 觸發器

Slack 觸發器屬於例程體系，用前需在賬戶繫結 Slack，參考[《Routines 幫助》](https://cursor.com/cn/help/grok-bot/routines)。

- **切勿在公開頻道設“收到任意訊息”觸發**，閒聊一天就會耗盡整週額度。
- 僅監聽 `#alerts-p0` 或 `#deploy-status` 等專屬通知頻道。
- 必須帶觸發字首，如 `!bot review` 或 `@bot summary`。
- 只響應建立後產生的新訊息，不追溯歷史。

### X 平臺聯動邊界

v0.70.2 起無需綁個人賬號即可搜推文。

在推文下評論 @bot 會通知星標主 Bot 分流，參考[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

- 限制：無法解析影片推文；評論同時帶 `@grok` 和 `@bot` 會衝突不觸發。
- 防注入：**主 Bot 僅允許做摘要、分類與入庫，嚴禁自動發帖、點贊或改動雲電腦**，所有對外動作必須退回桌面客戶端人工確認。

## 失敗兜底與容錯策略

![失敗兜底與容錯策略](/info/20-automation-s6.png)

介面超時或返回空資料易腦補，**Instruction 必須包含異常阻斷宣告**：

```text
前置校验步骤：
1. 检查抓取到的内容体积。如果内容为空、包含 HTTP 错误码（如 403、404、500）或少于 50 个字符，判定为源不可用。
2. 源不可用时，立刻终止后续分析流程。
3. 在 workspace/logs/routine_errors.log 中追加一行错误记录，格式：[ISO时间戳] [任务名] SOURCE_UNAVAILABLE [原因]。
4. 不得在公开聊天窗口发送报警消息，不得使用过往缓存伪造新数据，直接以退出状态结束本次 run。
```

Webhook 異常排查：
1. **401**：Header 查 `Authorization: Bearer <key>`，防多出空格換行或用了舊 Key。
2. **404**：核對 URL 完整性，防桌面端誤刪登出。
3. **429**：超併發上限，**必須增加重試佇列與指數退避**。
4. **未執行**：檢查是否被 **Paused**，或手機端 **Active** 開關被關。

**日誌落盤防刷屏**：僅審批攔截才彈卡片通知；摘要寫入 `docs/reports/YYYY-MM-DD.md`，單行日誌追加到 `workspace/run.log`。

## 監控與日常維護

桌面端在 **Details**、手機端在配置檔案裡看例程，**Failed** 能點開看報錯堆疊。

每週查 **Usage & Billing**（v0.70.2 修復了用量顯示），消耗陡增說明有例程在空轉或重試。

每週五固定花 15 分鐘清理例程。
1. 調出 `workspace/run.log` 看實際產出。
2. 連續 7 天無增量的例程先 **Pause**。
3. 停跑兩週無依賴再 **Delete routine**，**刪除不可撤銷且 Webhook 同步失效**。

## 容易踩的坑

- **工作日機制**：設“每天 8 點”常被當成工作日。全天候任務**提示詞必須寫明“包含週六和週日”**。
- **時區偏差**：建 Routine 先去 Settings -> Bot -> Timezone 查時區。雲端預設 UTC，設 9 點會跑在深夜。
- **加號建 Bot 失效**：側邊欄（+）新建容易卡死，不跑就**讓成熟 Bot 對話派生新 Bot**。
- **憑證未儲存**：配 Webhook **必須點底部 Save 簽發**，直接切走頁面會導致金鑰未生成。
- **系統更新重置**：“更新電腦”（Update computer）會初始化映象，`apt-get` 裝的 cron 會丟，**更新後進終端查 cron**。
- **金鑰洩露**：別把 Webhook 金鑰貼進普通聊天。誤發後**立刻刪訊息並在例程重置**。
- **Test 真實執行**：點 **Test** 會消耗用量並改動檔案，**嚴禁在生產資料上測試**。

## 做完怎麼驗收

1. 桌面端看 When to run 裡的英文計劃（如“Every day at 8:00 AM CST”），對準本地時區與週末。
2. 新例程等下個週期才跑，看 Next run 時間準不準。
3. 把資料來源改名或留空，點 Test 跑一次，確認輸出“資料來源異常”日誌且平穩停住，沒瞎編資訊。
4. 注入發郵件、發帖或刪目錄指令，**確認操作被攔截並彈卡片**，沒直接向外發包。
5. 終端用 curl 向 Webhook 發 POST 請求：
```bash
   curl -i -X POST "你的_WEBHOOK_URL" \
        -H "Authorization: Bearer 你的_KEY" \
        -H "Content-Type: application/json" \
        -d '{"test": "ping"}'
   ```
檢查 **1 秒內收到 200 狀態碼**，30 秒內客戶端裡 Bot 變 Running 並輸出回執與結構化結果。

## 延伸閱讀

- 相關章節：[第 8 章 技能與例程：把一次成功變成每天自動跑](/part1/08-skills-routines)
- 相關章節：[第 10 章 額度與成本：讓一週用量撐滿一週](/part1/10-usage)
- 官方文件：[《Cursor Help: Routines》](https://cursor.com/cn/help/grok-bot/routines)
- 社群原文：[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- 社群原文：[《Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- 社群原文：[《Grok Bot 額度再省一點：定時任務極限最佳化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
