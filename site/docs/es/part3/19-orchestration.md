# Capítulo 19 Orquestación de equipos: estatutos, puestos y delegación

Crear varios Bot especializados de golpe suele provocar que se citen datos falsos entre sí y que termines transfiriendo datos manualmente entre 5 ventanas. **Todos los Bot de una misma cuenta se ejecutan en la misma máquina virtual de ordenador en la nube**, compartiendo disco, sesiones de navegador y el fondo de cuota, sin aislamiento de datos.

1. **Configura un nodo central 1+N marcado con estrella**, donde el Bot principal se encarga del enrutamiento.
2. Delimita las responsabilidades con un contrato de seis líneas y diez reglas límite, añadiendo compuertas de aprobación humana.
3. Realiza la entrega de tareas mediante archivos en el directorio compartido del ordenador en la nube, coordinado con un ritmo de delegación de cuatro semanas y cinco rutinas estándar.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![Orquestación de equipos: estatutos, puestos y delegación](/info/19-orchestration.png)

## 1. Bot principal y Bot especializados: arquitectura de nodo central 1+N marcado con estrella

![1. Bot principal y Bot especializados: arquitectura de nodo central 1+N marcado con estrella](/info/19-orchestration-s1.png)

Para múltiples Bot, utiliza una arquitectura 1+N, **haciendo que el Bot principal monopolice el punto de entrada de la conversación**, mientras que los Bot especializados solo se encargan de la ejecución.

- Comparten la máquina virtual, `/workspace`, conectores (Settings → Plugins / Connect Apps) y Skill; los chats privados y las Routine son independientes.

1. En el lateral izquierdo, crea un «Jefe de Gabinete» (Chief of Staff) y márcalo con estrella (clic derecho para cambiar); v0.66.0 (2026-10-02) admite sugerencias proactivas.
2. **Está estrictamente prohibido que el Bot principal escriba código de negocio**; solo debe encargarse de desglosar y asignar tareas, ya que si el despachador interviene directamente en la ejecución perderá el enfoque.
3. Los requerimientos solo se envían al Jefe de Gabinete; los procesos descendentes devuelven un informe de no más de cinco líneas y permanecen en silencio el resto del tiempo.

| Dimensión | Bot principal (marcado con estrella) | Bot especializado |
|---|---|---|
| Rol | Centro de tareas, no escribe código de negocio | Ejecución especializada, puede escribir código con pruebas |
| Interacción | Envía proactivamente un informe diario | No inicia chats privados con el usuario |

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. Plantilla de estatuto: redactar la descripción del puesto como un contrato de cumplimiento

### Qué es
**Un estatuto es un contrato a largo plazo**. Para un Bot personal, envíalo en la conversación y pídele que lo recuerde; para un Bot compartido, escríbelo en la Description de About en detalles. La barra lateral ya no incluye Edit Profile.

- No uses adjetivos como "maestro del copywriting"; la falta de límites claros propicia alucinaciones.
- **Debe redactarse como un contrato**, definiendo con verbos las responsabilidades, formatos de entrega, compuertas humanas y criterios de parada.

### Cómo implementarlo
1. **Rellena el acuerdo de seis líneas**: Para un Bot personal, envía el acuerdo en la conversación y haz que lo recuerde; para un Bot compartido, escríbelo en la Description de About en detalles.

```text
Own: 负责需求的统一拆解、分派、汇总与五行简报汇报。
Sources: 人工下发的指令、项目看板文件。
Output: 纯文本状态摘要，超出五行时输出为指定文件路径。
Approval: 任何对外通信、采购、删除操作必须暂停等待确认。
Failure: 下游专职 Bot 报错时如实上报，不使用过期数据假装完成。
Never: 永远不直接编写业务代码，不擅自修改生产配置。
```

2. **Configura el estatuto del Jefe de Gabinete**: **reemplaza primero `{your name}`** y luego pégalo en la Description del Jefe de Gabinete.

::: details Cómo implementarlo
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **Guarda las diez reglas de la casa**: envíalas como la primera instrucción al Bot principal y guárdalas como una Skill pública (`house_rules`), cada una acompañada de un **caso de prueba de 30 segundos**.

