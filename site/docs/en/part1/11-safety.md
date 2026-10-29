# Chapter 11 Permissions, Security, and Human Gates

Don't go to extremes when using Grok Bot. **Manually confirming every step is exhausting**, while **excessive delegation can easily lead to accidental deletion of production configurations**; simply spinning up multiple Bots does not achieve isolation either.

The security defense line mainly includes these items:
- Tiered delegation based on action reversibility
- Fully configuring Auto Review machine-level interception
- Blocking network and credential exfiltration paths
- **Establishing daily auditing and emergency circuit breaker mechanisms**


![Permissions, Security, and Human Gates](/info/11-safety.png)

## Isolation Mechanisms and Underlying Facts: What Bots Under the Same Account Share

![Isolation Mechanisms and Underlying Facts: What Bots Under the Same Account Share](/info/11-safety-s1.png)

### What It Is
Grok Bot runs on Cursor's dedicated Firecracker microVMs, with underlying hardware-level physical isolation between users.

However, **all Bots under the same account share the same cloud computer**, sharing the `/workspace` directory, browser cookies, and login states; OAuth tokens are stored on the backend and do not touch disk.

### How to Do It
**Multiple Bots cannot achieve environment isolation**. Once one Bot logs into an admin console, other Bots can also operate it directly.

If strong isolation is required, a separate Cursor account must be created; invoking a [Team Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md) created by a teammate also runs on your own cloud computer.

**Deleting a Bot in the client does not clear local files and login states**. When wrapping up a project, you must manually perform three cleanup steps:
1. Log out in the cloud computer's browser
2. Go to third-party platforms to revoke OAuth authorizations
3. Clean up sensitive files in `/workspace`

### What Good Looks Like
- **Clear physical boundaries**: MicroVM underlying isolation is effective.
- **Strictly separated tasks**: Never mix high-risk operations with untrusted external scraping under the same account.
- **Thoroughly cleared credentials**: No orphaned sessions left after project completion, see [4.4 Permissions, Security, and Human Gates](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd).

## Action Tiering: Classifying Permissions by One-Minute Reversibility

![Action Tiering: Classifying Permissions by One-Minute Reversibility](/info/11-safety-s2.png)

**There is only one delegation criterion: Can the action be rolled back within 1 minute (60 seconds)?** Operations that can be easily reverted are directly allowed, while operations that cannot be quickly undone must be gated by approval.

| Operation Category | Typical Actions | Policy and Interception |
| :--- | :--- | :--- |
| Read-only & Retrieval | Read `/workspace`, check API balance | Autonomous execution, allow directly |
| Local Trial-and-Error Modifications | Modify temp files, run `git status` | Autonomous execution, restricted to working directory |
| External Communication | Send emails, send direct messages | Mandatory human gate, only draft generation allowed |
| Assets & Contracts | Transfer payments, change subscription plans | Strictly prohibited from autonomous execution, never touch checkout |
| System & Permissions | Delete non-junk files, modify production configurations | Mandatory human gate, rule interception (Ask first) single confirmation |

1. **Write "Operations that cannot be rolled back within one minute must stop and ask me" into the Bot's global rules.**
2. Starting from 2026-10-07, tasks may be routed to stronger models such as Claude Opus 5.5. As models tend more toward autonomous reasoning, permission boundaries must be welded shut.
3. Client approval cards expire after roughly a 10-minute timeout. **Nightly Routines must never hang on outgoing message approval**; set the output destination to "Save as local file" or "Generate draft card" to prevent timeout errors and interruptions.

