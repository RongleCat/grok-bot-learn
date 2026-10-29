# Capítulo 20 Automatización confiable: programación, Webhooks y disparadores de eventos

Una Routine se despierta docenas de veces al día solo para responder "sin cambios hoy", y la cuota se deduce de todos modos. **La falta de especificaciones en las tareas conduce fácilmente a errores silenciosos**.
- Desviación de zona horaria (se ejecuta a las 3 a. m. en lugar de las 9 a. m.)
- Juicio erróneo de periodicidad (el valor predeterminado de días laborables hace que los fines de semana se omitan)
- Falta de contingencia (los errores modifican el entorno de producción a ciegas debido a datos vacíos)

**Una arquitectura en dos fases combinada con cron de Linux puede reducir más del 80% de las ejecuciones en vacío**. Solo definiendo contratos de límites y barreras humanas de seguridad, e integrando Atajos y flujos de eventos de X, la automatización será estable y económica.


![Automatización confiable: programación, Webhooks y disparadores de eventos](/info/20-automation.png)

## Selección de disparadores: entrega puntual vs. espera de cambios

![Selección de disparadores: entrega puntual vs. espera de cambios](/info/20-automation-s1.png)

Primero distingue si se trata de entregar resultados a una hora fija o de esperar datos nuevos. **El Bot comparte el fondo de cuota semanal con Grok y Cursor**, y un sondeo de alta frecuencia lo agotará en pocos días.

### Suscripciones y límites de cuota

En The X Subscription (12-10-2026), Plus no incluye Bot; los planes compatibles son Premium ($30/mes o $300/año, 4x), Super ($100/mes o $1000/año, 15x) y Ultra ($200/mes o $2000/año, 50x).

Un solo Bot está limitado a 50 Routines, con un historial de 20 ejecuciones, y el **intervalo mínimo de programación es de 5 minutos**.

### Métodos de disparo y selección

- Routines programadas: se facturan al llegar la hora independientemente de si hay datos o no; adecuadas para informes diarios fijos.
- Webhook: consumo cero en reposo, **exclusivamente para solicitudes POST con token Bearer**.
- Eventos de terceros (GitHub, Slack, etc.): solo se activan cuando hay eventos; los canales muy activos pueden agotar la cuota con facilidad.
- Interacción en X (responder a @bot): no puede procesar publicaciones con video; mencionar a @grok y a @bot simultáneamente no activa el disparador.

**Si solo se debe procesar al llegar nuevos datos, utiliza siempre Webhooks o eventos de terceros.**

## Plantilla de diseño de Routines: redacta contratos, no títulos

Si el prompt solo contiene títulos de puestos o roles, fallará fácilmente; **las Routines en producción deben especificar un contrato de ejecución claro**.

Fuente: [«4.3 Disparadores y automatización: programación, Webhooks y asignación de tareas en X»](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg); se deben preparar cuatro elementos esenciales que abarquen fuentes de datos, formatos de salida, así como políticas de manejo de errores por datos faltantes y aprobación humana.

### Redacción de contratos y configuración de Routines

1. **Envía el contrato que restringe las entradas y salidas al Bot y haz que lo memorice**; para un Bot compartido, escríbelo en la Description de la sección About en los detalles.
```text
负责范围：监控指定数据源并生成标准化 Markdown 摘要。
允许读取的数据源：工作区目录下的 data/incoming/ 文件夹及指定公开 RSS 链接。
输出格式规范：必须输出包含“标题、核心要点（最多3条）、影响评估、原始链接”的 Markdown 结构，存入 docs/daily/ 目录。
数据异常策略：若数据源无更新或文件为空，仅在工作区追加一行日志“[时间戳] NO_NEW_DATA”，严禁编造或推测新闻内容，严禁在聊天窗口发送刷屏提示。
权限边界：只读外部内容与本地写入。禁止调用外部发帖、转账、发送邮件或删除文件操作。
```
2. En el chat, guarda el flujo de trabajo como una Skill con lógica de autocomprobación y envía directamente el comando para crear una Routine programada.
```text
每个工作日上午 8:30，运行“晨间资讯归档”Skill。如果数据源没有更新，记录日志后保持沉默。
```
3. En la lista de "Routines" dentro de Details, utiliza el interruptor para alternar entre Pause o Resume.

   Haz clic para entrar al panel y modificar Instruction, When to run y Webhook; la parte inferior admite Pause/Resume, Test, Edit y Delete routine (icono de papelera).

