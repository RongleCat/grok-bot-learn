# Capítulo 10 Cuota y costes: cómo hacer que el uso semanal dure toda la semana

Quedarse sin cuota un martes y recibir cargos de cientos de dólares suele deberse a ciclos de computación en vacío. **Cada vez que el Bot se reactiva, relee el historial completo**, inflando el contexto a cientos de miles de tokens en pocas horas.

Para aguantar toda la semana sin problemas, sigue estos tres pasos:
1. Desactiva el pago bajo demanda en segundo plano.
2. Reduce los sondeos frecuentes y las conversaciones entre múltiples Bots.
3. Ajusta las sesiones y evita enviar archivos grandes en la ventana de chat.


![Cuota y costes: cómo hacer que el uso semanal dure toda la semana](/info/10-usage.png)

## ¿Cómo funciona el cobro de la cuota en Grok Bot? {#扣费原理-额度是怎么被花掉的}

**Grok Bot factura por tokens consumidos en cada llamada. Su mecanismo central se basa en sesiones largas individuales: cada respuesta o reactivación vuelve a leer el contexto histórico completo, y el consumo total equivale al número de reactivaciones multiplicado por la longitud del contexto releído en cada ocasión.**

![Principio de cobro: cómo se consume la cuota](/info/10-usage-s1.png)

Grok Bot factura según los tokens que el modelo realmente consume. **Su mecanismo principal es la conversación larga única: cada respuesta o reactivación programada vuelve a leer todo el historial desde el principio.**

```
每周总消耗 = Bot 唤醒的总次数 × 每次唤醒时重读的上下文长度
```

Cuando una conversación acumula gran cantidad de registros o páginas web, una sola relectura puede alcanzar cientos de miles de tokens; responder una sola frase implicará procesarlo todo por completo.

Para ver un desglose de la comunidad, consulta [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).

A partir del 12 de octubre de 2026, se implementa el plan de suscripción unificado The X Subscription. Los estándares para cada nivel son los siguientes:

| Nivel del plan | Precio suscripción individual | Precio por plaza de equipo | Multiplicador de cuota y permisos de Grok Bot |
| :--- | :--- | :--- | :--- |
| **Free** | $0 | No aplicable | Limited, sin Bot completo |
| **Plus** | $8/mes ($80/año) | No aplicable | Base, **explícitamente sin Grok Bot** |
| **Premium** | $30/mes ($300/año) | $30/plaza/mes | 4x, incluye Grok Bot |
| **Super** | $100/mes ($1000/año) | $100/plaza/mes | 15x, incluye Grok Bot |
| **Ultra** | $200/mes ($2000/año) | $200/plaza/mes | 50x, incluye Grok Bot |

Para más detalles sobre las reglas de cuota, consulta la [Guía oficial de Cursor: Planes y facturación](https://cursor.com/cn/help/grok-bot/plans). Existen varias limitaciones estrictas en el uso diario:

- **Los fondos de cuota no se acumulan**: con múltiples suscripciones solo se toma la cuota semanal más alta, no se suman ni combinan.
- **Alcance del fondo compartido**: la cuota semanal cubre Grok Bot y Grok dentro de Cursor, además de la versión web, móvil, Imagine y Voice, y se restablece periódicamente en una fecha fija.
- **Los modelos de terceros se facturan por separado**: invocar modelos que no sean Grok dentro de Cursor se factura directamente según el consumo.
- **Pago bajo demanda y límite mensual**: tras agotar la cuota semanal, activar On-demand se cargará al límite mensual (Monthly Limit); una vez superado el límite, las tareas en curso terminarán de ejecutarse; si se desactiva, dejará de responder a la espera del restablecimiento.

**Oficialmente se especifica que no hay selector de modelos (there is no model picker), por lo que no es posible cambiar a un modelo inferior.** Para controlar los costes solo queda reducir la frecuencia de reactivación, recortar la longitud del contexto o desviar los cálculos de alto consumo hacia el exterior.

## ¿Cuáles son las trampas habituales de alto consumo de cuota en Grok Bot? {#高耗操作清单-坚决避开的六大陷阱}

**Es imprescindible evitar los chats grupales con múltiples Bots, enviar imágenes y vídeos en la conversación, los sondeos de alta frecuencia durante todo el día, mantener una conversación larga de principio a fin, los bucles infinitos de reintentos sin protección y activar a ciegas el pago bajo demanda sin fijar un límite mensual.**

![Lista de operaciones de alto consumo: seis trampas que debes evitar a toda costa](/info/10-usage-s2.png)

Referencias: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf).

