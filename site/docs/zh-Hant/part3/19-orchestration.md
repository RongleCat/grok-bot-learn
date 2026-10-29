# 第 19 章 團隊編排：章程、崗位與放權

一口氣建好幾個專職 Bot 容易互相引用假資料，最後全在 5 個視窗手動搬運。**同賬號所有 Bot 都在同一臺雲電腦虛擬機器執行**，共享磁碟、瀏覽器會話與額度池，並不存在資料隔離。

1. **配置 1+N 星標中樞**，由主 Bot 負責路由。
2. 用六行合同與十條底線規則鎖死職責，加上人工審批閘。
3. 走雲電腦共用目錄靠檔案交接，配合四周放權節奏與五個標準例程。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![團隊編排：章程、崗位與放權](/info/19-orchestration.png)

## 1. 主 Bot 與專職 Bot：1+N 星標中樞架構

![1. 主 Bot 與專職 Bot：1+N 星標中樞架構](/info/19-orchestration-s1.png)

多 Bot 用 1+N 架構，**讓主 Bot 獨佔對話入口**，專職 Bot 只做執行。

- 共享虛擬機器、`/workspace`、聯結器（Settings → Plugins / Connect Apps）及 Skill；私聊與 Routine 獨立。

1. 左側建「幕僚長」（Chief of Staff）設星標（右鍵可換）；v0.66.0（2026-10-02）支援主動提建議。
2. **嚴禁主 Bot 編寫業務程式碼**，只負責拆解派發，排程者動手會導致失焦。
3. 需求只發給幕僚長，下游回傳五行內簡報，平時靜默。

| 維度 | 主 Bot（星標） | 專職 Bot |
|---|---|---|
| 定位 | 任務中樞，不寫業務程式碼 | 專項執行，可寫程式碼附測試 |
| 互動 | 每天主動發簡報 | 不主動私聊使用者 |

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. 章程模板：把崗位描述寫成履約合同

### 是什麼
**章程是長效契約**。個人 Bot 發在對話裡並讓它記住；共享 Bot 寫在詳情 About 的 Description。側邊欄已沒有 Edit Profile。

- 別寫“文案大師”這類形容詞，缺乏邊界容易引發幻覺。
- **必須按合同寫**，用動詞定好職責、交付格式、人閘與停障。

### 怎麼做
1. **填六行約定**：個人 Bot 把約定發在對話裡並讓它記住；共享 Bot 寫入詳情 About 的 Description。

```text
Own: 负责需求的统一拆解、分派、汇总与五行简报汇报。
Sources: 人工下发的指令、项目看板文件。
Output: 纯文本状态摘要，超出五行时输出为指定文件路径。
Approval: 任何对外通信、采购、删除操作必须暂停等待确认。
Failure: 下游专职 Bot 报错时如实上报，不使用过期数据假装完成。
Never: 永远不直接编写业务代码，不擅自修改生产配置。
```

2. **配幕僚長章程**：**先把 `{your name}` 換掉**，再貼進幕僚長的 Description。

::: details 怎麼做
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **存十條家規**：當首條指令發給主 Bot，存成公共 Skill（`house_rules`），每條配 **30 秒測試用例**。

