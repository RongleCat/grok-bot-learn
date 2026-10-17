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

## 来源

- [官方：快速入门](https://cursor.com/cn/docs/grok-bot/get-started)
- [官方：上手](https://cursor.com/cn/help/grok-bot/onboarding)
- [1.1 Grok Bot 是什么：一页看懂](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [万字长文｜Grok Bot 从入门到精通｜金尘马](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)（摘要见实战案例）
