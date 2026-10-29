# i18n 翻译脚本（草稿）

**未收到「审查完成、可以开译」前不要对站点正式目录写入，也不要跑正式全量。**

| 脚本 | 用途 |
|---|---|
| `opencc_zh_hant_batch.py` | 简体 → zh-Hant（OpenCC s2twp），保护代码块与 DO_NOT_TRANSLATE |
| `agy_translate_one.sh` | 单篇 agy（`gemini-3.8-flash-high`） |
| `agy_translate_batch.sh` | 按 TSV 批量调单篇 |

产出一律：`i18n-project/locales/<locale>/…`（相对 `site/docs/` 的路径）。

试跑：`AGY_DRY=1 ./agy_translate_one.sh en about.md`
