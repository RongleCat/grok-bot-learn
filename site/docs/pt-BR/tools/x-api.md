---
title: Publicação via API do X (OAuth 1.0a PIN)
sidebar: false
prev: false
next: false
---

# Publicação via API do X (OAuth 1.0a PIN)

<ToolMeta id="x-api" />

Uma solução de chamada da API oficial do X baseada em autorização OAuth 1.0a PIN, ideal para permitir que o Bot execute com segurança postagens, envio de imagens e exclusão de posts no **computador em nuvem**.

A conclusão é: esta ferramenta serve apenas para permitir que o Bot publique posts, envie imagens e exclua posts no computador em nuvem.

## Prompt para enviar ao Bot

Copie todo o conteúdo abaixo e envie para o seu Grok Bot; ele instalará e verificará tudo automaticamente no computador em nuvem, pausando para aguardar sua ação caso seja necessário fazer login ou configurar chaves.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置 X API 发帖（https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth），以后发帖、传图和管理推文用它。需要填密钥时请提醒我自己填，需要登录授权时把链接发给我。
````

</div>

## O que você precisa fazer

- Criar um aplicativo no portal de desenvolvedores do X e conceder permissões de leitura e gravação (Read and Write).
- Abrir o link de autorização e, após receber o código PIN exibido na página, enviá-lo ao Bot.

## Fontes

- [Documentação oficial do X: PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> Esta página é uma compilação não oficial da comunidade e não possui vínculo com o desenvolvedor da ferramenta nem com a xAI; os comandos oficiais prevalecem.

[← Voltar ao índice](/tools/)
