# 第 18 章 案例：一人公司與 AI 團隊

**同一賬號下的所有 Bot 共享同一臺雲端電腦**，自帶瀏覽器、檔案系統與終端。

一口氣新建十幾個 Bot 並交出全部賬號，容易踩坑。
- 外部網頁走錯路徑、靜默覆蓋資料
- 半夜頻繁觸發審批，讓人疲於稽核

理順崗位邊界、憑據隔離與審批紅線，就能**從配置首個 AI 員工演進到管理 29 個 Agent**。

## 第一個 AI 員工：像招聘一樣定義崗位與許可權

![第一個 AI 員工：像招聘一樣定義崗位與許可權](/info/18-solo-s1.png)

把 Bot 當作工具還是員工，取決於你是在寫單次提示詞，還是在確立崗位職責。單次提示詞只管眼前的一項事務，視窗一關上下文就消失。崗位職責是一份固定的檔案檔案，它決定了這個 Bot 每天處理事務時的行為底線與思考模式。

### 崗位定義與准入測試

**先別給不可逆許可權**，從枯燥、高頻且易撤銷的雜事切入。

讓 Bot 上手前，先跑兩項准入測試提前排錯。
1. **一句話職責測試**：一句講清交付什麼。塞入四五個無關動詞等於一人幹三人活，出錯沒法定位根因。
2. **純文字推演（Trial in text）**：耗時不到兩分鐘，先彙報步驟、預訪網址與存疑判斷。

崗位描述拆成五個欄位劃清邊界。
- Owns：交付固定產物。
- Inputs：允許讀取的渠道。
- May：可自理的操作。
- Must ask before：花錢或改配置等高危動作，**必須等人工審批**。
- Done when：客觀核對的驗收清單。

```text
先不要执行任何实际操作。请逐步向我推演你的完整执行方案：
1. 列出你准备依次打开的工具、网址与调用的插件。
2. 列出你在过程中需要做出的业务判断。
3. 标出你目前信息不足、存在疑虑或拿不准的决策点。
推演完毕后等待我的指令，严禁自行操作。
```

::: details 崗位定義與准入測試
```text
岗位名称：收件箱管理员（Inbox Manager）
Owns：
每天上午梳理工作邮箱，归档垃圾邮件与订阅通讯，起草客户咨询的回复草稿，标出需要我决策的紧急邮件。
Inputs：
仅限于 Gmail 中收件箱的未读邮件与公司提供的常见问题回复模版。
May：
阅读邮件、按标签分类、打上处理标记、撰写回复草稿、归档无回复价值的宣传邮件。
Must ask before：
严禁直接点击发送任何邮件；严禁归档来自财务、法务或房东的邮件；如果邮件涉及转账、退款、重置密码或修改凭证，立即停下向我确认。
Done when：
工作日上午 9:00 前收件箱所有未读邮件分类完毕；生成的草稿不超过四句话，语气平实直接，不使用任何客套空话；所有待办事项单独列出截止日期。遇到不确定如何处理的邮件，保持未读并挂起询问，严禁自行猜测意图。
```
:::

崗位設定與臨時提示詞完全不同。

| 維度 | 臨時提示詞 | 崗位設定 |
|---|---|---|
| **目標與形態** | 單次對話，關注單次動作 | 長期配置，交付業務產物 |
| **邊界與許可權** | 口頭交代易越權，出錯重跑 | 可逆自理，不可逆等審批，硬設人閘 |

### 三次執行試用期與晉升階梯

