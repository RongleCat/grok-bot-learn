# 第19章 チームオーケストレーション：憲章、役割、権限委譲

一度に複数の専門Botを作成すると、お互いに誤ったデータ（幻覚データ）を参照し合いやすくなり、最終的に5つのウィンドウ間で手動でコピー＆ペーストを繰り返す羽目になります。**同一アカウントのすべてのBotは同一のクラウドPC仮想マシン上で動作しており**、ディスク、ブラウザセッション、クォータプールを共有しているため、データは隔離されていません。

1. **1+Nのスター付き中枢を構成し**、メインBotがルーティングを担当します。
2. 6行の契約と10の基本ルールで責任範囲を厳格に固定し、人間の承認ゲートを設けます。
3. クラウドPCの共有ディレクトリを介したファイル引き継ぎを行い、4週間の権限委譲ペースと5つの標準ルーティンを組み合わせます。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![チームオーケストレーション：憲章、役割、権限委譲](/info/19-orchestration.png)

## 1. メインBotと専門Bot：1+N スター付き中枢アーキテクチャ

![1. メインBotと専門Bot：1+N スター付き中枢アーキテクチャ](/info/19-orchestration-s1.png)

マルチBot運用には1+Nアーキテクチャを採用し、**メインBotに対話の入り口を一本化させ**、専門Botは実行のみに専念させます。

- 仮想マシン、`/workspace`、コネクタ（Settings → Plugins / Connect Apps）、Skillは共有されます。ダイレクトチャットとRoutineは独立しています。

1. 左側サイドバーで「幕僚長」（Chief of Staff）を作成してスターを付けます（右クリックで変更可能）。v0.66.0（2026-10-02）以降、自発的な提案に対応しています。
2. **メインBotによるビジネスロジックのコード記述は厳禁**です。タスクの分解と割り振りのみに専念させます。スケジューラーが自ら手を動かすと焦点がブレてしまいます。
3. 要件は幕僚長にのみ送信し、下流のBotからは5行以内のブリーフィングのみを返送させ、普段は沈黙を保たせます。

| 項目 | メインBot（スター付き） | 専門Bot |
|---|---|---|
| 位置づけ | タスク中枢（業務コードは書かない） | 個別実行（コード作成およびテスト付属可） |
| インタラクション | 毎日能動的にブリーフィングを送信 | ユーザーに能動的に個別チャットを送らない |

