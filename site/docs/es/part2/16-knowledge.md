# Capítulo 16 Casos prácticos: Ingesta automática de conocimiento e integración con WeChat

Los favoritos del móvil se desordenan fácilmente, los archivos de los grupos caducan a menudo y, cuando estás fuera de casa o de la oficina, no puedes aprovechar Grok Bot ejecutándose en la nube las **24 horas del día, los 7 días de la semana (7×24 h)**.

1. Páginas web y vídeos cortos: Usa Webhook con Atajos de iOS para una **ingesta estructurada en un solo clic**.
2. Capturas de pantalla y grabaciones de audio: Los reenvíos de WeChat no extraen los archivos adjuntos; expórtalos **a través de un puente temporal en la red pública**.
3. Control de conversaciones: Usa el plugin oficial «微信ClawBot» mediante sondeo largo (long polling) para **controlar Grok Bot directamente desde la ventana de chat de WeChat**.

## Comparativa de capacidades y límites de las tres soluciones de automatización

![Comparativa de capacidades y límites de las tres soluciones de automatización](/info/16-knowledge-s1.png)

| Solución y escenario | Mecanismo y autenticación | Dificultades y precauciones |
| :--- | :--- | :--- |
| Ingesta unidireccional (páginas web, cuentas oficiales y vídeos cortos) | Atajos envía un POST al Webhook con clave Bearer para la ingesta | Solo recepción unidireccional |
| Ingesta multimodal (registros de WeChat, grabaciones de audio, múltiples capturas de pantalla) | Envío directo de texto; los archivos usan el almacenamiento temporal de filebin.net para generar enlaces públicos, y el Bot los descomprime e ingesta | **El almacenamiento en la nube no tiene contraseña: no envíes contenido sensible**; extraer fotogramas de paquetes grandes consume más tokens |
| Bidireccional con WeChat (enviar comandos, consultar información, controlar el Bot) | Vinculación escaneando código QR en WeChat; iLink colabora con scripts en la nube para escuchar y reenviar texto plano mediante Webhook | **Es necesario controlar la frecuencia para evitar consumo innecesario en reposo** |

A partir del 12-10-2026, se unifica bajo The X Subscription, descontándose por uso de la cuota semanal.

**El plan Plus de $8/mes no incluye Grok Bot**; es necesario elegir Premium ($30/mes o $300/año, cuota 4x), Super ($100/mes o $1000/año, cuota 15x) o Ultra ($200/mes o $2000/año, cuota 50x).

Para más detalles, consulta la documentación oficial de [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans).

## Caso práctico 1: Creación de un pipeline de ingesta automática de conocimiento con Webhook y Atajos

![Caso práctico 1: Creación de un pipeline de ingesta automática de conocimiento con Webhook y Atajos](/info/16-knowledge-s2.png)

**Esta solución centraliza todo el rastreo, la transcripción de audio y vídeo y el resumen en la nube de Grok Bot; el teléfono móvil solo envía la URL como disparador.