> 來源：[Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> 作者：[distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

新 Bot 剛跑通，**千萬別直接放後臺無人值守**，先按 distort 的「三次執行法則」測試。

1. 第 1 次（全程旁觀）：盯著螢幕看每步操作，記下誤讀指令、丟上下文和瞎猜的地方。
2. 第 2 次（修復規則）：換同難度任務，不提醒舊錯。重點看崗位規則與許可權改動是否生效，不替它改結果。
3. 第 3 次（放手實測）：全程不插手，只在審批或達到重試上限時介入，核驗完成度、干預次數、耗時與額度。

**透過三次測試後進入晉升階梯**，分五級許可權。

| 級別 | 機制 | 邊界 |
| :--- | :--- | :--- |
| Level 0 | 僅觀察 | 不改任何資料 |
| Level 1 | 僅準備 | 搜尋、摘要與排版等可逆工作 |
| Level 2 | 人工審批 | 關鍵步驟掛起等待確認 |
| Level 3 | 獨立執行 | 定時或觸發執行，定期產出證據鏈彙報 |
| Level 4 | 多 Bot 協同 | 擔任分發與質檢節點 |

升到下一級必須滿足四項**硬性指標**。
- 連續 5 次實跑無瑕疵
- 驗證步驟全透過
- 無未解決的副作用
- 回滾機制驗證可用

實踐參考 [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) 與 [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)。

## 從零到運轉的公司：幕僚長與專職團隊編排

一個人使用 Grok Bot 搭建完整業務運轉體系時，最容易走入的死衚衕就是給單個 Bot 堆積太多能力。一個既管銷售線索、又管內容寫作、還管對賬和改程式碼的 Bot，其上下文視窗很快會被大量不相干的偏好填滿，不僅容易混淆業務語境，還會加速額度損耗。

### 幕僚長架構與部門拆分

搭團隊先建幕僚長 Bot。你日常**只跟幕僚長對接**，由它拆解任務、排程專職崗位並彙總交付。

::: details 幕僚長架構與部門拆分
```text
你是一人公司的幕僚长（Chief of Staff），也是我日常沟通的唯一入口。
你的核心职责：
1. 接收我的业务目标，拆解为明确的工作阶段，派发给对应的专职 Bot（调研、内容、代码、运维）。
2. 在群聊中调度各岗位接力，跟踪各任务交付状态。
3. 检查专职 Bot 提交的产物是否符合完成标准，核对数据来源与执行录屏。
4. 每天晚上汇总团队进展，用不超过五行文字向我汇报核心结果、阻塞问题与需要我决策的审批项。
行为底线：
若无任何新进展或异常，保持静默；严禁越权代替专职 Bot 编写业务交付内容；严禁绕过人工审批直接执行外发、扣款或修改生产环境。
```
:::

- 調研 Bot：論斷須注日期與網址，存疑主動標出，不強行編造。
- 內容 Bot：按模版排版，**嚴禁直接對外發布**。
- 銷售 Bot：拜訪郵件全存草稿箱，等人工核准再發。
- 技術 Bot：提 GitHub PR 必附測試透過截圖。
- 財務 Bot：涉及資金調整必須單獨列出待確認。

::: details 幕僚長架構與部門拆分
```text
团队总体目标：
在两周内针对新上线的知识库产品，完成竞品定价调研，产出一份对比简报，并根据简报结构生成 3 篇官网更新草稿。

协作规则：
1. 调研 Bot 先行检索 5 家竞品公开定价，生成包含引用网址的 Markdown 表格。
2. 调研完成后在群内移交给内容 Bot，内容 Bot 根据数据起草 3 篇文案，放入指定 Notion 页面。
3. 幕僚长全程跟进看板状态，若遇到数据缺失，要求责任 Bot 重新抓取或报错，不得擅自编造。
4. 全流程中所有涉及对外发布的操作全部挂起，等待我在看板中勾选通过。
```
:::

| 架構 | 單兵全能 | 幕僚長流水線 |
|---|---|---|
| 協作 | 記憶混雜難定位 | **各崗獨立記憶**，精準定責 |

### 證據鏈審查與四周信任轉移

> 來源：[From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> 作者：[NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**想放心合上電腦，前提是看到憑證（Show the tape）。** Bot 交付必須帶齊三項憑據。

- 操作錄屏或呼叫記錄：展示完整網頁軌跡或工具呼叫序列。
- 資料與數字的原始出處：禁止無來源引用。
- 報錯跳過項與推測結論說明。

**信任分四周逐步轉移。**

1. 第 1 周（草稿階段）：Bot 僅起草，人工通讀並手動執行。
2. 第 2 周（審批階段）：Bot 跑到關鍵步停下，人工僅核對動作並審批。
3. 第 3 周（異常上報階段）：低風險事務自主跑，遇異常或越權才彈窗求助。
4. 第 4 周（例程巡檢階段）：按例程完全自主執行，週末只看審計報告。

相關實踐參考 [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) 與 [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)。

## 一人公司實戰：單臺雲電腦的邊界與獨立運營

### 物理邊界

**同賬戶所有 Bot 共享單臺電腦**，共用目錄與會話。官方明確別把 Bot 當隔離邊界，Prompt 防不住注入，誤跑命令會洩露 Cookie 與 Session。

平時守住三條。
- 不登主網銀和核心倉庫，不存機密網盤。
- 外部平臺只用最小許可權子賬號。
- 外部登入走 Handoff，人工輸密碼，Bot 只繼承 Session。

### 無 API 系統自動化

**無 API 系統靠計算機能力點選填表**，四類工作適合先交接。
- 獲客調研：掃社群目錄並起草郵件。
- 履約跟進：核對缺貨並跟進延誤運單。
- 內容排期：文案填進草稿箱。
- 程式碼維護：排查獨立站報錯並出補丁。

::: details 無 API 系統自動化
```text
岗位名称：供应链履约跟踪员（Supplier Logistics Bot）
Owns：
每天上午 10:00 登录供应商门户，核对昨天未发货订单状态，提取物流单号，更新至运营表格。
Inputs：
供应商订货后台会话、本地待处理订单表格。
May：
在供应商后台查询订单状态、下载发货清单 CSV、更新本地表格对应列的运单号与发货时间。
Must ask before：
严禁点击「重新下单」或「取消订单」；严禁修改收货地址；若供应商后台提示账户欠款或商品缺货，停止处理并立即向我报警。
Done when：
所有处理过的运单在表格中均标注状态与回填时间；遇到后台页面改版导致按钮无法识别时，截取当前屏幕报错并退出，不得盲目重试。
```
:::

### 門檻與評分

> 來源：[One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> 作者：[ZER @zerqfer](https://x.com/zerqfer)

**人工審查穩定降至每天 15 分鐘內**才能加新 Bot，避免放大負擔。每月填一次評分卡防靜默衰退。

::: details 門檻與評分
```text
Bot 月度运行评分卡
评估周期：2026 年 10 月
岗位名称：[例如：订单跟进助理]
1. 实际工时节省：本月相比纯手工操作，实际节省了约多少小时？
2. 人工介入程度：产出草稿中，需要人工手动大幅修改的比例是多少（低于 10% 算达标）？
3. 信任度变化趋势：对该岗位的自主执行信任度处于上升、持平还是下滑？
4. 异常与回滚记录：本月出现过几次页面识别错误或越权报警？
5. 处置结论：[保留继续运行 / 降级为人工审批执行 / 彻底停用删除]
```
:::

參考 [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)。

## AI Agency 交付體系：月交付流水線與質檢人閘

![AI Agency 交付體系：月交付流水線與質檢人閘](/info/18-solo-s4.png)

對於面向多客戶交付的 AI 代理機構（AI Agency），核心難點在於多客戶併發時的質量穩定與額度成本控制。

社群作者 maestro 分享了單人服務 5 家 Retainer 客戶、實現月度業務運轉的體系架構（社群作者 maestro 自述月營 1.8 萬美元、服務 5 家客戶，未核）。

### 業務選單的「三項准入測試」

別接全定製淪為手工外包，**業務進自動交付選單得過三關**。

1. Brief 能寫成結構化清單。
2. 交付物有第三方客觀驗收標準。
3. **此前純手工交付至少 10 次**。沒做滿 10 次摸不清紅線，交給智慧體只會產出廢話。

達標業務包含 500K 上下文比對 40 篇資料做研報、按聲音樣本（Voice File）批次寫稿，或搭建看板與輕量抓取工具。

### 模型路由與 19.5 萬 Token 計費懸崖攔截

模型按活分配，別全上旗艦。
- Grok 4.1 Fast：2M 上下文，跑清洗初篩。
- Grok Build 0.1：負責 80% 開發物料。
- Grok 4.6：500K，跑長程 Agent 與推理。

**輸入超 200,000 Token 費率直接翻倍**。閘道器要**硬編碼 195,000 Token 閾值**，超限報錯截斷或剪枝。

### 獨立只讀稽核者與三次重試人閘

> 來源：[How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> 作者：[maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

生產 Bot 審自己的產物會有自洽傾向，容易掩蓋提示詞失效。**稽核必須切成獨立的只讀迴路**。

- 獨立上下文：只輸入原始 Brief、客戶規範和產物，不給中間推理。
- 嚴格只讀：**發現缺陷只報 FAIL 絕不代筆**，防止私自修補掩蓋問題。
- 對抗挑刺：專抓硬傷，沒有資料支援的數字一律判掛。

::: details 獨立只讀稽核者與三次重試人閘
```text
# 独立审查者审核准则（reviewer.md）
你是一名独立质量审查员，负责评估一份并非由你生产的交付产物。
你的唯一任务是找出交付物不符合客户要求的地方。你绝不需要去赞美它的优点。

输入物料：
原始需求 Brief、服务核对清单、客户品牌声音规范文件、最终交付草稿。
你未被提供、也严禁索取生产 Bot 的思考草稿。

审查规则（按顺序严格执行）：
1. 逐条核对需求 Brief 中的清单项。指出任何未被完全覆盖的要点。
2. 检查全文，严禁残留任何占位符文字、TODO 标记或括号说明文本。
3. 全文中的每一个具体数字、引文、统计百分比与人名，必须能在客户资料库中找到对应出处。发现任何未注明来源的数字，必须直接判定为 FAIL。
4. 语言风格是否符合客户过往已批准作品的语气标准。

输出格式：
第一行必须且只能输出一个词：PASS 或 FAIL。
如果判定为 FAIL，按以下格式列出所有缺陷：[清单条款] - [出现位置] - [具体问题及修正要求]。第一行后严禁输出任何空洞的总结段落。
若因上下文缺少凭据导致无法核验某一项，直接判定为 FAIL。
```
:::

```text
单任务自动化生产循环规则：
1. 生产 Bot 基于需求与声音规范生成第 1 版草稿。
2. 独立审核 Bot 执行审查。若返回 PASS，记录日志并进入待交付队列。
3. 若返回 FAIL，系统将审查不通过的具体原因拼接入下一轮 Brief，由生产 Bot 进行针对性修复重试。
4. 重试上限（MAX_ATTEMPTS）严格设定为 3 次。
5. 若连续 3 次均无法通过审查，系统立即终止自动重试，触发报警将原始 Brief、草稿与审查报错完整推送到人工桌面由人工兜底接管。
```

**交接重試最多 3 次**，防止死迴圈刷出高額 Token 賬單。機器試了三次仍不達標，說明需求衝突，必須由人工介入判定。

參考 [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)。

## 29 個 Agent 的實戰：如何從單兵平滑擴編到軍團

![29 個 Agent 的實戰：如何從單兵平滑擴編到軍團](/info/18-solo-s5.png)

當你熟悉了單個員工的配置與雙 Bot 的質檢閉環，業務需求自然會推動你擴建團隊。

社群作者 Melvin Vivas 記錄了自己如何一步步將 Grok Bot 擴充至 29 個專職智慧體的完整實踐（社群作者 Melvin Vivas 自述擁有 29 個 Bot，未核）。

### 29 個 Agent 的職能佈局與漸進演進

**這 29 個 Bot 全是按需長出來的**：平時遇到重複事務就建專職角色，角色多了再由幕僚長 Emma 統管。業務分為七大板塊：

- 排程中樞：Emma 負責統管全域性與分發任務。
- 技術研發：CTO 管架構；**Coder 調動 Cursor 自動編寫程式碼提 PR 並修復報錯**，全程不用開本地編輯器。
- 前沿調研：全天掃描 X 平臺開源動態並出簡報。
- 內容矩陣：負責各渠道文案創作與覆盤。
- 商務拓展：挖掘商機與合作線索。
- 運營安全：負責郵件、備份與安全審查。
- 個人成長：處理打卡、行情追蹤與決策論證。

### 多 Agent 協同流水線：以技術原型到內容轉換為例

各 Bot 靠共享雲電腦和會話引用接力。

::: details 多 Agent 協同流水線：以技術原型到內容轉換為例
```text
端到端跨团队协同案例：
1. 【情报捕获】：X 调研员监控到某大模型最新发布，抓取官方文档与代码仓库地址，整理为技术要点。
2. 【任务调度】：幕僚长 Emma 捕获该报告，根据设定规则判定该模型具备测试价值，自动将任务下发给技术团队。
3. 【工程交付】：编码员 Coder 接收技术说明，调起 Cursor Cloud coding agent 在云端编写 Google Colab 演示笔记本，推送到 GitHub 仓库并自动创建 Pull Request。
4. 【排错闭环】：执行测试出现依赖包版本冲突，终端 Traceback 自动返回 Coder，Coder 修复代码再次提交 PR 通过测试。
5. 【内容物料转译】：PR 合并后，Emma 将成功代码仓库与技术参数推送给内容创作团队，YouTube 脚本助手与 X 内容经理在半小时内完成多平台发布草稿，存入指定待审目录。
6. 【人闸闭环】：创始人全程不介入代码编写与格式排版，仅在最后核验 Colab 实际运行效果，并点击确认对外发布推文。
```
:::

**改動不用挨個點開 29 個視窗**，總管廣播一條指令幾秒就能同步。

### 角色拆分的五大訊號與自動化七步法

考核目標、呼叫工具、工作風格、審批邊界（草稿與對外溝通絕不能混）或排程週期不同時，必須**拆分獨立 Bot**。

1. 把目標、資料來源、格式與停機邊界發給 Bot 並讓它記住；共享 Bot 寫在詳情 About。
2. 挑受控真實任務單次執行。
3. 人工調優到免檢。
4. 沉澱為複用 Skill。
5. 換新資料複測泛化。
6. **定好重試上限與缺失報警，才開 Routine**。
7. 發信、付款或改動，強綁 Require Approval 人閘。

| 階段 | 規模 | 架構與瓶頸 |
| :-- | :-- | :-- |
| 1 單兵 | 1 Bot | 全量人閘驗證閉環；需時刻盯盤 |
| 2 小組 | 2-3 Bot | 生產與稽核分離；日維護壓進 15 分鐘 |
| 3 幕僚長 | 4-6 Bot | 分發與看板；**杜絕幕僚長幹雜活** |
| 4 軍團 | 10-30 Bot | 多線 standup；定期修剪無效例程 |

### 看板系統與晨會機制

> 來源：[How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> 作者：[Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Bot 超過 5 個就別用多聊天視窗了，根本看不過來。**多 Bot 協同主要靠看板和定時巡檢兩件事**：

- **共享狀態看板**：任務別散在聊天記錄裡，統一收攏到 Notion 或資料庫看板，定好五種狀態：`Todo`、`Working`、`Blocked`、`Ready for Review`、`Done`。

  Bot 遇到未知報錯或缺許可權直接改標 `Blocked` 並呼叫人工，平時看卡片流轉就行。
- **定時巡檢與對賬**：單 Bot 最多配 50 個 Routine，最高每 5 分鐘跑一次。

  **凌晨 3:00 自動體檢程式碼死鏈與包體積，5:00 由總管 Bot（如 Jenny）逐個核對專職 Bot 的 Playbook**，能有效防止模型久了遺忘。

```text
全体专职 Bot，开始进行本周团队回顾审计。请各岗位汇报：
1. 本周你实际执行了多少次任务，其中失败或异常的中断有多少次？
2. 在执行过程中，有哪些步骤存在推测行为、跳过行为或由于数据缺失强行拼凑的情况？
3. 有哪些挂起的审批事项我一直没有回应？有哪些生成的物料我从来没有打开查看过？
4. 请指出：在当前的工作流中，你发现哪两个 Bot 存在职责重叠或重复工作？
5. 给出客观建议：为了节省整体用量额度，我们下周最应该裁撤哪一个无效的 Routine 或岗位？
```

相關實踐參考 [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)、[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54) 與 [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)。

## 容易踩的坑

### 許可權與審批
1. 共享雲電腦共用 Session 無隔離，**絕不要登入主賬戶和敏感系統**。
2. Require Approval 只能攔未執行操作，無法撤銷破壞，**高危動作首次就設死人閘**。
3. 審批約 10 分鐘不理會失效（Lapse），夜間**必須配 Allow rule 白名單或停在草稿**。

### 成本與架構
4. 輸入超 20 萬（200,000）Token 單價翻倍：**路由層要設 195,000 Token 硬攔截與剪枝**。
5. 別搞單 Bot 攬全活或克隆 5 個通用 Bot，**分工不清只會汙染上下文並浪費額度**。
6. 別設 5 分鐘輪詢或監聽全訊息，**缺 No-data policy 時斷網容易瞎編資料耗盡額度**。

### 規則與交接
7. 聊天框叮囑重新整理就失效，**跨任務紀律要讓 Bot 記住**；共享 Bot 寫在詳情 About，個人 Bot 已沒有 Description。
8. 跨 Bot 別搬運全部記錄，**交接包只留目標與交付物路徑，加上結論和下一步要求**。

## 做完怎麼驗收

1. **查憑據**：清掉 Plugins 和瀏覽器的銀行與主憑據，改用子賬號或 Session，**聊天記錄絕不存明文密碼**。
2. **驗崗位**：Bot 須包含 Owns/Inputs/May/Must ask before/Done when，末尾加反漂移宣告，**缺資料立即報錯、嚴禁編造**。
3. **測人閘**：發扣款或刪除指令，必須 **100% 觸發 Require Approval 掛起**。
4. **抗稽核**：喂假資料草稿，質檢 Bot 須 **第一行返回 FAIL** 且不擅改；連續失敗 3 次停機報警。
5. **穩例程**：看板狀態實時流轉，開啟前點 Test run 跑通，**定時任務不依賴超 10 分鐘夜間審批**。

## 延伸閱讀

### 官方文件

- [在 Grok Bot 中組織業務與工作](https://cursor.com/cn/docs/grok-bot/work.md)
- [團隊版 Bot 協作與許可權管理](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Grok Bot 安全架構與執行環境](https://cursor.com/cn/docs/grok-bot/security.md)
- [方案、額度與計費說明](https://cursor.com/cn/help/grok-bot/plans.md)
- [配置定時任務與觸發例程](https://cursor.com/cn/help/grok-bot/routines.md)
- [連線應用](https://cursor.com/cn/help/grok-bot/connect-apps.md)

### 社群實戰來源

> 來源：[GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> 作者：[Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
