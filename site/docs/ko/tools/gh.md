---
title: GitHub CLI(gh)
sidebar: false
prev: false
next: false
---

# GitHub CLI(gh)

<ToolMeta id="gh" />

GitHub 공식 명령줄 도구로, Bot이 **클라우드 PC**에서 비공개 리포지토리를 복제하고 코드를 푸시하며 PR을 생성하고 Actions를 관리하는 데 적합합니다.

결론: 이 도구는 Bot이 클라우드 PC에서 GitHub 비공개 리포지토리를 복제하고, 코드를 푸시하며, PR을 생성하고 Actions를 관리하는 용도로만 사용됩니다.

## Bot에 보낼 프롬프트

아래 내용을 전체 복사하여 Grok Bot에게 전송하면, 클라우드 PC에 자동으로 설치하고 검증하며 로그인이나 키 설정이 필요할 때 일시 중지하고 사용자의 작업을 기다립니다.

<div class="tool-prompt">

````text
帮我在你的云电脑上安装 GitHub CLI（https://github.com/cli/cli/blob/trunk/docs/install_linux.md），以后管理代码仓库、推送分支和提交 PR 用它。需要登录或授权时停下来把链接发给我由我完成。
````

</div>

## 직접 해야 할 일

- GitHub 계정 준비.
- 브라우저에서 인증 링크를 열고 해당하는 일회용 인증 코드를 입력.

## 출처

- [GitHub CLI Linux 설치 문서](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 공식 매뉴얼](https://cli.github.com/manual/gh_auth_login)

> 이 문서는 커뮤니티에서 비공식적으로 정리한 것으로, 해당 도구 제작사 및 xAI와 어떠한 제휴 관계도 없으며, 명령어는 공식 문서를 따릅니다.

[← 목록으로 돌아가기](/tools/)
