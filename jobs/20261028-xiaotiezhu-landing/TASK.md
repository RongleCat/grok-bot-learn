You are a heavy-job worker. job-id = 20261028-xiaotiezhu-landing. This is a JUDGMENT task: think carefully, verify facts against sources, cite URLs for every claim, and prefer saying 'not found' over guessing.

Hard rules:
- First run `bash scripts/setup.sh` (installs ffmpeg/yt-dlp/faster-whisper/python data libs; idempotent).
- Write the task verbatim to jobs/20261028-xiaotiezhu-landing/TASK.md.
- Put every output in `outputs/20261028-xiaotiezhu-landing/`. Single file <= 50MB; never commit video/audio files (list source URLs in LINKS.md instead).
- You must write `outputs/20261028-xiaotiezhu-landing/SELF_CHECK.md`: copy every item of the task's「验收标准」section, and for EACH item write
  PASS or FAIL + concrete evidence (file name, count, sample line, command output). No item may be skipped.
- You must write `outputs/20261028-xiaotiezhu-landing/RESULT.txt` (1-2 lines, Chinese). Line 1 MUST start with `SUCCESS:` only if every
  acceptance item is PASS; otherwise start with `FAILED:` and name the failing items / reason.
- Also write `outputs/20261028-xiaotiezhu-landing/METRICS.json`: {"steps": {"<step>": seconds}, "notes": "..."}.
- When done (success OR failure), git add/commit/push the current branch (never push to main). No PR needed.
- Never put keys/tokens/cookies into files or commits. Never use the X (Twitter) official API; X content only via fxtwitter (api.fxtwitter.com) or public web pages.
- Do not write article bodies; only collect material / process data.
- Translation/summarization: do it yourself as the model; do not call external translation APIs or sign up for services.
- If yt-dlp gets 403 on a direct file URL, fall back to curl with a browser User-Agent.

Task:
# Task: 学习站「小铁柱」周边生态落地页

- job-id: 20261028-xiaotiezhu-landing
- Requester: Bot学习站
- Type: judgment
- Input repo: https://github.com/RongleCat/grok-bot-learn （VitePress，docs 在 `site/docs`，主题在 `site/docs/.vitepress/theme`）
- 起点：当前 main（已含素材与文案 commit `f0ede16`）
- Output：全部放在 `outputs/20261028-xiaotiezhu-landing/`
  - SELF_CHECK.md（逐条对照验收标准，PASS/FAIL + 证据）
  - CHANGED_FILES.md
  - 可应用的完整改动已 push 到本任务分支（不要直接推 main）

## 背景
铁柱要求在「周边生态」里与 Grok Bot Clipper **同级**增加「小铁柱」卡片入口，并做落地页，包装成付费服务。文案与图片已入库，禁止改写读者文案措辞与价格数字。

已入库（勿改文件内容，只引用）：
- 文案：`site/docs/.vitepress/theme/ecosystem.json` 的 `index.items` 第二项「小铁柱」与顶层键 `xiaotiezhu`
- 链接：`site/docs/.vitepress/theme/links.json` 的 `xiaotiezhuSample`、`xiaotiezhuWechat`
- 图片（public）：
  - `/ecosystem/xiaotiezhu-banner.webp`（生态卡片封面）
  - `/ecosystem/xiaotiezhu-avatar.webp`（头像）
  - `/ecosystem/xiaotiezhu-digest-page.webp`（群聊网页总结截图）
  - `/ecosystem/xiaotiezhu-vip-preview.webp` / `xiaotiezhu-vip-card.webp`（VIP 群总结卡）
  - `/ecosystem/xiaotiezhu-xiaowan-preview.webp` / `xiaotiezhu-xiaowan-card.webp`（小晚群总结卡）

参考实现：`ClipperLanding.vue` + `EcoIndex.vue` + `ecosystem/grok-bot-clipper.md`。整体视觉对齐现有站（圆角卡片、GrokOrb 点缀、深浅色变量、移动端单列）。页面禁止输出代码注释、多余解释性标签文字；只放网页展示内容。非官方声明保留。域名对外用 https://bot.fmcat.top。

