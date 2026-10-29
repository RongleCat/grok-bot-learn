# stash@{0}: seo-temp 处理说明

- **时间**：2026-10-29（Asia/Singapore）
- **stash 名**：`On main: seo-temp`
- **内容**：仅改 `site/docs/.vitepress/config.mts`（+139/-3），为早期 i18n 骨架：`I18N_*` 辅助函数、`sidebar.zh-Hant` 导入、locales 七语种占位（他语种 sidebar 多为空/初期）。
- **核对**：`git stash show -p stash@{0} --stat`；与当前工作区 `config.mts` 对比后，stash 内所有实质改动均已被当前完整七语种 + hreflang/og:locale 接线覆盖，**无独有有用片段**。
- **处理**：确认无独有有用改动后执行 `git stash drop stash@{0}`。
- **结论**：可安全丢弃；不要从该 stash 回滚覆盖当前工作区。
