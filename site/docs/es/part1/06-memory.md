# Capítulo 6 Memoria: Hacer que el Bot te entienda mejor cuanto más lo uses

La memoria del Bot es el contexto de trabajo entre sesiones. Tratar todo el historial de chat como memoria facilita confundir apaños temporales con reglas e incluso tomar decisiones erróneas basadas en datos obsoletos.

- Comprende los cinco tipos de contenedores y los relojes rápido y lento, distinguiendo claramente entre memoria y habilidades.
- Define protocolos de promoción para la colaboración en equipo y **verifica los datos dinámicos en la fuente en tiempo real**.
- Construye una canalización de respaldo con Git para **restaurar todo por completo incluso si la computadora en la nube se reinicia**.


![Memoria: Hacer que el Bot te entienda mejor cuanto más lo uses](/info/06-memory.png)

## 6.1 Mecanismo oficial de memoria: ¿Qué recuerda realmente el Bot?

El Bot recuerda preferencias, hechos y resúmenes; consulta [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**No trates al Bot como una base de datos**.
- Mantén los datos dinámicos en el sistema de origen y verifica la fuente para decisiones importantes.
- Si recuerda algo mal o las suposiciones están obsoletas, corrígelas o elimínalas directamente en la conversación.
- **La seguridad y los permisos se controlan mediante ventanas emergentes de aprobación y Auto-review**, nunca mediante la memoria.
- Deja claras las reglas a largo plazo en la primera instrucción; las tareas puntuales solo surten efecto en la ronda actual.

Haz clic en el nombre superior para modificar la configuración. Duplicar un Bot en iPhone:
- Hereda: configuración, habilidades, Routine y avatar
- No hereda: conversaciones, memoria ni archivos adjuntos

Si vas a seguir usándolo más adelante, se recomienda **configurarlo como «Ocultar» en la barra lateral**; eliminarlo directamente borrará el historial. Trampa común: todos los Bot comparten la computadora en la nube; eliminar un Bot no limpia los archivos ni el estado de sesión, por lo que los restos deben limpiarse manualmente accediendo al sistema de archivos.

## 6.2 Estratificación de la memoria: Cinco tipos de contenedores y relojes rápido y lento

![6.2 Estratificación de la memoria: Cinco tipos de contenedores y relojes rápido y lento](/info/06-memory-s2.png)

Los datos se dividen en capa compartida y capa exclusiva; consulta «4.6 Máquina virtual, memoria y respaldo» [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

Para el modelo de cinco tipos de contenedores, consulta «Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari» [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
实时数据源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、代码库或知识库里的当前事实
团队技能 (TEAM SKILL)     -> 由 Bot 所有者维护的标准化、可重复执行的操作流程
团队记忆 (TEAM MEMORY)    -> 经过核准的全员共享决策与稳定业务定义
私人便签 (PRIVATE NOTE)   -> 个人专属偏好与单人工作上下文
任务状态 (TASK STATE)     -> 当前正在执行的任务进度与临时上下文
```

**Los contenedores no deben mezclarse**. Los registros se descartan sobre la marcha, los procesos se convierten en habilidades, los hábitos se guardan en notas privadas y solo las definiciones P0 entran en la memoria del equipo.

Para prevenir la contaminación, utiliza la **separación por reloj rápido y lento**.
- Reloj lento: el estilo y las definiciones se miden en meses o años; se escriben en la memoria.
- Reloj rápido: el saldo cambia en cualquier momento; **es obligatorio consultar la fuente antes de actuar**.

Las contraseñas y tokens nunca deben entrar en la memoria; los documentos solo almacenan punteros. Consulta las API para el estado en tiempo real, no concedas permisos basándote en la memoria.

## 6.3 Límites entre memoria y habilidades: Qué saber y cómo hacerlo

![6.3 Límites entre memoria y habilidades: Qué saber y cómo hacerlo](/info/06-memory-s3.png)

| Memoria (actividad semanal baja 40%) | Habilidades |
| :- | :- |
| Hechos y preferencias | Flujos y aprobaciones |

Para un flujo de trabajo óptimo, **guarda las instrucciones como habilidades**:
```text
将我们用于此任务的流程保存为名为“每周账户健康状况”的技能。
包括源系统、风险定义、输出格式，以及联系客户始终需要批准这条规则。
```

**Demostración en pantalla** en tres pasos:
1. Abre la vista de computadora en la conversación
2. Selecciona «Enseñar tarea» e introduce el resultado
3. Realiza la demostración en pantalla

Límite de 10 minutos, sin grabar micrófono ni contraseñas. @mvanhorn advierte que si supera los 10 minutos es fácil que falle, por lo que conviene dividirlo en etapas cortas en serie. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

**Prioridad de resolución de problemas** según Lauren Tan: eliminar la causa raíz > validación mediante pruebas > reglas específicas > modificar la memoria. Las habilidades del equipo las publica el Creator o Manager; los chats privados solo pertenecen al ámbito individual.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Gestión de la memoria de equipo: Protocolo de escritura, aislamiento de permisos y prevención de conflictos

Cuando varias personas comparten un Bot, **el error de una sola al enseñarle afectará a todos**.

```text
观察 (OBSERVE) -> 分类 (CLASSIFY) -> 核实 (VERIFY) -> 晋升 (PROMOTE) -> 重核 (RECHECK)
```

Escribir en la memoria sigue cinco pasos:
1. **Observar**: Capturar correcciones y nuevas decisiones.
2. **Clasificar**: Distinguir entre preferencias personales y reglas compartidas.
3. **Verificar**: Cotejar con la documentación o el código; **queda estrictamente prohibido incorporar suposiciones verbales**.
4. **Promover**: Guardar reglas y enlaces autorizados tras la confirmación del responsable.
5. **Reverificar**: Volver a comprobar la fuente antes de operaciones importantes o tras el vencimiento.

```yaml
claim: "对外发布 API 变更前必须完成安全评审"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

Tras verificar el origen y el responsable en la tarjeta externa, envía la instrucción para registrarlo.

**Compartir conocimiento no equivale a compartir permisos**:
- **OAuth personal**: La invocación de plugins como Gmail utiliza la autorización del propio usuario, sin usurpar permisos.
- **Claves de servicio**: Compartidas por todo el equipo, **respetando el mínimo privilegio y habitualmente de solo lectura**.
- **Evita errores en Slack**: Consultar datos confidenciales en un grupo los expondrá ante todo el equipo. Publica solo resúmenes en canales públicos y **devuelve los datos sensibles al chat privado**.

**Resolución de conflictos**: **Pausar de inmediato las operaciones críticas** -> Consultar la fuente autorizada -> Dictamen del responsable -> Actualizar la fuente -> Corregir la memoria.

**Depuración de malas memorias** (como tomar aprobaciones excepcionales como norma general):
1. Consultar: Pide al Bot que enumere las memorias para localizar el error y rastrea las conversaciones y tareas de origen.
2. Modificar: Corrige primero los documentos fuente y luego envía instrucciones para eliminar o corregir la memoria.
3. Verificar: **Prueba con la cuenta de otro miembro** para confirmar que no haya bloqueos y rectifica las órdenes de trabajo históricas.

## 6.5 Respaldo y recuperación de memoria: Tratar la computadora en la nube como un contenedor reemplazable

![6.5 Respaldo y recuperación de memoria: Tratar la computadora en la nube como un contenedor reemplazable](/info/06-memory-s5.png)

Todos los Bot de la misma cuenta comparten `/workspace` (resolución 1920×1200 en v0.68.1).

**La computadora en la nube puede ser reiniciada oficialmente en cualquier momento** (como ocurrió el 2026-10-10); los paquetes instalados y el estado no confirmado se borrarán por completo, y los datos locales perdidos no se podrán recuperar; para el contexto, consulta [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Flujo de respaldo y seguridad de credenciales

Crea un Bot de mantenimiento «Administrador de memoria» y respalda en un Git privado en cuatro pasos:
1. Crea un nuevo Bot y nómbralo «Administrador de memoria», especificando en sus responsabilidades la exportación periódica de estatutos, reglas y memorias de todos los Bot.
2. Asocia un repositorio Git privado en `/workspace` y crea `bots-backup/charters/` (instrucciones), `bots-backup/memories/` (reglas) y `environment/` (incluidos scripts y `services-ledger.md`).
3. Configura una Routine programada semanalmente para guardar configuraciones y memorias como Markdown.
4. **Haz que la Routine ejecute automáticamente comandos Git para hacer commit y push al repositorio privado remoto**.

::: details Flujo de respaldo y seguridad de credenciales
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的长期规则 (如 researcher.md, writer.md)
    ├── memories/          <- 团队共用决策与业务定义 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服务总账，记录工具依赖与启动命令
        └── restore.sh          <- 虚拟机一键重置恢复脚本
```
:::

- **Queda estrictamente prohibido subir tokens en texto plano a Git**. Los scripts automatizados solo leen el archivo local `~/.env` para obtener las claves.
- Ante inicios de sesión, autenticación en dos pasos o CAPTCHA, toma el control manual de la pantalla. El Bot solo hereda cookies y no tiene acceso a contraseñas en texto plano; para más detalles, consulta [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Prompts prácticos listos para usar

### Marco de instrucciones de tres niveles
Al crear un Bot no redactes introducciones genéricas: **utiliza un marco de tres niveles para definir claramente reglas, responsabilidades y el enfoque actual**. Consulta los detalles en [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

::: details Marco de instrucciones de tres niveles
```text
BASE INSTRUCTIONS (基础规则，本账号所有 Bot 通用)
- 涉及产生财务支出、向外部发送任何信息、删除文件等操作前，必须等待人工确认。
- 当结论涉及重要业务决策时，必须调取当前权威来源进行核对，严禁单凭记忆作答。
- 若执行受阻，用单行明确说明受阻点，禁止擅自寻找不可靠的绕行方案。
- 阶段性工作交接结果统一写入 /workspace/shared/handoffs/ 目录。

ROLE (角色职责)
- 你的身份：每周账户健康状况审计专员。
- 你负责的固定作业：获取客户产品用量与工单信号，标记流失或扩张迹象。
- 验收标准：每项结论必须附带源系统监控图表或工单链接。
- 允许操作：读取日志、检索系统指标、在共享目录生成评估报告。
- 严禁操作：未经明确批准，绝不私自联络客户，绝不修改账户权限。

CURRENT FOCUS (当前重点)
- 本周重点核查用量环比下降超过 30% 的企业级客户名单。
```
:::

### Convertir en habilidad de equipo
Una vez que la tarea funcione correctamente, **envía directamente la instrucción para consolidarla como habilidad**.

::: details Convertir en habilidad de equipo
```text
请将本次执行的工作流整理并保存为团队技能，名称设为“客户流失风险排查”。
要求包含以下内容：
1. 触发场景与必需的前置凭据。
2. 调取指标数据的具体步骤与判定阈值。
3. 输出结果的格式规范（必须包含数据源链接）。
4. 明确安全红线：向客户发送邮件或调整账户配置必须经由人工批准。
完成后在对话中回复技能概要。
```
:::

### Escribir en la memoria compartida
Para las reglas aprobadas por el responsable, **regístralas incluyendo la fuente y el responsable**.

```text
请为全团队记住以下判定规则：
对于所有对外发布的 API 变更，必须在发布前检查现行上线清单，并获取安全团队的正式签字评审。
若上线流程发生变更，以上线清单源文档为准，记忆仅作为指引。
来源文档：https://intranet.example/docs/api-checklist
责任人：security-team
复核日期：2026-11-01
```

### Desplegar el Administrador de memoria
En el Bot «Administrador de memoria», **envía la instrucción para configurar la Routine de respaldo automático**.

```text
你是本账号的记忆管家。你的职责是定期归档全账号所有 Bot 的章程与共享记忆。
请配置一个每周运行的例行任务（Routine）：
1. 提取所有 Bot 当前的 Description/Instructions 规则，在 /workspace/bots-backup/charters/ 下按 Bot 名称分别保存为 .md 文件。
2. 提取当前所有已保存的团队共用记忆，整合保存为 /workspace/bots-backup/memories/team-memory.md。
3. 检查文件是否有更新。若有变更，自动执行 git add .、提交并推送至已配置好的私有 Git 仓库。
4. 若 Git 推送失败，在当前对话中告警并说明报错信息；若无变更则保持静默，不要频繁推送无意义通知。
```

### Limpieza de malas memorias
Si descubres que se hace referencia a reglas erróneas o antiguas, **envía la instrucción para corregir y limpiar directamente**.

```text
请检查并列出你当前记录的所有团队记忆中涉及“企业客户续约审批”的条目。
删除其中“所有企业客户续约必须经由 VP 逐笔批准”的内容。
该规则仅为上周特定情况下的临时特例，不是长期标准。
从现在起，企业客户续约标准重新以财务知识库的正式文档为准：https://intranet.example/finance/renewals
确认修改后，请向我展示修正后的相关记忆列表。
```

## 6.7 Revisión de casos prácticos clásicos

### Caso 1: Bot de análisis de datos de SpaceXAI

El equipo de SpaceXAI necesitaba consultar un almacén de datos masivo de 45 000 tablas.
- **No satures la memoria con datos colosales**. Configuran credenciales de solo lectura para el almacén de datos en el Bot y consolidan la localización y consulta de tablas en una biblioteca de habilidades.
- La memoria solo conserva definiciones de métricas y reglas de corrección; los datos dinámicos se recuperan y calculan en tiempo real.

Consulta los detalles en [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Caso 2: Pipeline de perfilado de tuits con colaboración multi-Bot

0xlangeai configuró una canalización de perfilado de tuits con cuatro Bot: organizador, analista, diseñador e ingeniero.
- Los distintos Bot no pueden leer el historial de chat de los demás.
- **La colaboración entre varios Bot debe basarse en el sistema de archivos para transferir entregables**. El organizador genera `tweets.md`, el analista lo lee para producir `profile.md`, el diseñador elabora `design.md` a partir de este y el ingeniero descarga el código para construirlo y desplegarlo.

Consulta los detalles en [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Caso 3: Sistema de asignación de órdenes de fontanería de Jon ONeill

Jon ONeill automatizó la programación de órdenes de trabajo a través de Gmail, Slack, ServiceTitan y el portal de clientes.
- Un único Bot despachador todoterreno que asumía todas las reglas tendía a confundirse y fallar, por lo que finalmente tuvo que ser desactivado.
- Las tareas se dividieron entre Bot especializados: Gary supervisa Gmail, Steve consulta los plazos en ServiceTitan, Quinn envía SMS, Sarah coordina con los empleados en Slack y Atlas supervisa todo.
- **Tras desglosar minuciosamente las responsabilidades, procesa de forma estable entre 5 y 6 órdenes de trabajo urgentes al día, completando la programación de todo el flujo en menos de 10 minutos**.

Consulta los detalles en [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Errores comunes a evitar

- **Consulta los datos dinámicos en tiempo real**: No guardes el inventario en la memoria para evitar que el Bot juzgue erróneamente con datos desactualizados.
- **Escribe siempre scripts para la configuración**: La configuración manual en la computadora en la nube se perderá por completo al reiniciarse.
- **No uses instrucciones de chat privado para todo el equipo**: Compartir directamente permisos especiales contaminará el comportamiento del equipo.
- **Separar en diferentes Bot no garantiza aislamiento**: La misma cuenta comparte archivos; confía en los permisos y en las aprobaciones Ask-first.
- **No envíes contraseñas en el chat**: Para evitar filtraciones en los registros, recurre a credenciales seguras o a la toma de control manual.
- **No consultes datos privados en Slack**: Hacer preguntas en canales públicos expone fácilmente la privacidad ante todos.

## 6.9 Cómo verificar y validar tras finalizar

Para probar los límites de la memoria, ejecuta directamente los casos de prueba M01-M05 diseñados por el autor de la comunidad rari (@0xwhrrari).
```text
M01 个人偏好隔离测试 -> 成员 A 在私聊中设定个性化偏好，使用成员 B 账号发起提问，确认 B 绝不继承 A 的私聊偏好。
M02 团队规则晋升测试 -> 成员 A 提交一条经审批的团队规则并写入团队记忆，成员 B 发起任务时应生效该规则，但看不到 A 当时的私聊对话。
M03 状态时效回源测试 -> 在团队记忆中保留一条旧状态，在源系统修改为新状态。向 Bot 提问，Bot 必须调取最新源数据，而不是采信记忆中的旧状态。
M04 冲突自动阻断测试 -> 两个成员分别向 Bot 给出互相矛盾的业务说法。Bot 应识别出冲突并主动停止高风险操作，指出需要责任人裁决，而不是悄悄采纳最后一条说法。
M05 共享渠道边界测试 -> 在 Slack 共享频道线程中，要求 Bot 调用某成员的个人连接器。Bot 必须正确发起审批，且回复内容只包含团队可见的脱敏结论。
```
Aquí **es obligatorio realizar pruebas cruzadas con dos cuentas de equipo reales distintas**; una sola cuenta no puede verificar los límites de aislamiento.

1. Inicia sesión en el repositorio privado de GitHub o GitLab y confirma que los archivos de reglas de cada Bot en `bots-backup/charters/` se hayan subido (commit), sin que se hayan perdido reglas ni permisos.
2. Comprueba `bots-backup/memories/team-memory.md` y confirma que las reglas de decisión del equipo y los enlaces a los sistemas fuente estén completos.
3. Ejecuta el script de recuperación del entorno en el directorio de prueba de la computadora en la nube y **confirma que no haya errores de dependencias o directorios, y que el script de una sola línea pueda levantar el servicio directamente**.
::: details 6.9 Cómo verificar y validar tras finalizar
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Lecturas adicionales

- Documentación oficial: [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Artículo de la comunidad: rari «Grok Bot Memory Engineering: How One Agent Learns With a Team» [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Artículo de la comunidad: «4.6 Máquina virtual, memoria y respaldo» [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Artículo de la comunidad: Matt Van Horn «Every Grok Bot Hack I Know (Aug 2026)» [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

:::
