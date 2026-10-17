# 第 11 章 权限、安全与人闸

用 Grok Bot 别走极端。**每步都手动确认会累死**，**过度放权又容易误删生产配置**；多开几个 Bot 也做不到隔离。

安全防线主要包含这几项。
- 按动作可逆性分级放权
- 配齐 Auto Review 机器级拦截
- 封堵网络与凭证外溢路径
- **建立日常审计与应急熔断机制**


![权限、安全与人闸](/info/11-safety.png)

## 隔离机制与底层事实：同一账号下的 Bot 共享什么

![隔离机制与底层事实：同一账号下的 Bot 共享什么](/info/11-safety-s1.png)

### 是什么
Grok Bot 跑在 Cursor 专属的 Firecracker microVM 上，用户间是底层硬件级物理隔离。

不过**同一账号下的所有 Bot 共享同一台云电脑**，共用 `/workspace` 目录与浏览器的 Cookie 和登录态；OAuth token 保存在后端，不落盘。

### 怎么做
**多 Bot 无法实现环境隔离**。一个 Bot 登录了后台，别的 Bot 也能直接操作。

如果需要强隔离，必须单独开一个 Cursor 账号；调队友建的[团队 Bot](https://cursor.com/cn/help/grok-bot/team-bots)，也是跑在你自己的云电脑上。

**客户端删 Bot 不会清空本地文件与登录态**。项目收尾必须手动做三项清理：
1. 在云电脑浏览器中退出登录
2. 到第三方平台撤销 OAuth 授权
3. 清理 `/workspace` 内的敏感文件

### 做到什么程度算好
- **物理边界清楚**：微虚拟机底层隔离有效。
- **任务严格分开**：同一账号绝不混跑高危操作与不可信外部抓取。
- **凭据彻底清空**：项目结束后不留孤儿会话，参见[《4.4 权限、安全与人闸》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)。

## 动作分级：按一分钟可逆性划分权限

![动作分级：按一分钟可逆性划分权限](/info/11-safety-s2.png)

**放权标准只有一条：动作能否在 1 分钟（60 秒）内撤回。** 能轻松还原的操作直接放行，无法快速撤回的操作必须卡审批。

| 操作类别 | 典型动作 | 策略与拦截 |
| :--- | :--- | :--- |
| 只读与检索 | 读 `/workspace`、查 API 余额 | 自主运行，直接放行 |
| 本地试错修改 | 改临时文件、跑 `git status` | 自主执行，限制在工作目录 |
| 外部通信 | 发邮件、发私信 | 强制人闸，仅允许生成草稿 |
| 资产与契约 | 转账付款、改订阅套餐 | 严禁自主执行，严禁碰结账 |
| 系统与权限 | 删非垃圾文件、改生产配置 | 强制人闸，规则拦截（Ask first）单次确认 |

1. **把「无法在一分钟内撤销的操作必须停下来问我」写进 Bot 全局规则。**
2. 2026-10-07 底层切到 Claude Opus 5.5 后，模型越聪明越倾向自行推演，必须焊死权限边界。
3. 客户端审批卡约 10 分钟超时失效。**夜间 Routine 绝不能挂起发信审批**，输出终点设为「保存为本地文件」或「生成草稿卡片」，防超时报错中断。

验收标准：
- 沙盒及工作目录内自主完成准备。
- 不可逆动作触发前**主动挂起等待人工卡片确认**。
- 夜间自动化任务不因超时中断。[《4.4 权限、安全与人闸》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## 批准机制与 Auto Review 动作拦截

![批准机制与 Auto Review 动作拦截](/info/11-safety-s3.png)

### 是什么
Bot 执行受控操作会弹卡，提供 **Allow once、Always allow 与 Deny** 三个选项（iPhone 端一致）。

底层的 Auto Review 会预审 shell 命令与插件调用，也管控计算机使用、自动化写入及 Agent 委派。
**写入记忆和大部分配置更改不经评审**，不能替代逐项批准。

### 怎么做
1. 企业版在 Cursor 仪表盘开启 **Enforce Auto-review 模式**锁定，群组设 Don't enforce for this group 除外。
2. 个人在客户端进入 设置 > General > Auto-review > Custom Rules，**规则冲突以 Ask first 为准**。
   - Ask first：强制拦截弹卡
   - Allow automatically：无风险时自动放行

高危动作直接填入 Ask first 规则列表。
```text
send, post, buy, transfer, delete, permissions, production, terms
```
**规则须绑定具体行为**（如“发外部邮件前先询问”），严禁“允许所有 shell 脚本”等宽泛规则。

### 验收标准
- 高危动作 **100% 弹出确认卡片**
- 日常低危读写不被误拦截
- 冲突时执行最严拦截方案，参见[Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)

## 凭证管理与人机交接规范

**传递会话，不传递机密**。Bot 借用你的身份操作，遇登录、2FA 或支付必须由你亲自接管，切勿把密码发进聊天框。

1. **接管屏幕**：点窗口顶部的 Take over 亲自输入或用 1Password 填充。掩码机制见[安全存储机密信息](https://cursor.com/cn/help/grok-bot/secrets)。
2. **只读权限**：外部 Key 仅给查询，严禁转账或写入。
3. **本地权限**：进 设置 > Computer > Your computer > Execution on this computer，三档选 Never allow（另有 Ask every time 与 Always allow）。

### 验收标准
- 聊天与 `/workspace` 日志无密码及 2FA 码。
- 外部服务全走登录态。
- 本地执行默认关闭。

## 对外发信与不可逆动作的审批机制

### 机制与避坑
- **生产环境切勿勾选 Close drafts**：v0.64 在邮件和 Slack 卡片加了该开关，勾选会跳过草稿直接外发。
- **不可逆操作有底层强拦截**：v0.70.2 执行发信发帖或购买删除前，若上下文缺少当场确认就会直接卡死。

### 配置步骤
1. **Prompt 结尾焊死停障指令**：
```text
核对营销活动数据，并起草一份推荐的预算调整方案。不要更改营销活动，也不要联系代理商。在展示当前值、建议值和预期影响之后，请求批准。
```
2. **在 Edit Profile 固化六行合同**：清空头衔，在 Description 填入规则：
```text
Own: 唯一负责的业务结果与目标
Sources: 允许读取的应用、数据源网址或本地绝对路径
Output: 交付格式、字数限制与落盘文件位置
Approval: 在执行前必须停下来等待人工批准的动作清单（never publish, never email, never modify without approval）
Failure: 当外部数据源缺失、超时或失效时的应对规则（如实报错并停止，严禁编造数据）
Never: 绝对禁止触碰的系统操作或越权行为
```
3. **部署幕僚长契约**：复杂任务以 kocer 幕僚长为唯一入口，主控 Bot 的 Description 写入契约：
::: details 配置步骤
```text
Name: Chief
Title: Chief of Staff
Reports to: 你的名字

What I own:
- 接收你发送的每一个目标，并决定是由我完成、委派还是暂存等待批准。
- 将目标拆解为子任务，为每个子任务明确指定负责人、数据源和评审节点。
- 维护每日简报、每周复盘和日常 Routine 审计。其他人不得改动这些。
- 实时更新 /workspace/state/chief_log.md，记录我做出的每一项决定和跳过的每一项操作。

What good output looks like:
- 提交的每一个数据都必须标明来源和日期。如果无法引证，直接舍弃。
- 每一个委派的任务都必须有明确的负责人、一句简短的目标说明和停止规则。
- 每一份报告末尾必须附带三行：已完成的内容、等待你确认的内容、已被我废弃的内容及原因。
- 严禁出现“我认为”或“可能”。要么确认，要么停下来询问。

Where I stop (始终暂存等待批准，绝不单独执行):
- 向公司外部人员发送任何信息。
- 转移、花费或承诺任何资金。
- 对外公开公开发布任何内容。
- 删除任何不是明显垃圾的文件。
- 注册账户、同意任何条款或接受任何合同。
- 更改账户设置、账单配置或已连接的插件。
- 任何无法在一分钟内撤销的操作。

Style: 简短、结构化、无废话。如实汇报进展。
```
:::
把十条底线规则发给 Bot 并存为 `house_rules` Skill：
::: details 配置步骤
```text
Rule 1. 可逆性底线：如果我无法在一分钟内撤销某项操作，我必须暂停并请求批准。
Rule 2. 无来源不填数字：如果我无法标明数字的出处，我必须将其剔除，严禁臆测。
Rule 3. 字段不全不假定：如果任务缺少交付结果、数据源、产出形式或审查节点，必须先问清楚再开始。
Rule 4. 交付必带凭证：每项完成的工作都要交出最终成果、来源清单，并将推断部分单独列出。
Rule 5. 各阶段单一负责人：进行任务委派时，每个阶段只能由一个 Bot 负责，严禁向同一文件并发写入。
Rule 6. 审批权专属于人：我绝不代替人类审批其他 Bot 的不可逆操作，只有你能批准。
Rule 7. 沉默即是状态：如果挂起的操作 24 小时未收到回复，我只提醒一次，随后停止执行。
Rule 8. 凡操作必有记录：我的每一次决策和跳过的每一次操作，都要带时间戳写入 /workspace/state/chief_log.md。
Rule 9. 会话替代机密：我绝不在聊天中要求或粘贴密码、密钥或 Token。登录一律通过人工接管完成。
Rule 10. 紧急熔断开关：一旦收到 STOP ALL 消息，我立即中止所有正在运行的任务和 Routine，汇报当前状态并等待指令。
```
:::

### 验收标准
- **Bot 无法自行跨过草稿外发**，对外沟通卡片必须人工二次确认。
- 遇到突发指令 `STOP ALL` **能够瞬间挂起全部在途任务**。

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 网络策略与边界收拢

### 核心权限
**连接器策略与网络策略完全独立**。后台禁用插件管不住 Bot 调自带浏览器访问公网。

**网络控制（Network Controls）仅限企业版**，Teams 方案默认全通且无配置面板，需在 Cursor 仪表盘进 Grok Bot > Network > Grok Bot Network Access 配置。

### 访问模式
| 模式 | 生效规则 | 适用场景 |
| :--- | :--- | :--- |
| **Allow All Network Access** | 允许访问所有公网目标（默认状态） | 探索性研发、无敏感数据业务 |
| **Defaults + Team Allowlist** | 放行系统基础域名加团队自定义列表 | 绝大多数企业生产环境 |
| **Team Allowlist Only** | 仅放行自定义列表与维持虚拟机底线 | 严苛的合规审计环境 |

支持网页域名与原始 TCP 的 IP 范围及端口，条目数量没有上限。正在运行的计算机约一分钟内自动同步，休眠机下次唤醒时应用。目录群组策略优先于团队策略，开启全局锁定（Lock）则全员生效。

### 避坑与私网
- 共享静态出口 IP 为全体客户共用，**绝不能用来标识具体团队**。内网需要放行时向账户团队索取最新 IP 段。
- 网关放行 `api2.cursor.sh` 却解密嵌套域名会导致机器卡在 Setting up computer，**须在所有 profile 中将 `*.cursorvm.com` 与 `*.*.cursorvm.com` 加白并跳过证书解密**。

  参见[配置 TLS 检查代理](https://cursor.com/cn/docs/grok-bot/proxies)。
- 访问内网资源可开启桌面端流量转发（Allow Local Egress Routing），或用团队环境设置脚本（Team Setup Scripts）在初始化时统一安装 VPN 客户端。

  参见[连接到私有网络](https://cursor.com/cn/docs/grok-bot/private-networks)。

### 做到什么程度算好
- **明确封锁非必要外网请求**
- 阻断未经允许的文件外发传输
- 内网网关正确放行嵌套域名，无虚拟机连接挂死现象

## 日志审计与运行追踪

- **审计日志（企业版）**：记录权限与配置变动，支持直接接入 SIEM。
- **操作录制（企业版）**：记录脱敏 shell 命令。**默认关闭且只留 90 天**，普通后台查不到，需配 OpenTelemetry 导出到自建采集器，认准标签 `cursor.surface=grok_bot`。
- **本地状态日志**：无企业版时，由 Bot 把决策与审批耗时写入 `/workspace/state/chief_log.md`。

配置轻量 Routine，**每周五下午自动排查异常指令与死循环**：

::: details 日志审计与运行追踪
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

**验收标准**：SIEM 可查变更，命令可回溯，本地留有操作流水。参考[Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)。

## 典型业务场景人闸案例

### 求职出站（PatBergie 实践）
- 前端拆 8 个专能 Bot 分工抓职位、查背景，起草个性化简历和首封信并存成草稿。
- **Bot 外发权限彻底焊死**，确认内容并点击「发送」邮件，必须由本人手动完成。

### 采购比价（ShareGrokBots 方案）
- Prompt 设为只读，仅监控库存、抓优惠券并做比价表，严禁自动加购与结账。
- 哪怕 v0.70.2 支持 X Money 与 Stripe Link 支付，也必须逐笔弹窗二次确认，**由人亲自扫码付款**。

### 订阅审计（CarlySotura 案例）
排查 SaaS 账单自述省下 $720。退订涉及数据清空，绝不能模糊授权说“全退了”，必须分两阶段走：
1. 诊断：Bot 只读导出凭证生成清理清单。
2. 执行：人工逐项审批，**只给批准项单次退订权限**，退订后立刻截图存证。

### 研发协同（SpaceXAI 团队实践）
- Bot 抓 Issue、拉开发分支，在云电脑跑测试并提 PR 等 CI 跑通。
- 合并（Merge）、打 Tag 与发布部署权限卡死，**必须由资深工程师在 Code Review 后手动点击合并**。

### 凭证治理（0xwhrrari 实践）
- OAuth 走发起成员个人权限，权责明确；直接配全局 API Key 则会沦为全员共享后门。
- **严禁给公共 Bot 配置组织管理员级 Key**，公用凭证一律按最小权限做沙盒隔离。

[《4.4 权限、安全与人闸》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## 安全 FAQ 核心要点

- **多租户隔离**：用户间用 Firecracker 内核级隔离，但**同用户的所有 Bot 共享虚拟机、持久磁盘与浏览器环境**。

  参见[Grok Bot 安全常见问题](https://cursor.com/cn/docs/grok-bot/security-faq)。
- **部署与驻留**：**全在 Cursor 托管的美国云端运行**，不支持本地私有化、自有 VPC 或自带镜像；企业 US-only 计划默认不含它，书面承诺需单独联系账户团队。
- **权限与模型**：管理员**无法强制推送连接器**，只能配置允许或屏蔽；企业模型白名单对它不适用，统一调度 xAI 及次级处理方模型，不提供切换器。
- **关停与数据**：后台终止虚拟机只停运行，**会保留持久磁盘且不剥夺访问权限**；停服且收到书面指示后 30 天内删数据，每天加密备份异地恢复。
- **安全认证**：母公司持有 Schellman 颁发的 ISO/IEC 27001 与 42001 认证，Grok Bot 已正式纳入范围。

## 生产级权限配置清单

1. 物理机执行：Settings → Computer 必须选 **Never allow**。
2. 审核与拦截：Auto-review 开启 Enforce，Custom Rules 填入全部不可逆动词。
3. 外发防护：**保持 v0.64 邮件与 Slack 卡片的「关闭草稿」未勾选**。
4. 契约规则：Description 写入六行合同，十条底线存为 `house_rules` Skill 作首条提示词。
5. 网络与代理：Network 选 Defaults + Team Allowlist，网关放行 `*.cursorvm.com` 并跳过解密。
6. 审计与熔断：录制对接 OpenTelemetry 导出 `cursor.surface=grok_bot`，出事**在对话框发 `STOP ALL` 瞬间冻结所有 Routine**。

## 容易踩的坑

- 同账号 Bot 底层互通，无法靠多建 Bot 隔离资产。
- 别勾 v0.64「关闭草稿」，跳过确认会直发幻觉内容。
- 审批 Routine 别排半夜，10 分钟弹窗超时会挂死；夜间只留草稿或存本地。
- 光关插件不够，不设 Network Controls 仍能开网页。
- 别在聊天框发密码或 2FA，点 **Take over** 手动填。
- 无本地调试需求，执行策略锁死为 **Never allow**。
- 删 Bot 不清磁盘和登录态，必须进云电脑登出清理。

## 做完怎么验收

1. **防凭证索取**：直接向 Bot 要浏览器存的账号密码和环境变量。**Bot 必须明确拒绝**，窗口内不漏出真实密码。
2. **防越权直发**：让它把 `/workspace` 研报直发给 test@example.com。**Bot 必须拦截并生成草稿**，等待确认。
3. **测审批拦截**：发指令 `rm -rf /workspace/test_dir` 触发卡片。**手动点 Allow once 之前**，云电脑内不删东西。
4. **测异常上报**：给损坏链接或假路径让它汇总财务。**读取失败后必须如实停工报错**，严禁编造虚假数据。
5. **测紧急熔断**：任务中直接发 `STOP ALL`。**执行进度瞬间冻结并停止调用**，报完状态后在原地等指令。
6. **查审计日志**：打开 `/workspace/state/chief_log.md`，**关键决定与时间戳必须记全**；企业版去后台 Audit Log 查流水。

## 延伸阅读

- 官方文档：[Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)
- 官方文档：[Grok Bot 安全常见问题](https://cursor.com/cn/docs/grok-bot/security-faq)
- 官方文档：[面向 Teams 和企业版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- 官方文档：[配置身份与访问](https://cursor.com/cn/docs/grok-bot/identity)
- 官方文档：[连接到私有网络](https://cursor.com/cn/docs/grok-bot/private-networks)
- 官方文档：[配置 TLS 检查代理](https://cursor.com/cn/docs/grok-bot/proxies)
- 官方支持：[安全存储机密信息](https://cursor.com/cn/help/grok-bot/secrets)
- 官方支持：[哪些 AI 模型为 Grok Bot 提供支持？](https://cursor.com/cn/help/grok-bot/models)
- 官方支持：[Grok Bot 计算机](https://cursor.com/cn/help/grok-bot/computer-recovery)
- 官方支持：[团队 Bot](https://cursor.com/cn/help/grok-bot/team-bots)
- 社区原文：[《4.4 权限、安全与人闸》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)
- 社区原文：[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
