---
title: agently-cli（Agent 邮箱命令行）
sidebar: false
prev: false
next: false
---

# agently-cli（Agent 邮箱命令行）

<ToolMeta id="agently-cli" />

`agently-cli` 是腾讯 QQ 邮箱推出的 Agent 邮箱命令行工具。**适合让 Bot 在云电脑上完成邮件收发、回复、转发、搜索以及附件下载。**

## 前置条件

- **系统需安装 Node.js 与 npm。**

## 安装

```bash
npm install -g @tencent-qqmail/agently-cli
npx skills add https://agent.qq.com --skill -g -y
```

## 登录与授权

**后台运行 `agently-cli auth login` 并将输出的原样链接在浏览器中打开完成授权。** 授权完成后命令会自动退出，切勿修改链接中的任何字符。

```bash
agently-cli auth login
```

## 验证

```bash
agently-cli auth status
agently-cli +me
```

## 常见坑与解决

### 浏览器打开授权链接提示无效或失败

**授权链接必须完整原样打开，禁止编码、拼接或添加空格。** 若失败超时切勿盲目重复重试，先排查具体报错。

### Bot 自行发信导致误发送

**执行发信操作前必须先让人工核对收件人与正文。** 发送邮件属于对外操作，需严格确认。

## 来源

- [Agent 邮箱官网](https://agent.qq.com)
- [agently-cli npm 包](https://www.npmjs.com/package/@tencent-qqmail/agently-cli)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
