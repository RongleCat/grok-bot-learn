# SELF_CHECK

job-id: 20261028-xiaotiezhu-landing
分支: `cursor/heavy-job-20261028-xiaotiezhu-landing-5ae6`
起点: `f0ede16`

## 验收标准

### `outputs/20261028-xiaotiezhu-landing/SELF_CHECK.md` 存在，下列每条 PASS 并附证据

PASS. 本文件即该路径。下列 7 条均有 PASS 与命令或文件证据。

### 存在 `site/docs/ecosystem/xiaotiezhu.md` 且渲染 `<XiaoTiezhuLanding />`

PASS. 文件正文：

```
layout: page
sidebar: false
title: 小铁柱
<XiaoTiezhuLanding />
```

构建产物 `site/docs/.vitepress/dist/ecosystem/xiaotiezhu.html` 含组件根节点 `class="xt"`，可见标题「小铁柱」。`sitemap.xml` 含 `https://bot.fmcat.top/ecosystem/xiaotiezhu`。

### `theme/index.ts` 已注册 `XiaoTiezhuLanding`

PASS. `site/docs/.vitepress/theme/index.ts`：

```
import XiaoTiezhuLanding from './XiaoTiezhuLanding.vue'
app.component('XiaoTiezhuLanding', XiaoTiezhuLanding)
```

与 `ClipperLanding` 同级注册。

### `EcoIndex` 第二张卡链接到 `/ecosystem/xiaotiezhu`，封面为 `xiaotiezhu-banner.webp`

PASS. `EcoIndex.vue` 从 `ecosystem.json` 的 `index.pages` / `index.covers` 按 items 下标读取；数组缺失时按 items 顺序回退到 `/ecosystem/` 与空封面。

构建后的 `ecosystem/index.html` 两张卡：

```
/ecosystem/grok-bot-clipper /ecosystem/clipper-banner.webp Grok Bot Clipper
/ecosystem/xiaotiezhu /ecosystem/xiaotiezhu-banner.webp 小铁柱
```

浏览器点击第二张卡落到 `http://127.0.0.1:5173/ecosystem/xiaotiezhu`。JSON-LD ItemList 第二项 url 为 `https://bot.fmcat.top/ecosystem/xiaotiezhu`。

### 落地页可见区块：英雄、功能（含至少 digest-page 与一张总结卡图）、定价（79 与 59）、+20 附加、主题 100 元说明、步骤、FAQ、底部 CTA

PASS. 构建 HTML `ecosystem/xiaotiezhu.html` 计数：

| 片段 | 次数 |
| --- | --- |
| `xiaotiezhu-avatar.webp` | 2（英雄与底部） |
| `xiaotiezhu-digest-page.webp` | 2（展示与点开） |
| `xiaotiezhu-vip-preview.webp` | 1 |
| `xiaotiezhu-vip-card.webp` | 1（preview 点开原图） |
| `xiaotiezhu-xiaowan-preview.webp` | 1 |
| `¥79` | 1 |
| `¥59` | 1 |
| `+20` | 8（正文含附加项与 FAQ，其余在描述） |
| `100 元一份` | 8（themeNote、功能与 FAQ） |
| `三步极速开通` | 1 |
| `常见问题解答` | 1 |
| `加微信咨询开通` | 2（英雄与底部，`href="/group"`） |

正文抽样：`邀请小铁柱进 1 个群：每月 79 元`、`每个群每月 59 元`、`每月 +20 元`、`后续更改主题：100 元一份`、`本服务由铁柱AGI 社区提供，非微信官方产品`。

主按钮 `href="/group"`，`data-from="xiaotiezhu"`，点击处理 `track('xiaotiezhu-cta', { from })`。次按钮 `https://vip.fmcat.top/?date=2026-10-27`，`target="_blank"`。点击主按钮后地址为 `http://127.0.0.1:5173/group`。390px 视口下定价、功能、附加项均为单列（computed grid 宽度 350px）。页面无「AI 生成」「内部路径」。

### `npm run build`（在 site/）成功，摘要写入 SELF_CHECK

PASS. 在 `site/` 执行 `npm run build`（`vitepress build docs`，vitepress v1.6.4），退出码 0。末尾摘要：

```
✓ building client + server bundles...
✓ rendering pages...
✓ generating sitemap...
build complete in 6.66s.
```

`llms.txt` 第 77 行：`- [小铁柱](https://bot.fmcat.top/ecosystem/xiaotiezhu): ...每月 79 元...每个群每月 59 元...每月 +20 元...100 元一份...`

### CHANGED_FILES.md 列出全部改动路径；改动已在任务分支

PASS. 清单见 `outputs/20261028-xiaotiezhu-landing/CHANGED_FILES.md`。`git branch --show-current` 输出 `cursor/heavy-job-20261028-xiaotiezhu-landing-5ae6`。未推 `main`。

### 未改价格数字与已入库文案关键句；未提交密钥

PASS. `git diff f0ede16 -- site/docs/.vitepress/theme/ecosystem.json site/docs/.vitepress/theme/links.json` 为空。JSON 现价仍是 plans `79` / `59`、addon `+20`、themeNote `后续更改主题：100 元一份`。`git diff` 无 `api_key` / `secret` / `token` / `cookie` / `password` / `BEGIN ` 行。`seo.json` 只新增 `ecosystem/xiaotiezhu.md` 的 meta 描述，句子取自上述 JSON，未改原文件。

## 备注

`bash scripts/setup.sh` 退出码 127：仓库内无该文件（`bash: scripts/setup.sh: No such file or directory`）。本任务不依赖 ffmpeg/yt-dlp。未下载视频或音频，故无 `LINKS.md`。
