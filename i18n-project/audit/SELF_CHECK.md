# 自检（同步云端产物后）

| 项 | 结果 | 证据 |
|---|---|---|
| 云端产物落盘 | PASS | `audit/cloud/content-fix.diff` + 15 个 `fixed-md` |
| P0 file:// 已修 | PASS | `rg file:///workspace site/docs -g'*.md'` 0 |
| connect-plugins.md / team-bots.md | PASS | 上线正文 0 命中（guide/core 未上线旧链保留） |
| 站内链死链（本地先前） | PASS | DEAD_LINKS_LOCAL FAIL=0 |
| 旧域正文 | PASS | md/json 无 bot.tiezhu.si（_worker 保留） |
| 付费答疑群标注 | PASS | group/about + cases/x-hot 已标「付费」 |
| 链1 routines.md | OK | HEAD 200（云端+本地） |
| 链2 plans.md | OK | HEAD 200 |
| 链3 connect-apps.md | OK | 200（替换 connect-plugins） |
| 链4 shared-bots.md | OK | 200（替换 team-bots） |
| 链5 github.com/RongleCat/grok-bot-learn | OK | HEAD 200 |
| 脚手架未覆盖 | PASS | config.mts / i18n.ts / locales / 语种目录仍为未提交脚手架 |
| 云端 i18n-audit 取回 | 已手工同步 | 原 FAILED=outputs 未自动取回/推送 403；现已从分支拉齐 |
