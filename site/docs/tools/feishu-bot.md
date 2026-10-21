---
title: 飞书机器人长连接
sidebar: false
prev: false
next: false
---

# 飞书机器人长连接

<ToolMeta id="feishu-bot" />

基于飞书官方 Python SDK `lark-oapi` 的 WebSocket 长连接模式接收事件并转给 Bot。**适合无需公网 IP 和回调地址在云电脑上接收私聊或群聊 @ 消息并派活。**

## 前置条件

- **需安装 Python 3 并使用 venv 虚拟环境。**
- 需在飞书开放平台创建企业自建应用并开启机器人能力。
- 需订阅 `im.message.receive_v1` 事件并选择长连接方式。
- 需开通 `im:message`、`im:message:send_as_bot`、`im:message.p2p_msg:readonly`、`im:message.group_at_msg:readonly`、`im:chat:readonly`、`im:resource` 权限。

## 安装

```bash
python3 -m venv .venv
./.venv/bin/pip install lark-oapi requests
```

## 登录与授权

**代码中传入应用的 app_id 与 app_secret 建立客户端连接。** 凭证仅保存在本地私密文件中，严禁打印或贴入聊天窗口。

## 验证

```bash
./.venv/bin/python -c "import lark_oapi; print('ok')"
```

## 常见坑与解决

### 群内 @ 机器人收不到推送消息

**检查并在开放平台补开 `im:message.group_at_msg:readonly` 权限。** 漏开此权限将无法接收群内 @ 事件。

### Debian 系统提示环境受外部管理且未安装 SDK

**必须在 Python venv 虚拟环境内安装 lark-oapi 并运行脚本。** Debian 系统的 PEP 668 机制会限制全局安装。

### 收到重复消息或多机器人互答死循环

**代码中根据 `message_id` 进行去重并设置白名单与限频。** 此外群消息应仅处理 @ 本机器人的内容以防误触发。

## 来源

- [飞书官方 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [飞书开放平台](https://open.feishu.cn/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
