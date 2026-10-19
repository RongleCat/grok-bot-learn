# 第 8 章 技能与例程：把一次成功变成每天自动跑

别直接设定时。**脱离人工盯梢易卡死，还会半夜三点误跑，空转耗尽整周额度。**

把操作沉淀为技能（Skill），组装成例程（Routine）：
1. 校准时区，规范 Webhook。
2. 限制 Slack 触发范围。
3. 加上虚拟机两段式检测。

**设好边界，合上电脑后台也能稳定交付。**


![技能与例程：把一次成功变成每天自动跑](/info/08-skills-routines.png)

## 技能的沉淀与引用：固定你的标准作业程序

![技能的沉淀与引用：固定你的标准作业程序](/info/08-skills-routines-s1.png)

技能是保存在账号里的操作指令，**名下所有 Bot 都能直接调用**。

### 怎么沉淀技能

**方式一：对话后文本总结**
任务跑通后先别关会话，直接让当前 Bot 提炼保存。提示词要明确输入源、异常处理与越界限制，直接发送这段模板。

::: details 怎么沉淀技能
```text
请把我们刚刚完成的这套流程保存为名为“每日工单异常审查”的技能。
技能内容必须包含以下要素：
1. 适用场景：工作日审查支持渠道中滞留超过 4 小时的工单。
2. 输入数据：从已连接的工单插件中读取状态为 Open 且优先级为 High 的列表。
3. 决策规则：若工单包含退款申请且金额大于 500 元，标记为一级风险；其余标记为二级跟进。
4. 交付格式：生成 Markdown 表格，列出工单编号、客户标识、滞留时长、风险等级与跟进建议。
5. 异常处理：若工单系统接口无响应或无符合条件的数据，输出明确说明，严禁使用历史缓存或伪造数据。
6. 安全边界：未经人工明确批准，严禁直接调用接口回复客户或变更工单状态。
```
:::

**方式二：演示教会（Teach task）**
界面操作复杂时，直接演示更省事。
1. 聊天窗口右侧打开计算机预览，选择“教会任务”（Teach task）。
2. 简述目标后在云电脑上操作。**系统最多录 10 分钟屏幕且不录麦克风音频，切勿输入密码等机密，敏感凭据走安全卡片**。
3. 自动生成草稿后，**必须补齐决策规则、报错与审批边界，切勿直接上线**。没看到入口说明还在灰度，改用方式一。

### 如何引用与管理技能

- **输入框引用**：输入框输入斜杠 `/` 即可选择技能载入。
- **开启权限**：列表中找不到时，去桌面侧边栏“连接应用”（Connected Apps）点已连数量，在“私有技能”里打开开关。

### 做到什么程度算合格

| 检查项 | 不合格写法 | 合格写法 |
| :--- | :--- | :--- |
| 输入来源 | “分析一下最近的数据” | 明确指定插件、API 端点、文件路径或数据库视图 |
| 边界控制 | “遇到问题看着办” | 数据缺失立即中断报错，严禁编造数据 |
| 动作权限 | “帮我把报表发给客户” | 生成草稿并在聊天停留，**等人工允许后再发送** |
| 输出结构 | 自由发挥的大段文本 | 固定字段列表、Markdown 表格或落盘路径 |

出处：[《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)

## 例程的核心机制：设置、查看与测试

![例程的核心机制：设置、查看与测试](/info/08-skills-routines-s2.png)

例程是挂在 Bot 名下的工作流触发器，跑在云端 Linux 的 `/workspace` 目录。**就算合上电脑或退出客户端，云端任务也会按计划推进。**

### 规格与限制

- 每个 Bot 最多创建 50 个例程，系统保留最近 20 次运行记录。
- 定时例程最短触发间隔为 5 分钟，不支持秒级调度。
- **删除例程不可逆**，后续执行会永久终止；删除 Bot 会连带清空全部例程。

