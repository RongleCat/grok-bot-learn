---
title: agently-cli（Agent メールコマンドライン）
sidebar: false
prev: false
next: false
---

# agently-cli（Agent メールコマンドライン）

<ToolMeta id="agently-cli" />

Tencent QQ メールが提供する公式コマンドラインツール。Bot が**クラウド PC** 上でメールの送受信、過去メールの検索、添付ファイルのダウンロードを行うのに適しています。
Bot がクラウド PC 内でメールを送受信し、履歴を検索し、添付ファイルをダウンロードします。
結論として、Bot はクラウド PC 側で日常的なメール送受信、履歴検索、添付ファイルの自動ダウンロードを単独で完結できます。


## Bot に送信するプロンプト

以下の内容をすべてコピーして Grok Bot に送信してください。クラウド PC 上で自動的にインストールと検証が行われ、ログインやキー設定が必要な場合は一時停止してユーザーの操作を待ちます。

<div class="tool-prompt">

````text
帮我在你的云电脑上安装 agently-cli（https://agent.qq.com），以后收发邮件、检索历史邮件和下载附件用它。需要登录或授权时停下来把链接发给我由我完成。
````

</div>

## ユーザー自身が行うこと

- QQ メールまたは Agent メールのアカウントを準備する。
- Bot から送信された認証リンクをブラウザで開き、認証を完了する。

## 出典

- [Agent メール公式サイト](https://agent.qq.com)
- [agently-cli npm パッケージ](https://www.npmjs.com/package/@tencent-qqmail/agently-cli)

> 本ページはコミュニティによる非公式なまとめであり、該当ツールのベンダーおよび xAI との提携関係はありません。コマンドの詳細は公式ドキュメントに準じます。

[← 目次に戻る](/tools/)
