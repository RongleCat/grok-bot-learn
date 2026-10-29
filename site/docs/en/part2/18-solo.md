# Chapter 18 Case Study: One-Person Company and AI Team

**All Bots under the same account share the same cloud computer**, equipped with a built-in browser, file system, and terminal.

Creating a dozen Bots all at once and handing over all accounts easily leads to pitfalls.
- Wandering off path on external web pages, silently overwriting data
- Frequently triggering approvals in the middle of the night, causing review fatigue

By sorting out role boundaries, credential isolation, and approval redlines, you can **evolve from configuring your first AI employee to managing 29 Agents**.

## The First AI Employee: Defining Roles and Permissions Like Hiring

![The First AI Employee: Defining Roles and Permissions Like Hiring](/info/18-solo-s1.png)

Whether you treat a Bot as a tool or an employee depends on whether you are writing a one-off prompt or establishing role responsibilities. A one-off prompt only handles the immediate single task; once the window is closed, the context vanishes. A role description is a permanent profile document that dictates the Bot's behavioral baseline and thinking pattern when handling daily tasks.

### Role Definition and Admission Testing

**Do not grant irreversible permissions at first**; start with tedious, high-frequency, and easily reversible chores.

Before letting a Bot get hands-on, run two admission tests in advance to troubleshoot.
1. **One-sentence responsibility test**: State what to deliver in a single sentence. Cramming four or five unrelated action verbs is like one person doing three people's jobs; when an error occurs, it's impossible to locate the root cause.
2. **Trial in text**: Takes less than two minutes—first report steps, intended URLs to visit, and doubtful judgments.

Break the job description into five fields to delineate boundaries.
- Owns: Deliver fixed outputs.
- Inputs: Allowed reading channels.
- May: Self-managed operations.
- Must ask before: High-risk actions like spending money or changing configurations, **which must wait for human approval**.
- Done when: An objective acceptance checklist.

```text
先不要执行任何实际操作。请逐步向我推演你的完整执行方案：
1. 列出你准备依次打开的工具、网址与调用的插件。
2. 列出你在过程中需要做出的业务判断。
3. 标出你目前信息不足、存在疑虑或拿不准的决策点。
推演完毕后等待我的指令，严禁自行操作。
```

::: details Role Definition and Admission Testing
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

Role settings are completely different from temporary prompts.

| Dimension | Temporary Prompt | Role Setting |
|---|---|---|
| **Goal and Form** | Single conversation, focusing on a single action | Long-term configuration, delivering business outputs |
| **Boundaries and Permissions** | Verbal instructions easily overstep bounds, errors require reruns | Reversible actions self-managed, irreversible actions wait for approval, hard-set human gates |

### Three-Run Probation Period and Promotion Ladder

