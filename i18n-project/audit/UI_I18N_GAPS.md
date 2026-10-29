# UI 多语言覆盖缺口（翻译后验收清单）

- **审查日期**：2026-10-29（America/Los_Angeles）
- **范围**：导航 pill、页脚、Changelog 筛选、PartBadge、小铁柱落地页、JoinCard 插槽、工具分类；以及同类主题组件/布局（Home / DocEndCard / EcoIndex / ToolMeta / SEO meta）
- **方法**：对照 `i18n-project/PLAN.md` + `ENGINEERING.md`；仓库扫 `site/docs/.vitepress/theme/*.vue`、`ui.json` / `locales/*/ui.json`、JSON 驱动文案与各语种 md；线上抽查 `https://bot.fmcat.top/en/`、`/en/changelog/`、`/en/tools/`、`/en/ecosystem/xiaotiezhu`、`/en/group`、`/en/part1/01-what-is`、`/ja/changelog/`、`/ko/`、`/es/tools/`（curl HTML，去 script/style 后检索可见简体）
- **结论一句话**：点名 chrome（nav pill / footer / Changelog 筛选与标题 / PartBadge / 小铁柱 h1·hint / JoinCard alt）在**仓库已于当日接入 `ui.json` + `localePath`**，但**线上尚未部署，非 zh 仍满屏简体**；仓库内另余 SEO meta、JSON-LD、友情链接站名等 P1。工程已在修，本清单供验收不漏项。

## 状态说明

| 标记 | 含义 |
|---|---|
| **线上 P0** | 线上非 zh 仍可见简体；仓库源码已修，**部署后必须复扫** |
| **仓库开放** | 当前仓库仍存在缺口 |
| **该区抽查通过** | 仓库 +（若适用）线上文案已走 locale / 插槽译文 |

---

## 点名区域

### 1. 导航 pill（`NavGroupPill.vue`）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| P0 | 顶栏 `nav-bar-content-after` · `NavGroupPill.vue` | `付费答疑群`；链接 `/group`（无语种前缀） | 硬编码（线上）；仓库已改读 `ui.json` → `nav.groupPill` + `localePath('/group')` | **线上 P0** | 部署后抽查 `/en/` 顶栏应为 Paid Q&A Group 等；链接须为 `/en/group` |

### 2. 页脚（`SiteFooter.vue`）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| P0 | 页脚按钮/链 | `公众号「铁柱AGI」`、`付费答疑群`、`关于作者` | 硬编码（线上）；仓库已读 `ui.footer.*` + `localePath` | **线上 P0** | 部署复扫；专名「铁柱AGI」可保留 |
| P0 | 页脚弹层/alt | `公众号「铁柱AGI」二维码`、`微信搜一搜：铁柱AGI` | 同上 | **线上 P0** | 部署复扫 `mpDialog` / `mpAlt` |
| P0 | 页脚说明 | `友情链接`、`本站是社区非官方学习站，非 xAI 官方。` | 同上 | **线上 P0** | 部署复扫 `friends` / `note` |
| P1 | `friends.json` | `噪音之后`、`万象 AI 实验室` | JSON 未走 i18n（站名专有名词） | **仓库开放** | 可保留站名；若要译加 `friends.<locale>.json` 或 ui 覆盖 |

### 3. Changelog 筛选（`Changelog.vue`）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| P0 | 页标题 h1 | `更新日志` | 硬编码（线上）；仓库已 `clUi.title` | **线上 P0** | 部署后 `/en/changelog/` 应为 Changelog |
| P0 | 筛选 tab | `全部`、`移动端`、`我们的解读` | 硬编码（线上）；仓库已 `tabAll`/`tabMobile`/`tabOurs` | **线上 P0** | 部署复扫 sticky tabs |
| P0 | chip | `我们的解读` | 同上 → `chipOurs` | **线上 P0** | 部署复扫 |
| P0 | 日期格式 | `10月28日`、`2026 年 10 月` | 硬编码中文日期（线上）；仓库已 `Intl.DateTimeFormat(bcp47(seg))` | **线上 P0** | 部署后应为 Oct 28 / October 2026 等 |

正文条目：`changelog.json` 各语种覆盖已存在；仓库已把 `items` 改为 `computed`。线上抽查 en 条目标题已为英文（数据层早于 chrome 修复）。

