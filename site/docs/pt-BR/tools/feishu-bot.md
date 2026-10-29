---
title: Conexão persistente de bot do Feishu
sidebar: false
prev: false
next: false
---

# Conexão persistente de bot do Feishu

<ToolMeta id="feishu-bot" />

Solução de mensagens via conexão persistente baseada no SDK oficial em Python do Feishu, adequada para implementar escuta de eventos e colaboração com bots em chats em grupo em um **computador na nuvem** sem a necessidade de um IP público.

## Prompt para enviar ao Bot

Copie todo o conteúdo abaixo e envie para o seu Grok Bot; ele instalará e validará tudo automaticamente no computador na nuvem, pausando e aguardando sua ação caso encontre etapas de login ou configuração de chaves.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于飞书 Python SDK（https://github.com/larksuite/oapi-sdk-python）的长连接机器人，以后接收群聊事件和派发任务用它。需要填密钥时请提醒我自己填。
````

</div>

## O que você precisa fazer

- Criar um aplicativo interno corporativo na plataforma aberta do Feishu e habilitar a conexão persistente e os recursos de bot.
- Preencher o App ID e o App Secret do aplicativo por conta própria conforme as instruções.

## Fontes

- [SDK oficial em Python do Feishu (larksuite/oapi-sdk-python)](https://github.com/larksuite/oapi-sdk-python)
- [Plataforma Aberta do Feishu](https://open.feishu.cn/)

> Esta página é uma compilação não oficial da comunidade e não possui qualquer afiliação com o fornecedor desta ferramenta ou com a xAI; os comandos devem seguir a documentação oficial como referência.

[← Voltar ao índice](/tools/)
