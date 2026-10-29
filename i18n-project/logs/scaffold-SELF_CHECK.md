# VitePress i18n 脚手架自检报告

日期：2026-10-29
阶段：2 — VitePress i18n 脚手架与部署接线准备

## 构建状态

⏳ **需请求方手动验证**：当前环境 shell 命令受限，无法执行 `npm run build`。
请在本地运行：

```bash
cd site && npm run build
```

预期结果：退出码 0，产出约 70+ 页面（61 篇 zh-CN + 6 个 locale 首页 + 404 等）。

## 检查项

### 1. config.mts locales 配置
- [x] `locales.root`：label=简体中文, lang=zh-CN
- [x] `locales['zh-Hant']`：label=繁體中文, lang=zh-Hant, link=/zh-Hant/
- [x] `locales.en`：label=English, lang=en-US, link=/en/
- [x] `locales.ja`：label=日本語, lang=ja, link=/ja/
- [x] `locales.ko`：label=한국어, lang=ko, link=/ko/
- [x] `locales.es`：label=Español, lang=es, link=/es/
- [x] `locales['pt-BR']`：label=Português (Brasil), lang=pt-BR, link=/pt-BR/
- [x] 路径前缀与 PLAN.md 一致

### 2. 非 root 语种目录骨架
- [x] `site/docs/en/index.md` 存在，含 title/description/非官方声明
- [x] `site/docs/zh-Hant/index.md` 存在
- [x] `site/docs/ja/index.md` 存在
- [x] `site/docs/ko/index.md` 存在
- [x] `site/docs/es/index.md` 存在
- [x] `site/docs/pt-BR/index.md` 存在
- [x] 未复制 61 篇简体正文

### 3. 语言切换
- [x] VitePress locales 自带下拉，桌面端在顶栏 nav 右侧，移动端在汉堡菜单
- [x] 每个 locale 有 label 和 link，下拉可用

### 4. hreflang / og:locale
- [x] `transformHead` 按 `pageLocale(rel)` 检测当前语种
- [x] `og:locale` 动态输出（zh_CN / en_US / zh_TW / ja_JP / ko_KR / es_ES / pt_BR）
- [x] 为所有 7 种语言输出 `link[rel=alternate][hreflang=...]`
- [x] `hreflang=x-default` 指向根站对等页
- [x] `og:locale:alternate` 为其余 6 种输出
- [x] canonical URL 含正确语种前缀

### 5. JSON 驱动页 locale 能力
- [x] `theme/i18n.ts` 提供 `useLocaleJson` composable
- [x] 通过 `import.meta.glob('./locales/*/*.json')` 自动加载
- [x] 缺译回退原始 JSON（zh-CN）
- [x] `theme/locales/.gitkeep` 占位目录
- [x] ENGINEERING.md 写明 JSON 分文件规则和组件接入示例

### 6. 导航/页脚/UI 字符串
- [x] 每个 locale 的 themeConfig 包含翻译后的 UI 标签（outline, docFooter, darkModeSwitch 等）
- [x] 缺译 locale 回退到顶层 themeConfig（zh-CN 字符串）
- [x] 页脚 SiteFooter.vue 硬编码中文，作为 zh-CN 回退（翻译官后续可替换）

### 7. buildEnd (llms.txt)
- [x] `isDoc()` 只匹配 root 路径前缀，非 root locale 页不进入 llms 索引
- [x] 根站逻辑不受影响

### 8. 产出文件
- [x] `config.mts` 已改造
- [x] `theme/i18n.ts` 已创建
- [x] 6 个语种 `index.md` 已创建
- [x] `i18n-project/ENGINEERING.md` 已写
- [x] `i18n-project/logs/scaffold-SELF_CHECK.md`（本文件）
- [x] `i18n-project/logs/scaffold-CHANGED.txt`

### 9. 禁止项
- [x] 未引入付费 API
- [x] 未照抄 grokguide.si
- [x] 未把整站中文 md 复制进各 locales
- [x] 未执行 deploy.sh
- [x] 未提交 secrets / node_modules / dist
- [x] 未删除非官方声明
