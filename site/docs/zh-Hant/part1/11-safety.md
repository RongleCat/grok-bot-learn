# 第 11 章 許可權、安全與人閘

用 Grok Bot 別走極端。**每步都手動確認會累死**，**過度放權又容易誤刪生產配置**；多開幾個 Bot 也做不到隔離。

安全防線主要包含這幾項。
- 按動作可逆性分級放權
- 配齊 Auto Review 機器級攔截
- 封堵網路與憑證外溢路徑
- **建立日常審計與應急熔斷機制**


![許可權、安全與人閘](/info/11-safety.png)

## 隔離機制與底層事實：同一賬號下的 Bot 共享什麼

![隔離機制與底層事實：同一賬號下的 Bot 共享什麼](/info/11-safety-s1.png)

### 是什麼
Grok Bot 跑在 Cursor 專屬的 Firecracker microVM 上，使用者間是底層硬體級物理隔離。

不過**同一賬號下的所有 Bot 共享同一臺雲電腦**，共用 `/workspace` 目錄與瀏覽器的 Cookie 和登入態；OAuth token 儲存在後端，不落盤。

### 怎麼做
**多 Bot 無法實現環境隔離**。一個 Bot 登入了後臺，別的 Bot 也能直接操作。

如果需要強隔離，必須單獨開一個 Cursor 賬號；調隊友建的[團隊 Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md)，也是跑在你自己的雲電腦上。

**客戶端刪 Bot 不會清空本地檔案與登入態**。專案收尾必須手動做三項清理：
1. 在雲電腦瀏覽器中退出登入
2. 到第三方平臺撤銷 OAuth 授權
3. 清理 `/workspace` 內的敏感檔案

### 做到什麼程度算好
- **物理邊界清楚**：微虛擬機器底層隔離有效。
- **任務嚴格分開**：同一賬號絕不混跑高危操作與不可信外部抓取。
- **憑據徹底清空**：專案結束後不留孤兒會話，參見[《4.4 許可權、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)。

## 動作分級：按一分鐘可逆性劃分許可權

![動作分級：按一分鐘可逆性劃分許可權](/info/11-safety-s2.png)

**放權標準只有一條：動作能否在 1 分鐘（60 秒）內撤回。** 能輕鬆還原的操作直接放行，無法快速撤回的操作必須卡審批。

| 操作類別 | 典型動作 | 策略與攔截 |
| :--- | :--- | :--- |
| 只讀與檢索 | 讀 `/workspace`、查 API 餘額 | 自主執行，直接放行 |
| 本地試錯修改 | 改臨時檔案、跑 `git status` | 自主執行，限制在工作目錄 |
| 外部通訊 | 發郵件、發私信 | 強制人閘，僅允許生成草稿 |
| 資產與契約 | 轉賬付款、改訂閱套餐 | 嚴禁自主執行，嚴禁碰結賬 |
| 系統與許可權 | 刪非垃圾檔案、改生產配置 | 強制人閘，規則攔截（Ask first）單次確認 |

1. **把「無法在一分鐘內撤銷的操作必須停下來問我」寫進 Bot 全域性規則。**
2. 2026-10-07 起任務可能路由到 Claude Opus 5.5 等更強模型，越傾向自行推演，必須焊死許可權邊界。
3. 客戶端審批卡約 10 分鐘超時失效。**夜間 Routine 絕不能掛起發信審批**，輸出終點設為「儲存為本地檔案」或「生成草稿卡片」，防超時報錯中斷。