## 目标
1. 新落地页路由 `/ecosystem/xiaotiezhu`
2. 周边生态索引卡片可点进该页（与 Clipper 并排）
3. 落地页含：英雄区（头像+口号+CTA）、功能区（带样例图）、定价区、附加项、开通步骤、FAQ、底部 CTA（微信咨询）

## 实现要求

### A. EcoIndex.vue
- 不要硬编码单页：从 `ecosystem.json` 的 `index.pages` / `index.covers`（已写好）读取；若缺失则按 items 顺序回退。
- 两卡网格已支持；确认第二卡封面与链接正确。

### B. 新建 `XiaoTiezhuLanding.vue`
- 注册到 `theme/index.ts`（与 ClipperLanding 同级）
- 文案全部来自 `copy.xiaotiezhu`（`ecosystem.json`），用现有 `rich` / `tidy`
- 结构建议（可微调，勿丢区块）：
  1. Hero：头像 `xiaotiezhu-avatar.webp`、meta、h1「小铁柱」、slogan、lead、主按钮（`links.xiaotiezhuWechat` → 站内 `/group`，用 withBase）、次按钮（`links.xiaotiezhuSample` 外链新标签）、unofficial
  2. Features：遍历 `features`；`shot` 映射：
     - `digest-page` → `xiaotiezhu-digest-page.webp`
     - `vip-card` → `xiaotiezhu-vip-preview.webp`（可点开看 `xiaotiezhu-vip-card.webp` 或直接展示 preview）
     - `xiaowan-card` → `xiaotiezhu-xiaowan-preview.webp`
     - `none` → 可用 GrokOrb 装饰，无图
     布局参考 ClipperLanding 的 feature 左右交错；图加圆角边框，深色模式可读
  3. Pricing：`plans` 两卡展示价格大字 + note；`addons` 列表；`themeNote` 单独一行提示
  4. Extras：四宫格/列表
  5. Steps：三步
  6. FAQ：与 Clipper 类似折叠或列表
  7. End：标题+文案+主按钮到 `/group`；可嵌 `<JoinCard from="xiaotiezhu" />` 或指向 `/group`（优先清晰的加微信 CTA）
- CSS：scoped，复用站内变量（`--vp-c-*`、`--tz-*`），适配 `.dark`，移动端单列
- 跟踪：主 CTA 可 `track('xiaotiezhu-cta', { from })`（若 track API 允许）

### C. 页面与导航
- 新建 `site/docs/ecosystem/xiaotiezhu.md`：`layout: page`、`sidebar: false`、`title: 小铁柱`，正文仅 `<XiaoTiezhuLanding />`
- `config.mts`：若有周边生态 sitemap / llms / JSON-LD 列表，把小铁柱页加进去（对照 clipper 那段）；nav 已是「周边生态」父级即可

### D. 构建
- 在 `site/` 执行项目既有 build（通常 `npm run build`）必须通过
- 不要提交 `node_modules`、`dist`、密钥

## 禁止
- 改写 `ecosystem.json` 里读者可见句子与价格（79 / 59 / +20 / 100）
- 照抄 grokguide.si
- 在页面放「AI 生成」「内部路径」等字样
- 直接 push main（只推任务分支）

## 验收标准
- `outputs/20261028-xiaotiezhu-landing/SELF_CHECK.md` 存在，下列每条 PASS 并附证据
- 存在 `site/docs/ecosystem/xiaotiezhu.md` 且渲染 `<XiaoTiezhuLanding />`
- `theme/index.ts` 已注册 `XiaoTiezhuLanding`
- `EcoIndex` 第二张卡链接到 `/ecosystem/xiaotiezhu`，封面为 `xiaotiezhu-banner.webp`
- 落地页可见区块：英雄、功能（含至少 digest-page 与一张总结卡图）、定价（79 与 59）、+20 附加、主题 100 元说明、步骤、FAQ、底部 CTA
- `npm run build`（在 site/）成功，摘要写入 SELF_CHECK
- CHANGED_FILES.md 列出全部改动路径；改动已在任务分支
- 未改价格数字与已入库文案关键句；未提交密钥

## Notes
- 定价文案以 JSON 为准；UI 可用「¥79」展示，但数字必须是 79/59/20/100
- 样例图很长：功能区用 preview；可用 `loading="lazy"`
- 本任务不负责线上 deploy（请求方合并后部署）
