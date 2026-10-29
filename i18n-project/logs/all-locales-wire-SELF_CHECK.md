# 六语种接线自检（2026-10-29）

## build
- `cd site && npm run build`：**PASS**（vitepress 1.6.4，约 26.2s，无 RangeError）
- 未执行 push / deploy

## locales 结构
| locale | md | UI JSON | sidebar JSON | nav/sidebar 非空 |
|---|---|---|---|---|
| zh-CN (root) | 真源 | theme/*.json | sidebar.json | 是 |
| zh-Hant | 61 | 6 | sidebar.zh-Hant.json | 是 |
| en | 61 | 6 | sidebar.en.json | 是 |
| ja | 61 | 6 | sidebar.ja.json | 是 |
| ko | 61 | 6 | sidebar.ko.json | 是 |
| es | 61 | 6 | sidebar.es.json | 是 |
| pt-BR | 61 | 6 | sidebar.pt-BR.json | 是 |

## 语言切换
- VitePress 内建 locales 下拉（顶栏 / 移动菜单）
- config.mts `locales` 含 root + 上述 6 语种

## JSON 接线
- `theme/i18n.ts`：`useLocaleJson` 按 `theme/locales/<locale>/*.json` 整文件覆盖
- 已接入：Home / BotHire / Changelog / EcoIndex / ClipperLanding / XiaoTiezhuLanding / ToolIndex / ToolMeta / JoinCard / DocEndCard

## 抽检注意
- **en/part1 部分标题混入日文**（如 `01-what-is.md`、`03-install.md` 含「とは」）——内容问题，交翻译官修；侧栏目前按页标题取文案会带出该瑕疵
- `git stash@{0}: seo-temp` 仍在，未 drop

## 待部署清单（等铁柱策略后再动）
1. 确认上线策略：七语种全开 / 先繁英日 / 先只繁体（若只开部分，部署前从 `locales` 与切换器隐藏未开放语种）
2. 保留 `stash@{0}: seo-temp`，合并/应用策略由总控定
3. `cd site && npm run build` 再跑一遍
4. 按仓库 `deploy.sh` 发布（Cloudflare Pages + EdgeOne bot.fmcat.top）
5. 抽检：每开放语种首页、一篇手册、一篇工具、语言切换、hreflang/og:locale
6. **本岗不自行 push/deploy**，等 Bot学习站指令
