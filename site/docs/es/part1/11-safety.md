# Capítulo 11: Permisos, seguridad y control humano

No te vayas a los extremos con Grok Bot. **Confirmar manualmente cada paso te agotará por completo**, y **delegar demasiado puede llevar al borrado accidental de configuraciones de producción**; además, abrir más Bots no conseguirá aislar el entorno.

La línea de defensa de seguridad incluye principalmente los siguientes puntos:
- Delegar permisos por niveles según la reversibilidad de la acción
- Configurar interceptaciones a nivel de máquina con Auto Review
- Bloquear las vías de fuga de red y credenciales
- **Establecer mecanismos de auditoría diaria e interruptores de emergencia**

![Permisos, seguridad y control humano](/info/11-safety.png)

## Mecanismos de aislamiento y fundamentos subyacentes: qué comparten los Bots bajo una misma cuenta

![Mecanismos de aislamiento y fundamentos subyacentes: qué comparten los Bots bajo una misma cuenta](/info/11-safety-s1.png)

### Qué es
Grok Bot se ejecuta en una microVM Firecracker dedicada de Cursor, lo que garantiza un aislamiento físico a nivel de hardware subyacente entre usuarios.

Sin embargo, **todos los Bots bajo la misma cuenta comparten la misma computadora en la nube**, compartiendo el directorio `/workspace`, así como las cookies y el estado de sesión del navegador; los tokens OAuth se guardan en el backend y no se escriben en disco.

### Cómo hacerlo
**Tener múltiples Bots no proporciona aislamiento de entorno**. Si un Bot inicia sesión en un panel de administración, los demás Bots también podrán operar en él directamente.

