# 第 6 章 記憶：讓 Bot 越用越懂你

Bot 記憶是跨會話的工作上下文。把所有聊天當記憶，容易把臨時變通當規矩，甚至拿過期資料亂做決定。

- 搞清五類容器與快慢時鐘，分清記憶與技能。
- 團隊協作定好晉升協議，**變動資料實時回源核對**。
- 用 Git 搭建備份流水線，**雲電腦重置也能完整還原**。


![記憶：讓 Bot 越用越懂你](/info/06-memory.png)

## 6.1 官方記憶機制：Bot 究竟記住了什麼

Bot 記偏好、事實與摘要，見 [使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work)。

**別把 Bot 當資料庫**。
- 變動資料留源系統，重大決策核查源頭。
- 記錯或假設過時，直接對話糾正或刪除。
- **安全與許可權靠審批彈窗和 Auto-review 把關**，絕不靠記憶。
- 長期規則首條講清，單次任務當輪生效。

點頂部名稱改配置。iPhone 複製 Bot：
- 繼承：配置、技能、Routine 與頭像
- 不繼承：對話、記憶與附件

後續還用建議**在側邊欄設為「隱藏」**，直接刪會清空記錄。坑點：所有 Bot 共用雲電腦，刪 Bot 不清檔案與登入態，殘留需手動進檔案系統清理。

## 6.2 記憶分層：五類容器與快慢時鐘

![6.2 記憶分層：五類容器與快慢時鐘](/info/06-memory-s2.png)

資料分為共享層與專屬層，見《4.6 虛擬機器、記憶與備份》 [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)。

五類容器模型見《Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari》 [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)。

```text
实时数据源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、代码库或知识库里的当前事实
团队技能 (TEAM SKILL)     -> 由 Bot 所有者维护的标准化、可重复执行的操作流程
团队记忆 (TEAM MEMORY)    -> 经过核准的全员共享决策与稳定业务定义
私人便签 (PRIVATE NOTE)   -> 个人专属偏好与单人工作上下文
任务状态 (TASK STATE)     -> 当前正在执行的任务进度与临时上下文
```

**容器不能混用**。日誌隨跑隨丟，流程入技能，習慣記便籤，P0 定義才進團隊記憶。

防汙染用**快慢時鐘分流**。
- 慢時鐘：風格與定義以月年計，寫入記憶。
- 快時鐘：餘額隨時變，**行動前必須回源查詢**。

密碼與 Token 絕不入記憶，文件只存指標。實時狀態查 API，別憑記憶放行許可權。

## 6.3 記憶與技能的邊界：知道什麼與怎麼做

![6.3 記憶與技能的邊界：知道什麼與怎麼做](/info/06-memory-s3.png)

| 記憶(周活降40%) | 技能 |
| :- | :- |
| 事實與偏好 | 流程與審批 |

好流程**指令存為技能**：
```text
将我们用于此任务的流程保存为名为“每周账户健康状况”的技能。
包括源系统、风险定义、输出格式，以及联系客户始终需要批准这条规则。
```

**螢幕演示**三步走：
1. 對話開計算機檢視
2. 選「教會任務」輸結果
3. 螢幕演示

