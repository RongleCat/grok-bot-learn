---
title: Proxy de salida fija (túnel SSH)
sidebar: false
prev: false
next: false
---

# Proxy de salida fija (túnel SSH)

<ToolMeta id="egress-proxy" />

El proxy de salida fija utiliza el reenvío dinámico de puertos SSH para configurar un proxy SOCKS5 local, ideal para que el Bot mantenga una IP de salida estable al **acceder a servicios con restricciones geográficas**.

## Prompt para enviar al Bot

Copia el texto completo de abajo y envíalo a tu Grok Bot; este se instalará y verificará automáticamente en la computadora en la nube, y se pausará para esperar tu intervención si requiere iniciar sesión o configurar claves.

<div class="tool-prompt">

````text
帮我在你的云电脑上配置基于 SSH 隧道的固定出口代理（https://man.openbsd.org/ssh），以后访问受地域限制的服务用它。需要填服务器地址和私钥时请提醒我自己填。
````

</div>

## Lo que debes hacer tú mismo

- Preparar un servidor en el extranjero que admita inicio de sesión mediante clave SSH.
- Escribir tú mismo la clave privada de inicio de sesión y la información de conexión en un archivo privado según las instrucciones.

## Fuentes

- [Manual de ssh de OpenSSH (reenvío dinámico -D)](https://man.openbsd.org/ssh)

> Esta página es una recopilación no oficial de la comunidad y no tiene afiliación con el proveedor de esta herramienta ni con xAI. Los comandos están sujetos a la documentación oficial.

[← Volver al índice](/tools/)