### Prueba en seco (dry run) antes del lanzamiento

Las Routines ejecutan operaciones reales en una máquina virtual en la nube; **por defecto, todos los Bots comparten el entorno de ejecución subyacente sin aislamiento de sandbox**, por lo que perder el control modificará archivos reales. Antes de activarla, envía un comando en el chat para realizar una validación de prueba en seco.
```text
针对即将上线的例程“晨间资讯归档”，进行一次干跑验证：
1. 复述你理解的执行触发条件与完整业务流程。
2. 列出本次执行涉及读写操作的路径，以及可能产生风险的 3 个最高风险步骤。
3. 说明如果源文件损坏或格式错误，你的具体兜底动作。
现在不要执行任何实际写文件和网络请求操作，仅输出分析报告。
```

### Bloqueo estricto con barreras humanas de seguridad

Ve a Custom Rules (o Auto-review) en Settings y **establece obligatoriamente la aprobación manual para acciones irreversibles**.

| Comando interceptado | Alcance de la acción |
|---|---|
| `send` / `post` | Envío externo de mensajes, correos o redes sociales |
| `buy` / `transfer` | Interfaces de pago y transferencias |
| `delete` / `permissions` | Eliminación de archivos/bases de datos, cambios de permisos |

Tras activarse el comando, el sistema mostrará una tarjeta de aprobación que pausará la ejecución y esperará la confirmación humana continua, sin realizar envíos externos automáticos bajo ninguna circunstancia.

## Integración de Webhooks: conexión entre dispositivos móviles y pipelines externos

Fuente: [«Grok Bot Webhook + Atajos: construcción de un pipeline de almacenamiento automático de conocimiento»](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)

### Credenciales y estados

En la Routine, selecciona "Cuando se activa el Webhook" (When webhook is triggered); **debes hacer clic en Save para generar la dirección, la clave y el Header**. En v0.68.1, si la tarjeta no muestra la URL completa, **pide al Bot que envíe el enlace en el chat** para copiarlo; nunca compartas la clave en grupos públicos.

**Una respuesta 200 solo indica que la nube ha iniciado la tarea, no que la ejecución haya finalizado**. Consulta los resultados en la ventana de chat; si el código no es 200, verifica si la Routine está en Paused y revisa la clave.

### Atajos

Con panel para compartir (navegadores, etc.):
1. Marca "Mostrar en hoja para compartir" para recibir enlaces y texto.
2. Utiliza "Obtener contenido de URL" para enviar una solicitud POST, completando la cabecera con `Authorization: Bearer <key>`, y añade `content` al cuerpo JSON con la entrada del Atajo.

```text
接收端 Bot 的配套 Instruction 模板：
收到 Webhook 传入的 JSON 数据后，提取 content 字段中的链接。
如果是普通网页，抓取正文，提炼核心结论与知识点。
整理完成后，以 Markdown 格式追加写入知识库目录下的 inbox.md，包含收录时间、原文链接、核心观点与分类标签。
处理完毕后在聊天中输出一句话确认回执。
```

Sin panel para compartir (WeChat, etc.):
1. Utiliza "Solicitar texto" seguido de "Ejecutar atajo" para reenviar.
2. Vincúlalo al botón de acción del iPhone 15 Pro o a la pantalla de inicio para enviarlo mediante una ventana emergente tras copiar.

**Los archivos grandes no se pueden incluir directamente en el cuerpo de la solicitud**. Sube audios, videos e imágenes a un almacenamiento en la nube para obtener una URL pública antes de enviarlos al Bot.

