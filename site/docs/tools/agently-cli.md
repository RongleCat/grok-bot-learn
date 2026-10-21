---
title: agently-cli（Agent 邮箱命令行）
sidebar: false
prev: false
next: false
---

# agently-cli（Agent 邮箱命令行）

<ToolMeta id="agently-cli" />

腾讯 QQ 邮箱推出的官方命令行工具，适合让 Bot 在**云电脑**上高效收发邮件、检索历史邮件并下载附件。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你现在的目标是在云电脑上安装 agently-cli 及其技能包，并完成 Agent 邮箱授权验证。

1. 请在终端按顺序执行参考安装命令：
npm install -g @tencent-qqmail/agently-cli
npx skills add https://agent.qq.com --skill -g -y

2. 登录与授权处理要求：
执行参考登录命令：
agently-cli auth login
该命令为交互式长命令，请将其置于后台运行。捕获到输出中的授权链接后立即停下，把原始链接原样发给我，不得对链接进行转义、拼接或添加空格。等待我在浏览器打开链接完成授权后，你再继续后续操作。

3. 安装完成标准：
授权完成后，在终端执行参考验证命令：
agently-cli auth status
agently-cli +me
预期结果：agently-cli auth status 显示授权正常，agently-cli +me 成功输出当前绑定的邮箱地址。

4. 常见坑及处理办法：
- 授权链接被改动会导致授权失败，必须原样打开。
- 授权超时或失败不要反复盲目重试，先查看具体报错排查原因。
- 发送邮件属于对外操作，执行发信前必须向我确认收件人与正文。

5. 完成后请用几句话汇报 CLI 与技能安装情况、授权状态及绑定的邮箱账号。
````

</div>

## 需要你自己做的事

- 准备 QQ 邮箱或 Agent 邮箱账号
- 打开 Bot 发送的原始链接在浏览器中完成授权
- 在 Bot 实际发信前确认收件人及正文内容

## 来源

- [Agent 邮箱官网](https://agent.qq.com)
- [agently-cli npm 包](https://www.npmjs.com/package/@tencent-qqmail/agently-cli)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
