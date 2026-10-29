# 学习站简体真源审查报告

更新：2026-10-29 Asia/Singapore

## 云端任务状态

- 任务：`i18n-audit-20261029`（分支 `cursor/heavy-job-i18n-audit-20261029-0172`）
- 云端 RESULT 自称 SUCCESS，但 **FAILED 于取回**：推送 403（cursor[bot] 无写权限），outputs 未自动落盘到站点仓
- 本轮已从私有仓 `RongleCat/tiezhu-heavy-jobs` 该分支 **手工同步** `outputs/i18n-audit-20261029/` → `i18n-project/audit/cloud/`（含 `content-fix.diff`、15 个 `fixed-md`、云端 REPORT/FIXED/SELF_CHECK）
- 正文修复已应用到本地 `site/docs/**`；i18n 脚手架（locales / config.mts / i18n.ts）未覆盖

## 问题与处理

| 优先级 | 文件 | 问题 | 建议/已改 |
|---|---|---|---|
| P0 | `part3/22-feishu-wechat.md` | 两处 `file:///workspace/...` | **已改**→ cursor.com routines / plans |
| P0 | `part2/18-solo.md` 等 | `connect-plugins.md` 404 | **已改**→ `connect-apps.md` |
| P0 | `part1/07-apps.md` 等 | `team-bots.md` 404 | **已改**→ `shared-bots.md` |
| P0 | `01-what-is` / `11-safety` / `19-orchestration` | 「默认切单一模型」表述 | **已改**→ 按任务路由 |
| P0 | `01-what-is.md` | dots/Astra 日期错误 | **已改**→ 2026-09-29 |
| P0 | `cases/x-hot.md` | 「答疑群」未标付费 | **已改**→「付费答疑群」 |
| P1 | 多篇 Profile / Edit Profile | 已删除入口 | **已改**→ 对话记住 / About |
| P1 | `01-what-is.md` | 移动端漏 iPad/Android | **已改** |
| P1 | `seo.json` 缺部分 description | 非死链 | **只记未改**（可交翻译前补） |
| P1 | `guide/` `core/` 旧链接 | srcExclude 未上线 | **只记未改** |
| P1 | `bots.json`「每个Bot」缺空格 | 本地审查官已改 | **已改**（云端未动此文件） |

完整云端明细见：`cloud/REPORT.md`。

## P0 清零状态

**P0 清零；阻塞 0。**

抽检（2026-10-29）：

```
rg 'connect-plugins\.md|team-bots\.md|file:///workspace' site/docs -g'*.md'
→ 0 命中
```

（`guide/`/`core/` 仍有无 `.md` 后缀的旧路径，未上线，不计入 P0。）

## 本轮实际改动文件（待 commit）

正文 15 篇（云端 fixed-md）：

- `site/docs/cases/x-hot.md`
- `site/docs/part1/01-what-is.md`
- `site/docs/part1/07-apps.md`
- `site/docs/part1/08-skills-routines.md`
- `site/docs/part1/09-group-team.md`
- `site/docs/part1/10-usage.md`
- `site/docs/part1/11-safety.md`
- `site/docs/part2/14-engineering.md`
- `site/docs/part2/17-gtm.md`
- `site/docs/part2/18-solo.md`
- `site/docs/part3/19-orchestration.md`
- `site/docs/part3/20-automation.md`
- `site/docs/part3/22-feishu-wechat.md`
- `site/docs/part4/23-enterprise.md`
- `site/docs/part4/25-faq.md`

另：

- `site/docs/.vitepress/theme/bots.json`（本地空格修复）
- `i18n-project/audit/**`（本报告、cloud 副本、READY_TO_TRANSLATE）

**未纳入本 commit**：`.vitepress/config.mts`、`theme/i18n.ts`、`theme/locales/**`、`site/docs/{en,es,ja,ko,pt-BR,zh-Hant}/**`（多语言脚手架，进行中）。
