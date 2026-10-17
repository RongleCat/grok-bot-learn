# Grok Bot 新手指南

https://bot.tiezhu.si 的源码，社区非官方新手指南，作者铁柱AGI（X @cgnot996）。

- 站点：VitePress，源文件在 `site/docs/`，信息图和案例图在 `site/docs/public/`
- 构建：`cd site && npm install && npm run build`
- 部署：`./deploy.sh`，发到 Cloudflare Pages 项目 `tiezhu-grokbot`，凭证从 `~/.agents/secrets/cloudflare.env` 读取，不进仓库
- 内容流水线脚本在 `v4/`，`v4/out5/` 是各章定稿，`v4/assemble.py` 把定稿组装进 `site/docs/`

仓库：https://github.com/RongleCat/grok-bot-learn