## Determinación incremental para evitar ejecuciones en vacío: arquitectura de verificación en dos fases

![Determinación incremental para evitar ejecuciones en vacío: arquitectura de verificación en dos fases](/info/20-automation-s4.png)

Ejecutar un modelo de lenguaje grande en cada ronda de inspección consume demasiada cuota; **divídelo directamente en dos fases**.

1. Utiliza el cron nativo de Linux para realizar inspecciones mecánicas.
2. Llama al Webhook para despertar al Bot y procesar **solo cuando los datos cambien**.

Fuente: [«Ahorra aún más cuota en Grok Bot: optimización extrema de tareas programadas»](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).

### 1. Principio de desacoplamiento: división del trabajo entre el reloj despertador y el cerebro

Detrás de Grok Bot hay una computadora en la nube con Linux siempre encendida.

1. **Comprobación mecánica**: ejecuta un script con cron para comparar datos. Durante este proceso, **nunca invoques ningún modelo de lenguaje grande**; finaliza en unos segundos sin consumir cuota.
2. **Activación incremental**: si hay cambios, envía un POST al Webhook local para despertar al Bot y realizar el análisis y resumen.

Modificar los 6 Routines de tipo espera tomó unos 23 minutos, reduciendo de 8 a 10 ejecuciones en vacío por semana y bajando la latencia de un día a menos de media hora.

### 2. Pasos de configuración para la implementación en la máquina virtual

1. Agrega una Routine llamada "Centro de procesamiento incremental" en el Bot, selecciona Webhook como disparador y **guarda bien la URL del Webhook y la clave Bearer**.
2. Abre la terminal y crea el script `check_update.sh` en el espacio de trabajo:

::: details 2. Pasos de configuración para la implementación en la máquina virtual
```bash
   #!/bin/bash
   # 监测目标 API 或页面是否有增量变化，纯机械对比，严禁调用 LLM

   TARGET_URL="https://api.example.com/v1/feed"
   STATE_FILE="/home/user/workspace/last_state.hash"
   WEBHOOK_URL="https://your-bot-webhook-url.com/api/v1/run"
   WEBHOOK_KEY="Bearer YOUR_SECRET_KEY"

   # 获取最新数据的哈希值或时间戳
   CURRENT_HASH=$(curl -s "$TARGET_URL" | md5sum | awk '{print $1}')

   if [ ! -f "$STATE_FILE" ]; then
       echo "$CURRENT_HASH" > "$STATE_FILE"
       exit 0
   fi

   OLD_HASH=$(cat "$STATE_FILE")

   # 比对是否有变化
   if [ "$CURRENT_HASH" != "$OLD_HASH" ]; then
       echo "检测到数据更新，正在唤醒 Bot..."
       echo "$CURRENT_HASH" > "$STATE_FILE"
       
       # 叫醒 Bot 进行智能分析
       curl -X POST "$WEBHOOK_URL" \
            -H "Authorization: $WEBHOOK_KEY" \
            -H "Content-Type: application/json" \
            -d '{"event": "data_changed", "source": "feed_monitor"}'
   else
       # 无变化，保持沉默，零额度消耗
       echo "无新变化，退出。"
   fi
   ```
:::

3. Instala e inicia el servicio cron en la terminal:

```bash
   sudo apt-get update && sudo apt-get install -y cron
   sudo service cron start
   ```

Ejecuta `crontab -e` para configurar la programación (días laborables de 9:00 a 19:00, verificando cada 30 minutos):

```cron
   */30 9-19 * * 1-5 /bin/bash /home/user/workspace/check_update.sh >> /home/user/workspace/cron_check.log 2>&1
   ```

