import json,os,textwrap
R="/workspace/grok-bot-learn"; D=R+"/site/docs"
t=json.load(open(R+"/sources/feishu/tree.json"))
F={i:(x[2],"https://jcng5q8n0f3z.feishu.cn/wiki/"+x[1]) for i,x in enumerate(t)}
def f(i): return f"[{F[i][0]}]({F[i][1]})"
def c(p,title=None): return f"[{title or p}](https://cursor.com/cn/{p})"
OLD={7,8}
def w(path,s):
    p=D+"/"+path; os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(textwrap.dedent(s).strip()+"\n")
def src(*items): return "\n## 来源\n\n"+"\n".join("- "+x for x in items)+"\n"
OUT="\n::: danger 已过时\n本文记录的是 8–9 月旧开发者积分/旧资费规则，已被 2026-10-12～13 推行的 X 统一订阅取代，仅作历史参考。\n:::\n"
def stub(path,title,points,sources):
    w(path,f"# {title}\n\n::: info 提纲\n本页目前为提纲，正文待补充。\n:::\n\n## 要点\n\n"+"\n".join("- "+p for p in points)+"\n"+src(*sources))

# ---------- 首页 ----------
w("index.md",f"""
---
layout: home
hero:
  name: Grok Bot 学习站
  text: 从第一个 Bot 到一支 AI 团队
  tagline: 基于 Cursor 官方文档 + 《Grok Bot 焚诀》知识库整理
  actions:
    - theme: brand
      text: 开始入门
      link: /start/what-is
    - theme: alt
      text: 核心概念
      link: /core/bots
features:
  - title: 🐣 路径一：新手
    details: 是什么 → 方案选择 → 快速入门 → 第一次好的交接。先跑通一个专职 Bot。
    link: /start/what-is
  - title: 💰 路径二：省额度的个人用户
    details: 例程频率、群聊回复、备份恢复——让每周用量撑满一周。
    link: /advanced/usage
  - title: 🏢 路径三：团队与工程
    details: 团队编排、权限与人闸、团队 Bot、企业身份与私有网络。
    link: /advanced/team-orchestration
---

::: warning 规则变动提示（2026-10-14 更新）
- **2026-10-12～13 官方推行 The X Subscription 统一订阅**（Plus / Premium / Super / Ultra，Grok、Grok Bot、Cursor 共享每周用量池；Plus 档不含 Grok Bot）。详见 {f(16)}。
- 8–9 月关于「绑定 X 送开发者积分」和旧资费的文章（{f(7)}、{f(8)}）**已过时**。
- 社区与官方帮助中心的方案描述可能不同步，开通与付费**以官方方案页和 changelog 为准**：{c('help/grok-bot/plans','方案和计费')}。
:::

## 本站怎么读

| 章节 | 内容 | 状态 |
|-|-|-|
| [入门](/start/what-is) | 是什么、怎么选、方案、快速入门、FAQ | ✅ 已写 |
| [核心概念](/core/bots) | Bot、消息、共享电脑、记忆、技能与例程、插件、群聊 | ✅ 已写 |
| [进阶](/advanced/usage) | 额度、编排、自动化、安全、备份、飞书/微信 | 📝 提纲 |
| [实战案例](/cases/) | 社区长文摘要 + 原文链接 | 📝 摘要索引 |
| [团队与企业](/admin/) | 身份、私有网络、代理、部署 | 📝 提纲 |
| [资源](/resources/) | 提示词、术语、时间线 | 📝 提纲 |
""")