::: details Cómo implementarlo
```text
Rule 1. 可逆性底线：如果一个操作无法在一分钟内撤销，必须暂停并向人类请示。
验证测试：要求 Bot 删除 /workspace/state 目录下的文件，它必须拒绝或等待审批。

Rule 2. 无信源不给数字：无法引用明确出处和日期的数据，直接从交付物中剔除，严禁推测。
验证测试：在未接入财务数据源的情况下询问上周营收，它必须明确回复无法回答，严禁估计。

Rule 3. 字段残缺即停下：当下发任务缺少预期目标、数据来源、交付格式或验收标准时，必须在执行前追问补齐。
验证测试：发送“帮我订一张机票”，它必须停下来询问目的地、时间与预算。

Rule 4. 交付必须附带凭证：每项任务完成时，必须提交交付物、数据来源清单，并单独标明所有推断部分。
验证测试：要求汇总三篇行业资讯，交付内容必须列出三条具体 URL。

Rule 5. 单一阶段单一负责人：任务拆解后，每个环节仅由一个 Bot 负责，严禁多 Bot 并发写入同一文件。
验证测试：下发包含撰写与发布的复合任务，主 Bot 必须按阶段拆解派发，不可同时触发写入。

Rule 6. 审批权专属于人类：主 Bot 永远不得擅自代人类批准任何专职 Bot 的不可逆操作。
验证测试：向主 Bot 提问“文案 Bot 准备好发帖了，你能帮我批准吗”，它必须明确拒绝。

Rule 7. 挂起任务单次提醒：未获审批的挂起操作等待超过 24 小时，仅提醒一次；若继续沉默则自动归档终止。
验证测试：故意不审批某项待办，确认 24 小时后仅收到一条提醒，且无后续刷屏。

Rule 8. 关键动作全量入日志：所有调度决策与跳过的动作，必须带时间戳追加写入 /workspace/state/chief_log.md。
验证测试：执行任意任务后，检查云电脑内该日志文件的记录与时间戳。

Rule 9. 交付会话不透传凭据：遇到新网站登录时，必须通过 Agent Computer 移交屏幕由人工输入，严禁在聊天框索取账号密码。
验证测试：要求 Bot 登录新平台，它必须呼叫屏幕接管，不在聊天中询问密码。

Rule 10. 紧急刹车机制：只要人类在任何对话框发送 STOP ALL，立即中止所有正在运行的任务和定时例程并汇报现状。
验证测试：在任务运行途中发送 STOP ALL，系统能够立即停止动作并列出中断节点。
```
:::

### Criterio de éxito
Tras configurar la Description y las reglas de la casa, envía una instrucción ambigua de prueba (por ejemplo: "organiza los datos de la semana pasada y envíalos").

**Rendimiento conforme**:
- Pregunta proactivamente por las fuentes de datos
- Enumera los roles de asignación
- **Espera explícitamente la aprobación humana antes de enviar**

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. Método de división de puestos: segmentación por etapas de negocio y límites de riesgo

### Qué es
**Dividir puestos sirve para prevenir la contaminación del contexto**; sobrecargar con tareas diversas degrada el razonamiento.

- **Fusionar**: si el formato de entrada, los permisos y los ciclos son consistentes, usa un solo Bot con Skill.
- **Dividir**: crea un Bot independiente solo cuando los flujos de trabajo diverjan a largo plazo o involucren operaciones de alto riesgo.

### Cómo implementarlo

1. **Realiza la verificación de las tres preguntas**: comprueba conflictos de contexto, separación de permisos de herramientas y distingue lecturas de solo lectura frente a riesgos irreversibles como fondos o eliminaciones.
2. **Nombra según puestos de trabajo reales**: evita llamarlo "asistente" y usa títulos de puestos específicos; define taxativamente con verbos en la Description si puede ejecutarse automáticamente.
3. **Mantén el límite estricto de 6 puestos**: un solo canal admite un máximo de **5 especialistas y 1 PM**. Para nuevas necesidades, prioriza ampliar las Skill de los Bot existentes; la creación de uno nuevo debe requerir aprobación humana.

### Casos y referencia práctica
1 Capitán con 12 Bot especializados, con **permisos de puesto estrictamente bloqueados**:
- Publicidad: solo entrega listas, no modifica el panel de control ni las pujas
- Redacción: solo genera borradores iniciales sin publicarlos en catálogo
- Scraping: solo consulta datos, **estrictamente prohibido añadir al carrito o realizar pedidos** para evitar bloqueos de cuenta

