# Grok 和 Grok Bot 有什么区别

**Grok 是对话助手，Grok Bot 是在云电脑上替你干活的常驻 AI 同事。**
Grok 负责你问我答，关闭网页或 App 对话即结束；Grok Bot 则在独立云电脑里常驻，关掉客户端后台任务依然照跑。
两者都来自 xAI（现名 SpaceXSI），但在交互形态与应用定位上完全不同。

## Grok 和 Grok Bot 的核心区别是什么？

**核心区别在于 Grok 只动嘴给建议，而 Grok Bot 会在云电脑里实际动手操作。**
Grok 是纯粹的对话助手，你问一句它答一句；Grok Bot 则是 2026 年 8 月 11 日由 xAI 和 Cursor 推出的常驻 AI 同事，目前仍是 Beta。
想要建立整体概念，可以先阅读[第 1 章 Grok Bot 是什么](/part1/01-what-is)。

| 维度 | Grok | Grok Bot |
| --- | --- | --- |
| 是什么 | xAI 的 AI 对话助手 | 一组常驻的 AI 同事（AI teammates），目前处于 Beta |
| 在哪用 | grok.com 网页、iOS 和 Android App、X 里的 Grok 标签页 | macOS、Windows、Linux 桌面端，iPhone、iPad、Android 移动端 |
| 怎么干活 | 你问一句它答一句，支持文字、语音、上传文件分析、生图生视频等 | 用打字或语音发消息交代任务，在带浏览器、文件系统和终端的常驻云电脑上跨应用干活，需批准时才找你 |
| 关掉后还跑不跑 | 不跑，用完关掉网页或 App 对话就结束 | 照样跑，合上笔记本、关掉 App，后台任务和例程继续跑 |
| 能不能操作网站和软件 | 不能，不替你在别的网站和软件里动手干活 | 能，登录常用网站和应用把活干完，敏感步骤由人点 Take over 接管 |
| 需要哪档订阅 | 免费可试用，订阅提高额度；包含在 The X Subscription 免费档、Plus 档及以上 | 包含在 The X Subscription 的 Premium、Super、Ultra；Plus 不含 |
| 适合的事 | 即时问答、查报错、写一段文字、生图生视频、看 X 最新动态 | 流程固定、高频重复、跨多网站或软件的活（如巡检官网、每周对账、汇总晨报、复现 Issue） |

**同一账号的所有 Bot 共用一台云电脑，共享文件、浏览器登录态和应用登录。**
每个 Bot 虽然有自己的屏幕，但官方提醒不要把不同 Bot 当成安全隔离，具体运行机制见[第 5 章 共享云电脑](/part1/05-computer)。
若需配置环境，可以参考[第 3 章 安装登录与第一个 Bot](/part1/03-install)。

## 什么时候用 Grok，什么时候用 Grok Bot？

**几秒内能给结果的即时问答用 Grok，需要跨软件、定时跑或多步执行的重复事务用 Grok Bot。**

**适合用 Grok 的场景，集中在即时问答与单次内容生成。**
比如查报错、写一段文字、生图生视频（视频最长 15 秒），或者实时联网搜索网页和 X 的最新动态。
这类任务几秒钟就能搞定，不用动用云电脑。

**适合用 Grok Bot 的场景，主要是流程固定、高频重复且跨多个网站或软件的繁杂工作。**
典型任务包括定期巡检官网出摘要、每周对账、每天汇总晨报、读 Issue 复现缺陷等。
这类工作必须能由人核验结果，高危动作（发信、付款、删除）会停下来等待批准，遇上输密码、两步验证、验证码或付款时可以点 Take over 人工接管。

一次跑通的流程还能存成技能，并设成例程定时自动跑，多个 Bot 也可以在群聊里协作交接。
**需要留意的是，高频轮询和视频处理等任务会迅速消耗每周额度。**
关于额度规划和消耗细节，建议提前查看[第 10 章 额度与成本](/part1/10-usage)。

## 用 Grok Bot 需要买哪档订阅？

**使用 Grok Bot 至少需要每月 30 美元的 Premium 方案，8 美元的 Plus 档并不包含 Grok Bot。**

自 2026 年 10 月起，官方推出了 The X Subscription 统一订阅方案，把 Grok、Grok Bot、Cursor 和 X Premium 整合在一起。
该订阅分为五档：Free（$0）、Plus（$8/月）、Premium（$30/月）、Super（$100/月）与 Ultra（$200/月）。

**Grok 在免费档和 Plus 档就能使用，而 Grok Bot 仅对 Premium、Super、Ultra 开放。**
付费档每周提供一个共享额度池，由 Grok、Grok Bot 以及 Cursor 里的 Grok 模型共同使用。

**老用户也可以直接使用 Grok Bot。**
拥有老的 Cursor 付费个人版、Cursor 团队版，或者关联了 SuperGrok、SuperGrok Plus、SuperGrok Heavy 的账号，都能直接使用 Grok Bot。
更详细的订阅权益，可以查阅[第 2 章 方案与订阅](/part1/02-plans)。

## 延伸阅读

本站章节：
- [第 1 章 Grok Bot 是什么](/part1/01-what-is)
- [第 2 章 方案与订阅](/part1/02-plans)
- [第 3 章 安装登录与第一个 Bot](/part1/03-install)
- [第 5 章 共享云电脑](/part1/05-computer)
- [第 10 章 额度与成本](/part1/10-usage)

官方页面：
- [Grok 官方页面](https://x.ai/grok)
- [Grok Bot 发布公告](https://x.ai/news/introducing-grok-bot)
- [Grok Bot 官方概览文档](https://docs.x.ai/grok-bot/overview)
- [The X Subscription 订阅文档](https://docs.x.ai/x-subscription/grok-bot)
