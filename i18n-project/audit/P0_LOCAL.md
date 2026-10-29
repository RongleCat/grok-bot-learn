# 本地已确认 P0（P0_LOCAL）

- 时间：2026-10-29（Asia/Singapore）
- 定义：死链/错链（站内已证实缺失；外链 HEAD+GET 均失败）、旧域 `bot.tiezhu.si` 落在读者正文、付费答疑群未写「付费」、明显错误事实
- 本轮：**只报告，未改 `site/` 真源**

## 已确认 P0 表

| 路径 | 问题 | 建议改法 |
|---|---|---|
| （无） | 本地抽样未确认到可直接落修的 P0 | — |

**P0 条数：0**

## 依据摘要
- 站内：抽样 17 篇明细内链 FAIL=0；SOURCE 全量约 286 处 FAIL=0；导航 JSON 路径 FAIL=0。
- 外链：抽检 14 条无 FAIL；3 条未判定（403 或 HEAD/GET 不一致），按规则不当死链。
- 域名：正文/目标 JSON 无 `bot.tiezhu.si`。
- 答疑群：`group.md` 等已写明付费。

## 观察项（非 P0，供云端/人工复核）
| 路径 | 观察 | 建议 |
|---|---|---|
| `tools/feishu-bot.md` + `theme/tools.json` | `https://open.feishu.cn/` HEAD=404 / GET=200 | 可改为 `https://open.feishu.cn/document/home/index` 更稳，非必须 |
| 多篇官方出处链 | Cursor 文档带 `.md` 后缀（如 `.../plans.md`） | HEAD=200，保持或统一去后缀均可（P2） |
| `seo.json` | 缺 `index.md` / `tools/deepseek-harness.md` / `xhs.md` | 补 description（P1） |
| `theme/bots.json` | `每个Bot` 缺空格 | 改 `每个 Bot`（P1 体例） |

