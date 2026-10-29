# Capítulo 4 Asignar tareas: mensajes, archivos adjuntos y un traspaso efectivo

Si los requisitos son demasiado breves, es fácil que busque docenas de páginas web irrelevantes y altere archivos. **Enviar un mensaje es hacer el traspaso de trabajo a una computadora en la nube**.

- **Establece límites estrictos de la tarea** y explica el propósito de los archivos adjuntos para evitar que tome decisiones por su cuenta
- Proporciona instrucciones claras a cambio de entregables listos para su aceptación directa
- Intervén en cualquier momento durante la ejecución para corregir desviaciones o usa la voz para complementar el contexto


![Asignar tareas: mensajes, archivos adjuntos y un traspaso efectivo](/info/04-handoff.png)

## Los cinco elementos de una buena solicitud

![Los cinco elementos de una buena solicitud](/info/04-handoff-s1.png)

Al asignar tareas a Grok Bot, **las instrucciones deben definir claramente los objetivos y el alcance de las herramientas**; consulta las especificaciones en la documentación de [《Grok Bot》](https://cursor.com/cn/docs/grok-bot).

1. **Acciones específicas y únicas**. Especifica «rastrear y comparar» o «redactar correo externo», no uses «investiga un poco»; cuanto más corta sea la ruta, más pasos se ahorran.
2. **Limitar las fuentes de datos**. Especifica páginas de Notion, canales de Slack como #sales-leads o URLs para evitar búsquedas descontroladas en toda la web.
3. **Trazar líneas rojas de aprobación**. La lectura y comparación se ejecutan automáticamente; **si implica enviar correos externos, pagos en línea o modificar/eliminar datos, debe pausarse y esperar aprobación**.
4. **Fijar el formato de entrega**. **Rechaza informes verbales** y exige generar informes en Markdown con enlaces o tablas CSV en `/workspace/leads/`.
5. **Establecer reglas de error y límites de hechos**. Distingue entre especulaciones y hechos objetivos; si la sesión expira, omite y registra, **prohibiendo bucles infinitos de reintento**.

## Especificaciones de archivos adjuntos y lista de restricciones

Consulta las reglas de subida en [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work).

### Restricciones de especificaciones

- En la versión de escritorio hay un **límite de 6 por mensaje** (el exceso debe colocarse en el espacio de trabajo); imágenes, texto y audio tienen un límite de 25MB, y video de 200MB.
- Si encuentras bloqueos o errores, conviértelo localmente a PDF, CSV o imagen antes de subirlo.

### Traspaso y chats grupales

1. **No presiones Enter inmediatamente después de arrastrar**, explica claramente la identidad de cada archivo, la lógica de correlación y las declaraciones de protección.

```text
上传的 PDF 是已经签署的标准采购合同模板。上传的 Excel 是本月供应商提交的实际报价清单。
请对照合同模板中第 4 条关于各类物料的基准单价，逐行核验 Excel 里的实际报价。
标出单价超出基准价的所有条目，在附带的备忘中引用合同中的对应条款编号。
将核验结果另存为一份新的 Excel 表格，并输出一份简短的异常摘要。
请勿改动原始上传文件。
```

2. Entre Bots en chats grupales **solo se admite texto plano**. Si un Bot posterior necesita ver los archivos adjuntos, deben enviársele por chat privado.

## Biblioteca de prompts prácticos para entrega de tareas

Para escenarios comunes, **usa directamente las plantillas**; solo modifícalas un poco y estarán listas.

1. **Investigación y contacto externo**: buscar pistas y preparar material, sin enviar directamente.
```text
从我们的 CRM 系统中获取本周销售管道的重点评审列表。
请跳过当前已经处于活跃跟进序列中的联系人。
在指定公开网页和已授权的 Slack 相关频道中，深入调研排名前五的重点账户，找出负责采购或技术的对口联系人。
参考我在系统中历史邮件的口吻，为这五位联系人分别起草个性化的初次外联邮件。
将草稿保存在系统草稿箱中，并在明天上午 9 点前在此对话中列出清单供我审批。未经我的明确确认，绝不向外发送任何邮件。
```
2. **Verificación de archivos adjuntos**: alinear múltiples tablas y auditar ingresos y gastos.
```text
附件中的 PDF 为《2026 年度差旅与报销政策细则》，CSV 表格为本月部门提交的待审批费用报销流水。
请逐项核对 CSV 中的每一笔申报项目：
1. 检查报销金额是否超过对应城市级别的住宿与餐饮标准。
2. 检查单笔超过 500 元的支出是否有对应的发票类别标记。
3. 提取所有不符合政策规定的异常申报，列明行号、申报人、金额、超标原因及违背的政策条款。
最后生成一份 Markdown 格式的核查报告，并列出通过与未通过的统计汇总。保持原始 CSV 文件不被改动。
```
3. **Inspección de sitios web**: inspeccionar páginas y conservar evidencia.
::: details Biblioteca de prompts prácticos para entrega de tareas
```text
你负责检查我的网站运行状态。本次只访问我提供的以下三个页面：首页、最新更新日志页、用户注册页。
逐一核验各页面是否能正常打开、关键按钮是否响应、文本信息是否存在断链或明显过期内容。
排查过程中必须执行以下要求：
1. 发现任何显示异常或报错时，保存完整的页面 URL、检查时间戳以及当时的屏幕截图。
2. 区分页面直接看到的事实与你的推测，事实写在证据栏，分析写在备注栏。
3. 检查受阻或遇到需要验证码时，记录阻碍原因并继续检查下一个页面，不要重复尝试。
4. 检查结果报告保存在 /workspace/site-check/ 目录下，命名为 check-report.md。
你仅有只读检查与生成报告的权限，严禁更改后台设置或提交任何表单。
```
:::
4. **Revisión de planes**: revisar la lógica antes de operaciones complejas para evitar desviaciones.
::: details Biblioteca de prompts prácticos para entrega de tareas
```text
我准备让你整理过去一个季度跨 Notion、Gmail 和 GitHub 的客户产品缺陷反馈。
在正式开始执行数据读取与整理之前，请先不要调用任何批量工具，先在对话中向我提交一份执行计划：
1. 列出你准备按顺序访问的系统、模块与具体检索词。
2. 说明你打算提取哪些关键字段，以及如何去重。
3. 标明整个流程中哪些环节可能涉及对外部状态的更改。
4. 说明你打算将阶段性文件保存在云电脑的哪个路径，以及遇到权限不足时如何处理。
我确认并批准你的计划后，你再开始执行。
```
:::
5. **Notificación de mensajes entrantes**: extraer puntos clave y clasificar para su derivación.
::: details Biblioteca de prompts prácticos para entrega de tareas
```text
使用已连接的邮箱插件，读取收件箱过去 24 小时内收到的全部新邮件。
按照以下业务逻辑进行分类处理：
1. 属于系统续费、订阅扣款账单的邮件，提取服务商、扣款金额与下次续费时间。
2. 属于用户直接提问或反馈 Bug 的邮件，提取发件人邮箱、问题概括与紧急程度。
3. 属于营销推广、垃圾资讯的邮件，直接归入忽略清单。
在当前会话中输出一份分栏概览：仅展示需我关注的账单与紧急反馈，并在每条记录后附带邮件主题与时间。
所有邮件保持未读或已读原状，未经审批严禁归档、删除或起草回复。
```
:::

## Reglas permanentes y tareas puntuales: no confundas las reglas de la casa con los quehaceres

![Reglas permanentes y tareas puntuales: no confundas las reglas de la casa con los quehaceres](/info/04-handoff-s4.png)

**Distingue claramente entre reglas permanentes y tareas puntuales** (consulta [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work)), no escribas parámetros temporales en configuraciones a largo plazo, ni vuelvas a definir las líneas rojas cada vez.

| Tipo | Ciclo y configuración | Ejemplos y restricciones |
| --- | --- | --- |
| Reglas permanentes | Efectivas en todas las sesiones; configurar en Bot Details o ingresar «Por favor, guarda esto en tu memoria como una regla permanente» | Líneas rojas de permisos, fecha YYYY-MM-DD |
| Tareas puntuales | Efectivas solo en la ronda actual sin persistencia; ordenar directamente | Procesar 12 cuentas o 3 audios, extraer la lista de la reunión de las diez en punto |

Todos los Bots comparten `/workspace` (consulta [《10 consejos esenciales para que tu Grok Bot funcione mejor》](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)).

**La memoria no puede reemplazar a los sistemas de negocio**; los saldos y el inventario deben consultarse en la fuente original, quedando estrictamente prohibido inventarlos.

## Intervención durante la ejecución de la tarea: detener, interrumpir y aprobar

![Intervención durante la ejecución de la tarea: detener, interrumpir y aprobar](/info/04-handoff-s5.png)

### Interrumpir y detener
Cuando el Bot se desvíe del objetivo, enviar un mensaje normal permite **interrumpir de inmediato**, por ejemplo enviando «cambia a la versión de especificaciones actualizada en octubre de 2026 y vuelve a verificar».

Si ocurre un error en la operación o una llamada de alto riesgo, envía cuatro caracteres en el cuadro de entrada para detenerlo.
```text
立即停止
```

**Detener solo bloquea acciones no ejecutadas; nunca revierte archivos ya guardados ni solicitudes de API ya enviadas**. Tras detenerlo, sigue tres pasos para la resolución de problemas.
1. Abre el panel de vista previa de la computadora en la nube para ver el estado.
2. Limpia los archivos a medio terminar o las escrituras incorrectas.
3. Reduce el alcance y define claramente los límites antes de reiniciar.

### Aprobación y tiempo de espera agotado
Al activar Auto-review o activar operaciones de alto riesgo, aparecerá una tarjeta de «Revisión de acción» (consulta la [《Guía de operaciones de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to)), que contiene tres opciones.
- Permitir una vez: solo aprueba esta vez; se seguirá preguntando en ocasiones similares posteriores.
- Permitir siempre: añadir a la lista blanca y no volver a avisar.
- Rechazar: bloquear completamente dicha operación.

| Escenario | Mecanismo de espera | Resultado por tiempo agotado |
| --- | --- | --- |
| Interacción en tiempo real | Suspensión en espera | Espera continua hasta que se haga clic para procesar |
| Desatendido en segundo plano | Expira automáticamente en unos 10 minutos (Expired) | **No se ejecuta la operación y finaliza la tarea** |

### Tomar el control de credenciales (Action needed)
Cuando involucre contraseñas, 2FA, así como CAPTCHA o pagos reales, aparecerá una tarjeta de toma de control; sigue estos tres pasos.
1. Haz clic en **Take over** e ingresa manualmente en la computadora en la nube.
2. Una vez completado, haz clic en **I'm done** para devolver el control.
3. **Nunca introduzcas contraseñas en texto plano en el cuadro de chat normal**.

## Interacción por voz: uso diferenciado entre llamadas de voz en tiempo real y dictado por voz

Grok Bot incluye **dos funciones de voz distintas**: dictado y llamadas; para más detalles, consulta [《Chat de voz con Bot》](https://cursor.com/cn/help/grok-bot/voice-chat) y la [《Guía de operaciones de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to).

### Comparación de los dos modos

| Modo | Activación y atajos | Salida y escenarios |
| --- | --- | --- |
| Entrada de voz (dictado) | En escritorio haz clic en «Iniciar entrada de voz», en Mac presiona Cmd+D, en Win/Linux presiona Ctrl+D, en el móvil toca «Iniciar dictado» | El texto se inserta en el cuadro de entrada, adecuado para ajustar prompts o añadir parámetros |
| Chat de voz en tiempo real | **Vacía el cuadro de entrada** y haz clic en el icono de onda (Start voice chat) | Llamada bidireccional en tiempo real, adecuada para ordenar ideas o realizar traspasos rápidos |

### Pasos para iniciar y errores a evitar

1. Abre una conversación individual con un Bot.
2. **El cuadro de entrada debe vaciarse por completo**; cualquier espacio o borrador residual ocultará el icono de onda.
3. Haz clic en el icono de onda; en el primer uso se deben conceder permisos de micrófono.
4. Aparecerá Connecting… (en móviles Calling…); cuando el Bot comience a hablar, la conexión estará establecida.

### Controles y restricciones estrictas

- Durante la llamada es posible silenciar, ver subtítulos desplazables y ajustar la velocidad y el timbre de voz; al cambiar de pantalla para consultar información, haz clic en la barra superior en «Volver al chat de voz» para regresar.
- **Solo admite chats individuales uno a uno**; no se puede iniciar en chats grupales, grupos de múltiples Bots ni con «Bots de equipo».
- **Solo se puede mantener una llamada al mismo tiempo**; para cambiar a un nuevo Bot es necesario confirmar «Finalizar y chatear».
- Al colgar, se genera automáticamente una tarjeta de Voice chat que registra la duración total; haz clic para consultar el texto completo y las tareas posteriores continuarán en el flujo de texto.

## Ejemplos comunes de errores y comparación con versiones optimizadas

1. **Restringir rutas**: si no se definen el alcance y el método, el Bot hará clics aleatorios en la consola, **e incluso modificará código en entornos de producción**.
```text
  帮我维护一下网站，看看有没有什么 Bug。
  ```
Cámbialo para delimitar páginas y pasos de inspección:
```text
  对站点清单（/workspace/sites.txt）中的三个静态展示页进行巡检。
  用云浏览器打开每个页面，检查控制台是否有 404 或 500 报错，检查顶部导航栏链接是否全部有效。
  将报错信息、对应页面 URL 及当时的屏幕截图写入 /workspace/logs/err-20261014.md。
  全程仅做只读检查，严禁点击任何带有提交或删除性质的表单按钮。
  ```

2. **Límites de aprobación**: no otorgues permisos de envío externo; si hay un malentendido, **es fácil enviar contenido incorrecto a clientes importantes**.
```text
  读取 Gmail 里的未读邮件，重要的直接帮我回一下。
  ```
Deja los puntos clave para la aprobación humana:
```text
  读取 Gmail 中过去 12 小时的未读邮件。
  仅筛选出发件人属于我们现有企业客户、且正文包含售后或咨询诉求的邮件。
  根据产品常见问题手册，为每封邮件起草回复草稿并存入 Gmail 草稿箱。
  在当前对话中列出客户名称、邮件摘要与草稿正文，等待我的审批。未经我的明确确认，绝不点击发送。
  ```

3. **Separación de hechos**: no incluyas sesgos en los prompts, **para evitar que el Bot se adapte a suposiciones y confunda una pequeña promoción con una guerra de precios**.
```text
  去看看竞品今天的动态，总结一下他们是不是要跟我们打价格战。
  ```
Separa los datos objetivos de las conjeturas:
```text
  访问竞品官网的公开定价页与首页横幅，获取他们当下的方案价格表。
  对照我们在 /workspace/competitor/last-month-price.json 中记录的旧价格：
  1. 事实列：标出哪些 SKU 的标价发生了变动，变动金额是多少，附带页面截图与访问时间。
  2. 推测列：基于该降价是限时促销还是永久调价，给出你的分析理由。
  两部分内容必须分开分栏呈现，不得将分析推论当作已知事实。
  ```

4. **Protección de solo lectura**: sin especificar las tablas principales/secundarias y los campos a conservar, **los datos originales pueden sobrescribirse y dañarse con facilidad**.
```text
  （直接拖入三个 Excel 表格）把这几个表整理一下。
  ```
Debe aclararse qué tabla sirve de referencia y establecerse como de solo lectura:
```text
  上传的三个表格分别是 7 月、8 月和 9 月的销售明细。
  以「订单编号」为唯一主键进行数据去重合并：
  1. 字段统一保留：订单号、成交日期、客户名称、销售代表、成交金额。
  2. 生成一份全新的 Q3_sales_summary.csv 文件，保存在当前工作区。
  3. 保持我上传的原始 7、8、9 月表格内容与文件名完全不变。
  ```

5. **Misión única**: no acumules múltiples tareas en un solo Bot; no solo desordenará la memoria, **sino que también agotará rápidamente la cuota semanal**.
```text
  你帮我写一篇关于新产品的推文，顺便把昨天的账目算了，然后再帮我看看竞品推特。
  ```
Divídelo en flujos de trabajo de tareas individuales:
```text
  遵循一个 Bot 负责一项核心任务的原则。当前 Bot 仅承担社媒文案起草职责：
  依据 /workspace/product/spec.md 中的新功能说明，为 X 平台起草三条不同风格的发布文案。
  要求突出性能提升数据，字数控制在 280 字符以内。
  账目核算与竞品调研交由对应的专用 Bot 负责，不要在此会话中处理。
  ```

## Casos reales de traspaso en negocios

### Inspección diaria de sitios web y conservación de evidencia
El webmaster yishan redactó los requisitos de inspección directamente como especificaciones de aceptación. El directorio de trabajo está estrictamente limitado a `/workspace/site-check/`, permitiendo únicamente inspeccionar la página de inicio, los artículos más recientes y los accesos de suscripción, prohibiendo estrictamente el rastreo exploratorio.
- El informe debe conservar los enlaces completos, marcas de tiempo y capturas de pantalla de ese momento. **Los errores observados directamente se consideran hechos, mientras que las causas investigadas se consideran conjeturas; deben registrarse por separado.**
- Al encontrar una sesión expirada o enlaces rotos, se registra la incidencia y se omite directamente, prohibiendo insistir repetidamente. Para el método específico, consulta [《Cómo profundizar en el uso de Grok Bot en una hora》](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg).

### Intermediación de la bandeja de entrada y distribución de operaciones
一泽Eze configuró especialmente un Bot de bandeja de entrada para hacerse cargo de Gmail, sin conceder permisos de correo electrónico individualmente a cada Bot posterior.
- Al recibir correos de comentarios, los reenvía por chat privado al «Bot de comentarios de productos», y las facturas al «Bot de gestión de suscripciones».
- La comparación puramente numérica se delega directamente a scripts de línea de comandos. **Sincronizar solo datos incrementales con el Bot permite ahorrar cuota de uso semanal.**
- No vincules herramientas de altos permisos en todas partes; usar un punto de entrada dedicado para el filtrado inicial es lo más seguro.

  Para un resumen de experiencias, consulta [《10 consejos esenciales para que tu Grok Bot funcione mejor》](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc).

### Evaluación inicial del jefe de gabinete y creación de Bots
CyrilXBT hizo primero que el Bot jefe de gabinete leyera el Notion y Slack del equipo para detectar las tres tareas que más tiempo consumían, más se repetían y presentaban mayores bloqueos, avanzando en tres pasos.
1. El Bot jefe de gabinete las ejecuta manualmente guiado, con supervisión humana de la calidad de los resultados.
2. Tras confirmar que no hay errores, se consolida como una habilidad y se crea un Bot dedicado independiente.
3. Finalmente, se configura para que se ejecute automáticamente de forma programada.
**Los puntos que involucren envíos, compras, publicaciones o modificaciones en sistemas en línea deben conservar estrictamente la aprobación manual.

** Tutorial completo en [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)。

## Errores comunes que debes evitar

1. **Adjuntar archivos con descripción**: al subir varias imágenes o dos o más hojas de cálculo, **asegúrate de especificar su propósito**, de lo contrario es fácil confundir la relación principal-secundaria.
2. **Guardar reglas permanentes en la memoria**: las instrucciones individuales se pierden al cambiar de sesión; las normas y líneas rojas deben **escribirse en Acerca de / Responsabilidades en los detalles del Bot** o guardarse en la memoria.
3. **Prevenir la suspensión en la vinculación local**: en la nube pura sigue funcionando al cerrar la tapa, pero al vincularse con la computadora local, entrar en suspensión cortará la conexión; recuerda **verificar la configuración de energía y suspensión**.
4. **Compartir imágenes entre Bots mediante rutas**: entre Bots en grupos solo se admite texto plano; para compartir imágenes debes **guardarlas en la ruta compartida `/workspace/`** para que el otro Bot las lea.
5. **Si el botón de voz desaparece, vacía primero**: si quedan textos o espacios no eliminados en el cuadro de entrada, el botón de onda se ocultará; **vacía completamente el cuadro de entrada** para restaurarlo.
6. **Seleccionar permitir una vez para operaciones de alto riesgo**: no elijas «Permitir siempre» al enviar correos o modificar/eliminar datos; antes de que funcione de forma estable durante varias semanas, **insiste en elegir «Permitir una vez»**.

## Cómo realizar la aceptación al terminar

1. Ve a `/workspace/` o al directorio especificado para verificar los archivos; **confirma que se puedan previsualizar normalmente y sin caracteres extraños**, no te limites a mirar el texto temporal.
2. Revisa al azar 2 o 3 datos clave abriendo los enlaces o capturas de pantalla para evitar que el modelo invente información.
3. Revisa los registros de llamadas para **confirmar que no haya enviado comunicaciones no autorizadas, ni modificado configuraciones o sobrescrito archivos originales**.
4. Distingue hechos de conjeturas: coloca las citas textuales de las páginas en el área de hechos y las inferencias o sugerencias en el área de notas, corrigiendo de inmediato cualquier confusión.
5. Revisa la lista de excepciones: **si encuentras páginas web no válidas o campos faltantes, registra el motivo y completa la ejecución**, sin interrumpirla al primer error.

## Lecturas recomendadas

- Documentación oficial: [《Grok Bot》](https://cursor.com/cn/docs/grok-bot)
- Documentación oficial: [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work)
- Soporte oficial: [《Guía de operaciones de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to)
- Soporte oficial: [《Chat de voz con Bot》](https://cursor.com/cn/help/grok-bot/voice-chat)
- Artículo de la comunidad: [《Cómo profundizar en el uso de Grok Bot en una hora》](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)
- Artículo de la comunidad: [《10 consejos esenciales para que tu Grok Bot funcione mejor》](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)
- Artículo de la comunidad: [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
