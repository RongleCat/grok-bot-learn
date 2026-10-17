# 0.1 · 和 Muse、Hermes、dots、Cue 怎么选

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

## 来源

- [1.2 Grok Bot 和 Muse、Hermes、dots、Cue 怎么选](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd)
- [铁柱推文合集④：社区、生态与竞品对照](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg)