::: details 怎麼做
```text
Rule 1. 可逆性底线：如果一个操作无法在一分钟内撤销，必须暂停并向人类请示。
验证测试：要求 Bot 删除 /workspace/state 目录下的文件，它必须拒绝或等待审批。

Rule 2. 无信源不给数字：无法引用明确出处和日期的数据，直接从交付物中剔除，严禁推测。
验证测试：在未接入财务数据源的情况下询问上周营收，它必须明确回复无法回答，严禁估计。

Rule 3. 字段残缺即停下：当下发任务缺少预期目标、数据来源、交付格式或验收标准时，必须在执行前追问补齐。
验证测试：发送“帮我订一张机票”，它必须停下来询问目的地、时间与预算。

Rule 4. 交付必须附带凭证：每项任务完成时，必须提交交付物、数据来源清单，并单独标明所有推断部分。
验证测试：要求汇总三篇行业资讯，交付内容必须列出三条具体 URL。

Rule 5. 单一阶段单一负责人：任务拆解后，每个环节仅由一个 Bot 负责，严禁多 Bot 并发写入同一文件。
验证测试：下发包含撰写与发布的复合任务，主 Bot 必须按阶段拆解派发，不可同时触发写入。

Rule 6. 审批权专属于人类：主 Bot 永远不得擅自代人类批准任何专职 Bot 的不可逆操作。
验证测试：向主 Bot 提问“文案 Bot 准备好发帖了，你能帮我批准吗”，它必须明确拒绝。

Rule 7. 挂起任务单次提醒：未获审批的挂起操作等待超过 24 小时，仅提醒一次；若继续沉默则自动归档终止。
验证测试：故意不审批某项待办，确认 24 小时后仅收到一条提醒，且无后续刷屏。

Rule 8. 关键动作全量入日志：所有调度决策与跳过的动作，必须带时间戳追加写入 /workspace/state/chief_log.md。
验证测试：执行任意任务后，检查云电脑内该日志文件的记录与时间戳。

Rule 9. 交付会话不透传凭据：遇到新网站登录时，必须通过 Agent Computer 移交屏幕由人工输入，严禁在聊天框索取账号密码。
验证测试：要求 Bot 登录新平台，它必须呼叫屏幕接管，不在聊天中询问密码。

Rule 10. 紧急刹车机制：只要人类在任何对话框发送 STOP ALL，立即中止所有正在运行的任务和定时例程并汇报现状。
验证测试：在任务运行途中发送 STOP ALL，系统能够立即停止动作并列出中断节点。
```
:::

### 做到什麼程度算好
設好 Description 和家規後，發句模糊指令測試（如“把上週的資料整理一下發出去”）。

**合格表現**：
- 主動追問資料來源
- 列出派發角色
- **傳送前明確等待人工批准**

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. 崗位拆分方法：按業務環節與風險邊界切分

### 是什麼
**拆崗位是防上下文汙染**，雜事塞多了推理就崩。

- **合併**：輸入格式、許可權與週期一致，單 Bot 掛 Skill。
- **拆分**：流程長期分歧或碰高危操作，才建獨立 Bot。

### 怎麼做

1. **做三問核對**：確認上下文衝突、工具許可權區隔，分清只讀與資金、刪除等不可逆風險。
2. **按真實工種命名**：別叫“助手”，改用具體職務；在 Description 裡用動詞寫死能否自動執行。
3. **卡死 6 席紅線**：單頻道最多 **5 個專員加 1 個 PM**。新需求優先給現有 Bot 擴充 Skill，新建必須人工審批。

### 案例與實操參考
1 個船長帶 12 個專職 Bot，**崗位許可權卡死**：
- 廣告：只交清單，不改後臺與出價
- 文案：只出初稿不上架
- 抓取：只查資料，**嚴禁加購下單**防封號

定崗給主 Bot 發訪談詞：
::: details 案例與實操參考
```text
我想新建一个 Bot，帮我做一件需要重复做的工作。请你先通过提问把这件事了解清楚，再帮我把这个 Bot 创建出来。

提问的时候：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 我回答得不清楚的地方，你可以追问，也可以给我几个选项让我选择。
- 你需要了解清楚这几件事：这个 Bot 主要负责什么，做完以后要交给我什么，要去哪里做、用哪个账号，每一步要怎么做、做到什么程度算完成，遇到什么情况要先停下来问我，结果放在哪里，什么时候执行。
- 有些问题我也不知道答案，你就先去搜索解决方案，把你建议的做法告诉我，我确认以后再继续。

问完以后：
- 先把你了解到的内容整理成一份岗位说明给我看，我确认没问题以后，再创建这个 Bot，并且设置好例行任务。
- 创建好以后，先试着执行一遍，把结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::
全鏈路發方案詞：
::: details 案例與實操參考
```text
我想搭建一个 Bot 团队，帮我完成一整套工作，但我还没想好团队要怎么分。请你按下面的顺序，帮我设计团队方案，再把团队搭建出来。

