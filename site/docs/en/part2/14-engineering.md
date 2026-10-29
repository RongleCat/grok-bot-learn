# Chapter 14 Case Studies: Engineering and R&D Teams

Stop babysitting tasks locally—**delegate work to the cloud**.

- Shut down your machine anytime while tasks run 24/7, sparing you from waking up at 2 AM to check CI.
- Code in isolated environments, attaching real evidence and logs to pull requests to prevent fake green builds through modified assertions.

Review the **delivery reports in the morning to gatekeep releases**.

## Core Architecture: Division of Labor Among Harness, Model Brain, and Local CLI Agent

![Core Architecture: Division of Labor Among Harness, Model Brain, and Local CLI Agent](/info/14-engineering-s1.png)

### Role Definition and Tripartite Division of Labor
On October 7, 2026, the platform introduced models such as Claude Opus 5.5 for inference. **The system schedules models automatically and does not provide a manual single-request picker**. Do not rely on specific model features; workflows must be strictly constrained by state files and automated verification.

| Role | Host Environment | Permissions & Responsibilities |
| :--- | :--- | :--- |
| Grok Bot | Cloud computer (`/workspace` shared storage) | Runs inspections and dispatches tasks; **generates Draft PRs only, strictly forbidden from pushing directly to default branches or deploying to production** |
| Local CLI Agent | Local terminal or ephemeral container | Pulls dependencies, modifies code on isolated branches, and executes builds |
| Human Lead | Personal workstation | **Holds release keys and production write access**, responsible for architectural decisions and merge approvals |

### Environment Configuration and Security Isolation
All bots under the same account share the same cloud computer, CLI credentials, and browser sessions; **renaming a bot does not provide permission isolation**. Avoid pasting plaintext credentials into chat dialogs during sensitive logins; **always use Take Control to authenticate manually on the remote screen**, leaving the active session in the browser.

### Runtime Environment Self-Check and Persistence
Before onboarding a new repository, run self-check commands in Grok Bot to understand the environment configuration.

::: details Runtime Environment Self-Check and Persistence
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

System dependencies may be reset during updates; only the `/workspace` directory persists across restarts. **All core state must be synchronized to remote remotes via Git or saved in structured files**.

