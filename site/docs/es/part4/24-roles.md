# Capítulo 24: Estructura tu equipo de IA por puestos de trabajo

**No trates a Grok Bot como una simple ventana de chat o un asistente para todo.** Meter todas las tareas diversas en la misma sesión provoca saturación de contexto, lentitud y desperdicio de cuota, y por la noche, sin supervisión, es fácil enviar correos por error, modificar código de producción o realizar cobros y transferencias indebidas.

En el fondo, Grok Bot es una computadora en la nube equipada con un navegador independiente y un sistema de archivos local; **aprovecharlo al máximo requiere establecer una plantilla clara organizada por puestos**.

1. **Establece líneas rojas estrictas de aprobación**. Divide las responsabilidades de cada puesto según 5 señales concretas; los correos no revisados, el código de producción y las deducciones o transferencias de fondos deben detenerse invariablemente antes de la aprobación humana.
2. **Valida la transición de rutinas**. Configura la primera tarea de validación y las rutinas programadas para los 7 puestos clave, consolidando los criterios de aceptación en las revisiones rutinarias.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)


![Estructura tu equipo de IA por puestos](/info/24-roles.png)

## Cinco señales y principios organizativos para la división de puestos

![Cinco señales y principios organizativos para la división de puestos](/info/24-roles-s1.png)

### Delimitación de límites y aislamiento de entornos

Todos los bots bajo una misma cuenta comparten la misma computadora en la nube: los archivos, las sesiones web activas y los conectores son comunes. Sin embargo, la memoria y los hilos de conversación de cada bot son independientes; **mezclar diferentes tareas saturará la memoria con información irrelevante, provocando desviaciones en las instrucciones**.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Cinco señales para la división de puestos

**Siempre que el trabajo presente cualquiera de las siguientes características, se debe crear un bot dedicado e independiente.**

- Objetivos distintos: por ejemplo, encargarse de descubrir fallos del sistema frente a optimizar la tasa de conversión de un texto.
- Herramientas distintas: por ejemplo, conectarse principalmente a un repositorio de código frente a conectarse a hojas de cálculo de CRM.
- Estilos de trabajo distintos: por ejemplo, atención al cliente prudente y comedida frente a análisis de datos riguroso y objetivo que solo presenta cifras.
- Límites de aprobación distintos: por ejemplo, redactar memorandos internos debe estar separado de tener permisos para enviar correos externos.
- Horarios distintos: por ejemplo, revisar tickets cada hora frente a consolidar informes financieros todos los lunes.

### Comparación entre asistente generalista y equipo dedicado

**En comparación con un asistente generalista, un equipo dedicado aísla eficazmente el contexto y los riesgos de permisos.**

| Dimensión de comparación | Asistente generalista (propenso a problemas) | Equipo de bots dedicados |
| :--- | :--- | :--- |
| Contexto | Mezcla múltiples tareas comerciales, proclive a confusión de memoria y alucinaciones | Hilos independientes mantienen una memoria exclusiva, funcionando de forma estable |
| Permisos y depuración | El exceso de permisos aumenta el riesgo de acciones peligrosas; los conflictos son difíciles de localizar | Aprobación granular; la atribución de fallos es directa |
| Expansión de rutinas | Las tareas programadas interfieren entre sí, congestionando fácilmente el calendario | Ejecución asíncrona mediante cronogramas independientes o disparadores de eventos |

### Barreras humanas de aprobación y el principio de reversibilidad

La gestión de permisos debe adherirse firmemente a la **regla de barrera humana centrada en la reversibilidad**.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| Categoría de operación | Ejemplos de comportamiento típico | Principio de tratamiento y mecanismo de aprobación |
| :--- | :--- | :--- |
| Operaciones reversibles | Redactar documentos, conciliar cuentas, etiquetar o extraer resúmenes | Permitir que el bot las complete de forma autónoma y registre logs |
| Operaciones irreversibles | Enviar correos externos, publicar abiertamente, fusionar código o debitar fondos | **Antes de ejecutarse, debe detenerse para generar un borrador o una comparación de diferencias, quedando en espera de que un humano haga clic en aprobar dentro de la interfaz** |

## De la validación en siete pasos a la implementación de bots persistentes

![De la validación en siete pasos a la implementación de bots persistentes](/info/24-roles-s2.png)

