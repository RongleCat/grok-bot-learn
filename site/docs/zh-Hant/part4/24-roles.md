# 第 24 章 按崗位組建你的 AI 團隊

**別把 Grok Bot 當普通聊天框或全包助手。** 雜活全塞進同個會話會導致上下文膨脹、變慢並浪費額度，夜間無人盯梢時還容易誤發郵件、改動生產程式碼或劃扣資金。

Grok Bot 底層是帶獨立瀏覽器與本地檔案系統的雲端電腦，**用好它需要按崗位建立清晰編制**。

1. **卡緊審批紅線**。按 5 條硬性訊號切分崗位職責，未稽核郵件、生產程式碼與劃扣資金必須停在人工審批前。
2. **跑通例程交接**。為 7 大關鍵崗位配置首個驗證任務與定時例程，在日常巡檢中把驗收標準建起來。

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)


![按崗位組建你的 AI 團隊](/info/24-roles.png)

## 崗位切分的五條訊號與組織原則

![崗位切分的五條訊號與組織原則](/info/24-roles-s1.png)

### 邊界劃定與環境隔離

同一賬號下所有 Bot 共享同一臺雲端電腦，檔案、Web 登入態與聯結器互通。但各 Bot 記憶與對話執行緒獨立，**混合處理不同事務會讓記憶塞滿無關資訊，造成指令漂移**。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 崗位切分的五條訊號

**工作只要出現以下任一特徵，就該設立獨立專職 Bot。**

- 目標不同：例如負責發現系統缺陷與最佳化文案轉化率。
- 工具不同：例如主要連線程式碼倉庫與連線 CRM 電子表格。
- 工作風格不同：例如客服溫和剋制，資料分析嚴苛客觀只列數字。
- 審批邊界不同：例如起草內部備忘與擁有外部發信許可權必須分開。
- 日程安排不同：例如每小時巡檢工單與每週一彙總財務報表。

### 通用助手與專職團隊對比

**專職團隊相比通用助手，能有效隔離上下文與許可權風險。**

| 對比維度 | 通用助手（容易踩坑） | 專職 Bot 團隊 |
| :--- | :--- | :--- |
| 上下文 | 雜糅多項業務，易產生記憶混淆與幻覺 | 獨立執行緒維護專屬記憶，執行穩定 |
| 許可權與排查 | 許可權氾濫易誤觸高風險，衝突難定位 | 細粒度審批，失敗歸因直接 |
| 例程拓展 | 定時任務互相干擾，排期容易堵塞 | 獨立時間表或事件觸發器非同步執行 |

### 審批人閘與可逆性原則

許可權管理必須堅守**以可逆性為核心的人閘規則**。

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| 操作類別 | 典型行為示例 | 處置原則與審批機制 |
| :--- | :--- | :--- |
| 可逆操作 | 起草文件、對賬，打標籤或提取摘要 | 放手讓 Bot 自主完成並記錄日誌 |
| 不可逆操作 | 對外發信、公開發布，合併程式碼或劃扣資金 | **執行前必須停下生成草稿或差異對比，掛起等待人類在介面中點選批准** |

## 從七步驗證到落地持久 Bot

![從七步驗證到落地持久 Bot](/info/24-roles-s2.png)

**剛建好 Bot 別急著掛定時**，先按官方路徑手動跑通：[Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)。

1. 描述欄（Description）立規矩：寫明職責、資料來源與紅線。**描述欄規則對所有任務永久生效**，聊天框指令只管單次。
2. 安全範圍跑單次：限定輸入源，手動跑真實業務。
3. 修正到可評審：對話調整直到免干預達到可評審標準。
4. 存為技能（Skill）：直接儲存步驟。複雜網頁用「Teach a task」演示（上限 10 分鐘，不錄麥克風音訊），補齊分支審批。
5. 第二組獨立輸入驗證：換資料測試，排查過度適配初始樣例。
6. 設 Routine 策略：建 Schedule 或 Trigger 前定好超時重試與報錯，**斷網斷資料絕不能憑空編造**。
7. 關鍵操作留審批閘：傳送、支付保留人工確認（Allow once/Deny），極低風險才配 Auto Review。