> Source: [Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> Author: [distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

Once a new Bot gets running, **never leave it unattended in the background right away**; test it first according to distort's "Three-Run Rule."

1. Run 1 (Full observation): Watch every step on the screen, noting down misinterpreted instructions, lost context, and wild guesses.
2. Run 2 (Fixing rules): Switch to a task of equal difficulty without reminding it of old mistakes. Focus on whether role rules and permission changes took effect, without altering the results for it.
3. Run 3 (Hands-off live test): Do not intervene throughout the entire process, stepping in only during approvals or when reaching retry limits, checking completeness, number of interventions, time elapsed, and quota usage.

**After passing the three tests, enter the promotion ladder**, divided into five levels of permissions.

| Level | Mechanism | Boundary |
| :--- | :--- | :--- |
| Level 0 | Observation only | Modifies no data |
| Level 1 | Preparation only | Reversible work such as searching, summarizing, and formatting |
| Level 2 | Human approval | Critical steps suspended pending confirmation |
| Level 3 | Autonomous execution | Scheduled or triggered runs, regularly generating evidence chain reports |
| Level 4 | Multi-Bot collaboration | Serving as dispatch and QA nodes |

Promoting to the next level requires meeting four **hard metrics**.
- 5 consecutive flawless live runs
- All validation steps passed
- No unresolved side effects
- Rollback mechanism verified as functional

For practical references, see ["Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort"](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) and ["Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez"](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg).

## From Zero to a Running Company: Chief of Staff and Dedicated Team Orchestration

When building a complete operational business system solo using Grok Bot, the easiest dead end to run into is piling too many capabilities onto a single Bot. A Bot that handles sales leads, writes content, reconciles accounts, and modifies code will quickly have its context window clogged with irrelevant preferences—not only confusing the business context easily, but also accelerating quota depletion.

### Chief of Staff Architecture and Department Breakdown

To build a team, create the Chief of Staff Bot first. In daily operations, you **interface only with the Chief of Staff**, which breaks down tasks, dispatches dedicated roles, and aggregates deliverables.

::: details Chief of Staff Architecture and Department Breakdown
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

- Research Bot: Assertions must include dates and URLs, actively mark doubtful points, and never force hallucinations.
- Content Bot: Formats according to templates, **strictly prohibited from publishing directly to external channels**.
- Sales Bot: Saves all outreach emails as drafts, waiting for human approval before sending.
- Tech Bot: Submitting GitHub PRs must include screenshots of passing tests.
- Finance Bot: Anything involving fund adjustments must be listed separately for confirmation.

::: details Chief of Staff Architecture and Department Breakdown
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

| Architecture | All-in-One Solo Bot | Chief of Staff Pipeline |
|---|---|---|
| Collaboration | Muddled memory makes troubleshooting hard | **Independent memory for each role**, pinpointing accountability accurately |

### Evidence Chain Review and Four-Week Trust Transfer

> Source: [From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> Author: [NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**To close your laptop with peace of mind, the prerequisite is seeing the proof (Show the tape).** Bot deliverables must include all three pieces of evidence:

- Screen recordings of operations or invocation logs: Showing the complete webpage trajectory or tool call sequences.
- Original sources for data and figures: Uncited references are prohibited.
- Explanations of error-skipped items and speculative conclusions.

**Trust is transferred gradually over four weeks.**

1. Week 1 (Draft Stage): Bot only drafts; a human reads through and executes manually.
2. Week 2 (Approval Stage): Bot stops at key steps; a human only verifies actions and approves.
3. Week 3 (Exception Reporting Stage): Low-risk tasks run autonomously; popup alerts for help occur only upon encountering anomalies or unauthorized actions.
4. Week 4 (Routine Inspection Stage): Runs fully autonomously according to routines; only audit reports are reviewed on weekends.

For related practices, see ["From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn"](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) and ["Grok Bot: How to Build Your First AI Team (Full Guide)"](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Solo Company in Practice: Boundaries and Independent Operation of a Single Cloud Computer

### Physical Boundaries

**All Bots under the same account share a single computer**, sharing directories and sessions. The official guidance clearly states not to treat Bots as isolation boundaries; prompts cannot prevent injection, and mistakenly running commands could leak Cookies and Sessions.

Stick to three rules in daily operations:
- Never log into primary online banking or core repositories; do not store confidential cloud drives.
- Use only least-privilege sub-accounts on external platforms.
- Route external logins through Handoff—humans enter passwords, and Bots only inherit the Session.

### Non-API System Automation

**Non-API systems rely on computer-use capabilities to click and fill forms**; four types of work are suitable for initial handover:
- Customer acquisition research: Scanning community directories and drafting emails.
- Fulfillment tracking: Checking stockouts and following up on delayed waybills.
- Content scheduling: Filling copy into draft boxes.
- Code maintenance: Troubleshooting errors on standalone sites and producing patches.

::: details Non-API System Automation
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

### Thresholds and Scoring

> Source: [One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> Author: [ZER @zerqfer](https://x.com/zerqfer)

Add new Bots only after **human review stabilizes to within 15 minutes per day** to avoid compounding burdens. Fill out a scorecard once a month to prevent silent degradation.

::: details Thresholds and Scoring
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

Refer to ["One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER"](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg).

## AI Agency Delivery System: Monthly Delivery Pipeline and Quality Control Human Gates

![AI Agency Delivery System: Monthly Delivery Pipeline and Quality Control Human Gates](/info/18-solo-s4.png)

For an AI Agency delivering to multiple clients, the core challenges lie in quality stability and quota cost control under multi-client concurrency.

Community author maestro shared an architecture for serving 5 retainer clients as a solo operator to achieve monthly business operations (community author maestro claims $18,000 monthly revenue serving 5 clients; unverified).

### The "Three Admission Tests" for the Service Menu

Avoid taking fully custom work and degenerating into manual outsourcing; **services entering the automated delivery menu must pass three hurdles**:

1. The brief can be written as a structured checklist.
2. Deliverables have third-party objective acceptance criteria.
3. **Delivered purely manually at least 10 times previously**. Without doing it 10 times, you cannot grasp the redlines; handing it over to agents will only yield fluff.

Qualified services include comparing 40 reference materials using a 500K context to produce research reports, batch-writing articles based on voice samples (Voice File), or building dashboards and lightweight scraping tools.

### Model Routing and the 195,000 Token Billing Cliff Interception

Allocate models by task; do not use flagship models for everything.
- Grok 4.1 Fast: 2M context, handles cleaning and preliminary filtering.
- Grok Build 0.1: Responsible for 80% of development materials.
- Grok 4.6: 500K, handles long-horizon Agents and reasoning.

**Input exceeding 200,000 tokens immediately doubles the rate**. Gateways must **hardcode a 195,000-token threshold**, throwing an error, truncating, or pruning when exceeded.

### Independent Read-Only Reviewer and Three-Retry Human Gate

> Source: [How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> Author: [maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

Production Bots reviewing their own outputs tend to rationalize them, easily masking prompt failures. **Review must be separated into an independent read-only loop**.

- Independent context: Inputs only the original brief, client specifications, and deliverables—no intermediate reasoning provided.
- Strictly read-only: **Reports only FAIL upon finding defects, never ghostwrites**, preventing covert patches from concealing issues.
- Adversarial nitpicking: Specifically targets critical flaws; any figure unsupported by materials is judged as failed.

::: details Independent Read-Only Reviewer and Three-Retry Human Gate
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

**Handover retries are capped at 3**, preventing infinite loops from running up steep Token bills. If the machine still fails to meet standards after three attempts, it indicates conflicting requirements, and human intervention is required to make a call.

Refer to ["How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro"](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf).

## 29-Agent Practice: How to Smoothly Scale from a Solo Bot to an Army

![29-Agent Practice: How to Smoothly Scale from a Solo Bot to an Army](/info/18-solo-s5.png)

Once you are familiar with configuring a single employee and the two-Bot QA closed loop, business demands will naturally push you to expand your team.

Community author Melvin Vivas documented his full journey of gradually expanding Grok Bot into 29 dedicated agents (community author Melvin Vivas claims to have 29 Bots; unverified).

### Functional Layout and Incremental Evolution of 29 Agents

**These 29 Bots all grew organically on demand**: when encountering repetitive tasks in daily work, create a dedicated role; once roles multiply, have the Chief of Staff, Emma, oversee them all. The business is divided into seven major areas:

- Dispatch hub: Emma is responsible for overall management and dispatching tasks.
- Tech R&D: CTO manages architecture; **Coder directs Cursor to automatically write code, submit PRs, and fix errors**, all without opening a local editor.
- Frontier research: Scans open-source dynamics on the X platform around the clock and produces briefing reports.
- Content matrix: Responsible for copywriting and retrospectives across channels.
- Business development: Uncovers business opportunities and collaboration leads.
- Operations & security: Handles emails, backups, and security audits.
- Personal growth: Handles check-ins, market tracking, and decision validation.

### Multi-Agent Collaboration Pipeline: Taking Technical Prototype to Content Conversion as an Example

The Bots hand off work to each other by relying on the shared cloud computer and session referencing.

::: details Multi-Agent Collaboration Pipeline: Taking Technical Prototype to Content Conversion as an Example
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

**Making changes doesn't require opening 29 windows one by one**; broadcasting a single command from the chief manager syncs across them within seconds.

### Five Signals for Role Separation and the Seven-Step Automation Method

When evaluation goals, invoked tools, working styles, approval boundaries (drafting and external communication must never be mixed), or scheduling cycles differ, you must **split them into independent Bots**.

1. Send the goals, data sources, formats, and shutdown boundaries to the Bot and have it remember them; for shared Bots, write them in the details About.
2. Pick a controlled real task for a single run.
3. Manually fine-tune until exempt from inspection.
4. Solidify into a reusable Skill.
5. Retest generalization with new data.
6. **Set clear retry limits and missing-data alerts before turning on Routine**.
7. Sending messages, making payments, or making modifications must be strictly bound to a Require Approval human gate.

| Stage | Scale | Architecture and Bottlenecks |
| :-- | :-- | :-- |
| 1 Solo | 1 Bot | Full human gate verification loop; requires constant monitoring |
| 2 Squad | 2-3 Bots | Separation of production and review; daily maintenance compressed to within 15 minutes |
| 3 Chief of Staff | 4-6 Bots | Dispatch and dashboard; **strictly prevent Chief of Staff from doing chores** |
| 4 Army | 10-30 Bots | Multi-line standup; regularly prune invalid routines |

### Kanban System and Morning Standup Mechanism

> Source: [How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> Author: [Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Once you have more than 5 Bots, stop using multiple chat windows—it's impossible to keep track. **Multi-Bot collaboration relies mainly on two things: Kanban and scheduled inspections**:

- **Shared status Kanban**: Do not scatter tasks across chat logs; consolidate them uniformly into Notion or a database Kanban board, defining five statuses: `Todo`, `Working`, `Blocked`, `Ready for Review`, and `Done`.

  When a Bot encounters an unknown error or lacks permissions, it directly changes the tag to `Blocked` and calls for human help; normally, just watch the cards flow.
- **Scheduled inspections and reconciliation**: A single Bot can be configured with up to 50 Routines, running at most once every 5 minutes.

  **At 3:00 AM, automatically run health checks on code for dead links and bundle sizes; at 5:00 AM, the manager Bot (such as Jenny) checks each dedicated Bot's Playbook one by one**, which effectively prevents the model from forgetting over time.

```text
全体专职 Bot，开始进行本周团队回顾审计。请各岗位汇报：
1. 本周你实际执行了多少次任务，其中失败或异常的中断有多少次？
2. 在执行过程中，有哪些步骤存在推测行为、跳过行为或由于数据缺失强行拼凑的情况？
3. 有哪些挂起的审批事项我一直没有回应？有哪些生成的物料我从来没有打开查看过？
4. 请指出：在当前的工作流中，你发现哪两个 Bot 存在职责重叠或重复工作？
5. 给出客观建议：为了节省整体用量额度，我们下周最应该裁撤哪一个无效的 Routine 或岗位？
```

For related practices, see ["How I use Grok Bot: My team of 29 AI agents"](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh), ["GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez"](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54), and ["Grok Bot: How to Build Your First AI Team (Full Guide)"](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Common Pitfalls

### Permissions and Approvals
1. The shared cloud computer shares sessions without isolation; **never log into primary accounts or sensitive systems**.
2. Require Approval only intercepts unexecuted operations and cannot undo damage; **hardcode human gates for high-risk actions from the very start**.
3. Approvals lapse if ignored for about 10 minutes; at night, **you must configure Allow rule whitelists or stop at drafts**.

### Cost and Architecture
4. Input exceeding 200,000 tokens doubles unit pricing: **The routing layer must set a 195,000-token hard interception and pruning**.
5. Avoid having a single Bot do everything or cloning 5 generic Bots; **unclear division of labor only pollutes context and wastes quota**.
6. Do not set 5-minute polling or listen to all messages; **without a No-data policy, network disconnections easily trigger fabricated data and burn through quota**.

### Rules and Handoffs
7. Chat instructions vanish upon refresh; **cross-task discipline must be committed to the Bot's memory**; write it in details About for shared Bots, as personal Bots no longer have a Description.
8. Across Bots, do not transfer entire chat logs; **handoff packages should keep only the goals and deliverable paths, along with conclusions and next-step requirements**.

## Acceptance Checklist

1. **Check credentials**: Clear banking and primary credentials from Plugins and the browser; switch to sub-accounts or Sessions; **never store plaintext passwords in chat logs**.
2. **Verify roles**: Bots must include Owns/Inputs/May/Must ask before/Done when, with an anti-drift declaration added at the end: **report errors immediately when data is missing; strictly forbid fabrication**.
3. **Test human gates**: Send deduction or deletion commands; they must **trigger Require Approval suspension 100% of the time**.
4. **Audit resilience**: Feed fake data drafts; the QA Bot must **return FAIL on the first line** without making unauthorized alterations; halt and trigger an alarm after 3 consecutive failures.
5. **Stabilize routines**: Ensure Kanban status flows in real time; click Test run to verify it works before enabling; **scheduled tasks must not rely on nighttime approvals exceeding 10 minutes**.

## Further Reading

### Official Documentation

- [Organizing Business and Work in Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)
- [Team Edition Bot Collaboration and Permission Management](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Grok Bot Security Architecture and Execution Environment](https://cursor.com/cn/docs/grok-bot/security.md)
- [Plans, Quotas, and Billing](https://cursor.com/cn/help/grok-bot/plans.md)
- [Configuring Scheduled Tasks and Trigger Routines](https://cursor.com/cn/help/grok-bot/routines.md)
- [Connecting Apps](https://cursor.com/cn/help/grok-bot/connect-apps.md)

### Community Case Sources

> Source: [GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> Author: [Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- ["From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn"](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- ["How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro"](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- ["One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER"](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- ["GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez"](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- ["Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort"](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- ["Grok Bot: How to Build Your First AI Team (Full Guide)"](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- ["How I use Grok Bot: My team of 29 AI agents"](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- ["Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez"](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