| Operación de alto consumo | Razón del gasto excesivo | Cómo evitar la trampa |
| :--- | :--- | :--- |
| Chats grupales con múltiples Bots | La reactivación mutua duplica los tokens en vacío | Un único Bot principal con Subagents asignados, o chats individuales humanos |
| Enviar imágenes y vídeos directamente en la conversación | Los fotogramas permanecen en el historial, pagando una relectura completa en cada turno | Procesar en la línea de comandos del terminal; el Bot solo recibe texto estructurado de menos de 100 palabras |
| Sondeos de alta frecuencia todo el día | Cada 15 minutos supone 672 veces por semana, la mayoría para confirmar que no hay cambios | Limitar al horario laboral o cambiar a scripts del sistema con Webhooks |
| Usar una sola conversación de principio a fin | Tras decenas de turnos, cada relectura consume cientos de miles de tokens | Una sola tarea por conversación; resumir periódicamente y reiniciar con Duplicate |
| Bucle infinito de reintentos sin protección | Decenas de auto-reintentos continuos tras un error | **Limitar obligatoriamente a un máximo de 2 reintentos en el prompt**; si falla, bloquear de inmediato y consultar a un humano |
| Activar a ciegas el pago por uso | Un bucle infinito puede generar facturas astronómicas de la noche a la mañana | **Mantener desactivado el pago bajo demanda habitualmente**; si se activa, establecer un límite mensual bajo y estricto |

## Flujo de trabajo en cuatro pasos para ahorrar cuota: del control de pérdidas a la derivación

![Flujo de trabajo en cuatro pasos para ahorrar cuota: del control de pérdidas a la derivación](/info/10-usage-s3.png)

### Asegurar la facturación y la línea de seguridad
1. Ve a Settings > Usage & Billing para comprobar tu plan (Premium $30/mes o Super $100/mes), el consumo y la cuenta atrás; si se queda bloqueado, haz clic en Stop para forzar la finalización.
2. **Desactiva Additional Usage / On-demand durante la depuración**; si lo activas, ve a cursor.com/dashboard > Gastos > Monthly Limit y fija un límite mensual ($10-$20).
3. Ve a Settings > General > Auto-review y **configura send, post, buy, transfer, delete y permissions en Ask first para aprobación manual**.

### Estandarizar sesiones e interacciones
- **Una sola tarea por sesión**; archívala inmediatamente al terminar.
- Guarda registros y textos largos en `/workspace/`, respondiendo únicamente con conclusiones y rutas; queda terminantemente prohibido pegarlos de vuelta en el chat.
- Las búsquedas en X están limitadas a 30 por minuto y 1000 al día (no descuentan de la cuota semanal); **indica al Bot que «extraiga los hechos clave y los presente en 3 a 5 puntos principales»**.
- Cuando una sesión se vuelva demasiado pesada, usa Duplicate para reiniciarla: primero haz que el Bot antiguo redacte un resumen de menos de 10 líneas, cópialo y envíaselo al nuevo Bot para que tome el relevo, y oculta el Bot antiguo.

