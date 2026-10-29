# Capítulo 7 Conectar aplicaciones: plugins, correo electrónico y Secrets

Al integrar herramientas, recuerda: **primero haz que funcionen en la interfaz, luego conecta los conectores**. No pegues claves de terceros en el chat; **guárdalas en el almacenamiento de solo escritura de Secrets** para evitar filtraciones.

- Instalar demasiados plugins saturará el contexto y provocará errores frecuentes; la búsqueda nativa de X se puede invocar sin plugins.
- El correo electrónico dedicado no tiene interfaz de bandeja de entrada ni ventanas emergentes; los envíos masivos automáticos se detendrán en la tarjeta de aprobación.
- En entornos empresariales, presta atención a los errores de Zoom, los bloqueos de Google Workspace y el control de riesgos por IP de centros de datos.


![Conectar aplicaciones: plugins, correo electrónico y Secrets](/info/07-apps.png)

## Orden de integración: primero haz que funcione en la interfaz, luego conecta los conectores

### Pasos de integración
1. Operación en interfaz: **primero haz que las tareas diarias funcionen en el navegador integrado**.
2. Conectores oficiales: una vez estabilizado, conecta los plugins de Connect Apps.
3. Scripts dedicados: para alta frecuencia y gran volumen, recurre finalmente a la API o CLI.

### Errores comunes y limitaciones
- Instalarlo todo consumirá contexto y provocará alucinaciones en las llamadas.
- **Los bots de la misma cuenta comparten la computadora en la nube, el navegador y `/workspace`**; crear un nuevo bot no permite aislar credenciales.

### Criterios de aceptación
**Completar tareas con precisión utilizando el conjunto mínimo de plugins**, sin declaraciones de herramientas redundantes ni activaciones erróneas en el contexto.