### 4. PartBadge（`PartBadge.vue`）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| P0 | `doc-before` badge 文案 | `第一篇 · 使用手册` 等（简体 label 写死在 skins） | 硬编码 + 路径取 `path[0]`（locale 页不渲染） | **线上**：非 zh 常不显示；**仓库已修** `partKeyFromPath` + `ui.parts.*` | 部署后打开 `/en/part1/01-what-is` 应出现 Part 1 · Handbook，勿再露简体 |

### 5. 小铁柱落地页（`XiaoTiezhuLanding.vue`）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| P0 | Hero h1 | `小铁柱` | 硬编码（线上）；仓库已 `xtUi.title`（en ui 仍为产品名「小铁柱」） | **线上 P0** / 产品名策略 | 部署复扫；若需拉丁化由产品定，非缺译事故 |
| P0 | JoinCard 插槽 hint | `扫码添加管家微信，开通小铁柱` | 硬编码（线上）；仓库已 `xtUi.joinHint` | **线上 P0** | 部署后应为 Scan to add butler WeChat… |
| P1 | `en|ja|ko|es|pt-BR/.../xiaotiezhu.md` frontmatter `title` | `小铁柱` | 缺译（或产品名保留） | **仓库开放（策略）** | 与 ui.xiaotiezhu.title 对齐策略；浏览器标签目前一律简体产品名 |
| — | 其余区块 | slogan/CTA/FAQ 等 | — | **该区抽查通过**（走 `ecosystem.json` locale） | — |

### 6. JoinCard 插槽（`JoinCard.vue` + md）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| — | `group.md` / 各语种 `*/group.md` 默认插槽 | （各语种已译；专名/验证语「小红书」按真源保留） | — | **该区抽查通过** | 保持插槽在 md 侧维护 |
| — | `xhs` 模式文案 | `join_*` / `copy_btn` 等 | — | **该区抽查通过**（`funnel.json` locale） | — |
| P0 | QR `alt` | `铁柱的个人微信二维码` | 硬编码（线上）；仓库已 `ui.join.qrAlt` | **线上 P0** | 部署复扫 |

### 7. 工具分类（`ToolIndex.vue` / `ToolMeta.vue` / `tools.json`）

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| — | 分类 tab / 卡片 cat | 线上 en 已见 `Coding Agents` 等 | — | **该区抽查通过**（`tools.json` locale + `ui.all` 等） | — |
| P1 | `ToolMeta`/`ToolIndex` skin 映射 | 源码内含简体 key（映射表，非直接渲染） | 维护型硬编码 | **仓库开放（低）** | 改按 root `cat` id 或 `rootCatById` 稳定键，避免多语种 label 漂移；线上曾出现 `/bots/undefined.svg`（旧 ToolMeta），仓库已补多语种 skin |

---

## 同类主题 / 布局附加项

| 优先级 | 位置 | 当前简体摘录 | 问题类型 | 状态 | 建议 |
|---|---|---|---|---|---|
| P0 | `Home.vue` 内链 | 线上 en 首页 CTA 仍指向 `/part1/...`、`/group`（无 `/en`）→ 点进整页变中文 | 链接未加 locale（线上）；仓库已全面 `localePath(...)` | **线上 P0** | 部署后点「Start from Chapter 1」须留在 `/en/part1/...` |
| P0 | `DocEndCard.vue` | 线上非 zh 文档页常不出现（旧正则不认 `/en/part…`）；若出现按钮链到 `/group` | 路径未剥 locale（线上）；仓库已 `stripLocalePrefix` + `localePath('/group')` + funnel 文案 | **线上 P0** | 部署后 `/en/part1/02-plans` 文末应出英文 CTA |
| P1 | `Home.vue` `segs()` | 按 `，。；！？` 切句 | 中文标点假设 | **仓库开放** | 扩拉丁标点或按语种分支；不直接露中文 |
| P1 | `.vitepress/seo.json` | 全站 `og:description` / `twitter:description` 仍用简体 `home` 等（线上 en 首页已确认） | JSON 未走 i18n | **仓库开放** | 按语种覆盖或改用各页 frontmatter `description`；`seo.json` 现无 `en/` key |
| P1 | `config.mts` JSON-LD | `inLanguage: 'zh-CN'` 多处写死 | 硬编码 | **仓库开放** | 按页 locale 输出；见 ENGINEERING 已知项 |
| — | `EcoIndex` / `BotHire` / `ClipperLanding` | 主体走 locale JSON | — | **该区抽查通过**（Eco 卡片名「小铁柱」同产品名策略） | Eco 卡片 `pages` 已 `localePath` |
| — | VitePress `themeConfig.nav` / outline / docFooter | 各 locale 已在 `config.mts` 配置 | — | **该区抽查通过** | 语言菜单中的「简体中文」等为语种名，非泄漏 |