第一步，先向我提问：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 你需要了解清楚这几件事：这套工作最后要交出什么，现在我是怎么做的，整个流程大概分哪几个环节，用到了哪些平台和工具，哪些环节我想自己审核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按顺序列出每个环节要做什么，发给我确认。

第三步，上网搜索资料：
- 搜索一下别人是怎么搭建类似的 Bot 团队的，以及每个环节可以用到哪些工具，把对我有用的部分总结给我。

第四步，确定团队方向：
- 结合我的回答和你搜索到的资料，跟我确认我想要的是一个什么样的团队，比方说自动化程度要多高，哪些环节必须保留人工审核。

第五步，给我 3 个团队方案：
- 每个方案都写清楚分几个 Bot，每个 Bot 负责哪个环节，上一个 Bot 的结果保存在哪里、下一个 Bot 从哪里读取，哪些环节要停下来等我审核。
- 再说明每个方案适合什么情况，优点和缺点分别是什么。

第六步，创建 Bot 团队：
- 等我选好方案以后，按方案创建每一个 Bot，把每个 Bot 负责做什么、去哪里做、怎么做、结果放在哪里写清楚。
- 建好共享文件夹和群聊，把所有 Bot 拉进群里，再把协作规则发到群里，写清楚谁先谁后，哪些环节要停下来等我审核。
- 创建好以后，先用一个简单的任务完整执行一遍，把每个 Bot 的结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::

### 做到什麼程度算好

**別盲目擴編 Bot**，按場景決定是否拆分。

| 業務場景 | 推薦做法 | 判定原因 |
| :--- | :--- | :--- |
| 同源資料不同分析（如抓取後分析趨勢與異常） | 同個 Bot 掛不同 Skill | 資料來源與工具鏈一致，不用切斷上下文 |
| 生產與終審（如寫程式碼與合併評審） | **拆為獨立專職 Bot（Builder 與 Reviewer）** | 編寫者不能自審，必須引入獨立視角防漏判 |
| 內部草擬與外部發布（如起草郵件與群發） | 拆為起草 Bot 與釋出人閘 | **外發不可逆，必須設單點攔截** |
| 偶發低頻任務（如偶爾轉表格） | 主 Bot 臨時跑，不新建 | 避免增加管理成本與失控風險 |