### Enrutamiento de capacidades y derivación
- El Bot principal solo se encarga de desglosar, asignar y resumir tareas; no debe escribir código extenso ni convertir archivos grandes.
- **Para escribir código, utiliza el Agent en la nube de Cursor** (consume la cuota de Cursor y no descuenta de la cuota semanal), o ejecuta de forma headless Grok Build CLI / Codex CLI en una máquina virtual.
- Procesa capturas de pantalla, audio y vídeo desde la línea de comandos del ordenador en la nube, o utiliza modelos gratuitos para transcribirlos a texto antes de pasárselos al Bot.

### Reestructuración de tareas programadas
1. En Details > Routines, **pausa o elimina aquellas rutinas que hayan estado notificando «sin cambios» a diario durante la última semana**.
2. Cámbialas por scripts de Linux para sondeos de bajo coste y envía un Webhook para reactivar al Bot solo cuando haya cambios.
3. **Añade una instrucción de silencio a las rutinas conservadas**: «Tras la comprobación, si no hay cambios, finaliza la tarea inmediatamente y abstente estrictamente de generar cualquier texto».

Referencia: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## Optimización profunda de rutinas y sondeos: adiós a las ejecuciones en vacío

Las rutinas son un agujero negro de cuota oculto: un sondeo de alta frecuencia **puede consumir la cuota de toda una semana en un solo día**.

### Reducción de frecuencia y control de ventanas de ejecución

Comprueba primero en el cliente si la Timezone del Bot coincide con la local. El consumo según las distintas configuraciones de programación es el siguiente:

| Configuración de programación | Ejecuciones semanales | Escenarios de aplicación |
| :--- | :--- | :--- |
| Cada 15 minutos (24/7) | 672 veces | Muy propenso a agotar la cuota en 1 o 2 días; rara vez necesario |
| Cada hora (24/7) | 168 veces | Monitorización de fallos en infraestructuras críticas |
| Cada hora de 9:00 a 17:00 en días laborables | 45 veces | Seguimiento de paneles Kanban, gestión de incidencias y triaje de correo |
| 3 veces por día laborable | 15 veces | Filtrado de bandeja de entrada por la mañana, mediodía y tarde; seguimiento del progreso |
| 1 vez por semana | 1 vez | Informes semanales del sector, resúmenes tecnológicos y archivado de documentación |

Para restringir al horario laboral, puedes usar el formato estándar de cron:

```text
CRON_TZ=Asia/Shanghai 0 9-17 * * 1-5
```

**Esta regla reduce las reactivaciones en un 93%**. Al ejecutarse a las horas en punto de 9:00 a 17:00 en días laborables en la zona horaria de Shanghái, solo se activa 45 veces por semana.

### Apuntar a habilidades y aplicar estrictamente la regla de silencio

Los prompts de las rutinas deben apuntar únicamente a las habilidades, sin entrar en detalles:
- Usa comandos de barra para especificar el nombre concreto de la habilidad y el objeto de inspección
- Define umbrales de decisión, condiciones de parada y límites de reintento único
- **Mantén un silencio absoluto cuando no haya cambios, sin enviar ningún mensaje**

