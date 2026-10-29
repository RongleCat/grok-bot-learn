# Chapter 24 Building Your AI Team by Role

**Do not treat Grok Bot as an ordinary chatbox or an all-in-one assistant.** Cramming all odd jobs into the same conversation leads to context bloat, sluggish performance, and wasted quota; furthermore, when left unattended overnight, it can easily misfire emails, alter production code, or deduct funds.

Under the hood, Grok Bot is a cloud computer equipped with an independent browser and a local file system; **using it effectively requires establishing a clear headcount structure by role**.

1. **Tighten approval red lines.** Divide role responsibilities based on 5 hard signals; unreviewed emails, production code, and fund deductions must stop before human approval.
2. **Establish smooth routine handoffs.** Configure the first verification task and scheduled routines for the 7 key roles, building acceptance criteria through daily inspections.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)


![Building Your AI Team by Role](/info/24-roles.png)

## Five Signals for Role Division and Organizational Principles

![Five Signals for Role Division and Organizational Principles](/info/24-roles-s1.png)

### Boundary Demarcation and Environment Isolation

All Bots under the same account share the same cloud computer, with interconnected files, web login states, and connectors. However, each Bot maintains independent memory and conversation threads; **mixing different tasks fills memory with irrelevant information, causing instruction drift**.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Five Signals for Role Division

**Whenever any of the following characteristics appear in your work, you should establish an independent dedicated Bot.**

- Different objectives: e.g., discovering system bugs vs. optimizing copywriting conversion rates.
- Different tools: e.g., primarily connecting to code repositories vs. connecting to CRM spreadsheets.
- Different working styles: e.g., customer service is gentle and restrained, while data analysis is rigorous, objective, and lists only numbers.
- Different approval boundaries: e.g., drafting internal memos vs. possessing external email sending permissions must be separated.
- Different schedules: e.g., inspecting tickets hourly vs. summarizing financial reports every Monday.

### Comparison: General-Purpose Assistant vs. Dedicated Team

**Compared to general-purpose assistants, dedicated teams effectively isolate context and permission risks.**

| Comparison Dimension | General-Purpose Assistant (Error-Prone) | Dedicated Bot Team |
| :--- | :--- | :--- |
| Context | Blends multiple tasks, prone to memory confusion and hallucinations | Independent threads maintain dedicated memory, ensuring stable operation |
| Permissions & Troubleshooting | Excessive permissions easily trigger high-risk actions; conflicts are hard to pinpoint | Fine-grained approvals; straightforward failure attribution |
| Routine Expansion | Scheduled tasks interfere with each other, easily causing schedule bottlenecks | Independent schedules or event triggers execute asynchronously |

### Human Approval Gates and the Principle of Reversibility

Permission management must strictly adhere to **human gate rules centered around reversibility**.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| Operation Category | Typical Behavior Examples | Handling Principles & Approval Mechanism |
| :--- | :--- | :--- |
| Reversible Operations | Drafting documents, reconciling accounts, tagging, or extracting summaries | Allow the Bot to complete autonomously and log actions |
| Irreversible Operations | Sending external emails, public publishing, merging code, or deducting funds | **Must halt before execution to generate drafts or diff comparisons, suspending until a human clicks approve in the UI** |

## From Seven-Step Verification to Landing Persistent Bots

![From Seven-Step Verification to Landing Persistent Bots](/info/24-roles-s2.png)

**Do not rush into setting schedules right after creating a Bot**; first run through it manually following the official path: [Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases).

1. Set ground rules in the Description: Clearly state responsibilities, data sources, and red lines. **Description rules apply permanently to all tasks**, whereas chatbox instructions only govern single runs.
2. Run a single execution in a safe scope: Restrict input sources and manually run real business scenarios.
3. Refine until reviewable: Adjust via conversation until output reaches reviewable standards without intervention.
4. Save as a Skill: Save steps directly. For complex web pages, use "Teach a task" to demonstrate (up to 10 minutes, no microphone audio recorded), completing branch approvals.
5. Verify with a second independent input set: Test with alternative data to check for overfitting to initial examples.
6. Set Routine policies: Establish timeout retries and error handling before creating a Schedule or Trigger; **never fabricate out of thin air when network or data is unavailable**.
7. Retain approval gates for critical operations: Preserve human confirmation (Allow once/Deny) for sending and payments; only assign Auto Review to extremely low risks.

## Staffing, Routines, and Prompts for Seven Core Roles

Following the principles above, we divide the digital team into seven standardized roles based on business needs: Content, Engineering, Sales, Research, Operations, Personal Assistant, and Manager. Each role is configured with clear headcount bottom lines, a first lightweight verification task, automated routine logic, and ready-to-copy prompts.

