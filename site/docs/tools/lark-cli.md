---
title: 飞书 CLI（lark-cli）
sidebar: false
prev: false
next: false
---

# 飞书 CLI（lark-cli）

<ToolMeta id="lark-cli" />

飞书官方命令行工具，适合让 Bot 以你的个人身份在**云电脑**上便捷操作飞书云文档、多维表格、云盘和知识库。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你现在的目标是在云电脑上安装飞书命令行工具 lark-cli 并完成用户授权。

1. 请在终端按顺序执行参考安装命令：
npx @larksuite/cli@latest install
npx skills add larksuite/cli -y -g

2. 凭证配置与登录处理要求：
首次配置应用凭证时执行参考命令：
lark-cli config init --new
请停下并将终端给出的链接发给我，由我在浏览器完成应用凭证创建。
用户登录时执行参考命令：
lark-cli auth login --no-wait --json --domain base,drive,docs,wiki
解析并提取返回结果中的 verification_url 和 device_code 原样发给我，随后停下；等待我在浏览器打开链接授权完成后，你再执行参考命令完成最终登录（将其中的 <device_code> 替换为实际设备码）：
lark-cli auth login --device-code '<device_code>'
整个过程不要向我索要密钥，不要打印密钥。

3. 安装完成标准：
登录完成后，在终端执行参考验证命令：
lark-cli --version
lark-cli auth status
lark-cli doctor
预期结果：lark-cli --version 正确输出版本号，lark-cli auth status 显示已登录，lark-cli doctor 诊断各项状态正常。

4. 常见坑及处理办法：
- 若环境未安装 Node.js 会导致安装失败，需确保已预装 Node.js 和 npm。
- 设备码过期需使用相同 domain 重新发起命令生成新码，切勿复用旧码。
- domain 参数必须写全所需权限（base,drive,docs,wiki），遗漏会导致相应模块缺少权限。

5. 完成后请用几句话汇报 CLI 版本、auth status 登录状态及 doctor 诊断结果。
````

</div>

## 需要你自己做的事

- 准备飞书账号并准备好 Node.js 环境
- 根据链接在浏览器中完成应用凭证初始化
- 打开验证链接输入 device_code 确认授权

## 来源

- [larksuite/cli 官方仓库](https://github.com/larksuite/cli)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
