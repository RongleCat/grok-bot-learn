---
title: Feishu ボット長接続
sidebar: false
prev: false
next: false
---

# Feishu ボット長接続

<ToolMeta id="feishu-bot" />

Feishu 公式 Python SDK をベースにした長接続メッセージングソリューションで、パブリック IP が不要な**クラウド PC**上でイベントリスニングやグループチャットボット連携を実現するのに適しています。

## Bot に送信するプロンプト

以下の内容をすべてコピーして Grok Bot に送信してください。クラウド PC 上で自動的にインストールと検証が行われ、ログインやシークレットキーの設定が必要な場合は一時停止して操作を待機します。

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于飞书 Python SDK（https://github.com/larksuite/oapi-sdk-python）的长连接机器人，以后接收群聊事件和派发任务用它。需要填密钥时请提醒我自己填。
````

</div>

## ご自身で行う作業

- Feishu オープンプラットフォームでカスタムアプリを作成し、長接続とボット機能を有効化する。
- プロンプトの案内に従って、アプリの App ID と App Secret を自身で入力する。

## 出典

- [Feishu 公式 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [Feishu オープンプラットフォーム](https://open.feishu.cn/)

> 本ページはコミュニティによる非公式なまとめであり、該当ツールの提供元および xAI との提携関係はありません。コマンドは公式ドキュメントに準拠します。

[← 目次に戻る](/tools/)