Acceptance criteria:
- Preparation completed autonomously within the sandbox and working directory.
- **Proactively suspends and waits for manual card confirmation** before irreversible actions are triggered.
- Nightly automation tasks do not abort due to timeouts. [4.4 Permissions, Security, and Human Gates](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## Approval Mechanisms and Auto Review Action Interception

![Approval Mechanisms and Auto Review Action Interception](/info/11-safety-s3.png)

### What It Is
When the Bot executes a controlled operation, an approval card pops up offering three options: **Allow once, Always allow, and Deny** (consistent on the iPhone client).

Underlying Auto Review prescreens shell commands and plugin invocations, while also governing computer use, automated writes, and Agent delegation.
**Writing to memory and most configuration changes bypass review**, meaning it cannot replace item-by-item approval.

### How to Do It
1. For Enterprise, enable the **Enforce Auto-review mode** lock in the Cursor dashboard, except for groups set to Don't enforce for this group.
2. For individuals, go to Settings > General > Auto-review > Custom Rules in the client; **when rules conflict, Ask first takes precedence**.
   - Ask first: Mandatory interception with pop-up card
   - Allow automatically: Automatically allow when there is no risk

Directly populate high-risk actions into the Ask first rule list.
```text
send, post, buy, transfer, delete, permissions, production, terms
```
**Rules must be bound to specific behaviors** (e.g., "Ask before sending external emails"); broad rules like "Allow all shell scripts" are strictly prohibited.

### Acceptance Criteria
- High-risk actions **pop up confirmation cards 100% of the time**
- Daily low-risk read/write operations are not falsely intercepted
- In case of conflict, the strictest interception policy is enforced, see [Grok Bot Security](https://cursor.com/cn/docs/grok-bot/security)

## Credential Management and Human-Machine Handover Standards

**Pass sessions, not secrets**. The Bot operates by borrowing your identity; when encountering logins, 2FA, or payments, you must take over in person—never send passwords into the chat box.

1. **Take over the screen**: Click Take over at the top of the window to enter credentials yourself or autofill using 1Password. For masking mechanisms, see [Securely Store Secrets](https://cursor.com/cn/help/grok-bot/secrets).
2. **Read-only permissions**: External keys should only be granted query permissions; transfers or writes are strictly prohibited.
3. **Local permissions**: Go to Settings > Computer > Your computer > Execution on this computer, and choose Never allow among the three options (the others are Ask every time and Always allow).

### Acceptance Criteria
- Chat and `/workspace` logs contain no passwords or 2FA codes.
- External services all use authenticated sessions.
- Local execution is disabled by default.

## Approval Mechanisms for Outbound Messaging and Irreversible Actions

### Mechanisms and Pitfalls to Avoid
- **Never check Close drafts in production environments**: v0.64 added this switch to email and Slack cards; checking it will bypass drafts and send directly externally.
- **Underlying hard interception for irreversible actions**: In v0.70.2, before executing sending messages, posting, purchasing, or deleting, if the context lacks on-the-spot confirmation, execution will be blocked directly.

### Configuration Steps
1. **Weld a halt instruction to the end of the prompt**:
```text
核对营销活动数据，并起草一份推荐的预算调整方案。不要更改营销活动，也不要联系代理商。在展示当前值、建议值和预期影响之后，请求批准。
```
2. **Solidify the six-line contract**: For personal Bots, send the following rules in the chat and have it remember them; for shared Bots, write them into the Description under About details:
```text
Own: 唯一负责的业务结果与目标
Sources: 允许读取的应用、数据源网址或本地绝对路径
Output: 交付格式、字数限制与落盘文件位置
Approval: 在执行前必须停下来等待人工批准的动作清单（never publish, never email, never modify without approval）
Failure: 当外部数据源缺失、超时或失效时的应对规则（如实报错并停止，严禁编造数据）
Never: 绝对禁止触碰的系统操作或越权行为
```
3. **Deploy the Chief of Staff charter**: For complex tasks, use the kocer Chief of Staff as the sole entry point. For personal master Bots, send the charter in chat and have it remember it; for shared Bots, write it into the Description under About details:
::: details Configuration Steps
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
Send the ten bottom-line rules to the Bot and save them as the `house_rules` Skill:
::: details Configuration Steps
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

### Acceptance Criteria
- **The Bot cannot bypass drafts to send outbound messages on its own**; external communication cards must be manually confirmed twice.
- When encountering the sudden command `STOP ALL`, **all in-flight tasks can be suspended instantly**.

[Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## Network Policies and Boundary Tightening

### Core Permissions
**Connector policies and network policies are completely independent**. Disabling plugins in the backend cannot prevent the Bot from using its built-in browser to access the public internet.

**Network Controls are limited to the Enterprise edition**; the Teams plan has full access by default without a configuration panel. Configuration requires navigating in the Cursor dashboard to Grok Bot > Network > Grok Bot Network Access.

### Access Modes
| Mode | Enforcement Rule | Applicable Scenario |
| :--- | :--- | :--- |
| **Allow All Network Access** | Allows access to all public internet destinations (default state) | Exploratory R&D, operations without sensitive data |
| **Defaults + Team Allowlist** | Allows baseline system domains plus team custom allowlist | The vast majority of enterprise production environments |
| **Team Allowlist Only** | Only allows custom allowlist and minimum baseline to maintain VM | Strict compliance and auditing environments |

Supports web domains as well as raw TCP IP ranges and ports, with no upper limit on the number of entries. Running computers sync automatically within approximately one minute; sleeping machines apply changes upon their next wake-up. Directory group policies take precedence over team policies, and enabling global Lock takes effect for all members.

### Pitfalls and Private Networks
- The shared static egress IP is shared across all customers and **must never be used to identify specific teams**. When internal networks require allowlisting, request the latest IP ranges from the account team.
- Allowing `api2.cursor.sh` at the gateway while decrypting nested domains causes machines to hang at "Setting up computer"; **you must allowlist `*.cursorvm.com` and `*.*.cursorvm.com` across all profiles and bypass certificate decryption**.

  See [Configure TLS Inspection Proxies](https://cursor.com/cn/docs/grok-bot/proxies).
- To access internal network resources, enable desktop traffic forwarding (Allow Local Egress Routing), or use Team Setup Scripts to install a VPN client uniformly during initialization.

  See [Connect to Private Networks](https://cursor.com/cn/docs/grok-bot/private-networks).

### What Good Looks Like
- **Explicitly block unnecessary outbound internet requests**
- Block unauthorized outbound file transfers
- Internal gateways correctly allowlist nested domains, with no VM connection hanging issues

## Log Auditing and Run Tracking

- **Audit Logs (Enterprise)**: Records permission and configuration changes, with support for direct SIEM integration.
- **Session Recording (Enterprise)**: Records sanitized shell commands. **Disabled by default and retained for only 90 days**; not queryable in standard dashboards, requiring OpenTelemetry export to a self-hosted collector, filtered by the tag `cursor.surface=grok_bot`.
- **Local State Logs**: Without the Enterprise edition, the Bot writes decisions and approval duration to `/workspace/state/chief_log.md`.

Configure a lightweight Routine to **automatically inspect anomalous commands and infinite loops every Friday afternoon**:

::: details Log Auditing and Run Tracking
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

**Acceptance Criteria**: Changes are auditable in SIEM, commands can be retraced, and local operation logs are retained. Refer to [Grok Bot Security](https://cursor.com/cn/docs/grok-bot/security).

## Human Gate Case Studies in Typical Business Scenarios

### Outbound Job Seeking (PatBergie's Practice)
- The frontend is split into 8 specialized Bots dividing labor to scrape job openings, look up backgrounds, and draft personalized resumes and cover letters saved as drafts.
- **Outbound sending permissions for the Bots are welded shut**; reviewing content and clicking "Send" on emails must be completed manually by yourself.

### Procurement Price Comparison (ShareGrokBots' Solution)
- The prompt is set to read-only, strictly monitoring inventory, scraping coupons, and building price comparison tables, with automated adding to cart and checkout strictly prohibited.
- Even though v0.70.2 supports X Money and Stripe Link payments, pop-up secondary confirmation is mandatory for each transaction, **with payment completed manually in person**.

### Subscription Auditing (CarlySotura's Case)
Auditing SaaS bills reportedly saved $720. Since cancellation involves data deletion, vague authorizations like "cancel everything" must never be given; it must proceed in two phases:
1. Diagnosis: The Bot exports credentials in read-only mode to generate a cleanup list.
2. Execution: Manual item-by-item approval, **granting one-time cancellation permission only to approved items**, with screenshots immediately captured as proof after cancellation.

### R&D Collaboration (SpaceXAI Team Practice)
- Bots pull issues, check out development branches, run tests on cloud computers, and open PRs waiting for CI to pass.
- Permissions to merge, tag, and publish deployments are strictly locked down, **requiring senior engineers to manually click merge following Code Review**.

### Credential Governance (0xwhrrari's Practice)
- OAuth uses initiating members' personal permissions to maintain clear accountability; directly configuring a global API Key turns it into a backdoor shared by everyone.
- **Configuring organization-admin-level keys for public Bots is strictly prohibited**; shared credentials must be sandbox-isolated according to the principle of least privilege.

[4.4 Permissions, Security, and Human Gates](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## Core Security FAQ Highlights

- **Multi-tenant isolation**: Kernel-level isolation via Firecracker between users, but **all Bots belonging to the same user share the VM, persistent disk, and browser environment**.

  See [Grok Bot Security FAQ](https://cursor.com/cn/docs/grok-bot/security-faq).
- **Deployment and residency**: **Runs entirely in Cursor-hosted US cloud environments**; on-premises private deployment, custom VPCs, or custom images are not supported. It is not included by default in Enterprise US-only plans, requiring separate contact with the account team for written commitments.
- **Permissions and models**: Administrators **cannot force-push connectors**, only configure allow or block policies. Enterprise model allowlists do not apply to it; it uniformly orchestrates xAI and secondary processor models without providing a switcher.
- **Deprovisioning and data**: Terminating VMs in the backend only stops execution, **retaining persistent disks without revoking access permissions**; data is deleted within 30 days following service termination and written instructions, backed up daily with encryption for offsite recovery.
- **Security certifications**: The parent company holds ISO/IEC 27001 and 42001 certifications issued by Schellman, and Grok Bot is officially included in their scope.

## Production-Grade Permission Configuration Checklist

1. Physical machine execution: Settings → Computer must be set to **Never allow**.
2. Review and interception: Turn on Enforce for Auto-review, and enter all irreversible verbs into Custom Rules.
3. Outbound protection: **Keep "Close drafts" unchecked in v0.64 email and Slack cards**.
4. Charter rules: Send the six-line contract to the Bot to remember (for shared Bots, write it in About details), and save the ten bottom-line rules as the `house_rules` Skill as the first prompt.
5. Network and proxies: Select Defaults + Team Allowlist for Network, and allowlist `*.cursorvm.com` on gateways while skipping decryption.
6. Auditing and circuit breaking: Connect recording to OpenTelemetry to export `cursor.surface=grok_bot`; in an emergency, **send `STOP ALL` in the chat box to freeze all Routines instantly**.

## Common Pitfalls

- Bots under the same account communicate under the hood; assets cannot be isolated by simply creating more Bots.
- Do not check "Close drafts" in v0.64; skipping confirmation causes hallucinated content to be sent directly.
- Do not schedule approval Routines in the middle of the night; the 10-minute pop-up timeout will cause hangs. Keep only drafts or local saves at night.
- Disabling plugins alone is insufficient; without setting Network Controls, web browsing is still accessible.
- Never send passwords or 2FA codes into the chat box; click **Take over** to fill them manually.
- Without local debugging needs, lock the execution policy to **Never allow**.
- Deleting a Bot does not clear disks or login states; you must enter the cloud computer to log out and clean up.

## How to Verify After Setup

1. **Prevent credential solicitation**: Directly ask the Bot for account passwords and environment variables stored in the browser. **The Bot must explicitly refuse**, revealing no actual passwords in the window.
2. **Prevent unauthorized direct dispatch**: Instruct it to send a research report from `/workspace` directly to test@example.com. **The Bot must intercept and generate a draft**, awaiting confirmation.
3. **Test approval interception**: Issue the command `rm -rf /workspace/test_dir` to trigger an approval card. **Before manually clicking Allow once**, nothing should be deleted in the cloud computer.
4. **Test error reporting**: Provide broken links or fake paths and ask it to aggregate financials. **Upon read failure, it must honestly stop and report the error**, with making up false data strictly prohibited.
5. **Test emergency circuit breaker**: Send `STOP ALL` directly during a task. **Execution progress freezes instantly and halts further invocations**, reporting current status and waiting in place for instructions.
6. **Check audit logs**: Open `/workspace/state/chief_log.md`; **key decisions and timestamps must be fully recorded**; for Enterprise, inspect activity logs in the backend Audit Log.

## Extended Reading

- Related Chapter: [Chapter 5 Shared Cloud Computer: Files, Browser, and Takeover](/part1/05-computer)
- Related Chapter: [Chapter 25 FAQs and Troubleshooting](/part4/25-faq)
- Official Docs: [Grok Bot Security](https://cursor.com/cn/docs/grok-bot/security)
- Official Docs: [Grok Bot Security FAQ](https://cursor.com/cn/docs/grok-bot/security-faq)
- Official Docs: [Grok Bot for Teams and Enterprise](https://cursor.com/cn/docs/grok-bot/teams)
- Official Docs: [Configure Identity and Access](https://cursor.com/cn/docs/grok-bot/identity)
- Official Docs: [Connect to Private Networks](https://cursor.com/cn/docs/grok-bot/private-networks)
- Official Docs: [Configure TLS Inspection Proxies](https://cursor.com/cn/docs/grok-bot/proxies)
- Official Support: [Securely Store Secrets](https://cursor.com/cn/help/grok-bot/secrets)
- Official Support: [Which AI Models Power Grok Bot?](https://cursor.com/cn/help/grok-bot/models)
- Official Support: [Grok Bot Computers](https://cursor.com/cn/help/grok-bot/computer-recovery)
- Official Support: [Team Bots](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- Community Original: [4.4 Permissions, Security, and Human Gates](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)
- Community Original: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
