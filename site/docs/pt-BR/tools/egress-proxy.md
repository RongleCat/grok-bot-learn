---
title: Proxy de Saída Fixo (Túnel SSH)
sidebar: false
prev: false
next: false
---

# Proxy de Saída Fixo (Túnel SSH)

<ToolMeta id="egress-proxy" />

O proxy de saída fixo utiliza o encaminhamento dinâmico de portas do SSH para criar um proxy SOCKS5 local, ideal para que o Bot mantenha um IP de saída estável ao **acessar serviços com restrições geográficas**.

## Prompt para enviar ao Bot

Copie todo o conteúdo abaixo e envie para o seu Grok Bot. Ele fará a instalação e a verificação automáticas no computador na nuvem e pausará aguardando sua ação caso seja necessário fazer login ou configurar chaves.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于 SSH 隧道的固定出口代理（https://man.openbsd.org/ssh），以后访问受地域限制的服务用它。需要填服务器地址和私钥时请提醒我自己填。
````

</div>

## O que você precisa fazer

- Preparar um servidor no exterior compatível com login por chave SSH.
- Seguir as orientações para gravar a chave privada de login e as informações de conexão em um arquivo confidencial por conta própria.

## Fontes

- [Manual do OpenSSH ssh (encaminhamento dinâmico -D)](https://man.openbsd.org/ssh)

> Esta página é uma compilação não oficial da comunidade e não possui qualquer vínculo com o desenvolvedor da ferramenta nem com a xAI; os comandos devem seguir a documentação oficial.

[← Voltar ao índice](/tools/)
