# 第 7 章 · 记忆与上下文

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

## 来源

- [官方：Bot 会记住什么](https://cursor.com/cn/docs/grok-bot/work)
- [4.6 虚拟机、记忆与备份](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- [Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)（英文，摘要见案例）
- [Grok Bot 百万撤离：一套完善的 Agent 系统备份方案](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)