# ---------- 入门 ----------
w("start/what-is.md",f"""
# Grok Bot 是什么

Grok Bot 提供**可长期协作的 AI 队友**：每个 Bot 有名称、职责和会随时间积累的上下文，并在一台配备**浏览器、文件系统和终端的持久化云端电脑**上干活——所以任务直接在真实工具里完成，而不是停在聊天草稿里。

## 它和普通聊天助手的区别

- **每个 Bot 都有一台电脑。** 能用插件就用插件，没有插件就用"电脑操作"（computer use）点网页；合上笔记本工作也继续。
- **设置就是发一条消息。** 不需要工作流搭建器：创建 Bot、描述任务、按它的要求授权即可。
- **Bot 之间能协作。** 并行运行、互发消息、群聊共享上下文、交接任务所有权。
- **演示一次就能学会。** 带它走完一遍多步骤流程，它能存成技能并按计划重复执行。
- **上下文持续积累。** 记忆、文件、浏览器会话、偏好跨会话保留。

## 必须知道的三条边界

1. **所有 Bot 共用一台电脑。** 文件、浏览器登录态、已装工具对你名下所有 Bot 可见；不同用户之间严格隔离。
2. **分 Bot ≠ 安全边界。** 研究 Bot 登录过的网站，财务 Bot 也能用。敏感资产不要指望靠"拆 Bot"隔离。
3. **对话上下文彼此隔离，交接靠落盘。** Bot 读不到彼此的私聊；协作时把产出存到 `/workspace` 固定文件里。

## 什么样的活适合交给它

用三条标准筛：**能否在网页/API 上完整跑通**、**结果能否被人核验**、**敏感步骤能否停下来等你确认**。高频重复、可离线巡检、产出明确的任务最合适；纯本地代码重构仍适合本地命令行 Agent。

## 新手最常见的坑

- 一上来建十几个 Bot → 额度耗尽、流程失控。**先跑通一个专职 Bot。**
- 让主 Bot 亲自干所有细活 → 总控失焦。主 Bot 负责派活与验收。
- 每 5 分钟无过滤轮询 → 几天吃完一周额度。
- 把密码贴进对话框 → 一律在云电脑画面里自己输入。

## 平台

桌面端支持 macOS（Apple silicon / Intel）、Windows（x64 / Arm64）、Linux（x64 / Arm64），移动端支持 iPhone；Bot 用的电脑运行在 Cursor 云中。
{src(c('docs/grok-bot','官方：Grok Bot 总览'), f(2), f(1))}
""")
w("start/compare.md",f"""
# 和 Muse、Hermes、dots、Cue 怎么选

铁柱的比喻：Grok Bot 和 Muse 像**品牌整机**——开箱即用，但有平台边界；Hermes 像 **DIY 组装机**——自由度高，要自己维护。

| 产品 | 中心对象 | 特点 | 适合 |
|-|-|-|-|
| **Grok Bot** | 岗位分工（多 Bot、团队 Bot） | 共享云电脑、多 Bot 异步协作、例程与技能 | 团队业务自动化、检索、巡检、跨 Bot 交接 |
| OpenAI dots | 个人主 Dot | 常驻、自带云电脑（2026-09-30 发布） | 个人伴随、日常代办 |
| Manus Cue | 独立身份 Agent | 独立邮箱/电话/钱包，便利与风险同步放大 | 自主跑腿、跨平台注册 |
| Meta Muse | 个人生活与社交 | 深度整合 Meta 生态 | 家庭日程、生活琐事 |
| Hermes | 自定义节点 | 开源自建 | 极客定制、本地深度自动化 |

## 取舍建议

- 多岗位交接、共享文件、定时巡检 → **Grok Bot**。
- 纯代码实现与终端调试 → 保留本地 CLI Agent（Codex CLI / Claude Code 等）。
- 偶发即时问答 → 普通对话模型即可，不值得常驻一台云电脑。
- 新上线的自主 Agent → 不要直接放开真实资产与全局发信权限。

## 落地三步

1. 列出想自动化的任务，逐条标注：能否网页/API 闭环、是否可验收、是否涉及不可撤销操作。
2. 把"高频重复、可巡检、产出明确"的划给 Grok Bot。
3. 每项任务标明归属工具与**停止确认点**。
{src(f(3), f(21))}
""")
w("start/plans.md",f"""
# 方案与订阅

::: warning 规则变动频繁
官方帮助中心与 2026-10-12 起的 X 统一订阅说法并存。下单前务必打开官方页面核对：{c('help/grok-bot/plans','方案和计费')}。
:::

## 官方帮助中心口径

- 所有**付费个人 Cursor 方案**（Pro / Pro+ / Ultra）和 **Cursor 团队版**都包含 Grok Bot，用同一个 Cursor 账户登录即可，层级越高每周用量越多。
- 也可**关联个人 SuperGrok / SuperGrok Plus / SuperGrok Heavy / X Premium+**，或用自助式 **Grok Business** 席位通过 *Sign in with Grok* 登录。SuperGrok Lite 不含 Grok Bot。
- 关联是一项**用量授权**，不改变你的 Cursor 方案，两者用量**不叠加**。
- **每周用量**每周重置；用尽后若开启按需，可继续按需计费。团队版默认启用按需。
- 用量按**智能体步骤和 token** 扣除，而不是按消息条数；macOS 与 iOS 共享同一用量池。
- 免费试用给的是**额度**，同时有 7 天期限；大任务可能一次用光，且不补发。

## X 统一订阅（2026-10-12～13 起，社区解读）

- X Premium、Grok、Grok Bot、Cursor 合并为 **The X Subscription**，分 Plus / Premium / Super / Ultra 四档，另有 \\$0 免费档；年付为月付 10 倍。
- 每个付费席位**每周一个共享用量池**，Grok、Grok Bot、Cursor 共用；只覆盖官方自家模型。
- **Plus 不含 Grok Bot**，至少 Premium。
- 老订阅切换后**永久生效、无法撤销**，先算清楚再切。

## 怎么选

- 先确认自己要不要 Bot：只聊天/生图 → 不需要含 Bot 的档。
- 个人轻度使用 → 最低含 Bot 的档位 + 节制例程频率。
- 多 Bot、多例程、团队 → 看每周用量与按需上限。

::: danger 已过时内容
{f(7)}、{f(8)} 中的"绑定 X 送 \\$100 开发者积分"旧玩法与旧资费已被新规取代。
:::
{src(c('help/grok-bot/plans','官方：方案和计费'), c('help/grok-bot/supergrok','官方：关联 SuperGrok'), c('help/grok-bot/mobile-purchase','官方：移动端购买'), f(16), f(18))}
""")
w("start/quickstart.md",f"""
# 快速入门：第一个 Bot

## 1. 安装与登录

1. 从 [Cursor 仪表盘的 Grok Bot 页面](https://cursor.com/dashboard/bot) 下载桌面端（没有仪表盘权限就找管理员要链接）；iPhone 在 App Store 安装（iOS 18+）。
2. 欢迎页选 **登录**，在浏览器完成认证。用的就是 Cursor 账户，SSO 自动生效。
3. 使用旧版隐私模式的账户会被提示切换（Grok Bot 需要云端存储）。

## 2. 认识第一个 Bot

登录后系统自动创建一个名为 **Grok Bot** 的 Bot。要更多 Bot：侧边栏 **+ 新建聊天 → 创建新 Bot**（团队里可选"创建新团队 Bot"）。

**在第一条消息里给它一个主要职责，并让它记住。** 聚焦职责的 Bot 比"万能助手"积累的上下文更有用：

```text
你的职责是产品性能。使用我们的可观测性工具调查性能问题。
保留链接和截图，区分证据与假设，优先说明影响最大的问题。
绝不更改生产环境设置。请记住这些要求。
```

社区推荐的"六行合同"写法（Own / Sources / Output / Approval / Failure / Never）：

```text
Own: 负责监控目标清单的每周功能与定价变动
Sources: 关注名单、目标官网 Changelog
Output: 不超过 8 条核心动态，附日期与原始链接，存入 /workspace/scan.md
Approval: 严禁对外发布内容，严禁主动发邮件
Failure: 页面打不开就标为缺失，严禁推测或编造
```

## 3. 第一个任务

好请求 = **预期结果 + 重要来源 + 约束 + 交付物 + 在哪里停下交给你**。五分钟出结果的例子：

```text
用五个要点总结这份文档。在单独的部分列出每个日期、决策和
未解决的问题，并注明对应章节。不要更改源文件。
```

## 4. 登录它需要的工具

Bot 遇到登录页会把电脑控制权交给你：点 **打开计算机** → 接管 → 自己输密码/两步验证 → 交还。Bot 看不到密码，会话保留供以后使用。支持的服务也可以直接连插件。

## 5. 审查、修正、固化

提修改意见，说清长期偏好（比如固定的报告格式）。流程稳定后存成[技能或例程](/core/skills-routines)。允许 Bot 改外部系统前，先读[权限与人闸](/advanced/security)。

## 验收清单

- [ ] 侧边栏能看到 Bot 处于就绪状态
- [ ] 发中文问候，回复是中文（Bot 名字起中文名更容易默认中文）
- [ ] 右侧能调出云电脑实时画面
- [ ] 第一份交付物已保存为文件
{src(c('docs/grok-bot/get-started','官方：快速入门'), c('help/grok-bot/onboarding','官方：上手'), f(2), f(24)+"（摘要见实战案例）")}
""")
w("start/first-handoff.md",f"""
# 一次好的交接

从一项**需要几个工具、完成目标明确**的真实任务开始。官方示例：

> 从我们的 CRM 中获取本周的销售管道评审列表。跳过已处于活跃跟进序列中的人员。在网页和 Slack 上调研排名前五的账户，找出合适的联系人，以我的口吻起草外联内容，并在明天早上前留下草稿供我审批。

这条消息说清了：**做什么、在哪做、要取哪些上下文、完成后长什么样、哪里要我批**。

## 交接模板

```text
目标：……（完成后的样子）
来源：……（系统 / 文件 / 网址）
约束：……（不能动什么）
交付：……（文件格式、路径）
停下点：……（发送、付款、删除前先问我）
截止：……
```

## 之后

1. 审查结果并修正。
2. 让 Bot 记住长期规则（"从现在起，未经批准绝不发送外部消息"）。
3. 把稳定流程变成技能或例程。
{src(c('docs/grok-bot','官方：良好的首次交接'), c('docs/grok-bot/use-cases','官方：使用场景'))}
""")
w("start/faq.md",f"""
# 常见问题

**合上电脑还能继续吗？** 能。工作在云端电脑上跑，关应用、合盖、锁手机都不影响后台轮次和例程。

**多个 Bot 能同时工作吗？** 能。每个 Bot 在共享电脑上有自己的屏幕，但一个 Bot 同一时间只跑一个电脑操作任务。

**Bot 会记住什么？** 稳定偏好、角色上下文、先前工作摘要。重要决策请让它核查当前来源，别依赖记忆。

**任何网站都能用吗？** 很多可以，但网站可能拦截自动化、让会话失效或要求人工操作——Bot 会交给你，不会尝试绕过。

**要立刻停下怎么办？** 发"立即停止"。停止不会撤销已完成的操作。

**费用？** 见[方案与订阅](/start/plans)。用量每周重置。

**需要帮助？** {c('help/grok-bot/get-help','官方：获取帮助')}、{c('help/grok-bot/faqs','官方 FAQ')}。
{src(c('docs/grok-bot','官方总览 FAQ'), c('help/grok-bot/faqs','官方 FAQ'), c('help/grok-bot/how-to','官方：操作指南'))}
""")

