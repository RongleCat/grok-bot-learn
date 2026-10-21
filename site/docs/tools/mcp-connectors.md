---
title: MCP 连接器
sidebar: false
prev: false
next: false
---

# MCP 连接器

<ToolMeta id="mcp-connectors" />

`MCP 连接器` 让 Grok 对话直接调用外部服务或自定义接口。**适合接入官方内置应用、预置第三方服务或自定义部署的 MCP 服务端工具。**

## 前置条件

- **需拥有 Grok 账号，商业版与企业版需团队管理员在控制台开通权限。**
- 自定义服务端必须具备公网可访问地址与鉴权防护。

## 登录与授权

**在 grok.com/connectors 点击 New Connector 完成对应服务的 OAuth 授权或填入 Custom 地址。** 自定义服务器需按需配置认证密钥，仅授予必要权限。

## 常见坑与解决

### 本地部署的 MCP 服务无法被 Grok 连接

**使用隧道服务将服务暴露至公网。** 运行在 `localhost` 的服务无法直接访问，需参考官方 Custom MCP Server Tunneling 进行内网穿透。

### 自定义接口存在未授权访问风险

**为自定义 MCP 服务器配置严格的鉴权机制。** 严禁将无保护的内部接口直接暴露在公网环境下。

## 来源

- [Grok 官方文档：Connectors](https://docs.x.ai/grok/connectors)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
