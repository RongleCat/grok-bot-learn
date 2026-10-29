# 第 23 章 團隊版與企業落地

給團隊部署 Grok Bot，常見卡點主要是這幾項。

- 閘道器在握手階段攔截，導致**雲端電腦連不上**。
- Linux 虛機沒裝 MDM 客戶端，會被企業 IdP 判為不受信任裝置。
- 存在憑據洩漏與內網穿透風險，也缺客戶端靜默分發手段。

按流程配好 **SSO 與安全閘道器豁免**，打通私網訪問，就能搞定批次生命週期管理。


![團隊版與企業落地](/info/23-enterprise.png)

## 團隊版與企業版管理控制：架構與能力邊界

![團隊版與企業版管理控制：架構與能力邊界](/info/23-enterprise-s1.png)

### 是什麼

**每位使用者獨享一臺雲端 Firecracker microVM**，本地發指令審批，程式碼與瀏覽器在雲端跑。

提醒個坑，**名下所有 Bot 共享這臺虛機**，檔案和登入態完全互通。

2026-10-12 The X Subscription 方案劃分了兩版許可權：

- **團隊版**：全員預設開啟，走共享靜態出口 IP，帶基礎審計與團隊規則。
- **企業版**：支援按組授權與 SCIM 2.0，能用 sudo 和網路白名單，帶操作錄製與 OpenTelemetry 匯出（打 `cursor.surface=grok_bot` 標籤）。

文件見 [面向 Teams 和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)。

### 怎麼做

