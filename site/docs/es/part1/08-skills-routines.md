# Capítulo 8 Habilidades y rutinas: convertir un éxito puntual en una ejecución diaria automática

No configures programaciones directamente. **Sin supervisión humana es fácil que se bloquee, se ejecute por error a las tres de la madrugada y gire en vacío agotando la cuota de toda la semana.**

Consolida las operaciones en habilidades (Skill) y organízalas en rutinas (Routine):
1. Calibra la zona horaria y estandariza los Webhooks.
2. Limita el alcance de activación en Slack.
3. Añade una verificación en dos fases en la máquina virtual.

**Establece límites claros para que, incluso al cerrar el ordenador, se siga entregando en segundo plano de forma estable.**


![Habilidades y rutinas: convertir un éxito puntual en una ejecución diaria automática](/info/08-skills-routines.png)

## Consolidación y referencia de habilidades: fija tu procedimiento operativo estándar

![Consolidación y referencia de habilidades: fija tu procedimiento operativo estándar](/info/08-skills-routines-s1.png)

Las habilidades son instrucciones operativas guardadas en la cuenta, y **todos los Bots bajo tu cuenta pueden invocarlas directamente**.

### Cómo consolidar habilidades

**Método 1: Resumen de texto tras la conversación**
Una vez que la tarea funcione correctamente, no cierres la conversación todavía; pide directamente al Bot actual que la sintetice y guarde. El prompt debe especificar con claridad las fuentes de entrada, el manejo de excepciones y los límites de acción; envía directamente esta plantilla.

::: details Cómo consolidar habilidades
```text
请把我们刚刚完成的这套流程保存为名为“每日工单异常审查”的技能。
技能内容必须包含以下要素：
1. 适用场景：工作日审查支持渠道中滞留超过 4 小时的工单。
2. 输入数据：从已连接的工单插件中读取状态为 Open 且优先级为 High 的列表。
3. 决策规则：若工单包含退款申请且金额大于 500 元，标记为一级风险；其余标记为二级跟进。
4. 交付格式：生成 Markdown 表格，列出工单编号、客户标识、滞留时长、风险等级与跟进建议。
5. 异常处理：若工单系统接口无响应或无符合条件的数据，输出明确说明，严禁使用历史缓存或伪造数据。
6. 安全边界：未经人工明确批准，严禁直接调用接口回复客户或变更工单状态。
```
:::

**Método 2: Demostración práctica (Teach task)**
Cuando la operación en la interfaz sea compleja, hacer una demostración directa resulta más práctico.
1. Abre la vista previa del ordenador en la parte derecha de la ventana de chat y selecciona "Enseñar tarea" (Teach task).
2. Describe brevemente el objetivo y opera en el ordenador en la nube. **El sistema graba un máximo de 10 minutos de pantalla y no graba audio del micrófono; no introduzcas contraseñas ni otra información confidencial; las credenciales sensibles deben gestionarse mediante tarjetas seguras**.
3. Tras generar automáticamente el borrador, **es obligatorio completar las reglas de decisión, los errores y los límites de aprobación; bajo ningún concepto lo pongas en producción directamente**. Si no ves el punto de acceso, significa que aún está en fase de despliegue gradual; utiliza el Método 1.

### Cómo referenciar y gestionar habilidades

- **Referencia en el cuadro de entrada**: Escribe una barra diagonal `/` en el cuadro de entrada para seleccionar y cargar la habilidad.
- **Habilitar permisos**: Si no la encuentras en la lista, ve a "Aplicaciones conectadas" (Connected Apps) en la barra lateral del escritorio, haz clic en el número de conexiones y activa el interruptor en "Habilidades privadas".

### Qué nivel se considera aceptable

| Elemento de comprobación | Redacción deficiente | Redacción adecuada |
| :--- | :--- | :--- |
| Fuente de entrada | "Analiza los datos recientes" | Especifica claramente complementos, endpoints de API, rutas de archivo o vistas de base de datos |
| Control de límites | "Si surge algún problema, actúa según veas" | Interrumpe y reporta el error de inmediato ante la falta de datos; queda terminantemente prohibido inventar información |
| Permisos de acción | "Ayúdame a enviar el informe al cliente" | Genera un borrador y déjalo en el chat, **espera la autorización humana antes de enviarlo** |
| Estructura de salida | Texto largo libre | Lista de campos fija, tabla Markdown o ruta de guardado en disco |

