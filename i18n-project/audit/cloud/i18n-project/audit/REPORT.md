# 翻译前审查报告

审查日：2026-10-29。真源：`RongleCat/grok-bot-learn` `main` @ `03c8f24`（本环境克隆到 `/workspace/grok-bot-learn`）。站点：https://bot.fmcat.top

## 清单怎么定的

`i18n-project/SOURCE_PAGES.tsv` 在该提交和 `https://raw.githubusercontent.com/RongleCat/grok-bot-learn/main/i18n-project/SOURCE_PAGES.tsv` 都不存在（raw 返回 404）。未猜一份不存在的表。

上线篇目按站点配置重建，共 **61** 篇，与任务所说篇数一致：

- `site/docs/.vitepress/config.mts` 的 `srcExclude` 排除 `admin/`、`advanced/`、`appendix/`、`core/`、`guide/`、`resources/`、`start/`、`zz-bots.md`、`cases/outdated.md` 后，剩余 **60** 篇。
- 这 60 篇与 https://bot.fmcat.top/sitemap.xml 的 60 个 `<loc>` 一一对应。
- 第 61 篇是 `site/docs/xhs.md`：会构建，但 `sitemap.transformItems` 去掉它，并 `noindex`。https://bot.fmcat.top/xhs 返回 200。

另扫：`site/docs/.vitepress/theme/tools.json`、`bots.json`、`ecosystem.json`、`changelog.json`，以及 `site/docs/.vitepress/seo.json`。

站内相对链接 1033 条里，图片与已发布路由均能落到文件。`guide/`、`core/` 里的旧帮助链接不在这 61 篇里，未改。

## 问题

