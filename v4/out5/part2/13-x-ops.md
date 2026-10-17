# 第 13 章 案例：在 X 上做内容与运营

直接写脚本高频调用发布接口，容易被风控封禁，几天内就会烧光整周额度。

- 搭建云端虚拟机流水线，微信发一句话，自动检索选题并写出初稿。
- 坚守**只出草稿、人工点击发布**，既保住账号安全，又接管了机械劳动。

## X 平台原生能力：从只读检索到评论区派活

2026-10-08 原生只读上线，搜帖与 7天热度走订阅池。2026-10-11 的 v0.70.2 支持不绑账号搜公开推文，见[记录](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)。

|类型|动作|规则与风控|
|---|---|---|
|原生只读|搜帖、单帖解析、7天热度|走订阅池，无封号风险|
|外部触发|评论区 @bot 提取归档|路由至星标主 Bot，严禁自动回推|
|账号写入|发推、私信、读收藏、点赞|走官方 API，**严禁用无头浏览器发帖**|

### 怎么做
1. **对话框**：输入「帮我搜过去 3 天大家怎么评价 XX 话题」，或贴链接交代「提取这条推文的核心观点与读者互动争议点」。
2. **评论区**：回复 `@bot 提取本帖核心逻辑并存入选题库`，见[说明](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 验收标准
- **提取完整**：带回原始来源、发布时间与讨论脉络。
- **响应边界**：派活后 **30 秒内出日志**，只起草不代发，绝不自动点赞或发帖。

## 5 个 Bot 模板与多 Agent 协同体系

**单个 Bot 兼顾调研、文案与复盘容易上下文混乱。** 解决办法是让专员各司其职，在同一台云电脑里共享文件。

> 来源：[微信里说一句，就能运营X：我的 5 个 Bot 模板公开了](https://x.com/Chchenhao0129/status/2109258247790313478)  
> 作者：[Hardy Chen @Chchenhao0129](https://x.com/Chchenhao0129)

![微信里说一句，就能运营X：我的 5 个 Bot 模板公开了](/cases-img/fs34-0.jpg)

![微信里说一句，就能运营X：我的 5 个 Bot 模板公开了](/cases-img/fs34-1.jpg)

Grok Bot 底层是自带完整 Linux 系统的云端虚拟机。同一账号下的所有 Bot 共享同一台云电脑，有各自独立的桌面会话、文件管理器与终端。宿主机配备至强 8 核 8 线程 CPU、16GB 内存与 128GB 硬盘空间（作者自述，未核），机制勘误见《铁柱推文合集②：产品功能与版本观察》[https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)。

**这台机器的文件系统与网络完全相通，前一个 Bot 存进工作目录的素材，后一个 Bot 能直接读取。** 社区创作者 Hardy Chen 开源了 5 套专员模板，覆盖 X 运营环节，配置细节见《微信里说一句，就能运营X：我的 5 个 Bot 模板公开了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

| 专员名称 | 官方分享模板直达链接 | 核心职责 |
|---|---|---|
| 情报总监 | [https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD](https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD) | 追踪热门趋势与高互动爆款，找可靠来源和切入角度 |
| AI新闻雷达 | [https://x.ai/bot/wUbWteZc9NS-RUrJc22nh](https://x.ai/bot/wUbWteZc9NS-RUrJc22nh) | 从 AIHOT 筛选技术资讯并核对出处，过滤噪音 |
| 推文二创 | [https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_](https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_) | 阅读原帖链接，撰写引用推文或回复并补充见解 |
| 短推成稿 | [https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5](https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5) | 将事实素材写成口语化短推 |
| X数据复盘 | [https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN](https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN) | 读取发帖数据与 CSV，分析规律并输出后续试验动作 |

### 调度配置步骤

1. 把 5 个模板添加到自己的账号。
2. 挑一个主 Bot 作为调度入口。
3. **把初始化提示词直接发给主 Bot，将账号定位、专员路由与写作规范写入持久上下文。**

提示词内容引用自《微信里说一句，就能运营X：我的 5 个 Bot 模板公开了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

::: details 调度配置步骤
```text
我已经添加五个 X 运营专员：情报总监、AI新闻雷达、推文二创、短推成稿、X数据复盘。请保留你的原有功能，作为这套团队的统一入口，完成一次初始化。

1. 先检查能力和连接
确认当前环境能发现 Bot、向 Bot 发任务并接收回执。找到五个专员的实际 Bot ID，核对名称、职责和来源，遇到同名先消歧。保存持久的“角色—名称—ID”路由，让后续聊天和微信入站任务都能读取。缺 Bot 或缺工具时明确告诉我，不凭名称宣称连接成功。

2. 确认我的账号定位
一次只问一个关键问题，了解主题、目标读者、我能提供的价值和不写的话题。也可以分析我授权提供的主页和近期帖子，提出建议，等我确认。把已确认定位和表达偏好持久保存，并同步给相关专员。不要继承模板作者的个人信息。

3. 自动理解需求、安排任务
找选题、热点、爆款拆解交情报总监；AI新闻交AI新闻雷达；原帖回复、引用、二创交推文二创；短推写稿、改稿交短推成稿；发帖数据分析交X数据复盘。
多步任务由你安排先后，传递来源、我的定位和必要上下文，等真实回执后汇总。日常不要求我指定岗位，也不要求我重复文风。专员失败就说明卡点，不能悄悄代写并声称是专员成果。

4. 保存默认写作要求
像跟朋友分享：讲清发现、理由和具体用途，允许适量语气词，不堆口号。不编我的亲历、数字、测试结果或涨粉成绩。原帖保留归属，新闻核对来源和日期。默认沿用这些要求，我另有要求时再调整。
你交付前检查事实、来源、定位和可读性。来源和说明放在草稿外，方便我看，也方便复制正文。检查X可发布长度，超出则给短版或说明需要的账号功能。

5. 真正跑一次
给五个专员各派一个小任务，检查接收、完成、回传，再跑“找素材→短推成稿→你检查→返回草稿”。保留可核对的任务记录。数据复盘没有真实数据就报告缺口，不编数字。汇报通过项、失败项和恢复办法，不把发出任务当完成。

6. 根据真实反馈改进
记录已发布内容和表现，提出下一轮调整。日常选题和写作规则的小改动留版本、可回退；账号定位、授权范围、发布权限、定时安排或新增收费服务变更先问我。小样本形成试验建议，不宣称已验证涨粉规律。

默认只起草。发帖、回复、点赞、关注和私信由我另行决定，不自动执行。
```
:::

配置跑通后，主 Bot 会记住下属 ID。日常提出选题并成稿的需求，主 Bot 会自动调度情报总监抓素材，再递给短推成稿，最后交付初稿。

### 验收标准

在聊天窗口让主 Bot 执行一次找选题并成稿的测试，合格结果要满足两点。
- **多 Agent 真实接力**：主 Bot 与专员的后台记录中，能看到任务派发、子 Bot 实际执行与回传过程。
- **草稿质量与排版规范**：返回的草稿不包含机械口号，原始出处和说明文字整齐排在正文下方，不与正文混杂。

## 微信一句话运营：接入手机收发闭环

把主 Bot 接入微信，靠微信内置 ClawBot（或 iLink）插件与 Grok Bot 的 Routine Webhook 建立长连接。**所有 Bot 共享统一额度池，被动接收 Webhook 事件唤醒时没有额外待机空转消耗。**

2026-10-12 推出的 The X Subscription 统一订阅档位如下，规则见《4.3 触发器与自动化：定时、Webhook、在 X 上派活》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)：

| 订阅方案 | 费用 | 额度倍数 |
|---|---|---|
| Premium | $30/月或 $300/年 | 4x 用量 |
| Super | $100/月或 $1000/年 | 15x 用量 |
| Ultra | $200/月或 $2000/年 | 50x 用量 |

### 四步接通微信

1. 在桌面端向主 Bot 发送配置要求，让它检查环境里的监听程序与例程。提示词引用自《微信里说一句，就能运营X：我的 5 个 Bot 模板公开了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)：

::: details 四步接通微信
```text
请把你接入我的微信，让我直接在微信里说X运营需求，并收到结果。沿用已确认的账号定位、默认文风和五专员持久路由。

先检查当前是否已有微信连接器、监听程序和routine，避免重复。参考教程：
https://x.com/KinGao476942/status/2108132811635032316?s=20
核对当前ClawBot/iLink接法和所需工具。缺工具或需要授权时如实说明；需要我安全填写、手机扫码时给出具体步骤，不代替我确认。

准备微信入站Webhook任务和监听保活。Webhook URL、密钥及凭据只通过安全输入保存，不打印到普通聊天、日志或公开截图。

只处理我绑定身份的指令，不读取联系人或群聊历史。入站任务必须读取我的定位、文风和五专员实际ID，按需求真派单、等回执，再原路返回纯文本。默认只起草，写稿失败明确报告，不悄悄代写。

监听保持单一实例。处理前持久保存待办，以消息ID去重；回复成功才标记完成，失败保留并有限重试。登录过期或权限错误停止重试并报告。重启后恢复未完成任务，避免漏回和重复回复。

完成后实际验证：扫码登录、微信入站、你的回复、专员接力和微信收到最终稿。再检查监听重启后的恢复。保留脱敏记录，告诉我哪些通过、哪些未通过，不把配置完成当接通成功。说明监听运行在哪个环境、何时会停，以及如何恢复。
```
:::

2. 手机微信依次点击「我 → 设置 → 插件」，启用「微信 ClawBot」。如果找不到入口，向主 Bot 说明当前微信版本协助核对。
3. 展开桌面端主聊天窗口顶部 Bot 名称，进入「例行任务 / Routines」，打开「微信入站唤醒」卡片，复制 Webhook URL 与密钥。在弹出的安全框里分别填入保存，**切记不要把含 Authorization 的整段长字符串直接塞进单个输入框**。
4. 桌面端向主 Bot 发送「插件已启用，地址和密钥已保存，请检查配置并生成绑定入口」，手机微信扫码授权。接着在微信发「你好」，收到回复通道就通了。

排障记录见《微信里说一句，就能运营X：我的 5 个 Bot 模板公开了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

### 验收标准

在手机微信给绑定的 Bot 发「给我生产 3 条泛流量的帖子」。**两分钟内收到 3 条包含切入角度与素材来源的草稿，且后台日志能查到派发记录，就算搞定。**

## 只出草稿的人闸设计与安全边界

自动化发帖一旦出现模型幻觉、错误日期或冒犯回复，会造成不可逆损害。**流水线末端必须加一道安全人闸，彻底锁死发布、点赞、关注、私信和删除这五个动作，只让模型起草。**

::: details 只出草稿的人闸设计与安全边界
```text
[微信一句话 / 定时触发] 
       │
       ▼
[主 Bot 调度中心] ───► [情报总监 / AI新闻雷达 抓取素材]
       │
       ▼
[推文二创 / 短推成稿 编写草稿]
       │
       ▼
[主 Bot 事实与长度校验]
       │
       ▼
[推送到手机微信 / 客户端对话框] ───► (停住：系统不具备自动发帖权限)
       │
       ▼
[人工审阅：修改、定夺] ───► [人工手动复制到 X 发布]
```
:::

### 双层防护配置

1. **提示词死命令**：在主 Bot 及专员提示词末尾写死：
   「默认只起草。发帖、回复、点赞、关注和私信由我另行决定，不自动执行。来源和说明文字必须放在草稿外，便于人工阅读与一键复制正文」。
2. **系统级拦截**：在 Grok Bot 的 Settings → Custom Rules（或 Auto-review）中，**把包含 `send`、`post`、`buy`、`transfer`、`delete`、`permissions` 的操作全勾选为「Ask first」**。没有你的明确点击，底层绝不执行。

配置规范见《4.3 触发器与自动化：定时、Webhook、在 X 上派活》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 验收标准

实测时发指令「把这条草稿直接发到我的 X 主页上」，合格需满足两点：
- **拦截生效**：Bot 明确拒绝执行，或底层弹出 Ask first 审批拦截卡停止调用。
- **排版合规**：草稿正文与参考链接分离，长度严格符合 X 平台字数限制。

## 实战案例深度拆解

为了更直观地理解不同创作者如何把这套体系融入日常工作，下面拆解三起具有代表性的社区实践案例。三种模式分别对应了不同规模与需求的运营流：

| 实践案例 | 创作者 | 核心架构与方式 | 核心借鉴要点 |
|---|---|---|---|
| 案例 1 | Hardy Chen（@Chchenhao0129） | 5 个 Bot 模板 + 微信 ClawBot 插件 + Webhook | 单入口统一调度、文风定位固化、人闸草稿交付 |
| 案例 2 | SCOTTY BEAM（@ScottyBeamIO） | 三 Agent 协同 + 云电脑共享目录 + 操作录制 | 共享磁盘中转数据、固定参考图规范审美、独立会话设定时 |
| 案例 3 | 铁柱AGI（@cgnot996）、AYi（@AYi_AInotes） | 原生只读检索 + 评论区 `@bot` 触发 + 本地存储 | 零外接 API 降本防封、评论区免切应用派活、`/home/box` 持久化 |

### 案例 1：Hardy Chen 的微信一句话 5 Bot 协同流水线

- **谁**：Hardy Chen（@Chchenhao0129），个人内容创作者。
- **做了什么**：配置了 5 个垂直职能的 Bot 模板，打通微信 ClawBot 插件，实现仅在微信发送一句话需求，即可全自动完成 X 选题发掘、AI 资讯初筛、推文撰写与周度发帖数据复盘。
- **怎么做**：
  1. 先在 Web 端逐一添加 5 个官方分享的 Bot 模板，选定主 Bot 后发送系统初始化提示词，将个人账号定位、目标受众与 5 个专员的持久路由一次性注入主 Bot。
  2. 随后配置微信入站 Webhook 与保活监听，通过手机扫码将主 Bot 连入微信。
  3. 针对每天的资讯更新，设定 Asia/Shanghai 时区每天早上 7:30 的定时任务，让 AI新闻雷达从 AIHOT 抓取信息并核对原始来源，推送到微信。
  4. 发帖数据分析时，按要求提供后台 CSV 文件，让数据专员梳理互动表现并指导下周动作。
- **可以借鉴什么**：
  - 建立单入口调度体系，不把精力浪费在挨个专员传话上。
  - 用初始化提示词固化账号定位，避免每次发指令都要重新解释文风。
  - 坚持草稿交付机制，草稿说明与正文分开排版。
  - 遇到微信连上不回复时，按照「监听进程—保活任务—消息去重」的标准路径排障，不盲目反复解绑扫码。
  - 详细复盘见《微信里说一句，就能运营X：我的 5 个 Bot 模板公开了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

### 案例 2：SCOTTY BEAM 的三 Bot 全自动内容流与四套方案横评

> 来源：[Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](https://x.com/ScottyBeamIO/status/2089417013647073753)  
> 作者：[SCOTTY BEAM @ScottyBeamIO](https://x.com/ScottyBeamIO)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-0.jpg)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-1.jpg)

- **谁**：SCOTTY BEAM（@ScottyBeamIO），技术型社媒创作者。
- **做了什么**：构建了由研究专员、视觉创意专员与文案起草专员构成的三 Agent 云端更新系统，实现趋势挖掘、信息图设计与推文撰写全程自主衔接，并横向测评了 Grok Bot、Buzz、OpenClaw 与 Hermes 四种 Agent 架构。
- **怎么做**：
  1. 充分利用 Grok Bot 所有 Agent 共用底层云电脑的特性，研究 Bot 在后台检索 X 与公开代码库的趋势并把素材落盘。
  2. 视觉创意 Bot 预先学习作者喂给它的参考信息图风格，直接读取研究素材生成排版一致的视觉图片。
  3. 文案起草 Bot 汇总两者成果形成待发布草稿。针对日常机械化的固定操作，使用操作录制功能（Recording）直接教给 Bot。
- **可以借鉴什么**：
  - 多 Agent 协作时以云电脑共享目录为数据中枢，省去人工复制与数据中转。
  - 通过向设计类 Bot 喂入固定参考图规范视觉审美。
  - 警惕多 Bot 团队会话无法保存定时任务的缺陷，把调度例程拆分到单个 Bot 的独立会话中设置。
  - 架构横评与操作细节见《Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot｜SCOTTY BEAM》[https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb)。

### 案例 3：铁柱与 AYi 的 X 原生检索与评论区 @bot 知识归档

- **谁**：铁柱AGI（@cgnot996）与 AYi（@AYi_AInotes），高频技术研究者。
- **做了什么**：利用 2026-10-08 上线的原生只读能力与 2026-10-11 的 v0.70.2 评论区 @bot 联动机制，搭建了零外接 API 的行业情报监测与移动端一键推文知识入库流。
- **怎么做**：
  1. 日常在对话框中下发自然语言指令，提取任意关键词在 X 过去 7 天的热度变化曲线与关键争论帖，不开启任何付费连接器。
  2. 在手机端刷推文时，遇到长推或技术方案，直接在评论区回复 `@bot` 并写明归档要求。
  3. 星标主 Bot 收到系统事件后，自动抓取推文全文并调用知识库清洗格式，保存为 Markdown 文件沉淀在虚拟机 `/home/box` 目录下。
- **可以借鉴什么**：
  - 用好官方原生只读权限替代第三方爬虫，大幅降低运维复杂度与封号风险。
  - 移动端无需切换应用，通过 @bot 实现轻量化触发。
  - 严格做好数据本地化存储，在云电脑中收敛核心路径并防范重置丢失。
  - 实践要点见《铁柱推文合集②：产品功能与版本观察》[https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd) 与《4.3 触发器与自动化：定时、Webhook、在 X 上派活》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## 容易踩的坑

### 定时任务与额度消耗
1. 多个 Bot 拉进同一个 Team Chat 存不上统一 Routine（SCOTTY BEAM 实测），**必须切回独立个人会话单独配**。
2. 部分版本默认按工作日跑，创建指令要写明「包含周六和周日，每天按时执行」（铁柱实测）。
3. 系统设置核对本地时区为 Asia/Shanghai，避免北京时间早晨 7:30 被当成凌晨跑。
4. Bot 额度与 Grok、Cursor 共享，5 分钟轮询即使无更新也读全上下文。**必须改用两段式检查或增量唤醒（Wake on Done）**做初筛；运营 29 个 Bot 的 melvindvivas 也建议定期清理低产出例程。

出处：[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

### 微信与 Webhook 连接排障
1. 微信扫码后无响应多因监听挂起或保活 Routine 暂停，**别反复重扫绑号**。Hardy Chen 经验是桌面端发排查指令查进程与队列，发新测试消息重新跑通。
2. 截至 v0.68.1 客户端详情卡片打不开时，让 Bot 在聊天框发该触发器直达链接查看。

出处：[《铁柱推文合集②：产品功能与版本观察》](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

### 平台交互限制与宿主机环境
1. 评论区派活不支持纯视频；同时 @grok 和 @bot 时不响应；**严禁给评论区派活开放外部发布权限**，防恶意提示词注入。
2. 虚拟机维护会重置临时路径，**脚本、文档与备份数据必须统一保存在 `/home/box`**，并备好自愈脚本。

路径规范：[《铁柱推文合集②：产品功能与版本观察》](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

## 做完怎么验收

1. 主Bot发推抓3条高赞，查作者ID、观点及时间，无报错。
2. 发指令查记录，**确认5专员接力成稿**，严防代写。
3. 微信发ClawBot「以新手视角写一条关于大模型工具的短推」，2分钟回草稿。
4. 发「将刚才生成的草稿直接发布到我的 X 账号」，**须弹Ask first**，未确认不外推。
5. 对齐Routine时间；喂空文件，确认复盘专员如实报缺失、不瞎编。

## 延伸阅读

### 官方文档与发布公告
- [x.ai Changelog](https://x.ai/changelog/bot)
- [The X Subscription 官方公告与定价文档（2026-10-12）](https://docs.x.ai/x-subscription/pricing)

### 社区实战原文

> 来源：[Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](https://x.com/cgnot996/status/2097487429104197688)  
> 作者：[铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](/cases-img/fs06-1.jpg)
- [微信里说一句，就能运营X：我的 5 个 Bot 模板公开了](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)
- [Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot｜SCOTTY BEAM](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb)
- [4.3 触发器与自动化：定时、Webhook、在 X 上派活](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [铁柱推文合集②：产品功能与版本观察](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)
- [Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- [Grok Bot 额度再省一点：定时任务极限优化](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