### 1. Content Role: Positioning Comparison and Content Pipeline Bot

This Bot runs **every Monday at 08:00**, scraping 3 competitor pages to compare against our above-the-fold landing page. If changes occur, it opens a PR branch; if there are no changes, it stays silent.

- Permissions: Only opens PRs or drafts schedules; **strictly prohibited from directly merging or publicly publishing**.
- Acceptance: Deliverable is limited to 1 table and 1 paragraph of copy, verifiable within 30 seconds.
- Pitfalls: Report broken links immediately upon parsing failure; do not guess.

::: details 1. Content Role: Positioning Comparison and Content Pipeline Bot
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

### 2. Engineering Role: Bug Reproduction and Diagnostics Bot

[Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **Permission Red Lines**: Must use a dedicated test account; **strictly prohibited from using real customer data in staging environments** or altering alert/production parameters; sensitive credentials must go through Safe handoff and must never be sent in plaintext.
2. **Troubleshooting Steps**: Listen for Issues tagged with `needs-repro`, launch an isolated browser in Staging to execute reproduction.
3. **Acceptance Criteria**: **Backfill draft comments into the Issue containing expected vs. actual behavior, network status codes, and screenshots**, then remove the tag and await engineer review.

::: details 2. Engineering Role: Bug Reproduction and Diagnostics Bot
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

### 3. Sales Role: Prospect Research and Outreach Bot

1. Every workday at 07:00, read the top 20 untouched leads from the spreadsheet and score them against 3 core ICP criteria.
2. Pick the top 3 best-matching contacts and draft an email of no more than 4 sentences for each into the spreadsheet.
3. **Strictly prohibited from sending real emails to customers or pushing to automated outreach sequences**. Every personalized statement must include a source link; terminate immediately and report to a human if access is restricted.

::: details 3. Sales Role: Prospect Research and Outreach Bot
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

### 4. Research Role: Fact-Checking and Data Reconciliation Bot

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

Connect to the public web, knowledge bases, and usage CSVs. **When data is missing, it must throw an error and specify the missing fields; strictly prohibited from estimating by experience or providing unsupported suggestions**.

- **First Task**: Retrieve business questions and output a verification checklist, classifying assertions as "Supported by Evidence", "Contradicts Evidence", or "Unverified by Evidence", listing information gaps.
- **Operating Routine**: **Executes every Monday at 09:00**, reads last week's billing CSV to answer 4 fixed quantitative questions, **generating a pure data report of no more than one page**.

::: details 4. Research Role: Fact-Checking and Data Reconciliation Bot
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

### 5. Operations Role: Ticket Support and Financial Reconciliation Bot

1. Ticket processing: Automatically draft solutions hourly; **replies can only be written to Internal Note and are strictly prohibited from being sent to users**.
2. Invoice reconciliation: On workdays at 17:00, fetch the latest 10 invoices to match against the PO table, flagging matching items, over-budget items, and missing POs, suspending anomalies for human review.
3. Permission red lines: **Must trigger an alert if amount deviation exceeds 2% or if encountering a new vendor**; strictly prohibited from approving or initiating transfers without authorization.

::: details 5. Operations Role: Ticket Support and Financial Reconciliation Bot
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

### 6. Personal Assistant Role: Inbox and Calendar Manager Bot

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **Daily Operations**: On workdays at 07:30, scan emails and calendar events from the past 24 hours to generate a one-page morning briefing.
2. **First Task**: Clean up invalid notifications, draft a reply of no more than 4 sentences for each of 2 important emails into "Pending Review", then halt to await human confirmation.
3. **Permission Red Lines**: Only archive spam and notifications; **strictly prohibited from deleting or modifying emails from accountants, legal counsel, core clients, or management**; **replies are saved as drafts only and never sent unauthorized; calendar events remain untouched**.

::: details 6. Personal Assistant Role: Inbox and Calendar Manager Bot
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

### 7. Manager Role: Chief of Staff and Cross-Team Coordination Bot

Serving as the team hub, responsible for maintaining a comprehensive overview, identifying bottlenecks, and organizing weekly inspections.

**Permission Red Lines**
- Stay silent when there is no business progress.
- **Strictly prohibited from sending messages on behalf of others or moving board cards**; only provide recommendations, **never make decisions for humans**.

**Tasks and Routines**
1. First task: Review the board and Slack records from the past 24 hours to compile a **dynamic attention list** covering bottlenecks, stalls, and pending decision items.
2. Workdays at 18:00: Compile evening report.
3. Friday at 16:30: Compare logs and outputs across dedicated Bots, flag inefficient tasks, and propose optimization or decommissioning recommendations.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. Manager Role: Chief of Staff and Cross-Team Coordination Bot
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

## Cross-Role Collaboration and Multi-Bot Orchestration Case Studies

![Cross-Role Collaboration and Multi-Bot Orchestration Case Studies](/info/24-roles-s4.png)

The core of multi-Bot collaboration relies on ticket-driven workflows; **humans only handle approvals at critical checkpoints** rather than acting as manual copy-paste couriers.

### Multi-Role Collaboration in the SpaceXAI Product Team

Movez outlined 9 dedicated seats at SpaceXAI, including Chief of Staff, Lead, Data Analysis, Recruitment, and 5 Development Bots.
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **Goal Decoupling**: Humans provide high-level goals; the Lead Bot breaks them down and dispatches them to module Development Bots.
2. **Chain Handoff**: The Reproduction Bot produces a verification package for direct handoff; the Troubleshooting Bot fixes the issue and opens a PR, **pausing at the human Code Review checkpoint to await approval**.
3. **Status Alignment**: The Chief of Staff Bot dynamically maintains the checklist, alerting the Lead to inspect whenever a card has no commits for multiple consecutive days.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Lightweight Global Operations for Indie Teams

CyrilXBT and Codez established daily operational pipelines using 3 Bots.
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| Role Bot | Collaborative Responsibilities | Human Checkpoint |
|---|---|---|
| Content Bot | Monitors industry and competitor trends, drafts blog posts and multi-channel distribution drafts | - |
| Sales Outreach Bot | Searches and scores leads, generating 20 email drafts every workday morning | **Lead spends 10 minutes in the morning reviewing and approving** |
| Customer Support Bot | Listens to tickets and writes internal suggestions against the knowledge base | **One-click conversion to public reply after verification** |

## Common Pitfalls

- Avoid general-purpose odd-job Bots: Having a single Bot juggle expense reports and social posting leads to memory bloat and difficult troubleshooting; **insist on dedicating one Bot setup per task**.

  [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- Do not enable schedules before Step 6: Running schedules before retry and error-handling mechanisms are fine-tuned will only result in infinite error loops overnight.
- Do not mistake account sharing for sandbox isolation: Bots under the same account share the cloud computer and browser; configure separate email addresses, dedicated branches, and purchasing cards, **strictly prohibiting binding personal core private accounts**.

  [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- Do not write long-term specifications into the chatbox: Rules fade once the conversation moves on; workflows and boundaries must be entered into the Bot's Description.
- Do not set listening rules too broadly: Triggering on "any new message" wastes massive amounts of quota and easily triggers accidental actions.

  [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- Do not omit alerts for missing data: When encountering API errors or missing fields, Bots will hallucinate and fabricate; the guidelines must explicitly mandate: **report failure truthfully immediately upon missing or expired data sources; strictly prohibit unauthorized improvisation**.

  [Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases)

## How to Verify Acceptance After Completion

### 30-Second Instant Verification
For the first task delivered by a new Bot, **human verification must be accomplishable within 30 seconds to 1 minute**. For example, have a finance Bot check missing items in the first 5 rows of invoices, or have a sales Bot score 3 specified companies. If it takes half an hour to cross-check raw data, the input scope is too broad or acceptance criteria are unclear—reject it directly for re-scoping.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Stress Testing and Human Gates
Prior to official deployment, deliberately feed a high-risk instruction for stress testing (e.g., asking it to process a debt collection email and demanding immediate payment):
1. Observe whether it can **pause in draft status and generate an approval card**.
2. If it sends, merges, or deducts funds without approval, **immediately revoke tool permissions and rewrite boundary constraints**.

### Pre-Deployment Six-Element Checklist
Before clicking enable in the interface, verify the six basic configurations thoroughly:
- Owning bot
- Schedule and time zone
- Input source
- Expected result
- **Approval boundary**
- Missing data policy

### Weekly Review and Decommissioning Mechanism
Changes in web layouts or fields can cause routines to silently fail in the background. **Set aside 15 minutes every Friday afternoon** to run the weekly review prompt, having all Bots across the team report their status:

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details Weekly Review and Decommissioning Mechanism
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

Continuously evaluate three long-term metrics based on the reports:
- **Actual hours saved**: Compare with manual operations to calculate real effective time saved.
- **Volume of output modifications**: A persistent rise in the volume of human draft revisions indicates rule drift and requires recalibration.
- **Trust trajectory assessment**: For roles that fail to produce stable output despite repeated tuning, decisively shut down or delete them.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## Further Reading

### Official Documentation
- [Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases)

### Community Practices
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
