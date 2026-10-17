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

## 来源

- [官方：群组聊天](https://cursor.com/cn/help/grok-bot/group-chats)
- [官方：团队 Bot](https://cursor.com/cn/help/grok-bot/team-bots)
- [官方：消息与协作](https://cursor.com/cn/docs/grok-bot/work)
- [4.2 团队编排：章程、岗位与放权](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- [Meet your Team Bots｜n2parko](https://jcng5q8n0f3z.feishu.cn/wiki/KS9Cwan52idy1xkLbnTcSC3xnxb)
