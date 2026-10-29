# UI i18n gap FIX（对照 audit/UI_I18N_GAPS.md）

- **日期**：2026-10-29（America/Los_Angeles）
- **范围**：theme chrome 硬编码抽出 → `ui.json` + `locales/*/ui.json`；内部链接 `localePath`
- **约束**：本轮 **未 push / 未 deploy**；仅本地 commit
- **对照**：`i18n-project/audit/UI_I18N_GAPS.md`

## 改了哪些文件

### 新增
| 文件 | 说明 |
|---|---|
| `site/docs/.vitepress/theme/ui.json` | root（zh-CN）UI 字符串真源 |
| `site/docs/.vitepress/theme/locales/{zh-Hant,en,ja,ko,es,pt-BR}/ui.json` | 六语种覆盖（短标签占位/可用译文） |
| `i18n-project/logs/ui-i18n-gap-FIX.md` | 本文件 |
| `i18n-project/audit/UI_I18N_GAPS.md` | 验收缺口清单（审计侧） |

### 修改（组件 / i18n）
| 文件 | 改动 |
|---|---|
| `theme/i18n.ts` | 新增 `useLocalePath` / `useLocaleSeg` / `stripLocalePrefix` / `partKeyFromPath` / `bcp47`；导出 `NON_ROOT` |
| `theme/NavGroupPill.vue` | `ui.nav.groupPill` + `localePath('/group')` |
| `theme/SiteFooter.vue` | `ui.footer.*` + `localePath('/group'|'/about')` |
| `theme/PartBadge.vue` | `partKeyFromPath` + `ui.parts.*`（修 locale 页不渲染） |
| `theme/Changelog.vue` | `ui.changelog.*` tabs/title/chip；日期改 `Intl.DateTimeFormat(bcp47)`；`items` 改 `computed` |
| `theme/XiaoTiezhuLanding.vue` | `ui.xiaotiezhu.title` / `joinHint`；CTA `/group` → `localePath` |
| `theme/JoinCard.vue` | QR `alt` → `ui.join.qrAlt` |
| `theme/DocEndCard.vue` | `stripLocalePrefix` 匹配 + `localePath('/group')` |
| `theme/Home.vue` | 内链全面 `localePath` |
| `theme/EcoIndex.vue` | 卡片页 `localePath` |
| `theme/ToolIndex.vue` | 工具卡链接 `localePath` |
| `theme/ToolMeta.vue` | 多语种 skin + `rootCatById` 回退 + `localePath` |
| `i18n-project/ENGINEERING.md` | 补充 `ui.json` 表项 +「UI 字符串走 theme/locales + localePath」 |

## `ui.json` key 列表

```
nav.groupPill
footer.mpBtn / mpDialog / mpAlt / group / about / friends / note
parts.part1 / part2 / part3 / part4 / cases
changelog.title / tabAll / tabPc / tabMobile / tabOurs / chipOurs
xiaotiezhu.title / joinHint
join.qrAlt
```

六语种文件路径：
- `theme/locales/zh-Hant/ui.json`
- `theme/locales/en/ui.json`
- `theme/locales/ja/ui.json`
- `theme/locales/ko/ui.json`
- `theme/locales/es/ui.json`
- `theme/locales/pt-BR/ui.json`

**请翻译官复核/润色**：以上六文件全部 key（产品名 Grok Bot / 铁柱AGI / 小铁柱 按既有惯例可保留）。英文等已有可用短译文，非空白。

## 抽检（本地 dist，build 后）

| 检查 | 结果 |
|---|---|
| `npm run build` | **PASS**（exit 0，~42s，约 428 HTML） |
| NavGroupPill `/en/` | `<a class="tz-nav-pill" href="/en/group">Paid Q&A Group</a>` |
| NavGroupPill `/`（zh-CN） | `href="/group"` + 文案「付费答疑群」 |
| SiteFooter en | `About the Author`、`/en/about`、`/en/group` 存在 |
| Changelog tabs | 走 `clUi.tab*`；日期 `Intl`（不再写死「×月×日」） |
| PartBadge | locale 页用 `partKeyFromPath`，label 读 `ui.parts` |

验证方式：`cd site && npm run build`，读 `docs/.vitepress/dist/en/index.html` 检索 `tz-nav-pill`。

## 对照 audit：已修 vs 仍未覆盖

### 本轮已修（audit 点名 P0 chrome — 仓库侧）
- NavGroupPill / SiteFooter / Changelog 标题·tabs·chip·日期 / PartBadge / 小铁柱 h1·hint / JoinCard alt
- Home / DocEndCard / EcoIndex / ToolIndex·ToolMeta 内链 locale 前缀

### 仍未覆盖 / follow-up（P1，本轮未修）
| 项 | 说明 |
|---|---|
| **P1** `.vitepress/seo.json` og/twitter description | 仍简体 home 文案；需按语种覆盖或改 frontmatter |
| **P1** `config.mts` JSON-LD `inLanguage: 'zh-CN'` | 写死；需按页 locale |
| **P1** `friends.json` 站名 | 「噪音之后」「万象 AI 实验室」等专名；可保留或另做 locale |
| **P1** `Home.vue` `segs()` | 按中文标点切句；扩拉丁标点 |
| **P1** Tool skin 映射表 | 多语种 label 作 key（已有 `rootCatById` 回退）；可再收敛到稳定 cat id |
| **策略** 小铁柱 title | en ui 仍产品名「小铁柱」；md frontmatter 同 |

### 线上
点名 P0 在**仓库已修**；**未 deploy**，线上非 zh 仍会见旧简体，直至铁柱确认部署。

## 请翻译官补的文件与 key

优先润色（非空白，求自然 UI 短句）：

1. `theme/locales/en/ui.json` — 全部 key  
2. `theme/locales/zh-Hant/ui.json` — 全部 key  
3. `theme/locales/ja/ui.json` — 全部 key  
4. `theme/locales/ko/ui.json` — 全部 key  
5. `theme/locales/es/ui.json` — 全部 key  
6. `theme/locales/pt-BR/ui.json` — 全部 key  

专名勿乱译：Grok Bot、铁柱AGI、小铁柱、xAI、X @cgnot996。

## 本地 commit

见最终回报 hash。作者：`学习站多语言工程 <i18n@bot.fmcat.top>`。未 push。
