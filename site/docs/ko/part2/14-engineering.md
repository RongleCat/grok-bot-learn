# 제14장 사례: 엔지니어링 및 R&D 팀

로컬에서 일일이 감시하지 말고, 작업을 **클라우드에 호스팅**하세요.

- 컴퓨터를 언제든 끄더라도 24시간 가동되므로, 새벽 2시에 일어나 CI를 확인할 필요가 없습니다.
- 격리된 환경에서 코딩하고 풀 리퀘스트에 실제 증거와 로그를 첨부하여, 어설션만 수정해 억지로 테스트를 통과시키는 편법을 방지합니다.

아침에 **인도 보고서를 검토하고 배포 여부를 결정**하세요.

## 핵심 아키텍처: Harness, 모델 브레인 및 로컬 CLI Agent 역할 분담

![핵심 아키텍처: Harness, 모델 브레인 및 로컬 CLI Agent 역할 분담](/info/14-engineering-s1.png)

### 역할 정의 및 3자 분업
2026년 10월 7일 플랫폼에 Claude Opus 5.5 등의 모델이 추론에 도입되었습니다. **시스템이 모델을 자동으로 스케줄링하며, 수동 단일 선택기는 제공되지 않습니다**. 단일 모델의 특성에만 의존하지 말고, 프로세스는 상태 파일과 자동화된 검증으로 확실하게 제어해야 합니다.

| 역할 | 실행 호스트 | 권한 및 책임 |
| :--- | :--- | :--- |
| Grok Bot | 클라우드 컴퓨터(`/workspace` 공유 스토리지) | 정기 점검 실행 및 작업 분배, **Draft PR만 생성하며 기본 브랜치로의 직접 푸시 또는 배포 엄격히 금지** |
| 로컬 CLI Agent | 로컬 터미널 또는 임시 컨테이너 | 독립 브랜치에서 의존성 설치, 코드 수정 및 빌드 실행 |
| 엔지니어링 리드(사람) | 개인 워크스테이션 | **배포 키 및 프로덕션 쓰기 권한 보유**, 아키텍처 결정 및 병합 승인 담당 |

### 환경 구성 및 보안 격리
동일한 계정 아래의 모든 Bot은 동일한 클라우드 컴퓨터, 명령줄 자격 증명 및 브라우저 세션을 공유하므로, **Bot의 이름을 바꾸는 것만으로는 권한 격리 효과가 없습니다**. 민감한 로그인 정보는 대화창에 평문으로 입력하지 마시고, **반드시 Take Control을 사용하여 원격 화면에서 수동 인증**한 뒤 세션을 브라우저에 유지해야 합니다.

### 실행 환경 자체 점검 및 영속화
새 저장소를 연동하기 전에 먼저 Grok Bot에서 자체 점검 명령을 실행하여 환경 구성을 파악하세요.

::: details 运行环境自检与持久化
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

업데이트 시 시스템 의존성이 초기화될 수 있으며, `/workspace` 디렉터리만 영속적으로 보존됩니다. **모든 핵심 상태는 Git을 통해 원격으로 동기화하거나 구조화된 파일에 저장해야 합니다**.

