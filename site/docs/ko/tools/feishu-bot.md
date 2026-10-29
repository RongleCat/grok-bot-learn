---
title: Feishu 봇 지속 연결
sidebar: false
prev: false
next: false
---

# Feishu 봇 지속 연결

<ToolMeta id="feishu-bot" />

Feishu 공식 Python SDK 기반의 지속 연결 메시지 솔루션으로, 공인 IP가 필요 없는 **클라우드 PC**에서 이벤트 리스닝 및 그룹 채팅 봇 협업을 구현하는 데 적합합니다.

## Bot에 보낼 프롬프트

아래 내용 전체를 복사하여 Grok Bot에 전송하면 클라우드 PC에 자동으로 설치 및 검증하며, 로그인이나 키 설정이 필요할 때는 일시 정지하고 사용자의 작업을 기다립니다.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于飞书 Python SDK（https://github.com/larksuite/oapi-sdk-python）的长连接机器人，以后接收群聊事件和派发任务用它。需要填密钥时请提醒我自己填。
````

</div>

## 직접 해야 할 일

- Feishu 오픈 플랫폼에서 사내 자체 앱을 생성하고 지속 연결 및 봇 기능을 활성화합니다.
- 안내에 따라 앱의 App ID 및 App Secret을 직접 입력합니다.

## 출처

- [Feishu 공식 Python SDK(larksuite/oapi-sdk-python)](https://github.com/larksuite/oapi-sdk-python)
- [Feishu 오픈 플랫폼](https://open.feishu.cn/)

> 본 페이지는 커뮤니티에서 비공식적으로 정리한 내용이며, 해당 도구 제조사 및 xAI와 어떠한 제휴 관계도 없습니다. 명령어는 공식 문서를 기준으로 합니다.

[← 목록으로 돌아가기](/tools/)