Fuente: [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)

## Mecanismos centrales de las rutinas: configuración, visualización y pruebas

![Mecanismos centrales de las rutinas: configuración, visualización y pruebas](/info/08-skills-routines-s2.png)

Las rutinas son desencadenadores de flujos de trabajo asociados a un Bot y se ejecutan en el directorio `/workspace` de un Linux en la nube. **Incluso si cierras el ordenador o sales del cliente, las tareas en la nube avanzarán según lo previsto.**

### Especificaciones y limitaciones

- Cada Bot puede crear hasta 50 rutinas como máximo; el sistema conserva los registros de las últimas 20 ejecuciones.
- El intervalo mínimo de activación para las rutinas programadas es de 5 minutos; no admite programación a nivel de segundos.
- **Eliminar una rutina es irreversible**, y las ejecuciones posteriores finalizarán definitivamente; eliminar un Bot borrará todas sus rutinas asociadas.

Fuente: [《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### Creación y gestión de rutinas

En la versión de escritorio, envía una instrucción directamente en el cuadro de chat para crearla:

```text
每个工作日上午 8:30，调用“每日工单异常审查”技能，在此对话中输出审查清单。如果未检索到高风险工单，只发一行“今日无高风险工单”即可，不要刷屏。
```

Gestión en la versión de escritorio:
1. Haz clic en el nombre del Bot en la parte superior de la ventana de chat para entrar en Details; en la lista de rutinas (Routines) podrás ver el tiempo de ejecución o Paused, y el interruptor de la derecha permite pausar (Pause) o reanudar (Resume) en cualquier momento.
2. Al hacer clic en una rutina específica, puedes consultar tres propiedades: Instruction (prompt de ejecución), When to run (descripción de la programación) y Webhook (URL exclusiva, clave y encabezados de solicitud).
3. La barra de herramientas inferior ofrece Test, Edit y la papelera roja (Delete routine). **Al hacer clic en Edit, se rellenará automáticamente en el diálogo "Edit your routine: [nombre de la rutina]"**; completa con los cambios deseados y envía para actualizar.

Gestión en la versión móvil:
1. Abre la página de perfil del Bot para encontrar las rutinas; al pulsar Add routine, se autorrellenará "Set up a routine to "; completa la instrucción y envíala para crearla.
2. Pulsa en una rutina existente para consultar Schedule, Next run e Instruction; también puedes ver el interruptor Active y el historial de ejecuciones (Run history).
3. **Desactivar el interruptor Active pausará la rutina, y deslizar la fila hacia la izquierda permite eliminarla directamente.** El estado se sincroniza en tiempo real de forma bidireccional con la versión de escritorio.

Fuente: [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)。

### Programación de horarios y configuración de zona horaria

Ruta para comprobar la zona horaria: Settings -> Bot -> Timezone.

| Modo | Mecanismo de funcionamiento | Consideraciones |
| :--- | :--- | :--- |
| Auto-detect | Sigue automáticamente la zona horaria del ordenador actual | Adecuado para ubicaciones fijas; los viajes internacionales pueden provocar cambios imprevistos en la hora de ejecución |
| Zona horaria manual | Selección manual de la zona horaria correspondiente en el menú desplegable | Recomendado para regiones específicas (como la hora de Pekín UTC+8 o la hora del este de EE. UU. EST) |

- **Una rutina programada recién creada no se ejecutará de inmediato por primera vez**; debe esperar al siguiente punto programado. Por ejemplo, si a las 8:05 de la mañana configuras una ejecución diaria a las 8:00, la primera ejecución será a las 8:00 de la mañana siguiente.
- **Si se requieren inspecciones continuas los fines de semana, debe enfatizarse explícitamente en la instrucción: "ejecutar todos los días, incluidos los fines de semana".** Salvo indicación expresa, el Bot se ejecuta de lunes a viernes por defecto.

Fuente: [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)，[《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### Probar rutinas

En la página de detalles de la versión de escritorio, haz clic en el botón Test en la parte inferior para activarla manualmente; el estado del botón cambiará a Running…, y el resultado de la ejecución aparecerá directamente en la ventana de chat.

**La prueba realiza operaciones reales**: iniciará el navegador del ordenador en la nube, modificará archivos del espacio de trabajo y descontará cuota con normalidad; si implica eliminar o modificar, prueba primero con datos de prueba/sandbox. **Si aparece el mensaje Couldn't start a test run, es necesario comprobar el estado de conexión del ordenador en la nube o si hay tareas previas bloqueando.**

Fuente: [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)。

## Desencadenadores Webhook y Slack: de la consulta periódica (polling) al despertar pasivo

![Desencadenadores Webhook y Slack: de la consulta periódica al despertar pasivo](/info/08-skills-routines-s3.png)

Hacer polling programado de páginas web externas consume muchísima cuota, y girar en vacío a alta frecuencia agotará rápidamente la capacidad de cómputo de toda la semana. **Cambia a un modelo impulsado por eventos para despertar al Bot**: permanece completamente inactivo de forma habitual y se activa pasivamente solo cuando hay cambios externos.

A partir del 2026-10-12, Grok Bot se integra en el sistema The X Subscription, compartiendo el fondo de cuota con Grok y Cursor:

| Nivel de suscripción | Precio | Multiplicador de uso | Compatibilidad con Bot |
| :--- | :--- | :--- | :--- |
| Premium | $30 al mes o $300 al año | 4 veces el uso base | Incluye Bot |
| Super | $100 al mes o $1000 al año | 15 veces el uso | Incluye Bot |
| Ultra | $200 al mes o $2000 al año | 50 veces el uso | Incluye Bot |
| Plus | - | - | No incluye Bot |

### Configuración de Webhook y verificación asíncrona

Envía una instrucción en la ventana de chat para que el Bot cree un desencadenador Webhook.

```text
为当前 Bot 创建一个 Webhook 触发的例程，命名为“外部知识接收端”。
指令内容：读取请求体中的 JSON 数据，提取 url 和 note 字段，将其抓取整理为 Markdown 存入 /workspace/notes 目录。
```

Abre los detalles de la rutina en la versión de escritorio y despliega Webhook para ver los campos principales:
1. POST to: URL pública única para recibir solicitudes externas.
2. key: Clave privada de autenticación; al invocar, se debe incluir `Authorization: Bearer <key>` en el encabezado de la solicitud.
3. header: Texto completo concatenado del encabezado de la solicitud; haz clic para copiarlo directamente.

**Es obligatorio hacer clic en Save para guardar la configuración; solo entonces surtirá efecto en la pasarela y generará la clave.** Si la página de detalles se queda bloqueada y no se abre, pide al Bot que te envíe el enlace directo.

[《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

Los sistemas externos envían datos mediante solicitudes POST, incluyendo directamente el cuerpo de la solicitud en JSON.

```json
{
  "url": "https://example.com/article/1024",
  "source": "ios_share",
  "note": "精读核心论点并归档"
}
```

El Bot tomará el JSON como variable de contexto y lo enviará al modelo junto con la Instruction preestablecida. [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)

- **HTTP 200 solo representa que la pasarela ha recibido la solicitud con éxito y ha iniciado la ejecución; no garantiza que la tarea se haya completado con éxito.** El éxito o fracaso operativo debe comprobarse en la ventana de chat o en los archivos guardados en el espacio de trabajo.
- Una respuesta distinta de 200 indica que la tarea no se ha creado, normalmente porque la rutina está en estado de pausa (Paused) o la clave no es válida. [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)

### Desencadenadores de Slack y prevención de consumo desmedido de cuota

El complemento de Slack es una herramienta de lectura y escritura invocada en tiempo real durante la conversación; el desencadenador de Slack es una condición de inicio de rutina, y antes de usarlo se debe completar la autorización en la integración de la cuenta de Cursor.

Envía una instrucción en lenguaje natural para configurar la escucha.

```text
创建一个 Slack 触发例程：当 #incident-response 频道中有人发消息提及 @bot 且包含短语 "needs repro" 时，在云电脑上拉取报错日志并尝试复现。不要监听其他频道，也不要在没有该短语时响应。
```

Se admiten cuatro tipos de escucha: mención al Bot, coincidencia de palabras o frases específicas, adición de reacciones con emojis o recepción de cualquier mensaje.

- **Está terminantemente prohibido escuchar cualquier mensaje en canales públicos**; las conversaciones informales y los mensajes cotidianos activarán coincidencias constantes, consumiendo la cuota de toda la semana en un solo día.
- Debe vincularse a un único canal dedicado; no selecciones "todo el espacio de trabajo".
- Ajusta las condiciones de filtrado tanto como sea posible, por ejemplo limitándolas a prefijos específicos o enlaces a incidencias.
- Los desencadenadores solo se aplican a los nuevos mensajes posteriores a su creación; los mensajes históricos no se procesan retrospectivamente. [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)

## Casos prácticos de automatización: tres pipelines típicos

### Caso 1: Entrada directa a la base de conocimiento desde el móvil con un toque (Atajos de iOS + Webhook)

El autor de la comunidad 铁柱 (@cgnot996) configuró un flujo de archivado. Al ver un artículo técnico o un vídeo en el móvil y pulsar la opción de compartir del sistema, Grok Bot extrae automáticamente el texto completo, resume los puntos clave y lo estructura en formato Markdown guardándolo en `/workspace/knowledge/inbox.md`.

Configúralo siguiendo estos pasos:
1. **Crear una nueva rutina en la nube**: En Grok Bot, crea una nueva rutina "Archivado de conocimiento móvil", selecciona Webhook como condición de activación y obtén la URL de POST exclusiva y el encabezado Authorization.
2. **Escribir la instrucción de procesamiento**: Configura la instrucción para recibir la URL entrante y abrirla en el navegador del ordenador en la nube; si es un vídeo, extrae la transcripción; tras analizarlo, extrae el título y las etiquetas según el formato, organiza los puntos clave y los enlaces relacionados, y añádelos al final de `/workspace/knowledge/inbox.md`.
3. **Crear el atajo en el móvil**: Abre la app "Atajos" en el iPhone y crea uno nuevo, activa "Mostrar al compartir" y selecciona "Páginas web y texto" como tipo de entrada aceptada.
4. **Añadir el nodo de solicitud**: Añade la acción "Obtener contenido de URL", selecciona `POST` como método, introduce la dirección de destino del Webhook en la URL, añade el encabezado `Authorization` con el valor `Bearer [你的私钥]`, selecciona `JSON` en el cuerpo de la solicitud y vincula `url` a "Entrada del atajo".
5. **Resolver limitaciones al compartir**: Aplicaciones como las cuentas oficiales de WeChat no pueden abrir directamente el panel de compartir con atajos. **Crea un atajo adicional de "puente por cuadro de texto" vinculado al Botón de acción (Action Button)**, ábrelo para pegar el enlace en la ventana emergente y luego reenvíalo al Webhook.

**El móvil solo realiza la captura ligera de parámetros y el envío HTTP, mientras que la pesada extracción de contenidos y maquetación se delegan por completo a la nube para ejecutarse de forma asíncrona.** De este modo, el móvil no consume batería ni te obliga a esperar, permitiéndote salir en pocos segundos.

Fuente: [《Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)，[《4.3 触发器与自动化：定时、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### Caso 2: Inspección en dos fases en máquina virtual y optimización extrema de cuota

El autor de la comunidad 铁柱 (@cgnot996) optimizó las 6 tareas rutinarias del Bot "Director de Marketing". Cambió las inspecciones de seguimiento de respuestas de xAI y la revisión diaria de PRs —que consistían puramente en esperar cambios— por comparaciones ligeras, despertando al modelo solo cuando hay avances reales, ahorrando entre 8 y 10 ejecuciones innecesarias en vacío por semana.

Las tareas se dividen en dos categorías:

| Tipo de tarea | Representantes típicos | Estrategia de programación y características operativas |
| :--- | :--- | :--- |
| Entrega obligatoria a una hora fija | Informe diario de SEO, informe mensual de autoridad/posicionamiento | Genera un informe completo a la hora prevista para revisión humana; conserva la programación temporal nativa |
| Espera pasiva de cambios a una hora fija | Monitorización de actualizaciones en páginas, comprobación de nuevas PR | El giro en vacío programado descuenta cuota; es necesario cambiarlo a una verificación ligera |

La implementación se realiza en cuatro pasos:
1. **Desplegar un centinela local**: Escribe un script minimalista local en la máquina virtual Linux donde corre Grok Bot, ya sea en Python o Bash, sin invocar en absoluto al modelo de lenguaje.
2. **Configurar la comparación programada**: Usa el temporizador `cron` integrado de Linux para ejecutar el script cada media hora en días laborables. El script solo compara el hash de la página web o consulta la API de GitHub para verificar el número de PRs, tardando unos segundos y sin consumir cuota de suscripción de Grok.
3. **Implementar el despertar por diferencias**: **Solo cuando la comparación detecta un cambio sustancial, el script ejecuta `curl` para realizar una llamada POST al Webhook.**
4. **Intervención y resolución por parte del modelo**: Tras despertarse, el Bot comienza a leer el código del PR o el contenido de la respuesta, organiza las recomendaciones de decisión y envía notificaciones.

El juicio mecánico se delega a los scripts locales, y el modelo solo se despierta cuando se requiere capacidad de razonamiento. Así se evita consumir en vano el contexto del modelo de lenguaje para un simple "hoy no ha ocurrido nada".

Fuente: [《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。

### Caso 3: Monitorización diaria del riesgo de pérdida de clientes (churn)

El equipo oficial y el autor melvindvivas, quien opera 29 Bots, utilizan esta solución para monitorizar cambios y anomalías en los clientes. Cada mañana se extraen automáticamente las métricas de uso y los tickets de soporte para generar una lista de observación de alerta temprana, bajo estricto control en todo momento.

La implementación se realiza en cuatro pasos:
1. **Establecer el contrato y estatuto del rol**: Crea un Account Risk Bot dedicado, envía el contrato de reglas en la conversación y haz que lo recuerde (en el caso de Bots compartidos, escríbelo en el About de los detalles), definiendo umbrales de riesgo claros. Por ejemplo, que el volumen de llamadas a la API caiga más del 40% durante tres días consecutivos y vaya acompañado de incidencias P1 sin resolver.
2. **Configurar la tarea de extracción programada**: Configura una rutina que se ejecute a las 8:00 de la mañana en días laborables para extraer periódicamente las métricas de los sistemas de origen.
3. **Configurar el mecanismo de disyuntor (circuit breaker)**: **Si se agota el tiempo de espera de conexión con el almacén de datos o la información no está lista, reporta directamente el motivo del fallo por ausencia de datos; queda terminantemente prohibido hacer suposiciones con la instantánea de ayer y está estrictamente vetado mostrar datos no verificados.**
4. **Establecer una compuerta de aprobación humana de seguridad**: En Custom Rules dentro de Settings, configura el envío de correos, la modificación de campos del CRM y la distribución de listas como "Preguntar primero" (Ask first). La lista elaborada por el Bot solo se muestra silenciosamente en la ventana de chat, a la espera de que el gestor de cuentas la verifique y haga clic manualmente en la tarjeta de aprobación.

**La automatización de alto valor no debe delegar todo el poder al modelo: al otorgar capacidad de ejecución, es indispensable añadir contratos de límites y compuertas humanas.**

Fuente: [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)，[《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## Guía de resolución de problemas con rutinas

### Llegó la hora programada, pero el Bot no responde en absoluto
- En Details de la versión de escritorio, confirma que no esté en Paused; en la versión móvil, confirma que Active esté activado. **Si llevas mucho tiempo sin iniciar sesión y expira el tiempo sin responder a las confirmaciones del Bot, la tarea se pausará automáticamente**.
- Comprueba la zona horaria en When to run y la configuración de fines de semana. Una programación recién creada esperará al siguiente ciclo natural; haz clic primero en Test para comprobar el enlace.
- Consulta el "Historial de ejecuciones" en la versión móvil: **si muestra No runs yet, significa que la señal no llegó a la pasarela**; si muestra Failed, puedes pulsar para ver el error específico.

Fuente: [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)

### El Webhook externo envió datos, pero la rutina no se inició
- Al llamar a la API, comprueba primero el valor de retorno: **si no es 200, significa que la solicitud fue interceptada por la pasarela**.
- Comprueba la clave Bearer en el encabezado de solicitud `Authorization`; tras regenerarla, la clave anterior queda invalidada de inmediato.
- Tras crear un nuevo desencadenador, **es obligatorio hacer clic en Save en la esquina inferior derecha** para que el endpoint y la clave surtan efecto en la pasarela.

Fuente: [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)

### El desencadenador de Slack no se activa
- El desencadenador **solo se aplica a los nuevos mensajes posteriores a su activación**; editar mensajes antiguos no lo activará.
- Asegúrate de no haberlo enviado al canal equivocado; la cuenta debe tener permisos de lectura en el canal de destino y **las palabras clave deben coincidir con exactitud**.

Fuente: [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)

### La tarea se bloqueó o interrumpió a mitad de la ejecución
- Las tarjetas de aprobación desatendidas en segundo plano **solo esperan unos 10 minutos**; al agotarse el tiempo cambian a Expired y se interrumpen fallando.
- Activa las notificaciones o autoriza la ejecución automática de acciones de confianza en las "Reglas personalizadas" del modo Settings > Bot > Auto-review.
- Si encuentras un error, haz clic derecho en el bocadillo de mensaje, selecciona **Copy request ID** y envía el texto del error al equipo oficial para revisar los registros.

Fuente: [《Guía de uso de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to.md)

### Tras actualizar el ordenador en la nube, se perdieron los scripts locales y los temporizadores
| Tipo de actualización | Conservación del entorno |
| :--- | :--- |
| Actualización de software | El entorno y los archivos del ordenador en la nube no se ven afectados |
| Actualización del ordenador ("Ajustes" > "Ordenador" > "Actualizar ordenador del Bot") | Reconstruye la imagen; conserva `/workspace` y la sesión iniciada en el navegador, pero **borra los paquetes globales de apt (como cron)** |

Fuente: [《Guía de uso de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to.md)，[《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)

## Errores comunes que debes evitar

1. **Hacer clic en Test realiza una ejecución real**: invocará herramientas y podrá eliminar archivos; **antes de probar, deja puntos de interrupción para aprobación en la instrucción** [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)。
2. **Mecanismo de sondeo (polling) y programación**: Un sondeo cada 5 minutos agotará la cuota de toda la semana; **usa scripts ligeros de comparación y despierta al modelo solo si hay cambios**. "Todos los días a las 9:00" se ejecuta por defecto en días laborables; **especifica "incluidos los fines de semana" y fija la zona horaria en Settings**.

   [《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。
3. **No pegues claves de Webhook en el chat**: Quedarán registradas en el historial en la nube. **Las credenciales deben introducirse en la tarjeta de solicitud de información confidencial segura**; si la pegas por error, elimínala de inmediato.

   [《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。
4. **Evitar fallos silenciosos por intercepción de aprobación**: Al configurar intercepciones, debes activar las notificaciones móviles. **Tras aparecer la solicitud de aprobación, caduca y se cancela si nadie responde en 10 minutos** [《Guía de uso de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to.md)。
5. **Entorno compartido de Bots**: Borrar archivos en `/workspace/temp` afectará a otros Bots; **al escribir archivos, es obligatorio especificar subdirectorios independientes para cada proyecto**.

   [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)。

## Cómo verificar una vez completado

Pasa por estos cuatro pasos en orden; **solo cuando los superes todos podrás dejarlo funcionar desatendido**:

1. Comprobar la hora: En la página de detalles, confirma que la marca de tiempo de **Next run** coincida exactamente con tu zona horaria local.
2. Probar datos ausentes: Desconecta la red o pasa un archivo vacío y haz clic en Test; la rutina debe informar del error y detenerse, sin inventar contenido.
3. Probar la intercepción de aprobación: Envía deliberadamente instrucciones de eliminación o de envío externo; si se ejecutan directamente sin mostrar una tarjeta de aprobación, indica que hay una brecha de seguridad y debes configurarla en Settings.
4. Comprobar registros y guardado en disco: Ejecútala una vez con normalidad, ve a `/workspace` para confirmar que los documentos se hayan escrito correctamente y que no haya saturado la ventana de chat.

Fuente: [《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## Lecturas complementarias

### Capítulos relacionados

- [第 20 章 可靠的自动化：定时、Webhook 与事件触发](/part3/20-automation)

### Documentación oficial

- [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)
- [《Rutinas》](https://cursor.com/cn/help/grok-bot/routines.md)
- [《Guía de uso de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to.md)

### Prácticas de la comunidad

- [《4.3 Desencadenadores y automatización: programación, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [《Grok Bot 额度再省一点：定时任务极限优化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [《Grok Bot Webhook + 快捷指令：知识自动入库流水线搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
