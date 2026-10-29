# Capítulo 18 Caso de estudio: Empresa unipersonal y equipo de IA

**Todos los Bots bajo la misma cuenta comparten la misma computadora en la nube**, equipada con su propio navegador, sistema de archivos y terminal.

Crear una docena de Bots de golpe y entregarles todas las cuentas es una receta para caer en trampas:
- Rutas equivocadas en páginas web externas y sobreescritura silenciosa de datos.
- Aprobaciones frecuentes en mitad de la noche que agotan al revisor.

Al aclarar los límites del puesto, el aislamiento de credenciales y las líneas rojas de aprobación, es posible **evolucionar desde la configuración del primer empleado de IA hasta la gestión de 29 Agents**.

## El primer empleado de IA: definir puestos y permisos como en una contratación

![El primer empleado de IA: definir puestos y permisos como en una contratación](/info/18-solo-s1.png)

Tratar a un Bot como una herramienta o como un empleado depende de si estás escribiendo un prompt puntual o estableciendo responsabilidades de un puesto. Un prompt puntual solo se ocupa de una tarea inmediata; una vez que se cierra la ventana, el contexto desaparece. Las responsabilidades del puesto constituyen un archivo fijo que determina la línea base de comportamiento y el modelo de pensamiento del Bot al procesar asuntos cotidianos.

### Definición del puesto y pruebas de admisión

**No otorgues permisos irreversibles al principio**; comienza con tareas monótonas, frecuentes y fáciles de revertir.

Antes de poner al Bot a trabajar, ejecuta dos pruebas de admisión para detectar errores con anticipación:
1. **Prueba de responsabilidad en una sola frase**: explica en una sola frase qué debe entregar. Meter cuatro o cinco verbos no relacionados equivale a que una sola persona haga el trabajo de tres, y si algo sale mal, no podrás localizar la causa raíz.
2. **Simulación en texto puro (Trial in text)**: toma menos de dos minutos; primero reporta los pasos, las URL que prevé visitar y los juicios dudosos.

La descripción del puesto se desglosa en cinco campos para delimitar claramente las fronteras:
- Owns: Entregables fijos.
- Inputs: Canales cuya lectura está permitida.
- May: Operaciones que puede gestionar de forma autónoma.
- Must ask before: Acciones de alto riesgo como gastar dinero o modificar configuraciones; **deben esperar aprobación humana**.
- Done when: Lista de verificación de aceptación objetiva.

```text
先不要执行任何实际操作。请逐步向我推演你的完整执行方案：
1. 列出你准备依次打开的工具、网址与调用的插件。
2. 列出你在过程中需要做出的业务判断。
3. 标出你目前信息不足、存在疑虑或拿不准的决策点。
推演完毕后等待我的指令，严禁自行操作。
```

::: details Definición del puesto y pruebas de admisión
```text
岗位名称：收件箱管理员（Inbox Manager）
Owns：
每天上午梳理工作邮箱，归档垃圾邮件与订阅通讯，起草客户咨询的回复草稿，标出需要我决策的紧急邮件。
Inputs：
仅限于 Gmail 中收件箱的未读邮件与公司提供的常见问题回复模版。
May：
阅读邮件、按标签分类、打上处理标记、撰写回复草稿、归档无回复价值的宣传邮件。
Must ask before：
严禁直接点击发送任何邮件；严禁归档来自财务、法务或房东的邮件；如果邮件涉及转账、退款、重置密码或修改凭证，立即停下向我确认。
Done when：
工作日上午 9:00 前收件箱所有未读邮件分类完毕；生成的草稿不超过四句话，语气平实直接，不使用任何客套空话；所有待办事项单独列出截止日期。遇到不确定如何处理的邮件，保持未读并挂起询问，严禁自行猜测意图。
```
:::

La configuración del puesto es completamente diferente a los prompts temporales.

| Dimensión | Prompt temporal | Configuración del puesto |
|---|---|---|
| **Objetivo y forma** | Conversación única, enfocada en una sola acción | Configuración a largo plazo, entrega resultados de negocio |
| **Límites y permisos** | Las instrucciones verbales facilitan extralimitarse; si hay error se reinicia | Tareas reversibles autónomas; irreversibles esperan aprobación; barrera humana obligatoria |

