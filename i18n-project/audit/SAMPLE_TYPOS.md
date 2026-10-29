# 本地错别字 / 病句轻扫候选（SAMPLE_TYPOS）

- 时间：2026-10-29（Asia/Singapore）
- 范围：SOURCE_PAGES.tsv 全部 md + `theme/{tools,bots,ecosystem,changelog}.json` + `seo.json`
- 原则：只记高置信；第三方英文原标题中的 `GrokBot` 不改
- 约束：本轮只写报告，未改真源

## 高置信候选

| 置信 | 文件 | 原文片段 | 建议 | 说明 |
|---|---|---|---|---|
| 中 | `site/docs/.vitepress/theme/bots.json` | `给每个Bot配独立飞书机器人` / `给每个Bot都配上独立身份` | `每个 Bot`（Bot 前加空格） | 中文文案产品名空格规范；非错别字，偏体例 |
| 中 | `site/docs/.vitepress/theme/bots.json` | `定期把所有Bot的设定` / `你各个Bot的心血` / `所有Bot的家底` | `所有 Bot` / `各个 Bot` | 同上 |

## 已扫未命中（高置信规则）

| 规则 | 结果 |
|---|---|
| `登陆`（应为登录） | 清单 md / 目标 JSON：**未命中** |
| `帐号`（应为账号） | **未命中** |
| `部份` | **未命中** |
| 宜写「其他」处的 `其它` | **未命中** |
| 正文自造 `GrokBot`（非引用外文标题） | 正文多为引用 Movez 等外文原标题/`@GrokBotRadar`；**不建议改引用标题** |
| `的/地/得` 明显错用（跑的快、看的见等） | **未命中高置信例**；命中句均为合法「地方」「回答得清楚」等 |
| `bot.tiezhu.si` 出现在正文/目标 JSON | **未命中**（仅 `public/_worker.js` 旧域跳转白名单，属正确保留） |
| 付费答疑群未标「付费」 | `group.md` / `about.md` / `home.json` / `funnel.json` / `seo.json` 均已标明付费 |

## JSON 文案扫（tools / bots / ecosystem / changelog / seo）

| 检查项 | 结果 |
|---|---|
| `bot.tiezhu.si` | 无 |
| 未标付费的答疑群文案 | 无（相关文案在 funnel/home/seo，均含「付费」） |
| 明显错字（登陆/帐号/部份/GrokBot 自造） | bots.json 仅有「每个Bot」空格体例；其余未命中 |
| seo 覆盖 | 缺 `index.md`、`tools/deepseek-harness.md`、`xhs.md` 三钥（偏 P1/P2，非错别字） |

## 不改清单（避免误伤）
- 案例/引用里的英文标题 `GrokBot Agents...`、账号 `@GrokBotRadar`
- `ShareGrokBots` 等专有方案名
- `_worker.js` 中的 `bot.tiezhu.si` 跳转集合