# ---------- 核心概念 ----------
w("core/bots.md",f"""
# Bot：创建、编辑与管理

Bot 是拥有**名称、职责、专属对话和持续积累上下文**的 AI 队友。当一类工作有明显不同的**目标、工具集、工作方式、审批边界或定期安排**时，就值得单独建一个 Bot。

## 创建

1. 侧边栏 **+**（或 Cmd+N）→ **Create new Bot**。
2. 第一条消息说明**职责、信息来源、审批边界**，让它记住；再发一个有完成标准的真实任务。
3. 点聊天顶部的 Bot 名称可改名、加标签、换头像。

## 长期规则 vs 任务

- **长期规则**："从现在起，未经批准，绝不发送外部消息。" → 让它记住。
- **任务**："为这十二个账户起草后续跟进。" → 普通消息即可。

团队 Bot 另有一段 **关于** 描述，由所有者编辑。

## 整理、分享、删除

- **固定**常用 Bot；右键 **移至新分区** 按项目/客户分组。
- **分享**会生成公开链接，暴露身份、描述、技能和例程——先删掉 API 密钥、内部 URL、客户信息。
- **删除**会移除配置、对话和例程，但共享电脑上的**文件和登录不会随之删除**，要另行清理。

## 编制建议（社区经验）

- 一个 Bot 只管一个确定结果；主 Bot（幕僚长）只负责派活与验收。
- 先 1 个，跑顺再加；社区里 29 个 Bot 的编制是一步步迭代来的。
{src(c('docs/grok-bot/work','官方：使用 Grok Bot · Bot'), c('help/grok-bot/edit-bot','官方：编辑 Bot'), f(2), f(65))}
""")
w("core/messaging.md",f"""
# 消息、附件与接管

## 发消息

- 可粘贴文本、链接、图片，附加文件；`/` 引用已保存的技能，`@` 提及其他 Bot。
- 你的私信**优先于后台工作**，可以改变当前轮次方向；发"立即停止"即停（不会撤销已做的操作）。
- 说清**预期结果和决策边界**：能改什么、在哪一步必须停下。

## 附件

支持图片、音频、视频、PDF、Office、CSV、JSON、YAML、源码、HTML、邮件文件、笔记本等。

| 限制 | 值 |
|-|-|
| 每条消息附件数（桌面） | 6 |
| 文档、图片、音频 | 每个 25 MB |
| 视频 | 200 MB |

**告诉 Bot 每个附件是什么、拿来干嘛**：

```text
PDF 是已签署的政策文件，表格是本月交易记录。根据政策核对表格，
为每个异常引用对应条款，返回新表格和简短摘要。不要修改原文件。
```

## 敏感操作：接管电脑

需要登录、两步验证、付款时，Bot 会交出控制权：打开电脑画面 → Take over → 自己操作 → 交还。**永远不要把密码打在对话框里。**

## 语音与移动端

可与单个 Bot 语音聊天（群聊不支持）；iPhone 与桌面端共用同一批 Bot、对话、例程和电脑。
{src(c('docs/grok-bot/work','官方：消息与协作'), c('help/grok-bot/voice-chat','官方：语音聊天'), c('help/grok-bot/mobile','官方：移动端'))}
""")
w("core/computer.md",f"""
# 共享云电脑

你名下所有 Bot **共用一台云端电脑**：同一文件系统、同一浏览器登录态、同一批已装应用。电脑属于你的账户而不是某个 Bot，所以放在上面的东西对你所有 Bot 都可见；不同用户严格隔离。与队友的团队 Bot 聊天时，它通常也在**你的**电脑上运行。

## 关键事实

- 每个 Bot 有自己的屏幕，可并行；单个 Bot 同时只跑一个电脑操作任务。
- 客户端右侧可随时看实时画面，敏感步骤点 Take over 接管。
- 部分站点屏蔽机房 IP：可在设置的 Computer 页开启"流量经过本地设备"。
- 云电脑可能因底层更新/维护被**重建**：自装的应用和包会被移除（持久盘上的文件与登录通常保留）。

## 推荐做法

1. 把云电脑当**可丢弃容器**：配置、服务清单、脚本同步到私有 Git 仓库。
2. 维护一份 `services-ledger.md`（服务用途、依赖、启动命令、数据目录）和一键 `restore.sh`。
3. 跨 Bot 交接用 `/workspace` 下的固定文件。
4. 凭证不落明文；登录一律人工接管完成。

## 电脑坏了怎么办

见 {c('help/grok-bot/computer-recovery','官方：电脑恢复')}；企业管理员可在仪表盘 **Manage Bot Computers** 重建或终止成员电脑（详见[团队与企业](/admin/)）。
{src(c('docs/grok-bot','官方：你的 Bot 共用一台计算机'), c('docs/grok-bot/computers','官方：管理 Bot 电脑'), c('help/grok-bot/computer-recovery','官方：电脑恢复'), f(69), f(14))}
""")
w("core/memory.md",f"""
# 记忆与上下文

## 官方说法

Bot 会保留**稳定偏好、重要事实和工作摘要**，无需重放全部历史也能保持角色。但**记忆不能替代权威来源**——变化中的事实留在源系统，需要时让 Bot 重新取。每个 Bot 的对话和习得上下文彼此独立；共享文件、浏览器会话和直接交接可以在 Bot 之间传递上下文。

## 分层（社区总结）

- **共享层**：共用记忆、公共技能、插件/连接器、云电脑文件。
- **专属层**：单个 Bot 的描述（长期合同）、专属记忆、专属例程。

## 三条原则

1. 记忆只记**判断和指针**，经常变动的数据回源系统取。
2. 只有**核实过的结论**才写入团队共用记忆。
3. 记忆 ≠ 技能：偏好进记忆，**操作流程进技能**并指定维护人。

## 备份：记忆管家

建一个运维 Bot，每周例程导出所有 Bot 的描述与共用记忆为 Markdown，提交到私有仓库的 `bots-backup/charters/`、`bots-backup/memories/`。
{src(c('docs/grok-bot/work','官方：Bot 会记住什么'), f(69), f(57)+"（英文，摘要见案例）", f(10))}
""")
w("core/skills-routines.md",f"""
# 技能与例程

- **技能（Skill）**：教 Bot *怎么做*一件事的可复用流程。演示一次多步骤流程，Bot 就能存成技能；对话里用 `/` 引用。
- **例程（Routine）**：告诉 Bot *何时*做——按计划，或由 Slack 消息、邮件、webhook、GitHub 等事件触发。

> Skill 负责教授做事步骤，Bot 是承担职责的队友。先写清流程的 Skill，再决定要不要专职 Bot。

## 设置例程

直接在聊天里说："每个工作日上午 9:00，在此聊天中汇总新的支持工单。" Bot 会创建并显示在例程列表。

- 查看：点 Bot 名称 → **Details** → **例程**；每行可开关暂停。
- 打开某例程可见 **Instruction / When to run / Webhook**，按钮 **Pause、Test、Edit、Delete**（删除不可撤销）。
- 时区取 **设置 → Bot → Timezone**（Auto-detect 跟随本机）。
- **新建例程不会立即运行**，等下一个计划点；要马上试用 **Test**（会执行真实操作）。

## Webhook

让 Bot 给例程加 webhook 触发器，打开例程可复制 **POST to**（URL）、**key**（以 `Authorization: Bearer <key>` 携带）、**header**。可发 JSON 体，Bot 会连同指令一起收到。返回 **200 只代表已启动一次运行**，结果看 Bot 聊天。

## Slack 触发器

属于例程而非 Slack 插件：可在被提及、某短语出现、你加表情、收到任意消息时启动。**频道与短语尽量收窄**。

## 省用量

每次运行都扣用量。用量掉得快 → 先暂停不需要的例程，再放宽频率、收窄触发器。避免"每 5 分钟无过滤轮询"。

## 例程没跑？

检查是否 Paused、When to run 与时区是否正确、是不是还没到首次时间点。
{src(c('docs/grok-bot/work','官方：技能与例程'), c('help/grok-bot/routines','官方：例程'), f(66), f(12), f(6))}
""")
w("core/plugins.md",f"""
# 插件、邮箱与 Secrets

## 接入顺序：先跑通界面，再挂连接器

人能手动点完的事，先让 Bot 用云电脑和浏览器去点；跑稳、验证过价值，再换成插件/连接器或脚本，避免一次装一堆插件徒增维护。

## 插件（连接器）

在设置里连接支持的服务（如 Slack、GitHub、Google 等），Bot 以你的身份读写。插件 ≠ 触发器：要"某事发生就开工"请用[例程](/core/skills-routines)。

## Bot 专属邮箱

对 Bot 说 `claim your email`，可获得 `名字@mail.grokbot.com` 地址，用于收信、注册网站、联络客户；从该地址**发信前需要你在界面批准**。团队账号需管理员允许。

## Secrets

API Key 等放进设置的 **Secrets**，不要贴在对话里。

## 技能/CLI 扩展

- 开源 Skill：把仓库地址发给 Bot 说"帮我安装"，所需 Key 放 Secrets。
- 云电脑上的 CLI 工具要在 Bot 电脑终端里**单独登录**，不要拷贝本机登录态（会互相顶 token）。
{src(c('help/grok-bot/connect-plugins','官方：连接插件'), c('help/grok-bot/agent-email','官方：Bot 邮箱'), c('help/grok-bot/secrets','官方：Secrets'), f(68))}
""")
w("core/group-chats.md",f"""
# 群聊、多 Bot 协作与团队 Bot

## 群聊

- 把多个 Bot 拉进同一对话；也可加队友发布的团队 Bot。
- 你在群里发消息，Bot 直接在群里回；`@名字` 只发给某个 Bot。
- Bot 也会私信你或私信其他 Bot 交接工作，这些消息出现在各自聊天里，不进群。
- 想让 Bot 只在群里回："记住：在群组聊天中，要在群里回复。"
- **没有禁止 Bot 互发消息的开关**：告诉它"不要给其他 Bot 发消息，先问我"，并让它记住。
- **每条回复都扣用量**，包括群回复和 Bot 间消息——群里 Bot 越少越省。
- 群聊不支持语音。

## 团队 Bot

团队内所有成员都能与之聊天的 Bot，有独立 Slack 应用和账号名。在 Slack 频道里要让 Bot 之间交接，需要用团队 Bot：

| Bot | 提问位置 | 能否给其他 Bot 发消息 | 代表谁 |
|-|-|-|-|
| 个人 Bot | 应用内或 Slack 私信 | 能 | 你 |
| 个人 Bot | Slack 频道消息串 | 不能 | 无人（共享串） |
| 团队 Bot | Slack 频道或私信 | 能（发给该成员自己的 Bot） | 提及它的成员 |

## 协作建议

- 主 Bot 派活 + 专职 Bot 执行 + 文件落盘交接。
- 交接物写到 `/workspace/<项目>/` 固定路径。
{src(c('help/grok-bot/group-chats','官方：群组聊天'), c('help/grok-bot/team-bots','官方：团队 Bot'), c('docs/grok-bot/work','官方：消息与协作'), f(65), f(53))}
""")

