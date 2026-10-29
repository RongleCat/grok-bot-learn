# go-live SELF_CHECK（本地，未 deploy）

- **时间**：2026-10-29 17:06 Asia/Singapore
- **仓库**：`/workspace/grok-bot-learn`（branch `main`）
- **站点**：https://bot.fmcat.top（本次未部署）

## 验收项

| # | 项 | 结果 | 证据 |
|---|---|---|---|
| 1 | CSS 切换器规则（≥960px 显示 VPNavBarTranslations / translations） | **PASS** | `site/docs/.vitepress/theme/style.css` L1017–1032：`@media (min-width: 960px)` 对 `.VPNavBar .content-body > .VPNavBarAppearance/.VPNavBarTranslations/.translations` 设 `display:flex !important`；960–1279 隐藏 `.VPNavBarExtra .group.translations` 与 `.item.appearance`。产物 `site/docs/.vitepress/dist/assets/style.CK8Kwh2Y.css` 含同规则（minify）。 |
| 2 | locales 七语种全开 | **PASS** | `config.mts` `locales`：`root`（简体中文/zh-CN）、`zh-Hant`（/zh-Hant/）、`en`（/en/）、`ja`（/ja/）、`ko`（/ko/）、`es`（/es/）、`pt-BR`（/pt-BR/）；均有 label，非 root 均有 link。 |
| 3 | stash@{0} seo-temp | **PASS** | 已核对 `git stash show -p --stat`：仅旧版 `config.mts` 骨架，已被当前七语种+hreflang 覆盖、无独有有用改动。说明见 `i18n-project/logs/stash-seo-temp-NOTE.md`；已 `git stash drop stash@{0}`（原对象 `0ae8bf3f801eb5eebfb9c125d353b6878eaaebd1`）。当前 `git stash list` 为空。 |
| 4 | build | **PASS** | `cd site && npm run build` 退出码 0；`build complete in 36.47s`；dist HTML **428** 页。 |
| 5 | commit | **PASS** | `0ae8bf3f801eb5eebfb9c125d353b6878eaaebd1`（short `2c39f16`）；message: `feat(i18n): 七语种全开、顶栏语言切换与主题并排`；author 学习站多语言工程 <i18n@bot.fmcat.top>。本地 ahead 1，未 push。 |
| 6 | dist hreflang / og:locale 抽检 | **PASS** | 见下节。 |
| 7 | 未 push / 未 deploy | **PASS** | 按任务要求未执行 `deploy.sh`、未 `git push`；等铁柱确认上线。 |

## dist 抽检片段

### `dist/index.html`（首页 zh-CN）
- `og:locale` = `zh_CN`
- hreflang：zh-Hans / zh-Hant / en / ja / ko / es / pt-BR / **x-default** → `https://bot.fmcat.top/`

```html
<meta property="og:locale" content="zh_CN">
<link rel="alternate" hreflang="zh-Hans" href="https://bot.fmcat.top/">
<link rel="alternate" hreflang="en" href="https://bot.fmcat.top/en/">
<link rel="alternate" hreflang="x-default" href="https://bot.fmcat.top/">
```

### `dist/en/index.html`
- `og:locale` = `en_US`
- 8 条 hreflang（含 x-default → 根站）

### `dist/en/part1/01-what-is.html`（手册）
- `og:locale` = `en_US`
- `hreflang="en" href="https://bot.fmcat.top/en/part1/01-what-is"`
- `hreflang="x-default" href="https://bot.fmcat.top/part1/01-what-is"`

### `dist/tools/index.html`（工具）
- `og:locale` = `zh_CN`
- `hreflang` 含七语种 + x-default → `https://bot.fmcat.top/tools/`

### `dist/part1/01-what-is.html`（根站手册）
- 同上结构，og:locale=`zh_CN`

## Commit

- **hash**：`0ae8bf3f801eb5eebfb9c125d353b6878eaaebd1`
- **short**：`0ae8bf3`
- **message**：`feat(i18n): 七语种全开、顶栏语言切换与主题并排`
- **author**：学习站多语言工程 <i18n@bot.fmcat.top>

## ENGINEERING

「语言切换」一节已更新：桌面 ≥960px 右上角与主题并排；移动端汉堡菜单。

## 未部署原因

任务明确：**不要 push，不要执行 deploy.sh**；部署由主代理等铁柱确认后再跑。
