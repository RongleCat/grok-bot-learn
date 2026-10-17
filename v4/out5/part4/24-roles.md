# 第 24 章 按岗位组建你的 AI 团队

**别把 Grok Bot 当普通聊天框或全包助手。** 杂活全塞进同个会话会导致上下文膨胀、变慢并浪费额度，夜间无人盯梢时还容易误发邮件、改动生产代码或划扣资金。

Grok Bot 底层是带独立浏览器与本地文件系统的云端电脑，**用好它需要按岗位建立清晰编制**。

1. **卡紧审批红线**。按 5 条硬性信号切分岗位职责，未审核邮件、生产代码与划扣资金必须停在人工审批前。
2. **跑通例程交接**。为 7 大关键岗位配置首个验证任务与定时例程，在日常巡检中把验收标准建起来。

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

## 岗位切分的五条信号与组织原则

### 边界划定与环境隔离

同一账号下所有 Bot 共享同一台云端电脑，文件、Web 登录态与连接器互通。但各 Bot 记忆与对话线程独立，**混合处理不同事务会让记忆塞满无关信息，造成指令漂移**。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 岗位切分的五条信号

**工作只要出现以下任一特征，就该设立独立专职 Bot。**

- 目标不同：例如负责发现系统缺陷与优化文案转化率。
- 工具不同：例如主要连接代码仓库与连接 CRM 电子表格。
- 工作风格不同：例如客服温和克制，数据分析严苛客观只列数字。
- 审批边界不同：例如起草内部备忘与拥有外部发信权限必须分开。
- 日程安排不同：例如每小时巡检工单与每周一汇总财务报表。

### 通用助手与专职团队对比

**专职团队相比通用助手，能有效隔离上下文与权限风险。**

| 对比维度 | 通用助手（容易踩坑） | 专职 Bot 团队 |
| :--- | :--- | :--- |
| 上下文 | 杂糅多项业务，易产生记忆混淆与幻觉 | 独立线程维护专属记忆，运行稳定 |
| 权限与排查 | 权限泛滥易误触高风险，冲突难定位 | 细粒度审批，失败归因直接 |
| 例程拓展 | 定时任务互相干扰，排期容易堵塞 | 独立时间表或事件触发器异步执行 |

### 审批人闸与可逆性原则

权限管理必须坚守**以可逆性为核心的人闸规则**。

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| 操作类别 | 典型行为示例 | 处置原则与审批机制 |
| :--- | :--- | :--- |
| 可逆操作 | 起草文档、对账，打标签或提取摘要 | 放手让 Bot 自主完成并记录日志 |
| 不可逆操作 | 对外发信、公开发布，合并代码或划扣资金 | **执行前必须停下生成草稿或差异对比，挂起等待人类在界面中点击批准** |

## 从七步验证到落地持久 Bot