出处：[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 创建与管理例程

桌面端在聊天框发指令直接创建：

```text
每个工作日上午 8:30，调用“每日工单异常审查”技能，在此对话中输出审查清单。如果未检索到高风险工单，只发一行“今日无高风险工单”即可，不要刷屏。
```

桌面端管理：
1. 点击聊天窗口顶部的 Bot 名称进入 Details，在例程（Routines）列表能看运行时间或 Paused，右侧开关随时暂停（Pause）或恢复（Resume）。
2. 点击具体例程可查三项属性：Instruction（执行提示词）、When to run（计划描述）与 Webhook（专属 URL、密钥与请求头）。
3. 底部工具栏提供 Test、Edit 与红色垃圾桶（Delete routine）。**点击 Edit 会在对话框预填 "Edit your routine: [例程名]"**，补上修改要求发送即可更新。

手机端管理：
1. 打开 Bot 资料页找到例程，点击 Add routine 会预填 "Set up a routine to "，补齐指令发送即可创建。
2. 点击已有例程能查 Schedule、Next run 与 Instruction，也能看 Active 开关和运行历史（Run history）。
3. **关闭 Active 开关即可暂停，向左滑动所在行可直接删除。** 状态与桌面端双向实时同步。

出处：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)。

### 计划调度与时区配置

时区检查路径：Settings -> Bot -> Timezone。

| 模式 | 运行机制 | 注意事项 |
| :--- | :--- | :--- |
| Auto-detect | 自动跟随当前电脑时区 | 适合固定地点；跨国差旅容易导致运行时间变动 |
| 手动指定时区 | 手动下拉选择对应时区 | 面向特定区域（如北京时间 UTC+8 或美东 EST）建议手动指定 |

- **新建定时例程不会立刻首跑**，必须等待下一个计划时间点。例如早上 8:05 设每天 8:00 运行，首次执行是在明早 8:00。
- **周末若需连续巡检，指令中必须明确强调“包括周末在内每天运行”。** 未作特殊声明时，Bot 默认按周一至周五执行。

出处：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)，[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 测试例程

在桌面端详情页点击底部的 Test 按钮即可手动触发，按钮状态会变为 Running…，执行反馈直接打在聊天窗口中。

**测试执行的是真实操作**，会启动云电脑浏览器、改写工作区文件并正常扣除额度，涉及删改先用沙箱数据测试。**若提示 Couldn't start a test run，需要检查云电脑连接状态或是否有前序任务阻塞。**

出处：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)。

## Webhook 与 Slack 触发器：从轮询走向被动唤醒

![Webhook 与 Slack 触发器：从轮询走向被动唤醒](/info/08-skills-routines-s3.png)

定时轮询外部网页极费额度，高频空转会迅速耗尽整周算力。**改用事件驱动唤醒 Bot**，平时彻底休眠，外部有变化时再被动触发。

2026-10-12 起，Grok Bot 纳入 The X Subscription 体系，与 Grok、Cursor 共享额度池：

| 订阅档位 | 价格 | 用量倍数 | Bot 支持情况 |
| :--- | :--- | :--- | :--- |
| Premium | 每月 $30 或每年 $300 | 4 倍基础用量 | 包含 Bot |
| Super | 每月 $100 或每年 $1000 | 15 倍用量 | 包含 Bot |
| Ultra | 每月 $200 或每年 $2000 | 50 倍用量 | 包含 Bot |
| Plus | - | - | 不包含 Bot |

### Webhook 配置与异步验收

在聊天窗口发送指令，可让 Bot 创建 Webhook 触发器。

```text
为当前 Bot 创建一个 Webhook 触发的例程，命名为“外部知识接收端”。
指令内容：读取请求体中的 JSON 数据，提取 url 和 note 字段，将其抓取整理为 Markdown 存入 /workspace/notes 目录。
```

在桌面端打开例程详情，展开 Webhook 查看核心字段：
1. POST to：接收外部请求的公网唯一 URL。
2. key：鉴权私钥，调用时需在请求头携带 `Authorization: Bearer <key>`。
3. header：拼接完整的请求头文本，点击可直接复制。

**配置必须点击 Save 保存后才会在网关生效并生成密钥。** 详情页若卡住点不开，让 Bot 发送直达链接。

