---
title: muse2api
sidebar: false
prev: false
next: false
---

# muse2api

<ToolMeta id="muse2api" />

社区开源的 muse.ai 逆向封装项目，适合在**云电脑**上通过 OpenAI 兼容接口直接调用网页端免费额度进行对话、生图和生视频。

## 发给 Bot 的提示词

复制下方整段内容发送给你的 Grok Bot，它会在云电脑上自动安装并验证，遇到登录或配置密钥时会暂停等待你操作。

<div class="tool-prompt">

````text
你现在的目标是在云电脑上部署 muse2api 容器服务，并验证 OpenAI 兼容接口。

1. 请在终端按顺序执行参考安装命令：
git clone https://github.com/czg86389-hub/muse2api.git
cd muse2api
cp .env.example .env
docker compose up -d

2. 凭证与授权处理要求：
执行 cp .env.example .env 后先停下，请我将 .env 中的 MUSE2API_KEY 修改为自定义随机密钥，不要让我把密钥贴进聊天，不要打印密钥。登录时请停下，等待我在云电脑浏览器登录 muse.ai，并在 chrome://extensions 开发者模式加载解压后的 extension 目录扩展，填入服务地址与 MUSE2API_KEY 完成登录态导入。

3. 安装完成标准：
导入登录态后，在终端执行参考验证命令：
curl -s http://127.0.0.1:18610/v1/chat/completions -H "Authorization: Bearer $MUSE2API_KEY" -H "Content-Type: application/json" -d '{"model":"muse-spark","messages":[{"role":"user","content":"只回复 OK"}]}'
预期结果：接口正常返回包含 OK 的 JSON 格式响应。

4. 常见坑及处理办法：
- 扩展导入若提示缺少核心 cookie hatch_vml，先在同一浏览器打开 https://muse.ai/api/session 刷新 muse.ai，再重新导入。
- 调用视频接口时，时长参数必须用 duration，传 seconds 会被忽略，默认 6 秒；视频为异步任务，需轮询 /v1/videos/{task_id}。
- 若返回 Sorry, I ran into a problem 或未生成媒体，属于临时错误，执行退避重试。
- 网页会话约 48 小时到期会自动续期，若长时间不用失效需重新导入。
- 逆向项目存在封号与失效风险，更新前先检查代码改动，切勿一键在线升级。

5. 完成后请用几句话汇报容器运行状态、端口监听情况及验证接口返回结果。
````

</div>

## 需要你自己做的事

- 准备 muse.ai 账号并在云电脑浏览器中登录
- 在本地私密 .env 文件中设置自定义 MUSE2API_KEY
- 在浏览器加载仓库 extension 目录扩展并点击读取导入登录态

## 来源

- [muse2api 项目仓库（czg86389-hub）](https://github.com/czg86389-hub/muse2api)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