- **Hacer clic en "Actualizar computadora" en el cliente restablecerá el sistema**: aunque los scripts del espacio de trabajo se conserven, el cron instalado mediante `apt-get` se borrará; tras una actualización, deberás reinstalarlo e iniciarlo nuevamente.
- **No invoques la API de modelos grandes en el script**: realiza solo comprobaciones ligeras; delegar la evaluación al modelo no ahorra costes, ya que todo el gasto se transferirá a la facturación de la API.

## Eventos de terceros e integración con la plataforma X

### Disparador de Slack

El disparador de Slack pertenece al sistema de Routines; antes de usarlo debes vincular Slack a tu cuenta, consulta [«Ayuda de Routines»](https://cursor.com/cn/help/grok-bot/routines).

- **Nunca configures el disparador "al recibir cualquier mensaje" en canales públicos**; las conversaciones casuales de un solo día consumirán la cuota de toda la semana.
- Escucha únicamente canales de notificación exclusivos como `#alerts-p0` o `#deploy-status`.
- Debe incluir un prefijo de activación, como `!bot review` o `@bot summary`.
- Solo responde a nuevos mensajes generados después de su creación, sin consultar el historial.

### Límites de la integración con la plataforma X

A partir de v0.70.2, no es necesario vincular una cuenta personal para buscar publicaciones.

Comentar @bot debajo de una publicación notificará al Bot principal marcado con estrella para distribuir la tarea; consulta [«4.3 Disparadores y automatización: programación, Webhooks y asignación de tareas en X»](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

- Limitaciones: no puede procesar publicaciones con video; los comentarios que contengan tanto `@grok` como `@bot` entrarán en conflicto y no activarán el disparador.
- Prevención de inyecciones: **el Bot principal solo tiene permitido resumir, clasificar y archivar; está estrictamente prohibido publicar, dar 'me gusta' o alterar la computadora en la nube automáticamente**, y cualquier acción orientada al exterior debe remitirse al cliente de escritorio para su confirmación manual.

## Planes de contingencia ante fallos y estrategias de tolerancia a errores

![Planes de contingencia ante fallos y estrategias de tolerancia a errores](/info/20-automation-s6.png)

Los tiempos de espera agotados en interfaces o las respuestas con datos vacíos provocan fácilmente alucinaciones; **la Instruction debe incluir una declaración de interrupción por anomalías**:

```text
前置校验步骤：
1. 检查抓取到的内容体积。如果内容为空、包含 HTTP 错误码（如 403、404、500）或少于 50 个字符，判定为源不可用。
2. 源不可用时，立刻终止后续分析流程。
3. 在 workspace/logs/routine_errors.log 中追加一行错误记录，格式：[ISO时间戳] [任务名] SOURCE_UNAVAILABLE [原因]。
4. 不得在公开聊天窗口发送报警消息，不得使用过往缓存伪造新数据，直接以退出状态结束本次 run。
```

Resolución de problemas de anomalías en Webhooks:
1. **401**: Revisa `Authorization: Bearer <key>` en el Header para evitar espacios o saltos de línea adicionales, o el uso de una clave antigua.
2. **404**: Verifica la integridad de la URL para evitar que se haya eliminado o cancelado por error en el cliente de escritorio.
3. **429**: Límite de concurrencia superado; **se debe agregar una cola de reintentos y retroceso exponencial**.
4. **No ejecutado**: Comprueba si está en **Paused** o si el interruptor **Active** en el móvil está desactivado.

**Persistencia de registros en disco para evitar saturar la pantalla**: solo las intercepciones de aprobación generan notificaciones en tarjetas; los resúmenes se escriben en `docs/reports/YYYY-MM-DD.md` y los registros de una sola línea se anexan a `workspace/run.log`.

## Monitorización y mantenimiento diario

Revisa las Routines en **Details** en el cliente de escritorio o en el archivo de configuración en el móvil; puedes hacer clic en **Failed** para ver la traza del error.

Revisa **Usage & Billing** semanalmente (v0.70.2 corrigió la visualización del consumo); un aumento repentino en el gasto indica que hay Routines ejecutándose en vacío o reintentando constantemente.

Dedica 15 minutos fijos cada viernes para depurar Routines:
1. Abre `workspace/run.log` para revisar la producción real.
2. Pon en **Pause** las Routines que lleven 7 días consecutivos sin actividad incremental.
3. Tras dos semanas detenidas y sin dependencias, procede con **Delete routine**; **la eliminación es irreversible y el Webhook quedará invalidado de inmediato**.

## Errores comunes

- **Mecanismo de días laborables**: Configurar "todos los días a las 8:00" a menudo se interpreta como solo días laborables. Para tareas ininterrumpidas, **el prompt debe indicar explícitamente "incluyendo sábados y domingos"**.
- **Desviación de zona horaria**: Al crear una Routine, ve primero a Settings -> Bot -> Timezone para consultar la zona horaria. El valor predeterminado en la nube es UTC, por lo que configurar las 9:00 podría hacer que se ejecute en plena noche.
- **Fallo al crear Bot con el botón (+)**: Crear uno nuevo desde la barra lateral (+) suele bloquearse; si no funciona, **haz que un Bot ya configurado derive un nuevo Bot a través de una conversación**.
- **Credenciales no guardadas**: Al configurar un Webhook, **es obligatorio hacer clic en Save en la parte inferior para emitirlo**; salir de la página directamente provocará que la clave no se genere.
- **Reinicio por actualización del sistema**: "Actualizar computadora" (Update computer) restablece la imagen del sistema, por lo que el cron instalado con `apt-get` se perderá; **revisa cron en la terminal después de actualizar**.
- **Filtración de claves**: No pegues las claves del Webhook en chats convencionales. Si las envías por error, **elimina el mensaje de inmediato y restablece la clave en la Routine**.
- **Ejecución real con Test**: Hacer clic en **Test** consumirá cuota y modificará archivos; **está estrictamente prohibido probar sobre datos de producción**.

## Cómo verificar y validar tras finalizar

1. En el cliente de escritorio, revisa la programación en inglés dentro de When to run (por ejemplo, "Every day at 8:00 AM CST") y asegúrate de que coincida con tu zona horaria local y los fines de semana.
2. Las Routines nuevas esperan al siguiente ciclo para ejecutarse; comprueba si la hora de Next run es precisa.
3. Renombra la fuente de datos o déjala vacía, haz clic en Test para ejecutarla una vez y confirma que se registre un log de "anomalía en la fuente de datos", deteniéndose de forma limpia sin inventar información.
4. Inyecta comandos para enviar correos, publicar posts o eliminar directorios, y **confirma que la operación sea interceptada y muestre una tarjeta de confirmación**, sin enviar paquetes al exterior directamente.
5. Usa curl en la terminal para enviar una solicitud POST al Webhook:
```bash
   curl -i -X POST "你的_WEBHOOK_URL" \
        -H "Authorization: Bearer 你的_KEY" \
        -H "Content-Type: application/json" \
        -d '{"test": "ping"}'
   ```
Verifica que **recibas el código de estado 200 en 1 segundo**, y que en menos de 30 segundos el estado del Bot en el cliente cambie a Running y emita un acuse de recibo y resultados estructurados.

## Lecturas complementarias

- Capítulos relacionados: [Capítulo 8 Skills y Routines: convierte un éxito puntual en una ejecución automática diaria](/part1/08-skills-routines)
- Capítulos relacionados: [Capítulo 10 Cuota y costes: cómo hacer que el uso semanal rinda toda la semana](/part1/10-usage)
- Documentación oficial: [«Cursor Help: Routines»](https://cursor.com/cn/help/grok-bot/routines)
- Artículo original de la comunidad: [«4.3 Disparadores y automatización: programación, Webhooks y asignación de tareas en X»](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- Artículo original de la comunidad: [«Grok Bot Webhook + Atajos: construcción de un pipeline de almacenamiento automático de conocimiento»](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- Artículo original de la comunidad: [«Ahorra aún más cuota en Grok Bot: optimización extrema de tareas programadas»](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