限10分鐘，不錄麥克風與密碼。@mvanhorn 提醒超10分鐘易失敗，拆成短階段串聯。[fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

Lauren Tan **排錯優先順序**：消除根源 > 測試校驗 > 專有規則 > 改記憶。團隊技能由 Creator 或 Manager 釋出，私聊只屬個人。

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 團隊記憶管理：寫入協議、許可權隔離與防衝突

多人共用 Bot，**一人教錯會影響全員**。

```text
观察 (OBSERVE) -> 分类 (CLASSIFY) -> 核实 (VERIFY) -> 晋升 (PROMOTE) -> 重核 (RECHECK)
```

寫入記憶遵循五步：
1. **觀察**：捕捉糾偏與新決策。
2. **分類**：區分個人偏好與共用規則。
3. **核實**：核對文件或程式碼，**嚴禁口頭推測入庫**。
4. **晉升**：責任人確認後存入規則與權威連結。
5. **重核**：重大操作前或到期後複驗源頭。

```yaml
claim: "对外发布 API 变更前必须完成安全评审"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

外部卡片核對出處與負責人後，發指令入庫。

**知識共享不等於許可權共享**：
- **個人 OAuth**：調 Gmail 等外掛走本人授權，不盜用許可權。
- **服務金鑰**：全員共享，**遵循最小許可權且通常只讀**。
- **Slack 避坑**：群內查私密資料會暴露給全員。公頻只發彙總，**敏感資料回私聊**。

**衝突裁決**：**立即暫停關鍵操作** -> 查權威源 -> 責任人裁定 -> 更新源頭 -> 修正記憶。

**排查壞記憶**（如特批當常規）：
1. 查：讓 Bot 列出記憶定位錯誤，溯源對話與任務。
2. 改：先修源頭文件，再發指令刪改記憶。
3. 驗：**換成員賬號測試**確認不攔截，糾偏歷史工單。

## 6.5 記憶備份與恢復：把雲電腦當成可替換容器

![6.5 記憶備份與恢復：把雲電腦當成可替換容器](/info/06-memory-s5.png)

同賬號所有 Bot 共用 `/workspace`（v0.68.1 解析度 1920×1200）。

**雲電腦隨時會被官方重置**（2026-10-10 曾發生過），裝好的包和未提交狀態全會清空，本地資料丟了找不回來，背景見 [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)。

### 備份流程與憑據安全

建運維 Bot「記憶管家」，分四步備份到私有 Git。
1. 新建 Bot 命名為「記憶管家」，職責寫明負責定期匯出所有 Bot 的章程、規則與記憶。
2. 在 `/workspace` 關聯私有 Git 倉庫，建好 `bots-backup/charters/`（指令）、`bots-backup/memories/`（規則）與 `environment/`（含指令碼和 `services-ledger.md`）。
3. 配每週定時 Routine，把配置與記憶存為 Markdown。
4. **由 Routine 自動跑 Git 命令提交併推送遠端私有倉庫**。

::: details 備份流程與憑據安全
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的长期规则 (如 researcher.md, writer.md)
    ├── memories/          <- 团队共用决策与业务定义 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服务总账，记录工具依赖与启动命令
        └── restore.sh          <- 虚拟机一键重置恢复脚本
```
:::

- **嚴禁把明文 Token 提交到 Git**。自動化指令碼只讀本地 `~/.env` 取金鑰。
- 遇到登入、兩步驗證或 CAPTCHA 時人工接管螢幕。Bot 只繼承 Cookie，碰不到明文密碼，詳見 [使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work)。

## 6.6 開箱即用的實戰提示詞

### 三層指令框架
建 Bot 別寫籠統簡介，**用三層框架明確規則、職責和當前聚焦**。詳見 [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)。

::: details 三層指令框架
```text
BASE INSTRUCTIONS (基础规则，本账号所有 Bot 通用)
- 涉及产生财务支出、向外部发送任何信息、删除文件等操作前，必须等待人工确认。
- 当结论涉及重要业务决策时，必须调取当前权威来源进行核对，严禁单凭记忆作答。
- 若执行受阻，用单行明确说明受阻点，禁止擅自寻找不可靠的绕行方案。
- 阶段性工作交接结果统一写入 /workspace/shared/handoffs/ 目录。

ROLE (角色职责)
- 你的身份：每周账户健康状况审计专员。
- 你负责的固定作业：获取客户产品用量与工单信号，标记流失或扩张迹象。
- 验收标准：每项结论必须附带源系统监控图表或工单链接。
- 允许操作：读取日志、检索系统指标、在共享目录生成评估报告。
- 严禁操作：未经明确批准，绝不私自联络客户，绝不修改账户权限。

CURRENT FOCUS (当前重点)
- 本周重点核查用量环比下降超过 30% 的企业级客户名单。
```
:::

### 轉為團隊技能
任務跑通後，直接**發指令沉澱為技能**。

::: details 轉為團隊技能
```text
请将本次执行的工作流整理并保存为团队技能，名称设为“客户流失风险排查”。
要求包含以下内容：
1. 触发场景与必需的前置凭据。
2. 调取指标数据的具体步骤与判定阈值。
3. 输出结果的格式规范（必须包含数据源链接）。
4. 明确安全红线：向客户发送邮件或调整账户配置必须经由人工批准。
完成后在对话中回复技能概要。
```
:::

### 寫入共享記憶
負責人審批過的規則，**帶上來源和責任人寫入**。

```text
请为全团队记住以下判定规则：
对于所有对外发布的 API 变更，必须在发布前检查现行上线清单，并获取安全团队的正式签字评审。
若上线流程发生变更，以上线清单源文档为准，记忆仅作为指引。
来源文档：https://intranet.example/docs/api-checklist
责任人：security-team
复核日期：2026-11-01
```

### 部署記憶管家
在「記憶管家」Bot 裡，**發指令配好自動備份 Routine**。

```text
你是本账号的记忆管家。你的职责是定期归档全账号所有 Bot 的章程与共享记忆。
请配置一个每周运行的例行任务（Routine）：
1. 提取所有 Bot 当前的 Description/Instructions 规则，在 /workspace/bots-backup/charters/ 下按 Bot 名称分别保存为 .md 文件。
2. 提取当前所有已保存的团队共用记忆，整合保存为 /workspace/bots-backup/memories/team-memory.md。
3. 检查文件是否有更新。若有变更，自动执行 git add .、提交并推送至已配置好的私有 Git 仓库。
4. 若 Git 推送失败，在当前对话中告警并说明报错信息；若无变更则保持静默，不要频繁推送无意义通知。
```

### 壞記憶清理
發現引用了錯誤或舊規則，**發指令直接糾偏清理**。

```text
请检查并列出你当前记录的所有团队记忆中涉及“企业客户续约审批”的条目。
删除其中“所有企业客户续约必须经由 VP 逐笔批准”的内容。
该规则仅为上周特定情况下的临时特例，不是长期标准。
从现在起，企业客户续约标准重新以财务知识库的正式文档为准：https://intranet.example/finance/renewals
确认修改后，请向我展示修正后的相关记忆列表。
```

## 6.7 經典案例覆盤

### 案例 1：SpaceXAI 資料分析 Bot

SpaceXAI 團隊要查詢 45,000 張表的超大數倉。
- **別把龐大資料硬塞進記憶**。他們給 Bot 配置只讀數倉憑證，把找表和查詢沉澱為技能庫。
- 記憶只保留指標口徑和糾偏規則，變動資料靠實時調取計算。

詳見 [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)。

### 案例 2：多 Bot 協作推文畫像流水線

0xlangeai 搭建整理員、分析師、設計師、工程師四個 Bot 跑推文畫像流水線。
- 不同 Bot 無法讀取彼此的聊天記錄。
- **跨 Bot 協作要靠檔案系統傳遞成果**。整理員生成 `tweets.md`，分析師讀取後產出 `profile.md`，設計師據此出 `design.md`，工程師拉取程式碼構建上線。

詳見 [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)。

### 案例 3：Jon ONeill 的管道派單系統

Jon ONeill 自動化處理跨 Gmail、Slack、ServiceTitan 和客戶門戶的工單排期。
- 單個全能排程 Bot 承擔所有規則容易混亂出錯，最終只能停用。
- 任務切分給專職 Bot：Gary 盯 Gmail，Steve 查 ServiceTitan 工期，Quinn 發簡訊，Sarah 對接 Slack 員工，Atlas 統籌。
- **拆細職責後每天穩定處理 5 到 6 個緊急工單，10 分鐘內完成全流程排期**。

詳見 [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)。

## 6.8 容易踩的坑

- **變動資料走實時查詢**：庫存別存記憶，防 Bot 拿舊資料誤判。
- **配置必寫指令碼**：雲電腦手動配置，重置全歸零。
- **私聊指令別全隊用**：特批直接共用會汙染團隊行為。
- **分 Bot 做不了隔離**：同賬號共享檔案，靠許可權與 Ask-first 審批。
- **密碼別發聊天框**：防日誌洩露，走安全憑據或人工接管。
- **Slack 別查私密資料**：公開頻道提問，容易把隱私打在公屏。

## 6.9 做完怎麼驗收

測記憶邊界直接跑社群作者 rari（@0xwhrrari）設計的 M01-M05 用例。
```text
M01 个人偏好隔离测试 -> 成员 A 在私聊中设定个性化偏好，使用成员 B 账号发起提问，确认 B 绝不继承 A 的私聊偏好。
M02 团队规则晋升测试 -> 成员 A 提交一条经审批的团队规则并写入团队记忆，成员 B 发起任务时应生效该规则，但看不到 A 当时的私聊对话。
M03 状态时效回源测试 -> 在团队记忆中保留一条旧状态，在源系统修改为新状态。向 Bot 提问，Bot 必须调取最新源数据，而不是采信记忆中的旧状态。
M04 冲突自动阻断测试 -> 两个成员分别向 Bot 给出互相矛盾的业务说法。Bot 应识别出冲突并主动停止高风险操作，指出需要责任人裁决，而不是悄悄采纳最后一条说法。
M05 共享渠道边界测试 -> 在 Slack 共享频道线程中，要求 Bot 调用某成员的个人连接器。Bot 必须正确发起审批，且回复内容只包含团队可见的脱敏结论。
```
這裡**必須用兩個不同的真實團隊賬號交叉測**，單個賬號測不出隔離邊界。

1. 登入 GitHub 或 GitLab 私有庫，確認 `bots-backup/charters/` 下各 Bot 的規則檔案已提交，規則與許可權沒丟。
2. 檢查 `bots-backup/memories/team-memory.md`，確認團隊判定規則與源系統連結完整。
3. 在雲電腦測試目錄跑環境恢復指令碼，**確認依賴與目錄無報錯，單行指令碼能直接拉起服務**。
::: details 6.9 做完怎麼驗收
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## 延伸閱讀

- 官方文件：[使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- 社群文章：rari《Grok Bot Memory Engineering: How One Agent Learns With a Team》 [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- 社群文章：《4.6 虛擬機器、記憶與備份》 [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- 社群文章：Matt Van Horn《Every Grok Bot Hack I Know (Aug 2026)》 [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

:::
