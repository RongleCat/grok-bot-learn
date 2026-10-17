# 第 18 章 案例：一人公司与 AI 团队

**同一账号下的所有 Bot 共享同一台云端电脑**，自带浏览器、文件系统与终端。

一口气新建十几个 Bot 并交出全部账号，容易踩坑。
- 外部网页走错路径、静默覆盖数据
- 半夜频繁触发审批，让人疲于审核

理顺岗位边界、凭据隔离与审批红线，就能**从配置首个 AI 员工演进到管理 29 个 Agent**。

## 第一个 AI 员工：像招聘一样定义岗位与权限

![第一个 AI 员工：像招聘一样定义岗位与权限](/info/18-solo-s1.png)

把 Bot 当作工具还是员工，取决于你是在写单次提示词，还是在确立岗位职责。单次提示词只管眼前的一项事务，窗口一关上下文就消失。岗位职责是一份固定的档案文件，它决定了这个 Bot 每天处理事务时的行为底线与思考模式。

### 岗位定义与准入测试

**先别给不可逆权限**，从枯燥、高频且易撤销的杂事切入。

让 Bot 上手前，先跑两项准入测试提前排错。
1. **一句话职责测试**：一句讲清交付什么。塞入四五个无关动词等于一人干三人活，出错没法定位根因。
2. **纯文字推演（Trial in text）**：耗时不到两分钟，先汇报步骤、预访网址与存疑判断。

岗位描述拆成五个字段划清边界。
- Owns：交付固定产物。
- Inputs：允许读取的渠道。
- May：可自理的操作。
- Must ask before：花钱或改配置等高危动作，**必须等人工审批**。
- Done when：客观核对的验收清单。

```text
先不要执行任何实际操作。请逐步向我推演你的完整执行方案：
1. 列出你准备依次打开的工具、网址与调用的插件。
2. 列出你在过程中需要做出的业务判断。
3. 标出你目前信息不足、存在疑虑或拿不准的决策点。
推演完毕后等待我的指令，严禁自行操作。
```

::: details 岗位定义与准入测试
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

岗位设定与临时提示词完全不同。

| 维度 | 临时提示词 | 岗位设定 |
|---|---|---|
| **目标与形态** | 单次对话，关注单次动作 | 长期配置，交付业务产物 |
| **边界与权限** | 口头交代易越权，出错重跑 | 可逆自理，不可逆等审批，硬设人闸 |

### 三次运行试用期与晋升阶梯

