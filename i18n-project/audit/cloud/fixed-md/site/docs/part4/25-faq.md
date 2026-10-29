# 第 25 章 常见问题与排错

遇到报错或卡顿，**千万别盲目重装或重置**，这会冲掉刚写好的环境和临时脚本。

1. **先看服务状态**。
2. 再排查是本地网络、插件授权、云端环境还是每周额度的问题。


![常见问题与排错](/info/25-faq.png)

## Grok Bot 登录与绑定账号出问题怎么办？ {#登录与身份验证}

**个人用户通过设置页面或专用链接关联授权，企业席位直接用 Grok 登录，若绑错需找人工客服，遇循环跳回可清 Cookie 用无痕模式认证。**

### 账号与订阅限制
Grok Bot 依托 Cursor 运行，与 Grok 手机端付费墙及每周额度限制（Weekly SuperGrok Limit）无关。

个人版支持 SuperGrok 与 Plus、Heavy 版本，以及 X Premium+；SuperGrok Lite 与 Grok Enterprise 无法关联个人账户，企业席位由管理员统一分配。

**账户邮箱注册后无法修改，关联 Cursor 是一次性永久绑定**。绑错账号无法自行转移，必须联系人工客服处理。

### 绑定与登录步骤
1. 个人绑定：打开 [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) 或在客户端进入 **设置** > **用量和计费**，在 **管理方案** 下点击 **通过 Grok 获取访问权限**（仅在能提升当前用量层级时显示）。
2. 企业席位：拥有 Grok Business 席位无需在方案页手动绑定，完全退出后在登录页点击 **Sign in with Grok** 即可。
3. 服务确认：遇到异常先访问 [status.cursor.com](https://status.cursor.com) 查看 **Grok Bot** 实时状态，操作要求详见[登录 Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in)。

   **服务故障时等待官方修复，切勿重装应用或重置电脑**。

### 故障排查与验收
客户端版本过旧会引发协议不匹配；突发认证故障建议静置 30 到 60 分钟再试。**验收标准是账号邮箱、订阅归属与客户端登录状态一一对应**。

| 故障现象 | 正确处置路径 | 严禁操作 |
| :--- | :--- | :--- |
| 循环跳回登录页 | 清理 `cursor.com` 与 `x.ai` 的 Cookie，用桌面端无痕模式认证 | 连续卸载重装客户端 |
| 找不到关联入口 | 确认当前账号层级低于待绑定方案，未达上限 | 注册新账号重复购买 |
| 提示 Model provider is overloaded | 复制报错的 Request ID，等待 2 分钟重新发送 | 立即点击 Reset 重置电脑 |
| 提示邮箱需变更 | 重新注册账号并迁移资产 | 尝试在设置中强改绑定邮箱 |

向 Bot 发送提示词确认登录状态。
```text
请检查当前运行环境的网络连通性与 Cursor 身份验证状态，汇报当前登录的用户环境标识，但不要输出任何敏感 Token。
```

## Grok Bot 连不上云端电脑该如何恢复？ {#云端电脑与环境恢复}

**遇到断连可先等两分钟重试或彻底重启应用，卡死时点 Recover 存现场重建，而会覆盖快照丢失未同步修改的 Reset 只能作最后兜底手段。**

![云端电脑与环境恢复](/info/25-faq-s2.png)

所有 Bot 共享同一台云端电脑。**对话记录独立存在数据库**，崩溃清空都不丢。

提示 Reconnecting、Couldn't Reach Grok Bot's Computer 或 Bot failed to respond 时：
1. 等 1 到 2 分钟点 Retry。
2. 彻底退出应用。Mac 按 `Cmd+Q`，Win/Linux 退出托盘，别只关窗口。
3. 进设置 > 计算机点更新。备份未完或 Bot 工作时切勿中断。
4. 卡住点 Recover。
5. **Reset 是最后手段**。快照覆盖会丢未同步修改。详见[Grok Bot 电脑](https://cursor.com/cn/help/grok-bot/computer-recovery)。

|操作|现场保存|环境影响|场景|
|---|---|---|---|
|Retry|原样保留|无影响|网络抖动|
|Update|等备份完|全留软件；整机清自装包|官方补丁|
|Recover|存现场建机|移除自装应用与环境|卡死损坏|
|Reset|快照覆盖|丢未同步修改|连不上兜底|

**电脑状态变绿显示已连接**、终端正常且配置完整就算修好。

- 遇到 SSO 登录，点卡片上的 Take over 手动验证，搞定点 I'm done。
- 密钥与网络：在设置 > General > Security Key 开 Use hardware security keys 插 YubiKey；遇验证码在设置 > 计算机勾“通过此计算机路由流量”。
- 本地执行：在设置 > 计算机开“在此计算机上执行”（跑命令先确认）。详见[Grok Bot 设置](https://cursor.com/cn/docs/grok-bot/settings)。
- 磁盘告警：报 Computer is low on disk space 时点 Go to Disk Saver，**必须人工确认才删**。

```text
请检查当前云端计算机根目录与工作目录的磁盘占用情况，找出体积超过 200MB 的文件与缓存目录，列出清单供我确认，不要擅自执行任何删除命令。
```

## Grok Bot 自动化例程不触发该怎么排错？ {#例程管理与自动化排错}

**例程无动静先确认状态非暂停并校对时区与 Test 测试，Webhook 需带鉴权密钥且 200 仅代表入队，Slack 触发必须限定频道白名单与过滤词。**

![例程管理与自动化排错](/info/25-faq-s3.png)

例程在云端自动跑，关机也生效，支持定时、Webhook 与 Slack 推送。

1. **查状态与时区**：Details 确认非 **Paused**（手机看 **Active**）；在“设置 > Bot > Timezone”手动选时区，跨国别用 Auto-detect。
2. **定时触发时机**：只等下个周期（09:05 设 09:00 明早跑），即时测逻辑点 **Test**。
3. **校验 Webhook**：POST 带 `Authorization: Bearer <key>`。**200 仅代表入队**，结果去聊天窗口看；非 200 为密钥错或暂停。
4. **收窄 Slack 触发**：**必须限频道与过滤词**，防闲聊几小时烧光配额。详见[例程](https://cursor.com/cn/help/grok-bot/routines)。

手机端“运行历史”查 **Running**、**Succeeded**、**Failed**；显示 **No runs yet** 为未触发。

| 故障 | 原因 | 修复 |
|---|---|---|
| 无动静 | Paused/未到点/时区偏差 | 查 Active，点 Test，校对 Timezone |
| 401/403 | 漏 Token/密钥重置/例程已删 | 重新复制 header 覆盖配置 |
| Slack 无回应 | 旧消息/频道或词未命中 | 只认新消息，核对频道白名单与短语 |
| 配额消耗快 | 间隔过短/大群无过滤词 | 暂停例程，拉长间隔，限定运维频道 |

创建与修正自动化例程提示词：
```text
请修改名为“工单同步”的例程：仅在 #ops-alert 频道出现包含“[P0-Error]”文字的新消息时才触发，忽略其他日常聊天，并列出更新后的 When to run 描述。
```

## 用量异常与配额控制

![用量异常与配额控制](/info/25-faq-s4.png)

Grok Bot 配额按周重置。基础额度用完会中断回复，**这属于正常的配额熔断**。一次性试用额度跑复杂任务耗尽后无法恢复。

### 操作与防坑
1. 恢复额度：等每周刷新，或在 **设置** > **用量和计费** 开按需用量，也可升订阅。
2. 设定封顶：客户端或网页 [cursor.com/dashboard](https://cursor.com/dashboard) 设限。**在跑任务不强切，扣费微超几个百分点属正常。**
3. 额度对齐：外部账号不叠加取高者（Pro 对应 SuperGrok/X Premium+，Pro+ 对应 SuperGrok Plus，Ultra 对应 SuperGrok Heavy）。
4. 移动端退订：多端共享订阅。商店付款需在 Apple ID 或 Google Play 退，官方不直退，见[方案和计费](https://cursor.com/cn/help/grok-bot/plans)。

### 验收标准
| 场景 | 操作 | 边界与坑点 |
| :--- | :--- | :--- |
| 防超额 | 客户端或控制台设月度限额 | **封顶拒新请求，在跑任务跑完才停** |
| 查用量 | Bot 内部设置查实时剩余 | 外部 Grok 看板不互通 |
| 试用清零 | 排查大工程扫描或重构 | 一次性耗尽不恢复 |

```text
请列出你当前账号下所有处于活跃状态的例程，评估它们各自的执行频率与触发条件，指出哪一个例程最容易引发高额用量消耗。
```

## 群聊、协作与辅助 Bot 治理

辅助 Bot 会进侧边栏并弹通知，改文件或连外网会触发 **Auto-review** 审批。

### 操作与审批
1. 降噪隐藏：桌面端右键选 Hide from sidebar 或发指令关通知；手机端进配置关通知。
2. 恢复误藏：桌面在 **隐藏的机器人** 选 Show in sidebar，手机选 Unhide。**严禁为找 Bot 去点云端 Recover 或 Reset。**
3. 审批与白名单：高频操作点 **始终允许**（存入 设置 > Bot > 自定义规则）；冲突先询问，显示“由管理员强制要求”的不可跳过。

   规范见 [Grok Bot 操作指南](https://cursor.com/cn/help/grok-bot/how-to)。

### 验收标准
侧边栏无杂乱 Bot，日常高频**免打扰自动通过**。

|场景|超时|表现|对策|
|---|---|---|---|
|前台人工|永久等待|持续挂起|核对后允许或拒绝|
|后台/Webhook|约 10 分钟|变 Expired 取消|配“始终允许”或开通知|
|管理员强制|视场景|无法跳过|必须人工授权|

```text
请梳理我们在此会话中频繁执行的文件读取与构建指令，为它们生成一组最小权限的安全规则建议，以便我添加到 Auto-review 的自定义白名单中。
```

## 插件与外部应用连接

### 授权排错
**Added 只表示已安装，不等于已登录**。卡片没弹去侧边栏手动验证。**授权须在 10 分钟内完成**，超时点 Reopen；持续报错点 Remove 删掉重装。

| 状态 | 处理 |
| :-- | :-- |
| **Added / Needs auth** | 点「验证身份」去浏览器登录 |
| **Connected 报错** | 发送带插件名的指令刷新会话 |
| **Disabled by team admin** | 找团队管理员解禁 |

### 多账号与验收
1. **多账号**：在「连接应用」> 插件 > Accounts 点 **Add Another Account**（手机端点 Authorize new account）并打标签。对话指明标签调用；无按钮则仅支持单账号。
2. **验收**：**状态显示绿色 Connected 且标签清晰**，发指令能一次准确调用。

详见[连接应用](https://cursor.com/cn/help/grok-bot/connect-apps.md)。

```text
请刷新当前已连接的插件列表，使用带有“工作”标签的账户连接，读取最近更新的 3 个页面，确认授权是否正常。
```

## 账号注销与数据清理

Grok Bot 共用 Cursor 账号，**删号不可逆**，无法单独保留 Cursor。换电脑用直接退出登录或卸载就行。

### 终端注销步骤
注销前务必取消自动续费，避免账单纠纷。
1. 手机端（iOS/Android）：点头像进“设置” > 账户信息 >“删除账户”，网页验证中键入“**删除**”两字确认。
2. 桌面与网页端：**客户端无法直接注销**。登录 [cursor.com/dashboard](https://cursor.com/dashboard) >“设置” >“更多” >“删除账户”确认。
3. 企业或团队席位：个人无法独立注销，必须联系管理员解绑或提工单。条款见[删除你的 Grok Bot 账户](https://cursor.com/cn/help/grok-bot/delete-account)。

### 资产清理与避坑
| 资产与订阅 | 处置结果 | 必做处理 |
| :--- | :--- | :--- |
| 云端对话与环境 | **30 天内**物理擦除，快照销毁 | 提前导出代码和对话，下载文件 |
| 本地文件 | 完好无损 | 无需处理 |
| 商店与 X 独立订阅 | **不会自动取消** | 需去 Apple、Google 或 x.ai 手动退订 |

## 获取官方支持与工单规范

### 怎么做
本地排查没用时，发邮件到 **hi@cursor.com**。**别只发“我的 Bot 坏了”这类模糊描述**，邮件里带齐这六项。

1. 账号凭证：注册邮箱。
2. 运行环境：平台与客户端版本号。从账户菜单 > 支持 > 关于，点 Copy version info 复制。
3. 准备执行的操作：说明故障前想跑什么任务。
4. 真实报错凭据：完整错误弹窗、控制台报错或计费截图。
5. 排查记录：写明做过哪些排查，避免客服给重复建议。
6. Request ID：右键报错消息或悬停点 More message actions 选 Copy request ID。若没有该项，必须附原始报错文本与全屏截图。

Linux 若弹 Update required 且自动更新失败，按发行版在终端执行更新指令：
- Debian / Ubuntu：`sudo apt update && sudo apt install --only-upgrade grok-bot`
- Fedora / RPM 系列：`sudo dnf upgrade --refresh grok-bot`

::: details 怎么做
```text
收件人：hi@cursor.com
主题：【Grok Bot 故障申报】云端电脑持续重连且 Recover 失败 - [你的账号邮箱]

支持团队：
我的账号遇到了云端电脑无法连通的故障，无法正常执行任务，以下是详细环境与排查信息：

1. 账号邮箱：developer@example.com
2. 版本信息：Version 1.2.4 (Channel: stable, OS: Darwin x64 23.4.0)
3. 故障发生场景：我尝试让 Bot 运行自动化部署脚本，终端在拉取镜像时中断。
4. 核心报错信息：界面持续提示“Couldn't Reach Grok Bot's Computer”，伴随“Bot failed to respond”。
5. 已尝试的排错操作：
   - 已彻底 Quit 应用并重启；
   - 尝试在“设置 > 计算机”执行 Update，提示备份未就绪；
   - 尝试点击 Recover，重试一次后依然在进度条处卡住报错；
   - 查看 status.cursor.com 确认官方各项服务状态正常。
6. 请求 ID (Request ID)：req_98af7c32e01b44d7a1
7. 附件：包含当前报错卡片截图及“设置 > 计算机”面板状态截图。

请协助在后台检查该实例的宿主节点状态，谢谢。
```
:::

### 做到什么程度算好
**发信后能收到自动回执，且技术无需二次追问即可调出日志**。详细规范见[获取帮助](https://cursor.com/cn/help/grok-bot/get-help.md)。

## 典型故障排错案例

### 案例一：云端电脑 Reconnecting 循环
报 Couldn't Reach Grok Bot's Computer 时，**千万别先点破坏性的 Reset**。
1. 访问 [status.cursor.com](https://status.cursor.com) 确认服务正常，按 `Cmd+Q` 重启应用。
2. 进设置 > 计算机，若提示未及时暂停，等约 5 分钟让后台超时。
3. 待 Recover 电脑亮起后点击恢复并重跑安装脚本，**保全历史脚本与登录态**。

### 案例二：Slack 触发器用量雪崩
因监听 3000 多人的 `#general` 全量闲聊，每周用量在 24 小时内归零。
1. **先在支出面板设死按需月度限额**，防止信用卡扣费。
2. 将例程切为 Paused 止血。
3. 规则收窄为“仅在 `#bot-help` 且被 `@Grok` 时触发”。
4. 点 Test 单次验证后再恢复上线。

### 案例三：Notion 认证失效与接管登录
Notion 报 Action needed 且 Okta SSO 拦截时，**必须用 Take over 在内置浏览器闭环认证**。
1. 见 Needs auth 提示后，点击卡片中的 Take over 接管。
2. 在云端内置浏览器输工号过二次验证，点 I'm done。
3. 在 Accounts 点 Add Another Account 授权个人空间，**打上“个人库”标签防凭证冲突**。

## 容易踩的坑

1. 丢聊天别点 Reset，会抹掉代码。找回先**退出重启**，核对 Cursor 账号或看隐藏机器人。
2. 14:05 设 14:00 例程次日才跑，测逻辑点 **Test**。
3. Slack 大群无触发词监听，打招呼会**烧光整周额度**。
4. 删 App 仍会扣费，退订去 **Apple ID 或 Google Play** 订阅中心取消。
5. Updating 时点 Reset 会**损坏文件系统**，只能找人工。
6. 插件 Added 需确认 **Connected**；显示 Needs auth 需浏览器授权。
7. 更新、Recover 或 Reset 清空 `node_modules` 与 `.venv`，依赖写进**初始化脚本**。
8. 审批卡片 **10 分钟后 Expired 终止**，记得开通知或设“始终允许”。

## 做完怎么验收

- 查 [status.cursor.com](https://status.cursor.com) 无故障且邮箱正确。
- 进设置 > 计算机看绿灯，给 Bot 发基础 Linux 命令测回包。
- 例程保持激活，核对 When to run 时区，点 Test 跑通。
- 进设置 > 用量与计费，**必须设定按需用量月度限额**防天价账单。
- 连接应用显 Connected，写操作能弹 Auto-review 且手机有推送。
- 工单只留 Request ID 和 Copy version info，**切勿泄露 Bearer Token 请求头**。

## 延伸阅读

- 相关章节：[第 5 章 共享云电脑：文件、浏览器与接管](/part1/05-computer)
- 相关章节：[第 10 章 额度与成本：让一周用量撑满一周](/part1/10-usage)
- [Grok Bot 常见问题官方解答](https://cursor.com/cn/help/grok-bot/faqs)
- [Grok Bot 操作与排错指南](https://cursor.com/cn/help/grok-bot/how-to)
- [Grok Bot 电脑环境管理与灾难恢复](https://cursor.com/cn/help/grok-bot/computer-recovery)
- [自动化例程与触发器详细配置](https://cursor.com/cn/help/grok-bot/routines)
- [账号体系与注销说明](https://cursor.com/cn/help/grok-bot/delete-account)
- [支持团队联系与工单规范](https://cursor.com/cn/help/grok-bot/get-help)
- [Grok Bot 系统全局设置参考](https://cursor.com/cn/docs/grok-bot/settings)
