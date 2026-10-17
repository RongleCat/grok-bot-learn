import json
t = json.load(open("/workspace/grok-bot-learn/sources/feishu/tree.json"))
U = {f"fs{i:02d}": (x[2], "https://jcng5q8n0f3z.feishu.cn/wiki/" + x[1]) for i, x in enumerate(t)}
D = lambda *n: [f"docs_grok-bot{'_' + x if x else ''}.md" for x in n]
H = lambda *n: [f"help_grok-bot_{x}.md" for x in n]
F = lambda *n: [f"fs{x:02d}.md" for x in n]
J = [
 ("part1/01-what-is", "第 1 章 Grok Bot 是什么：一个自带电脑的 AI 同事", "产品机制、和普通聊天助手的区别、共享云电脑的边界、适合与不适合的任务、和 Muse/Hermes/dots/Cue 的选型对比表", D("", "use-cases") + F(2, 3, 21, 24)),
 ("part1/02-plans", "第 2 章 方案与订阅：先选对档位", "以 2026-10-12 起的 The X Subscription 为准讲四档与免费档、每周共享用量池、哪些档含 Grok Bot、Cursor 方案与 SuperGrok 关联、团队版与按需、老订阅切换注意、如何查看用量；不要写任何开发者积分或旧资费", H("plans", "supergrok", "mobile-purchase", "models") + F(16, 18)),
 ("part1/03-install", "第 3 章 安装登录与第一个 Bot", "下载安装、登录、iOS、创建第一个 Bot、写职责（六行合同）、第一条任务、验收清单、常见登录问题", D("get-started") + H("onboarding", "sign-in", "mobile", "edit-bot") + F(2, 24, 30)),
 ("part1/04-handoff", "第 4 章 交代任务：消息、附件与一次好的交接", "好请求的五要素、附件限制表、提示词示例多条、长期规则 vs 任务、停止与插话、语音、常见失败写法对照", D("", "work") + H("how-to", "voice-chat") + F(33, 37, 49)),
 ("part1/05-computer", "第 5 章 共享云电脑：文件、浏览器与接管", "共享电脑机制、各 Bot 屏幕、接管登录、文件交接约定、本地网络出口、重建与恢复、实操步骤与坑", D("computers", "settings") + H("computer-recovery") + F(69, 14)),
 ("part1/06-memory", "第 6 章 记忆：让 Bot 越用越懂你", "官方记忆说明、记忆分层、什么该记什么不该记、记忆与技能的边界、团队记忆、记忆备份流程、提示词", D("work") + F(57, 69, 46)),
 ("part1/07-apps", "第 7 章 连接应用：插件、邮箱与 Secrets", "先界面后连接器的接入顺序、插件连接步骤、Bot 专属邮箱、Secrets、X 检索、安装开源 Skill 与 CLI、坑点", H("connect-plugins", "agent-email", "secrets") + F(68, 42)),
 ("part1/08-skills-routines", "第 8 章 技能与例程：把一次成功变成每天自动跑", "技能的生成与引用、例程设置/查看/测试、时区、webhook 字段与 200 含义、Slack 触发器、例程排错、示例例程若干", H("routines", "how-to") + D("work") + F(66, 12, 6)),
 ("part1/09-group-team", "第 9 章 群聊与团队 Bot：从一个 Bot 到一组 Bot", "群聊规则、Bot 互发消息、团队 Bot 与 Slack 对照表、主 Bot 派活模式、交接文件约定、用量影响", H("group-chats", "team-bots") + F(53, 35, 65)),
 ("part1/10-usage", "第 10 章 额度与成本：让一周用量撑满一周", "扣费原理、高耗操作清单、省额度四步、例程与轮询优化、群聊回复控制、用量审计、直接发给 Bot 的省额度指令", H("plans", "routines") + F(64, 9, 12, 13, 54)),
 ("part1/11-safety", "第 11 章 权限、安全与人闸", "批准与 Auto Review、按可逆性分级放权、网络策略、日志、凭证处理、对外发信审批、安全 FAQ 要点、配置清单", D("security", "security-faq") + F(67, 45)),
 ("part2/12-content", "第 12 章 案例：自媒体与内容团队", "以多篇案例为素材讲内容团队的岗位设计、选题-起草-配图-分发流程、提示词、坑点，每个案例写清做法与可借鉴点", F(26, 28, 32, 36, 20)),
 ("part2/13-x-ops", "第 13 章 案例：在 X 上做内容与运营", "X 检索、自动化 X 内容、微信一句话运营 X、5 个 Bot 模板、只出草稿的审批设计", F(34, 41, 66, 19)),
 ("part2/14-engineering", "第 14 章 案例：工程与研发团队", "PR 巡检、仓库值班台、工程 harness、与本地 CLI agent 分工、九类工作清单、提示词与坑", F(25, 31, 50, 51, 58, 62, 59)),
 ("part2/15-ecommerce", "第 15 章 案例：电商与生活实操", "闲鱼上架、小红书做图、找工具、做短视频、整理收藏、亚马逊团队搭建", F(27, 38)),
 ("part2/16-knowledge", "第 16 章 案例：知识自动入库与微信打通", "Webhook+快捷指令入库流水线、微信聊天记录打通、接入微信、步骤与提示词", F(6, 11, 29)),
 ("part2/17-gtm", "第 17 章 案例：GTM、销售与幕僚长", "GTM 用法、Chief of Staff 章程与例程、销售外联只出草稿", F(40, 45, 56) + D("use-cases")),
 ("part2/18-solo", "第 18 章 案例：一人公司与 AI 团队", "一人公司、AI agency、从零到运转的公司、29 个 Agent、第一个 AI 员工，如何逐步扩编", F(44, 47, 48, 52, 55, 60, 61, 43)),
 ("part3/19-orchestration", "第 19 章 团队编排：章程、岗位与放权", "主 Bot 与专职 Bot、章程模板、岗位拆分方法、放权分级、交接规范、扩编节奏", F(65, 45, 35, 36, 44)),
 ("part3/20-automation", "第 20 章 可靠的自动化：定时、Webhook 与事件触发", "触发器选型、例程设计模板、Webhook 接入、增量判断避免空跑、失败兜底、监控", F(66, 6, 12) + H("routines")),
 ("part3/21-backup", "第 21 章 备份与恢复：电脑重置也不慌", "服务总账、restore.sh、私有仓库、记忆管家、恢复提示词、百万撤离方案", F(10, 14, 69) + H("computer-recovery")),
 ("part3/22-feishu-wechat", "第 22 章 接入飞书与微信", "团队接入飞书步骤与飞书管家模板、微信接入、权限与坑", F(15, 29, 11)),
 ("part4/23-enterprise", "第 23 章 团队版与企业落地", "团队版管理控制、身份与 SSO、私有网络与环境脚本、代理、桌面端分发、管理 Bot 电脑、推广建议", D("teams", "identity", "private-networks", "proxies", "deployment", "computers")),
 ("part4/24-roles", "第 24 章 按岗位组建你的 AI 团队", "按岗位（内容、工程、销售、研究、运营、个人助理、管理者）给出 Bot 编制、首个任务、例程、提示词", D("use-cases") + F(56, 49, 43, 52)),
 ("part4/25-faq", "第 25 章 常见问题与排错", "按主题分组的问答：登录、电脑、例程、用量、群聊、插件、删除账号、获取帮助", H("faqs", "how-to", "get-help", "delete-account", "computer-recovery", "routines")),
]
json.dump({"jobs": J, "urls": U}, open("jobs.json", "w"), ensure_ascii=False, indent=1)
print(len(J))
