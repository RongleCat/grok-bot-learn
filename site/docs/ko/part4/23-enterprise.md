# 제 23 장 팀 플랜 및 엔터프라이즈 도입

팀에 Grok Bot을 배포할 때 주로 다음과 같은 병목 현상이 발생합니다.

- 게이트웨이가 핸드셰이크 단계에서 차단하여 **클라우드 컴퓨터에 연결되지 않음**.
- Linux VM에 MDM 클라이언트가 설치되어 있지 않아 엔터프라이즈 IdP에서 신뢰할 수 없는 디바이스로 판단됨.
- 자격 증명 유출 및 내부망 침투 위험이 존재하며, 클라이언트 사일런트 배포 수단이 부족함.

절차에 따라 **SSO 및 보안 게이트웨이 예외 처리**를 구성하고 사설망 접근을 연결하면, 대규모 라이프사이클 관리를 완벽하게 처리할 수 있습니다.


![팀 플랜 및 엔터프라이즈 도입](/info/23-enterprise.png)

## 팀 및 엔터프라이즈 관리 제어: 아키텍처와 기능 경계

![팀 및 엔터프라이즈 관리 제어: 아키텍처와 기능 경계](/info/23-enterprise-s1.png)

### 무엇인가

**사용자마다 1대의 전용 클라우드 Firecracker microVM이 제공**되며, 로컬에서 명령 승인을 보내고 코드와 브라우저는 클라우드에서 실행됩니다.

한 가지 주의할 점은, **계정 내의 모든 Bot이 이 가상 머신을 공유**하므로 파일과 로그인 상태가 완전히 공유된다는 점입니다.

2026-10-12 The X Subscription 플랜에서는 두 가지 버전의 권한을 구분했습니다:

- **팀 플랜**: 전원 기본 활성화, 공유 정적 아웃바운드 IP 사용, 기본 감사 및 팀 규칙 제공.
- **엔터프라이즈**: 그룹별 권한 부여 및 SCIM 2.0 지원, sudo 및 네트워크 화이트리스트 사용 가능, 작업 녹화 및 OpenTelemetry 내보내기 지원(`cursor.surface=grok_bot` 태그 지정).

문서는 [Teams 및 엔터프라이즈용 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)을 참고하세요.

### 진행 방법

