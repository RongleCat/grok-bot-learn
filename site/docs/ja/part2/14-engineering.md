# 第 14 章 事例：エンジニアリング＆研究開発チーム

ローカルで監視し続けるのはやめ、作業を**クラウドに委任**しましょう。

- PCはいつでもシャットダウン可能。24時間稼働するため、深夜2時に起きてCIを確認する必要はありません。
- 隔離された環境でコーディングし、プルリクエストには本物のエビデンスとログを添付して、アサーションの改ざんによる偽のパスを防ぎます。

朝は**納品レポートを確認してリリースを判断**します。

## コアアーキテクチャ：Harness、モデルの頭脳、ローカル CLI Agent の役割分担

![コアアーキテクチャ：Harness、モデルの頭脳、ローカル CLI Agent の役割分担](/info/14-engineering-s1.png)

### 各役割の位置づけと3者の分担
2026年10月7日、プラットフォームに Claude Opus 5.5 などのモデルが推論に導入されました。**システムがモデルを自動スケジューリングし、手動による単発のセレクターは提供されません**。単一モデルの特性に頼るのではなく、プロセスはステータスファイルと自動検証によって厳格に制御する必要があります。

| 役割 | 実行ホスト | 権限と責務 |
| :--- | :--- | :--- |
| Grok Bot | クラウドPC（`/workspace` 共有ストレージ） | パトロールとタスク割り振りを実行。**Draft PR の作成のみ行い、デフォルトブランチへの直接プッシュや本番リリースは厳禁** |
| ローカル CLI Agent | ローカルターミナルまたは一時コンテナ | 独立ブランチで依存関係の取得とコード変更を行い、ビルドを実行 |
| 人間の責任者 | 個人のワークステーション | **リリースキーと本番環境への書き込み権限を保持**し、アーキテクチャの意思決定とマージの承認を担当 |

### 環境設定とセキュリティの分離
同一アカウント配下のすべての Bot は、同じクラウドPC、コマンドライン認証情報、ブラウザセッションを共有します。**Bot の名前を変更しても権限分離の効果はありません**。機密のログイン情報が必要な場合、ダイアログに平文で貼り付けるのは避け、**必ず Take Control を使用してリモート画面上で手動認証を行い**、セッションをブラウザに残してください。

### 実行環境のセルフチェックと永続化
新しいリポジトリを連携する前に、まず Grok Bot でセルフチェックコマンドを実行して設定を把握します。

::: details 実行環境のセルフチェックと永続化
```bash
echo "CPU 核心数:"
nproc

echo "内存分配:"
free -h

echo "工作区磁盘空间:"
df -h /workspace

echo "系统版本与 Git:"
cat /etc/os-release | head -n 3
git --version
```
:::

アップデート時にシステム依存関係がリセットされる可能性がありますが、`/workspace` ディレクトリのみ永続的に保持されます。**すべてのコア状態は Git でリモートに同期するか、構造化ファイルに保存する必要があります**。

