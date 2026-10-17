# 第 6 章 · 共享云电脑

你名下所有 Bot **共用一台云端电脑**：同一文件系统、同一浏览器登录态、同一批已装应用。电脑属于你的账户而不是某个 Bot，所以放在上面的东西对你所有 Bot 都可见；不同用户严格隔离。与队友的团队 Bot 聊天时，它通常也在**你的**电脑上运行。

## 关键事实

- 每个 Bot 有自己的屏幕，可并行；单个 Bot 同时只跑一个电脑操作任务。
- 客户端右侧可随时看实时画面，敏感步骤点 Take over 接管。
- 部分站点屏蔽机房 IP：可在设置的 Computer 页开启"流量经过本地设备"。
- 云电脑可能因底层更新/维护被**重建**：自装的应用和包会被移除（持久盘上的文件与登录通常保留）。

## 推荐做法

1. 把云电脑当**可丢弃容器**：配置、服务清单、脚本同步到私有 Git 仓库。
2. 维护一份 `services-ledger.md`（服务用途、依赖、启动命令、数据目录）和一键 `restore.sh`。
3. 跨 Bot 交接用 `/workspace` 下的固定文件。
4. 凭证不落明文；登录一律人工接管完成。

## 电脑坏了怎么办

见 [官方：电脑恢复](https://cursor.com/cn/help/grok-bot/computer-recovery)；企业管理员可在仪表盘 **Manage Bot Computers** 重建或终止成员电脑（详见[团队与企业](/appendix/d-enterprise)）。

## 来源

- [官方：你的 Bot 共用一台计算机](https://cursor.com/cn/docs/grok-bot)
- [官方：管理 Bot 电脑](https://cursor.com/cn/docs/grok-bot/computers)
- [官方：电脑恢复](https://cursor.com/cn/help/grok-bot/computer-recovery)
- [4.6 虚拟机、记忆与备份](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- [Grok Bot 虚拟机重置后工具全没了？备份恢复教程（附提示词）](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)
