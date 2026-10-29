# 제19장 팀 오케스트레이션: 헌장, 역할 및 권한 위임

한 번에 여러 전담 Bot을 생성하면 가짜 데이터를 서로 참조하기 쉬워, 결국 5개 창에서 수동으로 내용을 옮겨 적게 됩니다. **동일 계정의 모든 Bot은 동일한 클라우드 PC 가상 머신(VM)에서 실행되며**, 디스크, 브라우저 세션 및 크레딧 풀을 공유하므로 데이터 격리가 존재하지 않습니다.

1. **1+N 스타 허브 구성**: 메인 Bot이 라우팅을 담당합니다.
2. 6줄 계약과 10대 기본 규칙으로 책임을 명확히 고정하고, 인간 승인 게이트를 추가합니다.
3. 클라우드 PC 공유 디렉터리를 통한 파일 기반 인수인계를 진행하며, 4주간의 권한 위임 템포 및 5가지 표준 루틴과 연계합니다.

[《4.2 팀 오케스트레이션: 헌장, 역할 및 권한 위임》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![팀 오케스트레이션: 헌장, 역할 및 권한 위임](/info/19-orchestration.png)

## 1. 메인 Bot과 전담 Bot: 1+N 스타 허브 아키텍처

![1. 메인 Bot과 전담 Bot: 1+N 스타 허브 아키텍처](/info/19-orchestration-s1.png)

다중 Bot 환경에서는 1+N 아키텍처를 적용하여, **메인 Bot이 대화 입구를 독점하도록 하고** 전담 Bot은 실행만 담당하게 합니다.

- 가상 머신, `/workspace`, 커넥터(Settings → Plugins / Connect Apps) 및 Skill을 공유하며, 1:1 대화(DM) 및 Routine은 독립적입니다.

1. 좌측에 '비서실장(Chief of Staff)'을 생성하고 스타(즐겨찾기)로 설정합니다(우클릭으로 변경 가능). v0.66.0(2026-10-02)부터 선제적 제안을 지원합니다.
2. **메인 Bot의 비즈니스 코드 작성은 엄격히 금지됩니다.** 분해 및 할당만 담당해야 하며, 조율자가 직접 실무 작업을 하면 포커스를 잃게 됩니다.
3. 요구사항은 비서실장에게만 전달하고, 다운스트림은 5줄 이내의 브리핑으로 회신하며 평소에는 침묵을 유지합니다.

| 구분 | 메인 Bot(스타) | 전담 Bot |
|---|---|---|
| 역할 정의 | 작업 허브, 비즈니스 코드를 작성하지 않음 | 전문 실행, 코드 작성 및 테스트 첨부 가능 |
| 인터랙션 | 매일 능동적으로 브리핑 발송 | 사용자에게 먼저 1:1 대화를 보내지 않음 |

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. 헌장 템플릿: 직무 기술서를 계약서 형식으로 작성하기

### 개념
**헌장은 장기적인 계약입니다.** 개인 Bot의 경우 대화창에 전송하여 기억하도록 하고, 공유 Bot의 경우 상세 정보(About)의 Description에 작성합니다. 사이드바에는 더 이상 Edit Profile이 없습니다.

- '카피라이팅의 달인'과 같은 형용사는 쓰지 마십시오. 경계가 모호하면 환각(할루시네이션)이 발생하기 쉽습니다.
- **반드시 계약서처럼 작성해야 하며**, 동사를 사용하여 책임, 산출물 형식, 인간 승인 게이트, 중단 기준을 명확히 규정해야 합니다.

### 실행 방법
1. **6줄 규약 작성**: 개인 Bot의 경우 규약을 대화창에 전송하여 기억하도록 하고, 공유 Bot의 경우 상세 정보(About)의 Description에 입력합니다.

```text
Own: 负责需求的统一拆解、分派、汇总与五行简报汇报。
Sources: 人工下发的指令、项目看板文件。
Output: 纯文本状态摘要，超出五行时输出为指定文件路径。
Approval: 任何对外通信、采购、删除操作必须暂停等待确认。
Failure: 下游专职 Bot 报错时如实上报，不使用过期数据假装完成。
Never: 永远不直接编写业务代码，不擅自修改生产配置。
```

2. **비서실장 헌장 구성**: **먼저 `{your name}`을 변경한 후**, 비서실장의 Description에 붙여넣습니다.

::: details 실행 방법
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

3. **10대 기본 규칙(가훈) 저장**: 첫 번째 지시로 메인 Bot에 전달하고, 공용 Skill(`house_rules`)로 저장하며, 각 규칙마다 **30초 테스트 케이스**를 연결합니다.

::: details 실행 방법
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

### 완료 및 검증 기준
Description과 기본 규칙을 설정한 후, 모호한 지시를 보내 테스트합니다(예: "지난주 데이터 정리해서 발송해 줘").

**합격 기준**:
- 데이터 출처를 능동적으로 재확인
- 작업을 할당할 역할 나열
- **발송 전 명시적으로 인간 승인 대기**

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. 역할 분할 방법: 비즈니스 단계 및 리스크 경계에 따른 분할

### 개념
**역할을 분할하는 목적은 컨텍스트 오염 방지입니다.** 온갖 잡무가 뒤섞이면 추론 능력이 무너집니다.

- **통합**: 입력 형식, 권한 및 주기가 일치하는 경우, 단일 Bot에 Skill을 연결합니다.
- **분할**: 프로세스가 장기적으로 갈리거나 고위험 작업을 다룰 때만 독립 Bot을 생성합니다.

### 실행 방법

1. **3가지 체크리스트 확인**: 컨텍스트 충돌, 툴 권한 격리를 점검하고, 읽기 전용과 자금·삭제 등 비가역적 리스크를 명확히 구분합니다.
2. **실제 직무명으로 명명**: '어시스턴트' 대신 구체적인 직책명을 사용하고, Description에 자동 실행 가능 여부를 동사로 명확히 명시합니다.
3. **최대 6인 마지노선 준수**: 단일 채널당 최대 **스페셜리스트 5명 + PM 1명**으로 제한합니다. 새로운 요구사항은 기존 Bot의 Skill 확장을 우선 고려하며, 신규 생성 시에는 반드시 인간의 승인을 거쳐야 합니다.

### 사례 및 실무 참고
캡틴 1명이 12개의 전담 Bot을 이끌며, **역할 권한을 엄격히 제한**합니다:
- 광고: 목록만 제출하며, 관리자 페이지 설정 및 입찰가는 수정하지 않음
- 카피라이팅: 초안만 작성하며 실제 게재하지 않음
- 크롤링: 데이터 조회만 수행하며, 계정 정지 방지를 위해 **장바구니 담기 및 주문은 엄격히 금지**

역할 정의를 위해 메인 Bot에 전송하는 인터뷰 프롬프트:
::: details 사례 및 실무 참고
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
엔드투엔드 팀 설계를 위해 전송하는 기획 프롬프트:
::: details 사례 및 실무 참고
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

### 완료 및 검증 기준

**맹목적으로 Bot을 늘리지 말고**, 시나리오에 따라 분할 여부를 결정해야 합니다.

| 비즈니스 시나리오 | 권장 방식 | 판단 근거 |
| :--- | :--- | :--- |
| 동일 데이터 소스 기반의 서로 다른 분석(예: 크롤링 후 트렌드 및 이상치 분석) | 동일한 Bot에 다른 Skill 연결 | 데이터 소스와 툴체인이 동일하여 컨텍스트를 끊을 필요가 없음 |
| 생산 및 최종 검토(예: 코드 작성 및 머지 리뷰) | **독립된 전담 Bot으로 분할(Builder 및 Reviewer)** | 작성자가 자체 검토할 수 없으며, 누락 방지를 위해 독립된 시각 필요 |
| 내부 초안 작성 및 외부 발행(예: 이메일 초안 작성 및 대량 발송) | 초안 작성 Bot과 발행용 인간 게이트로 분할 | **외부 발송은 되돌릴 수 없으므로(비가역적), 단일 차단 지점 필수** |
| 간헐적 저빈도 작업(예: 비정기적 스프레드시트 변환) | 메인 Bot에서 임시 실행, 새로 생성하지 않음 | 관리 비용 증가 및 통제 불능 리스크 방지 |

[《Bot 하나에서 조직 전체로, Grok Bot 고급 활용법 공유: 로컬 PC, AI 분업 및 지식베이스 연동 방법》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg); [《비전공자를 위한 전자동 Agent 팀 구축, Grok Bot 개통부터 멀티 AI 협업까지 전 과정 【만자 장문】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. 권한 위임 단계: 인간 게이트 기준선과 4주 전환 템포

![4. 권한 위임 단계: 인간 게이트 기준선과 4주 전환 템포](/info/19-orchestration-s4.png)

다중 Bot 오케스트레이션에서 권한 위임은 오직 **1분 내 가역성**만을 기준으로 삼습니다. 1분 이내에 원클릭으로 완벽히 되돌릴 수 없는 작업은 모두 고위험으로 간주하여 반드시 인간 게이트를 설정하고 팝업 확인을 기다려야 합니다.

클라이언트 경로 `Settings → General → Auto-review`에서 리스크에 따라 두 가지 목록으로 구분합니다:
- **Ask first 필수 항목**: `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- **Always allow 승인 항목**: 공개 웹페이지 읽기 전용 검색, 인가된 파일 읽기, `/workspace`에 초안 및 중간 데이터 쓰기.

여기에는 두 가지 엄격한 제한이 있습니다. v0.70.2부터 Bot이 독립된 이메일 계정을 할당받을 수 있지만, **메일 발송 전 반드시 초안 카드에서 수동 승인을 거쳐야 합니다.** 작업이 Claude Opus 5.5 등의 모델로 라우팅될 수 있더라도 승인 기준선은 동일하게 유지해야 합니다. **신규 팀은 첫날부터 야간 무인 운영을 시작해서는 안 되며**, 4주 템포에 맞춰 단계적으로 전환해야 합니다.

::: details 4. 권한 위임 단계: 인간 게이트 기준선과 4주 전환 템포
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

| 권한 위임 등급 | 해당 주기 | 자율 실행 허용 | 강제 인간 게이트 작업(팝업 승인) | 검수 기준 |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1(초안 단계)** | 1주 차 | 지정 문서 읽기, 공개 웹 검색, 서식 정리 | 외부 발송, 프로덕션 시스템 쓰기 | 산출물의 100%가 초안이며 출처 링크 포함 |
| **Level 2(제어 단계)** | 2주 차 | 실행 매개변수 생성, 사전 설정된 Skill 호출 | 단계별 클릭 승인, 외부 툴 제출 | 승인 카드에 트리거된 규칙과 해당 Bot이 정확히 표시됨 |
| **Level 3(위탁 단계)** | 3주 차 | 정해진 프로세스 내 자동 읽기/쓰기 진행 | Ask first 동사 트리거, 외부 시스템 에러 | 정상 루틴은 원활히 진행되며 고위험 작업은 100% 일시 중단 대기 |
| **Level 4(감사 단계)** | 4주 차 | 주기적 예약 작업, 역할 간 파일 릴레이 | 자금 이체, 공식 성명 발표, 인프라 설정 변경 | 주말 리뷰 주간 보고서에 리소스 소모 및 이상 항목이 정확히 반영됨 |

[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd); [《4.2 팀 오케스트레이션: 헌장, 역할 및 권한 위임》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. 인수인계 규격: 파일 기반의 원활한 전달 및 상태 영속화

![5. 인수인계 규격: 파일 기반의 원활한 전달 및 상태 영속화](/info/19-orchestration-s5.png)

동일한 계정의 Bot은 모두 같은 가상 머신(VM)에서 동작하므로, **업무 인수인계는 반드시 `/workspace` 절대 파일 경로를 통해 이루어져야 합니다.** 그룹 대화창에 장문의 텍스트를 전송하지 마십시오. 대화 기록이 늘어나 토큰을 배로 소모할 뿐만 아니라, 서식이 깨져 다운스트림 Bot이 잘못 해석할 위험이 있습니다.

### 작업 흐름
1. 작업 공간 경로 통일: `/workspace/project-alpha/`에 전용 디렉터리를 생성하고, 협업 Bot들이 모두 이곳에서 읽고 쓰도록 통일합니다.
2. 산출물 파일 생성: 업스트림 Bot이 처리를 완료한 후 `research.md` 또는 `data.json`으로 저장하며, 헤더에 타임스탬프, 데이터 소스 링크, 담당 Bot을 명시합니다.
3. 파일 경로 전달: 선행 Bot은 비서실장에게 절대 경로만 반환하고, 비서실장이 이를 후행 Bot에 할당하여 읽도록 합니다. **대화창에 전문을 붙여넣는 행위는 엄격히 금지됩니다.**
4. 의사결정 기록 및 저장: 비서실장은 각 할당 결정, 건너뛴 이유, 승인 대기 항목을 모두 `/workspace/state/chief_log.md`에 기록합니다.

### 커뮤니티 실전 패턴
| 사례 및 출처 | 협업 프로세스 | 핵심 벤치마킹 포인트 |
| :--- | :--- | :--- |
| 트윗 페르소나 사이트(@0xlangeai) | 4개의 전담 Bot이 순차적으로 `/workspace/tweet-portrait/`을 읽고 쓰며 코드 및 스크린샷 생성 | 파일 경로만 참조, 수동 전송 제로 |
| 바이럴 콘텐츠 수집(xilo @xilo2991) | 수집 및 주제 선정을 Feishu 시트에 작성, 원고는 로컬에 저장, 운영자가 일정에 맞춰 발행 | 스프레드시트 비동기 버퍼링, 인간의 비동기 교차 검토 |
| 크로스보더 이커머스 진단(Zach @1999Zach22) | 캡틴이 작업을 할당하고, 스페셜리스트가 문서에 방안을 보완하며, 인간이 Feishu 코멘트로 확인 | **전담 Bot은 승인 대기 제안만 작성하며, 절대 권한을 넘지 않음** |

### 검수 기준
업스트림 전달 파일에는 **반드시 표준 메타데이터 헤더가 포함되어야 합니다**:

::: details 검수 기준
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

- 다운스트림 Bot은 파일 경로만으로 독립적으로 파싱하고 후속 작업을 시작할 수 있어야 하며, **대화창에서 사람이 배경 설명을 다시 보충해 줄 필요가 없어야 합니다.**

[《4.2 팀 오케스트레이션: 헌장, 역할 및 권한 위임》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh); [《비전공자를 위한 전자동 Agent 팀 구축, Grok Bot 개통부터 멀티 AI 협업까지 전 과정 【만자 장문】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. 팀 확장 템포 및 루틴 유지관리: 단일 허브에서 다중 역할 운영으로

### 개념
루틴(Routine)은 상태 영역의 '상세 정보(Details)'에서 설정합니다.

- 잘못된 로직이 매시간 실행되면, **백그라운드에서 일주일에 168회나 오작동**하게 됩니다.
- 2026-10-12부터 The X 통합 구독(Premium 월 $30, Super 월 $100, Ultra 월 $200)은 주 단위로 공유 크레딧을 차감하므로, **고빈도로 헛돌 경우 며칠 만에 크레딧이 소진**됩니다.

### 실행 방법
1. **메인 Bot의 초기 루틴은 3~5개로 제한**하고, 비서실장에게 전달하여 고정합니다:

아침 브리핑(평일 07:00)
::: details 실행 방법
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
주간 리뷰(매주 금요일 16:00)
::: details 실행 방법
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
유효성 감사(매월 첫째 주 월요일 09:00)
::: details 실행 방법
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
누락 방지 알림(이벤트 트리거)
::: details 실행 방법
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
일일 마감 인수인계(매일 18:00)
::: details 실행 방법
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **주차별 단계적 확장**:
- 1주 차: 비서실장 1명만 유지하고, 아침/저녁 보고를 완전히 작동시키며, Description을 정비하고 기본 규칙을 검증합니다.
- 2주 차: 병목 구간에 맞춰 전담 Bot 1개를 추가하고, 클라우드 PC 공유 디렉터리를 생성하여 인수인계를 테스트합니다.
- 3주 차: 다운스트림 Bot을 연결하여 파이프라인을 가동하고, 작업 동작을 Skill로 고정합니다.
- 4주 차 이후: 상주 스페셜리스트는 5명 이내로 제한하고, 월간 감사를 통해 불필요한 타이머(루틴)를 정리합니다.

3. **금요일마다 15분씩 정기 유지관리 수행**:
- `/workspace/state/reviews/YYYY-WW.md`를 확인하여 산출물 활용률을 점검합니다.
- 리스크가 없고 자주 승인하는 작업은 Ask first에서 Always allow로 이동합니다.
- 아무도 보지 않는 무효한 Routine을 종료하여, **헛돌면서 주간 크레딧이 낭비되는 것을 방지**합니다.

### 완료 및 검증 기준
- **07:00 아침 브리핑이 정시에 발송**되며, 핵심 항목이 3개를 넘지 않음
- **금요일 16:00 주간 보고서가 정시에 생성됨**
- **18:00 이후에는 시스템이 조용히 유지**되며, 매주 금요일 크레딧 소모가 안정적이고 비정상적인 야간 사용량 급증이 없음

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. 자주 빠지는 함정(주의사항)

1. **한 번에 대여섯 명의 어시스턴트를 만들지 마십시오**: 구체적인 비즈니스 동사 3개로 요약할 수 없다면, 메인 Bot의 Skill로 직접 통합하십시오.
2. **입구 매니저에게 무거운 실무 작업을 맡기지 마십시오**: 긴 문서를 작성하거나 수천 줄의 코드를 작성하게 하면 허브의 작업 분해 및 할당 능력이 마비됩니다.
3. **동일 계정 Bot은 클라우드 PC를 공유합니다**: 물리적 격리가 없으므로 은행 비밀번호나 민감한 데이터를 절대로 저장해서는 안 됩니다.
4. **긴 인수인계 내용은 반드시 클라우드 PC 파일 경로를 거쳐야 합니다**: 그룹 대화에 장문을 올리면 주간 크레딧 풀이 순식간에 소진됩니다.
5. **단일 단계가 안정적으로 동작하기 전에 고빈도 루틴을 설정하지 마십시오**: 예를 들어 매시간 크롤링하도록 설정했는데 제대로 동작하지 않으면 **일주일에 168회나 헛돌게 됩니다**.
6. **헌장에 '출처 없이는 숫자를 제시하지 말 것'을 명시하십시오**: 전담 Bot은 정보가 부족할 때 자신 있게 데이터를 지어내곤 합니다.
7. **SNS의 과장 광고를 맹신하지 마십시오**: 수십 개의 Bot, 수천 개의 PR, 1,100달러 수익 등은 대부분 검증되지 않은 경우가 많으므로, **실제 결과물의 품질을 기준으로 판단하십시오**.

[《4.2 팀 오케스트레이션: 헌장, 역할 및 권한 위임》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. 완료 후 검수 방법

### 비서실장 단독 검수(1주 차)
- 좌측 사이드바를 확인하여, 비서실장 프로필에 **노란색 스타 표시 및 상단 고정**이 되어 있어야 합니다. 6줄 계약 또는 이행 헌장을 기억하고 있어야 합니다(개인 Bot은 대화에서 확인, 공유 Bot은 상세 정보 About에서 확인).
- 데이터 소스가 연결되지 않은 매출 정보(예: "지난주 비즈니스 이익이 얼마인가요?")를 질문했을 때, **추측은 엄격히 금지되며, 가져올 수 없다고 사실대로 답변해야 합니다**.
- "`/workspace/state` 디렉터리 아래의 로그를 삭제해 줘"라고 보냈을 때, **정확하게 일시 중단하고 수동 승인을 요청해야 합니다**. 작업 진행 중 "STOP ALL"을 전송하면 즉시 중단하고 중단 지점을 보고할 수 있어야 합니다.

### 역할 분할 및 파일 인수인계(2주 차)
- 전담 Bot이 업무 경계를 숙지하고 있는지, 업스트림 및 다운스트림 인수인계 대상을 명시하고 있는지 확인합니다(공유 Bot은 상세 정보 About 확인).
- 복합 작업(예: 경쟁사 크롤링 및 분석)을 할당했을 때, 업스트림은 `/workspace/project-alpha/`에 타임스탬프와 출처가 포함된 파일을 생성해야 합니다.
- **다운스트림은 파일 경로만으로 독립적으로 실행될 수 있어야 하며, 사람이 창에서 내용을 복사해 줄 필요가 없어야 합니다.** `/workspace/state/chief_log.md`를 확인하여 모든 할당 및 건너뜀이 기록되었는지 확인합니다.

### 권한 위임 인간 게이트 및 루틴 운영관리(3~4주 차)
- `Settings → General → Auto-review`로 이동하여 `Ask first` 목록에 `send`, `post`, `buy`, `transfer`, `delete`, `permissions`가 유지되고 있는지 확인합니다.
- 외부 전송 의도를 테스트할 때 **반드시 일시 중단되고 Bot 이름과 규칙 출처가 표시된 승인 카드가 팝업되어야 하며**, 읽기 전용 검색은 팝업 없이 자율 실행되어야 합니다.
- 평일 07:00에 아침 브리핑, 18:00에 인수인계 보고를 수신(특이사항 없으면 조용히 유지)하고, 금요일 16:00에 `/workspace/state/reviews/YYYY-WW.md`를 확인하여 **주간 보고서가 생성되었으며 크레딧 소모가 공유 풀 범위 내에 있는지 확인합니다**.

[《4.2 팀 오케스트레이션: 헌장, 역할 및 권한 위임》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 추가 참고 자료

### 관련 챕터

- [제9장 그룹 대화 및 팀 Bot: Bot 하나에서 Bot 그룹으로](/part1/09-group-team)
- [제24장 역할별 AI 팀 구성하기](/part4/24-roles)

### 공식 제품 및 문서
- [Grok Bot 공식 업데이트 로그](https://x.ai/changelog/bot)
- [Grok Bot 공식 문서 저장소](https://docs.x.ai/grok-bot/bots)

### 커뮤니티 실전 자료 출처
- [《4.2 팀 오케스트레이션: 헌장, 역할 및 권한 위임》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach: [《Bot 하나에서 조직 전체로, Grok Bot 고급 활용법 공유: 로컬 PC, AI 분업 및 지식베이스 연동 방법》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo: [《비전공자를 위한 전자동 Agent 팀 구축, Grok Bot 개통부터 멀티 AI 협업까지 전 과정 【만자 장문】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn: [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
