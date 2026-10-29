# 学习站多语言工程 · 翻译官接入手册

## 目录约定

```
site/docs/
├── index.md                  ← zh-CN 根站首页（真源）
├── part1/ part2/ part3/ part4/ cases/ tools/ bots/ ecosystem/ changelog/
│                             ← 简体中文正文（真源，不动）
├── en/                       ← English
│   └── index.md              ← 占位首页，翻译官在此目录下补充译文
├── zh-Hant/                  ← 繁體中文
├── ja/                       ← 日本語
├── ko/                       ← 한국어
├── es/                       ← Español
└── pt-BR/                    ← Português (Brasil)
```

每个非 root 语种目录复刻与根站相同的子目录结构。例如英文版第 1 章：
```
site/docs/en/part1/01-what-is.md
```

**禁止**把 61 篇简体正文整库复制到各语种。翻译官按页翻译，一篇 ready 放一篇。

## 翻译官接入步骤

1. 在 `site/docs/<locale>/` 下新建与根站同路径的 `.md` 文件。
2. 如果该页需要 sidebar，在 `config.mts` 对应 locale 的 `themeConfig.sidebar` 中加入条目（加语种前缀）。**zh-Hant 已接好**：`sidebar.zh-Hant.json` + `config.mts` 中 `sidebarZhHant` / 完整 nav；其他语种仍多为占位空 sidebar，译文齐后再接。
3. 构建验证：`cd site && npm run build`。
4. `npm run dev` 打开 `http://localhost:5173/<locale>/` 预览。

## JSON 驱动页的多语言规则

### 同结构分文件（推荐）

在 `site/docs/.vitepress/theme/locales/<locale>/` 放与 root JSON 同名文件。只需包含要覆盖的字段：

```
theme/locales/en/home.json      ← 覆盖 theme/home.json 的英文字段
theme/locales/ja/tools.json     ← 覆盖 theme/tools.json 的日文字段
```

组件使用 `useLocaleJson(rootData, 'home.json')` 获取合并后的数据（缺译回退简体）。

### 组件接入示例

```ts
// 原来的 import
import copy from './home.json'

// 改为 locale 感知
import rootCopy from './home.json'
import { useLocaleJson } from './i18n'
const copy = useLocaleJson(rootCopy, 'home.json')
// 模板中用 copy.value.title（注意 .value，因为返回的是 ComputedRef）
```

### JSON 文件命名

| root 文件 | locale 覆盖路径 |
|---|---|
| `theme/home.json` | `theme/locales/<locale>/home.json` |
| `theme/tools.json` | `theme/locales/<locale>/tools.json` |
| `theme/bots.json` | `theme/locales/<locale>/bots.json` |
| `theme/ecosystem.json` | `theme/locales/<locale>/ecosystem.json` |
| `theme/changelog.json` | `theme/locales/<locale>/changelog.json` |
| `theme/funnel.json` | `theme/locales/<locale>/funnel.json` |
| `.vitepress/seo.json` | 暂无 locale 覆盖机制，SEO 描述按语种写在各页 frontmatter `description` |
| `.vitepress/sidebar.json` | 各语种 sidebar 通过 `config.mts` 的 `locales.<key>.themeConfig.sidebar` 配置 |

## 禁止翻译的内容

- 产品名：Grok Bot、Grok、xAI、Cursor、SuperGrok、Hermes
- 人名：铁柱AGI
- URL / 域名 / 仓库地址
- 代码块 / shell 命令
- 非官方声明原文：「本站是社区非官方学习站，非 xAI 官方。」（各语种需保持同等含义）

## hreflang / og:locale 行为

每个页面的 `<head>` 包含：
- `<link rel="alternate" hreflang="zh-Hans" href="https://bot.fmcat.top/..." />`（根站）
- `<link rel="alternate" hreflang="en" href="https://bot.fmcat.top/en/..." />`
- 同理 `zh-Hant`、`ja`、`ko`、`es`、`pt-BR`
- `<link rel="alternate" hreflang="x-default" href="https://bot.fmcat.top/..." />`（指向根站对等页）
- `<meta property="og:locale" content="<当前语种 og 格式>" />`
- `<meta property="og:locale:alternate" content="..." />`（其余 6 种）

### og:locale 映射

| 语种 | og:locale |
|---|---|
| zh-CN | zh_CN |
| zh-Hant | zh_TW |
| en | en_US |
| ja | ja_JP |
| ko | ko_KR |
| es | es_ES |
| pt-BR | pt_BR |

## 语言切换

VitePress 内建 locales 下拉（`VPNavBarTranslations`）。

- **桌面（≥960px）**：右上角与主题切换（appearance）并排显示；主题自定义 CSS 把默认 ≥1280px 的可见阈值下调到 ≥960px，与 appearance 对齐。
- **平板过渡（960–1279px）**：顶栏直接显示语言/主题切换；`VPNavBarExtra` 内的重复 translations / appearance 项隐藏。
- **移动端（<960px）**：顶栏不单独露出语言切换，改在汉堡菜单内的 Translations 选择语种。

切换时替换当前路径的语种前缀。如果目标语种无对等页，浏览器显示 404。

## llms.txt / llms-full.txt

`buildEnd` 只索引根站（zh-CN）正文。多语言 llms.txt 暂不分语种生成。如需分语种索引，在 `buildEnd` 内按 locale 前缀过滤 `cfg.pages` 再单独生成。

## 构建与部署

```bash
cd site
npm run build        # 产物在 docs/.vitepress/dist/
npm run preview      # 本地预览 http://localhost:5173
```

build 产物路径不变（`docs/.vitepress/dist/`），非 root 语种页面在 `dist/en/`、`dist/ja/` 等子目录。`deploy.sh` 无需修改。

## 本地预览各语种

```bash
cd site && npm run dev
# 根站：http://localhost:5173/
# 英文：http://localhost:5173/en/
# 日文：http://localhost:5173/ja/
# 韩文：http://localhost:5173/ko/
# 西文：http://localhost:5173/es/
# 巴葡：http://localhost:5173/pt-BR/
# 繁中：http://localhost:5173/zh-Hant/
```

## JSON-LD inLanguage

当前 JSON-LD schema 的 `inLanguage` 字段硬编码为 `'zh-CN'`。翻译官补充正文后，需按页面实际语种更新（可在后续阶段统一处理）。

## 六语种接线状态（2026-10-29）

- 全部非 root 语种（zh-Hant/en/ja/ko/es/pt-BR）已有完整 `sidebar.<locale>.json` + `config.mts` nav/sidebar。
- 主题 JSON 经 `useLocaleJson` 读取 `theme/locales/<locale>/`。
- 语言切换：桌面右上角与主题切换并排（≥960px）；移动端在汉堡菜单。
- **未 push / 未 deploy**；上线策略由铁柱选定后执行。见 `logs/all-locales-wire-SELF_CHECK.md`。