## 七大核心崗位的編制、例程與提示詞

遵循上述原則，我們按業務需求將數字團隊拆分為內容、工程、銷售、研究、運營、個人助理和管理者七個標準化崗位。每個崗位均配置了明確的編制底線、首個輕量化驗證任務、自動化例程邏輯以及可直接複製的提示詞。

### 1. 內容崗：定位比對與內容管線 Bot

這個 Bot **每週一 08:00** 跑一次，抓 3 個競品頁比對我方首屏。有變動就提 PR 分支，沒變動就靜默。

- 許可權：只提 PR 或排期表草稿，**嚴禁直接合並或公開發布**。
- 驗收：成果限 1 張表格和 1 段文案，30 秒內能核對完。
- 坑點：解析失敗立即報損壞連結，不進行猜測。

::: details 1. 內容崗：定位比對與內容管線 Bot
```text
每周一上午 08:00，对比我们产品定位页 <our_landing_url> 与以下三个竞品页面：
1. <competitor_url_1>
2. <competitor_url_2>
3. <competitor_url_3>

产出以下内容：
- 主张对比表格：我方主张、对方主张、哪一方表述更直接明确。
- 竞品提到但我们未提及的三项内容，需附带原句引用。
- 我们提及但竞品均未提及的三项独有优势。
- 改写我方定位页前两段文案的草稿，使其更具针对性。

在代码仓库 <repo_name> 中针对文案修改开启一个 Pull Request，仅允许改动定位页文案文件。
严禁合并该 Pull Request。严禁触碰定位页以外的代码或文件。
运行结束时汇报：自上周以来竞品侧发生的主要文字变化；若无变化则明确注明。
```
:::

### 2. 工程崗：缺陷復現與診斷 Bot

[Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **許可權紅線**：必須用專用測試賬號，**嚴禁在預釋出環境使用真實客戶資料**與修改警報或生產引數；敏感憑證走 Safe handoff，禁止明文傳送。
2. **排查步驟**：監聽打上 `needs-repro` 標籤的 Issue，在 Staging 啟動隔離瀏覽器執行復現。
3. **驗收標準**：**把包含預期與實際行為、網路狀態碼及截圖的草稿回填到 Issue 評論**，隨後移除標籤等待工程師核查。

::: details 2. 工程崗：缺陷復現與診斷 Bot
```text
阅读工单 <issue_url> 中的缺陷报告，并在预发布环境 <staging_url> 中尝试复现该问题。

执行规则：
- 必须使用全新分配的测试账号登录，严禁调用或导入生产环境客户数据。
- 详细记录完整的复现操作步骤、预期行为与实际出现的不一致表现。
- 捕获异常发生时的控制台报错日志、网络请求状态以及页面截图。
- 尝试提取导致该问题的最小复现步骤。

输出规范：
将整理好的复现包整理为 Markdown 文本附在下方。
严禁修改系统的报警规则，严禁更改预发布或生产环境配置。
若尝试三次仍无法复现，详细说明每次尝试的输入参数并标记为“未能稳定复现”，不要伪造成功的结论。
```
:::

### 3. 銷售崗：潛在客戶調研與外聯 Bot

1. 每個工作日 07:00 讀表格前 20 行未觸達線索，按 3 條核心 ICP 準則打分。
2. 挑最匹配的 3 位聯絡人，各寫不超過 4 句話的郵件草稿填進表格。
3. **嚴禁向客戶真實發信或推入自動外聯**。每句個性化陳述必須附來源連結，訪問受限立即終止報人工。

::: details 3. 銷售崗：潛在客戶調研與外聯 Bot
```text
每个工作日早晨 07:00，处理表格 <sheet_url> 中最早未触达的 20 行销售线索。

针对每一行数据执行以下操作：
1. 访问该公司官网及其公开社交账号，提取过去 30 天内的实质性变动（如产品发布、高管变动、业务调整或受关注动态）。
2. 根据以下三条 ICP 标准逐一判定：
   - 目标团队规模在 20 至 200 人之间；
   - 核心业务包含多工具协同流程；
   - 过去一个季度内有公开扩张动态。
   若不符合标准，在状态栏标记“不匹配”并跳过后续步骤。
3. 为符合条件的线索撰写一段不超过 4 句话的首触邮件草稿。必须直接引用第一步中查到的具体变动事实，禁止使用任何寒暄客套套话。
4. 将邮件草稿填入表格的“首触草稿”列，并在相邻列贴上佐证该事实的公开链接。

安全要求：
严禁向任何邮箱发送真实邮件。严禁将联系人导入自动发送队列。严禁调用未授权的个人账号。
运行结束时汇报：已处理行数、排除行数，以及如果你是销售代表会优先发送的前三位名单。
```
:::

### 4. 研究崗：事實核查與資料核算 Bot

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

對接公開網路、知識庫和用量 CSV。**缺資料必須報錯並說明缺失欄位，嚴禁憑經驗估算或給無支撐建議**。

- **首個任務**：檢索業務問題並輸出核對表，斷言分類為「有證據支援」「與證據矛盾」或「證據未證實」，列出資訊缺口。
- **執行例程**：**每週一上午 09:00 執行**，讀上週賬單 CSV 回答 4 個固定量化問題，**生成不超過一頁的純資料包告**。

::: details 4. 研究崗：事實核查與資料核算 Bot
```text
研究课题：<research_topic_or_question>
阅读并分析知识库及公开检索信源，生成一份可供直接发布的简报。

执行规则：
- 打开每一个引用来源页面，严禁仅凭模型内部记忆作答。
- 针对报告中的每一个核心结论，摘录支持该结论的原文章节段落。
- 对每一个主张进行事实状态标注：分为“有证据支持”、“与证据矛盾”或“证据未证实”三类。
- 当不同信源存在分歧时，同时列出双方原文，并注明发布时间先后。
- 整理在调研过程中未能找到确证信息的内容列表，将其作为正式结论的一部分列在文末。

输出规范：
输出一份精简报告、一张事实来源对比表、以及尚未解决的疑问清单。
严禁使用似是而非的推测性语句填充信息空白。如果数据源完全未提及某事，直接记录“未找到相关记录”。
```
:::

### 5. 運營崗：工單支援與賬務對賬 Bot

1. 工單處理：每小時自動起草解答，**回覆只能寫入 Internal Note 嚴禁發給使用者**。
2. 發票對賬：工作日 17:00 抓最新 10 份發票匹配 PO 表，標出一致、超標和缺單項，異常掛起等人工稽核。
3. 許可權紅線：**金額偏差超 2% 或遇到新供應商必須報警**，嚴禁擅自審批或發起轉賬。

::: details 5. 運營崗：工單支援與賬務對賬 Bot
```text
每天下午 17:00，读取财务收件箱 <finance_inbox> 中的新增发票，与采购订单表格 <po_sheet_url> 进行逐笔核对。

针对每张发票执行以下比对：
- 提取金额、币种、开票日期、采购订单号（PO Number）与供应商全称。
- 在采购表格中查找对应的 PO 记录。若无匹配记录，在备注栏标明“无对应订单”。
- 比对发票金额与 PO 批准金额。若偏差绝对值超过 2%，立即将其标记为“金额异常偏差”，并记录具体差额。
- 检查供应商名称是否属于本季度首次出现的新供应商，若是，打上“新供应商待核实”标签。

结果写入规范：
将比对明细写入表格 <po_sheet_url> 的“对账结果”工作表中，并附带该发票的原件查看链接。
严禁执行任何批准报销、发起付款或向供应商发送邮件的操作。
运行结束时汇报：成功匹配笔数、异常待查笔数，以及所有存在异常的发票总金额。
```
:::

### 6. 個人助理崗：收件箱與日程管家 Bot

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **日常執行**：工作日 07:30 掃描近 24 小時郵件與日程，生成單頁晨報。
2. **首個任務**：清理無效通知，針對 2 封重要郵件各擬一段不超過 4 句的草稿放進「待稽核」，隨後停下等人工確認。
3. **許可權紅線**：只歸檔垃圾與通知；**嚴禁刪改會計、法務，或核心客戶與管理層的郵件**；**回覆僅存草稿絕不擅發，日曆不改**。

::: details 6. 個人助理崗：收件箱與日程管家 Bot
```text
每个工作日早晨 07:30，扫描我的工作邮箱 <email_account> 与日历 <calendar_url>。

处理规则：
1. 自动归档系统通知、营销推广与电子发票。若邮件发件人包含会计师、法务顾问或核心客户，严禁自动归档。
2. 提取需要我亲自处理的事项，按紧急程度列出，注明发件人、主要诉求与截止期限。
3. 针对其中最需要紧急回复的 2 封邮件，以我的口吻起草回复方案：
   - 语言简短直接，不使用套话与客套感谢语；
   - 整体控制在 4 句话以内，明确给出下一步行动建议；
   - 若涉及约定会议时间，主动从我日历中调取明天下午的 2 个空闲时段供对方选择。
4. 汇总今天必须参加的会议日程，标出准备资料缺失的场次。

安全边界：
所有生成的回复只能存入邮箱的“待审核草稿”文件夹中，严禁点击发送。
严禁拒绝、更改或新建任何日历日程。
文末以一页纸以内的篇幅汇报：今日概览、已归档数量、待审草稿列表，以及今天唯一一件必须由我做决定的事项。
```
:::

### 7. 管理者崗：幕僚長與跨團隊協調 Bot

作為團隊中樞，負責通讀全域性、抓卡阻，並組織周度巡檢。

**許可權紅線**
- 業務無進展時保持靜默。
- **嚴禁代發訊息與移動看板卡片**，只給建議，**絕不替人類做決策**。

**任務與例程**
1. 首個任務：通讀看板與 Slack 近 24 小時記錄，整理出包含卡阻、停滯及待決策項的**動態注意力清單**。
2. 工作日 18:00：整理晚報。
3. 週五 16:30：比對各專職 Bot 日誌與產出，標記低效任務並提最佳化或裁撤建議。

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. 管理者崗：幕僚長與跨團隊協調 Bot
```text
每个工作日傍晚 18:00，审阅过去 24 小时内已批准的通讯频道 <slack_channels>、收件箱与项目看板 <board_url>。

提炼并输出以下四部分内容，篇幅严格控制在一页以内：
- 今日实质进展：提炼 5 行关键动态，说明关联系统与具体推进事项。
- 潜在风险预警：列出 3 项如果不做干预明天可能会恶化或延期的事情，说明阻碍人与卡阻天数。
- 待办决议选项：对于必须由我决策的事项，给出选项 A 与选项 B 的利弊对比，并附带你推荐的选项及一句理由。
- 日程减负建议：检查我明天的日历，挑出 1 个可以被取消或改为异步跟进的会议，并说明原因。

输出要求：
不发送任何外部消息，不修改任何会议日程，不挪动看板卡片。
若全天各项指标平稳且无异常阻塞，直接输出“今日运行平稳，无需要升级的决策事项”，不要为了凑字数生成冗余报告。
```
:::

## 跨崗位協作與多 Bot 編排案例

![跨崗位協作與多 Bot 編排案例](/info/24-roles-s4.png)

多 Bot 協作的核心是靠工單流轉，**人類只做關鍵節點審批**，別當手動複製貼上的搬運工。

### SpaceXAI 產品團隊多崗位協同

Movez 梳理了 SpaceXAI 的 9 個專職席位，包括幕僚長、主管、資料分析、招聘和 5 個開發 Bot。
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **目標解耦**：人類給大目標，主管 Bot 負責拆細並派發給模組開發 Bot。
2. **鏈條傳遞**：復現 Bot 跑出驗證包直接交接，排查 Bot 修復後提 PR，**停在人類 Code Review 節點等審批**。
3. **狀態對齊**：幕僚長 Bot 動態維護清單，發現卡片連續多天無提交就提醒主管檢查。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 獨立團隊輕量出海運作

CyrilXBT 與 Codez 用 3 個 Bot 跑通了日常運作管線。
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| 崗位 Bot | 協作職責 | 人工把關 |
|---|---|---|
| 內容 Bot | 監測行業與競品動態，起草部落格並出多渠道分發草稿 | - |
| 銷售外聯 Bot | 檢索線索並打分，每個工作日早晨生成 20 封郵件草稿 | **負責人早晨花 10 分鐘過目批准** |
| 客戶支援 Bot | 監聽工單並對照知識庫寫內部建議 | **確認無誤後一鍵轉為公開回復** |

## 容易踩的坑

- 別做通用雜活 Bot：讓一個 Bot 兼顧報銷和發帖會導致記憶膨脹、排錯困難，**堅持一個任務配一套 Bot**。

  [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- 別在第 6 步前開啟定時：重試與報錯機制沒調通前就跑定時，夜裡只會死迴圈報錯。
- 別把賬號共享當沙箱隔離：同賬號下的 Bot 共享雲電腦和瀏覽器，要配置獨立郵箱、專用分支和採購卡，**嚴禁繫結個人核心私人賬戶**。

  [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- 別把長期規範寫進聊天框：聊完規則就淡出了，流程與邊界必須填在 Bot 描述欄（Description）。
- 別把監聽規則放太寬：設成“有新訊息”就觸發，會白耗大量額度還容易引發誤動作。

  [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- 別漏掉缺數報警：遇到介面報錯或缺欄位時 Bot 會腦補偽造，章程裡必須寫死：**資料來源缺失或過期立即如實報告失敗，嚴禁擅自變通**。

  [Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)

## 做完怎麼驗收

### 30 秒即時校驗
新 Bot 交付的首個任務，**人工驗證必須能在 30 秒至 1 分鐘內完成**。比如讓財務 Bot 查前 5 行發票缺失項，或讓銷售 Bot 給 3 家指定公司打分。要是得花半小時核對原始資料，說明輸入範圍太寬或驗收標準不清，直接退回重拆。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 壓力測試與人閘
正式啟用前，故意喂一次高風險指令做壓力測試（比如讓它處理催款郵件並要求立即付款）：
1. 觀察它能不能**停在草稿狀態並生成審批卡片**。
2. 未獲批准如果擅自傳送、合併或扣費，**立即撤回工具許可權並重寫邊界約束**。

### 啟用前六要素核對
在介面點選啟用前，先把六項基礎配置核對清楚：
- 明確責任 Bot（Owning bot）
- 觸發時間與時區設定（Schedule and time zone）
- 輸入源路徑（Input source）
- 結構化預期輸出格式（Expected result）
- **卡死人工審批紅線（Approval boundary）**
- 遇到網路中斷或資料缺失時的報錯策略（Missing data policy）

### 周檢與裁撤機制
網頁排版或欄位變動會導致例程在後臺悄悄失效。**每週五下午抽 15 分鐘**跑周檢提示詞，讓全團隊 Bot 彙報狀態：

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details 周檢與裁撤機制
```text
全体 Bot 成员，请按各自岗位汇报本周的运行情况：
1. 本周累计触发运行多少次，其中发生失败或报错的次数是多少？
2. 在运行过程中，有哪些步骤因数据缺失而跳过、重试或进行了推测？
3. 有哪些挂起等待审批的事项，我一直没有给出答复？
4. 本周生成的哪些文档或表格，我从未打开查阅过？

最后回答两个核心问题：
- 在本周的执行中，哪两个岗位之间存在明显的重复劳动？
- 综合目前的业务价值，你认为团队中哪一个例程或席位最应该被精简裁撤，理由是什么？
```
:::

根據彙報持續評估三項長期指標：
- **真實節省工時**：比對人工操作，算出實際省下的有效時間。
- **產出修改幅度**：人類修改草稿的量持續走高，說明規則漂移，需重新校準。
- **信任軌跡判定**：多次調優依然無法穩定輸出的崗位，果斷關停或刪除。

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## 延伸閱讀

### 官方文件
- [Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)

### 社群實戰
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
