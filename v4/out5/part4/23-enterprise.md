# 第 23 章 团队版与企业落地

给团队部署 Grok Bot，常见卡点主要是这几项。

- 网关在握手阶段拦截，导致**云端电脑连不上**。
- Linux 虚机没装 MDM 客户端，会被企业 IdP 判为不受信任设备。
- 存在凭据泄漏与内网穿透风险，也缺客户端静默分发手段。

按流程配好 **SSO 与安全网关豁免**，打通私网访问，就能搞定批量生命周期管理。

## 团队版与企业版管理控制：架构与能力边界

### 是什么

**每位用户独享一台云端 Firecracker microVM**，本地发指令审批，代码与浏览器在云端跑。

提醒个坑，**名下所有 Bot 共享这台虚机**，文件和登录态完全互通。

2026-10-12 The X Subscription 方案划分了两版权限：

- **团队版**：全员默认开启，走共享静态出口 IP，带基础审计与团队规则。
- **企业版**：支持按组授权与 SCIM 2.0，能用 sudo 和网络白名单，带操作录制与 OpenTelemetry 导出（打 `cursor.surface=grok_bot` 标签）。

文档见 [面向 Teams 和企业版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)。

### 怎么做

日常配置都在 [Cursor 仪表盘的 Grok Bot 页面](https://cursor.com/dashboard/bot) 处理，主要分四步走。

1. 划分权限与基础开关
- 灰度期点 **Manage Group Access** 勾选试点；不用云端编码就关掉 Cloud Agents；公开模板共享保持关闭防外泄。
- **本地执行建议设为 Never allow**，同时关闭本地出口路由防绕道转发。
- 侧边栏 Bot 在 Auto-add 列选 All team 或指定群组固定。

2. 配置审批锁与规则
- 开启 **Enforce Auto-review 模式**，成员在客户端就没法自关审查。
- 生产部署或对外发邮件等高危操作设为 Ask first，限定只读设为 Allow automatically。
- **团队规则与个人规则冲突时，系统强制以 Ask first 为准**。

3. 设置网络与密钥
- 网络选仅团队允许列表或加默认值，填入域名与 IP 段；防系统篡改可关闭默认开启的 sudo。
- **Team Secrets 团队最多添加 100 条**，单条上限 32 KB，总容量上限 96 KB，保存后不显示明文。
- 密钥变量名禁止使用 `PATH`、`HOME` 及 `SAND_` 或 `LD_` 开头的系统保留名。

4. 配置群组级策略
- 从 [Members > Groups](https://cursor.com/dashboard/members?subtab=groups) 进群组，**配置原则是只能放宽、不能更严**。
- 勾选 Don't enforce for this group 可解开自动审查锁。
- 网络策略是特例，群组会直接覆盖团队；如果成员跨多个群组，网络按最严执行，权限按最宽生效。

### 做到什么程度算好

- 仪表盘中明确区分了试点群组与未授权群组，非授权人员在客户端无法激活 Bot。
- 团队规则与 Auto-review 规则已锁定，成员在客户端设置页面能看到团队规则，但编辑与删除按钮处于禁用状态。
- 高危操作（外部通信、文件破坏、特权命令）百分之百触发审批拦截。

---

## 身份与 SSO：打通全员访问与兼容设备信任

### 是什么

Grok Bot 沿用 Cursor 账号体系，**不用在 IdP 中单独建应用**。参考文档：[配置身份与访问](https://cursor.com/cn/docs/grok-bot/identity)。

Bot 跑在云端 Linux 虚机，未装 MDM，无法满足 FastPass 或 Hybrid Join。**切记不能全局关闭设备合规**，要在拦截规则前为目标群组配置放行策略。

### 怎么做

- **Okta 扩大分配**：进 Cursor 应用的 **Assignments** > **Assign to Groups** 勾选业务群组；启用 SCIM 时同步分配并推送（Push Groups）。**SAML SSO 与 SCIM 必须同时分配**，漏配 SSO 登录会被拦截。
- **Entra ID 扩大分配**：在 Cursor 应用的 **Users and groups** 点 **Add user/group** 添加群组（需 P1/P2 许可，不支持嵌套组）；预配应用同步分配相同群组。
- **Okta 放行 Linux**：在认证策略拦截规则前新建 `Grok Bot computer (Linux)`。用户限 Cursor 组，**Device platform 选 Other Desktop**（无独立 Linux 项），Device state 选 Any；验证选 Password + Another factor，不勾抗钓鱼限制。
- **Entra ID 放行 Linux**：新建高优先级策略，指定 Cursor 组和目标应用；Device platforms 包含 Linux，排除 Windows 与 macOS；Grant 勾 Require multifactor authentication；**原有合规策略中必须排除该群组或 Linux 平台**。

### 做到什么程度算好

- 业务用户用企业 SSO 登录桌面端，不报 `User is not assigned to this application`。
- 在 Bot 浏览器中凭密码加二次验证能访问内网，不弹 FastPass 或设备不合规拦截。
- **员工在个人电脑上访问，原有的 FastPass 和设备合规仍严格生效**。

## 私有网络接入：桌面路由与 Team Setup 脚本自动化

### 是什么

Grok Bot 跑在云端，**访问内网必须打通私网**。

- 桌面端路由：适合临时调试。在客户端开启 `Settings > Computer > Route traffic through this computer`，流量走本机网卡，管理员可在后台一键禁用。
- Team Setup 安装客户端：常态化访问且**仅限企业版**。由 IT 统一维护脚本，Bot 启动或刷新时自动拉起并加入内网。

详情见 [连接到私有网络](https://cursor.com/cn/docs/grok-bot/private-networks)。

### 怎么做

团队环境设置脚本在仪表盘 **Bot Computers** 下，以 `sudo` 普通用户身份在 Debian Linux 虚拟机中跑。**脚本开机时运行且每天约周期刷新一次，超时上限 30 分钟**。
- `check` 退出码为 0 就跳过安装，装完会再次运行 `check` 验证。
- **执行失败不阻塞电脑启动**，会在下次周期刷新时重试。

#### 接入 Tailscale 组网方案

1. 打开 **Team Secrets**，添加 Tailscale 认证密钥 `TS_AUTHKEY`（值为 `tskey-auth-...`），并在 Tailscale 控制台绑定专属 ACL 标签（如 `tag:grok-bot`）**严格限制访问权限**。
2. 进入团队环境设置脚本点 **+** 新建清单，Manifest ID 填 `private-network-tailscale`，切换 JSON 或表单模式填入配置：

::: details 接入 Tailscale 组网方案
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

- 私有 HTTP 服务：直接访问隧道路由域名，由 Cloudflare Access 鉴权并在 Bot 浏览器交互完成认证。
- 私有 TCP 服务（如数据库、SSH）：在清单安装 `cloudflared`，需要连接时在 Shell 跑命令**打开本地转发端口**：

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

#### 配合网络策略放行控制面端点

团队如果开启**仅团队允许列表**网络控制，**必须把网络工具的控制面加入允许列表**，否则客户端无法完成认证。比如用 Tailscale 时，要在策略中放行协调服务器与 DERP 中继服务器域名；策略变更 1 分钟左右即可下发到虚拟机。

### 做到什么程度算好

- 新建或重建的 Bot 电脑在启动完成后，自动出现在 Tailscale 或 Cloudflare 的管理控制台设备列表中，状态为在线。
- 清单中的 `check` 脚本能在后续每日轮巡刷新中稳定返回 0，不会重复执行安装逻辑。
- 敏感 Token 完全由 Team Secrets 注入，清单文本和执行日志中没有任何明文凭据。

---

## 代理与企业网关避坑：放行规则与 TLS 检查豁免

企业网关（如 Zscaler、Palo Alto）常导致聊天正常，却**无法截图或控制终端**。根源在于控制平面使用 `<computer>.<cluster>.cursorvm.com` 二级嵌套域名的 HTTP/2 或 SSE 流式长连接，普通单级规则无法匹配。官方说明见 [配置 TLS 检查代理](https://cursor.com/cn/docs/grok-bot/proxies)。

### 配置要点

网关必须放行以下域名，同时**关闭响应缓冲并豁免 TLS 检查**，防止端到端握手失败与流式超时：
- `*.cursor.sh`：核心 API
- `*.cursorvm.com` 与 **`*.*.cursorvm.com`**：控制通道，必须支持双级通配符
- `*.cursor-cdn.com`、`*.cursorapi.com`、`downloads.cursor.com` 及主站：静态资源与下载更新

策略配完后，**务必同步至 Off-Network 漫游配置**，避免员工离网或居家时连不上。

### 设备排查与验收

在员工电脑终端按步骤排查：

1. 验证证书是否被篡改，正常颁发者必须是 **Amazon RSA**：
```bash
   curl -v https://api2.cursor.sh |& grep -C1 issuer:
   ```
2. 验证多级 DNS 解析，若失败可对比 `nslookup test.us9.cursorvm.com 1.1.1.1`：
```bash
   nslookup test.us9.cursorvm.com
   ```
3. 检查流式传输：数据应逐行输出；若停顿数秒后突然整体打印，说明网关缓冲未关。

验收标准：**办公网和居家漫游均在 5 秒内连上云端电脑**，证书直透 Amazon RSA，流式长连接无缓冲延迟。

## 桌面客户端分发与版本控制

### 平台与更新机制

| 平台 | 安装格式 | 更新逻辑 |
| --- | --- | --- |
| macOS | `.dmg`（Apple Silicon / Intel） | 启动自动检查更新，**不支持策略关闭** |
| Windows | Setup `.exe`（x64 / Arm64） | 启动自动检查更新，不支持策略关闭 |
| Linux | `.deb`、`.rpm`、AppImage | deb 与 rpm 由包管理器控制；AppImage 自动检查更新 |
| iOS | App Store | 依赖 iOS 18 或更高版本 |
| Android | Google Play | 依赖 Android 9 或更高版本，支持托管推送 |

官方部署说明见 [将 Grok Bot 部署到你的组织](https://cursor.com/cn/docs/grok-bot/deployment)。

### 部署与版本控制

1. **获取安装包**
   获取安装包不要去网页手点，直接调官方的 JSON feed：`https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`。
   `{platform}` 支持 macOS（`darwin-arm64`、`darwin-x64`）、Windows（`win32-x64-user`、`win32-arm64-user`）与 Linux（`linux-x64`、`linux-arm64`）。
```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand
```
   接口返回 `version`、`commitSha`、`downloadUrl`，以及 Linux 的 `debUrl` 与 `rpmUrl`。macOS 与 Windows 也可以按规则直接拼安装包地址：
   - Windows: `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`
   - macOS: `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`

2. **MDM 推送**
   - Windows（Intune / SCCM）：静默安装参数加 `/S`。安装程序默认写入当前用户的 `%LOCALAPPDATA%\Programs`，**必须在用户上下文（User Context）运行**。切勿使用本地 SYSTEM 账户，否则装错路径员工找不到应用。
```cmd
  Grok_Bot_1.0.0_Setup.exe /S
  ```
   - macOS（Jamf / Kandji / Intune）：把对应架构的 `.dmg` 推送到 `/Applications` 目录即可。
   - Linux（Ansible / Puppet）：安装 `.deb` 或 `.rpm` 软件包，系统会自动写入官方软件源配置。

3. **版本控制与锁定**
   macOS 与 Windows 无法通过策略彻底关掉自动升级。Linux 端可以通过包管理器锁定版本，或在 `/etc/apt/sources.list.d/grok-bot.sources` 中设 `Enabled: no`、在 `/etc/yum.repos.d/grok-bot.repo` 中设 `enabled=0` 暂停同步：
```bash
  sudo apt-mark hold grok-bot
  ```
   Cursor 会对旧版本设支持期限。**客户端低于最低支持阈值会全屏弹窗 Update required 强制阻断**，Linux 锁了版本超期同样会被阻断。运维团队需要**每两到四周灰度上线一次经过测试的新稳定版**。

### 验收标准

- 办公设备通过 MDM 静默安装完成，**新员工开机后桌面已就绪**。
- IT 团队掌握固定版本轮转节奏，在官方强制阻断前完成组织内部版本轮换。

## 管理 Bot 电脑：批量运维与生命周期

### 核心操作与权限

入口在 [Cursor 仪表盘的 Grok Bot 页面](https://cursor.com/dashboard/bot) 的 **Bot Computers** 分区，点击 **Manage Bot Computers** 就能进入。**该功能仅限企业版组织管理员（Organization Admins）使用**，普通团队管理员看不到入口。文档见 [管理 Grok Bot 电脑](https://cursor.com/cn/docs/grok-bot/computers)。

| 操作名称 | 底层行为 | 数据与文件保留状态 | 适用场景 |
| --- | --- | --- | --- |
| **重建 VMs（Recreate VMs）** | 用最新镜像重装并重跑环境脚本 | **保留**。磁盘完好，Bot、个人文件与 Cookie 均保留，仅清除自装系统软件 | 环境脚本变更生效、灰度新镜像 |
| **终止 VMs（Terminate VMs）** | 立即销毁运行或休眠实例，中断当前计算 | **保留**。保留磁盘，下次在客户端发消息会重新拉起干净虚拟机 | 解决实例卡死、释放云端占用 |
| **删除虚拟机和数据** | 销毁虚拟机并彻底删除底层绑定的持久存储 | **不保留**。数据彻底清空，下次使用重新初始化为空白电脑 | 员工离职清理、数据损坏彻底重置 |

### 控制台操作与排坑

1. 进入页面点击 **管理**，搜索姓名或邮箱筛选成员，支持单选、多选或 **Select all**。
2. 在 **Manage selected** 下拉框选择目标操作，确认受影响人数后开始执行。
3. 执行完毕**必须点击卡片上的 Done 按钮**。每个团队同一时间只能运行一项批量操作，不点 Done 后续按钮会保持锁定。

遇到跳过或失败状态，按回执对应处理。
- **已跳过（无 VM / 操作无法完成）**：名下没有 VM 或排队期间退出了团队，无需处理。
- **失败（另一项重建正在进行中 / VM 扫描未完成）**：其他更新未结束或后台暂时未取到状态，等几分钟重试。
- **失败（操作无法完成）**：Bot 正在高强度跑任务导致超时，通知成员暂时空闲 Bot 后再重试。

### 自动化与验收标准

在操作按钮上方打开 **Terminate Inactive Computers** 开关。**成员电脑连续 30 天无活动会自动终止**，只释放计算实例且保留磁盘，系统按滚动周期清理。

多团队批量运维可调用 [组织 Admin API](https://cursor.com/docs/account/organizations/organization-admin-api.md#grok-bot-computers)。调用时需提供 `admin:*` 权限的组织 API 密钥，传入团队 ID、成员邮箱数组和动作类型（`recreate` 或 `terminate`）并轮询进度，同样受单团队单并发限制。

验收时重点关注两项指标。
- 能平滑批量重建实例且不丢数据。
- 开启 30 天闲置自动终止，避免僵尸虚拟机占用组织云端配额。

## 企业安全基准配置与实战提示词

### 管理员配置
1. 网络锁在“仅团队允许列表”，关闭公开模板和邮件通道。
2. 开启 **Enforce Auto-review**，本地执行设为 **Never allow** 防私自降级。
3. 凡调生产 API 与改库，或涉及外发邮件、签协议及合入 main，必须设为 **Ask first**；日志查询与编译直接放行。

### 员工守则
1. 凭证走环境变量，**严禁在对话框贴明文密码**。
2. 敏感授权选 **Allow once**，别点始终允许，用完及时退出。

### 实战提示词
::: details 实战提示词
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

::: details 实战提示词
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

::: details 实战提示词
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

1. **网关漏配多级通配符**：主机名是 `<vm-id>.<cluster-id>.cursorvm.com`，只配 `*.cursorvm.com` 卡在 99%，**要加配 `*.*.cursorvm.com`**。
2. **代理开缓冲截断流**：Zscaler 开启 Response Buffering 会断连。**必须对 Cursor 域名关闭缓冲，透传 Server-Sent Events**。
3. **漫游策略漏白名单**：回家连不上是因 Zscaler 切了 Off-Network 策略。记得把域名白名单和 TLS 豁免同步到离网策略。
4. **误开旧版隐私模式**：后台开启“隐私模式 (旧版)”会彻底禁用 Bot，在团队设置中关掉。
5. **IdP 强求合规设备**：云端 Linux VM 没纳管 MDM 跑不了 FastPass。**在 Okta/Entra ID 针对 Linux（Other Desktop）加高优先级规则**，改用密码加手机二次认证放行。
6. **脚本明文存密钥**：Team Setup 是明文 JSON。Token 存进 **Team Secrets**，脚本用 `"$TS_AUTHKEY"` 读。
7. **SYSTEM 权限安装找不着**：程序装在 `%LOCALAPPDATA%\Programs`。**要在当前用户上下文运行 `/S` 安装命令**。
8. **误把终止当撤权**：Terminate 仅停进程保留磁盘，发消息又会拉起。**彻底收权要在 IdP 取消分配或用 Manage Group Access 移除**。
9. **跨团队丢失密钥**：加入两个以上配了 Team Setup 的团队会被**拒收任何 Team Secrets**，退掉多余团队即可。
10. **锁版本跌破下限**：`apt-mark hold` 锁的版本低于生命周期下限会被“Update required”阻断，解锁升级即可。

## 做完怎么验收

### 网络与网关
- 办公机跑 `curl -v https://api2.cursor.sh |& grep -C1 issuer:`，确保证书为 **Amazon RSA**。
- 跑 `nslookup test.us9.cursorvm.com` 测多级域名解析；切手机热点连接云端电脑，验证**无证书告警**。

### 身份与 SSO
- 找非研发账号登 Grok Bot，确认 Cursor SSO 一次登录成功。
- Bot 浏览器用“密码+手机验证码”登录内部单点，**无 FastPass 拦截弹窗**，办公机合规策略照常生效。

### 私网与环境脚本
- Tailscale 或 Cloudflare 控制台确认新机器自动入网且标签正确。
- 终端 ping 或 curl 私有主机验证连通；Team Setup 日志无超时且**机密已打掩码**。

### 客户端与安全基准
- Windows 普通账号静默安装到 `%LOCALAPPDATA%\Programs` 并生成桌面快捷方式。
- “设置 > 常规 > 自动审查”中全局规则锁定不可改；测试删根目录文件或调未授权 Webhook，系统**强制弹出审批**。

### 电脑生命周期
- 管理员在控制台执行 **重建 VMs**，确认原文件与历史记录完好。
- 批量任务跑完点击 **Done**，系统能正常开启下一轮。

## 延伸阅读

- 官方文档：[面向 Teams 和企业版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- 官方文档：[配置身份与访问](https://cursor.com/cn/docs/grok-bot/identity)
- 官方文档：[连接到私有网络](https://cursor.com/cn/docs/grok-bot/private-networks)
- 官方文档：[配置 TLS 检查代理](https://cursor.com/cn/docs/grok-bot/proxies)
- 官方文档：[将 Grok Bot 部署到你的组织](https://cursor.com/cn/docs/grok-bot/deployment)
- 官方文档：[管理 Grok Bot 电脑](https://cursor.com/cn/docs/grok-bot/computers)
- 官方帮助：[方案和计费](https://cursor.com/cn/help/grok-bot/plans)
- 官方帮助：[团队 Bot](https://cursor.com/cn/help/grok-bot/team-bots)
- 官方帮助：[连接插件](https://cursor.com/cn/help/grok-bot/connect-plugins)
- 官方指南：[Grok Bot 安全架构说明](https://cursor.com/cn/docs/grok-bot/security)
