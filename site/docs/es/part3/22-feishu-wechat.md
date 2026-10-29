# Capítulo 22 Integración con Feishu y WeChat

Conecte Grok Bot de forma segura a Feishu y WeChat sin necesidad de una IP pública ni de servidores propios.

The X Subscription (vigente a partir del 12 de octubre de 2026) descuenta la cuota semanalmente; **es obligatorio configurar el filtrado de mensajes en chats grupales**, de lo contrario las conversaciones triviales agotarán la cuota de toda la semana.

- **Colaboración multibot en Feishu**: utiliza la conexión persistente del SDK oficial de Python y la plantilla «Administrador de aplicaciones de Feishu».
- **Conexión directa de WeChat ClawBot**: a través del complemento oficial «WeChat ClawBot» y la interfaz iLink.
- **Recopilación mediante Atajos de WeChat**: mediante Atajos de Apple y Webhook para archivar registros.


![Integración con Feishu y WeChat](/info/22-feishu-wechat.png)

## Comparación de canales de integración y selección tecnológica

![Comparación de canales de integración y selección tecnológica](/info/22-feishu-wechat-s1.png)

**Ninguno de los tres métodos de integración requiere una IP pública**.

- Canal multibot de Feishu: diseñado para el trabajo en equipo y la asignación de tareas en chats grupales. Utiliza una conexión persistente saliente por WebSocket oficial, admite texto enriquecido y tarjetas interactivas, y en grupos solo responde a menciones con @ para proteger la cuota.
- Canal WeChat ClawBot: diseñado para asistente personal diario y orquestación. Utiliza sondeo largo (long polling) de iLink, solo admite texto plano y se basa en una lista blanca de chats individuales para evitar activaciones innecesarias.
- Canal de Atajos de WeChat: diseñado para la ingesta de recursos gráficos, de texto y de audio. Utiliza inserción unidireccional por Webhook con confirmación de recepción, se activa bajo demanda y no genera consumo adicional si no hay mensajes.

## Integración de equipos en Feishu: colaboración multibot y Administrador de aplicaciones de Feishu

![Integración de equipos en Feishu: colaboración multibot y Administrador de aplicaciones de Feishu](/info/22-feishu-wechat-s2.png)

### Mecanismo de conexión persistente y disparador de timbre en Feishu

Utiliza una conexión persistente saliente, **eliminando la necesidad de IP pública, certificados y apertura de puertos**.

1. Aplicación personalizada de Feishu: responsable de enviar y recibir mensajes en chats grupales e individuales.
2. Programa de reenvío en la nube: escucha la conexión persistente en segundo plano y retransmite los mensajes.
3. Disparador de timbre: despierta al bot y llama al SDK para responder.

Para evitar configuraciones repetitivas, utilice el «Administrador de aplicaciones de Feishu» para **crear aplicaciones automáticamente escaneando un código QR**.

### Cómo implementarlo: de un solo bot operativo a la colaboración multibot

#### Escanear el código para crear el primer bot (Editor jefe de artículos)
1. En un chat privado, pídale al bot que invoque el SDK de Feishu para generar el código QR de creación de la aplicación. **Este enlace es una credencial de un solo uso exclusiva para administradores; nunca haga clic en enlaces de terceros ni los reenvíe.**
2. Abra el enlace en el navegador, haga clic en «Crear» y confirme los permisos; las credenciales se transmitirán de vuelta automáticamente.
3. Tras recibir el mensaje de prueba en Feishu, responda con un mensaje; **el bot escribirá automáticamente su Open ID en la lista blanca**.