**刚建好 Bot 别急着挂定时**，先按官方路径手动跑通：[Grok Bot 使用场景](https://cursor.com/cn/docs/grok-bot/use-cases)。

1. 描述栏（Description）立规矩：写明职责、数据源与红线。**描述栏规则对所有任务永久生效**，聊天框指令只管单次。
2. 安全范围跑单次：限定输入源，手动跑真实业务。
3. 修正到可评审：对话调整直到免干预达到可评审标准。
4. 存为技能（Skill）：直接保存步骤。复杂网页用「Teach a task」演示（上限 10 分钟，不录麦克风音频），补齐分支审批。
5. 第二组独立输入验证：换数据测试，排查过度适配初始样例。
6. 设 Routine 策略：建 Schedule 或 Trigger 前定好超时重试与报错，**断网断数据绝不能凭空编造**。
7. 关键操作留审批闸：发送、支付保留人工确认（Allow once/Deny），极低风险才配 Auto Review。

## 七大核心岗位的编制、例程与提示词

遵循上述原则，我们按业务需求将数字团队拆分为内容、工程、销售、研究、运营、个人助理和管理者七个标准化岗位。每个岗位均配置了明确的编制底线、首个轻量化验证任务、自动化例程逻辑以及可直接复制的提示词。

### 1. 内容岗：定位比对与内容管线 Bot

这个 Bot **每周一 08:00** 跑一次，抓 3 个竞品页比对我方首屏。有变动就提 PR 分支，没变动就静默。

- 权限：只提 PR 或排期表草稿，**严禁直接合并或公开发布**。
- 验收：成果限 1 张表格和 1 段文案，30 秒内能核对完。
- 坑点：解析失败立即报损坏链接，不进行猜测。

::: details 1. 内容岗：定位比对与内容管线 Bot
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

### 2. 工程岗：缺陷复现与诊断 Bot

[Grok Bot 使用场景](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **权限红线**：必须用专用测试账号，**严禁在预发布环境使用真实客户数据**与修改警报或生产参数；敏感凭证走 Safe handoff，禁止明文发送。
2. **排查步骤**：监听打上 `needs-repro` 标签的 Issue，在 Staging 启动隔离浏览器执行复现。
3. **验收标准**：**把包含预期与实际行为、网络状态码及截图的草稿回填到 Issue 评论**，随后移除标签等待工程师核查。

::: details 2. 工程岗：缺陷复现与诊断 Bot
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

### 3. 销售岗：潜在客户调研与外联 Bot

1. 每个工作日 07:00 读表格前 20 行未触达线索，按 3 条核心 ICP 准则打分。
2. 挑最匹配的 3 位联系人，各写不超过 4 句话的邮件草稿填进表格。
3. **严禁向客户真实发信或推入自动外联**。每句个性化陈述必须附来源链接，访问受限立即终止报人工。

::: details 3. 销售岗：潜在客户调研与外联 Bot
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

### 4. 研究岗：事实核查与数据核算 Bot

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

对接公开网络、知识库和用量 CSV。**缺数据必须报错并说明缺失字段，严禁凭经验估算或给无支撑建议**。

- **首个任务**：检索业务问题并输出核对表，断言分类为「有证据支持」「与证据矛盾」或「证据未证实」，列出信息缺口。
- **运行例程**：**每周一上午 09:00 执行**，读上周账单 CSV 回答 4 个固定量化问题，**生成不超过一页的纯数据报告**。

::: details 4. 研究岗：事实核查与数据核算 Bot
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

### 5. 运营岗：工单支持与账务对账 Bot

1. 工单处理：每小时自动起草解答，**回复只能写入 Internal Note 严禁发给用户**。
2. 发票对账：工作日 17:00 抓最新 10 份发票匹配 PO 表，标出一致、超标和缺单项，异常挂起等人工审核。
3. 权限红线：**金额偏差超 2% 或遇到新供应商必须报警**，严禁擅自审批或发起转账。

::: details 5. 运营岗：工单支持与账务对账 Bot
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

### 6. 个人助理岗：收件箱与日程管家 Bot

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **日常运行**：工作日 07:30 扫描近 24 小时邮件与日程，生成单页晨报。
2. **首个任务**：清理无效通知，针对 2 封重要邮件各拟一段不超过 4 句的草稿放进「待审核」，随后停下等人工确认。
3. **权限红线**：只归档垃圾与通知；**严禁删改会计、法务，或核心客户与管理层的邮件**；**回复仅存草稿绝不擅发，日历不改**。

::: details 6. 个人助理岗：收件箱与日程管家 Bot
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

### 7. 管理者岗：幕僚长与跨团队协调 Bot

作为团队中枢，负责通读全局、抓卡阻，并组织周度巡检。

**权限红线**
- 业务无进展时保持静默。
- **严禁代发消息与移动看板卡片**，只给建议，**绝不替人类做决策**。

**任务与例程**
1. 首个任务：通读看板与 Slack 近 24 小时记录，整理出包含卡阻、停滞及待决策项的**动态注意力清单**。
2. 工作日 18:00：整理晚报。
3. 周五 16:30：比对各专职 Bot 日志与产出，标记低效任务并提优化或裁撤建议。

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. 管理者岗：幕僚长与跨团队协调 Bot
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

## 跨岗位协作与多 Bot 编排案例

多 Bot 协作的核心是靠工单流转，**人类只做关键节点审批**，别当手动复制粘贴的搬运工。

### SpaceXAI 产品团队多岗位协同

Movez 梳理了 SpaceXAI 的 9 个专职席位，包括幕僚长、主管、数据分析、招聘和 5 个开发 Bot。
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **目标解耦**：人类给大目标，主管 Bot 负责拆细并派发给模块开发 Bot。
2. **链条传递**：复现 Bot 跑出验证包直接交接，排查 Bot 修复后提 PR，**停在人类 Code Review 节点等审批**。
3. **状态对齐**：幕僚长 Bot 动态维护清单，发现卡片连续多天无提交就提醒主管检查。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 独立团队轻量出海运作

CyrilXBT 与 Codez 用 3 个 Bot 跑通了日常运作管线。
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| 岗位 Bot | 协作职责 | 人工把关 |
|---|---|---|
| 内容 Bot | 监测行业与竞品动态，起草博客并出多渠道分发草稿 | - |
| 销售外联 Bot | 检索线索并打分，每个工作日早晨生成 20 封邮件草稿 | **负责人早晨花 10 分钟过目批准** |
| 客户支持 Bot | 监听工单并对照知识库写内部建议 | **确认无误后一键转为公开回复** |

## 容易踩的坑

- 别做通用杂活 Bot：让一个 Bot 兼顾报销和发帖会导致记忆膨胀、排错困难，**坚持一个任务配一套 Bot**。[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- 别在第 6 步前开启定时：重试与报错机制没调通前就跑定时，夜里只会死循环报错。
- 别把账号共享当沙箱隔离：同账号下的 Bot 共享云电脑和浏览器，要配置独立邮箱、专用分支和采购卡，**严禁绑定个人核心私人账户**。[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- 别把长期规范写进聊天框：聊完规则就淡出了，流程与边界必须填在 Bot 描述栏（Description）。
- 别把监听规则放太宽：设成“有新消息”就触发，会白耗大量额度还容易引发误动作。[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- 别漏掉缺数报警：遇到接口报错或缺字段时 Bot 会脑补伪造，章程里必须写死：**数据源缺失或过期立即如实报告失败，严禁擅自变通**。[Grok Bot 使用场景](https://cursor.com/cn/docs/grok-bot/use-cases)

## 做完怎么验收

### 30 秒即时校验
新 Bot 交付的首个任务，**人工验证必须能在 30 秒至 1 分钟内完成**。比如让财务 Bot 查前 5 行发票缺失项，或让销售 Bot 给 3 家指定公司打分。要是得花半小时核对原始数据，说明输入范围太宽或验收标准不清，直接退回重拆。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 压力测试与人闸
正式启用前，故意喂一次高风险指令做压力测试（比如让它处理催款邮件并要求立即付款）：
1. 观察它能不能**停在草稿状态并生成审批卡片**。
2. 未获批准如果擅自发送、合并或扣费，**立即撤回工具权限并重写边界约束**。

### 启用前六要素核对
在界面点击启用前，先把六项基础配置核对清楚：
- 明确责任 Bot（Owning bot）
- 触发时间与时区设置（Schedule and time zone）
- 输入源路径（Input source）
- 结构化预期输出格式（Expected result）
- **卡死人工审批红线（Approval boundary）**
- 遇到网络中断或数据缺失时的报错策略（Missing data policy）

### 周检与裁撤机制
网页排版或字段变动会导致例程在后台悄悄失效。**每周五下午抽 15 分钟**跑周检提示词，让全团队 Bot 汇报状态：

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details 周检与裁撤机制
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

根据汇报持续评估三项长期指标：
- **真实节省工时**：比对人工操作，算出实际省下的有效时间。
- **产出修改幅度**：人类修改草稿的量持续走高，说明规则漂移，需重新校准。
- **信任轨迹判定**：多次调优依然无法稳定输出的岗位，果断关停或删除。

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## 延伸阅读

### 官方文档
- [Grok Bot 使用场景](https://cursor.com/cn/docs/grok-bot/use-cases)

### 社区实战
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