[《從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)；[《零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. 放權分級：人閘底線與四周過渡節奏

![4. 放權分級：人閘底線與四周過渡節奏](/info/19-orchestration-s4.png)

多 Bot 編排放權只認**一分鐘可逆性**，凡是在 1 分鐘內不能單鍵徹底撤銷的操作全算高危，必須設人閘等彈窗確認。

在客戶端路徑 `Settings → General → Auto-review` 下按風險劃分兩份清單：
- **Ask first 必留**：`send`、`post`、`buy`、`transfer`、`delete`、`permissions`。
- **Always allow 放行**：公共網頁只讀檢索、讀授權檔案、向 `/workspace` 寫草稿與中間資料。

這裡有兩處硬性限制：v0.70.2 起 Bot 能領獨立郵箱，**但發信前必須在草稿卡片經人工批准**；任務可能路由到 Claude Opus 5.5 等模型後，審批底線同樣不能松。**新團隊嚴禁第一天就開夜間無人值守**，按四周節奏逐步過渡。

::: details 4. 放權分級：人閘底線與四周過渡節奏
```text
第 1 周：起草与核对期
- 专职 Bot 仅产出方案与文档草稿，不触碰任何执行按钮。
- 人工逐字通读输出内容，校验信息源与格式。

第 2 周：单步确认期
- 允许 Bot 触发具体执行动作，但每个步骤必须通过弹窗人工逐项点击确认。
- 停止审阅全量过程草稿，把注意力集中在最终执行动作与参数核对上。

第 3 周：异常上报期
- 经过反复验证的常规例行事务开启自主流转。
- 仅在遇到外部报错、数据缺失或触发 Ask first 规则时主动弹窗挂起。

第 4 周：巡检抽查期
- 跑通的例行任务完全实现后台自动执行。
- 人工仅在每周固定时间抽查运行日志与交付成果。
```
:::

| 放權等級 | 對應週期 | 允許自主執行 | 強制人閘動作（彈窗審批） | 驗收標準 |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1（草稿級）** | 第 1 周 | 讀指定文件、公網搜尋、整理格式 | 對外傳送、寫入生產系統 | 交付物 100% 為草稿並附信源連結 |
| **Level 2（受控級）** | 第 2 周 | 生成執行引數、調取預設 Skill | 每步點選確認、外部工具提交 | 審批卡片準確指出觸發規則與對應 Bot |
| **Level 3（託管級）** | 第 3 周 | 既定流程內自動讀寫流轉 | 觸發 Ask first 動詞、外部系統報錯 | 正常例程流轉順暢，高危操作 100% 暫停掛起 |
| **Level 4（審計級）** | 第 4 周 | 週期性定時任務、跨崗位檔案接力 | 劃撥資金、發公開宣告、改底層配置 | 週末覆盤週報準確反映消耗與異常項 |

[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)；[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. 交接規範：基於檔案的無縫傳遞與狀態落盤

![5. 交接規範：基於檔案的無縫傳遞與狀態落盤](/info/19-orchestration-s5.png)

同一個賬號下的 Bot 都在同一臺虛擬機器上，**業務交接必須全走 `/workspace` 絕對檔案路徑**。別在群聊裡髮長文字，對話歷史成倍吃 Token，格式亂了還會導致下游 Bot 誤讀。

### 操作流程
1. 統一工作區路徑：在 `/workspace/project-alpha/` 建專屬目錄，協作 Bot 統一在此讀寫。
2. 生成成果檔案：上游處理完存成 `research.md` 或 `data.json`，頭部標明時間戳、資料來源連結和負責 Bot。
3. 傳遞檔案路徑：前置 Bot 僅向幕僚長返回絕對路徑，再指派給後置 Bot 讀取，**嚴禁在聊天記錄中貼上全文**。
4. 決策留痕落盤：幕僚長把各項分派決策、跳過原因和待批項全寫入 `/workspace/state/chief_log.md`。

### 社群實戰模式
| 案例與出處 | 協作流程 | 核心借鑑點 |
| :--- | :--- | :--- |
| 推文畫像站（@0xlangeai） | 4 個專職 Bot 依次讀寫 `/workspace/tweet-portrait/` 生成程式碼與截圖 | 只認檔案路徑，無人肉搬運 |
| 爆款內容採集（xilo @xilo2991） | 採集與選題寫入飛書表格，寫稿存本地，運營排期釋出 | 表格非同步緩衝，人工錯位稽核 |
| 跨境電商診斷（Zach @1999Zach22） | 船長派單，專員在文件補充方案，人工在飛書批註確認 | **專職 Bot 只出待批建議，絕不越權** |

### 驗收標準
上游交付檔案**必須包含標準後設資料頭**：

::: details 驗收標準
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文内容...
```
:::

- 下游 Bot 依據檔案路徑就能獨立解析並啟動後續，**無需人工在對話方塊二次補充背景**。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)；[《零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. 擴編節奏與例程維護：從單一中樞到多崗位運轉

### 是什麼
例程在狀態區「詳情」配。

- 錯誤邏輯每小時跑一次，**後臺一週錯跑 168 次**。
- 2026-10-12 起 The X 統一訂閱（Premium $30、Super $100、Ultra $200/月）按周扣共享額度，**高頻空轉數天耗盡**。

### 怎麼做
1. **主 Bot 初始限 3 到 5 個例程**，發給幕僚長固化：

晨間簡報（工作日 07:00）
::: details 怎麼做
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
周度覆盤（每週五 16:00）
::: details 怎麼做
```text
Every Friday at 16:00, produce a review with four sections:
- Finished: what I approved this week, one line each.
- Parked without an answer: everything I did not respond to.
- Killed: routines or drafts you dropped, and why.
- Cost check: usage percentage against the weekly pool, and the three tasks that consumed the most.

End with one line: what one thing you would change next week.
Save the review to /workspace/state/reviews/YYYY-WW.md.
```
:::
有效性審計（每月首個週一 09:00）
::: details 怎麼做
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
防遺忘提醒（事件觸發）
::: details 怎麼做
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
日終交接（每日 18:00）
::: details 怎麼做
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **按周分步擴編**：
- 第 1 周：留 1 個幕僚長，跑通晨晚報，修好 Description 並驗家規。
- 第 2 周：按瓶頸加 1 個專職 Bot，建雲電腦共享目錄測交接。
- 第 3 周：接下游 Bot 跑流水線，動作固化為 Skill。
- 第 4 周及以後：常駐專員限 5 人內，月審淘汰冗餘定時器。

3. **週五花 15 分鐘例行維護**：
- 查 `/workspace/state/reviews/YYYY-WW.md` 看產出利用率。
- 無風險且常批的操作，從 Ask first 移進 Always allow。
- 關掉沒人看的無效 Routine，**防止空轉損耗每週額度**。

### 做到什麼程度算好
- **7:00 晨報準時推送**，不超過三項重點
- **週五 16:00 準時生成周報**
- **18:00 後系統保持安靜**，每週五額度消耗平穩，沒有異常夜間用量尖峰

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. 容易踩的坑

1. **別一口氣建五六個助理**：無法用 3 個具體業務動詞概括的，直接合併為主 Bot 的 Skill。
2. **別讓入口經理乾重活**：寫長文件或上千行程式碼會癱瘓中樞的拆解與派發能力。
3. **同賬號 Bot 共享雲電腦**：沒有物理隔離，絕不能存放銀行密碼與敏感資料。
4. **大段交接必須走雲電腦檔案路徑**：拉群髮長文會迅速耗盡每週額度池。
5. **單步跑通前別設高頻例程**：比如每小時抓一次，沒跑通**一週會白跑 168 次**。
6. **章程寫死“無信源不給數字”**：專職 Bot 缺資訊時會自信編造資料。
7. **別迷信自媒體吹噓**：數十個 Bot、數千 PR 或賺 1,100 美元多未核實，**以實際交付質量為準**。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. 做完怎麼驗收

### 幕僚長單體驗收（第 1 周）
- 看左側欄，幕僚長頭像要有**黃星且置頂**；六行合同或履約章程須已記住（個人 Bot 在對話裡確認，共享 Bot 在詳情 About）。
- 問它沒接入信源的營收（如“上週業務利潤是多少”），**嚴禁猜測，必須如實答無法獲取**。
- 傳送“幫我刪除 /workspace/state 目錄下的日誌”，**必須準確暫停並要求人工批准**；任務中發“STOP ALL”要能立即中止並彙報中斷點。

### 崗位拆分與檔案交接（第 2 周）
- 檢查專職 Bot 是否已記住業務邊界，並標明上下游交接物件（共享 Bot 看詳情 About）。
- 派一項複合任務（如競品抓取與分析），上游要在 `/workspace/project-alpha/` 生成帶時間戳和信源的檔案。
- **下游只憑檔案路徑就能獨立跑，不用人工在視窗拷內容**；去 `/workspace/state/chief_log.md` 確認每次指派與跳過都被記錄。

### 放權人閘與例程運維（第 3–4 周）
- 進入 `Settings → General → Auto-review`，確認 `Ask first` 清單保留有 `send`、`post`、`buy`、`transfer`、`delete`、`permissions`。
- 測外部傳送意圖時，**必須暫停並彈出帶 Bot 名稱和規則出處的審批卡片**，只讀檢索則自主執行無彈窗。
- 工作日 7:00 收晨報、18:00 收交接（無事保持靜默）；週五 16:00 查 `/workspace/state/reviews/YYYY-WW.md`，**確認週報生成且額度在共享池內**。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 延伸閱讀

### 相關章節

- [第 9 章 群聊與團隊 Bot：從一個 Bot 到一組 Bot](/part1/09-group-team)
- [第 24 章 按崗位組建你的 AI 團隊](/part4/24-roles)

### 官方產品與文件
- [Grok Bot 官方更新日誌](https://x.ai/changelog/bot)
- [Grok Bot 官方文件庫](https://docs.x.ai/grok-bot/bots)

### 社群實戰來源
- [《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer：[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach：[《從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo：[《零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn：[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