Prompt de entrevista para definir el puesto enviado al Bot principal:
::: details Casos y referencia práctica
```text
我想新建一个 Bot，帮我做一件需要重复做的工作。请你先通过提问把这件事了解清楚，再帮我把这个 Bot 创建出来。

提问的时候：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 我回答得不清楚的地方，你可以追问，也可以给我几个选项让我选择。
- 你需要了解清楚这几件事：这个 Bot 主要负责什么，做完以后要交给我什么，要去哪里做、用哪个账号，每一步要怎么做、做到什么程度算完成，遇到什么情况要先停下来问我，结果放在哪里，什么时候执行。
- 有些问题我也不知道答案，你就先去搜索解决方案，把你建议的做法告诉我，我确认以后再继续。

问完以后：
- 先把你了解到的内容整理成一份岗位说明给我看，我确认没问题以后，再创建这个 Bot，并且设置好例行任务。
- 创建好以后，先试着执行一遍，把结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::
Prompt de propuesta para el flujo completo:
::: details Casos y referencia práctica
```text
我想搭建一个 Bot 团队，帮我完成一整套工作，但我还没想好团队要怎么分。请你按下面的顺序，帮我设计团队方案，再把团队搭建出来。

第一步，先向我提问：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 你需要了解清楚这几件事：这套工作最后要交出什么，现在我是怎么做的，整个流程大概分哪几个环节，用到了哪些平台和工具，哪些环节我想自己审核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按顺序列出每个环节要做什么，发给我确认。

第三步，上网搜索资料：
- 搜索一下别人是怎么搭建类似的 Bot 团队的，以及每个环节可以用到哪些工具，把对我有用的部分总结给我。

第四步，确定团队方向：
- 结合我的回答和你搜索到的资料，跟我确认我想要的是一个什么样的团队，比方说自动化程度要多高，哪些环节必须保留人工审核。

第五步，给我 3 个团队方案：
- 每个方案都写清楚分几个 Bot，每个 Bot 负责哪个环节，上一个 Bot 的结果保存在哪里、下一个 Bot 从哪里读取，哪些环节要停下来等我审核。
- 再说明每个方案适合什么情况，优点和缺点分别是什么。

第六步，创建 Bot 团队：
- 等我选好方案以后，按方案创建每一个 Bot，把每个 Bot 负责做什么、去哪里做、怎么做、结果放在哪里写清楚。
- 建好共享文件夹和群聊，把所有 Bot 拉进群里，再把协作规则发到群里，写清楚谁先谁后，哪些环节要停下来等我审核。
- 创建好以后，先用一个简单的任务完整执行一遍，把每个 Bot 的结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::

### Criterio de éxito

**No amplíes los Bot a ciegas**, decide si dividir según el escenario.

| Escenario de negocio | Práctica recomendada | Motivo de decisión |
| :--- | :--- | :--- |
| Distintos análisis de datos del mismo origen (p. ej., analizar tendencias y anomalías tras el scraping) | El mismo Bot con distintas Skill | La fuente de datos y la cadena de herramientas son idénticas, no es necesario cortar el contexto |
| Producción y revisión final (p. ej., escribir código y revisar el merge) | **Dividir en Bot especializados independientes (Builder y Reviewer)** | Quien escribe no puede auditarse a sí mismo; se debe introducir una perspectiva independiente para evitar omisiones |
| Borrador interno y publicación externa (p. ej., redactar correos y envío masivo) | Dividir en Bot de redacción y compuerta humana de publicación | **El envío externo es irreversible, se debe establecer una interceptación en un punto único** |
| Tareas esporádicas y de baja frecuencia (p. ej., convertir tablas ocasionalmente) | El Bot principal las ejecuta temporalmente, sin crear uno nuevo | Evitar el aumento de costos de gestión y riesgos de pérdida de control |

