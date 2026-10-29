---
title: X API 포스팅(OAuth 1.0a PIN)
sidebar: false
prev: false
next: false
---

# X API 포스팅(OAuth 1.0a PIN)

<ToolMeta id="x-api" />

OAuth 1.0a PIN 인증 기반의 X 공식 API 호출 솔루션으로, Bot이 **클라우드 PC**에서 안전하게 포스팅, 이미지 업로드 및 트윗 삭제 작업을 수행하도록 하는 데 적합합니다.

결론적으로: 이 도구는 Bot이 클라우드 PC에서 포스팅, 이미지 업로드 및 트윗 삭제를 수행하도록 하는 용도로만 사용됩니다.

## Bot에 보낼 프롬프트

아래 전체 내용을 복사하여 Grok Bot에 보내면, 클라우드 PC에서 자동으로 설치 및 검증을 진행하며, 로그인이나 키 설정이 필요할 때는 일시 정지하여 사용자의 작업을 기다립니다.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置 X API 发帖（https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth），以后发帖、传图和管理推文用它。需要填密钥时请提醒我自己填，需要登录授权时把链接发给我。
````

</div>

## 직접 해야 할 일

- X 개발자 플랫폼에서 앱을 생성하고 읽기/쓰기 권한을 활성화합니다.
- 인증 링크를 열고 페이지에서 PIN 번호를 확인한 후 Bot에 전송합니다.

## 출처

- [X 공식 문서: PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> 이 페이지는 커뮤니티 비공식 정리 문서이며 해당 도구 제조사 및 xAI와 어떠한 제휴 관계도 없습니다. 명령어는 공식 문서를 따릅니다.

[← 목록으로 돌아가기](/tools/)