El silencio total puede ocultar fallos imprevistos. Para una estrategia combinada, consulta la [Guía oficial de Cursor: Rutinas](https://cursor.com/cn/help/grok-bot/routines): mantén silencio en las rutinas de alta frecuencia y, en las de baja frecuencia, envía un registro de latido de una sola línea a las 18:00 todos los días para confirmar que la ejecución del día transcurrió con normalidad.

### Separación de doble rol: inspección con scripts cron de Linux y reactivación mediante Webhook

Mientras el Bot está suspendido, el ordenador en la nube Linux subyacente sigue funcionando: **no utilices grandes modelos para hacer comparaciones mecánicas**.
- Rol de comprobación: el cron del propio sistema programa scripts de Python o Shell para comparar datos; tarda pocos segundos y consume cero cuota.
- Rol de decisión: solo cuando el script detecta un cambio envía un Webhook para reactivar al Bot, permitiéndole realizar el análisis lógico y generar el informe.

Pasos de reactivación por Webhook y criterios de aceptación:
1. Obtén la dirección `POST to` y la `key` en la sección de Webhook de la rutina.
2. Envía una petición POST a dicha URL incluyendo el encabezado `Authorization: Bearer <key>`.
3. Comprueba el código de estado de la respuesta: un código 200 indica que la reactivación se realizó con éxito.

### Casos prácticos y trampas a evitar

- **Reestructuración de 6 rutinas del Bot Director de Marketing por 铁柱**: se mantuvieron sin cambios 4 rutinas orientadas a entregas; 2 tareas en vacío que solo esperaban respuestas y revisiones de PR se sustituyeron por scripts cron del sistema con Webhook. El script realiza comprobaciones cada media hora durante el horario laboral diurno y reactiva al Bot solo si hay cambios.

  **La reestructuración tomó unos 23 minutos y redujo de 8 a 10 reactivaciones innecesarias a la semana**, logrando detectar novedades en menos de media hora.

  Origen del caso: [《Ahorrar un poco más de cuota en Grok Bot: optimización extrema de tareas programadas》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).
- **Craig Hewitt consumió toda la cuota semanal de Ultra en 24 horas**: con una suscripción al plan Cursor Ultra de $200/mes, agotó la cuota de toda una semana en un solo día el 23 de agosto de 2026.

  Archivó 10 años de correos antiguos en el Bot supervisor con el que chateaba a diario; la API recuperaba el cuerpo de los mensajes y los añadía continuamente a la sesión, inflando el contexto a cientos de miles de tokens y provocando una tormenta de relectura masiva.

  Origen del caso: [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).
- **Claves para evitar problemas con cargas pesadas**: **las tareas puntuales de alta carga nunca deben ejecutarse en el Bot principal con el que interactúas a diario**; es obligatorio crear un Bot dedicado o generar una copia mediante Duplicate; filtra el correo no deseado con reglas del buzón antes de procesar; y para tareas por lotes, valida siempre primero con 1 o 2 muestras antes del lanzamiento masivo.

## Control de chats grupales y múltiples Bots: erradicar las reactivaciones mutuas

**Bajo ninguna circunstancia incluyas varios Bots en un mismo chat grupal.** Cada mensaje nuevo se difunde a todos los integrantes, obligando a cada Bot a releer todo el historial para responder. 铁柱 relató que 4 Bots conversando entre sí consumieron rápidamente el 25% de la cuota semanal (sin verificar).

La colaboración entre múltiples Bots debe regirse por una arquitectura en **estrella (hub-and-spoke), prohibiendo las conexiones horizontales**.

- Líder único: conserva un único Bot principal como punto de entrada de la interacción.
- Asignación unidireccional: el Bot principal inicia Subagents o transferencias punto a punto (A2A); los subagentes finalizan su ejecución y se cierran automáticamente, sin responder en el chat.
- Persistencia de resultados: la tarea ascendente escribe los datos en archivos bajo `/workspace/` y la descendente los lee directamente, sin debatir ni procesar en la ventana de chat.
- Limpieza de inactivos: elimina a tiempo los Bots inactivos tras confirmar que no tienen rutinas asociadas, evitando así reactivaciones accidentales.

Origen: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## ¿Cómo realizar auditorías de uso y gestionar emergencias por agotamiento en Grok Bot? {#用量审计与应急机制-守住每周节奏}

**Dedica 15 minutos el día anterior al reinicio semanal para revisar los registros de las rutinas y la facturación; si la cuota se agota y la interfaz se bloquea, el ordenador en la nube Linux subyacente no se destruirá: puedes abrir el terminal directamente para tomar el control del código y hacer commits y pushes manualmente.**

### Proceso de auditoría semanal de 15 minutos

Se recomienda dedicar 15 minutos el día anterior al restablecimiento semanal para verificar lo siguiente:
1. Abre Settings > Usage & Billing para ver el porcentaje consumido. Si el consumo va por delante de lo previsto, revisa las tareas de días anteriores para localizar las fechas anómalas.
2. Accede a Details > Routines para examinar los últimos 20 registros de ejecución (Running, Succeeded o Failed), identificando rutinas con reintentos por error o ejecuciones frecuentes en vacío.
3. En cuanto al Bot principal marcado como favorito a partir de la v0.66.0, **prohíbe expresamente en su descripción que asuma tareas por iniciativa propia**, evitando que se encargue de tareas secundarias de forma autónoma.
4. Visita cursor.com/dashboard, revisa el Monthly Limit y el cobro real bajo demanda para confirmar que no haya cargos anómalos.

### Puntos ciegos de monitorización y cómo afrontarlos

El sistema no proporciona un desglose detallado del consumo por Bot, rutina, conversación o modelo, y el historial de 20 ejecuciones tampoco registra tokens ni importes económicos. **Para probar nuevos flujos es obligatorio utilizar el método de control de variables**:
1. Crea o modifica únicamente un Bot o una rutina cada vez.
2. Consulta el porcentaje en Usage & Billing antes y después de la ejecución para comparar el incremento; evita bajo cualquier circunstancia desplegar varias rutinas nuevas al mismo tiempo.

### Respuesta de emergencia: toma de control del ordenador en la nube al agotarse la cuota

Cuando la cuota semanal se agota al 100% y el chat de la interfaz se bloquea, el ordenador en la nube Linux subyacente no se destruye; puedes tomar el control abriendo el escritorio o el terminal del sistema desde el cliente:
1. Revisa el código y los archivos no entregados en el directorio `/workspace/`.
2. Ejecuta manualmente `git commit` y `git push` para subir los cambios al repositorio remoto.
3. Utiliza herramientas de línea de comandos locales en el terminal para continuar con la depuración, **sin necesidad alguna de gastar dinero comprando uso adicional**.

Origen: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Biblioteca de prompts para ahorrar cuota listos para enviar al Bot

### Prevención de la sobrecarga del contexto
- Haz que el Bot sintetice y memorice las reglas para **evitar repetir instrucciones continuamente en el chat**; en Bots compartidos, puedes añadirlas en el campo About de los detalles.
```text
请回顾我们至今的协作流程，执行两项沉淀工作：
1. 把你需要长期遵守的行为边界、汇报格式与约束规矩，提炼成一段不超过 300 字的精简文本，我将直接粘贴到你的描述（Description）中；
2. 把我们刚才已经跑通的标准操作流程，封装为一个可复用的技能（Skill），供后续例程直接调用。
完成提取后直接在对话中给出文本，不要展开多余闲聊。
```
- Fuerza el guardado en disco de registros originales y documentación extensa en lugar de pegarlos directamente en la conversación.
```text
从现在起执行上下文瘦身规则：
所有抓取的长篇网页、接口调试日志、大批原始数据和阶段性中间产物，一律直接保存为 /workspace/ 目录下的文本文件。在聊天窗口中回复我时，严格只提供核心结论、关键变动要点以及对应的文件绝对路径。严禁将大段原始文本或日志代码贴回对话。
```
- Convierte imágenes multimodales para analizarlas desde la línea de comandos, **evitando el alto consumo en la ventana de chat**.
```text
遇到查看多张截图、分析视频画面、逐帧拉片、音频转写或处理长扫描件的任务时，严禁在当前对话框中直接读取原始多模态文件。
你应当在云电脑终端中调用系统已配置的命令行工具（如 Grok Build 或相关转录 CLI）在后台执行，并输出简明的结构化文字摘要；你只需阅读生成的文字结论。如果当前环境无法执行命令行解析，请停下提醒我先在网页端转换成文字后再发给你。
```

### Derivación de tareas y código
- Las rutinas de monitorización deben cerrarse en silencio si no hay cambios.
```text
请列出当前你名下的全部例行任务（Routines），注明每条任务的触发频率、每周预计运行次数以及没有变化时的处理逻辑。
找出其中运行最频繁、消耗最大的任务，向我提出降低频率的具体建议；同时为所有监控类例程添加硬性约束：执行检查后若目标无实质变动，立刻静默退出，严禁向我发送「一切正常」或「没有新消息」等无有效信息的通报。
```
- Las tareas deben asignarse mediante chats individuales, **prohibiendo estrictamente que los Bots creen grupos o conversen entre sí por su cuenta**.
```text
严格执行独立单聊工作模式：
只接收并执行我本人下达的直接指令。严禁在没有得到我明确授权的情况下，主动在会话中唤醒、提及或联络其他 Bot 开展群聊协同；如果任务涉及多个专业环节，请将结果写成文件并由我来负责跨 Bot 调度，或者将其派发给云电脑内的后台 CLI 工具独立运行。
```
- El Bot se enfoca en la orquestación; la redacción y depuración de código extenso **se delega a la CLI en segundo plano de Grok Build**.
```text
明确你的角色定位是任务调度主管，核心职责是理解目标、拆解方案、组织逻辑和验收结果。
不要在聊天窗口中直接编写整段的长篇代码，也不要通读整个大型仓库做全量重构。涉及代码编写、项目调试和环境排查的工作，统一在后台调用云电脑内已经授权的 Grok Build 命令行工具执行。执行完毕后，你仅需检查其退出状态码并将最终结论同步给我。
```

### Búsqueda, control de riesgos y relevo
- Guarda en disco los resultados de búsqueda en la plataforma X y reporta solo puntos clave simplificados en la conversación.
```text
在检索 X 平台的推文、观点或动态时，使用你自带的免费搜索能力。
搜索到的批量推文原文，请直接写入 /workspace/ 下的对应 markdown 文件中保存。在聊天框中向我汇报时，严格限制为 3 到 5 条提炼后的核心事实与推文对应链接，严禁把多条推文的大段原文搬运回聊天中。
```
- La automatización y las llamadas a API deben contar con un límite de reintentos, **interrumpiendo de forma obligatoria para aprobación humana en caso de anomalía**.
```text
在执行自动化任务、网络请求或文件排查时，严格执行防死循环规则：
同一操作或相似接口调用的重试上限为 2 次。如果连续 2 次重试均未成功，或者对下一步执行动作存在疑问，立刻中断自动化流程并向我发起提问，详细说明遇到的错误原因，严禁自行无限重试或在后台空转。
```
- Antes de duplicar con Duplicate, haz que el Bot antiguo elabore una ficha de traspaso **estrictamente limitada a menos de 10 líneas**.
::: details Búsqueda, control de riesgos y relevo
```text
当前会话历史较长，需要进行交接重置。请为我梳理一份 10 行以内的结构化交接总结，严格包含以下五项内容：
1. 你的角色设定与核心职责；
2. 当前正在进行的任务目标；
3. 已经达成的关键结论与做过的核心决定；
4. 下一步必须立刻执行的动作；
5. 新会话需要优先读取的关键文件绝对路径。
输出完毕后不要执行任何新任务，等待我启动新会话。
```
:::
- Rellena la clave gratuita de OpenRouter en el cuadro de claves para desviar directamente las tareas ligeras.
```text
请协助配置 OpenRouter 免费模型调用环境，严格遵循以下安全执行流程：
1. 在聊天框中调出系统的密钥输入弹窗向我收取 API Key，严禁让我把密钥明文发送在普通对话中；
2. 将获取到的 Key 保存到 ~/.agents/secrets/openrouter.env 文件中，环境变量名指定为 OPENROUTER_API_KEY；
3. 对该密钥文件执行 chmod 600 设置安全权限；
4. 执行全程严禁在终端标准输出或聊天消息中打印该 Key 的明文内容；
5. 使用 curl 调用一个以 :free 结尾的免费模型进行一次最小文本测试，确认调用成功且费用为 0，并将测试结果告诉我。
```

Referencia del prototipo: [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Errores comunes

- En Details > Routines, hacer clic en Test ejecuta el flujo real en la máquina, **descontando cuota real en cada ocasión**.
- Las cuotas de Cursor y SuperGrok **no se acumulan**: solo se toma en cuenta la que tenga mayor uso semanal y la otra queda inactiva.
- La facturación de grok.com y Grok Bot es independiente; las recargas de la versión web **no son deducibles ni reembolsables**.
- Pegar una API Key o Webhook en la ventana de chat consume tokens y es peligroso: **debes usar la ventana emergente segura para definir variables de entorno**.
- Hacer clic en «Actualizar ordenador» borrará el cron de Linux, conservando `/workspace/`; **tras actualizar, deberás reinstalar cron**.
- Duplicate descarta la conversación, la learned memory y los archivos adjuntos: **tendrás que proporcionar el contexto manualmente al nuevo Bot**.
- Al alcanzarse el Monthly Limit no se eliminan los procesos en curso: **las tareas largas seguirán ejecutándose hasta el final**, por lo que un bucle infinito podría generar costes excesivos.

## Cómo verificar y validar los resultados

1. Ve a Settings > Usage & Billing y a cursor.com/dashboard para revisar la facturación, asegurándote de ver el porcentaje consumido y la cuenta atrás de reinicio; **desactiva Additional Usage o fija el Monthly Limit en un valor bajo y seguro**.
2. Haz que el Bot simule borrar archivos o enviar peticiones de red hacia el exterior; debe mostrar obligatoriamente la tarjeta de aprobación **Ask first** y quedar en pausa a la espera, sin ejecutarse nunca en silencio.
3. Revisa la conversación actual y lanza una búsqueda en X de múltiples publicaciones: la barra lateral no debe acumular conversaciones largas de decenas de turnos, debe devolver solo de 3 a 5 puntos de resumen, guardar los textos largos en `/workspace/` y no volcar el texto original en el chat.
4. Dirígete a Details > Routines y haz clic en Test en una rutina de monitorización sin cambios; tras la comprobación debe cerrarse en silencio de inmediato, sin enviar mensajes innecesarios de «sin actualizaciones».
5. Pide al Bot que escriba código con dependencias multifichero y comprueba que invoque Grok Build en segundo plano o el Agent en la nube, **mostrando únicamente el estado final y el resumen de ejecución**, sin pegar pantallas enteras de código en el chat.

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 2 Planes y suscripciones: elige el nivel adecuado](/part1/02-plans)
- [Capítulo 8 Habilidades y rutinas: convierte un éxito puntual en una ejecución automática diaria](/part1/08-skills-routines)
- [Capítulo 20 Automatización fiable: programación, Webhooks y disparadores de eventos](/part3/20-automation)
- [Capítulo 25 Preguntas frecuentes y resolución de problemas](/part4/25-faq)

### Documentación oficial y centro de ayuda
- [Guía oficial de Cursor: Planes y facturación](https://cursor.com/cn/help/grok-bot/plans)
- [Guía oficial de Cursor: Rutinas](https://cursor.com/cn/help/grok-bot/routines)

### Casos prácticos de la comunidad y resúmenes de optimización
- [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)
- [《Resumen del evento presencial de Hangzhou: cómo hice que la cuota de Grok Bot durara más》](https://jcng5q8n0f3z.feishu.cn/wiki/D04JwEvL7iss9UkDBvLcLuvyncf)
- [《Ahorrar un poco más de cuota en Grok Bot: optimización extrema de tareas programadas》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)
- [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi)