일상적인 설정은 [Cursor 대시보드의 Grok Bot 페이지](https://cursor.com/dashboard/bot)에서 처리하며, 크게 네 단계로 진행됩니다.

1. 권한 및 기본 스위치 분할
- 파일럿 기간에는 **Manage Group Access**를 클릭하여 파일럿 대상을 체크합니다. 클라우드 코딩을 사용하지 않는다면 Cloud Agents를 끄고, 외부 유출 방지를 위해 공개 템플릿 공유는 비활성화 상태를 유지합니다.
- **로컬 실행은 Never allow로 설정하는 것을 권장**하며, 우회 전달 방지를 위해 로컬 아웃바운드 라우팅도 함께 비활성화합니다.
- 사이드바 Bot은 Auto-add 열에서 All team 또는 지정된 그룹을 선택하여 고정합니다.

2. 승인 잠금 및 규칙 구성
- **Enforce Auto-review 모드**를 켜면 구성원이 클라이언트에서 자체적으로 검토를 끌 수 없습니다.
- 프로덕션 배포나 외부 이메일 발송 등 위험도가 높은 작업은 Ask first로 설정하고, 한정된 읽기 전용 작업은 Allow automatically로 설정합니다.
- **팀 규칙과 개인 규칙이 충돌할 경우, 시스템은 강제적으로 Ask first를 우선 적용합니다**.

3. 네트워크 및 시크릿 설정
- 네트워크는 팀 허용 목록 전용을 선택하거나 기본값을 추가한 뒤 도메인과 IP 대역을 입력합니다. 시스템 변조 방지를 위해 기본 활성화된 sudo를 끌 수 있습니다.
- **Team Secrets는 팀당 최대 100개까지 추가 가능**하며, 단일 항목 상한 32 KB, 총 용량 상한은 96 KB이고 저장 후 평문은 표시되지 않습니다.
- 시크릿 변수명에는 `PATH`, `HOME` 및 `SAND_` 또는 `LD_`로 시작하는 시스템 예약어를 사용할 수 없습니다.

4. 그룹 레벨 정책 구성
- [Members > Groups](https://cursor.com/dashboard/members?subtab=groups)에서 그룹으로 진입하며, **구성 원칙은 완화만 가능하고 더 엄격하게 제한할 수는 없습니다**.
- Don't enforce for this group을 선택하면 자동 검토 잠금을 해제할 수 있습니다.
- 네트워크 정책은 예외로 그룹이 팀 설정을 직접 덮어씁니다. 구성원이 여러 그룹에 걸쳐 있는 경우 네트워크는 가장 엄격한 규칙이, 권한은 가장 관대한 규칙이 적용됩니다.

### 완료 기준

- 대시보드에서 파일럿 그룹과 미승인 그룹이 명확히 구분되며, 미승인 인원은 클라이언트에서 Bot을 활성화할 수 없습니다.
- 팀 규칙 및 Auto-review 규칙이 잠겨 있어, 구성원이 클라이언트 설정 페이지에서 팀 규칙을 볼 수는 있지만 편집 및 삭제 버튼은 비활성화 상태입니다.
- 위험 작업(외부 통신, 파일 파괴, 권한 상승 명령)이 100% 승인 인터셉트를 트리거합니다.

---

## ID 및 SSO: 전사 접근 연동과 디바이스 신뢰 호환

### 무엇인가

Grok Bot은 Cursor 계정 체계를 그대로 사용하므로 **IdP에 별도의 애플리케이션을 생성할 필요가 없습니다**. 참고 문서: [ID 및 액세스 구성](https://cursor.com/cn/docs/grok-bot/identity).

Bot은 MDM이 설치되지 않은 클라우드 Linux VM에서 실행되므로 FastPass 또는 Hybrid Join을 충족할 수 없습니다. **절대로 디바이스 컴플라이언스를 전체 비활성화해서는 안 되며**, 차단 규칙 앞단에서 대상 그룹에 대한 예외 허용 정책을 구성해야 합니다.

### 진행 방법

- **Okta 할당 확장**: Cursor 앱의 **Assignments** > **Assign to Groups**로 이동하여 비즈니스 그룹을 체크합니다. SCIM 활성화 시 동시에 할당 및 푸시(Push Groups)를 진행합니다.

  **SAML SSO와 SCIM은 반드시 동시에 할당해야 하며**, SSO 누락 시 로그인이 차단됩니다.
- **Entra ID 할당 확장**: Cursor 앱의 **Users and groups**에서 **Add user/group**을 클릭하여 그룹을 추가합니다(P1/P2 라이선스 필요, 중첩 그룹 미지원). 프로비저닝 앱에서도 동일한 그룹을 동기화하여 할당합니다.
- **Okta Linux 예외 허용**: 인증 정책 차단 규칙 앞에 `Grok Bot computer (Linux)` 규칙을 새로 만듭니다.

  사용자는 Cursor 그룹으로 한정하고, **Device platform은 Other Desktop을 선택**하며(독립된 Linux 항목 없음), Device state는 Any를 선택합니다. 인증은 Password + Another factor를 선택하고 피싱 방지 제한은 선택 해제합니다.
- **Entra ID Linux 예외 허용**: 높은 우선순위 정책을 새로 만들고 Cursor 그룹과 대상 애플리케이션을 지정합니다. Device platforms는 Linux를 포함하고 Windows와 macOS는 제외합니다. Grant에서 Require multifactor authentication을 체크합니다. **기존 컴플라이언스 정책에서 해당 그룹 또는 Linux 플랫폼을 반드시 제외해야 합니다**.

### 완료 기준

- 비즈니스 사용자가 엔터프라이즈 SSO로 데스크톱 클라이언트에 로그인할 때 `User is not assigned to this application` 오류가 발생하지 않습니다.
- Bot 브라우저에서 비밀번호와 2차 인증을 통해 내부망에 접근할 수 있으며, FastPass나 디바이스 비준수 차단 팝업이 뜨지 않습니다.
- **직원이 개인 PC에서 접근할 때는 기존의 FastPass 및 디바이스 컴플라이언스가 여전히 엄격하게 적용됩니다**.

## 사설망 연동: 데스크톱 라우팅 및 Team Setup 스크립트 자동화

![사설망 연동: 데스크톱 라우팅 및 Team Setup 스크립트 자동화](/info/23-enterprise-s3.png)

### 무엇인가

Grok Bot은 클라우드에서 실행되므로 **내부망에 접근하려면 사설망을 연동해야 합니다**.

- 데스크톱 라우팅: 임시 디버깅에 적합합니다. 클라이언트에서 `Settings > Computer > Route traffic through this computer`를 켜면 트래픽이 로컬 네트워크 카드를 경유하며, 관리자가 백엔드에서 원클릭으로 비활성화할 수 있습니다.
- Team Setup 클라이언트 설치: 상시 접근용이며 **엔터프라이즈 전용**입니다. IT 부서에서 스크립트를 통합 관리하여, Bot 시작 또는 새로고침 시 자동으로 실행하고 내부망에 조인합니다.

자세한 내용은 [사설망 연결](https://cursor.com/cn/docs/grok-bot/private-networks)을 참고하세요.

### 진행 방법

팀 환경 설정 스크립트는 대시보드의 **Bot Computers** 하위에 있으며, Debian Linux 가상 머신에서 `sudo` 권한을 가진 일반 사용자 자격으로 실행됩니다. **스크립트는 부팅 시 실행되며 매일 약 1회 주기로 새로고침되고, 타임아웃 제한은 30분입니다**.
- `check` 종료 코드가 0이면 설치를 건너뛰고, 설치 완료 후 다시 `check`를 실행하여 검증합니다.
- **실행이 실패하더라도 컴퓨터 부팅을 차단하지 않으며**, 다음 주기 새로고침 시 재시도합니다.

#### Tailscale 네트워크 구성 솔루션 연동

1. **Team Secrets**를 열고 Tailscale 인증 키 `TS_AUTHKEY`(값: `tskey-auth-...`)를 추가한 뒤, Tailscale 콘솔에서 전용 ACL 태그(예: `tag:grok-bot`)를 바인딩하여 **접근 권한을 엄격하게 제한**합니다.
2. 팀 환경 설정 스크립트로 이동하여 **+**를 클릭해 새 매니페스트를 만들고, Manifest ID에 `private-network-tailscale`을 입력한 다음 JSON 또는 폼 모드로 전환하여 구성을 입력합니다:

::: details Tailscale 네트워크 구성 솔루션 연동
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

#### Cloudflare Tunnel 솔루션 연동

- 프라이빗 HTTP 서비스: 터널 라우팅 도메인으로 직접 접근하며, Cloudflare Access가 인증하고 Bot 브라우저에서 대화형으로 인증을 완료합니다.
- 프라이빗 TCP 서비스(예: 데이터베이스, SSH): 매니페스트에 `cloudflared`를 설치하고, 연결이 필요할 때 Shell에서 명령을 실행하여 **로컬 포트 포워딩을 엽니다**:

`cloudflared access tcp --hostname db-internal.corp.com --url localhost:5432`

::: details Cloudflare Tunnel 솔루션 연동
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

#### 네트워크 정책과 연계하여 제어 평면 엔드포인트 허용

팀에서 **팀 허용 목록 전용** 네트워크 제어를 활성화한 경우, **반드시 네트워크 도구의 제어 평면을 허용 목록에 추가**해야 하며, 그렇지 않으면 클라이언트가 인증을 완료할 수 없습니다. 예를 들어 Tailscale을 사용할 때는 코디네이션 서버와 DERP 릴레이 서버 도메인을 정책에서 허용해야 합니다. 정책 변경 사항은 약 1분 내에 가상 머신에 전달됩니다.

### 완료 기준

- 새로 생성되거나 재생성된 Bot 컴퓨터가 부팅을 마친 후, Tailscale 또는 Cloudflare 관리 콘솔 디바이스 목록에 온라인 상태로 자동 표시됩니다.
- 매니페스트의 `check` 스크립트가 이후 매일 진행되는 주기적 순회 새로고침에서 안정적으로 0을 반환하여 설치 로직을 중복 실행하지 않습니다.
- 민감한 Token이 완전히 Team Secrets를 통해 주입되어, 매니페스트 텍스트 및 실행 로그에 평문 자격 증명이 전혀 남지 않습니다.

---

## 프록시 및 엔터프라이즈 게이트웨이 주의사항: 허용 규칙 및 TLS 검사 예외 처리

엔터프라이즈 게이트웨이(예: Zscaler, Palo Alto)로 인해 채팅은 정상이지만 **스크린샷 캡처나 터미널 제어가 불가능한** 경우가 자주 발생합니다.

근본 원인은 제어 평면이 `<computer>.<cluster>.cursorvm.com` 2단계 중첩 도메인의 HTTP/2 또는 SSE 스트리밍 장기 연결을 사용하기 때문이며, 일반적인 단일 단계 규칙으로는 매칭할 수 없습니다.

공식 설명은 [TLS 검사 프록시 구성](https://cursor.com/cn/docs/grok-bot/proxies)을 참고하세요.

### 구성 핵심 사항

게이트웨이에서 다음 도메인을 반드시 허용해야 하며, 엔드투엔드 핸드셰이크 실패 및 스트리밍 타임아웃을 방지하기 위해 **응답 버퍼링을 끄고 TLS 검사를 예외 처리**해야 합니다:
- `*.cursor.sh`: 핵심 API
- `*.cursorvm.com` 및 **`*.*.cursorvm.com`**: 제어 채널, 반드시 2단계 와일드카드를 지원해야 함
- `*.cursor-cdn.com`, `*.cursorapi.com`, `downloads.cursor.com` 및 메인 사이트: 정적 리소스 및 업데이트 다운로드

정책 구성을 마친 후, 직원이 사외에 있거나 재택근무 시 연결되지 않는 문제를 방지하기 위해 **반드시 Off-Network 로밍 구성에도 동기화**해야 합니다.

### 디바이스 문제 해결 및 검증

직원 컴퓨터의 터미널에서 단계별로 확인합니다:

1. 인증서 변조 여부 검증 (정상 발급자는 반드시 **Amazon RSA**여야 함):
```bash
   curl -v https://api2.cursor.sh |& grep -C1 issuer:
   ```
2. 다단계 DNS 확인 검증 (실패 시 `nslookup test.us9.cursorvm.com 1.1.1.1`과 비교):
```bash
   nslookup test.us9.cursorvm.com
   ```
3. 스트리밍 전송 확인: 데이터가 한 줄씩 출력되어야 합니다. 몇 초간 멈췄다가 갑자기 한꺼번에 출력된다면 게이트웨이 버퍼링이 꺼지지 않은 것입니다.

검증 기준: **사내 네트워크 및 재택 로밍 모두 5초 이내에 클라우드 컴퓨터에 연결**되고, 인증서가 Amazon RSA로 직접 투과되며, 스트리밍 장기 연결에 버퍼링 지연이 없어야 합니다.

## 데스크톱 클라이언트 배포 및 버전 관리

### 플랫폼 및 업데이트 메커니즘

| 플랫폼 | 설치 형식 | 업데이트 로직 |
| --- | --- | --- |
| macOS | `.dmg`（Apple Silicon / Intel） | 시작 시 자동 업데이트 확인, **정책으로 비활성화 불가** |
| Windows | Setup `.exe`（x64 / Arm64） | 시작 시 자동 업데이트 확인, 정책으로 비활성화 불가 |
| Linux | `.deb`、`.rpm`、AppImage | deb 및 rpm은 패키지 관리자가 제어, AppImage는 자동 업데이트 확인 |
| iOS | App Store | iOS 18 이상 버전 필요 |
| Android | Google Play | Android 9 이상 버전 필요, 관리형 푸시 지원 |

공식 배포 설명은 [조직에 Grok Bot 배포하기](https://cursor.com/cn/docs/grok-bot/deployment)를 참고하세요.

### 배포 및 버전 관리

1. **설치 패키지 다운로드**
   설치 패키지를 웹페이지에서 직접 수동으로 다운로드하지 말고 공식 JSON 피드를 호출하세요: `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`.
   `{platform}`은 macOS(`darwin-arm64`, `darwin-x64`), Windows(`win32-x64-user`, `win32-arm64-user`), Linux(`linux-x64`, `linux-arm64`)를 지원합니다.
```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand
```
   API 응답으로 `version`, `commitSha`, `downloadUrl`, 그리고 Linux의 `debUrl`, `rpmUrl`이 반환됩니다. macOS 및 Windows는 규칙에 따라 설치 패키지 URL을 직접 조합할 수도 있습니다:
   - Windows: `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`
   - macOS: `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`

2. **MDM 푸시 배포**
   - Windows（Intune / SCCM）: 사일런트 설치 인수로 `/S`를 추가합니다. 설치 프로그램은 기본적으로 현재 사용자의 `%LOCALAPPDATA%\Programs`에 기록되므로, **반드시 사용자 컨텍스트(User Context)에서 실행**해야 합니다.

     로컬 SYSTEM 계정을 절대 사용하지 마세요. 잘못된 경로에 설치되어 직원이 애플리케이션을 찾을 수 없게 됩니다.
```cmd
  Grok_Bot_1.0.0_Setup.exe /S
  ```
   - macOS（Jamf / Kandji / Intune）: 해당 아키텍처에 맞는 `.dmg`를 `/Applications` 디렉터리에 푸시하면 됩니다.
   - Linux（Ansible / Puppet）: `.deb` 또는 `.rpm` 패키지를 설치하면 시스템이 공식 소프트웨어 저장소 구성을 자동으로 추가합니다.

3. **버전 관리 및 잠금**
   macOS와 Windows는 정책을 통해 자동 업데이트를 완전히 끌 수 없습니다.

Linux에서는 패키지 관리자를 통해 버전을 고정하거나, `/etc/apt/sources.list.d/grok-bot.sources`에서 `Enabled: no`로 설정하거나 `/etc/yum.repos.d/grok-bot.repo`에서 `enabled=0`으로 설정하여 동기화를 일시 중지할 수 있습니다:
```bash
  sudo apt-mark hold grok-bot
  ```
   Cursor는 구버전에 대한 지원 기한을 설정합니다. **클라이언트가 최소 지원 임계값보다 낮으면 전체 화면에 Update required 팝업이 뜨며 강제로 차단**되며, Linux에서 버전을 고정하여 기한을 초과한 경우에도 동일하게 차단됩니다. 운영팀은 **2~4주마다 테스트를 거친 안정적인 새 버전을 카나리 롤아웃**해야 합니다.

### 검증 기준

- 업무용 디바이스에 MDM을 통한 사일런트 설치가 완료되어, **신규 직원이 부팅한 후 바탕화면에 즉시 준비**되어 있어야 합니다.
- IT 팀이 정기적인 버전 롤링 주기를 확보하여 공식 강제 차단 전에 조직 내부 버전 전환을 완료해야 합니다.

## Bot 컴퓨터 관리: 대규모 운영 관리 및 라이프사이클

![Bot 컴퓨터 관리: 대규모 운영 관리 및 라이프사이클](/info/23-enterprise-s6.png)

### 핵심 작업 및 권한

진입 경로는 [Cursor 대시보드의 Grok Bot 페이지](https://cursor.com/dashboard/bot) 내 **Bot Computers** 섹션에서 **Manage Bot Computers**를 클릭하면 됩니다.

**이 기능은 엔터프라이즈 조직 관리자(Organization Admins) 전용**이며, 일반 팀 관리자에게는 메뉴가 표시되지 않습니다.

문서는 [Grok Bot 컴퓨터 관리](https://cursor.com/cn/docs/grok-bot/computers)를 참고하세요.

| 작업 이름 | 기본 동작 | 데이터 및 파일 보존 상태 | 적용 시나리오 |
| --- | --- | --- | --- |
| **VM 재구축（Recreate VMs）** | 최신 이미지로 재설치하고 환경 스크립트 재실행 | **보존됨**. 디스크가 유지되며 Bot, 개인 파일, Cookie가 모두 보존되고 자체 설치한 시스템 소프트웨어만 제거됨 | 환경 스크립트 변경 적용, 새 이미지 카나리 배포 |
| **VM 종료（Terminate VMs）** | 실행 중이거나 유휴 상태인 인스턴스를 즉시 폐기하고 현재 연산 중단 | **보존됨**. 디스크가 보존되며, 다음에 클라이언트에서 메시지를 보내면 깨끗한 가상 머신을 다시 시작함 | 인스턴스 멈춤 해결, 클라우드 리소스 점유 해제 |
| **가상 머신 및 데이터 삭제** | 가상 머신을 폐기하고 기본 연결된 영구 스토리지를 완전히 삭제 | **보존되지 않음**. 데이터가 완전히 삭제되며 다음 사용 시 빈 컴퓨터로 다시 초기화됨 | 직원 퇴사 정리, 데이터 손상 시 완전 초기화 |

### 콘솔 작업 및 주의사항

1. 페이지에 진입하여 **관리**를 클릭하고, 이름이나 이메일로 구성원을 검색하여 단일 선택, 다중 선택 또는 **Select all**을 진행합니다.
2. **Manage selected** 드롭다운 상자에서 대상 작업을 선택하고, 영향을 받는 인원 수를 확인한 후 실행을 시작합니다.
3. 실행 완료 후 **반드시 카드에 있는 Done 버튼을 클릭**해야 합니다. 각 팀은 동일한 시간에 하나의 대규모 작업만 실행할 수 있으며, Done을 클릭하지 않으면 후속 버튼이 잠긴 상태로 유지됩니다.

건너뜀이나 실패 상태가 발생하면 리포트에 따라 대응합니다.
- **건너뜀（VM 없음 / 작업 완료 불가）**: 계정에 VM이 없거나 대기열에 있는 동안 팀을 나간 경우이므로 조치가 필요하지 않습니다.
- **실패（다른 재구축이 진행 중임 / VM 검색 미완료）**: 다른 업데이트가 아직 끝나지 않았거나 백엔드에서 일시적으로 상태를 가져오지 못한 경우이므로 몇 분 후 재시도합니다.
- **실패（작업 완료 불가）**: Bot이 고부하 작업을 실행 중이어서 타임아웃이 발생한 경우이므로, 구성원에게 안내하여 Bot이 잠시 유휴 상태가 된 후 재시도합니다.

### 자동화 및 검증 기준

작업 버튼 상단의 **Terminate Inactive Computers** 스위치를 켭니다. **구성원 컴퓨터에 30일 연속 활동이 없으면 자동으로 종료**되며, 디스크를 보존한 채 컴퓨팅 인스턴스만 해제하고 시스템 롤링 주기에 따라 정리됩니다.

여러 팀의 대규모 운영 관리는 [조직 Admin API](https://cursor.com/docs/account/organizations/organization-admin-api.md#grok-bot-computers)를 호출하여 처리할 수 있습니다.

호출 시 `admin:*` 권한의 조직 API 키가 필요하며, 팀 ID, 구성원 이메일 배열, 작업 유형(`recreate` 또는 `terminate`)을 전달하고 진행 상황을 폴링합니다. 이 역시 단일 팀 단일 동시성 제한이 적용됩니다.

검증 시 다음 두 가지 지표에 중점을 둡니다.
- 데이터 유실 없이 인스턴스를 매끄럽게 대규모 재구축할 수 있는지 여부.
- 30일 유휴 자동 종료가 활성화되어 유령 가상 머신이 조직의 클라우드 쿼터를 점유하지 않는지 여부.

## 엔터프라이즈 보안 베이스라인 구성 및 실전 프롬프트

### 관리자 구성
1. 네트워크는 "팀 허용 목록 전용"으로 잠그고 공개 템플릿과 이메일 채널을 비활성화합니다.
2. **Enforce Auto-review**를 활성화하고, 무단 다운그레이드 방지를 위해 로컬 실행은 **Never allow**로 설정합니다.
3. 프로덕션 API 호출, DB 수정, 또는 외부 이메일 발송, 계약 서명, main 브랜치 머지가 포함된 작업은 반드시 **Ask first**로 설정해야 하며, 로그 조회 및 컴파일은 바로 허용합니다.

### 직원 수칙
1. 자격 증명은 환경 변수를 사용하며, **대화창에 평문 비밀번호를 붙여넣는 행위를 엄격히 금지**합니다.
2. 민감한 권한 부여 시 **Allow once**를 선택하고, 항상 허용을 누르지 않으며 사용 후 즉시 로그아웃합니다.

### 실전 프롬프트
::: details 실전 프롬프트
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

::: details 실전 프롬프트
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

::: details 실전 프롬프트
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

## 자주 겪는 함정

1. **게이트웨이의 멀티 레벨 와일드카드 누락**: 호스트명이 `<vm-id>.<cluster-id>.cursorvm.com`이므로 `*.cursorvm.com`만 구성하면 99%에서 멈춥니다. **반드시 `*.*.cursorvm.com`을 추가로 구성해야 합니다**.
2. **프록시 버퍼링 활성화로 인한 스트림 단절**: Zscaler에서 Response Buffering을 켜면 연결이 끊어집니다. **Cursor 도메인에 대해 반드시 버퍼링을 끄고 Server-Sent Events를 직접 투과시켜야 합니다**.
3. **로밍 정책의 화이트리스트 누락**: 퇴근 후 집에서 연결되지 않는 원인은 Zscaler가 Off-Network 정책으로 전환되었기 때문입니다. 도메인 화이트리스트 및 TLS 예외 처리를 오프 네트워크 정책에도 동기화해야 합니다.
4. **구버전 프라이버시 모드 오작동**: 백엔드에서 "프라이버시 모드 (레거시)"를 켜면 Bot이 완전히 비활성화되므로, 팀 설정에서 이를 꺼야 합니다.
5. **IdP의 컴플라이언스 디바이스 강제**: 클라우드 Linux VM은 MDM으로 관리되지 않아 FastPass를 실행할 수 없습니다. **Okta/Entra ID에서 Linux(Other Desktop)를 대상으로 높은 우선순위 규칙을 추가**하고, 비밀번호와 모바일 2차 인증을 사용하여 통과시키도록 변경합니다.
6. **스크립트 내 평문 키 저장**: Team Setup은 평문 JSON입니다. 토큰은 **Team Secrets**에 저장하고, 스크립트에서는 `"$TS_AUTHKEY"`로 읽어와야 합니다.
7. **SYSTEM 권한 설치 시 앱 미발견**: 프로그램은 `%LOCALAPPDATA%\Programs`에 설치됩니다. **반드시 현재 사용자 컨텍스트에서 `/S` 설치 명령을 실행해야 합니다**.
8. **종료를 권한 회수로 오해**: Terminate는 프로세스만 중지하고 디스크는 보존하므로 메시지를 보내면 다시 실행됩니다. **완전히 권한을 회수하려면 IdP에서 할당을 취소하거나 Manage Group Access에서 제거해야 합니다**.
9. **복수 팀 가입으로 인한 시크릿 유실**: Team Setup이 구성된 팀에 둘 이상 참여하면 **모든 Team Secrets 수신이 거부**되므로, 불필요한 팀에서 탈퇴하면 해결됩니다.
10. **고정 버전이 지원 하한선 미달**: `apt-mark hold`로 고정한 버전이 라이프사이클 하한선보다 낮으면 “Update required”로 차단되므로, 고정을 해제하고 업그레이드하면 됩니다.

## 완료 후 검증 방법

### 네트워크 및 게이트웨이
- 업무용 PC에서 `curl -v https://api2.cursor.sh |& grep -C1 issuer:`를 실행하여 인증서 발급자가 **Amazon RSA**인지 확인합니다.
- `nslookup test.us9.cursorvm.com`을 실행하여 다단계 도메인 확인을 테스트하고, 모바일 핫스팟으로 전환하여 클라우드 컴퓨터에 연결한 뒤 **인증서 경고가 없는지** 확인합니다.

### ID 및 SSO
- 비개발 직군 계정으로 Grok Bot에 로그인하여 Cursor SSO를 통한 원클릭 로그인이 성공하는지 확인합니다.
- Bot 브라우저에서 “비밀번호 + 모바일 인증 코드”로 내부 SSO에 로그인하여 **FastPass 차단 팝업이 발생하지 않는지**, 업무용 PC의 컴플라이언스 정책이 정상적으로 적용되는지 확인합니다.

### 사설망 및 환경 스크립트
- Tailscale 또는 Cloudflare 콘솔에서 새 머신이 자동으로 네트워크에 진입하고 태그가 올바른지 확인합니다.
- 터미널에서 프라이빗 호스트로 ping 또는 curl을 실행하여 연결 상태를 확인하고, Team Setup 로그에 타임아웃이 없으며 **시크릿이 마스킹 처리되었는지** 확인합니다.

### 클라이언트 및 보안 베이스라인
- Windows 일반 사용자 계정으로 `%LOCALAPPDATA%\Programs`에 사일런트 설치되고 바탕화면 바로가기가 생성되는지 확인합니다.
- “설정 > 일반 > 자동 검토”에서 전역 규칙이 잠겨 수정 불가능한지 확인하고, 루트 디렉터리 파일 삭제 또는 미승인 Webhook 호출을 테스트하여 시스템이 **강제로 승인 팝업을 띄우는지** 확인합니다.

### 컴퓨터 라이프사이클
- 관리자가 콘솔에서 **VM 재구축**을 실행하여 기존 파일과 히스토리 기록이 그대로 보존되는지 확인합니다.
- 대규모 작업 완료 후 **Done**을 클릭하여 시스템이 다음 작업을 정상적으로 시작할 수 있는지 확인합니다.

## 추가 참고 자료

- 공식 문서: [Teams 및 엔터프라이즈용 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- 공식 문서: [ID 및 액세스 구성](https://cursor.com/cn/docs/grok-bot/identity)
- 공식 문서: [사설망 연결](https://cursor.com/cn/docs/grok-bot/private-networks)
- 공식 문서: [TLS 검사 프록시 구성](https://cursor.com/cn/docs/grok-bot/proxies)
- 공식 문서: [조직에 Grok Bot 배포하기](https://cursor.com/cn/docs/grok-bot/deployment)
- 공식 문서: [Grok Bot 컴퓨터 관리](https://cursor.com/cn/docs/grok-bot/computers)
- 공식 도움말: [요금제 및 결제](https://cursor.com/cn/help/grok-bot/plans)
- 공식 도움말: [팀 Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- 공식 도움말: [앱 연결](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- 공식 가이드: [Grok Bot 보안 아키텍처 설명](https://cursor.com/cn/docs/grok-bot/security)