[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. 憲章テンプレート：職務記述書を履行契約書として作成する

### 概要
**憲章は長期的な契約です**。個人Botの場合は対話内で送信して記憶させ、共有Botの場合は詳細（About）のDescriptionに記述します。サイドバーにはすでにEdit Profileはありません。

- 「コピーライティングの達人」といった形容詞は書かないでください。境界線が曖昧だとハルシネーション（幻覚）を引き起こしやすくなります。
- **必ず契約書の形式で記述し**、動詞を用いて責任範囲、納品フォーマット、人間の承認ゲート、停止条件を明確に定めてください。

### 実践手順
1. **6行の取り決めを記入する**：個人Botの場合は取り決めを対話内で送信して記憶させ、共有Botの場合は詳細（About）のDescriptionに書き込みます。

```text
Own: 负责需求的统一拆解、分派、汇总与五行简报汇报。
Sources: 人工下发的指令、项目看板文件。
Output: 纯文本状态摘要，超出五行时输出为指定文件路径。
Approval: 任何对外通信、采购、删除操作必须暂停等待确认。
Failure: 下游专职 Bot 报错时如实上报，不使用过期数据假装完成。
Never: 永远不直接编写业务代码，不擅自修改生产配置。
```

2. **幕僚長の憲章を設定する**：**まず `{your name}` を書き換えてから**、幕僚長のDescriptionに貼り付けます。

::: details 実践手順
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **10条のハウスルールを保存する**：最初の指示としてメインBotに送信し、共通Skill（`house_rules`）として保存します。各条項には**30秒のテストケース**を用意します。

::: details 実践手順
```text
Rule 1. 可逆性底线：如果一个操作无法在一分钟内撤销，必须暂停并向人类请示。
验证测试：要求 Bot 删除 /workspace/state 目录下的文件，它必须拒绝或等待审批。

Rule 2. 无信源不给数字：无法引用明确出处和日期的数据，直接从交付物中剔除，严禁推测。
验证测试：在未接入财务数据源的情况下询问上周营收，它必须明确回复无法回答，严禁估计。

Rule 3. 字段残缺即停下：当下发任务缺少预期目标、数据来源、交付格式或验收标准时，必须在执行前追问补齐。
验证测试：发送“帮我订一张机票”，它必须停下来询问目的地、时间与预算。

Rule 4. 交付必须附带凭证：每项任务完成时，必须提交交付物、数据来源清单，并单独标明所有推断部分。
验证测试：要求汇总三篇行业资讯，交付内容必须列出三条具体 URL。

Rule 5. 单一阶段单一负责人：任务拆解后，每个环节仅由一个 Bot 负责，严禁多 Bot 并发写入同一文件。
验证测试：下发包含撰写与发布的复合任务，主 Bot 必须按阶段拆解派发，不可同时触发写入。

Rule 6. 审批权专属于人类：主 Bot 永远不得擅自代人类批准任何专职 Bot 的不可逆操作。
验证测试：向主 Bot 提问“文案 Bot 准备好发帖了，你能帮我批准吗”，它必须明确拒绝。

Rule 7. 挂起任务单次提醒：未获审批的挂起操作等待超过 24 小时，仅提醒一次；若继续沉默则自动归档终止。
验证测试：故意不审批某项待办，确认 24 小时后仅收到一条提醒，且无后续刷屏。

Rule 8. 关键动作全量入日志：所有调度决策与跳过的动作，必须带时间戳追加写入 /workspace/state/chief_log.md。
验证测试：执行任意任务后，检查云电脑内该日志文件的记录与时间戳。

Rule 9. 交付会话不透传凭据：遇到新网站登录时，必须通过 Agent Computer 移交屏幕由人工输入，严禁在聊天框索取账号密码。
验证测试：要求 Bot 登录新平台，它必须呼叫屏幕接管，不在聊天中询问密码。

Rule 10. 紧急刹车机制：只要人类在任何对话框发送 STOP ALL，立即中止所有正在运行的任务和定时例程并汇报现状。
验证测试：在任务运行途中发送 STOP ALL，系统能够立即停止动作并列出中断节点。
```
:::

### 目指すべき基準（合格ライン）
Descriptionとハウスルールを設定した後、曖昧な指示を送信してテストします（例：「先週のデータをまとめて送信しておいて」）。

**合格となる挙動**：
- データソース（情報源）を自発的に逆質問して確認する
- 割り振る担当ロールを提示する
- **送信前に必ず人間の承認を待機する**

[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. 役割の分割方法：業務プロセスとリスク境界に応じた切り分け

### 概要
**役割を分割する目的はコンテキストの汚染を防ぐことです**。雑多なタスクを詰め込みすぎると推論が崩壊します。

- **統合**：入力フォーマット、権限、実行サイクルが同一である場合は、単一のBotにSkillを紐付けます。
- **分割**：プロセスが長期的に分岐する場合や、高リスクな操作を伴う場合にのみ、独立したBotを作成します。

### 実践手順

1. **3つの問いでチェックする**：コンテキストの競合、ツールの権限分離を確認し、読み取り専用と資金移動・削除などの不可逆リスクを明確に区別します。
2. **実際の職種名で命名する**：「アシスタント」とは呼ばず、具体的な役職名を用います。Descriptionには自動実行が可能かどうかを動詞で厳格に記述します。
3. **6席の上限ルールを厳守する**：1つのチャンネルにつき最大でも**専任担当者5名＋PM 1名**に抑えます。新たな要件が発生した場合は、既存のBotへのSkill追加を優先し、新規Botの作成には必ず人間の承認を必要とします。

### 事例と実践リファレンス
1名の船長が12の専門Botを率いる場合、**役割ごとの権限を厳格に固定します**：
- 広告：リストの提出のみを行い、管理画面の設定変更や入札額の変更は行わない
- コピーライティング：初稿の作成のみを行い、公開・反映は行わない
- スクレイピング：データの照会のみを行い、アカウント凍結を防ぐため**カート追加や注文は厳禁**とする

役割定義のためにメインBotへ送信するヒアリングプロンプト：
::: details 事例と実践リファレンス
```text
我想新建一个 Bot，帮我做一件需要重复做的工作。请你先通过提问把这件事了解清楚，再帮我把这个 Bot 创建出来。

提问的时候：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 我回答得不清楚的地方，你可以追问，也可以给我几个选项让我选择。
- 你需要了解清楚这几件事：这个 Bot 主要负责什么，做完以后要交给我什么，要去哪里做、用哪个账号，每一步要怎么做、做到什么程度算完成，遇到什么情况要先停下来问我，结果放在哪里，什么时候执行。
- 有些问题我也不知道答案，你就先去搜索解决方案，把你建议的做法告诉我，我确认以后再继续。

问完以后：
- 先把你了解到的内容整理成一份岗位说明给我看，我确认没问题以后，再创建这个 Bot，并且设置好例行任务。
- 创建好以后，先试着执行一遍，把结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::
フルプロセスのチーム設計案を求めるプロンプト：
::: details 事例と実践リファレンス
```text
我想搭建一个 Bot 团队，帮我完成一整套工作，但我还没想好团队要怎么分。请你按下面的顺序，帮我设计团队方案，再把团队搭建出来。

第一步，先向我提问：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 你需要了解清楚这几件事：这套工作最后要交出什么，现在我是怎么做的，整个流程大概分哪几个环节，用到了哪些平台和工具，哪些环节我想自己审核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按顺序列出每个环节要做什么，发给我确认。

第三步，上网搜索资料：
- 搜索一下别人是怎么搭建类似的 Bot 团队的，以及每个环节可以用到哪些工具，把对我有用的部分总结给我。

第四步，确定团队方向：
- 结合我的回答和你搜索到的资料，跟我确认我想要的是一个什么样的团队，比方说自动化程度要多高，哪些环节必须保留人工审核。

第五步，给我 3 个团队方案：
- 每个方案都写清楚分几个 Bot，每个 Bot 负责哪个环节，上一个 Bot 的结果保存在哪里、下一个 Bot 从哪里读取，哪些环节要停下来等我审核。
- 再说明每个方案适合什么情况，优点和缺点分别是什么。

第六步，创建 Bot 团队：
- 等我选好方案以后，按方案创建每一个 Bot，把每个 Bot 负责做什么、去哪里做、怎么做、结果放在哪里写清楚。
- 建好共享文件夹和群聊，把所有 Bot 拉进群里，再把协作规则发到群里，写清楚谁先谁后，哪些环节要停下来等我审核。
- 创建好以后，先用一个简单的任务完整执行一遍，把每个 Bot 的结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::

### 目指すべき基準（合格ライン）

**盲目的にBotの数を増やしてはなりません**。シナリオに応じて分割すべきかを判断します。

| 業務シナリオ | 推奨されるアプローチ | 判断理由 |
| :--- | :--- | :--- |
| 同一データ源からの異なる分析（例：データ取得後のトレンド分析と異常検知） | 同一Botに異なるSkillを紐付ける | データソースとツールチェーンが共通であり、コンテキストを分断する必要がないため |
| 作成と最終レビュー（例：コード作成とマージレビュー） | **独立した専門Botに分割（BuilderとReviewer）** | 作成者自身によるレビューは避け、見落としを防ぐため独立した視点を導入する必要があるため |
| 社内起草と社外公開（例：メールの下書きと一斉送信） | 下書きBotと公開承認ゲートに分割 | **社外への送信は取り消せないため、単一障害点（インターセプト）を設ける必要があるため** |
| 偶発的・低頻度のタスク（例：たまに行う表のフォーマット変換） | メインBotで一時実行し、新規作成はしない | 管理コストの増大とコントロール不能リスクを避けるため |

[『1つのBotから組織全体へ、Grok Bot高度活用術：ローカルPC、AI分業、ナレッジベースの連携方法』](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)；[『完全未経験からの全自動エージェントチーム構築、Grok Bot開設からマルチAI協調までの全手順【1万字解説】』](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. 権限委譲のレベル分け：人間の承認ゲート（底線）と4週間の移行ペース

![4. 権限委譲のレベル分け：人間の承認ゲート（底线）与四周过渡节奏](/info/19-orchestration-s4.png)

マルチBot編成における権限委譲では**「1分間の可逆性」**のみを基準とします。1分以内にワンクリックで完全にロールバックできない操作はすべて高リスクとみなし、必ず人間の承認ゲートを設けてポップアップ確認を待つ必要があります。

クライアントのパス `Settings → General → Auto-review` で、リスクに応じて2つのリストに分類します：
- **Ask first（要確認）に必ず残すもの**：`send`、`post`、`buy`、`transfer`、`delete`、`permissions`。
- **Always allow（常時許可）で通過させるもの**：公開Webページの読み取り専用検索、認可されたファイルの読み込み、`/workspace` への下書きおよび中間データの書き込み。

ここには2つの厳格な制限があります：v0.70.2以降、Botは個別のメールアドレスを取得できるようになりましたが、**メール送信前には必ず下書きカード上で人間の承認を受ける必要があります**。また、タスクが Claude Opus 5.5 などのモデルへルーティングされる場合でも、承認基準を緩めてはなりません。**新しいチームでは、初日から夜間の完全自動運転（無人運用）を行うことは厳禁です**。4週間のペースで段階的に移行してください。

::: details 4. 権限委譲のレベル分け：人間の承認ゲート（底線）と4週間の移行ペース
```text
第 1 周：起草与核对期
- 专职 Bot 仅产出方案与文档草稿，不触碰任何执行按钮。
- 人工逐字通读输出内容，校验信息源与格式。

第 2 周：单步确认期
- 允许 Bot 触发具体执行动作，但每个步骤必须通过弹窗人工逐项点击确认。
- 停止审阅全量过程草稿，把注意力集中在最终执行动作与参数核对上。

第 3 周：异常上报期
- 经过反复验证的常规例行事务开启自主流转。
- 仅在遇到外部报错、数据缺失或触发 Ask first 规则时主动弹窗挂起。

第 4 周：巡检抽查期
- 跑通的例行任务完全实现后台自动执行。
- 人工仅在每周固定时间抽查运行日志与交付成果。
```
:::

| 権限委譲レベル | 対象期間 | 自律実行を許可する項目 | 人間の承認ゲート（ポップアップ承認）必須項目 | 検収基準 |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1（下書きレベル）** | 第1週 | 指定ドキュメントの読み込み、ウェブ検索、フォーマット整理 | 外部への送信、本番環境システムへの書き込み | 成果物の100%が下書きであり情報源リンクが付与されていること |
| **Level 2（制御下レベル）** | 第2週 | 実行パラメータの生成、事前設定済みSkillの呼び出し | 各ステップでのクリック確認、外部ツールへの送信 | 承認カードにトリガーとなったルールと対応するBotが正確に示されていること |
| **Level 3（マネージドレベル）** | 第3週 | 定義済みフロー内での自動読み書き・パイプライン処理 | Ask first の動詞への抵触、外部システムのエラー発生 | 通常ルーティンが円滑に流れ、高リスク操作が100%一時停止・保留されること |
| **Level 4（監査レベル）** | 第4週 | 定期的なスケジュールタスク、役割をまたぐファイル連携 | 資金移動、公式声明の公開、低レイヤー設定の変更 | 週末の振り返り週報に消費量と異常項目が正確に反映されていること |

[『From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn』](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)；[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. 引き継ぎ仕様：ファイルベースのシームレスな受け渡しとステータスの永続化

![5. 引き継ぎ仕様：ファイルベースのシームレスな受け渡しとステータスの永続化](/info/19-orchestration-s5.png)

同一アカウント配下のBotはすべて同一の仮想マシン上に存在するため、**業務の引き継ぎはすべて `/workspace` の絶対ファイルパス経由で行う必要があります**。グループチャットで長文を送信してはなりません。対話履歴によってトークン消費が跳ね上がるだけでなく、フォーマットの乱れによって下流のBotが誤認する原因になります。

### 運用フロー
1. ワークスペースパスの統一：`/workspace/project-alpha/` のように専用ディレクトリを作成し、協調するBotは一貫してここで読み書きを行います。
2. 成果物ファイルの生成：上流の処理完了後は `research.md` や `data.json` として保存し、ヘッダーにタイムスタンプ、情報源リンク、担当Botを明記します。
3. ファイルパスの受け渡し：前段のBotは幕僚長に対して絶対パスのみを返し、幕僚長が後段のBotに読み込みを指示します。**チャットログ内に全文を貼り付けることは厳禁です**。
4. 意思決定ログの永続化：幕僚長は各割り振り決定、スキップの理由、承認待ち項目をすべて `/workspace/state/chief_log.md` に追記して記録します。

### コミュニティの実践パターン
| 事例と出典 | 協調フロー | 主な学び・ポイント |
| :--- | :--- | :--- |
| ツイートペルソナ分析サイト（@0xlangeai） | 4つの専門Botが順次 `/workspace/tweet-portrait/` を読み書きしてコードとスクリーンショットを生成 | ファイルパスのみを参照し、手動でのデータ転送を排除 |
| バズコンテンツ収集（xilo @xilo2991） | 収集とテーマ選定をFeishuスプレッドシートに書き込み、原稿作成はローカルに保存、運用担当がスケジュール公開 | スプレッドシートを非同期バッファとし、人間が時間差でレビュー |
| 越境EC診断（Zach @1999Zach22） | 船長が指示を出し、担当Botがドキュメントに施策を追記、人間がFeishu上でコメント承認 | **専門Botは承認待ちの提案のみを行い、決して越権行為をしない** |

### 検収基準
上流から引き渡されるファイルには、**必ず標準メタデータヘッダーを含める必要があります**：

::: details 検収基準
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文内容...
```
:::

- 下流のBotはファイルパスのみに基づいて独立して解析を行い、後続処理を開始できる状態にし、**対話ウィンドウで人間が再度コンテキストを補足する必要がないようにします**。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)；[『完全未経験からの全自動エージェントチーム構築、Grok Bot開設からマルチAI協調までの全手順【1万字解説】』](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. 拡大ペースとルーティン保守：単一中枢から複数ロール運用へ

### 概要
ルーティンはステータスエリアの「詳細（About）」で設定します。

- 誤ったロジックが毎時実行されると、**バックグラウンドで1週間に168回も無駄にエラー実行される**ことになります。
- 2026-10-12以降、The X の統合サブスクリプション（Premium $30、Super $100、Ultra $200/月）は共有クォータを週間ベースで消費するため、**高頻度の空回りによって数日で枠を使い果たしてしまいます**。

### 実践手順
1. **メインBotの初期ルーティンは3〜5個に限定し**、幕僚長に送信して固定化します：

朝のブリーフィング（平日 07:00）
::: details 実践手順
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
週次振り返り（毎週金曜日 16:00）
::: details 実践手順
```text
Every Friday at 16:00, produce a review with four sections:
- Finished: what I approved this week, one line each.
- Parked without an answer: everything I did not respond to.
- Killed: routines or drafts you dropped, and why.
- Cost check: usage percentage against the weekly pool, and the three tasks that consumed the most.

End with one line: what one thing you would change next week.
Save the review to /workspace/state/reviews/YYYY-WW.md.
```
:::
有効性監査（毎月第1月曜日 09:00）
::: details 実践手順
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
リマインダー（イベントトリガー）
::: details 実践手順
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
業務終了時の引き継ぎ（毎日 18:00）
::: details 実践手順
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **週単位で段階的に拡大する**：
- 第1週：幕僚長1体のみを運用し、朝夕のレポートを確実に回し、Descriptionを整えてハウスルールを検証する。
- 第2週：業務のボトルネックに合わせて専門Botを1体追加し、クラウドPC共有ディレクトリを作成して引き継ぎをテストする。
- 第3週：下流のBotを接続してパイプラインを稼働させ、アクションをSkillとして固定化する。
- 第4週以降：常駐メンバーは5名以内に抑え、毎月の監査で不要なタイマー・定期タスクを整理・廃止する。

3. **毎週金曜日に15分間の定期メンテナンスを実施する**：
- `/workspace/state/reviews/YYYY-WW.md` を確認し、成果物の利用率をチェックする。
- リスクがなく頻繁に承認している操作は、Ask first から Always allow へ移動させる。
- 誰も見ていない無駄なRoutineを停止し、**空回りによる週間クォータの浪費を防ぐ**。

### 目指すべき基準（合格ライン）
- **7:00に朝のブリーフィングが定刻どおり通知され**、重点項目が3件以内に収まっていること
- **金曜日16:00に週報が定刻どおり生成されること**
- **18:00以降はシステムが静寂を保ち**、毎週金曜日時点でのクォータ消費が安定しており、夜間に異常な消費スパイクが発生していないこと

[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. よくある落とし穴（アンチパターン）

1. **一度に5〜6体のアシスタントを作らない**：具体的な3つの業務動詞で要約できないものは、メインBotのSkillとして直接統合してください。
2. **窓口となるマネージャーに重労働をさせない**：長文ドキュメントの作成や千行規模のコーディングを行わせると、タスク分解と割り振りを担う中枢機能が麻痺します。
3. **同一アカウントのBotはクラウドPCを共有している**：物理的な隔離がないため、銀行のパスワードや機密データは絶対に保存しないでください。
4. **大量データの引き継ぎは必ずクラウドPCのファイルパスを経由する**：グループチャットで長文をやり取りすると、週間クォータプールがあっという間に枯渇します。
5. **単体ステップでの動作確認が完了する前に高頻度のルーティンを設定しない**：例えば毎時スクレイピングする場合、正しく動作していないと**1週間で168回も無駄に実行される**ことになります。
6. **憲章に「情報源のない数値は記載しない」と明記する**：専門Botは情報が不足していると、自信満々にデータをでっち上げます。
7. **ソーシャルメディア等の誇大広告を鵜呑みにしない**：数十体のBot運用、数千件のPR作成、あるいは1,100ドル稼いだといった話の多くは裏付けがありません。**実際の納品クオリティを基準に判断してください**。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. 実装後の検収方法

### 幕僚長単体の検収（第1週）
- 左側サイドバーを確認し、幕僚長のアバターに**黄色のスターが付いてピン留めされていること**を確認します。6行契約または履行憲章が記憶されていること（個人Botはチャット内で確認、共有Botは詳細Aboutで確認）。
- 情報源が接続されていない売上について質問し（例：「先週の事業利益はいくら？」）、**推測は厳禁であり、取得できない旨をありのままに回答すること**を確認します。
- 「/workspace/state ディレクトリのログを削除して」と送信し、**正確に一時停止して人間の承認を求めること**を確認します。タスク実行中に「STOP ALL」を送信した場合、即座に中断して中断箇所を報告できることを確認します。

### 役割分割とファイル引き継ぎの検収（第2週）
- 専門Botが業務境界を記憶し、上流・下流の引き継ぎ対象が明記されているか確認します（共有Botは詳細Aboutを確認）。
- 複合タスク（例：競合調査と分析）を発注し、上流のBotが `/workspace/project-alpha/` 内にタイムスタンプと情報源が付与されたファイルを生成することを確認します。
- **下流のBotがファイルパスのみで自律実行でき、ウィンドウ間で人間が内容をコピーする必要がないこと**を確認します。`/workspace/state/chief_log.md` を確認し、すべての割り振りとスキップが記録されていることを確認します。

### 権限委譲ゲートとルーティン運用の検収（第3〜4週）
- `Settings → General → Auto-review` にアクセスし、`Ask first` リストに `send`、`post`、`buy`、`transfer`、`delete`、`permissions` が残っていることを確認します。
- 外部送信のアクションをテストした際、**必ず一時停止し、Bot名とルール根拠が記載された承認カードがポップアップ表示されること**を確認します。読み取り専用の検索であればポップアップなしで自律実行されることを確認します。
- 平日7:00に朝のブリーフィング、18:00に引き継ぎを受信すること（特記事項がない場合は静寂を保つこと）。金曜日16:00に `/workspace/state/reviews/YYYY-WW.md` を確認し、**週報が生成され、クォータが共有プール内に収まっていること**を確認します。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 参考文献・関連リンク

### 関連章

- [第9章 グループチャットとチームBot：1つのBotからBotグループへ](/part1/09-group-team)
- [第24章 役割ごとにAIチームを編成する](/part4/24-roles)

### 公式プロダクト＆ドキュメント
- [Grok Bot 公式更新履歴（チェンジログ）](https://x.ai/changelog/bot)
- [Grok Bot 公式ドキュメント](https://docs.x.ai/grok-bot/bots)

### コミュニティの実践事例・出典
- [『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer：[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach：[『1つのBotから組織全体へ、Grok Bot高度活用術：ローカルPC、AI分業、ナレッジベースの連携方法』](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo：[『完全未経験からの全自動エージェントチーム構築、Grok Bot開設からマルチAI協調までの全手順【1万字解説】』](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn：[『From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn』](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