# ---------- 进阶（提纲） ----------
stub("advanced/usage.md","额度与成本优化",["额度扣除规则：按智能体步骤与 token 计，非消息条数","值得/不值得做的操作判断","四步省额度工作流","额度耗尽应急与每周审计","例程频率与群聊回复是两大消耗源"],
 [c('help/grok-bot/plans','官方：方案和计费'),c('help/grok-bot/models','官方：模型'),f(64),f(9),f(12),f(13),f(54)])
stub("advanced/team-orchestration.md","团队编排：章程、岗位与放权",["主 Bot（幕僚长）只派活与验收","六行合同式描述","从 1 个专职 Bot 逐步扩编","放权分级"],[f(65),f(45),f(35),f(36)])
stub("advanced/automation.md","触发器与自动化：定时、Webhook、在 X 上派活",["定时例程设计","Webhook + iOS 快捷指令入库","在 X 上派活","避免无增量轮询"],[c('help/grok-bot/routines','官方：例程'),f(66),f(6),f(12)])
stub("advanced/security.md","权限、安全与人闸",["批准与 Auto Review","按可逆性分级：只读/草稿放行，外发/付费/删除必批","网络策略与日志","凭证处理"],[c('docs/grok-bot/security','官方：安全'),c('docs/grok-bot/security-faq','官方：安全 FAQ'),f(67)])
stub("advanced/backup.md","备份与灾备",["云电脑重置会清掉自装工具","服务总账 + restore.sh","记忆管家每周导出到私有仓库","恢复提示词"],[f(10),f(14),f(69)])
stub("advanced/im.md","外部入口：飞书 / 微信接入",["团队接入飞书（飞书管家模板）","微信聊天记录打通（快捷指令）","微信一句话运营 X"],[f(15),f(11),f(29),f(34)])