### Período de prueba de tres ejecuciones y escala de promoción

> Fuente: [Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> Autor: [distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

Cuando un nuevo Bot funcione por primera vez, **nunca lo dejes desatendido en segundo plano de inmediato**; pruébalo primero según la «regla de las tres ejecuciones» de distort.

1. 1.ª vez (observación total): mira la pantalla en cada paso y anota malinterpretaciones de instrucciones, pérdidas de contexto y conjeturas a ciegas.
2. 2.ª vez (corrección de reglas): cambia a una tarea de dificultad similar sin recordarle los errores anteriores. Enfócate en si los cambios en las reglas del puesto y permisos surtieron efecto, sin corregir los resultados por él.
3. 3.ª vez (prueba real sin intervención): no intervengas en todo el proceso; actúa solo ante aprobaciones o al alcanzar el límite de reintentos, verificando el nivel de completitud, número de intervenciones, tiempo consumido y cuota.

**Tras superar las tres pruebas, ingresa en la escala de promoción**, dividida en cinco niveles de permisos.

| Nivel | Mecanismo | Límite |
| :--- | :--- | :--- |
| Level 0 | Solo observación | No modifica ningún dato |
| Level 1 | Solo preparación | Tareas reversibles como búsqueda, resumen y maquetación |
| Level 2 | Aprobación humana | Pasos críticos suspendidos a la espera de confirmación |
| Level 3 | Ejecución independiente | Ejecución programada o por disparador, generando reportes periódicos con cadena de evidencias |
| Level 4 | Colaboración multi-Bot | Actúa como nodo de distribución y control de calidad |

Para ascender al siguiente nivel, se deben cumplir cuatro **indicadores estrictos**:
- 5 ejecuciones reales consecutivas sin fallos
- Todos los pasos de verificación superados
- Sin efectos secundarios no resueltos
- Mecanismo de reversión (rollback) verificado y operativo

Para prácticas relacionadas, consulta [«Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort»](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) y [«Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez»](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg).

## De cero a una empresa operativa: Jefe de Gabinete y orquestación de equipos dedicados

Cuando una sola persona utiliza Grok Bot para construir un sistema operativo empresarial completo, el callejón sin salida más común es sobrecargar a un único Bot con demasiadas capacidades. Un Bot que gestiona clientes potenciales de ventas, redacta contenido, concilia cuentas y además modifica código verá su ventana de contexto rápidamente saturada de preferencias irrelevantes, lo que no solo confunde el contexto de negocio, sino que acelera el consumo de cuota.

### Arquitectura de Jefe de Gabinete y división departamental

Al crear un equipo, comienza construyendo un Bot Jefe de Gabinete (Chief of Staff). En el día a día, **solo interactúas con el Jefe de Gabinete**, y este se encarga de desglosar tareas, coordinar puestos dedicados y consolidar las entregas.

::: details Arquitectura de Jefe de Gabinete y división departamental
```text
你是一人公司的幕僚长（Chief of Staff），也是我日常沟通的唯一入口。
你的核心职责：
1. 接收我的业务目标，拆解为明确的工作阶段，派发给对应的专职 Bot（调研、内容、代码、运维）。
2. 在群聊中调度各岗位接力，跟踪各任务交付状态。
3. 检查专职 Bot 提交的产物是否符合完成标准，核对数据来源与执行录屏。
4. 每天晚上汇总团队进展，用不超过五行文字向我汇报核心结果、阻塞问题与需要我决策的审批项。
行为底线：
若无任何新进展或异常，保持静默；严禁越权代替专职 Bot 编写业务交付内容；严禁绕过人工审批直接执行外发、扣款或修改生产环境。
```
:::

- Bot de investigación: Las afirmaciones deben incluir fecha y URL; marcar dudas de forma proactiva; no inventar a la fuerza.
- Bot de contenido: Dar formato según plantilla; **queda estrictamente prohibido publicar directamente al exterior**.
- Bot de ventas: Guardar todos los correos de prospección en la bandeja de borradores; esperar aprobación humana antes de enviar.
- Bot técnico: Todo PR de GitHub debe adjuntar capturas de pantalla de pruebas superadas.
- Bot de finanzas: Cualquier ajuste de fondos debe listarse por separado para confirmación.

::: details Arquitectura de Jefe de Gabinete y división departamental
```text
团队总体目标：
在两周内针对新上线的知识库产品，完成竞品定价调研，产出一份对比简报，并根据简报结构生成 3 篇官网更新草稿。

协作规则：
1. 调研 Bot 先行检索 5 家竞品公开定价，生成包含引用网址的 Markdown 表格。
2. 调研完成后在群内移交给内容 Bot，内容 Bot 根据数据起草 3 篇文案，放入指定 Notion 页面。
3. 幕僚长全程跟进看板状态，若遇到数据缺失，要求责任 Bot 重新抓取或报错，不得擅自编造。
4. 全流程中所有涉及对外发布的操作全部挂起，等待我在看板中勾选通过。
```
:::

| Arquitectura | Todoterreno individual | Línea de producción con Jefe de Gabinete |
|---|---|---|
| Colaboración | Memoria mezclada difícil de rastrear | **Memoria independiente por puesto**, atribución precisa de responsabilidades |

### Revisión de la cadena de evidencias y transferencia de confianza en cuatro semanas

> Fuente: [From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> Autor: [NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**Para poder cerrar la laptop con tranquilidad, el requisito previo es ver las pruebas (Show the tape).** Las entregas del Bot deben incluir tres credenciales/evidencias:

- Grabación de pantalla o registros de invocación de operaciones: mostrar la trayectoria web completa o la secuencia de llamadas a herramientas.
- Fuente original de datos y cifras: prohibidas las citas sin procedencia.
- Explicación de elementos omitidos por error y conclusiones deducidas.

**La confianza se transfiere gradualmente a lo largo de cuatro semanas:**

1. Semana 1 (fase de borrador): El Bot solo redacta; el humano lee todo y ejecuta manualmente.
2. Semana 2 (fase de aprobación): El Bot se detiene en los pasos clave; el humano solo verifica las acciones y aprueba.
3. Semana 3 (fase de reporte de anomalías): Las tareas de bajo riesgo se ejecutan de forma autónoma; solo solicita ayuda si hay anomalías o intento de extralimitación.
4. Semana 4 (fase de inspección de rutinas): Ejecución totalmente autónoma según rutinas; los fines de semana solo se revisa el informe de auditoría.

Para prácticas relacionadas, consulta [«From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn»](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) y [«Grok Bot: How to Build Your First AI Team (Full Guide)»](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Práctica de empresa unipersonal: límites y operación independiente en una sola computadora en la nube

### Límites físicos

**Todos los Bots bajo la misma cuenta comparten una sola computadora**, utilizando los mismos directorios y sesiones. Oficialmente se especifica no considerar al Bot como una frontera de aislamiento: los prompts no evitan inyecciones y ejecutar comandos por error puede filtrar cookies y sesiones.

Respeta tres reglas básicas en todo momento:
- No inicies sesión en la banca electrónica principal ni en repositorios centrales, ni almacenes datos confidenciales en discos en la nube.
- En plataformas externas, utiliza únicamente subcuentas con privilegios mínimos.
- Los inicios de sesión externos deben realizarse mediante Handoff: el humano introduce la contraseña y el Bot solo hereda la Session.

### Automatización de sistemas sin API

**Los sistemas sin API dependen de las capacidades informáticas para hacer clics y rellenar formularios**; cuatro tipos de trabajo son idóneos para delegar primero:
- Prospección de clientes: Explorar directorios de comunidades y redactar correos.
- Seguimiento de entregas: Verificar desabastecimientos y rastrear envíos retrasados.
- Programación de contenido: Rellenar textos en la bandeja de borradores.
- Mantenimiento de código: Diagnosticar errores en sitios web independientes y generar parches.

::: details Automatización de sistemas sin API
```text
岗位名称：供应链履约跟踪员（Supplier Logistics Bot）
Owns：
每天上午 10:00 登录供应商门户，核对昨天未发货订单状态，提取物流单号，更新至运营表格。
Inputs：
供应商订货后台会话、本地待处理订单表格。
May：
在供应商后台查询订单状态、下载发货清单 CSV、更新本地表格对应列的运单号与发货时间。
Must ask before：
严禁点击「重新下单」或「取消订单」；严禁修改收货地址；若供应商后台提示账户欠款或商品缺货，停止处理并立即向我报警。
Done when：
所有处理过的运单在表格中均标注状态与回填时间；遇到后台页面改版导致按钮无法识别时，截取当前屏幕报错并退出，不得盲目重试。
```
:::

### Umbrales y puntuación

> Fuente: [One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> Autor: [ZER @zerqfer](https://x.com/zerqfer)

Solo cuando la **revisión humana se reduzca de forma estable a menos de 15 minutos al día** se deben añadir nuevos Bots, evitando multiplicar la carga. Completa una tarjeta de puntuación una vez al mes para prevenir el deterioro silencioso.

::: details Umbrales y puntuación
```text
Bot 月度运行评分卡
评估周期：2026 年 10 月
岗位名称：[例如：订单跟进助理]
1. 实际工时节省：本月相比纯手工操作，实际节省了约多少小时？
2. 人工介入程度：产出草稿中，需要人工手动大幅修改的比例是多少（低于 10% 算达标）？
3. 信任度变化趋势：对该岗位的自主执行信任度处于上升、持平还是下滑？
4. 异常与回滚记录：本月出现过几次页面识别错误或越权报警？
5. 处置结论：[保留继续运行 / 降级为人工审批执行 / 彻底停用删除]
```
:::

Consulta [«One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER»](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg).

## Sistema de entrega para AI Agency: línea de entrega mensual y barrera humana de control de calidad

![Sistema de entrega para AI Agency: línea de entrega mensual y barrera humana de control de calidad](/info/18-solo-s4.png)

Para una agencia de IA (AI Agency) que entrega a múltiples clientes, la principal dificultad radica en la estabilidad de la calidad y el control de costes de cuota ante la concurrencia de clientes.

El autor comunitario maestro compartió la arquitectura del sistema con la que una sola persona atiende a 5 clientes con cuota de retención (retainer) y mantiene la operativa mensual (el autor comunitario maestro afirma facturar 18 000 USD mensuales atendiendo a 5 clientes, no verificado).

### Las «tres pruebas de admisión» del menú de servicios

No aceptes proyectos totalmente a medida para no caer en la subcontratación manual; **para que un servicio entre en el menú de entrega automática, debe superar tres filtros**:

1. El brief se puede redactar como una lista estructurada.
2. El entregable cuenta con criterios objetivos de aceptación por parte de terceros.
3. **Haberlo entregado manualmente al menos 10 veces con anterioridad**. Sin haberlo hecho 10 veces no se conocen las líneas rojas, y delegarlo a un agente solo generará palabrería inútil.

Los servicios conformes incluyen comparar 40 documentos con un contexto de 500K para elaborar informes de investigación, redactar textos en lote a partir de archivos de muestra de voz (Voice File), o crear paneles de control y herramientas ligeras de extracción (scraping).

### Enrutamiento de modelos e intercepción del abismo de facturación de 195 000 Tokens

Asigna los modelos según la tarea; no recurras siempre al modelo insignia:
- Grok 4.1 Fast: Contexto de 2M, ejecuta limpieza y filtrado inicial.
- Grok Build 0.1: Responsable del 80 % de los materiales de desarrollo.
- Grok 4.6: 500K, ejecuta Agents de largo recorrido y razonamiento.

**Si la entrada supera los 200 000 Tokens, la tarifa se duplica de inmediato**. La pasarela debe **codificar un umbral estricto de 195 000 Tokens**, truncando o podando con error al excederlo.

### Revisor de solo lectura independiente y barrera humana tras tres reintentos

> Fuente: [How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> Autor: [maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

Cuando un Bot de producción revisa su propio producto tiende a la autovalidación, lo que oculta fácilmente fallos en los prompts. **La revisión debe dividirse en un circuito independiente de solo lectura**.

- Contexto independiente: introducir únicamente el brief original, las especificaciones del cliente y el producto final, sin proporcionar el razonamiento intermedio.
- Estrictamente de solo lectura: **al detectar defectos solo reporta FAIL y nunca reescribe**, evitando parches no autorizados que encubran problemas.
- Crítica adversarial: enfocada en detectar fallos graves; cualquier cifra no respaldada por datos se califica automáticamente como reprobada.

::: details Revisor de solo lectura independiente y barrera humana tras tres reintentos
```text
# 独立审查者审核准则（reviewer.md）
你是一名独立质量审查员，负责评估一份并非由你生产的交付产物。
你的唯一任务是找出交付物不符合客户要求的地方。你绝不需要去赞美它的优点。

输入物料：
原始需求 Brief、服务核对清单、客户品牌声音规范文件、最终交付草稿。
你未被提供、也严禁索取生产 Bot 的思考草稿。

审查规则（按顺序严格执行）：
1. 逐条核对需求 Brief 中的清单项。指出任何未被完全覆盖的要点。
2. 检查全文，严禁残留任何占位符文字、TODO 标记或括号说明文本。
3. 全文中的每一个具体数字、引文、统计百分比与人名，必须能在客户资料库中找到对应出处。发现任何未注明来源的数字，必须直接判定为 FAIL。
4. 语言风格是否符合客户过往已批准作品的语气标准。

输出格式：
第一行必须且只能输出一个词：PASS 或 FAIL。
如果判定为 FAIL，按以下格式列出所有缺陷：[清单条款] - [出现位置] - [具体问题及修正要求]。第一行后严禁输出任何空洞的总结段落。
若因上下文缺少凭据导致无法核验某一项，直接判定为 FAIL。
```
:::

```text
单任务自动化生产循环规则：
1. 生产 Bot 基于需求与声音规范生成第 1 版草稿。
2. 独立审核 Bot 执行审查。若返回 PASS，记录日志并进入待交付队列。
3. 若返回 FAIL，系统将审查不通过的具体原因拼接入下一轮 Brief，由生产 Bot 进行针对性修复重试。
4. 重试上限（MAX_ATTEMPTS）严格设定为 3 次。
5. 若连续 3 次均无法通过审查，系统立即终止自动重试，触发报警将原始 Brief、草稿与审查报错完整推送到人工桌面由人工兜底接管。
```

**El traspaso admite como máximo 3 reintentos**, evitando bucles infinitos que disparen elevadas facturas de Tokens. Si la máquina no cumple con los estándares tras tres intentos, indica un conflicto en los requisitos y un humano debe intervenir para decidir.

Consulta [«How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro»](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf).

## Práctica con 29 Agents: cómo expandirse sin fricciones desde un operador individual hasta una legión

![Práctica con 29 Agents: cómo expandirse sin fricciones desde un operador individual hasta una legión](/info/18-solo-s5.png)

Una vez familiarizado con la configuración de un solo empleado y el bucle cerrado de control de calidad con dos Bots, las demandas del negocio te impulsarán naturalmente a expandir el equipo.

El autor comunitario Melvin Vivas documentó su experiencia completa expandiendo gradualmente Grok Bot a 29 agentes dedicados (el autor comunitario Melvin Vivas afirma tener 29 Bots, no verificado).

### Distribución funcional y evolución progresiva de 29 Agents

**Estos 29 Bots surgieron orgánicamente según la necesidad**: al encontrar tareas repetitivas en el día a día, se creaba un rol dedicado, y cuando hubo muchos roles, la Jefa de Gabinete Emma pasó a coordinarlos. El negocio se divide en siete áreas clave:

- Centro de despacho: Emma se encarga de la gestión global y la distribución de tareas.
- I+D técnica: El CTO gestiona la arquitectura; **Coder coordina Cursor para escribir código automáticamente, crear PR y corregir errores**, todo sin necesidad de abrir un editor local.
- Investigación de vanguardia: Escanea las novedades de código abierto en la plataforma X durante todo el día y elabora resúmenes.
- Matriz de contenido: Responsable de la redacción de textos y análisis posteriores en varios canales.
- Desarrollo de negocio: Búsqueda de oportunidades comerciales y prospectos de colaboración.
- Operaciones y seguridad: Gestión de correos, copias de seguridad y revisiones de seguridad.
- Crecimiento personal: Registro de hábitos, seguimiento del mercado y fundamentación de decisiones.

### Línea de producción colaborativa multi-Agent: caso de conversión de prototipo técnico a contenido

Cada Bot toma el relevo apoyándose en la computadora en la nube compartida y en referencias de sesión.

::: details Línea de producción colaborativa multi-Agent: caso de conversión de prototipo técnico a contenido
```text
端到端跨团队协同案例：
1. 【情报捕获】：X 调研员监控到某大模型最新发布，抓取官方文档与代码仓库地址，整理为技术要点。
2. 【任务调度】：幕僚长 Emma 捕获该报告，根据设定规则判定该模型具备测试价值，自动将任务下发给技术团队。
3. 【工程交付】：编码员 Coder 接收技术说明，调起 Cursor Cloud coding agent 在云端编写 Google Colab 演示笔记本，推送到 GitHub 仓库并自动创建 Pull Request。
4. 【排错闭环】：执行测试出现依赖包版本冲突，终端 Traceback 自动返回 Coder，Coder 修复代码再次提交 PR 通过测试。
5. 【内容物料转译】：PR 合并后，Emma 将成功代码仓库与技术参数推送给内容创作团队，YouTube 脚本助手与 X 内容经理在半小时内完成多平台发布草稿，存入指定待审目录。
6. 【人闸闭环】：创始人全程不介入代码编写与格式排版，仅在最后核验 Colab 实际运行效果，并点击确认对外发布推文。
```
:::

**Para hacer cambios no es necesario abrir las 29 ventanas una por una**; una sola instrucción emitida por el supervisor se sincroniza en cuestión de segundos.

### Cinco señales para la división de roles y el método de automatización en siete pasos

Cuando los objetivos de evaluación, las herramientas invocadas, el estilo de trabajo, los límites de aprobación (los borradores y la comunicación externa jamás deben mezclarse) o los ciclos de programación difieren, es imprescindible **separar en un Bot independiente**.

1. Envía los objetivos, fuentes de datos, formatos y límites de parada al Bot para que los memorice; para Bots compartidos, escríbelo en el About de los detalles.
2. Elige una tarea real controlada para una sola ejecución.
3. Ajuste manual hasta alcanzar la exención de inspección.
4. Consolidar en una Skill reutilizable.
5. Reevaluar la generalización con nuevos datos.
6. **Activa la Routine solo tras definir el límite de reintentos y las alertas por omisión**.
7. Para enviar correos, realizar pagos o aplicar cambios, vincula obligatoriamente la barrera humana Require Approval.

| Fase | Escala | Arquitectura y cuello de botella |
| :-- | :-- | :-- |
| 1 Operador individual | 1 Bot | Bucle cerrado de verificación con barrera humana completa; requiere supervisión continua |
| 2 Grupo | 2-3 Bots | Separación de producción y revisión; mantenimiento diario reducido a 15 minutos |
| 3 Jefe de Gabinete | 4-6 Bots | Distribución y panel de control; **evitar que el Jefe de Gabinete realice tareas menores** |
| 4 Legión | 10-30 Bots | Standups multilínea; poda periódica de rutinas ineficaces |

### Sistema de paneles de control y mecanismo de reuniones diarias (standups)

> Fuente: [How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> Autor: [Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Cuando los Bots superan los 5, olvídate de usar múltiples ventanas de chat; es imposible seguirles el ritmo. **La colaboración multi-Bot depende principalmente de dos aspectos: paneles de control e inspecciones periódicas**:

- **Panel de estado compartido**: No dejes las tareas dispersas en el historial de chat; consolídalas en un panel de Notion o de base de datos con cinco estados definidos: `Todo`, `Working`, `Blocked`, `Ready for Review`, `Done`.

  Si el Bot encuentra un error desconocido o carece de permisos, cambia directamente la etiqueta a `Blocked` y solicita asistencia humana; en el día a día basta con observar el flujo de las tarjetas.
- **Inspección periódica y conciliación**: Cada Bot admite como máximo 50 Routines, ejecutándose a lo sumo cada 5 minutos.

  **A las 3:00 a. m. se revisan automáticamente enlaces rotos en el código y el tamaño de los paquetes, y a las 5:00 a. m. un Bot supervisor (como Jenny) revisa uno a uno el Playbook de los Bots dedicados**, lo que previene eficazmente que el modelo olvide con el paso del tiempo.

```text
全体专职 Bot，开始进行本周团队回顾审计。请各岗位汇报：
1. 本周你实际执行了多少次任务，其中失败或异常的中断有多少次？
2. 在执行过程中，有哪些步骤存在推测行为、跳过行为或由于数据缺失强行拼凑的情况？
3. 有哪些挂起的审批事项我一直没有回应？有哪些生成的物料我从来没有打开查看过？
4. 请指出：在当前的工作流中，你发现哪两个 Bot 存在职责重叠或重复工作？
5. 给出客观建议：为了节省整体用量额度，我们下周最应该裁撤哪一个无效的 Routine 或岗位？
```

Para prácticas relacionadas, consulta [«How I use Grok Bot: My team of 29 AI agents»](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh), [«GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez»](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54) y [«Grok Bot: How to Build Your First AI Team (Full Guide)»](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Errores comunes

### Permisos y aprobaciones
1. Las computadoras en la nube compartidas utilizan la misma Session sin aislamiento: **jamás inicies sesión en cuentas principales ni en sistemas sensibles**.
2. Require Approval solo bloquea operaciones no ejecutadas y no puede revertir daños: **establece una barrera humana estricta desde el primer momento para acciones de alto riesgo**.
3. Las solicitudes de aprobación expiran tras unos 10 minutos sin respuesta (Lapse): durante la noche **es imprescindible configurar listas blancas Allow rule o detenerse en fase de borrador**.

### Costes y arquitectura
4. Si la entrada supera los 200 000 Tokens, el precio unitario se duplica: **la capa de enrutamiento debe establecer una intercepción estricta y poda en 195 000 Tokens**.
5. No intentes que un solo Bot se encargue de todo ni clones 5 Bots genéricos: **una división poco clara del trabajo solo contaminará el contexto y desperdiciará cuota**.
6. No configures sondeos (polling) cada 5 minutos ni escuches todos los mensajes: **ante la falta de una No-data policy, las caídas de red facilitan la invención de datos y agotan la cuota**.

### Reglas y traspaso
7. Las indicaciones en la ventana de chat pierden efecto al refrescar: **las disciplinas inter-tareas deben quedar memorizadas por el Bot**; en Bots compartidos, escríbelas en el About de los detalles; los Bots personales ya no cuentan con Description.
8. Entre distintos Bots, no transfieras todo el historial: **el paquete de traspaso solo debe conservar el objetivo y la ruta de los entregables, junto con las conclusiones y los requisitos para el siguiente paso**.

## Cómo verificar una vez completado

1. **Verificar credenciales**: Elimina las credenciales bancarias y principales de Plugins y del navegador, sustituyéndolas por subcuentas o Sessions; **jamás almacenes contraseñas en texto plano en el historial de chat**.
2. **Validar puestos**: El Bot debe incluir Owns/Inputs/May/Must ask before/Done when, añadiendo una declaración contra la desviación al final; **ante la falta de datos, reportar error de inmediato y prohibir estrictamente inventar información**.
3. **Probar la barrera humana**: Envía instrucciones de cargo o eliminación; deben **activar al 100 % la suspensión por Require Approval**.
4. **Resistencia a auditorías**: Alimentar con un borrador de datos falsos; el Bot de control de calidad debe **devolver FAIL en la primera línea** sin realizar cambios por su cuenta; tras 3 fallos consecutivos, detenerse y lanzar alarma.
5. **Estabilidad de rutinas**: El estado del panel debe actualizarse en tiempo real; antes de activarlo, pulsa Test run para comprobar que funcione; **las tareas programadas no deben depender de aprobaciones nocturnas que tarden más de 10 minutos**.

## Lecturas complementarias

### Documentación oficial

- [Organizar negocios y trabajo en Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)
- [Colaboración y gestión de permisos de Bots para equipos](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Arquitectura de seguridad y entorno de ejecución de Grok Bot](https://cursor.com/cn/docs/grok-bot/security.md)
- [Planes, cuotas y detalles de facturación](https://cursor.com/cn/help/grok-bot/plans.md)
- [Configurar tareas programadas y rutinas de activación](https://cursor.com/cn/help/grok-bot/routines.md)
- [Conectar aplicaciones](https://cursor.com/cn/help/grok-bot/connect-apps.md)

### Fuentes prácticas de la comunidad

> Fuente: [GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> Autor: [Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- [«From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn»](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- [«How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro»](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- [«One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER»](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- [«GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez»](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- [«Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort»](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- [«Grok Bot: How to Build Your First AI Team (Full Guide)»](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- [«How I use Grok Bot: My team of 29 AI agents»](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- [«Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez»](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
