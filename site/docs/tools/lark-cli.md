---
title: 飞书 CLI（lark-cli）
sidebar: false
prev: false
next: false
---

# 飞书 CLI（lark-cli）

<ToolMeta id="lark-cli" />

`lark-cli` 是飞书官方推出的命令行工具。**适合让 Bot 以个人用户身份直接操作飞书云文档、多维表格、云盘以及知识库。**

## 前置条件

- **系统需安装 Node.js 与 npm。**
- 拥有飞书账号。

## 安装

```bash
npx @larksuite/cli@latest install
npx skills add larksuite/cli -y -g
```

## 登录与授权

**首次运行 lark-cli config init --new 配置凭据，再通过设备码登录。** 运行 `lark-cli auth login --no-wait --json --domain base,drive,docs,wiki` 获取链接与码，授权后执行 `lark-cli auth login --device-code` 提交该码。

```bash
lark-cli config init --new
lark-cli auth login --no-wait --json --domain base,drive,docs,wiki
lark-cli auth login --device-code '<device_code>'
```

## 验证

```bash
lark-cli --version
lark-cli auth status
lark-cli doctor
```

## 常见坑与解决

### 提示设备码过期导致登录失败

**使用相同的 `--domain` 参数重新发起登录命令获取新码。** 切勿直接复用已过期的旧设备码。

### 执行特定模块命令提示无权限

**在 `--domain` 参数中将所需能力一次性写全。** 若发起授权时漏填对应域，相应命令将无法调用。

### 向导安装直接报错中断

**确认系统中已正确安装 Node.js 与 npm。** 缺少 Node 环境会导致向导脚本无法执行。

## 来源

- [larksuite/cli 官方仓库](https://github.com/larksuite/cli)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