#### Crear la rutina de timbre
1. Haga clic en el nombre del bot en la parte superior de la conversación y abra el panel **Details** en la sección de detalles. Consulte los pasos en [Rutinas](https://cursor.com/cn/help/grok-bot/routines.md).
2. Cree un timbre Webhook en las rutinas para obtener la dirección POST to y la clave key.
3. **Debe enviar las credenciales en el cuadro de entrada cifrado que muestra el bot** para evitar filtraciones en texto plano. Envíe un texto de prueba en un chat individual; si el bot responde con normalidad, la configuración estará completa.

#### Creación por lotes de aplicaciones y colaboración en chats grupales
1. Importe la plantilla `https://x.ai/bot/AJpUlCwa8tyMX7L5UHnuY`. La tabla de registro y los scripts de recuperación se almacenan en un repositorio privado de Git, sin guardar claves en texto plano.
2. Ordene al bot administrador generar enlaces de escaneo por lotes (**cada enlace es válido durante 1 hora**), escanee el código e introduzca la key en la ventana emergente cifrada; el administrador iniciará automáticamente el reenvío.
3. Cree un grupo e invite a los bots, **envíe `@所有人` para confirmar e informar sobre su ámbito de competencia**; `@文章主编` invocará a `虚拟机服务管家`, y el administrador de servicios enviará la tabla de registro al grupo para completar la colaboración.

#### Seguridad de la interacción
- **Validación del origen de instrucciones**: solo responde a instrucciones directas de administradores en la lista blanca dentro del grupo.
- **Confirmación mediante tarjetas de Feishu**: para operaciones de alto riesgo como modificaciones de configuración, escritura en bases de datos o reinicios, se envía una tarjeta con botones de «Aprobar» y «Rechazar», **permitiendo la autorización secundaria directamente con un clic dentro de Feishu**.

### Criterios de rendimiento esperado

- **Latencia de extremo a extremo inferior a 1 segundo**: las respuestas a los mensajes son prácticamente instantáneas.
- **Enrutamiento preciso de mensajes en chats grupales**: silencio ante charlas informales, solo responde quien sea mencionado individualmente con @, y ante @todos cada uno informa según sus responsabilidades sin adelantarse unos a otros.
- **Autorrecuperación de alta disponibilidad**: se reinicia en menos de 5 segundos tras salir, inspecciona bloqueos cada 5 minutos y se recupera en aproximadamente 9 segundos si el proceso se termina de forma forzada.

Para la práctica real, consulte [«Tutorial paso a paso para la integración de Grok Bot en Feishu en equipos (con plantilla de Administrador de Feishu)»](https://jcng5q8n0f3z.feishu.cn/wiki/F2VXw4hVbirRUjk5QgFcWS0jnJg).

## Integración personal en WeChat: conexión directa con el complemento WeChat ClawBot

![Integración personal en WeChat: conexión directa con el complemento WeChat ClawBot](/info/22-feishu-wechat-s3.png)

Utiliza la interfaz oficial iLink (`ilinkai.weixin.qq.com`) mediante sondeo largo exclusivamente saliente, **sin abrir puertos a la red pública, cumpliendo con la normativa y sin riesgo de bloqueo de cuenta**.

### Integración en tres pasos

1. **Enviar el prompt**: envíe la siguiente instrucción al bot principal desde el ordenador y espere a que se generen automáticamente los componentes de comunicación.
::: details Integración en tres pasos
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
2. **Configurar claves**: abra la rutina «Entrada de instrucciones de WeChat» del bot principal, copie el **POST to** y la **key** del Webhook y envíelos en el cuadro cifrado.
3. **Vinculación y activación**:
   - La versión de WeChat debe ser **iOS ≥ 8.0.70, Android ≥ 8.0.69**; habilite «WeChat ClawBot» en «Ajustes - Complementos».
   - Envíe «El complemento ya está habilitado» al bot en el ordenador y escanee el código QR con WeChat para autorizarlo (el código QR es válido durante 5 minutos).
   - **Es obligatorio enviar activamente un primer mensaje a WeChat ClawBot** (por ejemplo, «Hola») para obtener el `context_token` y activar la respuesta.

### Criterios de aceptación

- **Sincronización bidireccional**: respuestas en cuestión de segundos en WeChat y archivado en tiempo real en el ordenador.
- **Orquestación de subagentes**: asigne directamente desde WeChat tareas de búsqueda en Twitter y transcripción de video.
- **Aislamiento de seguridad**: las cuentas de WeChat no vinculadas no pueden activar el bot.

Para más detalles, consulte [«¿Cómo integrar Grok Bot en tu WeChat? Guía paso a paso para principiantes (con prompts detallados) | Kin»](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg).

## Ingesta de contenido de WeChat: Atajos conecta el historial de chat y multimedia

Transfiera el paquete ZIP de mensajes combinados y reenviados a un almacenamiento temporal en la nube mediante Atajos, **y luego envíelo al Webhook de Grok Bot para su archivado automático**.

### Configuración y funcionamiento

1. Envíe el prompt en la ventana de chat de Grok Bot para crear la rutina:
```text
帮我创建一个 Webhook 触发的例行任务。快捷指令会用 POST 请求发来一个 JSON，里面只有一个字段 info。info 可能是我输入的文字，也可能是一个文件下载链接，比如微信聊天记录压缩包、截图、录音。收到后：如果是链接就先下载文件再读取，压缩包先解压；然后整理出要点，收录进知识库，最后给我一份回执，写清楚收录了什么、存在哪里。
```
En la lista de Routine en la página de detalles, **copie la dirección POST to y la clave key del Webhook**.

2. Importe el atajo: `https://www.icloud.com/shortcuts/2b77155d7c744110a0f0f9ef1bdc42bf`.

3. Introduzca el POST to, la key y el ID del servicio de alojamiento. Los archivos en `filebin.net` se conservan durante 7 días; **el ID debe tener 8 o más caracteres aleatorios** (como `kb7x9q2m`) para evitar sobreescrituras y filtraciones; **asegúrese de borrar estos tres campos antes de compartirlo**.

4. En WeChat, seleccione múltiples mensajes del historial de chat, elija reenviar de forma combinada a otras aplicaciones y seleccione «Recibir reenvío» en el atajo «Enviar al bot de base de conocimientos». Si no se recibe ningún reenvío, leerá el portapapeles, y también se puede seleccionar «Captura de pantalla» o «Grabación de audio» para transferencia directa.

### Criterios de aceptación

- **Análisis multimedia completo**: descomprime y clasifica imágenes, documentos y notas de voz (por ejemplo, indexando 13 sitios web de inspiración de diseño por sitio completo, app o componentes).
- **Confirmación estandarizada**: detalla claramente los puntos temáticos clave, la ruta de almacenamiento de las notas y la ruta de archivado del archivo ZIP original.

Referencia: [«Conectar el historial de chat de WeChat con Grok Bot: Edición avanzada de Atajos»](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb).

## Errores comunes y soluciones de resolución de problemas

### 1. Configuración insuficiente de permisos en Feishu que impide recibir mensajes de grupo

- **Problema**: El chat individual funciona con normalidad, pero en el grupo no hay respuesta al usar `@` ni se generan registros, debido a que en la selección inicial de 7 permisos se omitió «Obtener todos los mensajes que mencionan al bot en el grupo».
- **Solución**: Genere un enlace de permisos adicionales escaneando el código mediante el SDK; una vez que el administrador confirme la ampliación a 14 permisos, **no será necesario publicar una nueva versión**.

### 2. Errores de filtrado en chats grupales de Feishu y reenvío tras desconexión persistente

1. Pérdida de mensajes y respuestas simultáneas no deseadas: En Feishu, `@所有人` no se incluye en el array de menciones (mention), y si no se valida el ID, todos los bots responderán al mismo tiempo. **El script debe verificar con precisión el ID de destino y responder únicamente a «`@自己`» o «`@所有人`»**.
2. Respuestas duplicadas: La plataforma reenviará automáticamente los mensajes pendientes tras restablecerse la red; **bajo ninguna circunstancia reenvíe manualmente por segunda vez**.

### 3. Falta de cadena de confianza y tarjetas de autorización en llamadas inter-bot

1. Si los bots no responden al llamarse entre sí en el grupo, se debe a que **los mensajes entre bots no son confiables de forma predeterminada** y quedan bloqueados en chats privados en espera de confirmación.
2. Configure una lista blanca en la capa de reenvío que reconozca el Open ID del administrador; para operaciones de alto riesgo, envíe **tarjetas interactivas de Feishu con opciones de Aprobar/Rechazar** para confirmación.

### 4. Ruta incorrecta del entorno de ejecución de Python en la máquina virtual

- Si el script muestra un error indicando que no se encuentra `lark-oapi`, generalmente se debe a que al configurar la tarea del demonio **se utilizó por error el `/usr/bin/python3` predeterminado del sistema**.
- En los scripts de inicio, Supervisor y tareas programadas, **debe definir de forma fija la ruta absoluta del entorno virtual** (como `/home/user/venv/bin/python3`) y evitar llamar directamente al entorno global del sistema.

### 5. Caducidad del código QR de WeChat ClawBot y código de error -14

- El código QR **solo es válido durante 5 minutos** y caducará si se supera el tiempo; escanéelo con el móvil en cuanto aparezca.
- Si el backend reporta el código de error **`-14`**, significa que las credenciales han caducado; basta con volver a generar el código QR y pedirle al administrador que lo escanee nuevamente.

### 6. Formato de mensajes desordenado en WeChat y fallos de renderizado de Markdown

- WeChat **no procesa Markdown**, por lo que los asteriscos, comillas invertidas y símbolos de encabezado se mostrarán literalmente.
- Añada un filtrado en el prompt de integración o en el script de reenvío para **convertir todo uniformemente a texto plano con saltos de línea** antes de enviarlo a WeChat.

### 7. Falta de archivos multimedia no descargados en el archivo ZIP reenviado de WeChat

WeChat no conserva los archivos originales en el dispositivo si no se abren; aquellos que no se hayan abierto para descargarse no se incluirán en el archivo comprimido y se perderán imágenes al descomprimirlo.

1. Antes de reenviar, **abra una por una las imágenes y archivos que necesite guardar**.
2. Espere a que se carguen completamente de forma local antes de empaquetar y reenviar.

### 8. Conflicto de nombres y riesgos de filtración de privacidad en el almacenamiento temporal

`filebin.net` no dispone de un sistema de cuentas; si el ID es demasiado simple, habrá colisiones, lo que provocará errores o la descarga de archivos ajenos. Al usarlo, tenga en cuenta:

- El ID del servicio de almacenamiento **debe configurarse como una cadena aleatoria de al menos 8 caracteres**.
- No suba información privada como contraseñas o documentos de identidad.
- Antes de compartir el atajo, **elimine su ID exclusivo y la clave del Webhook**.

### 9. Control del consumo de cuota bajo la suscripción unificada The X Subscription

Las charlas informales de los miembros del grupo activarán la ejecución inútil de rutinas, **lo que agotará la cuota semanal en uno o dos días y hará que el bot deje de responder**.

Desde el 12 de octubre de 2026, The X Subscription deduce la cuota semanalmente de un fondo compartido.

El plan Plus ($8/mes) no incluye Grok Bot; únicamente lo incluyen Premium ($30/mes, cuota 4x), Super ($100/mes, cuota 15x) y Ultra ($200/mes, cuota 50x).

Para controlar el consumo, céntrese en dos aspectos:
1. **Active el Webhook únicamente ante menciones directas (`@自己`) o instrucciones específicas de administradores**.
2. Queda estrictamente prohibida la escucha集群 indiscriminada de todo el grupo; evite configurar sondeos frecuentes con intervalos cortos.

Para consultar las reglas detalladas, remítase a [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans.md) y [Rutinas](https://cursor.com/cn/help/grok-bot/routines.md).

## Análisis de casos prácticos reales

### Colaboración multibot en Feishu (铁柱AGI)
Es posible lograr la colaboración sin IP pública; **la clave radica en utilizar conexiones persistentes salientes para evitar la apertura de puertos**.
1. **Registro por lotes**: Autorización mediante escaneo de código con el SDK de Python de Feishu; el bot administrador lee la tabla de respaldo en Git y gestiona las claves y Webhooks de 3 bots: editor jefe, contabilidad y máquina virtual.
2. **Confirmación de seguridad**: En el grupo solo se responde a `@自己` o `@所有人`. **Para operaciones altamente sensibles, el bot envía tarjetas con botones para autorización manual.**

### Terminal portátil de WeChat ClawBot (Kin)
Orqueste bots de gestión de Twitter y extracción de textos publicitarios dentro de WeChat; **utilizar el sondeo largo del complemento oficial evita el bloqueo de cuentas**.
1. Envíe el prompt al ordenador en la nube 7×24 para invocar iLink de Tencent (`ilinkai.weixin.qq.com`) y poner en marcha los scripts de sondeo `getupdates` y envío `sendmessage`.
2. Entregue el Webhook y la clave mediante la ventana emergente, escanee el código y envíe el primer mensaje para obtener el `context_token` inicial.
3. **Punto crítico**: **Las respuestas de WeChat deben convertirse obligatoriamente a texto plano**, eliminando los símbolos de Markdown.

### Canalización de archivo de contenido multimedia de WeChat
El sandbox de WeChat prohíbe la transferencia directa de paquetes completos; **usar un almacenamiento temporal en la nube como intermediario permite eludir esta restricción**.
1. **Carga intermedia**: Exporte el paquete ZIP del chat mediante «Reenvío combinado» en Mac o iPhone, y Atajos lo subirá automáticamente a `filebin.net`.
2. **Archivado automático**: Atajos compone el JSON y lo envía al Webhook de Grok Bot, descomprimiendo y archivando contenidos gráficos y textuales como «13 sitios web de inspiración de diseño».
3. **Criterios de aceptación**: **Debe generar un comprobante estructurado con la ruta y el resumen.**

## Cómo verificar y validar la implementación

### Feishu
1. **Respuesta a mensajes**: Respuestas en menos de 1 segundo en chats privados; silencio ante texto ordinario en chats grupales, respuesta individual a `@文章主编` y reporte sucesivo de cada bot ante `@所有人`.
2. **Permisos y autorrecuperación**: Habilitación completa de los 14 permisos de eventos en el backend y soporte para autorización mediante tarjetas; si se finaliza el proceso manualmente, se reinicia automáticamente en 5 a 10 segundos.

### WeChat
1. **Entorno y establecimiento de comunicación**: WeChat superior a iOS 8.0.70 o Android 8.0.69 con el complemento habilitado; el primer mensaje tras escanear el código responde utilizando `context_token` y sin símbolos corruptos de Markdown.
2. **Interceptación y gestión de errores**: Las cuentas no vinculadas se ignoran de inmediato; reinicio automático tras reiniciar, y **ante el código de error `-14`, indicación de volver a escanear el código**.

### Atajos
1. **Operación de ingesta**: Rellene el Webhook, la clave Bearer y el ID de almacenamiento de al menos 8 caracteres; en WeChat, abra primero los adjuntos para cargarlos antes del reenvío combinado, permitiendo también la activación independiente.
2. **Salida y verificación**: **El comprobante debe incluir el resumen, la ruta de la nota y la ruta de almacenamiento permanente**; verifique el consumo en la página de planes para evitar cobros continuos por ejecuciones vacías.

## Lecturas complementarias

- [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work) (Guía oficial de flujos de trabajo y habilidades de Grok Bot)
- [Guía de uso de rutinas](https://cursor.com/cn/help/grok-bot/routines) (Documentación oficial sobre configuración de rutinas, llamadas Webhook y tareas programadas)
- [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans) (Niveles de suscripción y especificaciones de uso de The X Subscription)
- [Gestión de secretos y claves](https://cursor.com/cn/help/grok-bot/secrets) (Variables de entorno seguras y mecanismo de ventanas emergentes cifradas)
- [«Tutorial paso a paso para la integración de Grok Bot en Feishu en equipos (con plantilla de Administrador de Feishu)»](https://jcng5q8n0f3z.feishu.cn/wiki/F2VXw4hVbirRUjk5QgFcWS0jnJg) (Artículo original del autor de la comunidad 铁柱AGI)
- [«¿Cómo integrar Grok Bot en tu WeChat? Guía paso a paso para principiantes (con prompts detallados) | Kin»](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg) (Artículo original del autor de la comunidad Kin)
- [«Conectar el historial de chat de WeChat con Grok Bot: Edición avanzada de Atajos»](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb) (Artículo original del autor de la comunidad 铁柱AGI)
