---
title: agently-cli(Agent 메일 CLI)
sidebar: false
prev: false
next: false
---

# agently-cli(Agent 메일 CLI)

<ToolMeta id="agently-cli" />

Tencent QQ 메일에서 출시한 공식 명령줄 도구로, Bot이 **클라우드 PC**에서 메일을 송수신하고 과거 메일을 검색하며 첨부파일을 다운로드하기에 적합합니다.
Bot이 클라우드 PC에서 메일을 송수신하고 기록을 검색하며 첨부파일을 다운로드합니다.
결론: Bot이 클라우드 PC 환경에서 일상적인 메일 송수신, 기록 검색 및 첨부파일 자동 다운로드를 독립적으로 처리할 수 있습니다.


## Bot에 보낼 프롬프트

아래 내용을 전체 복사하여 Grok Bot에게 전송하면, 클라우드 PC에서 자동으로 설치하고 검증합니다. 로그인이나 키 설정이 필요한 경우 일시 중지하고 사용자의 작업을 기다립니다.

<div class="tool-prompt">

````text
帮我在你的云电脑上安装 agently-cli（https://agent.qq.com），以后收发邮件、检索历史邮件和下载附件用它。需要登录或授权时停下来把链接发给我由我完成。
````

</div>

## 직접 해야 할 일

- QQ 메일 또는 Agent 메일 계정을 준비합니다.
- Bot이 보낸 인증 링크를 브라우저에서 열어 인증을 완료합니다.

## 출처

- [Agent 메일 공식 웹사이트](https://agent.qq.com)
- [agently-cli npm 패키지](https://www.npmjs.com/package/@tencent-qqmail/agently-cli)

> 이 페이지는 커뮤니티에서 비공식적으로 정리한 것으로, 해당 툴 제조사 및 xAI와 어떠한 제휴 관계도 없으며, 명령어는 공식 문서를 따릅니다.

[← 목차로 돌아가기](/tools/)