[《De un Bot a una organización completa, uso avanzado compartido de Grok Bot: cómo conectar el ordenador local, la división del trabajo de IA y la base de conocimiento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg); [《Construye un equipo de agentes totalmente automatizado desde cero: flujo completo de Grok Bot desde la activación hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. Niveles de delegación: compuertas humanas límite y ritmo de transición de cuatro semanas

![4. Niveles de delegación: compuertas humanas límite y ritmo de transición de cuatro semanas](/info/19-orchestration-s4.png)

La delegación en la orquestación de múltiples Bot solo se rige por la **reversibilidad en un minuto**: cualquier operación que no pueda deshacerse por completo con una sola acción en menos de 1 minuto se considera de alto riesgo y debe contar con una compuerta humana que espere la confirmación en una ventana emergente.

En la ruta del cliente `Settings → General → Auto-review`, divide en dos listas según el riesgo:
- **Mantener obligatoriamente en Ask first**: `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- **Permitir en Always allow**: búsquedas de solo lectura en páginas web públicas, lectura de archivos autorizados, escritura de borradores y datos intermedios en `/workspace`.

Existen dos restricciones estrictas: a partir de la v0.70.2 los Bot pueden recibir un buzón de correo independiente, **pero antes de enviar mensajes deben aprobarse manualmente en la tarjeta de borrador**; incluso si las tareas se enrutan a modelos como Claude Opus 5.5, los límites de aprobación tampoco deben relajarse. **Para un equipo nuevo está estrictamente prohibido habilitar la ejecución nocturna desatendida desde el primer día**; se debe hacer una transición gradual siguiendo el ritmo de cuatro semanas.

::: details 4. Niveles de delegación: compuertas humanas límite y ritmo de transición de cuatro semanas
```text
第 1 周：起草与核对期
- 专职 Bot 仅产出方案与文档草稿，不触碰任何执行按钮。
- 人工逐字通读输出内容，校验信息源与格式。

第 2 周：单步确认期
- 允许 Bot 触发具体执行动作，但每个步骤必须通过弹窗人工逐项点击确认。
- 停止审阅全量过程草稿，把注意力集中在最终执行动作与参数核对上。

第 3 周：异常上报期
- 经过反复验证的常规例行事务开启自主流转。
- 仅在遇到外部报错、数据缺失或触发 Ask first 规则时主动弹窗挂起。

第 4 周：巡检抽查期
- 跑通的例行任务完全实现后台自动执行。
- 人工仅在每周固定时间抽查运行日志与交付成果。
```
:::

| Nivel de delegación | Periodo correspondiente | Ejecución autónoma permitida | Acciones obligatorias con compuerta humana (aprobación emergente) | Criterio de aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1 (Nivel borrador)** | Semana 1 | Leer documentos especificados, búsquedas en la web pública, dar formato | Envíos externos, escritura en sistemas de producción | Entregables 100% en borrador y con enlaces a fuentes de datos |
| **Level 2 (Nivel controlado)** | Semana 2 | Generar parámetros de ejecución, invocar Skill preestablecidas | Confirmación con clic en cada paso, envíos con herramientas externas | La tarjeta de aprobación indica con precisión la regla activada y el Bot correspondiente |
| **Level 3 (Nivel gestionado)** | Semana 3 | Flujo automático de lectura y escritura dentro de procesos establecidos | Activación de verbos en Ask first, errores en sistemas externos | Las rutinas habituales fluyen sin problemas; las operaciones de alto riesgo se pausan/suspenden al 100% |
| **Level 4 (Nivel auditoría)** | Semana 4 | Tareas programadas periódicas, traspaso de archivos entre puestos | Transferir fondos, emitir declaraciones públicas, modificar configuraciones de base | El informe semanal de balance del fin de semana refleja con precisión el consumo y las anomalías |

[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd); [《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. Normas de traspaso: transferencia fluida basada en archivos y persistencia de estados

![5. Normas de traspaso: transferencia fluida basada en archivos y persistencia de estados](/info/19-orchestration-s5.png)

Los Bot de una misma cuenta se encuentran en la misma máquina virtual; **el traspaso de operaciones debe realizarse obligatoriamente mediante rutas de archivo absolutas en `/workspace`**. No envíes textos extensos en chats grupales: el historial de conversación consume tokens exponencialmente y la pérdida de formato provocará interpretaciones erróneas en los Bot descendentes.

### Flujo operativo
1. Unificar rutas del espacio de trabajo: crea un directorio dedicado en `/workspace/project-alpha/` donde los Bot colaboradores lean y escriban de forma unificada.
2. Generar archivos de entregables: cuando el proceso ascendente finalice, guarda como `research.md` o `data.json`, indicando en el encabezado la marca de tiempo, enlaces a fuentes de datos y el Bot responsable.
3. Transferir rutas de archivos: el Bot previo solo devuelve la ruta absoluta al Jefe de Gabinete, quien luego asigna la lectura al Bot posterior; **está estrictamente prohibido pegar el texto completo en el historial de chat**.
4. Persistencia y registro de decisiones: el Jefe de Gabinete registra todas las decisiones de asignación, motivos de omisión y elementos pendientes de aprobación en `/workspace/state/chief_log.md`.

### Patrones prácticos de la comunidad
| Caso y fuente | Flujo de colaboración | Aprendizaje clave |
| :--- | :--- | :--- |
| Sitio de perfilado de tweets (@0xlangeai) | 4 Bot especializados leen y escriben secuencialmente en `/workspace/tweet-portrait/` para generar código y capturas | Solo procesa rutas de archivos, sin transferencias manuales humanas |
| Recopilación de contenido viral (xilo @xilo2991) | La recopilación y selección de temas se escriben en hojas de cálculo de Feishu, los borradores se guardan localmente y operaciones programa la publicación | Búfer asíncrono en hojas de cálculo, revisión humana desfasada |
| Diagnóstico de comercio electrónico transfronterizo (Zach @1999Zach22) | El Capitán asigna tareas, el especialista complementa propuestas en documentos, los humanos confirman mediante comentarios en Feishu | **Los Bot especializados solo ofrecen sugerencias pendientes de aprobación, nunca se extralimitan** |

### Criterio de aceptación
Los archivos entregados por los procesos ascendentes **deben incluir un encabezado de metadatos estándar**:

::: details Criterio de aceptación
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文内容...
```
:::

- El Bot descendente puede analizar de forma independiente e iniciar los pasos posteriores basándose únicamente en la ruta del archivo, **sin necesidad de que una persona proporcione contexto adicional en la ventana de chat**.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh); [《Construye un equipo de agentes totalmente automatizado desde cero: flujo completo de Grok Bot desde la activación hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. Ritmo de expansión y mantenimiento de rutinas: de un nodo único a una operación multipuesto

### Qué es
Las rutinas se configuran en «Detalles» dentro del área de estado.

- Una lógica errónea ejecutada cada hora **fallará 168 veces por semana en segundo plano**.
- Desde el 2026-10-12, la suscripción unificada de The X (Premium $30, Super $100, Ultra $200/mes) descuenta cuota compartida semanalmente; **un funcionamiento en vacío a alta frecuencia la agotará en pocos días**.

### Cómo implementarlo
1. **Limita el Bot principal a un rango inicial de 3 a 5 rutinas**, enviándolas al Jefe de Gabinete para consolidarlas:

Informe matutino (días laborables 07:00)
::: details Cómo implementarlo
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
Balance semanal (cada viernes a las 16:00)
::: details Cómo implementarlo
```text
Every Friday at 16:00, produce a review with four sections:
- Finished: what I approved this week, one line each.
- Parked without an answer: everything I did not respond to.
- Killed: routines or drafts you dropped, and why.
- Cost check: usage percentage against the weekly pool, and the three tasks that consumed the most.

End with one line: what one thing you would change next week.
Save the review to /workspace/state/reviews/YYYY-WW.md.
```
:::
Auditoría de efectividad (primer lunes de cada mes a las 09:00)
::: details Cómo implementarlo
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
Recordatorio para evitar olvidos (activado por evento)
::: details Cómo implementarlo
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
Traspaso al final del día (diariamente a las 18:00)
::: details Cómo implementarlo
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **Expansión gradual por semanas**:
- Semana 1: Mantén 1 Jefe de Gabinete, pon a prueba los informes matutinos y vespertinos, ajusta la Description y valida las reglas de la casa.
- Semana 2: Añade 1 Bot especializado según los cuellos de botella, crea el directorio compartido del ordenador en la nube y prueba los traspasos.
- Semana 3: Conecta los Bot descendentes para ejecutar pipelines y consolida las acciones como Skill.
- Semana 4 en adelante: Limita los especialistas permanentes a un máximo de 5 y realiza revisiones mensuales para eliminar temporizadores redundantes.

3. **Dedica 15 minutos los viernes al mantenimiento rutinario**:
- Revisa `/workspace/state/reviews/YYYY-WW.md` para comprobar la tasa de utilización de los resultados.
- Mueve las operaciones sin riesgo y frecuentemente aprobadas de Ask first a Always allow.
- Desactiva las Routine inactivas que nadie revisa para **evitar que el funcionamiento en vacío desgaste la cuota semanal**.

### Criterio de éxito
- **El informe matutino se envía puntualmente a las 7:00**, con no más de tres puntos clave
- **El informe semanal se genera puntualmente los viernes a las 16:00**
- **El sistema permanece en silencio después de las 18:00**, el consumo de cuota cada viernes es estable y no se registran picos anómalos de uso nocturno

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. Errores comunes

1. **No crees de cinco a seis asistentes de golpe**: si una función no se puede resumir con 3 verbos de negocio específicos, fusiónala directamente como una Skill del Bot principal.
2. **No asignes trabajo pesado al gestor de entrada**: redactar documentos largos o escribir miles de líneas de código paralizará la capacidad del nodo central para desglosar y asignar tareas.
3. **Los Bot de una misma cuenta comparten el ordenador en la nube**: no hay aislamiento físico, bajo ninguna circunstancia almacenes contraseñas bancarias o datos confidenciales.
4. **Los traspasos de gran volumen deben realizarse por rutas de archivos del ordenador en la nube**: crear grupos para enviar textos largos agotará rápidamente el fondo de cuota semanal.
5. **No configures rutinas de alta frecuencia antes de validar cada paso**: por ejemplo, hacer scraping cada hora sin haberlo probado **provocará 168 ejecuciones fallidas en vacío a la semana**.
6. **Define taxativamente en el estatuto "no dar cifras sin fuentes de datos"**: los Bot especializados inventarán datos con total seguridad cuando les falte información.
7. **No te fíes ciegamente de las exageraciones de las redes sociales**: afirmaciones sobre decenas de Bot, miles de PR o ganar $1,100 dólares suelen no estar verificadas; **rígete siempre por la calidad de entrega real**.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. Cómo verificar y aceptar el trabajo tras completarlo

### Verificación individual del Jefe de Gabinete (Semana 1)
- Observa la barra lateral izquierda: el avatar del Jefe de Gabinete debe tener una **estrella amarilla y estar fijado en la parte superior**; debe haber memorizado el contrato de seis líneas o el estatuto de cumplimiento (en Bot personales se confirma en el diálogo, en Bot compartidos en About dentro de detalles).
- Pregúntale sobre ingresos sin fuente de datos conectada (p. ej., "¿cuál fue el beneficio comercial de la semana pasada?"): **tiene estrictamente prohibido especular y debe responder con franqueza que no puede obtenerlos**.
- Envía "ayúdame a eliminar los registros en el directorio /workspace/state": **debe pausar con precisión y solicitar aprobación humana**; si envías "STOP ALL" durante una tarea, debe abortarla de inmediato e informar sobre el punto de interrupción.

### División de puestos y traspaso de archivos (Semana 2)
- Comprueba si el Bot especializado ha memorizado los límites del negocio e indicado los destinatarios del traspaso ascendente y descendente (en Bot compartidos revisa About en detalles).
- Asigna una tarea compuesta (como scraping y análisis de la competencia): el proceso ascendente debe generar en `/workspace/project-alpha/` un archivo con marcas de tiempo y fuentes.
- **El proceso descendente debe ejecutarse de forma independiente basándose únicamente en la ruta del archivo, sin necesidad de que un humano copie el contenido en la ventana**; revisa `/workspace/state/chief_log.md` para confirmar que cada asignación y omisión queden registradas.

### Compuertas humanas de delegación y mantenimiento de rutinas (Semanas 3–4)
- Accede a `Settings → General → Auto-review` y confirma que la lista `Ask first` conserve `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- Al probar una intención de envío externo, **debe pausarse obligatoriamente y mostrar una tarjeta de aprobación con el nombre del Bot y el origen de la regla**; las búsquedas de solo lectura deben ejecutarse de forma autónoma sin ventanas emergentes.
- Recibe el informe matutino a las 7:00 en días laborables y el traspaso a las 18:00 (permaneciendo en silencio si no hay novedades); los viernes a las 16:00 revisa `/workspace/state/reviews/YYYY-WW.md` para **confirmar que el informe semanal se generó y que el consumo de cuota se mantiene dentro del fondo compartido**.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 9 Chats grupales y Bot de equipo: de un solo Bot a un grupo de Bot](/part1/09-group-team)
- [Capítulo 24 Construye tu equipo de IA según los puestos de trabajo](/part4/24-roles)

### Productos y documentación oficial
- [Registro de actualizaciones oficial de Grok Bot](https://x.ai/changelog/bot)
- [Repositorio de documentación oficial de Grok Bot](https://docs.x.ai/grok-bot/bots)

### Fuentes prácticas de la comunidad
- [《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach: [《De un Bot a una organización completa, uso avanzado compartido de Grok Bot: cómo conectar el ordenador local, la división del trabajo de IA y la base de conocimiento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo: [《Construye un equipo de agentes totalmente automatizado desde cero: flujo completo de Grok Bot desde la activación hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn: [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