[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

外部系统通过 POST 请求推送数据，直接带上 JSON 请求体。

```json
{
  "url": "https://example.com/article/1024",
  "source": "ios_share",
  "note": "精读核心论点并归档"
}
```

Bot 会把 JSON 作为上下文变量，连同预设 Instruction 一同送入模型。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

- **HTTP 200 仅代表网关成功接收请求并启动运行，不代表任务执行成功。** 业务成败需在聊天窗口或工作区落盘文件查看。
- 返回非 200 说明任务未建立，通常因例程处于暂停（Paused）状态或密钥失效。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### Slack 触发器与防爆额度

Slack 插件是随对话实时调用的读写工具；Slack 触发器是例程启动条件，使用前必须在 Cursor 账号集成中完成授权。

用自然语言发指令，即可建立监听。

```text
创建一个 Slack 触发例程：当 #incident-response 频道中有人发消息提及 @bot 且包含短语 "needs repro" 时，在云电脑上拉取报错日志并尝试复现。不要监听其他频道，也不要在没有该短语时响应。
```

监听类型支持四种：Bot 被提及、匹配特定词句、添加表情回应，或是接收任意消息。

- **严禁在公共频道监听任意消息**，闲聊打卡会触发全量匹配，整周额度一天就会烧光。
- 必须绑定单一专属频道，不能选“整个工作区”。
- 过滤条件尽量收紧，比如限定特定前缀或工单链接。
- 触发器只对创建后的新消息生效，历史消息不追溯。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

## 自动化实战案例：三种典型流水线

### 案例 1：手机一键入库知识库（iOS 快捷指令 + Webhook）

社区作者铁柱（@cgnot996）搭了一套归档流。在手机上刷到技术文章或视频时点系统分享，Grok Bot 会自动抓全文、提要点，整理成 Markdown 格式写进 `/workspace/knowledge/inbox.md`。

按这几步配置。
1. **新建云端例程**：在 Grok Bot 端新建“手机知识归档”例程，触发条件选 Webhook，拿到专属的 POST URL 和 Authorization 标头。
2. **编写处理指令**：指令设为接收传入的 URL，在云电脑用浏览器打开；要是视频就提取文稿；解析完后按格式提取标题与标签，并整理核心要点与关联链接，追加写入 `/workspace/knowledge/inbox.md`。
3. **创建手机快捷指令**：在 iPhone 打开“快捷指令”App 新建一条，打开“在共享表单中显示”，接收类型勾选“网页和文本”。
4. **添加请求节点**：添加“获取 URL 内容”节点，方法选 `POST`，URL 填 Webhook 目标地址，头部加 `Authorization` 值为 `Bearer [你的私钥]`，请求体选 `JSON` 并将 `url` 绑定到“快捷指令输入”。
5. **解决分享限制**：微信公众号等应用无法直接唤起带快捷指令的分享面板。**额外建一条“输入框中转”快捷指令绑到操作按钮（Action Button）**，点开弹窗贴链接，再转发给 Webhook。

**手机端只做轻量参数捕获与 HTTP 发送，繁重的内容抓取和排版全交给云端异步跑。** 这样手机不耗电也不用等，几秒就能退出来。

出处：[《Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)，[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 案例 2：虚拟机两段式巡检与额度极限优化

社区作者铁柱（@cgnot996）优化了“营销总监”Bot 的 6 条例行任务。他把盯 xAI 回复和每日审 PR 这两项纯等变动的巡检改成轻量比对，有实质进展才叫醒模型，每周省下 8 至 10 次无效空转。

任务分为两类。

| 任务类型 | 典型代表 | 调度策略与运行特征 |
| :--- | :--- | :--- |
| 到点必须交付产物 | SEO 日报、权重月报 | 到点产出完整报告让人查阅，保留原生定时调度 |
| 到点单纯等待变动 | 监控页面更新、新 PR 检查 | 定时空转会扣额度，需要改成轻量检测 |

落地分四步走。
1. **部署本地哨兵**：在 Grok Bot 跑着的 Linux 虚拟机本地写一个极简脚本，用 Python 或 Bash 都行，完全不调大模型。
2. **配置定时比对**：用 Linux 自带的 `cron` 定时器跑脚本，工作日每半小时查一次。脚本只比对网页哈希值或查 GitHub 接口看 PR 数，耗时几秒且不消耗 Grok 订阅额度。
3. **实施差异唤醒**：**比对发现实质变动后，脚本才执行 `curl` 向 Webhook 发起 POST 调用。**
4. **模型介入处置**：Bot 醒来后开始读 PR 代码或回复内容，梳理决策建议并推送通知。

机械判断交给本地脚本，需要动脑才叫醒大模型。这样不用为了一句“今日无事发生”白白消耗大模型上下文。

出处：[《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。

### 案例 3：每日客户流失风险监测

官方团队与运营 29 个 Bot 的作者 melvindvivas 采用这套方案监控客户异动。每天早晨自动拉取用量与工单指标，生成预警观察清单，全程严格受控。

落地分四步走。
1. **确立岗位章程合同**：建专职 Account Risk Bot，在 Profile 的 Description 写明规则合同，定好风险阈值。比如 API 调用量连续三天跌幅超 40%，且伴随没解决的 P1 工单。
2. **设定定时拉取任务**：配好工作日早晨 8:00 跑的例程，定时拉取源系统指标。
3. **配置故障熔断机制**：**数据仓库连接超时或数据未就绪，直接报告缺失失败原因，严禁拿昨天快照推测，严禁输出未证实数据。**
4. **设置安全审批人闸**：在 Settings 的 Custom Rules 里把发邮件、修改 CRM 字段和分发清单全部设为“先询问”（Ask first）。Bot 整理出的清单只在聊天窗口静默展示，等客户经理核实后手动点击批准卡片。

**高价值自动化不能只给模型放权，赋予执行能力的同时必须加上边界合同与人工闸门。**

出处：[《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)，[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## 例程排错指南

### 计划时间到了，Bot 完全没有反应
- 桌面端 Details 确认未被 Paused，手机端确认 Active 开启。**久未登录超时未回 Bot 确认，任务会自动暂停**。
- 核对 When to run 时区与周末设置。新建计划只等下个自然周期，先点 Test 测链路。
- 手机端查“运行历史”，**显示 No runs yet 说明信号没进网关**，显示 Failed 可点开看具体报错。

出处：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### 外部 Webhook 推送了，但例程未启动
- 调接口先看返回值，**非 200 说明请求被网关拦截**。
- 核对请求头 `Authorization` 的 Bearer 密钥，重新生成后旧密钥立刻作废。
- 新建触发器后**必须点右下角 Save**，端点和密钥才会在网关生效。

出处：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### Slack 触发器不触发
- 触发器**只对上线后的新增消息生效**，编辑历史消息不会触发。
- 确认没发错频道，账号在目标频道需有读取权限，**关键词要精确匹配**。

出处：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### 任务跑了一半突然卡死中断
- 后台无人值守的审批卡片**只等待约 10 分钟**，超时变 Expired 就会中断失败。
- 开启通知，或在 Settings > Bot > Auto-review 模式的“自定义规则”中放行信任动作自动执行。
- 遇报错右键气泡点 **Copy request ID**，带上报错文本找官方调日志排查。

出处：[《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)

### 云电脑更新后，本地脚本与定时器丢失
| 更新类型 | 环境保留情况 |
| :--- | :--- |
| 软件更新 | 云电脑环境与文件不受影响 |
| 计算机更新（“设置”>“计算机”>“更新 Bot 的计算机”） | 重构镜像；保留 `/workspace` 与浏览器登录态，**清空 apt 全局包（如 cron）** |

出处：[《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)，[《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)

## 容易踩的坑

1. **点 Test 会真执行**：会调用工具删文件，**测试前在指令留审批断点**。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)。
2. **轮询与定时机制**：每 5 分钟轮询耗尽整周额度，**用轻量脚本比对，有变动再唤醒模型**。“每天 9 点”默认工作日跑，**注明“包括周末在内”，在 Settings 固定时区**。

   [《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。
3. **聊天框勿贴 Webhook 密钥**：会记入云端历史。**凭证须在安全机密信息请求卡片输入**，误贴立刻删除。

   [《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。
4. **防审批拦截静默失败**：设拦截须开移动端通知。**审批弹出后 10 分钟无人应答超时报废**。[《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)。
5. **Bot 共享环境**：在 `/workspace/temp` 删文件影响其他 Bot，**写文件须为各项目指定独立子目录**。

   [《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)。

## 做完怎么验收

按顺序过完这四步，**全通过才能放手让它无人值守**：

1. 核对时间：在详情页确认 **Next run** 时间戳和本地时区完全对得上。
2. 测缺数据：断网或传空文件点 Test，例程必须报错终止，不能瞎编内容。
3. 测审批拦截：故意发删除或外发指令，要是没弹卡直接执行，说明有漏洞，得去 Settings 补。
4. 查日志落盘：正常跑一次，去 `/workspace` 确认文档已写入，且聊天窗口没有刷屏。

出处：[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## 延伸阅读

### 相关章节

- [第 20 章 可靠的自动化：定时、Webhook 与事件触发](/part3/20-automation)

### 官方文档

- [《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)
- [《例程》](https://cursor.com/cn/help/grok-bot/routines.md)
- [《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)

### 社区实战

- [《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [《Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