**No te apresures a programar tareas automáticas nada más crear el bot**; primero ejecútalo manualmente siguiendo la ruta oficial: [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

1. Establece reglas en el campo de descripción (Description): especifica con claridad las responsabilidades, las fuentes de datos y las líneas rojas. **Las reglas del campo de descripción tienen efecto permanente en todas las tareas**, mientras que las instrucciones en la ventana de chat solo aplican a una única sesión.
2. Ejecuta una prueba única en un entorno seguro: limita las fuentes de entrada y ejecuta manualmente un flujo de negocio real.
3. Ajusta hasta que sea revisable: realiza correcciones mediante el diálogo hasta que alcance el estándar de revisión sin intervención.
4. Guárdalo como habilidad (Skill): guarda los pasos directamente. Para páginas web complejas, utiliza la demostración «Teach a task» (límite de 10 minutos, no graba audio del micrófono) y completa las aprobaciones de ramificaciones.
5. Validación con un segundo conjunto de entradas independientes: prueba con datos diferentes para descartar el sobreajuste al ejemplo inicial.
6. Define la estrategia de rutina (Routine): antes de crear un Schedule o Trigger, define los reintentos por tiempo de espera y el manejo de errores; **ante la pérdida de red o datos faltantes, jamás debe inventar información de la nada**.
7. Mantén compuertas de aprobación para operaciones críticas: reserva la confirmación humana (Allow once/Deny) para envíos y pagos; solo asigna Auto Review a operaciones de riesgo extremadamente bajo.

## Dotación, rutinas y prompts para 7 puestos clave

Siguiendo estos principios, dividimos el equipo digital según las necesidades del negocio en siete puestos estandarizados: contenido, ingeniería, ventas, investigación, operaciones, asistente personal y gestión. Cada puesto cuenta con límites claros de dotación, una primera tarea ligera de validación, lógica de rutinas automatizadas y prompts listos para copiar y usar.

### 1. Puesto de contenido: Bot de comparación de posicionamiento y pipeline de contenido

Este bot se ejecuta **todos los lunes a las 08:00**, recopilando 3 páginas de competidores para compararlas con nuestra pantalla principal. Si hay cambios, abre una rama de PR; si no hay cambios, permanece en silencio.

- Permisos: solo abre PR o borradores de calendarios; **queda estrictamente prohibido fusionar directamente o publicar abiertamente**.
- Criterio de aceptación: el resultado se limita a 1 tabla y 1 párrafo de texto, verificable en menos de 30 segundos.
- Errores comunes: si falla el análisis, notifica inmediatamente un enlace roto sin hacer suposiciones.

::: details 1. Puesto de contenido: Bot de comparación de posicionamiento y pipeline de contenido
```text
每周一上午 08:00，对比我们产品定位页 <our_landing_url> 与以下三个竞品页面：
1. <competitor_url_1>
2. <competitor_url_2>
3. <competitor_url_3>

产出以下内容：
- 主张对比表格：我方主张、对方主张、哪一方表述更直接明确。
- 竞品提到但我们未提及的三项内容，需附带原句引用。
- 我们提及但竞品均未提及的三项独有优势。
- 改写我方定位页前两段文案的草稿，使其更具针对性。

在代码仓库 <repo_name> 中针对文案修改开启一个 Pull Request，仅允许改动定位页文案文件。
严禁合并该 Pull Request。严禁触碰定位页以外的代码或文件。
运行结束时汇报：自上周以来竞品侧发生的主要文字变化；若无变化则明确注明。
```
:::

### 2. Puesto de ingeniería: Bot de reproducción y diagnóstico de defectos

[Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **Líneas rojas de permisos**: es obligatorio utilizar una cuenta de prueba dedicada; **queda estrictamente prohibido usar datos reales de clientes en el entorno de preproducción** y modificar alertas o parámetros de producción. Las credenciales sensibles deben gestionarse mediante Safe handoff, quedando prohibido su envío en texto plano.
2. **Pasos de depuración**: monitorea los issues etiquetados con `needs-repro` e inicia un navegador aislado en Staging para ejecutar la reproducción.
3. **Criterios de aceptación**: **rellena los comentarios del issue con un borrador que incluya el comportamiento esperado frente al real, códigos de estado de red y capturas de pantalla**, y luego elimina la etiqueta a la espera de la revisión de un ingeniero.

::: details 2. Puesto de ingeniería: Bot de reproducción y diagnóstico de defectos
```text
阅读工单 <issue_url> 中的缺陷报告，并在预发布环境 <staging_url> 中尝试复现该问题。

执行规则：
- 必须使用全新分配的测试账号登录，严禁调用或导入生产环境客户数据。
- 详细记录完整的复现操作步骤、预期行为与实际出现的不一致表现。
- 捕获异常发生时的控制台报错日志、网络请求状态以及页面截图。
- 尝试提取导致该问题的最小复现步骤。

输出规范：
将整理好的复现包整理为 Markdown 文本附在下方。
严禁修改系统的报警规则，严禁更改预发布或生产环境配置。
若尝试三次仍无法复现，详细说明每次尝试的输入参数并标记为“未能稳定复现”，不要伪造成功的结论。
```
:::

### 3. Puesto de ventas: Bot de prospección y contacto con clientes potenciales

1. Cada día laborable a las 07:00, lee las primeras 20 filas de clientes potenciales no contactados en la hoja de cálculo y evalúalos según 3 criterios clave de ICP.
2. Selecciona a los 3 contactos más compatibles y redacta para cada uno un borrador de correo de no más de 4 frases, insertándolo en la hoja de cálculo.
3. **Queda estrictamente prohibido enviar correos reales a los clientes o añadirlos a secuencias automatizadas de contacto**. Cada afirmación personalizada debe incluir un enlace a la fuente; si el acceso está restringido, detén la tarea de inmediato y repórtala a un humano.

::: details 3. Puesto de ventas: Bot de prospección y contacto con clientes potenciales
```text
每个工作日早晨 07:00，处理表格 <sheet_url> 中最早未触达的 20 行销售线索。

针对每一行数据执行以下操作：
1. 访问该公司官网及其公开社交账号，提取过去 30 天内的实质性变动（如产品发布、高管变动、业务调整或受关注动态）。
2. 根据以下三条 ICP 标准逐一判定：
   - 目标团队规模在 20 至 200 人之间；
   - 核心业务包含多工具协同流程；
   - 过去一个季度内有公开扩张动态。
   若不符合标准，在状态栏标记“不匹配”并跳过后续步骤。
3. 为符合条件的线索撰写一段不超过 4 句话的首触邮件草稿。必须直接引用第一步中查到的具体变动事实，禁止使用任何寒暄客套套话。
4. 将邮件草稿填入表格的“首触草稿”列，并在相邻列贴上佐证该事实的公开链接。

安全要求：
严禁向任何邮箱发送真实邮件。严禁将联系人导入自动发送队列。严禁调用未授权的个人账号。
运行结束时汇报：已处理行数、排除行数，以及如果你是销售代表会优先发送的前三位名单。
```
:::

### 4. Puesto de investigación: Bot de verificación de hechos y cálculo de datos

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

Se conecta a la web pública, bases de conocimiento y archivos CSV de uso. **Si faltan datos, debe reportar un error e indicar los campos ausentes; queda estrictamente prohibido hacer estimaciones empíricas o dar sugerencias sin fundamento.**

- **Primera tarea**: buscar información sobre la consulta de negocio y generar una lista de verificación, clasificando las afirmaciones en «respaldada por pruebas», «contradice las pruebas» o «no confirmada por pruebas», enumerando las lagunas de información.
- **Rutina de ejecución**: **se ejecuta todos los lunes a las 09:00**, leyendo el CSV de facturación de la semana anterior para responder 4 preguntas cuantitativas fijas y **generando un informe de datos puros de no más de una página**.

::: details 4. Puesto de investigación: Bot de verificación de hechos y cálculo de datos
```text
研究课题：<research_topic_or_question>
阅读并分析知识库及公开检索信源，生成一份可供直接发布的简报。

执行规则：
- 打开每一个引用来源页面，严禁仅凭模型内部记忆作答。
- 针对报告中的每一个核心结论，摘录支持该结论的原文章节段落。
- 对每一个主张进行事实状态标注：分为“有证据支持”、“与证据矛盾”或“证据未证实”三类。
- 当不同信源存在分歧时，同时列出双方原文，并注明发布时间先后。
- 整理在调研过程中未能找到确证信息的内容列表，将其作为正式结论的一部分列在文末。

输出规范：
输出一份精简报告、一张事实来源对比表、以及尚未解决的疑问清单。
严禁使用似是而非的推测性语句填充信息空白。如果数据源完全未提及某事，直接记录“未找到相关记录”。
```
:::

### 5. Puesto de operaciones: Bot de soporte de tickets y conciliación contable

1. Gestión de tickets: redacta respuestas automáticamente cada hora; **las respuestas solo pueden escribirse en Internal Note, quedando estrictamente prohibido enviarlas al usuario**.
2. Conciliación de facturas: los días laborables a las 17:00, recopila las 10 facturas más recientes para cotejarlas con la tabla de órdenes de compra (PO), señalando coincidencias, excesos y partidas faltantes; las anomalías quedan suspendidas a la espera de revisión humana.
3. Líneas rojas de permisos: **debe emitir una alerta si la desviación del importe supera el 2% o si aparece un nuevo proveedor**; queda estrictamente prohibido aprobar transacciones o iniciar transferencias sin autorización.

::: details 5. Puesto de operaciones: Bot de soporte de tickets y conciliación contable
```text
每天下午 17:00，读取财务收件箱 <finance_inbox> 中的新增发票，与采购订单表格 <po_sheet_url> 进行逐笔核对。

针对每张发票执行以下比对：
- 提取金额、币种、开票日期、采购订单号（PO Number）与供应商全称。
- 在采购表格中查找对应的 PO 记录。若无匹配记录，在备注栏标明“无对应订单”。
- 比对发票金额与 PO 批准金额。若偏差绝对值超过 2%，立即将其标记为“金额异常偏差”，并记录具体差额。
- 检查供应商名称是否属于本季度首次出现的新供应商，若是，打上“新供应商待核实”标签。

结果写入规范：
将比对明细写入表格 <po_sheet_url> 的“对账结果”工作表中，并附带该发票的原件查看链接。
严禁执行任何批准报销、发起付款或向供应商发送邮件的操作。
运行结束时汇报：成功匹配笔数、异常待查笔数，以及所有存在异常的发票总金额。
```
:::

### 6. Puesto de asistente personal: Bot de gestión de bandeja de entrada y agenda

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **Operación diaria**: los días laborables a las 07:30, escanea los correos y calendarios de las últimas 24 horas y genera un informe matutino de una sola página.
2. **Primera tarea**: limpiar notificaciones irrelevantes y redactar para 2 correos importantes sendos borradores de no más de 4 frases cada uno, colocándolos en «Pendiente de revisión» y deteniéndose a la espera de la confirmación humana.
3. **Líneas rojas de permisos**: solo archivar correo no deseado y notificaciones; **queda estrictamente prohibido eliminar o modificar correos de contabilidad, legales, clientes clave o directivos**; **las respuestas solo se guardan como borradores sin enviarse jamás por iniciativa propia, y el calendario no se modifica**.

::: details 6. Puesto de asistente personal: Bot de gestión de bandeja de entrada y agenda
```text
每个工作日早晨 07:30，扫描我的工作邮箱 <email_account> 与日历 <calendar_url>。

处理规则：
1. 自动归档系统通知、营销推广与电子发票。若邮件发件人包含会计师、法务顾问或核心客户，严禁自动归档。
2. 提取需要我亲自处理的事项，按紧急程度列出，注明发件人、主要诉求与截止期限。
3. 针对其中最需要紧急回复的 2 封邮件，以我的口吻起草回复方案：
   - 语言简短直接，不使用套话与客套感谢语；
   - 整体控制在 4 句话以内，明确给出下一步行动建议；
   - 若涉及约定会议时间，主动从我日历中调取明天下午的 2 个空闲时段供对方选择。
4. 汇总今天必须参加的会议日程，标出准备资料缺失的场次。

安全边界：
所有生成的回复只能存入邮箱的“待审核草稿”文件夹中，严禁点击发送。
严禁拒绝、更改或新建任何日历日程。
文末以一页纸以内的篇幅汇报：今日概览、已归档数量、待审草稿列表，以及今天唯一一件必须由我做决定的事项。
```
:::

### 7. Puesto de gestión: Bot de jefe de gabinete y coordinación interdepartamental

Como centro neurálgico del equipo, se encarga de revisar el panorama general, detectar cuellos de botella y organizar la inspección semanal.

**Líneas rojas de permisos**
- Mantenerse en silencio si no hay avances en el negocio.
- **Queda estrictamente prohibido enviar mensajes en nombre de otros o mover tarjetas de tableros**, solo proporciona sugerencias y **jamás toma decisiones en lugar de los humanos**.

**Tareas y rutinas**
1. Primera tarea: revisar a fondo los registros de las últimas 24 horas en tableros y Slack, elaborando una **lista dinámica de atención** que incluya bloqueos, estancamientos y elementos pendientes de decisión.
2. Días laborables a las 18:00: compilar el informe vespertino.
3. Viernes a las 16:30: comparar los registros y resultados de cada bot dedicado, marcar tareas ineficientes y proponer optimizaciones o sugerencias de eliminación.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. Puesto de gestión: Bot de jefe de gabinete y coordinación interdepartamental
```text
每个工作日傍晚 18:00，审阅过去 24 小时内已批准的通讯频道 <slack_channels>、收件箱与项目看板 <board_url>。

提炼并输出以下四部分内容，篇幅严格控制在一页以内：
- 今日实质进展：提炼 5 行关键动态，说明关联系统与具体推进事项。
- 潜在风险预警：列出 3 项如果不做干预明天可能会恶化或延期的事情，说明阻碍人与卡阻天数。
- 待办决议选项：对于必须由我决策的事项，给出选项 A 与选项 B 的利弊对比，并附带你推荐的选项及一句理由。
- 日程减负建议：检查我明天的日历，挑出 1 个可以被取消或改为异步跟进的会议，并说明原因。

输出要求：
不发送任何外部消息，不修改任何会议日程，不挪动看板卡片。
若全天各项指标平稳且无异常阻塞，直接输出“今日运行平稳，无需要升级的决策事项”，不要为了凑字数生成冗余报告。
```
:::

## Colaboración entre puestos y casos prácticos de orquestación multibot

![Colaboración entre puestos y casos prácticos de orquestación multibot](/info/24-roles-s4.png)

El núcleo de la colaboración multibot se basa en el flujo de tickets de trabajo; **los humanos solo actúan aprobando en los nodos críticos**, sin convertirse en transportistas de copiar y pegar manualmente.

### Coordinación multipuesto en el equipo de producto de SpaceXAI

Movez detalló 9 puestos dedicados en SpaceXAI, incluyendo un jefe de gabinete, un supervisor, análisis de datos, reclutamiento y 5 bots de desarrollo.
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **Desacoplamiento de objetivos**: los humanos definen los grandes objetivos, mientras que el bot supervisor se encarga de desglosarlos y distribuirlos a los bots de desarrollo modular.
2. **Transferencia en cadena**: el bot de reproducción genera el paquete de validación y lo transfiere directamente; el bot de resolución implementa la corrección y abre un PR, **deteniéndose en el nodo de revisión de código (Code Review) humana a la espera de aprobación**.
3. **Alineación de estado**: el bot de jefe de gabinete mantiene una lista dinámica y, si detecta tarjetas sin commits durante varios días consecutivos, avisa al supervisor para que las revise.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Operaciones ligeras de expansión global para equipos independientes

CyrilXBT y Codez articularon un pipeline operativo diario con solo 3 bots.
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| Bot por puesto | Responsabilidades colaborativas | Supervisión humana |
|---|---|---|
| Bot de contenido | Monitorear dinámicas del sector y competidores, redactar artículos de blog y preparar borradores para distribución multicanal | - |
| Bot de prospección de ventas | Buscar clientes potenciales y puntuarlos, generando 20 borradores de correo cada mañana de un día laborable | **El responsable dedica 10 minutos por la mañana a revisarlos y aprobarlos** |
| Bot de soporte al cliente | Monitorear tickets y redactar sugerencias internas consultando la base de conocimiento | **Tras verificar que son correctas, se convierten en respuestas públicas con un solo clic** |

## Errores comunes a evitar

- No crees un bot comodín para tareas diversas: hacer que un solo bot gestione tanto reembolsos como publicaciones en redes provoca saturación de memoria y dificulta la resolución de problemas; **apégate al principio de asignar un bot específico para cada tarea**.

  [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- No actives tareas programadas antes del paso 6: ejecutar tareas programadas antes de afinar los mecanismos de reintento y reporte de errores solo generará bucles infinitos de fallos durante la noche.
- No confundas compartir una cuenta con aislamiento de sandbox: los bots bajo una misma cuenta comparten la computadora en la nube y el navegador; se deben configurar correos independientes, ramas dedicadas y tarjetas de compra, **quedando estrictamente prohibido vincular cuentas personales privadas críticas**.

  [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- No escribas normas a largo plazo en la ventana de chat: una vez finalizada la conversación, las reglas se desvanecen; los flujos y los límites deben especificarse en el campo de descripción (Description) del bot.
- No definas reglas de escucha demasiado laxas: configurarlo para que se active ante «cualquier mensaje nuevo» consumirá enormes cantidades de cuota en vano y provocará acciones erróneas fácilmente.

  [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- No omitas las alertas por datos faltantes: ante un error de API o campos ausentes, el bot tenderá a inventar o falsificar datos; debe quedar estipulado de forma rígida en sus normas: **si la fuente de datos falta o está desactualizada, debe reportar el fallo con total veracidad de inmediato, quedando estrictamente prohibido improvisar o hacer adaptaciones por cuenta propia**.

  [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

## Cómo evaluar y verificar los resultados

### Verificación instantánea en 30 segundos
En la primera tarea entregada por un nuevo bot, **la verificación humana debe poder completarse en un plazo de entre 30 segundos y 1 minuto**. Por ejemplo, pedirle al bot financiero que busque elementos faltantes en las primeras 5 filas de facturas, o al bot de ventas que evalúe 3 empresas designadas. Si requiere media hora para cotejar los datos originales, significa que el alcance de entrada es demasiado amplio o que los criterios de aceptación no son claros; descártalo y reestructúralo directamente.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Pruebas de estrés y barreras humanas
Antes de habilitarlo formalmente, introduce a propósito una instrucción de alto riesgo para realizar una prueba de estrés (por ejemplo, pedirle que gestione un correo de cobro y exigirle que pague de inmediato):
1. Observa si es capaz de **detenerse en estado de borrador y generar una tarjeta de aprobación**.
2. Si envía, fusiona o debita fondos por su cuenta sin haber obtenido aprobación, **revoca de inmediato los permisos de las herramientas y reescribe las restricciones de límites**.

### Verificación de los seis elementos antes de la activación
Antes de hacer clic en activar en la interfaz, verifica con claridad estas seis configuraciones básicas:
- Bot responsable asignado (Owning bot)
- Horario de activación y configuración de zona horaria (Schedule and time zone)
- Ruta de la fuente de entrada (Input source)
- Formato estructurado de salida esperada (Expected result)
- **Línea roja innegociable de aprobación humana (Approval boundary)**
- Política de reporte de errores ante cortes de red o datos faltantes (Missing data policy)

### Mecanismo de revisión semanal y recorte de puestos
Los cambios en el diseño web o en los campos pueden provocar que las rutinas fallen silenciosamente en segundo plano. **Dedica 15 minutos cada viernes por la tarde** a ejecutar el prompt de revisión semanal para que todos los bots del equipo informen de su estado:

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details Mecanismo de revisión semanal y recorte de puestos
```text
全体 Bot 成员，请按各自岗位汇报本周的运行情况：
1. 本周累计触发运行多少次，其中发生失败或报错的次数是多少？
2. 在运行过程中，有哪些步骤因数据缺失而跳过、重试或进行了推测？
3. 有哪些挂起等待审批的事项，我一直没有给出答复？
4. 本周生成的哪些文档或表格，我从未打开查阅过？

最后回答两个核心问题：
- 在本周的执行中，哪两个岗位之间存在明显的重复劳动？
- 综合目前的业务价值，你认为团队中哪一个例程或席位最应该被精简裁撤，理由是什么？
```
:::

Evalúa de forma continua tres métricas a largo plazo según los informes:
- **Horas de trabajo ahorradas reales**: compara con las operaciones manuales y calcula el tiempo efectivo realmente ahorrado.
- **Magnitud de modificaciones en los resultados**: si el volumen de correcciones humanas a los borradores sigue aumentando, indica una desviación de las reglas y requiere recalibración.
- **Determinación de la trayectoria de confianza**: para los puestos que, tras múltiples ajustes, sigan sin producir resultados estables, ciérralos o elimínalos con firmeza.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## Lecturas recomendadas

### Documentación oficial
- [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

### Casos prácticos de la comunidad
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
