---
title: 飞书机器人长连接
sidebar: false
prev: false
next: false
---

# 飞书机器人长连接

<ToolMeta id="feishu-bot" />

基于飞书官方 Python SDK 的长连接消息方案，适合在无需公网 IP 的**云电脑**上实现事件监听与群聊机器人派活。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你现在的目标是在云电脑上配置飞书官方 Python SDK 环境，使用 WebSocket 长连接模式接收消息。

1. 请在终端按顺序执行参考安装命令：
python3 -m venv .venv
./.venv/bin/pip install lark-oapi requests

2. 凭证与配置处理要求：
配置飞书应用凭证时请停下，指导我将 App ID 与 App Secret 填入本地私密配置文件或环境变量中，不要让我把密钥贴进聊天，严禁在终端或日志中打印密钥。

3. 安装完成标准：
在终端执行参考验证命令：
./.venv/bin/python -c "import lark_oapi; print('ok')"
预期结果：终端正常输出 ok。
随后使用 lark.EventDispatcherHandler.builder 注册 register_p2_im_message_receive_v1，并通过 lark.ws.Client 启动客户端，长连接成功建立且无报错。

4. 常见坑及处理办法：
- Debian 系统受 PEP 668 保护，必须通过 .venv 虚拟环境中的 python 和 pip 运行。
- 飞书开放平台自建应用必须开启机器人能力，事件接收方式务必选择长连接，并订阅 im.message.receive_v1 事件。
- 权限至少需开通 im:message、im:message:send_as_bot、im:message.p2p_msg:readonly、im:message.group_at_msg:readonly、im:chat:readonly、im:resource。缺少群 @ 权限将无法收到群消息。
- 飞书推送同一条消息可能重复，必须根据 message_id 进行去重处理。
- 多个机器人在同群互相回复会陷入死循环，必须配置白名单与限频机制，且群消息仅处理 @本机器人 的内容。

5. 完成后请用几句话汇报虚拟环境建立情况、依赖安装状态及模块导入验证结果。
````

</div>

## 需要你自己做的事

- 在飞书开放平台创建企业自建应用并开启机器人功能
- 配置长连接事件接收方式并开通所需消息权限
- 将 App ID 和 App Secret 存入云电脑本地私密文件

## 来源

- [飞书官方 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [飞书开放平台](https://open.feishu.cn/)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
