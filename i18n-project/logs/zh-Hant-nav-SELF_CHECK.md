# zh-Hant nav/sidebar 接线自检

- 时间：2026-10-29 09:35 Asia/Singapore
- `npm run build`（site/）：PASS，约 11.30s，vitepress 1.6.4
- `sidebar.zh-Hant.json`：与 root 同结构，链接均带 `/zh-Hant` 前缀，文案 s2twp
- `config.mts`：`zh-Hant.themeConfig.nav` 对齐简体（教程/案例庫/Bot 直聘/周邊生態/工具箱/更新日誌/付費答疑群）；`sidebar: sidebarZhHant`（非空）
- dist 含 `/zh-Hant/`、`/zh-Hant/part1/`、`/zh-Hant/tools/` 等产物
- 其他语种：仍占位空 sidebar（按总控要求可先不动）
