# 第 8 章 · 连接应用、邮箱与 Secrets

## 接入顺序：先跑通界面，再挂连接器

人能手动点完的事，先让 Bot 用云电脑和浏览器去点；跑稳、验证过价值，再换成插件/连接器或脚本，避免一次装一堆插件徒增维护。

## 插件（连接器）

在设置里连接支持的服务（如 Slack、GitHub、Google 等），Bot 以你的身份读写。插件 ≠ 触发器：要"某事发生就开工"请用[例程](/guide/09-routines)。

## Bot 专属邮箱

对 Bot 说 `claim your email`，可获得 `名字@mail.grokbot.com` 地址，用于收信、注册网站、联络客户；从该地址**发信前需要你在界面批准**。团队账号需管理员允许。

## Secrets

API Key 等放进设置的 **Secrets**，不要贴在对话里。

## 技能/CLI 扩展

- 开源 Skill：把仓库地址发给 Bot 说"帮我安装"，所需 Key 放 Secrets。
- 云电脑上的 CLI 工具要在 Bot 电脑终端里**单独登录**，不要拷贝本机登录态（会互相顶 token）。

## 来源

- [官方：连接插件](https://cursor.com/cn/help/grok-bot/connect-plugins)
- [官方：Bot 邮箱](https://cursor.com/cn/help/grok-bot/agent-email)
- [官方：Secrets](https://cursor.com/cn/help/grok-bot/secrets)
- [4.5 连接器、Skill、模板与对外入口](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