---

## 线上 vs 仓库对照（验收必读）

| 现象 | 线上（抽查时） | 仓库（2026-10-29 ~18:03 +08 源码） |
|---|---|---|
| Nav pill / Footer 简体 | 有 | 已接 `ui.json` |
| Changelog 标题/tab/日期中文 | 有 | 已接 `ui.json` + Intl |
| PartBadge | 非 zh 多不显示 | 已修路径 + `ui.parts` |
| 小铁柱 h1 / joinHint | 简体 | 已接 `ui.xiaotiezhu` |
| JoinCard alt | 简体 | 已接 `ui.join.qrAlt` |
| Home / DocEnd / Tool 内链无 locale | 有 | 已 `localePath` / `stripLocalePrefix` |
| 工具分类文案 | en 已英文 | 通过 |
| JoinCard group 插槽 | 各语种已译 | 通过 |
| SEO og:description 简体 | 有 | **仍有** |
| friends 站名简体 | 有 | **仍有** |

**部署后验收口令**：打开 `/en/`、`/en/changelog/`、`/en/ecosystem/xiaotiezhu`、`/en/part1/01-what-is`、`/ja/changelog/`，确认顶栏 pill、页脚、Changelog tabs、PartBadge、小铁柱 hint 无简体；Home CTA 不掉回根站中文。

---

## 按区域汇总

| 区域 | P0（含线上待部署） | P1 | 抽查通过 |
|---|---:|---:|---|
| 导航 pill | 1 | 0 | — |
| 页脚 | 3 | 1 | — |
| Changelog 筛选/标题/日期 | 4 | 0 | 正文数据层 |
| PartBadge | 1 | 0 | — |
| 小铁柱落地页 | 2 | 1 | 其余区块 |
| JoinCard | 1 | 0 | 插槽 / xhs / funnel |
| 工具分类 | 0 | 1 | 分类文案 |
| Home / DocEnd / SEO / 其它 | 2 | 3 | Eco/BotHire/Clipper/nav config |
| **合计（条目）** | **14** | **6** | 见上 |

说明：14 条 P0 中 **12 条为「线上仍见、仓库已修」**，**0 条点名 chrome 在仓库仍硬编码**；**2 条**（Home 掉语种、DocEnd 路径）同属待部署。仓库真正仍开放的以 **6 条 P1** 为主（SEO、JSON-LD、friends、segs、skin 映射、小铁柱 title 策略）。

### Top 5 最刺眼缺口（按读者体感）

1. **顶栏 pill「付费答疑群」**（全站非 zh 首屏）— 线上 P0，仓库已修待部署  
2. **页脚整组简体**（公众号 / 付费答疑群 / 关于作者 / 非官方声明）— 线上 P0，仓库已修待部署  
3. **Changelog「更新日志」+「全部/移动端/我们的解读」+「×月×日」** — 线上 P0，仓库已修待部署  
4. **小铁柱页 hint「扫码添加管家微信，开通小铁柱」**（及 h1）— 线上 P0，仓库已修待部署  
5. **SEO `og:description` 全语种仍简体**（分享卡片）— **仓库仍开放 P1**；叠加 Home CTA 无 locale 时一点就回中文站（线上 P0，仓库已修）

---

## 备注

- 工程与翻译官已在修硬编码；`theme/ui.json` + `theme/locales/*/ui.json` 六语种 key 已齐，组件接线落在 `NavGroupPill` / `SiteFooter` / `PartBadge` / `Changelog` / `XiaoTiezhuLanding` / `JoinCard` 等。  
- **本清单供验收**：部署后按「线上 vs 仓库」表复扫；未部署前勿关闭 P0。  
- 禁止项遵守：本文件只列问题，未改源码、未译正文、未动 locales 脚手架内容（只新增本审计 md）。
