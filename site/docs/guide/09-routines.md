# 第 9 章 · 技能与定时例程

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

## 来源

- [官方：技能与例程](https://cursor.com/cn/docs/grok-bot/work)
- [官方：例程](https://cursor.com/cn/help/grok-bot/routines)
- [4.3 触发器与自动化：定时、Webhook、在 X 上派活](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [Grok Bot 额度再省一点：定时任务极限优化](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