# ---------- 案例（摘要索引） ----------
groups=[("自媒体与内容运营",[26,28,32,34,41]),("工程与研发",[25,31,50,51,58,62]),("电商",[27,38]),("一人公司 / AI 团队",[44,47,48,52,55,59,60,61]),("GTM / 销售",[40]),("综合入门与技巧",[24,30,33,37,42,43,46,49,56])]
def summary(i):
    p=[x for x in os.listdir(R+"/sources/feishu") if x.startswith(f"{i:02d}_")][0]
    s=open(R+"/sources/feishu/"+p).read().split("-->",1)[1]
    import re
    m=re.search(r"\*\*整理者导读\*\*\s*\n>\s*(.+)",s)
    if m: return m.group(1).strip()[:160]
    for line in s.splitlines():
        l=line.strip()
        if len(l)>40 and not l.startswith(("#",">","!","|","-","[")): return l[:160]
    return ""
lines=["# 实战案例","","::: tip 说明\n社区长文版权归原作者，本站仅提供摘要与原文链接（飞书收录页，内含原始出处）。\n:::",""]
for g,ids in groups:
    lines.append(f"## {g}\n")
    for i in ids: lines.append(f"- **{f(i)}**  \n  {summary(i)}…\n")
lines.append("## 铁柱长文与推文合集\n")
for i in list(range(6,17))+[18,19,20,21]:
    tag=" **⚠️ 已过时**" if i in OLD else ""
    lines.append(f"- {f(i)}{tag}")