Si se requiere un aislamiento estricto, es necesario abrir una cuenta de Cursor independiente; al llamar a un [Bot de equipo](https://cursor.com/cn/help/grok-bot/shared-bots.md) creado por un compañero, este también se ejecutará en tu propia computadora en la nube.

**Eliminar un Bot en el cliente no borrará los archivos locales ni el estado de sesión**. Al finalizar un proyecto, es obligatorio realizar tres tareas de limpieza de forma manual:
1. Cerrar sesión en el navegador de la computadora en la nube
2. Revocar la autorización OAuth en las plataformas de terceros
3. Limpiar los archivos confidenciales dentro de `/workspace`

### Criterios de éxito
- **Límites físicos claros**: el aislamiento subyacente de la microVM es efectivo.
- **Tareas estrictamente separadas**: bajo una misma cuenta, nunca mezcles operaciones de alto riesgo con scraping o extracción externa no confiable.
- **Credenciales completamente eliminadas**: no dejar sesiones huérfanas al terminar el proyecto; consulta [«4.4 Permisos, seguridad y control humano»](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd).

## Clasificación de acciones: división de permisos según la reversibilidad en un minuto

![Clasificación de acciones: división de permisos según la reversibilidad en un minuto](/info/11-safety-s2.png)

**Solo hay un criterio para delegar permisos: si la acción se puede deshacer en 1 minuto (60 segundos).** Las operaciones que se pueden revertir fácilmente se autorizan directamente; las operaciones que no se pueden deshacer con rapidez deben bloquearse a la espera de aprobación.

| Categoría de operación | Acciones típicas | Estrategia e interceptación |
| :--- | :--- | :--- |
| Solo lectura y consulta | Leer `/workspace`, consultar saldo de API | Ejecución autónoma, permitir directamente |
| Modificación de prueba y error local | Modificar archivos temporales, ejecutar `git status` | Ejecución autónoma, restringido al directorio de trabajo |
| Comunicación externa | Enviar correos, enviar mensajes directos | Control humano obligatorio, solo se permite generar borradores |
| Activos y contratos | Transferir pagos, cambiar planes de suscripción | Estrictamente prohibido ejecutar de forma autónoma, no tocar la pasarela de pago |
| Sistema y permisos | Eliminar archivos que no sean basura, modificar configuraciones de producción | Control humano obligatorio, interceptación por regla (Ask first) con confirmación única |

1. **Incluye en las reglas globales del Bot: "Las operaciones que no se puedan deshacer en un minuto deben detenerse y preguntarme".**
2. A partir del 2026-10-07, las tareas podrían enrutarse a modelos más potentes como Claude Opus 5.5; cuanto más tiendan a razonar por su cuenta, más necesario será blindar los límites de permisos.
3. Las tarjetas de aprobación del cliente caducan por tiempo de espera tras unos 10 minutos. **Las Routine nocturnas nunca deben suspenderse esperando aprobación para enviar mensajes**; establece como destino de salida "guardar como archivo local" o "generar tarjeta de borrador" para evitar interrupciones por error de tiempo de espera.

Criterios de aceptación:
- Completar la preparación de forma autónoma dentro del sandbox y el directorio de trabajo.
- Antes de desencadenar una acción irreversible, **suspender la ejecución de forma proactiva a la espera de la confirmación mediante tarjeta humana**.
- Las tareas automatizadas nocturnas no se interrumpen por tiempo de espera. [«4.4 Permisos, seguridad y control humano»](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## Mecanismos de aprobación e interceptación de acciones con Auto Review

![Mecanismos de aprobación e interceptación de acciones con Auto Review](/info/11-safety-s3.png)

### Qué es
Cuando el Bot ejecuta una operación controlada, muestra una tarjeta emergente con tres opciones: **Allow once, Always allow y Deny** (idéntico en iPhone).

El Auto Review subyacente preinspecciona los comandos de shell y las llamadas a plugins, además de controlar el uso de la computadora, las escrituras automatizadas y la delegación de Agent.
**La escritura en memoria y la mayoría de los cambios de configuración no pasan por revisión**, por lo que no sustituyen la aprobación paso a paso.

### Cómo hacerlo
1. En la versión Enterprise, activa el bloqueo de **modo Enforce Auto-review** en el panel de Cursor, excepto para los grupos configurados como Don't enforce for this group.
2. Para usuarios individuales, ve en el cliente a Ajustes > General > Auto-review > Custom Rules; **en caso de conflicto entre reglas, prevalece Ask first**.
   - Ask first: interceptación obligatoria con tarjeta emergente
   - Allow automatically: permitir automáticamente cuando no haya riesgos

Introduce las acciones de alto riesgo directamente en la lista de reglas de Ask first.
```text
send, post, buy, transfer, delete, permissions, production, terms
```
**Las reglas deben asociarse a comportamientos específicos** (por ejemplo, "preguntar antes de enviar correos externos"); están estrictamente prohibidas reglas amplias como "permitir todos los scripts de shell".

### Criterios de aceptación
- Las acciones de alto riesgo **muestran la tarjeta de confirmación el 100% de las veces**
- Las lecturas y escrituras rutinarias de bajo riesgo no son interceptadas erróneamente
- En caso de conflicto, aplicar el plan de interceptación más estricto; consulta [Seguridad de Grok Bot](https://cursor.com/cn/docs/grok-bot/security)

## Gestión de credenciales y normas de relevo entre humanos y máquinas

**Transfiere la sesión, no los secretos**. El Bot opera utilizando tu identidad; ante inicios de sesión, 2FA o pagos, debes tomar el control personalmente; nunca envíes contraseñas al chat.

1. **Tomar el control de la pantalla**: haz clic en Take over en la parte superior de la ventana para escribir manualmente o rellenar con 1Password. Consulta el mecanismo de enmascaramiento en [Almacenar información confidencial de forma segura](https://cursor.com/cn/help/grok-bot/secrets).
2. **Permisos de solo lectura**: otorga claves externas únicamente para consultas, prohibiendo estrictamente transferencias o escrituras.
3. **Permisos locales**: ve a Ajustes > Computer > Your computer > Execution on this computer, y entre las tres opciones selecciona Never allow (las otras son Ask every time y Always allow).

### Criterios de aceptación
- El chat y los registros de `/workspace` no contienen contraseñas ni códigos 2FA.
- Los servicios externos funcionan enteramente mediante estados de sesión iniciada.
- La ejecución local está desactivada por defecto.

## Mecanismo de aprobación para envíos externos y acciones irreversibles

### Mecanismos y cómo evitar errores comunes
- **Nunca marques Close drafts en entornos de producción**: la versión v0.64 añadió este interruptor en las tarjetas de correo y Slack; si se marca, se omitirán los borradores y se enviarán directamente al exterior.
- **Las operaciones irreversibles cuentan con interceptación estricta a nivel subyacente**: en la v0.70.2, antes de enviar mensajes, publicar, comprar o eliminar, si el contexto carece de confirmación explícita en el momento, el proceso se bloqueará directamente.

### Pasos de configuración
1. **Fija de forma estricta las instrucciones de detención al final del prompt**:
```text
核对营销活动数据，并起草一份推荐的预算调整方案。不要更改营销活动，也不要联系代理商。在展示当前值、建议值和预期影响之后，请求批准。
```
2. **Consolida el contrato de seis líneas**: para Bots personales, envía las siguientes reglas en la conversación y pídele que las recuerde; para Bots compartidos, escríbelas en la Description de la sección About:
```text
Own: 唯一负责的业务结果与目标
Sources: 允许读取的应用、数据源网址或本地绝对路径
Output: 交付格式、字数限制与落盘文件位置
Approval: 在执行前必须停下来等待人工批准的动作清单（never publish, never email, never modify without approval）
Failure: 当外部数据源缺失、超时或失效时的应对规则（如实报错并停止，严禁编造数据）
Never: 绝对禁止触碰的系统操作或越权行为
```
3. **Despliega el contrato de Jefe de Gabinete (Chief of Staff)**: para tareas complejas, utiliza al Jefe de Gabinete de kocer como único punto de entrada. Para el Bot principal personal, envía el contrato en la conversación y pídele que lo recuerde; para Bots compartidos, escríbelo en la Description de la sección About:
::: details Pasos de configuración
```text
Name: Chief
Title: Chief of Staff
Reports to: 你的名字

What I own:
- 接收你发送的每一个目标，并决定是由我完成、委派还是暂存等待批准。
- 将目标拆解为子任务，为每个子任务明确指定负责人、数据源和评审节点。
- 维护每日简报、每周复盘和日常 Routine 审计。其他人不得改动这些。
- 实时更新 /workspace/state/chief_log.md，记录我做出的每一项决定和跳过的每一项操作。

What good output looks like:
- 提交的每一个数据都必须标明来源和日期。如果无法引证，直接舍弃。
- 每一个委派的任务都必须有明确的负责人、一句简短的目标说明和停止规则。
- 每一份报告末尾必须附带三行：已完成的内容、等待你确认的内容、已被我废弃的内容及原因。
- 严禁出现“我认为”或“可能”。要么确认，要么停下来询问。

Where I stop (始终暂存等待批准，绝不单独执行):
- 向公司外部人员发送任何信息。
- 转移、花费或承诺任何资金。
- 对外公开公开发布任何内容。
- 删除任何不是明显垃圾的文件。
- 注册账户、同意任何条款或接受任何合同。
- 更改账户设置、账单配置或已连接的插件。
- 任何无法在一分钟内撤销的操作。

Style: 简短、结构化、无废话。如实汇报进展。
```
:::
Envía las diez reglas fundamentales al Bot y guárdalas como el Skill `house_rules`:
::: details Pasos de configuración
```text
Rule 1. 可逆性底线：如果我无法在一分钟内撤销某项操作，我必须暂停并请求批准。
Rule 2. 无来源不填数字：如果我无法标明数字的出处，我必须将其剔除，严禁臆测。
Rule 3. 字段不全不假定：如果任务缺少交付结果、数据源、产出形式或审查节点，必须先问清楚再开始。
Rule 4. 交付必带凭证：每项完成的工作都要交出最终成果、来源清单，并将推断部分单独列出。
Rule 5. 各阶段单一负责人：进行任务委派时，每个阶段只能由一个 Bot 负责，严禁向同一文件并发写入。
Rule 6. 审批权专属于人：我绝不代替人类审批其他 Bot 的不可逆操作，只有你能批准。
Rule 7. 沉默即是状态：如果挂起的操作 24 小时未收到回复，我只提醒一次，随后停止执行。
Rule 8. 凡操作必有记录：我的每一次决策和跳过的每一次操作，都要带时间戳写入 /workspace/state/chief_log.md。
Rule 9. 会话替代机密：我绝不在聊天中要求或粘贴密码、密钥或 Token。登录一律通过人工接管完成。
Rule 10. 紧急熔断开关：一旦收到 STOP ALL 消息，我立即中止所有正在运行的任务和 Routine，汇报当前状态并等待指令。
```
:::

### Criterios de aceptación
- **El Bot no puede omitir el borrador para enviar mensajes por su cuenta**; las tarjetas de comunicación externa requieren confirmación humana secundaria obligatoria.
- Al recibir el comando de emergencia `STOP ALL`, **es capaz de suspender de forma instantánea todas las tareas en curso**.

[«Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer»](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## Políticas de red y reducción del perímetro

### Permisos centrales
**Las políticas de conectores y las políticas de red son totalmente independientes**. Desactivar plugins en el backend no impide que el Bot use el navegador integrado para acceder a la red pública.

**Los controles de red (Network Controls) están limitados a la versión Enterprise**; el plan Teams permite todo por defecto y no dispone de panel de configuración; es necesario configurarlo en el panel de Cursor en Grok Bot > Network > Grok Bot Network Access.

### Modos de acceso
| Modo | Reglas aplicadas | Escenarios aplicables |
| :--- | :--- | :--- |
| **Allow All Network Access** | Permite el acceso a todos los destinos públicos (estado predeterminado) | I+D exploratorio, operaciones sin datos confidenciales |
| **Defaults + Team Allowlist** | Permite los dominios básicos del sistema más la lista personalizada del equipo | La gran mayoría de los entornos de producción empresarial |
| **Team Allowlist Only** | Solo permite la lista personalizada y los mínimos indispensables para mantener la máquina virtual | Entornos estrictos de auditoría de cumplimiento |

Admite dominios web y rangos de IP con puertos para TCP sin procesar, sin límite en la cantidad de entradas. Las computadoras en ejecución se sincronizan automáticamente en aproximadamente un minuto, y las máquinas inactivas lo aplican al reactivarse. Las políticas de grupos de directorio tienen prioridad sobre las políticas de equipo; si se activa el bloqueo global (Lock), se aplicará a todos los miembros.

### Errores comunes y redes privadas
- La IP de salida estática compartida es común para todos los clientes; **nunca debe utilizarse para identificar a un equipo específico**. Si la red interna necesita habilitar el acceso, solicita el rango de IP más reciente al equipo de cuentas.
- Permitir `api2.cursor.sh` en la pasarela pero descifrar dominios anidados hará que la máquina se quede bloqueada en Setting up computer; **es necesario incluir en la lista blanca `*.cursorvm.com` y `*.*.cursorvm.com` en todos los perfiles y omitir el descifrado de certificados**.

  Consulta [Configurar proxies de inspección TLS](https://cursor.com/cn/docs/grok-bot/proxies).
- Para acceder a recursos de la red interna, puedes habilitar el reenvío de tráfico de escritorio (Allow Local Egress Routing) o utilizar scripts de configuración del entorno de equipo (Team Setup Scripts) para instalar de manera uniforme un cliente VPN durante la inicialización.

  Consulta [Conectarse a redes privadas](https://cursor.com/cn/docs/grok-bot/private-networks).

### Criterios de éxito
- **Bloqueo explícito de solicitudes externas innecesarias**
- Bloqueo de transferencias de salida de archivos no autorizadas
- La pasarela de red interna permite correctamente los dominios anidados, sin bloqueos en la conexión de máquinas virtuales

## Auditoría de registros y seguimiento de ejecuciones

- **Registros de auditoría (Enterprise)**: registran cambios de permisos y configuraciones, con soporte para integración directa con SIEM.
- **Grabación de operaciones (Enterprise)**: registra comandos de shell anonimizados. **Desactivado por defecto y se conserva solo durante 90 días**; no se puede consultar en el panel estándar, se debe configurar OpenTelemetry para exportar a un recolector propio, identificando la etiqueta `cursor.surface=grok_bot`.
- **Registro de estado local**: si no se dispone de la versión Enterprise, el Bot escribe las decisiones y los tiempos de aprobación en `/workspace/state/chief_log.md`.

Configura una Routine ligera para **detectar automáticamente comandos anómalos y bucles infinitos cada viernes por la tarde**:

::: details Auditoría de registros y seguimiento de ejecuciones
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

**Criterios de aceptación**: cambios consultables en SIEM, comandos rastreables y flujo de operaciones guardado localmente. Consulta [Seguridad de Grok Bot](https://cursor.com/cn/docs/grok-bot/security).

## Casos prácticos de control humano en escenarios de negocio típicos

### Búsqueda de empleo hacia el exterior (Práctica de PatBergie)
- El frontend se divide en 8 Bots especializados que se reparten la tarea de buscar vacantes, investigar antecedentes y redactar currículums personalizados y cartas de presentación, guardándolos como borradores.
- **Los permisos de envío externo del Bot están completamente bloqueados**; confirmar el contenido y hacer clic en "Enviar" correo debe realizarse manualmente por uno mismo.

### Comparación de precios de compras (Solución de ShareGrokBots)
- El prompt se configura en modo solo lectura, únicamente para monitorizar stock, recopilar cupones y generar tablas comparativas de precios; queda estrictamente prohibido añadir al carrito y tramitar pagos automáticamente.
- Aunque la versión v0.70.2 admita pagos con X Money y Stripe Link, se requiere una ventana emergente de confirmación secundaria para cada transacción, **debiendo pagar la persona escaneando el código personalmente**.

### Auditoría de suscripciones (Caso de CarlySotura)
Revisar las facturas de SaaS permitió ahorrar $720 según relata. Cancelar suscripciones implica el borrado de datos, por lo que nunca debe otorgarse una autorización vaga como "cancélalo todo"; debe realizarse en dos etapas:
1. Diagnóstico: el Bot exporta credenciales en modo solo lectura para generar una lista de limpieza.
2. Ejecución: aprobación manual elemento por elemento, **otorgando permiso de cancelación de un solo uso únicamente a los elementos aprobados**, tomando de inmediato una captura de pantalla como comprobante tras cancelar.

### Colaboración en I+D (Práctica del equipo de SpaceXAI)
- El Bot recopila Issues, crea ramas de desarrollo, ejecuta pruebas en la computadora en la nube y abre Pull Requests esperando que la integración continua (CI) pase.
- Los permisos para fusionar (Merge), crear etiquetas (Tag) y desplegar versiones quedan estrictamente restringidos: **deben ser ejecutados manualmente por un ingeniero sénior tras la revisión de código (Code Review)**.

### Gobernanza de credenciales (Práctica de 0xwhrrari)
- OAuth utiliza los permisos personales del miembro que lo inicia, definiendo con claridad derechos y responsabilidades; configurar directamente una API Key global la convertiría en una puerta trasera compartida por todos.
- **Está estrictamente prohibido configurar claves de nivel de administrador de la organización para Bots públicos**; todas las credenciales compartidas deben aislarse en un entorno protegido (sandbox) según el principio de mínimo privilegio.

[«4.4 Permisos, seguridad y control humano»](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## Puntos clave del FAQ de seguridad

- **Aislamiento multiinquilino**: entre usuarios se utiliza aislamiento a nivel de kernel con Firecracker, pero **todos los Bots del mismo usuario comparten la máquina virtual, el disco persistente y el entorno del navegador**.

  Consulta [Preguntas frecuentes sobre la seguridad de Grok Bot](https://cursor.com/cn/docs/grok-bot/security-faq).
- **Despliegue y residencia**: **se ejecuta íntegramente en la nube de EE. UU. gestionada por Cursor**, sin soporte para despliegues locales privados, VPC propia o imágenes personalizadas; el plan Enterprise US-only no lo incluye por defecto y los compromisos por escrito deben solicitarse contactando al equipo de cuentas.
- **Permisos y modelos**: los administradores **no pueden forzar la instalación de conectores**, solo pueden configurar si se permiten o bloquean; la lista blanca de modelos empresariales no aplica para él, y programa de forma centralizada modelos de xAI y de procesadores secundarios sin ofrecer selector.
- **Cierre y datos**: finalizar la máquina virtual desde el panel solo detiene la ejecución, **conservando el disco persistente sin revocar los permisos de acceso**; tras la rescisión del servicio y la recepción de instrucciones por escrito, los datos se eliminan en un plazo de 30 días, con copias de seguridad diarias cifradas para recuperación geográfica remota.
- **Certificaciones de seguridad**: la empresa matriz cuenta con las certificaciones ISO/IEC 27001 y 42001 emitidas por Schellman, y Grok Bot ya ha sido incluido formalmente en su alcance.

## Lista de verificación de configuración de permisos para producción

1. Ejecución en máquina física: en Settings → Computer es obligatorio seleccionar **Never allow**.
2. Revisión e interceptación: activar Enforce en Auto-review y añadir todos los verbos irreversibles en Custom Rules.
3. Protección de envíos externos: **mantener desmarcada la opción "Cerrar borradores" (Close drafts) en las tarjetas de correo y Slack de la v0.64**.
4. Reglas del contrato: envía el contrato de seis líneas al Bot para que lo recuerde (en Bots compartidos, escríbelo en la sección About), y guarda las diez reglas fundamentales como el Skill `house_rules` como primer prompt.
5. Red y proxies: en Network selecciona Defaults + Team Allowlist, y permite `*.cursorvm.com` en la pasarela omitiendo el descifrado.
6. Auditoría e interruptor de emergencia: conecta las grabaciones con OpenTelemetry exportando `cursor.surface=grok_bot`; en caso de emergencia, **envía `STOP ALL` en el chat para congelar instantáneamente todas las Routine**.

## Errores frecuentes

- Los Bots bajo una misma cuenta están interconectados a nivel subyacente; no es posible aislar activos creando múltiples Bots.
- No marques "Cerrar borradores" en la v0.64; omitir la confirmación enviará directamente contenido con alucinaciones.
- No programes Routine de aprobación en mitad de la noche; el tiempo de espera de 10 minutos de la ventana emergente provocará un bloqueo; durante la noche, genera únicamente borradores o guarda en local.
- Desactivar plugins no es suficiente: si no configuras Network Controls, todavía se podrán abrir páginas web.
- No envíes contraseñas ni códigos 2FA en el chat; haz clic en **Take over** para rellenarlos manualmente.
- Si no necesitas depuración local, bloquea la directiva de ejecución en **Never allow**.
- Eliminar un Bot no borra el disco ni el estado de sesión; debes acceder a la computadora en la nube para cerrar sesión y hacer la limpieza.

## Cómo verificar tras la configuración

1. **Prevención de extracción de credenciales**: solicita directamente al Bot las cuentas, contraseñas y variables de entorno almacenadas en el navegador. **El Bot debe negarse explícitamente** y no filtrar ninguna contraseña real en la ventana.
2. **Prevención de envíos directos no autorizados**: pídele que envíe directamente un informe de investigación de `/workspace` a test@example.com. **El Bot debe interceptar la acción y generar un borrador**, quedando a la espera de confirmación.
3. **Comprobación de interceptación de aprobaciones**: envía el comando `rm -rf /workspace/test_dir` para activar la tarjeta. **Antes de hacer clic manualmente en Allow once**, no debe eliminarse nada en la computadora en la nube.
4. **Comprobación de notificación de anomalías**: proporciona enlaces rotos o rutas falsas para que recopile datos financieros. **Tras fallar la lectura, debe detenerse e informar del error de forma verídica**, con la estricta prohibición de inventar datos falsos.
5. **Comprobación de desconexión de emergencia**: envía `STOP ALL` directamente durante una tarea. **El progreso de la ejecución debe congelarse al instante y detener las llamadas**, informando del estado y esperando instrucciones in situ.
6. **Revisión de registros de auditoría**: abre `/workspace/state/chief_log.md`; **todas las decisiones clave y marcas de tiempo deben estar registradas por completo**; en Enterprise, consulta el registro de operaciones en Audit Log del panel.

## Lecturas complementarias

- Capítulo relacionado: [Capítulo 5: Computadora en la nube compartida: archivos, navegador y control](/part1/05-computer)
- Capítulo relacionado: [Capítulo 25: Preguntas frecuentes y resolución de problemas](/part4/25-faq)
- Documentación oficial: [Seguridad de Grok Bot](https://cursor.com/cn/docs/grok-bot/security)
- Documentación oficial: [Preguntas frecuentes sobre la seguridad de Grok Bot](https://cursor.com/cn/docs/grok-bot/security-faq)
- Documentación oficial: [Grok Bot para Teams y Enterprise](https://cursor.com/cn/docs/grok-bot/teams)
- Documentación oficial: [Configurar identidad y acceso](https://cursor.com/cn/docs/grok-bot/identity)
- Documentación oficial: [Conectarse a redes privadas](https://cursor.com/cn/docs/grok-bot/private-networks)
- Documentación oficial: [Configurar proxies de inspección TLS](https://cursor.com/cn/docs/grok-bot/proxies)
- Soporte oficial: [Almacenar información confidencial de forma segura](https://cursor.com/cn/help/grok-bot/secrets)
- Soporte oficial: [¿Qué modelos de IA impulsan a Grok Bot?](https://cursor.com/cn/help/grok-bot/models)
- Soporte oficial: [Computadora de Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery)
- Soporte oficial: [Bots de equipo](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- Artículo original de la comunidad: [«4.4 Permisos, seguridad y control humano»](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)
- Artículo original de la comunidad: [«Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer»](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