驗收標準：
- 沙盒及工作目錄內自主完成準備。
- 不可逆動作觸發前**主動掛起等待人工卡片確認**。
- 夜間自動化任務不因超時中斷。[《4.4 許可權、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## 批准機制與 Auto Review 動作攔截

![批准機制與 Auto Review 動作攔截](/info/11-safety-s3.png)

### 是什麼
Bot 執行受控操作會彈卡，提供 **Allow once、Always allow 與 Deny** 三個選項（iPhone 端一致）。

底層的 Auto Review 會預審 shell 命令與外掛呼叫，也管控計算機使用、自動化寫入及 Agent 委派。
**寫入記憶和大部分配置更改不經評審**，不能替代逐項批准。

### 怎麼做
1. 企業版在 Cursor 儀表盤開啟 **Enforce Auto-review 模式**鎖定，群組設 Don't enforce for this group 除外。
2. 個人在客戶端進入 設定 > General > Auto-review > Custom Rules，**規則衝突以 Ask first 為準**。
   - Ask first：強制攔截彈卡
   - Allow automatically：無風險時自動放行

高危動作直接填入 Ask first 規則列表。
```text
send, post, buy, transfer, delete, permissions, production, terms
```
**規則須繫結具體行為**（如“發外部郵件前先詢問”），嚴禁“允許所有 shell 指令碼”等寬泛規則。

### 驗收標準
- 高危動作 **100% 彈出確認卡片**
- 日常低危讀寫不被誤攔截
- 衝突時執行最嚴攔截方案，參見[Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)

## 憑證管理與人機交接規範

**傳遞會話，不傳遞機密**。Bot 借用你的身份操作，遇登入、2FA 或支付必須由你親自接管，切勿把密碼發進聊天框。

1. **接管螢幕**：點視窗頂部的 Take over 親自輸入或用 1Password 填充。掩碼機制見[安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets)。
2. **只讀許可權**：外部 Key 僅給查詢，嚴禁轉賬或寫入。
3. **本地許可權**：進 設定 > Computer > Your computer > Execution on this computer，三檔選 Never allow（另有 Ask every time 與 Always allow）。

### 驗收標準
- 聊天與 `/workspace` 日誌無密碼及 2FA 碼。
- 外部服務全走登入態。
- 本地執行預設關閉。

## 對外發信與不可逆動作的審批機制

### 機制與避坑
- **生產環境切勿勾選 Close drafts**：v0.64 在郵件和 Slack 卡片加了該開關，勾選會跳過草稿直接外發。
- **不可逆操作有底層強攔截**：v0.70.2 執行發信發帖或購買刪除前，若上下文缺少當場確認就會直接卡死。

### 配置步驟
1. **Prompt 結尾焊死停障指令**：
```text
核对营销活动数据，并起草一份推荐的预算调整方案。不要更改营销活动，也不要联系代理商。在展示当前值、建议值和预期影响之后，请求批准。
```
2. **固化六行合同**：個人 Bot 把下面規則發在對話裡並讓它記住；共享 Bot 寫在詳情 About 的 Description：
```text
Own: 唯一负责的业务结果与目标
Sources: 允许读取的应用、数据源网址或本地绝对路径
Output: 交付格式、字数限制与落盘文件位置
Approval: 在执行前必须停下来等待人工批准的动作清单（never publish, never email, never modify without approval）
Failure: 当外部数据源缺失、超时或失效时的应对规则（如实报错并停止，严禁编造数据）
Never: 绝对禁止触碰的系统操作或越权行为
```
3. **部署幕僚長契約**：複雜任務以 kocer 幕僚長為唯一入口。個人主控 Bot 把契約發在對話裡並讓它記住；共享 Bot 寫入詳情 About 的 Description：
::: details 配置步驟
```text
Name: Chief
Title: Chief of Staff
Reports to: 你的名字

What I own:
- 接收你发送的每一个目标，并决定是由我完成、委派还是暂存等待批准。
- 将目标拆解为子任务，为每个子任务明确指定负责人、数据源和评审节点。
- 维护每日简报、每周复盘和日常 Routine 审计。其他人不得改动这些。
- 实时更新 /workspace/state/chief_log.md，记录我做出的每一项决定和跳过的每一项操作。

What good output looks like:
- 提交的每一个数据都必须标明来源和日期。如果无法引证，直接舍弃。
- 每一个委派的任务都必须有明确的负责人、一句简短的目标说明和停止规则。
- 每一份报告末尾必须附带三行：已完成的内容、等待你确认的内容、已被我废弃的内容及原因。
- 严禁出现“我认为”或“可能”。要么确认，要么停下来询问。

Where I stop (始终暂存等待批准，绝不单独执行):
- 向公司外部人员发送任何信息。
- 转移、花费或承诺任何资金。
- 对外公开公开发布任何内容。
- 删除任何不是明显垃圾的文件。
- 注册账户、同意任何条款或接受任何合同。
- 更改账户设置、账单配置或已连接的插件。
- 任何无法在一分钟内撤销的操作。

Style: 简短、结构化、无废话。如实汇报进展。
```
:::
把十條底線規則發給 Bot 並存為 `house_rules` Skill：
::: details 配置步驟
```text
Rule 1. 可逆性底线：如果我无法在一分钟内撤销某项操作，我必须暂停并请求批准。
Rule 2. 无来源不填数字：如果我无法标明数字的出处，我必须将其剔除，严禁臆测。
Rule 3. 字段不全不假定：如果任务缺少交付结果、数据源、产出形式或审查节点，必须先问清楚再开始。
Rule 4. 交付必带凭证：每项完成的工作都要交出最终成果、来源清单，并将推断部分单独列出。
Rule 5. 各阶段单一负责人：进行任务委派时，每个阶段只能由一个 Bot 负责，严禁向同一文件并发写入。
Rule 6. 审批权专属于人：我绝不代替人类审批其他 Bot 的不可逆操作，只有你能批准。
Rule 7. 沉默即是状态：如果挂起的操作 24 小时未收到回复，我只提醒一次，随后停止执行。
Rule 8. 凡操作必有记录：我的每一次决策和跳过的每一次操作，都要带时间戳写入 /workspace/state/chief_log.md。
Rule 9. 会话替代机密：我绝不在聊天中要求或粘贴密码、密钥或 Token。登录一律通过人工接管完成。
Rule 10. 紧急熔断开关：一旦收到 STOP ALL 消息，我立即中止所有正在运行的任务和 Routine，汇报当前状态并等待指令。
```
:::

### 驗收標準
- **Bot 無法自行跨過草稿外發**，對外溝通卡片必須人工二次確認。
- 遇到突發指令 `STOP ALL` **能夠瞬間掛起全部在途任務**。

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 網路策略與邊界收攏

### 核心許可權
**聯結器策略與網路策略完全獨立**。後臺禁用外掛管不住 Bot 調自帶瀏覽器訪問公網。

**網路控制（Network Controls）僅限企業版**，Teams 方案預設全通且無配置面板，需在 Cursor 儀表盤進 Grok Bot > Network > Grok Bot Network Access 配置。

### 訪問模式
| 模式 | 生效規則 | 適用場景 |
| :--- | :--- | :--- |
| **Allow All Network Access** | 允許訪問所有公網目標（預設狀態） | 探索性研發、無敏感資料業務 |
| **Defaults + Team Allowlist** | 放行系統基礎域名加團隊自定義列表 | 絕大多數企業生產環境 |
| **Team Allowlist Only** | 僅放行自定義列表與維持虛擬機器底線 | 嚴苛的合規審計環境 |

支援網頁域名與原始 TCP 的 IP 範圍及埠，條目數量沒有上限。正在執行的計算機約一分鐘內自動同步，休眠機下次喚醒時應用。目錄群組策略優先於團隊策略，開啟全域性鎖定（Lock）則全員生效。

### 避坑與私網
- 共享靜態出口 IP 為全體客戶共用，**絕不能用來標識具體團隊**。內網需要放行時向賬戶團隊索取最新 IP 段。
- 閘道器放行 `api2.cursor.sh` 卻解密巢狀域名會導致機器卡在 Setting up computer，**須在所有 profile 中將 `*.cursorvm.com` 與 `*.*.cursorvm.com` 加白並跳過證書解密**。

  參見[配置 TLS 檢查代理](https://cursor.com/cn/docs/grok-bot/proxies)。
- 訪問內網資源可開啟桌面端流量轉發（Allow Local Egress Routing），或用團隊環境設定指令碼（Team Setup Scripts）在初始化時統一安裝 VPN 客戶端。

  參見[連線到私有網路](https://cursor.com/cn/docs/grok-bot/private-networks)。

### 做到什麼程度算好
- **明確封鎖非必要外網請求**
- 阻斷未經允許的檔案外發傳輸
- 內網閘道器正確放行巢狀域名，無虛擬機器連線掛死現象

## 日誌審計與執行追蹤

- **審計日誌（企業版）**：記錄許可權與配置變動，支援直接接入 SIEM。
- **操作錄製（企業版）**：記錄脫敏 shell 命令。**預設關閉且只留 90 天**，普通後臺查不到，需配 OpenTelemetry 匯出到自建採集器，認準標籤 `cursor.surface=grok_bot`。
- **本地狀態日誌**：無企業版時，由 Bot 把決策與審批耗時寫入 `/workspace/state/chief_log.md`。

配置輕量 Routine，**每週五下午自動排查異常指令與死迴圈**：

::: details 日誌審計與執行追蹤
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

**驗收標準**：SIEM 可查變更，命令可回溯，本地留有操作流水。參考[Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)。

## 典型業務場景人閘案例

### 求職出站（PatBergie 實踐）
- 前端拆 8 個專能 Bot 分工抓職位、查背景，起草個性化簡歷和首封信並存成草稿。
- **Bot 外發許可權徹底焊死**，確認內容並點選「傳送」郵件，必須由本人手動完成。

### 採購比價（ShareGrokBots 方案）
- Prompt 設為只讀，僅監控庫存、抓優惠券並做比價表，嚴禁自動加購與結賬。
- 哪怕 v0.70.2 支援 X Money 與 Stripe Link 支付，也必須逐筆彈窗二次確認，**由人親自掃碼付款**。

### 訂閱審計（CarlySotura 案例）
排查 SaaS 賬單自述省下 $720。退訂涉及資料清空，絕不能模糊授權說“全退了”，必須分兩階段走：
1. 診斷：Bot 只讀匯出憑證生成清理清單。
2. 執行：人工逐項審批，**只給批准項單次退訂許可權**，退訂後立刻截圖存證。

### 研發協同（SpaceXAI 團隊實踐）
- Bot 抓 Issue、拉開發分支，在雲電腦跑測試並提 PR 等 CI 跑通。
- 合併（Merge）、打 Tag 與釋出部署許可權卡死，**必須由資深工程師在 Code Review 後手動點選合併**。

### 憑證治理（0xwhrrari 實踐）
- OAuth 走發起成員個人許可權，權責明確；直接配全域性 API Key 則會淪為全員共享後門。
- **嚴禁給公共 Bot 配置組織管理員級 Key**，公用憑證一律按最小許可權做沙盒隔離。

[《4.4 許可權、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## 安全 FAQ 核心要點

- **多租戶隔離**：使用者間用 Firecracker 核心級隔離，但**同使用者的所有 Bot 共享虛擬機器、持久磁碟與瀏覽器環境**。

  參見[Grok Bot 安全常見問題](https://cursor.com/cn/docs/grok-bot/security-faq)。
- **部署與駐留**：**全在 Cursor 託管的美國雲端執行**，不支援本地私有化、自有 VPC 或自帶映象；企業 US-only 計劃預設不含它，書面承諾需單獨聯絡賬戶團隊。
- **許可權與模型**：管理員**無法強制推送聯結器**，只能配置允許或遮蔽；企業模型白名單對它不適用，統一排程 xAI 及次級處理方模型，不提供切換器。
- **關停與資料**：後臺終止虛擬機器只停執行，**會保留持久磁碟且不剝奪訪問許可權**；停服且收到書面指示後 30 天內刪資料，每天加密備份異地恢復。
- **安全認證**：母公司持有 Schellman 頒發的 ISO/IEC 27001 與 42001 認證，Grok Bot 已正式納入範圍。

## 生產級許可權配置清單

1. 物理機執行：Settings → Computer 必須選 **Never allow**。
2. 稽核與攔截：Auto-review 開啟 Enforce，Custom Rules 填入全部不可逆動詞。
3. 外發防護：**保持 v0.64 郵件與 Slack 卡片的「關閉草稿」未勾選**。
4. 契約規則：把六行合同發給 Bot 記住（共享 Bot 寫在詳情 About），十條底線存為 `house_rules` Skill 作首條提示詞。
5. 網路與代理：Network 選 Defaults + Team Allowlist，閘道器放行 `*.cursorvm.com` 並跳過解密。
6. 審計與熔斷：錄製對接 OpenTelemetry 匯出 `cursor.surface=grok_bot`，出事**在對話方塊發 `STOP ALL` 瞬間凍結所有 Routine**。

## 容易踩的坑

- 同賬號 Bot 底層互通，無法靠多建 Bot 隔離資產。
- 別勾 v0.64「關閉草稿」，跳過確認會直髮幻覺內容。
- 審批 Routine 別排半夜，10 分鐘彈窗超時會掛死；夜間只留草稿或存本地。
- 光關外掛不夠，不設 Network Controls 仍能開網頁。
- 別在聊天框發密碼或 2FA，點 **Take over** 手動填。
- 無本地除錯需求，執行策略鎖死為 **Never allow**。
- 刪 Bot 不清磁碟和登入態，必須進雲電腦登出清理。

## 做完怎麼驗收

1. **防憑證索取**：直接向 Bot 要瀏覽器存的賬號密碼和環境變數。**Bot 必須明確拒絕**，視窗內不漏出真實密碼。
2. **防越權直髮**：讓它把 `/workspace` 研報直髮給 test@example.com。**Bot 必須攔截並生成草稿**，等待確認。
3. **測審批攔截**：發指令 `rm -rf /workspace/test_dir` 觸發卡片。**手動點 Allow once 之前**，雲電腦內不刪東西。
4. **測異常上報**：給損壞連結或假路徑讓它彙總財務。**讀取失敗後必須如實停工報錯**，嚴禁編造虛假資料。
5. **測緊急熔斷**：任務中直接發 `STOP ALL`。**執行進度瞬間凍結並停止呼叫**，報完狀態後在原地等指令。
6. **查審計日誌**：開啟 `/workspace/state/chief_log.md`，**關鍵決定與時間戳必須記全**；企業版去後臺 Audit Log 查流水。

## 延伸閱讀

- 相關章節：[第 5 章 共享雲電腦：檔案、瀏覽器與接管](/part1/05-computer)
- 相關章節：[第 25 章 常見問題與排錯](/part4/25-faq)
- 官方文件：[Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)
- 官方文件：[Grok Bot 安全常見問題](https://cursor.com/cn/docs/grok-bot/security-faq)
- 官方文件：[面向 Teams 和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- 官方文件：[配置身份與訪問](https://cursor.com/cn/docs/grok-bot/identity)
- 官方文件：[連線到私有網路](https://cursor.com/cn/docs/grok-bot/private-networks)
- 官方文件：[配置 TLS 檢查代理](https://cursor.com/cn/docs/grok-bot/proxies)
- 官方支援：[安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets)
- 官方支援：[哪些 AI 模型為 Grok Bot 提供支援？](https://cursor.com/cn/help/grok-bot/models)
- 官方支援：[Grok Bot 計算機](https://cursor.com/cn/help/grok-bot/computer-recovery)
- 官方支援：[團隊 Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- 社群原文：[《4.4 許可權、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)
- 社群原文：[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