w("cases/index.md","\n".join(lines))
w("cases/outdated.md",f"# 已过时文章\n{OUT}\n- {f(7)}\n- {f(8)}\n\n最新规则见 {f(16)} 与[方案与订阅](/start/plans)。")

# ---------- 团队与企业 / 资源 ----------
stub("admin/index.md","团队与企业",["团队版与管理控制、模板共享","身份与 SSO","私有网络与环境设置脚本","代理","桌面端分发与版本","Manage Bot Computers：重建/终止（企业版）"],
 [c('docs/grok-bot/teams','官方：团队版'),c('docs/grok-bot/identity','官方：身份'),c('docs/grok-bot/private-networks','官方：私有网络'),c('docs/grok-bot/proxies','官方：代理'),c('docs/grok-bot/deployment','官方：部署'),c('docs/grok-bot/computers','官方：管理 Bot 电脑'),c('help/grok-bot/delete-account','官方：删除账户')])
stub("resources/index.md","资源",["提示词库（从各文抽取可直接发给 Bot 的提示词）","术语表：Bot / 团队 Bot / 技能 / 例程 / 插件 / 人闸 / Auto Review","规则与版本变更时间线（8-11 上线 → 10-12 统一订阅）","原文索引"],
 [f(0),f(18),f(19),f(20),f(21),c('docs/grok-bot/settings','官方：设置')])