> 来源：[Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> 作者：[distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

新 Bot 刚跑通，**千万别直接放后台无人值守**，先按 distort 的「三次运行法则」测试。

1. 第 1 次（全程旁观）：盯着屏幕看每步操作，记下误读指令、丢上下文和瞎猜的地方。
2. 第 2 次（修复规则）：换同难度任务，不提醒旧错。重点看岗位规则与权限改动是否生效，不替它改结果。
3. 第 3 次（放手实测）：全程不插手，只在审批或达到重试上限时介入，核验完成度、干预次数、耗时与额度。

**通过三次测试后进入晋升阶梯**，分五级权限。

| 级别 | 机制 | 边界 |
| :--- | :--- | :--- |
| Level 0 | 仅观察 | 不改任何数据 |
| Level 1 | 仅准备 | 搜索、摘要与排版等可逆工作 |
| Level 2 | 人工审批 | 关键步骤挂起等待确认 |
| Level 3 | 独立运行 | 定时或触发运行，定期产出证据链汇报 |
| Level 4 | 多 Bot 协同 | 担任分发与质检节点 |

升到下一级必须满足四项**硬性指标**。
- 连续 5 次实跑无瑕疵
- 验证步骤全通过
- 无未解决的副作用
- 回滚机制验证可用

实践参考 [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) 与 [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)。

## 从零到运转的公司：幕僚长与专职团队编排

一个人使用 Grok Bot 搭建完整业务运转体系时，最容易走入的死胡同就是给单个 Bot 堆积太多能力。一个既管销售线索、又管内容写作、还管对账和改代码的 Bot，其上下文窗口很快会被大量不相干的偏好填满，不仅容易混淆业务语境，还会加速额度损耗。

### 幕僚长架构与部门拆分

搭团队先建幕僚长 Bot。你日常**只跟幕僚长对接**，由它拆解任务、调度专职岗位并汇总交付。

::: details 幕僚长架构与部门拆分
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

- 调研 Bot：论断须注日期与网址，存疑主动标出，不强行编造。
- 内容 Bot：按模版排版，**严禁直接对外发布**。
- 销售 Bot：拜访邮件全存草稿箱，等人工核准再发。
- 技术 Bot：提 GitHub PR 必附测试通过截图。
- 财务 Bot：涉及资金调整必须单独列出待确认。

::: details 幕僚长架构与部门拆分
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

| 架构 | 单兵全能 | 幕僚长流水线 |
|---|---|---|
| 协作 | 记忆混杂难定位 | **各岗独立记忆**，精准定责 |

### 证据链审查与四周信任转移

> 来源：[From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> 作者：[NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**想放心合上电脑，前提是看到凭证（Show the tape）。** Bot 交付必须带齐三项凭据。

- 操作录屏或调用记录：展示完整网页轨迹或工具调用序列。
- 数据与数字的原始出处：禁止无来源引用。
- 报错跳过项与推测结论说明。

**信任分四周逐步转移。**

1. 第 1 周（草稿阶段）：Bot 仅起草，人工通读并手动执行。
2. 第 2 周（审批阶段）：Bot 跑到关键步停下，人工仅核对动作并审批。
3. 第 3 周（异常上报阶段）：低风险事务自主跑，遇异常或越权才弹窗求助。
4. 第 4 周（例程巡检阶段）：按例程完全自主运行，周末只看审计报告。

相关实践参考 [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) 与 [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)。

## 一人公司实战：单台云电脑的边界与独立运营

### 物理边界

**同账户所有 Bot 共享单台电脑**，共用目录与会话。官方明确别把 Bot 当隔离边界，Prompt 防不住注入，误跑命令会泄露 Cookie 与 Session。

平时守住三条。
- 不登主网银和核心仓库，不存机密网盘。
- 外部平台只用最小权限子账号。
- 外部登录走 Handoff，人工输密码，Bot 只继承 Session。

### 无 API 系统自动化

**无 API 系统靠计算机能力点击填表**，四类工作适合先交接。
- 获客调研：扫社群目录并起草邮件。
- 履约跟进：核对缺货并跟进延误运单。
- 内容排期：文案填进草稿箱。
- 代码维护：排查独立站报错并出补丁。

::: details 无 API 系统自动化
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

### 门槛与评分

> 来源：[One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> 作者：[ZER @zerqfer](https://x.com/zerqfer)

**人工审查稳定降至每天 15 分钟内**才能加新 Bot，避免放大负担。每月填一次评分卡防静默衰退。

::: details 门槛与评分
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

参考 [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)。

## AI Agency 交付体系：月交付流水线与质检人闸

![AI Agency 交付体系：月交付流水线与质检人闸](/info/18-solo-s4.png)

对于面向多客户交付的 AI 代理机构（AI Agency），核心难点在于多客户并发时的质量稳定与额度成本控制。

社区作者 maestro 分享了单人服务 5 家 Retainer 客户、实现月度业务运转的体系架构（社区作者 maestro 自述月营 1.8 万美元、服务 5 家客户，未核）。

### 业务菜单的「三项准入测试」

别接全定制沦为手工外包，**业务进自动交付菜单得过三关**。

1. Brief 能写成结构化清单。
2. 交付物有第三方客观验收标准。
3. **此前纯手工交付至少 10 次**。没做满 10 次摸不清红线，交给智能体只会产出废话。

达标业务包含 500K 上下文比对 40 篇资料做研报、按声音样本（Voice File）批量写稿，或搭建看板与轻量抓取工具。

### 模型路由与 19.5 万 Token 计费悬崖拦截

模型按活分配，别全上旗舰。
- Grok 4.1 Fast：2M 上下文，跑清洗初筛。
- Grok Build 0.1：负责 80% 开发物料。
- Grok 4.6：500K，跑长程 Agent 与推理。

**输入超 200,000 Token 费率直接翻倍**。网关要**硬编码 195,000 Token 阈值**，超限报错截断或剪枝。

### 独立只读审核者与三次重试人闸

> 来源：[How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> 作者：[maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

生产 Bot 审自己的产物会有自洽倾向，容易掩盖提示词失效。**审核必须切成独立的只读回路**。

- 独立上下文：只输入原始 Brief、客户规范和产物，不给中间推理。
- 严格只读：**发现缺陷只报 FAIL 绝不代笔**，防止私自修补掩盖问题。
- 对抗挑刺：专抓硬伤，没有资料支持的数字一律判挂。

::: details 独立只读审核者与三次重试人闸
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

**交接重试最多 3 次**，防止死循环刷出高额 Token 账单。机器试了三次仍不达标，说明需求冲突，必须由人工介入判定。

参考 [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)。

## 29 个 Agent 的实战：如何从单兵平滑扩编到军团

![29 个 Agent 的实战：如何从单兵平滑扩编到军团](/info/18-solo-s5.png)

当你熟悉了单个员工的配置与双 Bot 的质检闭环，业务需求自然会推动你扩建团队。

社区作者 Melvin Vivas 记录了自己如何一步步将 Grok Bot 扩充至 29 个专职智能体的完整实践（社区作者 Melvin Vivas 自述拥有 29 个 Bot，未核）。

### 29 个 Agent 的职能布局与渐进演进

**这 29 个 Bot 全是按需长出来的**：平时遇到重复事务就建专职角色，角色多了再由幕僚长 Emma 统管。业务分为七大板块：

- 调度中枢：Emma 负责统管全局与分发任务。
- 技术研发：CTO 管架构；**Coder 调动 Cursor 自动编写代码提 PR 并修复报错**，全程不用开本地编辑器。
- 前沿调研：全天扫描 X 平台开源动态并出简报。
- 内容矩阵：负责各渠道文案创作与复盘。
- 商务拓展：挖掘商机与合作线索。
- 运营安全：负责邮件、备份与安全审查。
- 个人成长：处理打卡、行情追踪与决策论证。

### 多 Agent 协同流水线：以技术原型到内容转换为例

各 Bot 靠共享云电脑和会话引用接力。

::: details 多 Agent 协同流水线：以技术原型到内容转换为例
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

**改动不用挨个点开 29 个窗口**，总管广播一条指令几秒就能同步。

### 角色拆分的五大信号与自动化七步法

考核目标、调用工具、工作风格、审批边界（草稿与对外沟通绝不能混）或调度周期不同时，必须**拆分独立 Bot**。

1. Bot Description 写清目标、数据源、格式与停机边界。
2. 挑受控真实任务单次运行。
3. 人工调优到免检。
4. 沉淀为复用 Skill。
5. 换新数据复测泛化。
6. **定好重试上限与缺失报警，才开 Routine**。
7. 发信、付款或改动，强绑 Require Approval 人闸。

| 阶段 | 规模 | 架构与瓶颈 |
| :-- | :-- | :-- |
| 1 单兵 | 1 Bot | 全量人闸验证闭环；需时刻盯盘 |
| 2 小组 | 2-3 Bot | 生产与审核分离；日维护压进 15 分钟 |
| 3 幕僚长 | 4-6 Bot | 分发与看板；**杜绝幕僚长干杂活** |
| 4 军团 | 10-30 Bot | 多线 standup；定期修剪无效例程 |

### 看板系统与晨会机制

> 来源：[How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> 作者：[Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Bot 超过 5 个就别用多聊天窗口了，根本看不过来。**多 Bot 协同主要靠看板和定时巡检两件事**：

- **共享状态看板**：任务别散在聊天记录里，统一收拢到 Notion 或数据库看板，定好五种状态：`Todo`、`Working`、`Blocked`、`Ready for Review`、`Done`。

  Bot 遇到未知报错或缺权限直接改标 `Blocked` 并呼叫人工，平时看卡片流转就行。
- **定时巡检与对账**：单 Bot 最多配 50 个 Routine，最高每 5 分钟跑一次。

  **凌晨 3:00 自动体检代码死链与包体积，5:00 由总管 Bot（如 Jenny）逐个核对专职 Bot 的 Playbook**，能有效防止模型久了遗忘。

```text
全体专职 Bot，开始进行本周团队回顾审计。请各岗位汇报：
1. 本周你实际执行了多少次任务，其中失败或异常的中断有多少次？
2. 在执行过程中，有哪些步骤存在推测行为、跳过行为或由于数据缺失强行拼凑的情况？
3. 有哪些挂起的审批事项我一直没有回应？有哪些生成的物料我从来没有打开查看过？
4. 请指出：在当前的工作流中，你发现哪两个 Bot 存在职责重叠或重复工作？
5. 给出客观建议：为了节省整体用量额度，我们下周最应该裁撤哪一个无效的 Routine 或岗位？
```

相关实践参考 [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)、[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54) 与 [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)。

## 容易踩的坑

### 权限与审批
1. 共享云电脑共用 Session 无隔离，**绝不要登录主账户和敏感系统**。
2. Require Approval 只能拦未执行操作，无法撤销破坏，**高危动作首次就设死人闸**。
3. 审批约 10 分钟不理会失效（Lapse），夜间**必须配 Allow rule 白名单或停在草稿**。

### 成本与架构
4. 输入超 20 万（200,000）Token 单价翻倍：**路由层要设 195,000 Token 硬拦截与剪枝**。
5. 别搞单 Bot 揽全活或克隆 5 个通用 Bot，**分工不清只会污染上下文并浪费额度**。
6. 别设 5 分钟轮询或监听全消息，**缺 No-data policy 时断网容易瞎编数据耗尽额度**。

### 规则与交接
7. 聊天框叮嘱刷新就失效，**跨任务纪律必须写在设置界面的 Description**。
8. 跨 Bot 别搬运全部记录，**交接包只留目标与交付物路径，加上结论和下一步要求**。

## 做完怎么验收

1. **查凭据**：清掉 Plugins 和浏览器的银行与主凭据，改用子账号或 Session，**聊天记录绝不存明文密码**。
2. **验岗位**：Bot 须包含 Owns/Inputs/May/Must ask before/Done when，末尾加反漂移声明，**缺数据立即报错、严禁编造**。
3. **测人闸**：发扣款或删除指令，必须 **100% 触发 Require Approval 挂起**。
4. **抗审核**：喂假数据草稿，质检 Bot 须 **第一行返回 FAIL** 且不擅改；连续失败 3 次停机报警。
5. **稳例程**：看板状态实时流转，开启前点 Test run 跑通，**定时任务不依赖超 10 分钟夜间审批**。

## 延伸阅读

### 官方文档

- [在 Grok Bot 中组织业务与工作（docs_grok-bot_work.md）](https://cursor.com/cn/docs/grok-bot/work.md)
- [团队版 Bot 协作与权限管理（docs_grok-bot_teams.md）](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Grok Bot 安全架构与执行环境（docs_grok-bot_security.md）](https://cursor.com/cn/docs/grok-bot/security.md)
- [方案、额度与计费说明（help_grok-bot_plans.md）](https://cursor.com/cn/help/grok-bot/plans.md)
- [配置定时任务与触发例程（help_grok-bot_routines.md）](https://cursor.com/cn/help/grok-bot/routines.md)
- [连接外部应用与官方插件（help_grok-bot_connect-plugins.md）](https://cursor.com/cn/help/grok-bot/connect-plugins.md)

### 社区实战来源

> 来源：[GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
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
