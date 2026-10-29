# 自检

## P0 是否清零

清零。上线 61 篇中的 P0 均已写入 `FIXED.md`。`REPORT.md` 里「阻塞、需人工」为 0 条。

复核命令（在 `/workspace/grok-bot-learn`）：

- 61 篇中 `file://`、`tiezhu.si`、`v3/src/`：0 命中。
- `connect-plugins.md`、`team-bots.md`：仅剩未上线的 `site/docs/guide/` 与 `site/docs/core/`，不在 61 篇内。

## 链接抽检

| 结果 | URL | 证据 |
| --- | --- | --- |
| OK | https://cursor.com/cn/help/grok-bot/connect-apps.md | `curl` 200，正文以 `# Connect apps` 开头 |
| FAIL | https://cursor.com/help/grok-bot/connect-plugins.md | `curl` 404，正文 `# Page not found`。这是修改前的地址，已替换 |
| OK | https://cursor.com/cn/help/grok-bot/shared-bots.md | `curl` 200，正文以 `# Shared Bots` 开头 |
| FAIL | https://cursor.com/help/grok-bot/team-bots.md | `curl` 404，正文 `# Page not found`。这是修改前的地址，已替换 |
| OK | https://cursor.com/cn/help/grok-bot/routines.md | `curl` 200，正文以 `# Routines` 开头 |
| OK | https://cursor.com/cn/help/grok-bot/plans.md | `curl` 200，正文以 `# Plans and billing` 开头 |
| OK | https://docs.x.ai/x-subscription/pricing | `curl` 200 |
| OK | https://api.fxtwitter.com/status/2114883723930030505 | `curl` 200，`code: 200`，对应 `cases/x-hot.md` 付费答疑群案例原帖 |
| OK | https://bot.fmcat.top/group | `curl` 200 |
| OK | https://cursor.com/help/grok-bot/models | `curl` 200。页面说明 Grok Bot 不绑定单一模型 |