| 优先级 | 文件 | 问题 | 建议/已改 |
| --- | --- | --- | --- |
| P0 | `site/docs/part3/22-feishu-wechat.md` | 两处 `file:///workspace/grok-bot-learn/v3/src/help_grok-bot_*.md`。读者打不开，并暴露仓库内路径与源文件名。 | 已改。改为 [例程](https://cursor.com/cn/help/grok-bot/routines.md) 与 [方案与计费](https://cursor.com/cn/help/grok-bot/plans.md)。抽检均为 200。 |
| P0 | `site/docs/part2/18-solo.md` | 延伸阅读链出内部文件名 `docs_grok-bot_*.md`、`help_grok-bot_*.md`。其中 `connect-plugins.md` 返回 404。 | 已改。去掉内部文件名，插件页改为 [连接应用](https://cursor.com/cn/help/grok-bot/connect-apps.md)（200）。 |
| P0 | `site/docs/part1/07-apps.md` | `connect-plugins.md`、`team-bots.md` 的 `.md` 地址返回 404（正文以 `# Page not found` 开头）。不带 `.md` 的旧地址会 302 到新页。 | 已改。分别改为 `connect-apps.md`、`shared-bots.md`。 |
| P0 | `site/docs/part1/01-what-is.md`；`site/docs/part1/09-group-team.md`；`site/docs/part1/11-safety.md`；`site/docs/part4/23-enterprise.md`；`site/docs/part4/25-faq.md` | 仍指向已更名的 `team-bots` / `connect-plugins`。`.md` 形式 404；无后缀形式仅靠重定向。 | 已改。统一到 `shared-bots.md`、`connect-apps.md`。 |
| P0 | `site/docs/part1/01-what-is.md` | 「2026 年 10 月 7 日默认切为 Claude Opus 5.5」把路由说成单一默认模型。官方写明不绑定单一模型，也不能查看或指定。 | 已改。保留「可能路由到 Claude Opus 5.5 等模型」。依据：https://cursor.com/help/grok-bot/models |
| P0 | `site/docs/part1/11-safety.md` | 「底层切到 Claude Opus 5.5」同样写成整站换模。 | 已改。改为「可能路由到 Claude Opus 5.5 等更强模型」。依据同上。 |
| P0 | `site/docs/part3/19-orchestration.md` | 「系统解耦换上 Claude Opus 5.5」同样写成整站换模。 | 已改。改为「任务可能路由到 Claude Opus 5.5 等模型后」。依据同上。 |
| P0 | `site/docs/part1/01-what-is.md` | 「GPT-6 Astra（2026-09-30 发布）」把 dots 上线日写成 Astra 发布日。OpenAI 写明 dots 于 2026-09-29 上线，并由 GPT-6 Astra 驱动；Pro 与 Business Premium 包含第一个 dot，连接 4,000+ 应用。 | 已改。依据：https://openai.com/index/introducing-dots/ （本机 curl 对该页 403，属拦截；页面正文由直接抓取读到，日期以该页为准）。 |
| P0 | `site/docs/cases/x-hot.md` | 案例标题与收束句写「答疑群」，未写「付费」。同节下一段已有「付费答疑群」。 | 已改。标题与收束句改为「付费答疑群运维助手」。 |
| P1 | `site/docs/part1/01-what-is.md`；`part1/08-skills-routines.md`；`part1/09-group-team.md`；`part1/10-usage.md`；`part1/11-safety.md`；`part2/14-engineering.md`；`part2/17-gtm.md`；`part2/18-solo.md`；`part3/19-orchestration.md`；`part3/20-automation.md` | 仍指示打开已删除的 Edit Profile，或把长期规则写入个人 Bot 的 Description。第 3 章已是现行做法。官方：个人 Bot 没有 Description，长期规则在对话里让它记住；共享 Bot 仍在详情 About 编辑 Description。侧边栏移除 Edit Profile 见本站 `changelog.json` 的 PC 0.57.0。 | 已改。指令改为「个人 Bot 发在对话里并让它记住；共享 Bot 写在详情 About」。依据：https://cursor.com/help/grok-bot/edit-bot.md |
| P1 | `site/docs/part1/01-what-is.md` | 「移动端支持 iPhone」漏了 iPad 与 Android。同站 `part1/grok-vs-grok-bot.md` 已写这三端。 | 已改。补上 iPad 与 Android。依据：https://cursor.com/help/grok-bot/mobile.md （「available on iOS and Android」）。 |
| P1 | `site/docs/part1/07-apps.md` | 步骤仍写「搜插件点添加」。官方页已称 Connect apps。未对照现行客户端按钮原文，不敢改按钮字。 | 只记不改。链接已改到连接应用。 |
| P1 | `site/docs/.vitepress/seo.json` | `part2/14-engineering.md` 的描述写「自动匹配 Claude Opus 5.5 等模型」。有「等」，与「不绑定单一模型」不冲突。 | 只记不改。 |
| P1 | `site/docs/guide/`、`site/docs/core/` | 仍有 `team-bots`、`connect-plugins`。这两目录在 `srcExclude` 中，不在 61 篇、也不进 sitemap。 | 只记不改。未上线。 |
| P2 | 61 篇 Markdown | 没有连续 3 行及以上空行。引号和顿号风格不完全一致。 | 只记不改。 |

## 扫过但没有记成问题的项

- `bot.tiezhu.si`：61 篇与上述 5 个 JSON 中 0 次。
- 付费群：`group.md`、`about.md`、`seo.json` 的 `group.md` 条目已写「付费」。`group.md` 首段后半句是「群是付费群」，标题是「付费答疑群」。
- 错别字抽查：`做为`、`既使`、`必需要`、`阀值` 在 `site/docs` 中 0 次。
- 站内图片：`/info/*.png` 在 `public/info` 均有同名 webp 或 png，缺失 0。
- 五个 JSON：无 `file://`、无 `tiezhu.si`、无未标「付费」的「答疑群」。`changelog.json` 是官方更新译文，未改措辞。
- 飞书 wiki（`jcng5q8n0f3z.feishu.cn`）抽检会跳到登录页（HTTP 200），不能据此判死链，也不记「阻塞、需人工」。
- `https://x.ai/changelog/bot` 对本机 curl 为 403，是拦截，不是 404。
- 订阅价格（Plus $8、Premium $30、Super $100、Ultra $200，Plus 不含 Bot）与 https://docs.x.ai/x-subscription/pricing 一致，未改。
- 模型名：官方帮助页自己写出 Opus 5.5。本次只改「默认换成这一个模型」的错误事实，没有把官方已经公开的名字从正文里删掉。

## P0 清零

上线 61 篇里的 P0 都已改。标明「阻塞、需人工」的条数是 **0**。
