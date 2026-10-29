# 翻译进度

- 更新时间：2026-10-29 19:12 (Asia/Singapore)
- 状态：**UI locale key 巡检有实质改动**（补 zh-Hant changelog 两条官方更新；未 push/deploy）

| 语种 | 正文 SOURCE_PAGES | UI JSON (home/funnel/ui 等) | chrome ui.json | changelog official |
|---|---|---|---|---|
| zh-Hant | 61/61 | 齐 | 已润色 | **本轮补 ios-1.19.0 / pc-0.78.1** |
| en | 61/61 | 齐 | 已润色 | 齐（79） |
| ja | 61/61 | 齐 | 已润色 | 齐（79） |
| ko | 61/61 | 齐 | 已润色 | 齐（79） |
| es | 61/61 | 齐 | 已润色 | 齐（79） |
| pt-BR | 61/61 | 齐 | 已润色 | 齐（79） |

## 本轮巡检（routine 学习站 UI locale key 巡检）
- 对比 root：`home.json` / `funnel.json` / `ui.json` / `ecosystem.json` / `tools.json` / `bots.json` / `changelog.json`；六语种覆盖文件
- home/funnel/ui/ecosystem/bots：六语种 **无缺 key**；friends.json / links.json 无 locale 文件（友链品牌名 + URL，SiteFooter/Clipper 直接 import，属预期）
- JoinCard / NavGroupPill / SiteFooter：已用 `useLocaleJson`，无硬编码「付费答疑群」
- group.md 六语种抽检：**PASS**（无简体短语残留；专名 铁柱AGI / 小红书 / AI_Tiezhu 保留；付费语义 付費/Paid/有料/유료/pago 齐全）
- **缺口修复**：`theme/locales/zh-Hant/changelog.json` 缺工程今日新增 `ios-1.19.0`、`pc-0.78.1`（因 whole-file 覆盖，繁中页原先看不到这两条）。OpenCC s2twp 从 root 补译并前置；`updated` → 2026-10-29；专名 Shop Pay / Bot / Grok Bot 保留

### 抽检 PASS
- zh-Hant changelog ios-1.19.0 title「日常問題修復與體驗最佳化」；points 含「修復／應用／體驗」繁体
- zh-Hant changelog pc-0.78.1 title「新增購物卡片與訂閱管理」；points 含「支援／追蹤／訂閱」；Shop Pay 未改
- en/ja/ko/es/pt-BR group.md + ui.nav.groupPill / funnel.join_title：付费语义齐全

## 产出路径
- 改动文件：`site/docs/.vitepress/theme/locales/zh-Hant/changelog.json`
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻译进度

- 更新时间：2026-10-29 03:48 (America/Los_Angeles)
- 状态：**UI locale key 巡检有实质改动**（补译 ko ecosystem FAQ 题干；未 push/deploy）

| 语种 | 正文 SOURCE_PAGES | UI JSON (home/funnel 等) | chrome ui.json |
|---|---|---|---|
| zh-Hant | 61/61 | 齐 | 已润色 |
| en | 61/61 | 齐 | 已润色 |
| ja | 61/61 | 齐 | 已润色 |
| ko | 61/61 | **本轮补 FAQ.q** | 已润色 |
| es | 61/61 | 齐 | 已润色 |
| pt-BR | 61/61 | 齐 | 已润色 |

## 本轮巡检（routine 学习站 UI locale key 巡检）
- home/funnel/ui：六语种 **无缺 key**；付费答疑群 chrome 已抽出且含 paid/付費/有料/유료/pago
- JoinCard / NavGroupPill / SiteFooter：已用 useLocaleJson，无新增硬编码「付费答疑群」
- group.md 六语种抽检：**PASS**（无简体残留；专名 铁柱AGI / 小红书 保留）
- **缺口修复**：`theme/locales/ko/ecosystem.json` 中 clipper+xiaotiezhu 共 11 条 FAQ **题干**此前仍为简体（答案已是韩语），agy gemini-3.8-flash-high 补译

### 抽检 PASS
- ko funnel join_title / ui.nav.groupPill 含「유료」
- ko ecosystem FAQ.q 不再等于 zh-CN
- en/ja/es/pt-BR/zh-Hant group.md：无简体短语残留

## 产出路径
- 改动文件：`site/docs/.vitepress/theme/locales/ko/ecosystem.json`
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻译进度

- 更新时间：2026-10-29 03:10 (America/Los_Angeles)
- 状态：**ui.json chrome 已润色完成**（agy / OpenCC；未 push/deploy）

| 语种 | 正文 SOURCE_PAGES | UI JSON (home/funnel 等) | chrome ui.json |
|---|---|---|---|
| zh-Hant | 61/61 | 齐 | **已润色**（OpenCC + 专名回写） |
| en | 61/61 | 齐 | **已润色**（agy） |
| ja | 61/61 | 齐 | **已润色**（agy + 专名） |
| ko | 61/61 | 齐 | **已润色**（agy + 专名） |
| es | 61/61 | 齐 | **已润色**（agy） |
| pt-BR | 61/61 | 齐 | **已润色**（agy） |

## 本轮完成
- 工程抽出 `theme/ui.json` 后，六语种 `theme/locales/*/ui.json` 全 key 润色
- 专名强制：铁柱AGI / 小铁柱（禁止 鐵/鉄/철주/소철주）
- nav.groupPill / footer.group 均含付费语义（付費/Paid/有料/유료/pago）
- group.md 六语种抽检 **PASS**
- 详志：`i18n-project/logs/ui-json-polish-STATUS.md`

## 产出路径
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`
- chrome：`site/docs/.vitepress/theme/locales/<locale>/ui.json`