日常配置都在 [Cursor 儀表盤的 Grok Bot 頁面](https://cursor.com/dashboard/bot) 處理，主要分四步走。

1. 劃分許可權與基礎開關
- 灰度期點 **Manage Group Access** 勾選試點；不用雲端編碼就關掉 Cloud Agents；公開模板共享保持關閉防外洩。
- **本地執行建議設為 Never allow**，同時關閉本地出口路由防繞道轉發。
- 側邊欄 Bot 在 Auto-add 列選 All team 或指定群組固定。

2. 配置審批鎖與規則
- 開啟 **Enforce Auto-review 模式**，成員在客戶端就沒法自關審查。
- 生產部署或對外發郵件等高危操作設為 Ask first，限定只讀設為 Allow automatically。
- **團隊規則與個人規則衝突時，系統強制以 Ask first 為準**。

3. 設定網路與金鑰
- 網路選僅團隊允許列表或加預設值，填入域名與 IP 段；防系統篡改可關閉預設開啟的 sudo。
- **Team Secrets 團隊最多新增 100 條**，單條上限 32 KB，總容量上限 96 KB，儲存後不顯示明文。
- 金鑰變數名禁止使用 `PATH`、`HOME` 及 `SAND_` 或 `LD_` 開頭的系統保留名。

4. 配置群組級策略
- 從 [Members > Groups](https://cursor.com/dashboard/members?subtab=groups) 進群組，**配置原則是隻能放寬、不能更嚴**。
- 勾選 Don't enforce for this group 可解開自動審查鎖。
- 網路策略是特例，群組會直接覆蓋團隊；如果成員跨多個群組，網路按最嚴執行，許可權按最寬生效。

### 做到什麼程度算好

- 儀表盤中明確區分了試點群組與未授權群組，非授權人員在客戶端無法啟用 Bot。
- 團隊規則與 Auto-review 規則已鎖定，成員在客戶端設定頁面能看到團隊規則，但編輯與刪除按鈕處於禁用狀態。
- 高危操作（外部通訊、檔案破壞、特權命令）百分之百觸發審批攔截。

---

## 身份與 SSO：打通全員訪問與相容裝置信任

### 是什麼

Grok Bot 沿用 Cursor 賬號體系，**不用在 IdP 中單獨建應用**。參考文件：[配置身份與訪問](https://cursor.com/cn/docs/grok-bot/identity)。

Bot 跑在雲端 Linux 虛機，未裝 MDM，無法滿足 FastPass 或 Hybrid Join。**切記不能全域性關閉裝置合規**，要在攔截規則前為目標群組配置放行策略。

### 怎麼做

- **Okta 擴大分配**：進 Cursor 應用的 **Assignments** > **Assign to Groups** 勾選業務群組；啟用 SCIM 時同步分配並推送（Push Groups）。

  **SAML SSO 與 SCIM 必須同時分配**，漏配 SSO 登入會被攔截。
- **Entra ID 擴大分配**：在 Cursor 應用的 **Users and groups** 點 **Add user/group** 新增群組（需 P1/P2 許可，不支援巢狀組）；預配應用同步分配相同群組。
- **Okta 放行 Linux**：在認證策略攔截規則前新建 `Grok Bot computer (Linux)`。

  使用者限 Cursor 組，**Device platform 選 Other Desktop**（無獨立 Linux 項），Device state 選 Any；驗證選 Password + Another factor，不勾抗釣魚限制。
- **Entra ID 放行 Linux**：新建高優先順序策略，指定 Cursor 組和目標應用；Device platforms 包含 Linux，排除 Windows 與 macOS；Grant 勾 Require multifactor authentication；**原有合規策略中必須排除該群組或 Linux 平臺**。

### 做到什麼程度算好

- 業務使用者用企業 SSO 登入桌面端，不報 `User is not assigned to this application`。
- 在 Bot 瀏覽器中憑密碼加二次驗證能訪問內網，不彈 FastPass 或裝置不合規攔截。
- **員工在個人電腦上訪問，原有的 FastPass 和裝置合規仍嚴格生效**。

## 私有網路接入：桌面路由與 Team Setup 指令碼自動化

![私有網路接入：桌面路由與 Team Setup 指令碼自動化](/info/23-enterprise-s3.png)

### 是什麼

Grok Bot 跑在雲端，**訪問內網必須打通私網**。

- 桌面端路由：適合臨時除錯。在客戶端開啟 `Settings > Computer > Route traffic through this computer`，流量走本機網絡卡，管理員可在後臺一鍵禁用。
- Team Setup 安裝客戶端：常態化訪問且**僅限企業版**。由 IT 統一維護指令碼，Bot 啟動或重新整理時自動拉起並加入內網。

詳情見 [連線到私有網路](https://cursor.com/cn/docs/grok-bot/private-networks)。

### 怎麼做

團隊環境設定指令碼在儀表盤 **Bot Computers** 下，以 `sudo` 普通使用者身份在 Debian Linux 虛擬機器中跑。**指令碼開機時執行且每天約週期重新整理一次，超時上限 30 分鐘**。
- `check` 退出碼為 0 就跳過安裝，裝完會再次執行 `check` 驗證。
- **執行失敗不阻塞電腦啟動**，會在下次週期重新整理時重試。

#### 接入 Tailscale 組網方案

1. 開啟 **Team Secrets**，新增 Tailscale 認證金鑰 `TS_AUTHKEY`（值為 `tskey-auth-...`），並在 Tailscale 控制檯繫結專屬 ACL 標籤（如 `tag:grok-bot`）**嚴格限制訪問許可權**。
2. 進入團隊環境設定指令碼點 **+** 新建清單，Manifest ID 填 `private-network-tailscale`，切換 JSON 或表單模式填入配置：

::: details 接入 Tailscale 組網方案
```json
{
  "manifestId": "private-network-tailscale",
  "entries": [
    {
      "id": "install-tailscale",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://tailscale.com/install.sh | sh\nsudo tailscale up --authkey=\"$TS_AUTHKEY\" --accept-routes --hostname=\"grok-vm-${USER}\"",
      "check": "command -v tailscale && tailscale status"
    }
  ]
}
```
:::

#### 接入 Cloudflare Tunnel 方案

- 私有 HTTP 服務：直接訪問隧道路由域名，由 Cloudflare Access 鑑權並在 Bot 瀏覽器互動完成認證。
- 私有 TCP 服務（如資料庫、SSH）：在清單安裝 `cloudflared`，需要連線時在 Shell 跑命令**開啟本地轉發埠**：

`cloudflared access tcp --hostname db-internal.corp.com --url localhost:5432`

::: details 接入 Cloudflare Tunnel 方案
```json
{
  "manifestId": "private-network-cftunnel",
  "entries": [
    {
      "id": "install-cloudflared",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null\necho 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared bullseye main' | sudo tee /etc/apt/sources.list.d/cloudflared.list\nsudo apt-get update && sudo apt-get install -y cloudflared",
      "check": "command -v cloudflared"
    }
  ]
}
```
:::

#### 配合網路策略放行控制面端點

團隊如果開啟**僅團隊允許列表**網路控制，**必須把網路工具的控制面加入允許列表**，否則客戶端無法完成認證。比如用 Tailscale 時，要在策略中放行協調伺服器與 DERP 中繼伺服器域名；策略變更 1 分鐘左右即可下發到虛擬機器。

### 做到什麼程度算好

- 新建或重建的 Bot 電腦在啟動完成後，自動出現在 Tailscale 或 Cloudflare 的管理控制檯裝置列表中，狀態為線上。
- 清單中的 `check` 指令碼能在後續每日輪巡重新整理中穩定返回 0，不會重複執行安裝邏輯。
- 敏感 Token 完全由 Team Secrets 注入，清單文字和執行日誌中沒有任何明文憑據。

---

## 代理與企業閘道器避坑：放行規則與 TLS 檢查豁免

企業閘道器（如 Zscaler、Palo Alto）常導致聊天正常，卻**無法截圖或控制終端**。

根源在於控制平面使用 `<computer>.<cluster>.cursorvm.com` 二級巢狀域名的 HTTP/2 或 SSE 流式長連線，普通單級規則無法匹配。

官方說明見 [配置 TLS 檢查代理](https://cursor.com/cn/docs/grok-bot/proxies)。

### 配置要點

閘道器必須放行以下域名，同時**關閉響應緩衝並豁免 TLS 檢查**，防止端到端握手失敗與流式超時：
- `*.cursor.sh`：核心 API
- `*.cursorvm.com` 與 **`*.*.cursorvm.com`**：控制通道，必須支援雙級萬用字元
- `*.cursor-cdn.com`、`*.cursorapi.com`、`downloads.cursor.com` 及主站：靜態資源與下載更新

策略配完後，**務必同步至 Off-Network 漫遊配置**，避免員工離網或居家時連不上。

### 裝置排查與驗收

在員工電腦終端按步驟排查：

1. 驗證證書是否被篡改，正常頒發者必須是 **Amazon RSA**：
```bash
   curl -v https://api2.cursor.sh |& grep -C1 issuer:
   ```
2. 驗證多級 DNS 解析，若失敗可對比 `nslookup test.us9.cursorvm.com 1.1.1.1`：
```bash
   nslookup test.us9.cursorvm.com
   ```
3. 檢查流式傳輸：資料應逐行輸出；若停頓數秒後突然整體列印，說明閘道器緩衝未關。

驗收標準：**辦公網和居家漫遊均在 5 秒內連上雲端電腦**，證書直透 Amazon RSA，流式長連線無緩衝延遲。

## 桌面客戶端分發與版本控制

### 平臺與更新機制

| 平臺 | 安裝格式 | 更新邏輯 |
| --- | --- | --- |
| macOS | `.dmg`（Apple Silicon / Intel） | 啟動自動檢查更新，**不支援策略關閉** |
| Windows | Setup `.exe`（x64 / Arm64） | 啟動自動檢查更新，不支援策略關閉 |
| Linux | `.deb`、`.rpm`、AppImage | deb 與 rpm 由包管理器控制；AppImage 自動檢查更新 |
| iOS | App Store | 依賴 iOS 18 或更高版本 |
| Android | Google Play | 依賴 Android 9 或更高版本，支援託管推送 |

官方部署說明見 [將 Grok Bot 部署到你的組織](https://cursor.com/cn/docs/grok-bot/deployment)。

### 部署與版本控制

1. **獲取安裝包**
   獲取安裝包不要去網頁手點，直接調官方的 JSON feed：`https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`。
   `{platform}` 支援 macOS（`darwin-arm64`、`darwin-x64`）、Windows（`win32-x64-user`、`win32-arm64-user`）與 Linux（`linux-x64`、`linux-arm64`）。
```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand
```
   介面返回 `version`、`commitSha`、`downloadUrl`，以及 Linux 的 `debUrl` 與 `rpmUrl`。macOS 與 Windows 也可以按規則直接拼安裝包地址：
   - Windows: `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`
   - macOS: `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`

2. **MDM 推送**
   - Windows（Intune / SCCM）：靜默安裝引數加 `/S`。安裝程式預設寫入當前使用者的 `%LOCALAPPDATA%\Programs`，**必須在使用者上下文（User Context）執行**。

     切勿使用本地 SYSTEM 賬戶，否則裝錯路徑員工找不到應用。
```cmd
  Grok_Bot_1.0.0_Setup.exe /S
  ```
   - macOS（Jamf / Kandji / Intune）：把對應架構的 `.dmg` 推送到 `/Applications` 目錄即可。
   - Linux（Ansible / Puppet）：安裝 `.deb` 或 `.rpm` 軟體包，系統會自動寫入官方軟體源配置。

3. **版本控制與鎖定**
   macOS 與 Windows 無法透過策略徹底關掉自動升級。

Linux 端可以透過包管理器鎖定版本，或在 `/etc/apt/sources.list.d/grok-bot.sources` 中設 `Enabled: no`、在 `/etc/yum.repos.d/grok-bot.repo` 中設 `enabled=0` 暫停同步：
```bash
  sudo apt-mark hold grok-bot
  ```
   Cursor 會對舊版本設支援期限。**客戶端低於最低支援閾值會全屏彈窗 Update required 強制阻斷**，Linux 鎖了版本超期同樣會被阻斷。運維團隊需要**每兩到四周灰度上線一次經過測試的新穩定版**。

### 驗收標準

- 辦公裝置透過 MDM 靜默安裝完成，**新員工開機後桌面已就緒**。
- IT 團隊掌握固定版本輪轉節奏，在官方強制阻斷前完成組織內部版本輪換。

## 管理 Bot 電腦：批次運維與生命週期

![管理 Bot 電腦：批次運維與生命週期](/info/23-enterprise-s6.png)

### 核心操作與許可權

入口在 [Cursor 儀表盤的 Grok Bot 頁面](https://cursor.com/dashboard/bot) 的 **Bot Computers** 分割槽，點選 **Manage Bot Computers** 就能進入。

**該功能僅限企業版組織管理員（Organization Admins）使用**，普通團隊管理員看不到入口。

文件見 [管理 Grok Bot 電腦](https://cursor.com/cn/docs/grok-bot/computers)。

| 操作名稱 | 底層行為 | 資料與檔案保留狀態 | 適用場景 |
| --- | --- | --- | --- |
| **重建 VMs（Recreate VMs）** | 用最新映象重灌並重跑環境指令碼 | **保留**。磁碟完好，Bot、個人檔案與 Cookie 均保留，僅清除自裝系統軟體 | 環境指令碼變更生效、灰度新映象 |
| **終止 VMs（Terminate VMs）** | 立即銷燬執行或休眠例項，中斷當前計算 | **保留**。保留磁碟，下次在客戶端發訊息會重新拉起乾淨虛擬機器 | 解決例項卡死、釋放雲端佔用 |
| **刪除虛擬機器和資料** | 銷燬虛擬機器並徹底刪除底層繫結的持久儲存 | **不保留**。資料徹底清空，下次使用重新初始化為空白電腦 | 員工離職清理、資料損壞徹底重置 |

### 控制檯操作與排坑

1. 進入頁面點選 **管理**，搜尋姓名或郵箱篩選成員，支援單選、多選或 **Select all**。
2. 在 **Manage selected** 下拉框選擇目標操作，確認受影響人數後開始執行。
3. 執行完畢**必須點選卡片上的 Done 按鈕**。每個團隊同一時間只能執行一項批次操作，不點 Done 後續按鈕會保持鎖定。

遇到跳過或失敗狀態，按回執對應處理。
- **已跳過（無 VM / 操作無法完成）**：名下沒有 VM 或排隊期間退出了團隊，無需處理。
- **失敗（另一項重建正在進行中 / VM 掃描未完成）**：其他更新未結束或後臺暫時未取到狀態，等幾分鐘重試。
- **失敗（操作無法完成）**：Bot 正在高強度跑任務導致超時，通知成員暫時空閒 Bot 後再重試。

### 自動化與驗收標準

在操作按鈕上方開啟 **Terminate Inactive Computers** 開關。**成員電腦連續 30 天無活動會自動終止**，只釋放計算例項且保留磁碟，系統按滾動週期清理。

多團隊批次運維可呼叫 [組織 Admin API](https://cursor.com/docs/account/organizations/organization-admin-api.md#grok-bot-computers)。

呼叫時需提供 `admin:*` 許可權的組織 API 金鑰，傳入團隊 ID、成員郵箱陣列和動作型別（`recreate` 或 `terminate`）並輪詢進度，同樣受單團隊單併發限制。

驗收時重點關注兩項指標。
- 能平滑批次重建例項且不丟資料。
- 開啟 30 天閒置自動終止，避免殭屍虛擬機器佔用組織雲端配額。

## 企業安全基準配置與實戰提示詞

### 管理員配置
1. 網路鎖在“僅團隊允許列表”，關閉公開模板和郵件通道。
2. 開啟 **Enforce Auto-review**，本地執行設為 **Never allow** 防私自降級。
3. 凡調生產 API 與改庫，或涉及外發郵件、籤協議及合入 main，必須設為 **Ask first**；日誌查詢與編譯直接放行。

### 員工守則
1. 憑證走環境變數，**嚴禁在對話方塊貼明文密碼**。
2. 敏感授權選 **Allow once**，別點始終允許，用完及時退出。

### 實戰提示詞
::: details 實戰提示詞
```text
你现在负责对内部服务进行接口与架构调研。
请遵循以下严格的安全限制：
1. 本次任务为纯只读模式，严禁对目标服务发起任何 POST、PUT、DELETE 请求。
2. 检查网络连通性：尝试向内部端点 http://api-monitor.corp.internal/health 发起 GET 请求并打印状态码。
3. 如果遇到证书问题或连接被重定向，记录错误日志，不要尝试使用任何提权手段。
4. 将调研结果汇总输出为 Markdown 表格，包含服务名称、响应耗时、健康状态。
5. 完成后暂停执行，等待我的进一步指令，不要擅自读取其他网段资产。
```
:::

::: details 實戰提示詞
```text
请按规范完成本周发版代码的对比检查与 PR 草稿创建：
1. 切换到工作区代码目录，拉取 origin/main 最新分支。
2. 比对 feature/sso-login 分支与 main 分支的改动差异，列出所有变动的文件列表。
3. 检查是否有硬编码的密钥、密码或私钥文件被提交。如果发现任何形如 'AKIA...' 或 'BEGIN PRIVATE KEY' 的文本，立即中断任务并向我告警。
4. 在本地运行静态检查脚本：npm run lint 和 npm run test。
5. 准备 PR 描述文本草稿，包含变更摘要与测试结果。
6. 注意：严禁直接推送到远程仓库。把 PR 描述保存为 local-pr-draft.md 后向我申请确认。得到明确授权前不得执行 git push。
```
:::

::: details 實戰提示詞
```text
请处理今天未分配的内部支持工单：
1. 打开浏览器，访问内部工单控制台 https://tickets.corp.internal。
2. 过滤出状态为 'New' 且优先级为 'High' 的所有工单。
3. 逐条提取工单的核心问题，按照以下类别打标签：[账号登录]、[权限申请]、[网络故障]。
4. 为每条工单生成标准回复模版，存入草稿区。
5. 涉及权限开通的工单，一律在回复中注明：'需直属主管在 OA 提交审批流，当前仅作信息预审'。
6. 严格要求：所有邮件和系统回复只保留在草稿状态，严禁点击 'Send' 或 'Submit'。生成处理清单供我逐条审查。
```
:::

## 容易踩的坑

1. **閘道器漏配多級萬用字元**：主機名是 `<vm-id>.<cluster-id>.cursorvm.com`，只配 `*.cursorvm.com` 卡在 99%，**要加配 `*.*.cursorvm.com`**。
2. **代理開緩衝截斷流**：Zscaler 開啟 Response Buffering 會斷連。**必須對 Cursor 域名關閉緩衝，透傳 Server-Sent Events**。
3. **漫遊策略漏白名單**：回家連不上是因 Zscaler 切了 Off-Network 策略。記得把域名白名單和 TLS 豁免同步到離網策略。
4. **誤開舊版隱私模式**：後臺開啟“隱私模式 (舊版)”會徹底禁用 Bot，在團隊設定中關掉。
5. **IdP 強求合規裝置**：雲端 Linux VM 沒納管 MDM 跑不了 FastPass。**在 Okta/Entra ID 針對 Linux（Other Desktop）加高優先順序規則**，改用密碼加手機二次認證放行。
6. **指令碼明文存金鑰**：Team Setup 是明文 JSON。Token 存進 **Team Secrets**，指令碼用 `"$TS_AUTHKEY"` 讀。
7. **SYSTEM 許可權安裝找不著**：程式裝在 `%LOCALAPPDATA%\Programs`。**要在當前使用者上下文執行 `/S` 安裝命令**。
8. **誤把終止當撤權**：Terminate 僅停程序保留磁碟，發訊息又會拉起。**徹底收權要在 IdP 取消分配或用 Manage Group Access 移除**。
9. **跨團隊丟失金鑰**：加入兩個以上配了 Team Setup 的團隊會被**拒收任何 Team Secrets**，退掉多餘團隊即可。
10. **鎖版本跌破下限**：`apt-mark hold` 鎖的版本低於生命週期下限會被“Update required”阻斷，解鎖升級即可。

## 做完怎麼驗收

### 網路與閘道器
- 辦公機跑 `curl -v https://api2.cursor.sh |& grep -C1 issuer:`，確保證書為 **Amazon RSA**。
- 跑 `nslookup test.us9.cursorvm.com` 測多級域名解析；切手機熱點連線雲端電腦，驗證**無證書告警**。

### 身份與 SSO
- 找非研發賬號登 Grok Bot，確認 Cursor SSO 一次登入成功。
- Bot 瀏覽器用“密碼+手機驗證碼”登入內部單點，**無 FastPass 攔截彈窗**，辦公機合規策略照常生效。

### 私網與環境指令碼
- Tailscale 或 Cloudflare 控制檯確認新機器自動入網且標籤正確。
- 終端 ping 或 curl 私有主機驗證連通；Team Setup 日誌無超時且**機密已打掩碼**。

### 客戶端與安全基準
- Windows 普通賬號靜默安裝到 `%LOCALAPPDATA%\Programs` 並生成桌面快捷方式。
- “設定 > 常規 > 自動審查”中全域性規則鎖定不可改；測試刪根目錄檔案或調未授權 Webhook，系統**強制彈出審批**。

### 電腦生命週期
- 管理員在控制檯執行 **重建 VMs**，確認原檔案與歷史記錄完好。
- 批次任務跑完點選 **Done**，系統能正常開啟下一輪。

## 延伸閱讀

- 官方文件：[面向 Teams 和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- 官方文件：[配置身份與訪問](https://cursor.com/cn/docs/grok-bot/identity)
- 官方文件：[連線到私有網路](https://cursor.com/cn/docs/grok-bot/private-networks)
- 官方文件：[配置 TLS 檢查代理](https://cursor.com/cn/docs/grok-bot/proxies)
- 官方文件：[將 Grok Bot 部署到你的組織](https://cursor.com/cn/docs/grok-bot/deployment)
- 官方文件：[管理 Grok Bot 電腦](https://cursor.com/cn/docs/grok-bot/computers)
- 官方幫助：[方案和計費](https://cursor.com/cn/help/grok-bot/plans)
- 官方幫助：[團隊 Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- 官方幫助：[連線應用](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- 官方指南：[Grok Bot 安全架構說明](https://cursor.com/cn/docs/grok-bot/security)