[《4.5 Conectores, Skill, plantillas y puntos de entrada externos》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
[《Grok Bot Masterclass｜Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)

## Conexión de plugins: desde la autorización en la tienda hasta el traspaso de permisos empresariales

![Conexión de plugins: desde la autorización en la tienda hasta el traspaso de permisos empresariales](/info/07-apps-s2.png)

Los plugins están vinculados a la cuenta personal y tienen efecto global; **los permisos están limitados por la plataforma de terceros y no se pueden escalar**.

| Plugin | Operaciones admitidas | Limitaciones y precauciones |
|:---|:---|:---|
| **Google Calendar** | Leer y escribir eventos de calendario, consultar disponibilidad y responder a invitaciones | No se puede modificar la sala de espera de Meet; Zoom requiere ingresar el enlace manualmente |
| **Google Drive** | Buscar y leer archivos | Modificar hojas de cálculo requiere Sheets; no se puede modificar la lista de uso compartido |
| **Google Sheets** | Modificar celdas con permisos | No se pueden modificar archivos de solo lectura; la búsqueda la gestiona Drive |
| **Slack** | Enviar mensajes a canales | No puede entrar a canales privados a los que no se haya unido ni a canales silenciados; no es un bot para añadir miembros |
| **Gmail** | Buscar, leer y enviar correos, añadir etiquetas | Limitado a una sola cuenta de correo; no se pueden vincular simultáneamente correos personales y corporativos |

Para más detalles, consulta [Conectar aplicaciones](https://cursor.com/cn/help/grok-bot/connect-apps.md).

1. En la versión de escritorio, haz clic en «Conectar» en la barra lateral o en la tarjeta de chat; en el móvil, toca el avatar y selecciona «Conectar aplicaciones».
2. Busca el plugin, haz clic en «Añadir» (Add) e inicia sesión en el navegador para autorizar.
3. Confirma que aparezca en «Instalados» (Installed); si se interrumpe, haz clic en «Reconectar» para reintentar.

Si encuentras bloqueos con Google empresarial, cambiar de navegador no servirá de nada: **el nombre de autenticación es «Grok»**.

El administrador debe ir en la consola de Google Admin a Security > Access and data control > API controls > App access control > Manage third-party app access, añadir «Grok» (o introducir el Client ID) y marcarlo como Trusted.

Si aparece el aviso «Ha sido deshabilitado por el administrador del equipo», contacta al administrador de Cursor para habilitarlo en el panel de control.

**El éxito se confirma cuando no hay advertencias amarillas en la lista de «Instalados», los datos se pueden leer con normalidad y no se producen fallos de OAuth.**

## Correo electrónico dedicado del bot: reclamo, reglas de envío/recepción y aprobación humana

![Correo electrónico dedicado del bot: reclamo, reglas de envío/recepción y aprobación humana](/info/07-apps-s3.png)

El correo electrónico dedicado de Grok Bot (`yourname@mail.grokbot.com`) **pertenece a la cuenta personal**. Está disponible en chats privados y Routines; no se puede invocar en hilos de Slack ni en sesiones de otras personas, y no existen direcciones compartidas para equipos.

Para consultar las reglas detalladas, consulta el documento [Configurar una dirección de correo electrónico para tu bot](https://cursor.com/cn/help/grok-bot/agent-email.md).

### Limitaciones de uso y seguridad

| Elemento | Reglas y limitaciones |
|---|---|
| Atributos de dirección | Única y con validez permanente, **no se puede renombrar ni eliminar**, y no se libera ni al cancelar la cuenta |
| Cuota de envío | Máximo 50 destinatarios por correo; hasta 10 archivos adjuntos (cada uno ≤10MB, total ≤25MB, prohibidos los `.exe`) |
| Primer contacto externo | Limitado a 1 destinatario y el cuerpo debe incluir obligatoriamente un enlace de cancelación de suscripción; los rebotes o reportes de spam provocarán su desactivación directa |
| Seguridad en la recepción | **Sin bandeja de entrada independiente ni notificaciones**, consultable tras 1 minuto; el contenido es de solo lectura y no ejecuta instrucciones |

### Reclamo y configuración

Los equipos requieren que el administrador active «Agent Email» en el panel de control (`cursor.com/dashboard/bot`), mientras que los usuarios individuales pueden usarlo directamente. La dirección solo admite letras minúsculas, números y `.-_`, debe comenzar y terminar con un carácter alfanumérico, tener un máximo de 64 caracteres y evitar palabras reservadas.

1. Reclamar dirección: ve a la barra lateral en «Connect apps» > «Email» para crearla, o envía `claim your email` y el comando:
```text
  给自己申请一个电子邮件地址
  ```
2. Consultar correos recibidos: busca directamente en la conversación:
```text
今天你的收件箱里收到了什么？帮我找出过去一周收到的所有费用账单与回执。
```
3. Configurar rutinas: crea una Routine para monitorizar remitentes (admite `*@example.com`, no admite filtrado por asunto):
```text
收到来自 billing@example.com 的电子邮件时，总结其中的账单金额与截止日期，并将摘要整理后发送给我。
```
4. Aprobación humana (Human-in-the-loop): **el sistema prohíbe estrictamente los envíos externos silenciosos y desatendidos**. El bot solo genera una tarjeta de borrador, y el correo solo se envía realmente después de que un humano hace clic en «Send».

### Criterios de aceptación

Envía un correo de prueba externo y espera 1 minuto para que el bot lo consulte y redacte un borrador de respuesta. **El éxito se confirma cuando aparece en pantalla una tarjeta pendiente de aprobación y permanece suspendida hasta que se haga clic**.

## Información confidencial de seguridad: mecanismo de solo escritura de Secrets y aislamiento de equipos

![Información confidencial de seguridad: mecanismo de solo escritura de Secrets y aislamiento de equipos](/info/07-apps-s4.png)

**Las credenciales sensibles nunca deben enviarse en el chat, escribirse en la configuración de la shell ni registrarse en «Teach a task».** Que el campo de entrada quede en blanco tras guardar significa que ha entrado en estado de protección.

Ejecutar `Recover` o `Reset` en la computadora en la nube no provocará la pérdida de credenciales; para más detalles, consulta [Almacenar información confidencial de forma segura](https://cursor.com/cn/help/grok-bot/secrets.md).

### Envío y actualización

1. Envío por chat: cuando el bot solicita credenciales, aparece una tarjeta de seguridad con el campo de entrada enmascarado. Haz clic en «Save securely»; cuando aparezca «Saved», el proceso habrá finalizado.
2. Bots de equipo: en la sección «Secrets» de la configuración, haz clic en «Add secret», introduce el nombre (como `GITHUB_TOKEN`), la descripción y la clave secreta, y luego haz clic en «Save secret». **Para actualizar, haz clic en «Replace» y «Replace value»; el sistema no permite recuperar valores anteriores.**
3. Autocompletado web: si aparece la advertencia `Could not fill into the page`, **utiliza Takeover flow para tomar el control manual del inicio de sesión**; nunca envíes el usuario y la contraseña en la ventana de chat.

### Criterios de aceptación

- **El panel solo muestra el nombre y la descripción; el valor del secreto está completamente oculto.**
- Si se solicita en texto plano en la conversación, el bot no puede leerlo, pero la autenticación en CLI o en peticiones se realiza con normalidad.

## Búsqueda nativa en la plataforma X: consulta actividad social sin necesidad de plugins

Grok Bot integró la búsqueda de solo lectura de X en v0.70.2 (2026-10-08). **Utiliza directamente el consumo unificado de The X Subscription, sin necesidad de instalar plugins de terceros ni configurar un API Token**.

1. **Envía instrucciones directas en lenguaje natural**: admite la búsqueda global de publicaciones, la extracción del cuerpo de tweets públicos, la consulta de publicaciones de cuentas y menciones con @, o el análisis estadístico de tendencias de interacción de un tema específico durante 7 días.

```text
检索 X 平台账号 @xai 最近 24 小时发布的所有推文。按时间倒序整理每条推文的核心内容、发布时间、点赞数、转推数，并附带原帖链接。
```

```text
检索 X 平台上关于 #AIagents 话题过去 7 天的热门讨论。筛选互动量最高的前 5 条推文，提取核心观点，并汇总该话题本周的讨论热度变化趋势。
```

2. **Criterios de aceptación**: **los resultados deben incluir la hora de publicación, las métricas de interacción y el enlace original al tweet**, sin avisos de instalación de conectores ni truncamiento en la extracción durante todo el proceso.

Para un desglose de las funciones, consulta [《4.5 Conectores, Skill, plantillas y puntos de entrada externos》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e).

## Instalar Skills de código abierto y herramientas CLI: conectar capacidades locales y de terminal

### Límites de recursos

| Ámbito | Recursos y configuraciones incluidos |
| :--- | :--- |
| **Compartido globalmente** | Todos los bots comparten los Skills instalados, conectores oficiales, memoria compartida y el directorio `/workspace` |
| **Propiedad independiente** | Cada bot mantiene de forma independiente instrucciones de trabajo exclusivas, fragmentos de memoria independientes y rutinas programadas (Routines) |

Para un desglose de la arquitectura, consulta [《4.5 Conectores, Skill, plantillas y puntos de entrada externos》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e) y [《Grok Bot Masterclass｜Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned).

### Pasos operativos clave

1. Activa el retransmisor de tráfico de red local. La computadora en la nube utiliza una IP de centro de datos, lo que facilita el bloqueo al acceder a sitios externos como GitHub.

   En la versión de escritorio, ve a Settings -> Computer y marca «Enrutar tráfico a través de este equipo» (Route traffic through this computer) para retransmitir a través de la red local; tanto el cliente como la nube deben actualizarse simultáneamente.
2. Instala Skills de código abierto. Envía directamente la dirección del repositorio en el chat para que el bot lo despliegue. Si se requiere un Access Token, espera a que el sistema lo solicite y envíalo mediante la tarjeta de seguridad; **está estrictamente prohibido pegar el Token directamente en el chat**.

```text
帮我安装这个开源 Skill：https://github.com/example/custom-data-skill
阅读仓库内的说明文档，将其注册为我的可用技能，并告诉我它支持的触发指令与所需参数。
```

3. Inicia sesión de forma independiente en Codex CLI. Primero, en la interfaz web, ve a «Seguridad de la cuenta e inicio de sesión» y activa «Inicio de sesión con código de dispositivo» (Device code login). Ejecuta el comando de inicio de sesión en la terminal en la nube, obtén el código de verificación del dispositivo y verifícalo con el navegador local.

   **Nunca copies las credenciales de inicio de sesión locales al `/workspace` de la computadora en la nube**; de lo contrario, la caché compartida provocará conflictos de renovación de tokens y desconexiones frecuentes en ambos extremos.
4. Delega tareas pesadas al agente CLI. Para tareas mecánicas como el formateo masivo de código o la transcodificación, escribe scripts de Shell directamente y asígnalos a la CLI de la computadora en la nube para su ejecución. Utiliza el mecanismo «Wake on Done» para recibir notificaciones de finalización y evitar que el bot ocupe sesiones de inferencia de alto coste durante periodos prolongados.

### Qué define un buen resultado

- Ejecutar `codex --version` en la terminal de la computadora en la nube devuelve la información de la versión con normalidad, **y el uso diario de la terminal local no se verá interrumpido por cierres de sesión forzados**.
- Al enviar una tarea de prueba al bot, este puede generar archivos estructurados que cumplan con los estándares de entrega en el directorio `/workspace` siguiendo el flujo establecido.

## Errores y trampas frecuentes

### Plugins y permisos corporativos
- El error 4700 en la autorización de Zoom se debe a un fallo de redirección oficial y no se puede corregir dentro del cliente.
- Gmail solo admite la vinculación de una cuenta; para cambiarla, debes desconectar primero la cuenta actual y luego volver a autorizarla.
- En la aprobación de permisos de Google, **debes buscar obligatoriamente «Grok», no «Cursor»**; cambiar de navegador no servirá de nada.

### Correo dedicado y aprobación de envíos externos
- `mail.grokbot.com` no tiene interfaz ni notificaciones push; para consultar correos debes preguntar al bot o crear una rutina; las rutinas solo monitorizan por remitente y dominio (deben superar SPF/DKIM), y no admiten filtrado por asunto.
- En el nivel inferior existe una barrera de control humano obligatoria que los prompts no pueden eludir; para enviar correos debes **hacer clic manualmente en «Send»** en el borrador.

### Seguridad y entorno de red
- La grabación de pantalla de Teach a task dura hasta 10 minutos y no cuenta con enmascaramiento de Secrets; no introduzcas contraseñas ni muestres API Keys.
- Todos los bots comparten el almacenamiento y el estado de sesión; **no dejes archivos confidenciales en `/workspace`**.
- Copiar tokens locales provocará desconexiones mutuas; la terminal debe autorizarse de forma independiente mediante código de dispositivo.
- Si sitios externos bloquean la IP del centro de datos y devuelven errores, ve a la página Computer y **activa «Enrutar tráfico a través de este equipo»**.

## Cómo verificar una vez completado

1. Confirma en la barra lateral que Drive y Sheets funcionan correctamente. Pide al bot que busque Q3_Report y use Sheets para leer las celdas A1 a B10 de la tabla; **debe poder leerlas sin errores de permisos**.
2. Envía un correo con un código numérico desde tu cuenta personal a `yourname@mail.grokbot.com`, espera 2 minutos a que el bot lo revise, pídele que redacte una respuesta y **verifica el código antes de hacer clic en Send en la tarjeta de borrador**.
3. Pide al bot que imprima `GITHUB_TOKEN`: **debe rechazar mostrarlo en texto plano o mostrar solo la máscara**; luego ejecuta un comando de prueba para comprobar que supera la autenticación, confirmando que el Token no se ha filtrado.
4. Busca los dos tweets con más «me gusta» de `@xai` de las últimas 24 horas; **los enlaces originales deben ser cliqueables y no deben invocarse plugins de terceros**.
5. Ejecuta `codex --version` en la terminal para verificar que muestre la versión; la concurrencia local **no debe causar conflictos ni desconexiones**; al activar «Enrutar tráfico a través de este equipo», se deben poder abrir páginas sensibles a IPs de centros de datos.

## Lecturas adicionales

### Documentación oficial y páginas de soporte

- [Conectar aplicaciones](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- [Configurar una dirección de correo electrónico para tu bot](https://cursor.com/cn/help/grok-bot/agent-email.md)
- [Almacenar información confidencial de forma segura](https://cursor.com/cn/help/grok-bot/secrets.md)
- [Computadora de Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery.md)
- [Rutinas](https://cursor.com/cn/help/grok-bot/routines.md)
- [Bots de equipo](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- [Grok Bot para Teams y Enterprise](https://cursor.com/cn/docs/grok-bot/teams.md)

### Materiales prácticos de la comunidad

- 《4.5 Conectores, Skill, plantillas y puntos de entrada externos》: [Documento de la base de conocimiento de Feishu](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
- 《Grok Bot Masterclass｜Avi Chawla》: [Documento de la base de conocimiento de Feishu](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)