** 铁柱AGI（@cgnot996）aprovechó el Webhook de las [Rutinas](https://cursor.com/cn/help/grok-bot/routines) para lograr el inicio inmediato con solo enviar la petición.

### Pasos de configuración
1. En el cliente de escritorio, ve a Details y busca Routines. Haz que el Bot cree una tarea de análisis y **guarda de forma segura la URL del Webhook y la key generadas**.
2. Crea un nuevo atajo llamado "Enviar al Bot de la base de conocimiento", añade la acción "Obtener contenido de URL" y configura los parámetros según la tabla.

| Parámetro | Valor de configuración |
|---|---|
| URL | Dirección del Webhook |
| Método | POST |
| Cabeceras | Clave `Authorization`, valor `Bearer <key>` |
| Cuerpo de la solicitud | Selecciona JSON, añade "Entrada de atajo" |

3. **Añade un cuadro de entrada auxiliar para aplicaciones cerradas**. WeChat suele deshabilitar el panel de compartir, por lo que es necesario crear un segundo atajo ("Elegir del menú" más "Solicitar texto") como intermediario, vincularlo al Botón de acción del iPhone y pulsar el botón para pegar y enviar.

### Criterios de aceptación
> Fuente: [Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建](/cases-img/fs06-1.jpg)
Tras pulsar en Compartir, **en unos segundos el estado en el cliente de escritorio cambiará a En ejecución (Running)**. Una vez finalizada la tarea, la base de conocimiento generará automáticamente una entrada estandarizada:
- ID del vídeo o enlace corto original de la página web
- Ruta de almacenamiento en la nube y página de conocimiento asociada
- Puntos clave extraídos y etiquetas del autor
- Coste en créditos consumidos por cada análisis

Al recopilar artículos extensos como «Mi experiencia completa con Obsidian en 2026», es capaz de generar retroenlaces de forma automática.

Para ver una demostración práctica, consulta [《Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh).

## Caso práctico 2: Ingesta integrada de registros de chat de WeChat y material multimodal

### Resumen del caso
- Los chats de WeChat se reenvían de forma combinada y empaquetada a Grok Bot, que los descomprime automáticamente y emite un acuse de recibo.
- **Uso de filebin.net como intermediario** para eliminar la dependencia de rutas locales.
- Despliegue en Mac e iPhone de un atajo con **cinco modos de captura**.

### Qué es: Por qué es necesario introducir un almacenamiento temporal como intermediario

Entre distintos dispositivos no se pueden leer discos locales, y meter archivos ZIP grandes de WeChat en el cuerpo de la solicitud suele causar problemas de tiempo de espera agotado (timeout).

1. El texto se envía directamente mediante JSON.
2. Las imágenes, grabaciones de audio y archivos ZIP se suben primero a filebin.net, y luego se envía el enlace al Bot para su descarga.
3. El ID del contenedor debe tener **al menos 8 caracteres alfanuméricos aleatorios** para evitar colisiones de nombres y filtraciones no deseadas.
4. Por defecto, los archivos se conservan durante 7 días y no están cifrados: **está terminantemente prohibido subir datos privados o secretos comerciales**.

### Cómo hacerlo: Pasos de configuración detallados

#### 1. Configurar el Webhook
Envía este prompt en la conversación principal del cliente de escritorio:

```text
帮我创建一个 Webhook 触发的例行任务。快捷指令会用 POST 请求发来一个 JSON，里面只有一个字段 info。info 可能是我输入的文字，也可能是一个文件下载链接，比如微信聊天记录压缩包、截图、录音。收到后：如果是链接就先下载文件再读取，压缩包先解压；然后整理出要点，收录进知识库，最后给我一份回执，写清楚收录了什么、存在哪里。
```

**Tras enviarlo, anota la URL del Webhook y la key en las "Rutinas" (Routines) del Bot.**

#### 2. Configurar el atajo
Enlace de importación: `https://www.icloud.com/shortcuts/2b77155d7c744110a0f0f9ef1bdc42bf`
Edita "【分享版】发送给知识库 Bot", introduce la URL, la key y un **ID de almacenamiento complejo de al menos 8 caracteres** (como `kb7x9m2q`); las cabeceras ya vienen configuradas internamente y no requieren cambios.

#### 3. Ingesta de registros de WeChat
- **En Mac**: En Reenvío combinado hacia otra aplicación, selecciona dicho atajo y haz clic en Recibir reenvío; el ZIP se subirá al almacenamiento en la nube, se enviará el enlace y el Bot lo procesará de inmediato.
- **En el móvil**: En Reenvío combinado, selecciona este atajo y pulsa en Recibir reenvío; puedes fijarlo en el área de uso frecuente mediante "Editar acciones".

#### 4. Ejecución y captura independientes
En Mac se usa Raycast o la barra de menús; en el móvil se vincula al Botón de acción.
- Capturas de pantalla / Grabaciones de audio: Tras confirmar o finalizar la grabación, se suben al almacenamiento en la nube y se envía el enlace.
- Introducir texto: **Se añade directamente en el JSON y se envía**, sin pasar por el almacenamiento en la nube.
- Seleccionar imágenes adicionales: Tras seleccionar las imágenes, introduce una descripción y se empaquetarán para subirlas.
- Recibir reenvío: Si no se recibe contenido, lee el portapapeles y lo envía.

### Criterios de un resultado óptimo

> Fuente: [微信聊天记录打通 Grok Bot：快捷指令进阶版](https://x.com/cgnot996/status/2107039351519707602)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![微信聊天记录打通 Grok Bot：快捷指令进阶版](/cases-img/fs11-0.png)

![微信聊天记录打通 Grok Bot：快捷指令进阶版](/cases-img/fs11-1.jpg)

Tras enviar, espera entre unos segundos y una decena de segundos para que el Bot devuelva un **acuse de recibo estandarizado**:
- **Archivo de chats grupales**: Extrae los puntos centrales de la discusión y proporciona las rutas de la nota y del paquete comprimido.
- **Catalogación de recursos**: Al enviar 13 sitios web, los clasifica e indexa automáticamente y facilita los enlaces a la base de conocimiento.

Para consultar los pasos detallados, visita [《微信聊天记录打通 Grok Bot：快捷指令进阶版》](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb)。

## Caso práctico 3: Conectar Grok Bot directamente a WeChat para control bidireccional

![Caso práctico 3: Conectar Grok Bot directamente a WeChat para control bidireccional](/info/16-knowledge-s4.png)

### Resumen del caso
Kin conectó Grok Bot a WeChat, **permitiendo controlar el Bot en la nube directamente enviando mensajes desde el teléfono móvil**.

1. Pedir a Grok que utilice iLink para escribir un script de sondeo largo (long polling).
2. Crear un Webhook para recibir instrucciones.
3. Habilitar «微信ClawBot» en WeChat y escanear el código QR para vincularlo.

Funciona íntegramente mediante peticiones salientes por sondeo largo, por lo que **no es necesario abrir puertos a la red pública**.

### Qué es: El mecanismo de sondeo largo de 微信ClawBot e iLink

La solución utiliza el plugin oficial «微信ClawBot» y la interfaz iLink (`ilinkai.weixin.qq.com`), sin modificar la memoria del cliente, por lo que **no existe ningún riesgo de suspensión o baneo de cuenta**.

Toda la comunicación consiste en peticiones salientes, **sin necesidad de abrir puertos públicos**:
1. Grok Bot llama en segundo plano a `getupdates` mediante sondeo para obtener mensajes y, tras procesarlos, llama a `sendmessage` para responder.
2. Tras recibir el texto, el Webhook lo transfiere a los respectivos bots especializados para su ejecución colaborativa; para más detalles, consulta la documentación [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

### Cómo hacerlo: Pasos detallados y prompt completo

1. Envía el prompt en la conversación principal del ordenador y espera a que cree la rutina «微信下旨入口».
::: details Cómo hacerlo: Pasos detallados y prompt completo
```text
我想把你接到我的微信上，让我能在微信里直接给你发消息、收到你的回复。请按下面的思路做，每做完一步告诉我结果，需要我操作的地方停下来等我。

1、先调研方案：腾讯「微信ClawBot」插件用的是 iLink 接口（ilinkai.weixin.qq.com）。请确认怎么用 getupdates 长轮询收消息、怎么用 sendmessage 回消息。整个程序只走出站请求，不要开公网端口。

2、在 Grok Bot 里建一个由 webhook 触发的 routine，名字可以叫「微信下旨入口」。建好后告诉我去 routine 面板复制 Webhook URL 和 key，然后弹出加密弹框让我填进去，不要让我在聊天里发明文。

3、在你的云端电脑上写一个小转发程序：收到微信消息后 POST 给这个 routine；你处理完以后，用一个 reply 脚本把回复发回微信，同时在我们的主聊天里同步一份。

4、等我在手机微信里启用 ClawBot 插件以后，生成二维码让我用手机扫码确认，同时给我一个可以在微信里直接打开的备用链接。二维码大约 5 分钟有效。

5、绑定成功后，提醒我先在 ClawBot 对话里发一句话，因为回复要用到这条消息带的 context_token。

6、规则：只认绑定的这一个人，别人的消息不处理；回复一律用纯文本，不要用 Markdown，因为微信不渲染 Markdown。

7、最后告诉我：云端电脑重启以后，怎么把转发程序重新拉起来；如果遇到错误码 -14（凭证过期），提醒我重新扫码。
```
:::
2. Copia la URL y la key de la rutina. **Está terminantemente prohibido enviarlas en texto plano en el chat**; basta con introducirlas en la ventana modal de datos confidenciales hasta que muestre "Guardado de forma segura y mantenido privado", consulta [Almacenamiento seguro de información confidencial](https://cursor.com/cn/help/grok-bot/secrets).
3. La versión de WeChat debe ser **iOS 8.0.70 / Android 8.0.69 o superior**. En "Yo" -> "Ajustes" -> "Plugins", habilita el plugin con el icono de la langosta roja «微信ClawBot».
4. Envía "El plugin ya está activado", y escanea el código QR con WeChat para autorizar (el código QR es **válido durante 5 minutos**; si caduca, usa el enlace de respaldo).
5. **Es obligatorio enviar un primer mensaje de forma proactiva en WeChat** (por ejemplo, "Hola"). La interfaz necesita este mensaje para capturar el `context_token` y establecer la conexión; tras enviarlo, el canal quedará oficialmente listo.

### Criterios de un resultado óptimo

> Fuente: [如何把 Grok Bot 接入你的微信？保姆级新手指南来了（附详细提示词）](https://x.com/KinGao476942/status/2108132811635032316)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![如何把 Grok Bot 接入你的微信？保姆级新手指南来了（附详细提示词）](/cases-img/fs29-0.jpg)

![如何把 Grok Bot 接入你的微信？保姆级新手指南来了（附详细提示词）](/cases-img/fs29-1.jpg)

Prueba estos cuatro puntos en WeChat para comprobar **si todo funciona correctamente**:
1. Envía "Hola", y responderá **en cuestión de segundos con texto plano** de confirmación.
2. Invoca al Bot experto en Twitter/X, y WeChat generará directamente una lista de selección de temas.
3. Envía el enlace de un vídeo para invocar al Bot experto en descargas, y devolverá el texto limpio y procesado.
4. Verifica en el cliente de escritorio que todos los comandos y registros estén sincronizados.

Para ver capturas y la guía paso a paso, consulta [《如何把 Grok Bot 接入你的微信？保姆级新手指南来了（附详细提示词）｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)。

## Errores comunes y trampas a evitar

1. Antes de reenviar, **es obligatorio descargar los archivos adjuntos localmente**, de lo contrario el ZIP exportado solo contendrá texto de marcador de posición.
2. filebin.net no tiene contraseña; no uses `test` ni `123456`, **es obligatorio definir una cadena aleatoria de al menos 8 caracteres**, y está terminantemente prohibido subir documentos de identidad, tarjetas bancarias y contratos confidenciales.
3. Al configurar el Webhook, no pegues la key en el chat; **guárdala en una tarjeta segura**; antes de compartir atajos, borra tu key y URL personales.
4. El código QR de ClawBot caduca en 5 minutos; si no hay respuesta o devuelve el código de error `-14`, significa que **las credenciales han expirado y es necesario volver a generar y escanear el código QR**.
5. Tras hacer Reset o reiniciar el ordenador en la nube, el proceso de sondeo en Python se detendrá; si WeChat no responde, ve al cliente de escritorio y **pídele al Bot que vuelva a levantar el script**.
6. WeChat no renderiza Markdown, por lo que **debes exigir respuestas en texto plano en las instrucciones (Instruction)** para evitar que aparezcan `**` o `#`.
7. **No ejecutes múltiples procesos de escucha de OpenClaw simultáneamente**, para evitar que compitan por los mensajes en la cola de iLink y se pierdan instrucciones.
8. The X Subscription descuenta de la cuota semanal, por lo que **los disparadores de alta frecuencia deben incluir filtros obligatoriamente**; si el consumo es muy rápido, pausa las rutinas no esenciales o flexibiliza las condiciones de activación.

## Cómo verificar y validar la configuración

1. **Probar el Webhook**: Envía una petición POST con `Authorization: Bearer <key>`. **Si devuelve 200, está listo**; un error 401 indica clave incorrecta y 404 URL incorrecta. Basta con que el estado de "Rutinas" en el ordenador pase a `Running…` y aparezcan los registros.
2. **Probar los Atajos**: Envía texto para comprobar si el acuse de recibo llega en unas decenas de segundos; reenvía 2 imágenes para probar el archivado. Las capturas de pantalla deben mostrar una vista previa de autorización y solo se transferirán tras pulsar Permitir.
3. **Probar WeChat y la sincronización**: Envía un mensaje a «微信ClawBot»; **si recibes respuesta en menos de 5 segundos**, la conexión es válida. Luego revisa el cliente de escritorio: si el registro de chat se ha sincronizado, todo el flujo está plenamente operativo.

## Lecturas complementarias

### Documentación oficial
- [例程](https://cursor.com/cn/help/grok-bot/routines)
- [安全存储机密信息](https://cursor.com/cn/help/grok-bot/secrets)
- [使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- [方案和计费](https://cursor.com/cn/help/grok-bot/plans)

### Artículos originales de casos prácticos de la comunidad
- [《Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- [《微信聊天记录打通 Grok Bot：快捷指令进阶版》](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb)
- [《如何把 Grok Bot 接入你的微信？保姆级新手指南来了（附详细提示词）｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)