Reference documentation includes the [Grok Bot Official User Guide](https://cursor.com/cn/docs/grok-bot/work) and [Cloud Computer and Application Connection Guide](https://cursor.com/cn/docs/grok-bot/computers).

## Case Study 1: SpaceXAI Team's PR Inspection and Multi-Bot Orchestration

Lingxi Li (@lingxi) at SpaceXAI led 5 R&D bots plus 1 workflow bot, paired with Cursor cloud agent running 24/7.

@poteto on the team merged over 2,000 PRs in a single month, while Lingxi himself delivered iOS v0 in just 3 weeks.

The 5 R&D bots operated in isolated contexts, each monitoring a specific slice of the codebase and invoking designated commands per task:
- Baltata handled iOS and the shared mobile layer, while Craig handled Android.
- Shaoruru managed the desktop client and CI/CD, while Quill maintained the Harness toolchain.
- Hogan specialized in underlying infrastructure and unassigned bugs.
- Visual design routed through `/lingxi-design`, code quality through `/react-native-best-practices`, and architecture through `/lingxi-review`.

Supervisor bot Jenny wrote no code, syncing the runbooks across the team every morning at 5 AM. **Whenever an R&D bot relaxed review standards or delivered unverified changes, Jenny flagged it for an RCA and updated the operational rules**.

Long sessions easily exhaust context limits, so the team stored state in a Notion database and completed the closed loop via scheduled polling:
1. **Half-Hour Polling**: Scans open PRs every 30 minutes to verify Bugbot results, CI errors, and Git conflicts.

   When issues arise, it invokes Cursor to fix them and switches back to Working; once all checks are green, it transitions to Ready for Review. PRs are auto-merged only when confidence is exceptionally high and the change impact is minimal. **Concurrent dispatch capacity per person jumped from 15 to over 200**.
2. **Real-Device Screenshot Alignment**: Code assertions easily miss visual rendering defects. The team repurposed an idle Mac mini as a private worker running iOS Simulator, **using multimodal models to compare actual before-and-after screenshots**, rejecting changes immediately if the visuals do not match.
3. **3 AM Nightly Audit**: Cleans dead code to reduce bundle size, inspects dependency vulnerabilities and CI runtimes, fills in missing internationalization (i18n), validates cross-platform feature parity, and compiles a summary of PRs over the past 24 hours.

> Source: [How Can Engineers Make Good Use of Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Author: [Kin @KinGao476942](https://x.com/KinGao476942)

![How Can Engineers Make Good Use of Grok Bot?](/cases-img/fs25-0.jpg)

![How Can Engineers Make Good Use of Grok Bot?](/cases-img/fs25-1.jpg)

**Never let a single bot carry long sessions**. Split roles by business domain, assign a dedicated reviewer to iterate on rules, and track state in a dashboard for diff verification—it saves tremendous effort.

- [How Can Engineers Make Good Use of Grok Bot? | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [Grok Bot for Engineering | Lingxi Li](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## Case Study 2: Deconstructing R&D Work and Lauren's Nine-Category Checklist

### How It Works
Lauren (@poteto) merged 2,500 production PRs in a single month, while Jacob Gold (@jacobgold) averaged nearly 250 per day; both deconstructed engineering tasks into nine parallel tracks.

| Risk Level | Typical Scope & Rules | Review Method |
| :--- | :--- | :--- |
| Low to Medium | Dead code cleanup, unit tests, and type fixes | Auto-merge |
| High Risk | Core business logic, authentication, and data migrations | Mandatory human review |

**The moment a diff exceeds the intent of the original prompt, the system immediately escalates it for human approval.**

### Key Takeaways
Mai Yang (@MaiYangAI) generated 1,020 commits in ContextEcho over six months, opening PRs only 18 times. **Solo projects have a minimal blast radius; fabricating artificial PRs without real necessity creates zero value.**

> Source: [What Is the Point of Hundreds of PRs a Day? I Followed SpaceXAI Engineer Lauren's (@poteto) Nine Categories to Deconstruct My Own Work](https://x.com/MaiYangAI/status/2108519046446727633)  
> Author: [Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
Start with bug fixes and code styling/refactoring, accompanied by input constraints and acceptance criteria. **Save the mental energy spent reading code by eye and redirect it toward defining direction, boundary constraints, and testing.**

[What Is the Point of Hundreds of PRs a Day? I Followed SpaceXAI Engineer Lauren's (@poteto) Nine Categories to Deconstruct My Own Work](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## Case Study 3: 24/7 Repo Ops Desk

![Case Study 3: 24/7 Repo Ops Desk](/info/14-engineering-s3.png)

### Who Built It and What It Does
Independent developer Gipp 🦅 (@gippp69) designed a 24/7 Repo Ops Desk while maintaining multiple open-source and commercial repositories. The system combines concurrent sub-agents to monitor anomalies at the base level, while orchestrating 6 named roles via Grok Bot at the top level to process issues and CI failures.

According to the author, a single developer can typically oversee only 2 to 3 repositories manually. An automated ops desk, by contrast, monitors hundreds of change points across multiple repositories simultaneously.

### How It Works

::: details How It Works
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

1. **Deploy 6 Dedicated Bots**
   - Triage Bot: Categorizes issues by severity and type.
   - Fix Bot: Handles minor bugs, writes patches, and submits Draft PRs.
   - Test Bot: Executes tests to catch flaky tests and records failure context.
   - Dependency Bot: Monitors CVE vulnerabilities and outdated dependencies.
   - Release Bot: Organizes changelogs and bundles releases upon command.
   - Alert Bot: Dispatches instant notifications when human intervention is needed.

2. **Lock Down Permissions via a Routing Table**

| Permission Level | Monitoring Scope | Role and Action |
| :--- | :--- | :--- |
| `auto-fix` | Flaky tests, lint errors, and formatting | Fix Bot submits patches |
| `triage` | Uncategorized complex bugs and feature requests | Triage Bot escalates to humans |
| `security` | Medium- to high-risk CVE vulnerabilities | Dependency Bot forwards to Alert Bot upon detection |
| `release` | Version changes and release notes | Release Bot executes upon instruction |

3. **Uphold Three Strict Red Lines**
   - Never touch business logic: `auto-fix` changes are strictly confined to the failing test file itself or its direct imports; modifying core code is strictly forbidden.
   - Never auto-merge: Fix Bot opens only Draft PRs tagged with `auto-fix`, never auto-merging.
   - Canary run for one week: Run for a week in a single low-risk edge repository to evaluate the adoption rate (merged vs. discarded count) before rolling out to main repositories once stable.

### Key Takeaways

> Source: [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> Author: [Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**The ops desk troubleshoots errors in the middle of the night without making decisions**. Prompts and permissions are strictly locked to "only open Draft PRs, never modify business logic," allowing the system to run safely unattended.

For detailed configuration, see [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) | Gipp 🦅](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh).

## Case Study 4: Engineering Harness Based on State Machines and Multi-Bot Collaboration

![Case Study 4: Engineering Harness Based on State Machines and Multi-Bot Collaboration](/info/14-engineering-s4.png)

### Who Built It and What It Does
Developers Mori (@0xjmori), Morlex (@0xMorlex), and solopreneur architect beamnxw designed a standardized R&D collaboration pipeline. By establishing state machine contracts, a unified directory structure, and a six-field task board in the cloud, they implemented an end-to-end fix pipeline where 1 lead orchestrates 4 specialists.

The entire system decomposes complex code changes into state transitions backed by verifiable evidence. This design ensures that every handoff across stages is fully documented and auditable.

### How It Works

1. **Establish a Structured Workspace Directory**
Initialize the project in the Grok Bot cloud computer `/workspace`, placing each issue into an isolated directory `/workspace/devdesk/issues/<issue-id>/`.

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**Each directory must contain 6 standard files:**
- `task.md`: Original input and completion acceptance criteria
- `status.json`: Current machine-readable state and assignee
- `evidence/`: Directory storing failure logs, reproduction scripts, and screenshots
- `implementation.md`: Modified file manifest and minimal implementation plan
- `review.md`: Independent review conclusion
- `handoff.md`: Sign-off handoff report delivered to humans

2. **State Machine Transition Contract**
**The pipeline advances sequentially through predefined states; skipping steps is strictly forbidden.**

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage (`NEW` ──> `REPRODUCED`)**: Must provide reproducible steps and an executable failing test case.
- **Builder (`BUILDING` ──> `TESTED`)**: Dispatches a Cursor agent to modify code on a fresh branch and ensures regression tests pass.
- **Reviewer (`REVIEWING` ──> `REVIEW_PASSED`)**: Independently reviews diffs and logs to assign a rating. **A FAIL immediately sends the task back to `BUILDING` for rework, with a maximum of 2 retries.**
- **Release (`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`)**: After all checks pass, submits a Draft PR accompanied by complete evidence to the human engineer.

3. **Action Reversibility Grading**
**The system delineates approval permissions based on whether an action is reversible.**

| Operation Category | Permission Policy | Scope of Actions and Behaviors |
| :--- | :--- | :--- |
| **Reversible Actions** | Autonomous execution | Performing code analysis, writing patches and running unit tests on local branches, generating failing test cases, opening Draft PRs, and generating log reports |
| **Irreversible Actions** | Halt and await human review | Merging code into the default branch, deploying to production, modifying production databases, altering environment variables or secrets, calling billable external services |

4. **Board and Skill Solidification**
The board columns are strictly fixed to `Task | Owner | Source | Status | Deliverable | Next action`.
Task statuses are strictly restricted to five states: `ready`, `working`, `blocked`, `awaiting approval`, and `complete`.
**Once a type of task succeeds once, solidify it as a private Skill via command**, enabling routine schedules to invoke it repeatedly.

### Key Takeaways

> Source: [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> Author: [Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

Never let multiple agents chat casually in unstructured group conversations.

1. **If the previous step produced no test evidence, never start the next step**. Lock down progress using disk directories and state machines.
2. **Distinguish action reversibility** to balance automation velocity with production safety baselines.

For detailed implementation, refer to [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf), [Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps | Morlex](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh), and [Grok Bot Engineering: Set Up a Harness for Your One-Person Company | beamnxw ./](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm).

## Out of the Box: Engineering R&D Prompt Library

The following prompts are all verified in production. Copy and send them directly to your bots and ask them to remember them; for shared bots, paste them into the About details:

### 1. Architecture Master Charter (Chief)
**Send to the supervisor bot and ask it to remember it** (for shared bots, write to About details) to oversee workflows and log state.

::: details 1. Architecture Master Charter (Chief)
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

### 2. Bug Reproduction Specialist (Triage)

Paste directly **into Triage Bot** to investigate bugs and write failing test cases.

::: details 2. Bug Reproduction Specialist (Triage)
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

### 3. Coding Specialist (Builder)
Paste the prompt into **Builder Bot** to run on an isolated branch.

::: details 3. Coding Specialist (Builder)
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

### 4. Independent Review Specialist (Reviewer)
Paste the prompt into Reviewer Bot for **strict acceptance testing**.

::: details 4. Independent Review Specialist (Reviewer)
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

### 5. Delivery Specialist (Release)
**Paste the prompt into Release Bot** to aggregate artifacts and handle handoff:

::: details 5. Delivery Specialist (Release)
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

### 6. Engineering Night Shift Routine

Configure a scheduled routine in Grok Bot, **selecting Chief as the execution owner**.

::: details 6. Engineering Night Shift Routine
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

### 7. Reversibility Guardrails and Safety Red Line Directives

**Paste directly at the end of each bot's long-term rules** (send in chat for personal bots to remember; write into About details for shared bots).

::: details 7. Reversibility Guardrails and Safety Red Line Directives
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

## Common Pitfalls

### Automatic Model Matching
The backend automatically routes to underlying models such as Claude Opus 5.5, with no manual picker available. **Write transition conditions into structured files like `status.json` and validate them via strict scripts**; do not rely on models to maintain consistent output styles.

### Shared Environment Conflicts
All bots share `/workspace` on the cloud computer. **Each issue must use an isolated subdirectory and Git branch**; spawn a Cursor cloud agent when modifying code, and strictly avoid sharing uncommitted working trees.

### Review Deadlocks and Tampered Tests
When a fix fails, Builder can easily fall into an infinite loop or even tamper with test assertions to fake a green build. **Strictly limit retries for a single issue to 2 rounds**, immediately escalating to human review if exceeded. Reviewer must inspect Git diffs of test cases; any modified assertions must be marked as FAIL immediately.

### Subscription Quotas and Polling
Usage follows The X Subscription effective October 12, 2026, sharing a weekly quota pool across Grok and Cursor, with overages billed through Cursor.

Avoid 5-minute full repository sweeps; **set scheduled routines to once daily or nightly**, relying primarily on the `agent-ready` label for triggers.

| Subscription Tier | Monthly Price | Quota Multiplier | Includes Grok Bot |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | Bot Not Included |
| **Premium** | $30 / mo | 4x quota | Included |
| **Super** | $100 / mo | 15x quota | Included |
| **Ultra** | $200 / mo | 50x quota | Included |

### Branch Protection and Draft PRs
**Agent deliverables must be submitted exclusively as Draft PRs and are strictly prohibited from auto-merging into the default branch**. GitHub Branch Protection Rules must enforce three strict constraints:
- Prohibit direct pushes to the main or master branch
- Require at least one human approval (Approvals)
- Require existing CI pipelines to pass completely

### Preventing Sensitive Credential Leaks
Chat dialog content enters the model context; **never enter passwords, private keys, or API keys into prompts**. Access private systems via connectors in settings, or use Take Control remote desktop on Agent Computer to log in manually.

## Acceptance Verification

**Never roll this out across core production projects right from the start.**

### Single-Repo, Single-Bug Cold Start Acceptance
- Pick an edge repository, create `/workspace/devdesk/`, and tag a minor bug with `agent-ready`.
- Run the Chief workflow and verify that Triage saves reproduction logs and unit tests under `evidence/`.
- Verify that Builder modifies code on an isolated branch without touching main branch code, and that Reviewer provides line-number-level logic verification.
- **Confirm that only a Draft PR is created in the end**, leaving the main branch completely untouched.

### Metric Quantification and Patch Adoption Rate Inspection
- If the adoption rate is **below 70%, pause onboarding a second repository** and tighten prompt constraints.
- The morning report must allow you to clearly review qualified PRs, blocked items, and pending issues **within 3 minutes**; having to read through thousands of words of chat history is considered failing the criteria.
- Ensure early-morning scheduled tasks sleep when not triggered and terminate automatically upon timeout to avoid quota blowouts.

### Safety Red Lines and Permission Interception Drills
- Deliberately submit an issue that modifies schema migrations or authentication logic to verify that the task is intercepted and suspended.
- Have the bot run `git push origin main`, and verify that **branch protection successfully blocks it**.
- For external communications and configuration changes, verify that Auto-review is set to **Ask first**.

## Further Reading

### Official Documentation and Feature Pages
- [Grok Bot Official User Guide](https://cursor.com/cn/docs/grok-bot/work)
- [Cloud Computers and Application Connections](https://cursor.com/cn/docs/grok-bot/computers)
- [Model Selection and Routing Guide](https://cursor.com/cn/help/grok-bot/models)
- [Plans, Billing, and On-Demand Usage Help](https://cursor.com/cn/help/grok-bot/plans)
- [Settings and Security Specifications](https://cursor.com/cn/docs/grok-bot/settings)
- [Team Collaboration and Team Bots Configuration](https://cursor.com/cn/docs/grok-bot/teams)

### Original Community Case Studies

> Source: [Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> Author: [Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [How Can Engineers Make Good Use of Grok Bot? | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [Grok Bot for Engineering | Lingxi Li](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [What Is the Point of Hundreds of PRs a Day? I Followed SpaceXAI Engineer Lauren's (@poteto) Nine Categories to Deconstruct My Own Work](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) | Gipp 🦅](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps | Morlex](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [Grok Bot Engineering: Set Up a Harness for Your One-Person Company | beamnxw ./](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)