참고 문서는 [Grok Bot 공식 사용 가이드](https://cursor.com/cn/docs/grok-bot/work) 및 [클라우드 컴퓨터와 애플리케이션 연결 안내](https://cursor.com/cn/docs/grok-bot/computers)를 확인하세요.

## 사례 1: SpaceXAI 팀의 PR 점검 및 다중 Bot 오케스트레이션

SpaceXAI의 Lingxi Li(@lingxi)는 5개의 개발 Bot과 1개의 프로세스 Bot을 이끌고 Cursor cloud agent를 연계하여 24시간 가동하고 있습니다.

팀의 @poteto는 한 달에 2,000개 이상의 PR을 병합했으며, Lingxi 본인도 단 3주 만에 iOS v0을 완성했습니다.

5개의 개발 Bot은 컨텍스트가 격리되어 각각 코드의 한 영역을 전담하며, 작업에 따라 해당 명령을 호출합니다:
- Baltata는 iOS 및 모바일 공통 레이어를 담당하고, Craig는 Android를 담당합니다.
- Shaoruru는 데스크톱 및 CI/CD를 담당하고, Quill은 Harness 툴체인을 유지 관리합니다.
- Hogan은 인프라 하부 구조 및 담당자 미정의 버그를 전담 조사합니다.
- 시각적 요소는 `/lingxi-design`, 코드 품질은 `/react-native-best-practices`, 아키텍처는 `/lingxi-review`를 사용합니다.

리드 Bot인 Jenny는 코드를 작성하지 않으며, 매일 아침 5시에 매뉴얼을 하나씩 대조 점검합니다. **개발 Bot이 대충 리뷰하거나 완전히 검증하지 않고 넘길 경우, Jenny가 이를 찾아내 RCA(근본 원인 분석)를 수행하고 규칙을 업데이트합니다**.

긴 대화 세션은 컨텍스트 용량을 초과하기 쉬우므로, 팀은 상태를 Notion 데이터베이스에 저장하고 정기 폴링을 통해 폐쇄 루프(closed loop)를 실행합니다:
1. **30분 단위 폴링**: 30분마다 open PR을 스캔하여 Bugbot 결과, CI 에러 및 Git 충돌을 확인합니다.

   문제가 발생하면 Cursor를 호출해 수정한 뒤 다시 Working 상태로 전환하고, 모든 검사가 통과(All Green)하면 Ready for Review로 전환합니다. 신뢰도가 극히 높고 변경의 영향도가 매우 미미할 때만 자동 병합합니다. **이를 통해 1인 동시 스케줄링 용량이 15개에서 200개 이상으로 증가했습니다**.
2. **실기기 스크린샷 대조**: 코드 어설션만으로는 시각적 UI 문제를 놓치기 쉽기 때문에, 팀은 유휴 Mac mini를 프라이빗 Worker로 사용하여 iOS Simulator를 실행하고, **멀티모달로 전후 실제 스크린샷을 비교**하여 시각적으로 어긋나면 즉시 반려합니다.
3. **새벽 3시 야간 감사**: 데드 코드 정리 및 번들 크기 축소, 의존성 보안 및 CI 소요 시간 점검, 다국어 번역 보완, 멀티 플랫폼 기능 일치 여부 확인, 지난 24시간 동안의 PR 종합 요약을 진행합니다.

> 출처: [엔지니어는 Grok Bot을 어떻게 잘 활용할 수 있을까?](https://x.com/KinGao476942/status/2096232745538334913)  
> 작성자: [Kin @KinGao476942](https://x.com/KinGao476942)

![엔지니어는 Grok Bot을 어떻게 잘 활용할 수 있을까?](/cases-img/fs25-0.jpg)

![엔지니어는 Grok Bot을 어떻게 잘 활용할 수 있을까?](/cases-img/fs25-1.jpg)

**단일 Bot에게 장기 대화 세션을 부담시키지 마세요**. 업무 단위로 역할을 나누고, 규칙을 전담 복기하는 역할을 두며, 상태를 칸반 보드에 기록하여 차이를 대조하면 훨씬 수월해집니다.

- [《엔지니어는 Grok Bot을 어떻게 잘 활용할 수 있을까?｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## 사례 2: R&D 업무 분해 및 Lauren의 9가지 체크리스트

### 구체적인 실행 방법
Lauren(@poteto)은 한 달에 2,500개의 프로덕션 PR을 병합했고, Jacob Gold(@jacobgold)는 하루 평균 250개 가까이를 병합했습니다. 두 사람은 엔지니어링 작업을 9개의 라인으로 분해하여 병렬로 실행했습니다.

| 위험도 | 일반적인 범위 및 규칙 | 검토 방식 |
| :--- | :--- | :--- |
| 낮음~중간 | 데드 코드 정리, 단위 테스트 및 타입 수정 | 자동 병합 |
| 높음 | 핵심 비즈니스 로직, 인증 및 데이터 마이그레이션 | 수동 검토(사람) 필수 |

**Diff가 원래 프롬프트의 의도를 벗어나면, 시스템은 즉시 사람에게 결정을 넘깁니다.**

### 배울 수 있는 점
Mai Yang(@MaiYangAI)은 6개월 동안 ContextEcho에서 1,020개의 커밋을 생성했지만, PR을 거친 것은 18번에 불과했습니다. **1인 프로젝트는 장애 영향 범위가 매우 작으므로, 실제 필요가 없을 때 억지로 PR을 만드는 것은 아무런 가치가 없습니다.**

> 출처: [하루에 수백 개의 PR이 무슨 의미가 있을까? SpaceXAI 엔지니어 Lauren(@poteto)의 9가지 체크리스트를 따라 내 업무를 분해해 보았다](https://x.com/MaiYangAI/status/2108519046446727633)  
> 작성자: [Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
먼저 버그 수정과 코드 표준 리팩터링 두 가지 항목을 선택하고 입력 제약과 검수 기준을 추가하세요. **육안으로 코드를 검토하는 에너지를 아껴 방향성 정의, 경계 조건 설정 및 테스트 작성에 집중하십시오.**

[《하루에 수백 개의 PR이 무슨 의미가 있을까? SpaceXAI 엔지니어 Lauren(@poteto)의 9가지 체크리스트를 따라 내 업무를 분해해 보았다》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## 사례 3: 24/7 저장소 운영 데스크(Repo Ops Desk)

![사례 3: 24/7 저장소 운영 데스크(Repo Ops Desk)](/info/14-engineering-s3.png)

### 누가 무엇을 했는가
인디 개발자 Gipp 🦅(@gippp69)는 여러 오픈소스 프로젝트와 비즈니스 저장소를 유지보수하면서 24/7 저장소 운영 데스크를 설계했습니다. 이 시스템은 하위 레벨에서 동시성 서브 Agent를 결합하여 이상 징후를 모니터링하고, 상위 레벨에서는 Grok Bot을 통해 6개의 명명된 역할을 배포하여 Issue와 CI 에러를 처리합니다.

작성자의 설명에 따르면 한 사람이 수동으로 관리할 수 있는 저장소는 보통 2~3개에 불과하지만, 자동화된 운영 데스크는 여러 저장소의 수백 개 변경 사항을 동시에 모니터링할 수 있습니다.

### 구체적인 실행 방법

::: details 具体怎么做
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

1. **6개의 전담 Bot 배포**
   - Triage Bot: 심각도와 유형별로 Issue를 분류합니다.
   - Fix Bot: 경미한 버그를 인계받아 패치를 작성하고 Draft PR을 생성합니다.
   - Test Bot: 테스트를 실행하여 간헐적 실패(Flaky) 테스트를 잡아내고 실패 컨텍스트를 기록합니다.
   - Dependency Bot: CVE 취약점 및 오래된 의존성을 모니터링합니다.
   - Release Bot: 지침에 따라 변경 로그(Changelog)를 정리하고 패키징합니다.
   - Alert Bot: 사람의 개입이 필요할 때 즉시 알림을 발송합니다.

2. **라우팅 테이블에 따른 권한 제어**

| 권한 계층 | 모니터링 범위 | 역할 및 동작 |
| :--- | :--- | :--- |
| `auto-fix` | Flaky 테스트, Lint 에러 및 포맷 | Fix Bot이 패치 제출 |
| `triage` | 미분류 복잡 결함 및 요구사항 | Triage Bot이 사람에게 이관 |
| `security` | 중·고위험 CVE 취약점 | Dependency Bot이 발견 즉시 Alert에 전달하여 경고 |
| `release` | 버전 변경 및 릴리스 노트 | Release Bot이 명령에 따라 실행 |

3. **3가지 엄격한 레드라인 준수**
   - 비즈니스 로직 절대 불가침: `auto-fix` 변경은 실패한 테스트 파일 자체 또는 직접적인 참조로 엄격히 제한되며, 핵심 코드 수정은 엄격히 금지됩니다.
   - 자동 병합 절대 금지: Fix Bot은 `auto-fix` 태그가 달린 Draft PR만 생성하며, 절대 자동으로 Merge하지 않습니다.
   - 1주일간 시범 가동: 위험도가 낮은 단일 엣지 저장소에서 먼저 1주일간 시범 운영하여 채택률(병합 수 대비 폐기 수)을 확인하고, 안정화된 후 메인 저장소로 확장합니다.

### 배울 수 있는 점

> 출처: [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> 작성자: [Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**운영 데스크는 심야에 에러를 조사할 뿐, 의사결정을 내리지 않습니다**. 프롬프트와 권한을 "Draft PR만 생성, 비즈니스 로직 수정 절대 금지"로 확실히 제한하면 무인 상태에서도 시스템이 안전하게 실행됩니다.

자세한 설정 방법은 [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)를 참고하세요.

## 사례 4: 상태 머신 및 다중 Bot 협업 기반 엔지니어링 Harness

![사례 4: 상태 머신 및 다중 Bot 협업 기반 엔지니어링 Harness](/info/14-engineering-s4.png)

### 누가 무엇을 했는가
개발자 Mori(@0xjmori), Morlex(@0xMorlex)와 1인 기업 아키텍트 beamnxw는 표준화된 R&D 협업 파이프라인을 설계했습니다. 이들은 클라우드에 상태 머신 규약, 통일된 디렉터리 구조 및 6개 필드의 작업 칸반 보드를 구축하여, 1명의 총괄이 4명의 담당자를 조율하는 엔드투엔드(End-to-End) 수정 파이프라인을 구현했습니다.

전체 시스템은 복잡한 코드 변경을 검증 가능한 증거 기반의 상태 전이로 분해합니다. 이러한 설계를 통해 모든 단계의 인수인계가 명확한 근거를 갖추도록 보장합니다.

### 구체적인 실행 방법

1. **구조화된 작업 공간 디렉터리 구축**
Grok Bot 클라우드 컴퓨터의 `/workspace`에서 프로젝트를 초기화하고, 각 Issue는 독립된 디렉터리 `/workspace/devdesk/issues/<issue-id>/`로 관리합니다.

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**각 디렉터리에는 반드시 6개의 표준 파일이 구비되어야 합니다**.
- `task.md`: 원본 입력 및 완료 검수 기준
- `status.json`: 현재 머신 판독 가능 상태 및 담당자
- `evidence/`: 실패 로그, 재현 스크립트 및 스크린샷 저장
- `implementation.md`: 변경 파일 목록 및 최소 구현 방안
- `review.md`: 독립 검토 결론
- `handoff.md`: 사람에게 전달할 릴리스 승인 보고서

2. **상태 머신 전이 규약**
**파이프라인은 정해진 상태에 따라 단계별로 진행되며, 단계를 건너뛰는 것은 엄격히 금지됩니다**.

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage(`NEW` ──> `REPRODUCED`)**: 안정적인 재현 단계와 정상 실행되는 실패 테스트 케이스를 반드시 제공해야 합니다.
- **Builder(`BUILDING` ──> `TESTED`)**: 새 브랜치에서 Cursor agent를 실행하여 코드를 수정하고, 기존 회귀 테스트 케이스가 통과하도록 보장해야 합니다.
- **Reviewer(`REVIEWING` ──> `REVIEW_PASSED`)**: 독립적으로 Diff와 로그를 검토하고 평가를 내립니다. **FAIL 판정이 나면 `BUILDING`으로 되돌려 다시 수정하며, 재시도는 최대 2회로 제한됩니다**.
- **Release(`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`)**: 모든 검사 항목을 통과한 후, 엔지니어(사람)에게 완전한 증거가 첨부된 Draft PR을 제출합니다.

3. **작업 가역성 등급 분류**
**시스템은 작업의 가역 여부에 따라 승인 권한을 구분합니다**.

| 작업 분류 | 권한 정책 | 해당 행위 및 작업 범위 |
| :--- | :--- | :--- |
| **가역적 작업** | 자율 실행 | 코드 분석, 로컬 브랜치에서 패치 작성 및 단위 테스트 실행, 실패 테스트 케이스 생성, Draft PR 생성 및 로그 보고서 출력 |
| **비가역적 작업** | 중단 후 사람 승인 대기 | 기본 브랜치로의 코드 병합, 프로덕션 배포, 운영 데이터베이스 수정, 환경 변수 또는 키 변경, 유료 외부 서비스 호출 |

4. **칸반 보드 및 스킬 자산화**
칸반 필드는 `Task | Owner | Source | Status | Deliverable | Next action`으로 고정합니다.
작업 상태는 `ready`, `working`, `blocked`, `awaiting approval`, `complete`의 5가지로 엄격히 제한됩니다.
**특정 유형의 작업이 한 번 성공적으로 실행되면, 명령을 실행하여 비공개 Skill로 자산화**하여 정기 Routine에서 반복 호출할 수 있도록 합니다.

### 배울 수 있는 점

> 출처: [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> 작성자: [Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

비구조화된 그룹 채팅방에서 여러 Agent가 무분별하게 대화를 주고받게 두지 마세요.

1. **이전 단계의 테스트 증거가 저장되지 않았다면 다음 단계를 절대 시작하지 마세요**. 디스크 디렉터리와 상태 머신으로 진행을 엄격히 제어합니다.
2. **작업의 가역성을 구분**하여 자동화 속도를 확보하는 동시에 프로덕션 안전 기준을 지킵니다.

자세한 실천 방법은 [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf), [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh) 및 [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)를 참고하세요.

## 바로 사용 가능한 템플릿: 엔지니어링 R&D 프롬프트 라이브러리

다음 프롬프트는 모두 실제 프로덕션 환경에서 검증되었습니다. 직접 복사하여 Bot에게 전송하고 기억하도록 지시하거나, 공유 Bot의 경우 상세 정보(About)에 입력하세요:

### 1. 아키텍처 총괄 헌장 (Chief)
**리드 Bot에게 전송하여 기억하도록 하거나**(공유 Bot의 경우 상세 정보 About에 입력), 프로세스 제어 및 상태 기록에 사용합니다.

::: details 1. 架构总控章程（Chief）
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

### 2. 결함 재현 담당 (Triage)

버그를 탐색하고 실패 테스트 케이스를 작성할 수 있도록 **Triage Bot에 직접 붙여넣으세요**.

::: details 2. 缺陷复现专员（Triage）
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

### 3. 코딩 담당 (Builder)
격리된 브랜치에서 실행될 수 있도록 프롬프트를 **Builder Bot**에 붙여넣으세요.

::: details 3. 编码专员（Builder）
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

### 4. 독립 검토 담당 (Reviewer)
프롬프트를 Reviewer Bot에 붙여넣고 **엄격하게 검수**하도록 합니다.

::: details 4. 独立审查专员（Reviewer）
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

### 5. 릴리스 담당 (Release)
결과물을 취합하고 인도할 수 있도록 **프롬프트를 Release Bot에 붙여넣으세요**:

::: details 5. 交付专员（Release）
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

### 6. 야간 당직 정기 루틴 (Engineering Night Shift Routine)

Grok Bot에서 예약 작업을 설정하고, **실행 주체로 Chief를 선택**하세요.

::: details 6. 夜间值守例行任务（Engineering Night Shift Routine）
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

### 7. 가역성 휴먼 게이트 및 안전 레드라인 지침

**각 Bot의 장기 규칙 끝부분에 직접 추가하세요**(개인 Bot은 대화창에 전송하여 기억시키고, 공유 Bot은 상세 정보 About에 작성).

::: details 7. 可逆性人闸与安全红线指令
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

## 자주 겪는 함정 및 주의사항

### 모델 자동 매칭
백엔드에서 Claude Opus 5.5 등 기저 모델을 자동으로 매칭하며, 수동으로 선택할 수 없습니다. **진행 조건을 `status.json`과 같은 구조화된 파일에 작성하고 스크립트로 엄격하게 검증**해야 하며, 모델의 출력 스타일이 항상 일정할 것이라 기대해서는 안 됩니다.

### 공유 환경 충돌
모든 Bot은 클라우드 컴퓨터의 `/workspace`를 공유합니다. **각 Issue는 반드시 독립된 하위 디렉터리와 Git 브랜치를 사용**해야 하며, 코드 수정 시 Cursor cloud agent를 파생시키고 커밋되지 않은 작업 트리를 혼용해서는 안 됩니다.

### 검토 무한 루프 및 테스트 변조
Builder의 수정 실패 시 무한 루프에 빠지기 쉽고, 심지어 테스트 어설션을 임의로 수정하여 억지로 통과시키는 경우가 있습니다. **단일 Issue의 재시도는 최대 2회로 엄격히 제한**하고, 초과 시 즉시 사람에게 이관해야 합니다. Reviewer는 반드시 테스트 케이스의 Git Diff를 비교해야 하며, 어설션이 수정된 경우 즉시 FAIL로 판정해야 합니다.

### 구독 할당량 및 폴링
사용량은 2026년 10월 12일 발효된 The X Subscription에 따라 적용되며, Grok 및 Cursor와 주간 사용량 풀을 공유하고 초과분은 Cursor 요금 정책을 따릅니다.

5분마다 전체 스캔을 실행하지 말고, **예약 작업은 매일 또는 야간에 1회 실행**하도록 설정하며, 트리거는 가급적 `agent-ready` 태그를 활용하세요.

| 구독 플랜 | 월 요금 | 할당량 배수 | Grok Bot 포함 여부 |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | Bot 미포함 |
| **Premium** | $30 / 월 | 4x 할당량 | 포함 |
| **Super** | $100 / 월 | 15x 할당량 | 포함 |
| **Ultra** | $200 / 월 | 50x 할당량 | 포함 |

### 브랜치 보호 및 Draft PR
**Agent의 산출물은 반드시 Draft PR로만 생성하며, 메인 브랜치로의 자동 병합은 엄격히 금지됩니다**. GitHub의 Branch Protection Rules에서 세 가지 조건을 반드시 강제해야 합니다:
- main 또는 master 브랜치로의 직접 Push 금지
- 최소 1명 이상의 수동 승인(Approvals) 필수
- 기존 CI 파이프라인 통과 필수

### 민감 자격 증명 유출 방지
대화 내용은 모델 컨텍스트로 전달되므로, **프롬프트에 비밀번호, 개인 키(Private Key) 또는 API 키를 입력하는 것은 엄격히 금지됩니다**. 비공개 시스템 접근은 설정의 커넥터를 이용하거나 Agent Computer의 Take Control 원격 데스크톱을 통해 수동으로 로그인하세요.

## 완료 후 검수 방법

**처음부터 프로덕션 핵심 프로젝트에 전면 도입하지 마세요**.

### 단일 저장소 단일 버그 콜드 스타트 검수
- 엣지 저장소를 하나 골라 `/workspace/devdesk/`를 생성하고, 작은 버그를 선택해 `agent-ready` 태그를 지정합니다.
- Chief 프로세스를 실행하고, Triage가 `evidence/` 아래에 재현 로그와 단위 테스트를 제대로 저장했는지 확인합니다.
- Builder가 독립 브랜치에서 작업하며 메인 코드를 건드리지 않는지, Reviewer가 라인 번호와 로직을 검토했는지 확인합니다.
- **최종적으로 Draft PR만 생성되었는지**, 메인 브랜치에는 아무런 변경이 없는지 확인합니다.

### 지표 정량화 및 패치 채택률 검증
- 채택률이 **70% 미만일 경우 두 번째 저장소 연동을 중단**하고, 프롬프트 제약 조건을 강화합니다.
- 아침 보고서는 **3분 이내**에 적격 PR, 차단 항목 및 보류 항목을 명확히 파악할 수 있어야 하며, 수천 자의 대화를 일일이 읽어야 한다면 기준 미달입니다.
- 심야 예약 작업은 트리거가 없으면 절전 모드로 전환되고, 타임아웃 시 자동 중단되어 할당량 폭탄을 방지해야 합니다.

### 안전 레드라인 및 권한 차단 실전 훈련
- 테이블 스키마 변경(Migration)이나 인증 로직 수정을 요구하는 Issue를 일부러 등록하여, 작업이 차단되고 대기 상태로 전환되는지 확인합니다.
- Bot에게 `git push origin main`을 실행하게 하여, **브랜치 보호 규칙이 이를 성공적으로 차단하는지 확인**합니다.
- 외부 통신 및 설정 변경과 관련된 작업의 경우 Auto-review에 **Ask first**가 켜져 있는지 확인합니다.

## 참고 자료

### 공식 문서 및 기능 페이지
- [Grok Bot 공식 사용 가이드](https://cursor.com/cn/docs/grok-bot/work)
- [클라우드 컴퓨터 및 애플리케이션 연결](https://cursor.com/cn/docs/grok-bot/computers)
- [모델 선택 및 라우팅 안내](https://cursor.com/cn/help/grok-bot/models)
- [플랜, 요금 및 온디맨드 사용량 안내](https://cursor.com/cn/help/grok-bot/plans)
- [설정 및 보안 규정](https://cursor.com/cn/docs/grok-bot/settings)
- [팀 협업 및 Team Bots 설정](https://cursor.com/cn/docs/grok-bot/teams)

### 커뮤니티 실전 사례 원문

> 출처: [Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> 작성자: [Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [《엔지니어는 Grok Bot을 어떻게 잘 활용할 수 있을까?｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [《하루에 수백 개의 PR이 무슨 의미가 있을까? SpaceXAI 엔지니어 Lauren(@poteto)의 9가지 체크리스트를 따라 내 업무를 분해해 보았다》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)