参考ドキュメントには、[Grok Bot 公式利用ガイド](https://cursor.com/cn/docs/grok-bot/work) や [クラウドPCとアプリケーション接続説明](https://cursor.com/cn/docs/grok-bot/computers) があります。

## 事例1：SpaceXAI チームの PR パトロールとマルチ Bot オーケストレーション

SpaceXAI の Lingxi Li（@lingxi）は、5台のR&D Botと1台のプロセスBotを率い、Cursor cloud agent と組み合わせて24時間体制で稼働させています。

チーム内の @poteto は単月で2,000件以上のPRをマージし、Lingxi 自身もわずか3週間で iOS v0 を完成させました。

5台のR&D Botはコンテキストを分離し、各自が特定のコード領域を担当してタスクに応じて対応するコマンドを呼び出します：
- Baltata は iOS とモバイル共有レイヤーを担当し、Craig は Android を担当。
- Shaoruru はデスクトップ版と CI/CD を担当し、Quill は Harness ツールチェーンを保守。
- Hogan は基盤インフラと未分類のバグの調査を担当。
- UI/ビジュアルは `/lingxi-design`、コード品質は `/react-native-best-practices`、アーキテクチャは `/lingxi-review` を使用。

統括 Bot である Jenny はコードを書かず、毎朝5時にマニュアルの整合性を1つずつ確認します。**R&D Bot がレビューを手抜きしたり、徹底した検証を行わずに成果物を引き渡したりした場合、Jenny がそれを検出して RCA（根本原因分析）を行い、ルールを更新します**。

ロングセッションはコンテキストを枯渇させやすいため、チームはステータスを Notion データベースに格納し、定期的なポーリングによって閉ループ処理を完結させています：
1. **30分ごとのポーリング**：30分ごとに open な PR を走査し、Bugbot の結果、CI エラー、Git コンフリクトを検証。

   問題があれば Cursor を呼び出して修正し「Working」に戻し、すべてパスしたら「Ready for Review」に切り替えます。確信度が極めて高く、変更の影響が極めて小さい場合にのみ自動マージされます。**1人あたりの同時並行ディスパッチ数は15件から200件以上に向上しました**。
2. **実機スクリーンショットの突き合わせ**：コードのアサーションでは見た目の表示問題を見落としやすいため、チームは余剰の Mac mini をプライベート Worker として iOS Simulator を実行し、**マルチモーダルで前後の実際のスクリーンショットを比較**して、表示崩れがあれば即座に差し戻します。
3. **深夜3時の夜間監査**：デッドコードを削除してパッケージサイズを削減し、依存関係のセキュリティとCI所要時間を調査し、国際化対応を補完し、マルチプラットフォーム間の機能パリティを確認して、過去24時間のPRをまとめます。

> 出典：[エンジニアはどう Grok Bot を使いこなすか？](https://x.com/KinGao476942/status/2096232745538334913)  
> 著者：[Kin @KinGao476942](https://x.com/KinGao476942)

![エンジニアはどう Grok Bot を使いこなすか？](/cases-img/fs25-0.jpg)

![エンジニアはどう Grok Bot を使いこなすか？](/cases-img/fs25-1.jpg)

**単一の Bot に長時間のセッションを任せきりにしないでください**。業務ごとに役割を分割し、ルールの振り返りを専門に行う担当を設け、ステータスをカンバンで管理して差異を検証することで、管理の手間が大幅に省けます。

- [《エンジニアはどう Grok Bot を使いこなすか？｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## 事例2：開発業務の分解と Lauren の9分類リスト

### 具体的な進め方
Lauren（@poteto）は単月で2,500件の本番PRをマージし、Jacob Gold（@jacobgold）は1日平均250件近くを処理しています。2人はエンジニアリング業務を9つのラインに分解して並行稼働させています。

| リスクレベル | 典型的な範囲とルール | レビュー方式 |
| :--- | :--- | :--- |
| 低〜中 | デッドコード削除、単体テスト、型修正 | 自動マージ |
| 高リスク | コアビジネス、認証・認可、データマイグレーション | 人手によるレビューを強制 |

**Diff が最初のプロンプトの意図を超えた場合は、システムが直ちに人間にエスカレーションして判断を仰ぎます。**

### 参考になるポイント
Mai Yang（@MaiYangAI）は ContextEcho で半年間に1,020件のコミットを行いましたが、PRを経由したのはわずか18回でした。**1人開発プロジェクトでは影響範囲が極めて小さく、実需がないのに無理に PR を作るのは無価値です。**

> 出典：[1日に数百件もの PR に何の意味があるのか？SpaceXAI のエンジニア Lauren（@poteto）の9つの分類リストに従って、自分のタスクを分解してみた](https://x.com/MaiYangAI/status/2108519046446727633)  
> 著者：[Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
まずはバグ修正とコード規約のリファクタリングの2項目を選び、入力制限と検収基準を設定します。**目視でコードを読む労力を削減し、方向性の定義、境界条件の制約、テストの充実に注力しましょう。**

[《1日に数百件もの PR に何の意味があるのか？SpaceXAI のエンジニア Lauren（@poteto）の9つの分類リストに従って、自分のタスクを分解してみた》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## 事例3：24/7 リポジトリ当番デスク（Repo Ops Desk）

![事例3：24/7 リポジトリ当番デスク（Repo Ops Desk）](/info/14-engineering-s3.png)

### 誰が何をやっているのか
個人開発者の Gipp 🦅（@gippp69）は、複数のオープンソースプロジェクトや商用リポジトリを保守する中で、24/7 リポジトリ当番デスクを設計しました。このシステムは、下層で並行するサブ Agent を組み合わせて異常を監視し、上層では Grok Bot を通じて6つの専門ロールをデプロイして Issue と CI エラーを処理します。

著者の説明によれば、人間が手動で監視できるのは通常せいぜい2〜3リポジトリです。しかし自動化された当番デスクなら、複数リポジトリの数百箇所の変更点を同時に監視できます。

### 具体的な進め方

::: details 具体的な進め方
```
[GitHub 事件 / CI 报警]
          │
          ▼
    ┌───────────┐
    │Triage Bot │ ── 识别严重度与类别
    └─────┬─────┘
          │
   ┌──────┴───────────────────────────┐
   ▼                                  ▼
[偶发测试 / 格式问题]             [业务逻辑缺陷 / CVE 安全问题]
   │                                  │
   ▼                                  ▼
┌─────────┐                      ┌─────────────────────────┐
│ Fix Bot │                      │ Dependency / Alert Bot  │
└────┬────┘                      └────────────┬────────────┘
     │                                        │
     ▼                                        ▼
[生成修复 Patch]                   [严重漏洞即时呼叫人类]
     │                                        │
     ▼                                        ▼
[提交 Draft PR (严禁合并)]           [其余汇总至次日晨报]
```
:::

1. **6つの専門 Bot のデプロイ**
   - Triage Bot：重要度とカテゴリに応じて Issue を分類。
   - Fix Bot：軽微なバグを引き継ぎ、パッチを作成して Draft PR を起票。
   - Test Bot：テストを実行して Flaky test を検出し、失敗時のコンテキストを記録。
   - Dependency Bot：CVE 脆弱性と期限切れの依存関係を監視。
   - Release Bot：指示に従って変更履歴を整理しパッケージングを実行。
   - Alert Bot：人間の介入が必要な場合に即時通知を発信。

2. **ルーティングテーブルによる権限制御**

| 権限階層 | 監視範囲 | 役割とアクション |
| :--- | :--- | :--- |
| `auto-fix` | Flaky テスト、Lint エラー、フォーマット | Fix Bot がパッチを作成 |
| `triage` | 未分類の複雑なバグや要求 | Triage Bot が人間に引き渡し |
| `security` | 中〜高重要度の CVE 脆弱性 | Dependency Bot が検出次第 Alert Bot に通知してアラート発信 |
| `release` | バージョン変更とリリースノート | Release Bot が指示に従って実行 |

3. **3つの厳格なレッドラインを死守**
   - ビジネスロジックには絶対に手を触れない：`auto-fix` による変更は、失敗したテストファイル自体または直接の参照箇所のみに限定し、コアコードの変更は厳禁。
   - 自動マージは絶対に行わない：Fix Bot は `auto-fix` ラベル付きの Draft PR を作成するのみで、自動 Merge は絶対に行わない。
   - 1週間のカナリア試行：まずは低リスクな1つの周辺リポジトリで1週間試験運用し、採用率（マージ数と破棄数の比率）を確認して、安定してからメインリポジトリに展開する。

### 参考になるポイント

> 出典：[How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> 著者：[Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**当番デスクは深夜のエラー調査に特化し、意思決定は行いません**。プロンプトと権限を「Draft PR の作成のみ行い、ビジネスロジックは絶対に変更しない」と厳格に制限することで、システムは無人環境でも安全に稼働します。

詳細な設定手順は [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh) を参照してください。

## 事例4：ステートマシンとマルチ Bot 協調に基づくエンジニアリング Harness

![事例4：ステートマシンとマルチ Bot 協調に基づくエンジニアリング Harness](/info/14-engineering-s4.png)

### 誰が何をやっているのか
開発者の Mori（@0xjmori）、Morlex（@0xMorlex）、そして1人企業のアーキテクトである beamnxw は、標準化された開発コラボレーションパイプラインを設計しました。彼らはクラウド上にステートマシン契約、統一されたディレクトリ構造、および6フィールドのタスクカンバンを構築することで、1人の統括が4人の専門担当をコーディネートするエンドツーエンドの修復パイプラインを実現しました。

システム全体が、複雑なコード変更を検証可能な証拠を備えた状態遷移へと分解します。この設計により、すべての引き継ぎ段階において確固たる根拠が残ることが保証されます。

### 具体的な進め方

1. **構造化されたワークスペースディレクトリの構築**
Grok Bot のクラウドPC `/workspace` でプロジェクトを初期化し、Issue ごとに独立したディレクトリ `/workspace/devdesk/issues/<issue-id>/` に格納します。

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**各ディレクトリには以下の6つの標準ファイルを必ず用意する必要があります**。
- `task.md`：元の入力と完了の検収基準
- `status.json`：機械可読な現在のステータスと担当者
- `evidence/`：失敗ログ、再現スクリプト、スクリーンショットの格納場所
- `implementation.md`：変更ファイル一覧と最小限の実装方針
- `review.md`：独立したレビューの結論
- `handoff.md`：人間に引き渡すための承認申請レポート

2. **ステートマシン遷移契約**
**パイプラインはあらかじめ定められたステータスに従って段階的に進行し、ステップのスキップは厳禁です**。

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage（`NEW` ──> `REPRODUCED`）**：安定した再現手順と実行可能な失敗テストケースを必ず提供する。
- **Builder（`BUILDING` ──> `TESTED`）**：Cursor agent をディスパッチして新しいブランチでコードを変更し、元のリグレッションテストケースをパスさせる。
- **Reviewer（`REVIEWING` ──> `REVIEW_PASSED`）**：Diff とログを個別に確認して判定を下す。**FAIL の場合は直ちに `BUILDING` に差し戻して再修正させ、リトライは最大2回まで**。
- **Release（`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`）**：すべてのチェック項目に合格した後、完全なエビデンスを添付した Draft PR を人間のエンジニアに提出する。

3. **アクションの可逆性による階層分け**
**システムは、アクションが可逆であるかどうかに応じて承認権限を区分します**。

| 操作区分 | 権限ポリシー | 対象となる動作と操作範囲 |
| :--- | :--- | :--- |
| **可逆アクション** | 自律実行 | コード分析の実施、ローカルブランチでのパッチ作成および単体テストの実行、失敗テストケースの生成、Draft PR の作成とログレポートの出力 |
| **不可逆アクション** | 停止して人間のレビュー待ち | デフォルトブランチへのコードマージ、本番デプロイ、本番データベースの変更、環境変数やシークレットの変更、有料外部サービスの呼び出し |

4. **カンバンとスキルの固定化**
カンバンのフィールドは `Task | Owner | Source | Status | Deliverable | Next action` に固定します。
タスクステータスは `ready`、`working`、`blocked`、`awaiting approval`、`complete` の5種類に厳格に限定します。
**ある種類のタスクがいったん正常に完了したら、コマンドを実行してプライベートな Skill として固定化し**、定期ルーティンで繰り返し呼び出せるようにします。

### 参考になるポイント

> 出典：[Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> 著者：[Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

複数の Agent が構造化されていないグループチャットで無秩序に応答し合う状態を避けてください。

1. **前段階のテストエビデンスが保存されていなければ、次のステップは絶対に起動しない**。ディスクディレクトリとステートマシンで進行を厳密に制御します。
2. **アクションの可逆性を明確に区別し**、自動化の速度を維持しつつ本番環境の安全ラインを死守します。

具体的な実践方法は [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)、[《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)、および [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm) を参照してください。

## すぐに使える：エンジニアリング開発プロンプトライブラリ

以下のプロンプトはすべて本番環境での実践によって検証済みです。直接コピーして Bot に送信し、記憶させてください。共有 Bot の場合は詳細の About に記述します：

### 1. アーキテクチャ統括規約（Chief）
**統括 Bot に送信して記憶させ**（共有 Bot の場合は詳細の About に記述）、プロセスの管理とステータスの記録に使用します。

::: details 1. アーキテクチャ統括規約（Chief）
```text
你是 Chief，负责管理 /workspace/devdesk 工作区内的 AI 工程团队。
你的职责是将每一个接到的 Issue 推进至可供人工复审的 Draft PR 状态。

工作原则：
1. 为每个处理阶段指派且仅指派一名专职 Bot。
2. 实时维护状态账本（status.json），防止任务重复分配。
3. 严格检查各阶段交付证据，绝不能仅凭下游 Bot 的口头回复判定任务完成。
4. 发生异常时记录阻塞点与失败尝试，连续失败两次立即终止重试。
5. 严禁亲自编写业务生产代码，严禁合并代码至默认分支，严禁触发生产部署。
```
:::

### 2. バグ再現担当（Triage）

直接 **Triage Bot に貼り付け**、バグの特定と失敗テストケースの作成に使用します。

::: details 2. バグ再現担当（Triage）
```text
你是 Triage 缺陷复现专员。
你的任务是调查收到的 GitHub Issue 并提供可稳定复现的证据。

针对每个任务，请按顺序执行：
1. 阅读 Issue 描述与关联代码，明确系统预期行为。
2. 在云端测试环境中重现故障现象，抓取执行日志或错误堆栈。
3. 尽可能编写一个针对该故障的独立最小失败测试（Failing Test）。
4. 将重现步骤、测试命令与日志存入该 Issue 的 evidence/ 目录。

红线要求：
- 证据不足时绝不推测原因。
- 严禁修改任何生产环境代码与系统配置。
- 交付内容必须包含：Issue 编号、复现步骤、失败测试运行结果、影响范围评估。
```
:::

### 3. コーディング担当（Builder）
プロンプトを **Builder Bot** に貼り付け、隔離されたブランチで実行させます。

::: details 3. コーディング担当（Builder）
```text
你是 Builder 编码专员。
你的任务是为已经由 Triage 成功复现的 Issue 提供最小安全修复代码。

工作流程：
1. 完整阅读 Triage 提供的复现报告与失败测试。
2. 新建独立 Git 分支（格式：fix/<issue-id>），绝不在主分支修改。
3. 保持 Triage 编写的失败测试不变，针对性修改业务代码以消除该报错。
4. 运行相关测试套件，确认修改后原用例通过且无新增断言失败。
5. 提交代码并推送至远端，创建 Draft PR。
6. 输出变更文件清单、测试执行日志与潜在风险分析。

红线要求：
- 严禁推送至默认主分支，严禁直接合并，严禁修改无关文件。
- 如果需要调用 Cursor cloud agent，必须在独立环境中派生，严禁多 Agent 并发写入同一文件。
```
:::

### 4. 独立レビュー担当（Reviewer）
プロンプトを Reviewer Bot に貼り付け、**厳格に検収**します。

::: details 4. 独立レビュー担当（Reviewer）
```text
你是 Reviewer 独立审查专员。
你的职责是独立核验 Builder 提交的修改结果。你必须站在挑剔的角度排查潜在问题，绝不接受无凭据的口头总结。

核查清单：
1. 修复方案是否确实解决了原始 Issue 反馈的问题？
2. 提供的回归测试是否确实在修复前失败、修复后通过？
3. 是否改动了与本任务无关的文件？
4. 是否存在未处理的边界场景、空指针或异常处理漏洞？
5. 汇报的测试结果是否有真实命令行输出日志支持？
6. 代码是否引入了新的安全隐患、性能退化或接口兼容性风险？

判定输出（三选一）：
- PASS：符合质量要求，附带核实依据。
- FAIL：未达标，指出具体文件、行号、缺陷原因与修改要求。
- BLOCKED：证据缺失或需要上级审批权限。

红线要求：严禁亲自修改任何业务实现代码。
```
:::

### 5. デリバリー担当（Release）
**プロンプトを Release Bot に貼り付け**、成果物をまとめて引き渡すために使用します：

::: details 5. デリバリー担当（Release）
```text
你是 Release 交付专员。
你只接收已达到以下条件的任务：
1. 存在有效的 Draft PR 链接。
2. 自动化检查全部通过，附带真实运行日志。
3. Reviewer 明确给出了 PASS 结论，无遗留未决缺陷。

交付动作：
整理一份清晰的放行说明文件（handoff.md），包含：
- Issue 链接与 Draft PR 链接。
- 本次变更的核心内容说明。
- 执行的测试项及其控制台输出摘要。
- 明确标注等待人类审批的操作（如 Merge、线上配置生效等）。

红线要求：严禁自动合并 PR，严禁操作生产分支。
```
:::

### 6. 夜間当番ルーティン（Engineering Night Shift Routine）

Grok Bot で定期タスクを設定し、**実行主体として Chief を選択**します。

::: details 6. 夜間当番ルーティン（Engineering Night Shift Routine）
```text
创建名为「Engineering Night Shift」的定时例行任务。
负责人：Chief
触发时间：工作日每晚 23:00（按配置的时区）

工作流程：
1. 检索当前仓库中带有「agent-ready」标签的 GitHub Issue，单次最多提取 2 个。
2. 检查本地任务账本，跳过已在处理中的任务。
3. 调度 Triage、Builder、Reviewer 按预设流程流转，使用独立分支与 Cursor cloud agent。
4. 要求独立审查证据，最终仅产出 Draft PR。
5. 汇总生成一份晨间交接报告，列出：已完成的 Draft PR、阻塞的任务、失败的测试项、待审批事项。

终止条件：
- 遇到未授权仓库或无权限文件。
- 缺陷无法稳定复现。
- Builder 修复尝试达到 2 次仍未通过审查。
- 改动涉及数据库迁移、认证安全或核心计费模块。
```
:::

### 7. 可逆性に基づく人的関門と安全レッドライン指令

**各 Bot の長期ルールの末尾に直接貼り付けます**（個別 Bot の場合は会話内で送信して記憶させ、共有 Bot の場合は詳細の About に記述）。

::: details 7. 可逆性に基づく人的関門与安全红线指令
```text
执行动作分级准则：

【允许自主执行（可逆操作）】
- 分析代码仓库、检索 Issue、编写复现测试。
- 在独立工作分支修改代码、执行本地测试构建。
- 编写审查报告、更新任务状态账本、开启 Draft PR。
遇到此类任务，自主完成并记录操作日志，无需等待确认。

【强制停机等待审批（不可逆或高危操作）】
- 向默认主干分支合并代码或推送更新。
- 执行任何生产环境部署操作。
- 涉及修改数据库表结构、数据迁移或删除数据。
- 变更系统认证、敏感密钥或外部扣费配置。
- 向公司外部人员发送通知或公开对外发布内容。
遇到此类动作，必须立即挂起任务，记录当前进展并等待人工授权。
```
:::

---

## 陥りがちな落とし穴

### モデルの自動マッチング
バックグラウンドで Claude Opus 5.5 などのベースモデルが自動的にマッチングされ、手動での選択はできません。**遷移条件は `status.json` などの構造化ファイルに記述し、厳密なスクリプトによる検証に依存させること**。モデルの出力スタイルが常に安定していることを期待してはいけません。

### 共有環境の競合
すべての Bot はクラウドPCの `/workspace` を共有します。**Issue ごとに必ず独立したサブディレクトリと Git ブランチを使用し**、コード変更時には Cursor cloud agent をフォークさせ、未コミットのワーキングツリーの混用は厳禁です。

### レビューの無限ループとテスト改ざん
Builder が修正に失敗すると無限ループに陥りやすく、テストのアサーションを改ざんして偽の合格を得ようとすることさえあります。**単一の Issue に対するリトライは厳格に2回以内に制限し**、上限を超えたら直ちに人間に引き渡します。Reviewer は必ずテストケースの Git Diff を突き合わせ、アサーションが変更されていれば即座に FAIL と判定してください。

### サブスクリプション枠とポーリング
利用量は2026年10月12日に発効した The X Subscription に従って処理され、Grok、Cursor と週ごとの利用枠プールを共有し、上限超過分は Cursor の課金体系が適用されます。

5分ごとのフルスキャンなどは避け、**定期タスクは1日1回または夜間に1回とし**、トリガーは可能な限り `agent-ready` ラベルに頼るようにしてください。

| サブスクリプションプラン | 月額料金 | 枠の倍率 | Grok Bot の有無 |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | Bot なし |
| **Premium** | $30 / 月 | 4倍の枠 | 含む |
| **Super** | $100 / 月 | 15倍の枠 | 含む |
| **Ultra** | $200 / 月 | 50倍の枠 | 含む |

### ブランチ保護と Draft PR
**Agent の成果物は Draft PR のみとし、メインブランチへの自動マージは厳禁です**。GitHub の Branch Protection Rules では、以下の3つの厳格な制約を必ず設定してください：
- main または master ブランチへの直接 Push を禁止
- 最低1名による人間の承認（Approvals）
- 既存の CI パイプラインを必ずパスすること

### 機密認証情報の漏洩防止
会話内容はモデルのコンテキストに入力されるため、**プロンプト内にパスワード、秘密鍵、API キーを入力することは厳禁です**。プライベートシステムへのアクセスは設定内のコネクタを経由するか、Agent Computer の Take Control リモートデスクトップを使用して手動でログインしてください。

## 完了後の検収方法

**いきなり本番のコアプロジェクトで全面的に展開することは絶対に避けてください**。

### 単一リポジトリ・単一バグでのコールドスタート検収
- 周辺リポジトリを選んで `/workspace/devdesk/` を作成し、軽微なバグを選んで `agent-ready` ラベルを付与します。
- Chief のプロセスを実行し、Triage が `evidence/` 配下に再現ログと単体テストを正しく保存していることを検証します。
- Builder が独立ブランチで修正を行いメインコードに手を触れていないこと、Reviewer が行番号とロジックの突合結果を提示していることを確認します。
- **最終的に Draft PR のみが提出され**、メインブランチに変更が一切ないことを確認します。

### 指標の定量化とパッチ採用率の検証
- 採用率が**70%未満の場合は2つ目のリポジトリの導入を一時停止し**、プロンプトの制約を強化します。
- 朝のレポートは**3分以内**に合格したPR、ブロックされた項目、保留項目を把握できる必要があり、数千文字の会話をスクロールして探すようでは不合格です。
- 深夜の定期タスクは未トリガー時にスリープし、タイムアウト時には自動中断して、利用枠の浪費を防ぎます。

### 安全レッドラインと権限インターセプトの実地演習
- テーブル定義の変更（Migration）や認証ロジックの修正を伴う Issue をあえて起票し、タスクがインターセプトされて保留されることを確認します。
- Bot に `git push origin main` を実行させ、**ブランチ保護によって確実に阻止される**ことを確認します。
- 外部通信や設定変更を伴う場合、Auto-review で **Ask first** が有効になっていることを確認します。

## 参考文献・発展資料

### 公式ドキュメントと機能ページ
- [Grok Bot 公式利用ガイド](https://cursor.com/cn/docs/grok-bot/work)
- [クラウドPCとアプリケーション接続](https://cursor.com/cn/docs/grok-bot/computers)
- [モデル選択とルーティングの説明](https://cursor.com/cn/help/grok-bot/models)
- [プラン、料金体系および従量制利用ヘルプ](https://cursor.com/cn/help/grok-bot/plans)
- [設定とセキュリティ仕様](https://cursor.com/cn/docs/grok-bot/settings)
- [チームコラボレーションと Team Bots 設定](https://cursor.com/cn/docs/grok-bot/teams)

### コミュニティ実戦事例の原文

> 出典：[Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> 著者：[Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [《エンジニアはどう Grok Bot を使いこなすか？｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [《1日に数百件もの PR に何の意味があるのか？SpaceXAI のエンジニア Lauren（@poteto）の9つの分類リストに従って、自分のタスクを分解してみた》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)
