# Capítulo 1 Qué es Grok Bot: Un colega de IA con computadora propia

Las conversaciones tradicionales en páginas web no permiten acumular activos y, **al cerrar la computadora, las tareas se interrumpen de inmediato**. Ante la necesidad de invocar múltiples aplicaciones e inspeccionar de forma continua, las personas siguen atadas a la pantalla haciendo clics mecánicos.

Este capítulo incluye cuatro contenidos clave:
- Su mecanismo de funcionamiento y los límites físicos de la computadora en la nube compartida;
- Tipos de tareas aptas y no aptas para delegar;
- Diferencias de selección frente a otros agentes persistentes del mercado;
- **Redactar una descripción de puesto estandarizada y establecer controles de aprobación manual para evitar excesos de privilegios.**

![Qué es Grok Bot: Un colega de IA con computadora propia](/info/01-what-is.png)

## ¿Cuál es el mecanismo de funcionamiento subyacente de Grok Bot? {#产品机制-环境底座与思考模型拆分}

**El núcleo de Grok Bot consiste en desacoplar la base de Linux persistente en la nube del modelo de razonamiento programado bajo demanda; cuenta con terminal, navegador y archivos persistentes, de modo que incluso apagando la computadora o cerrando la tapa, las tareas en segundo plano siguen ejecutándose en la computadora en la nube.**

![Mecanismo del producto: Separación de la base de entorno y el modelo de razonamiento](/info/01-what-is-s1.png)

xAI y Cursor lanzaron Grok Bot el 11 de agosto de 2026, **cuya clave es desacoplar la base del entorno del modelo de razonamiento**.

- **Base (Harness)**: Residente de forma permanente en la nube, equipada con terminal Linux, navegador y archivos persistentes. Al apagar o cerrar la tapa, las tareas en segundo plano continúan ejecutándose con normalidad.
- **Modelo (Brain)**: Programado según la demanda, no está vinculado a un único modelo y no se puede consultar ni especificar. A partir del 7 de octubre de 2026, las tareas pueden enrutarse a modelos como Claude Opus 5.5 o derivarse a Cursor Agent para codificación colaborativa.

| Herramienta | Entorno de ejecución | Trabajo sin conexión y colaboración |
| --- | --- | --- |
| Asistente de chat | Web temporal | Se interrumpe al cerrar la página, conversación única |
| Agente de línea de comandos | Terminal local | Se detiene al salir, limitado al repositorio local |
| Grok Bot | Computadora en la nube persistente | **Sigue ejecutándose tras apagar**, entrega de archivos entre tareas |

Para más detalles sobre el mecanismo, consulte [«1.1 Qué es Grok Bot: Entiéndalo en una página»](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc).

## ¿Cómo aislar y tomar el control de la computadora en la nube compartida de Grok Bot? {#共享云电脑的物理边界与接管机制}

**Todos los Bot de una misma cuenta comparten la computadora en la nube y no pueden aislar rutas ni cookies; la transferencia entre tareas requiere guardar archivos en /workspace, y ante operaciones como introducir contraseñas o pagos, se puede hacer clic en Take over para tomar el control manual.**

![Límites físicos y mecanismo de toma de control de la computadora en la nube compartida](/info/01-what-is-s2.png)

Todos los Bot de una misma cuenta comparten la computadora en la nube. Las pruebas del nivel Heavy arrojaron un procesador Xeon de 8 núcleos y 8 hilos, 16 GB de RAM y 128 GB de disco duro (no verificado, sujeto a datos oficiales); en la versión v0.68.1 la resolución aumentó a 1920×1200.

Consulte las especificaciones en la [documentación de computadoras y aplicaciones de Grok Bot](https://cursor.com/cn/docs/grok-bot/work#the-computer-and-apps).

- Crear un nuevo Bot **no permite aislar permisos**. Comparten rutas y estados de inicio de sesión, y todos pueden leer cookies.
- La colaboración entre Bot depende del almacenamiento de archivos en disco. Los chats privados están aislados por naturaleza; para las transferencias es necesario guardar archivos en `/workspace`.
- Para introducir contraseñas, verificaciones en dos pasos o realizar pagos, haga clic en Take over para gestionarlo; **nunca envíe contraseñas en texto sin formato en el cuadro de chat**.
- Controlar el entorno local requiere autorización independiente. Está aislado de su máquina local; actívelo en Settings → General → Agent → Execution on Local Computer, lo que mostrará una ventana emergente de confirmación al ejecutarse.

## ¿Para qué tareas es adecuado y no adecuado Grok Bot? {#适合与不适合的任务类型}

**Grok Bot es adecuado para tareas de flujo fijo, alta frecuencia y repetitivas que requieran invocar múltiples herramientas, como la inspección de información y la reproducción de errores; sin embargo, no es adecuado para preguntas y respuestas instantáneas, codificación local ni operaciones de alto riesgo sin controles manuales.**

![Tipos de tareas adecuadas y no adecuadas](/info/01-what-is-s3.png)

### Criterios de filtrado de tareas
**Para determinar si una tarea debe delegarse a Grok Bot, observe directamente estos tres criterios de filtrado:**
- Puede ejecutarse por completo en el navegador web, terminal o a través de una API;
- Los archivos intermedios o los informes finales pueden ser verificados directamente por una persona;
- Las acciones sensibles o de alto riesgo pueden pausarse a la espera de una aprobación humana mediante una ventana emergente.

### Tareas adecuadas
**Adecuado para labores con procesos fijos, alta frecuencia y que requieran invocar múltiples herramientas.**
- Inspección de información: Visitar periódicamente sitios web oficiales específicos para generar tablas de resumen.
- Depuración de prospectos: Extraer cuentas objetivo del CRM y redactar cartas de contacto combinando información pública para su revisión.
- Conciliación financiera: Cotejar facturas semanalmente, marcar facturas faltantes y gestionar cobros.
- Reproducción de defectos: Leer Issues, reproducirlos en entornos de preproducción y extraer registros y capturas de pantalla.
- Informe matutino de operaciones: Consolidar diariamente métricas de inventario y detectar anomalías.

### Tareas no adecuadas
**No intente forzar tareas incompatibles; es fácil agotar inútilmente la cuota semanal o incluso perder el control.**
- Preguntas y respuestas instantáneas: Consultar errores se resuelve en segundos con modelos web convencionales, sin requerir una computadora en la nube.
- Codificación local: La depuración con puntos de interrupción y la resolución de conflictos de Git deben gestionarse localmente con Codex CLI o Claude Code.
- Asuntos personales y cotidianos: Gestionar calendarios carece de fuentes de datos de nivel empresarial; forzar su uso resulta poco práctico.
- Sondeo sin cambios incrementales: Actualizar incondicionalmente cada 5 minutos consumirá la cuota de inferencia en vano.
- Operaciones de alto riesgo: El envío masivo de correos y la eliminación de bases de datos deben contar obligatoriamente con controles de aprobación manual.

Consulte el método de planificación en [«1.2 Cómo elegir entre Grok Bot, Muse, Hermes, dots y Cue»](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd).

## Comparativa de selección: Grok Bot frente a los principales agentes persistentes

### Formato integrado frente a formato ensamblado

Elegir un agente persistente depende principalmente de si prefiere la comodidad o le gusta experimentar y configurar. Las **soluciones listas para usar** (Grok Bot, Muse) evitan las molestias del despliegue, pero están sujetas a los límites de cuota de la plataforma; las soluciones ensambladas (Hermes) conectadas a modelos de código abierto no tienen restricciones de cuota, pero los errores del entorno deben resolverse por cuenta propia.

### Características y comparativa de los principales agentes persistentes

| Producto | Base y requisitos de acceso | Características y casos de uso |
| --- | --- | --- |
| Grok Bot | Computadora Linux en la nube compartida. Desde el 2026-10-12 rige el plan unificado The X Subscription (Premium $30/mes, Super $100/mes, Ultra $200/mes), **el nivel Plus no incluye Bot**; el cliente v0.70.2 admite buzón de correo independiente y tarjetas de conexión | Residente 7×24 horas, compatible con rutinas y habilidades (Skills), transferencia asíncrona de archivos entre múltiples Bot y búsquedas en la plataforma X. Ideal para entornos sin mantenimiento, colaboración multipuesto, inspección y conciliación |
| OpenAI dots | Computadora en la nube personal persistente, ChatGPT Pro y Business Premium incluyen el primer dot | Basado en GPT-6 Astra (dots se lanzó el 2026-09-29), opera en segundo plano conectado a más de 4000 aplicaciones, orientado al acompañamiento diario y tareas ligeras |
| Manus Cue | Computadora en la nube independiente, en fase de acceso anticipado | Probado por 铁柱 el 2026-09-29; incluye de forma nativa buzón colaborativo independiente, teléfono y billetera, con capacidad autónoma para registrarse y realizar compras; autonomía sumamente alta acompañada de riesgos operativos |
| Meta Muse | Agente en la nube alojado por Meta, evaluado por 诺鸭船长 con enfoque en el ecosistema doméstico | Profundamente integrado con la red social y el hardware de Meta, adecuado para la vida cotidiana del hogar y la asistencia social |
| Hermes | Servidor local o privado, despliegue propio de código abierto | Libertad para cambiar de modelo de código abierto sin límites de cuota comercial. Adecuado para canalizaciones de datos sensibles locales, **requiere configurar el entorno y resolver errores manualmente** |

Para una comparativa detallada en tweets, consulte [«Colección de tweets de 铁柱 ④: Comunidad, ecosistema y comparativa con competidores»](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg).

## Análisis de casos prácticos típicos

### Director de inteligencia de 金尘马 (puesto de investigación personal)

金尘马 (@jinchenma_ai) especificó en su momento las reglas de puesto a largo plazo en la Description de Edit Profile (este menú ha sido eliminado; para el método actual, consulte el capítulo 3), definiéndolo como investigador de inteligencia. Al asignar tareas, se implementan los cinco elementos esenciales: resultado, fuente, restricciones, formato y puntos de confirmación; busca publicaciones largas en la plataforma X diferenciando posts con video e indicando métricas de exposición; **está estrictamente prohibido inventar información a falta de datos primarios**.

Tras corregir el formato por primera vez, ordenó al Bot consolidar el flujo como un Skill: «Recopilación de información de tutoriales de IA».

Tras validar con un segundo conjunto de entradas, configuró una Routine para ejecutar automáticamente el informe cada día laborable a las 8:10 de la mañana; creó un nuevo «Director de contenido» para evaluar los temas propuestos y guardó el borrador inicial en `/workspace/grokbot-demo/`.

**La descripción del puesto consolida las reglas a largo plazo, mientras que las necesidades temporales se gestionan mediante mensajes**, desacoplando múltiples Bot a través del almacenamiento en `/workspace`.

Consulte los detalles en [«Artículo extenso | Grok Bot de cero a experto | 金尘马»](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee).

### Equipo de operaciones de comercio electrónico de 金尘马 (línea de producción con división multirrol)

El equipo colabora con 4 Bot. Primero se creó el «Operador de guardia de la tienda» para leer tablas de productos, inventario y pedidos con el fin de enviar un informe matutino, **estableciendo una línea roja estricta de solo lectura: queda terminantemente prohibido modificar precios o inventarios, así como enviar correos o realizar reembolsos**.

El operador de guardia original fue ascendido a «Supervisor de operaciones de comercio electrónico», dividiéndose en especialista de crecimiento de contenido, analista de inventario de productos y asistente de postventa de pedidos, guardando los datos en `/workspace/ecommerce-ops/日期/`. Si un producto estrella solo tiene 3 días de inventario restante, el especialista de contenido suspende la promoción, el asistente de postventa prepara el argumento de retraso y el supervisor consolida la lista de decisiones.

No empiece construyendo un equipo enorme desde el principio; **bloquee con aprobación manual todas las operaciones que involucren fondos, inventario y comunicaciones externas**.

### Bot administrador de repositorios de código abierto de 铁柱 (inspección y mantenimiento automatizados)

铁柱AGI (@cgnot996) creó un Bot persistente para mantener la base de conocimiento awesome-grok-bot. El sistema inspecciona periódicamente los tweets de la plataforma X, los registros de actualizaciones oficiales y las comunidades técnicas, recopilando y categorizando nuevas funciones, tutoriales, documentación oficial y eventos.

Antes del lanzamiento oficial ya había recopilado material relevante de forma automática, **superando más de 130 estrellas en agosto de 2026 (declarado por el autor, no verificado)**, y recibió una invitación mediante formulario de solicitud por parte del equipo oficial.

## Guía de inicio rápido: Desde la activación hasta su primer Bot dedicado

![Guía de inicio rápido: Desde la activación hasta su primer Bot dedicado](/info/01-what-is-s6.png)

### Confirmar el nivel de suscripción e instalar el cliente

Elija el nivel según el plan unificado The X Subscription vigente a partir del 12 de octubre de 2026:
- **Nivel Premium**: $30/mes ($300 anuales), fondo de cuota 4x; opción ideal para uso personal diario.
- **Nivel Super**: $100/mes ($1000 anuales), fondo de cuota 15x; adecuado para investigación intensiva y múltiples rutinas.
- **Nivel Ultra**: $200/mes ($2000 anuales), fondo de cuota 50x; adecuado para equipos principales de alta frecuencia.
- **El nivel Plus de $8/mes ($80 anuales) no incluye la función Bot**, asegúrese de no elegirlo por error. Si ya dispone de una versión de pago de Cursor (Personal o Teams), una suscripción a SuperGrok o un asiento de Grok Business, también puede utilizarlo directamente.

  El cliente de escritorio es compatible con macOS, Windows y Linux; la versión móvil es compatible con iPhone, iPad y Android. Inicie sesión con su cuenta tras la instalación.

### Crear un Bot y asignar una tarea de prueba

1. Haga clic en **+** en la barra lateral (o Cmd+N) para crear un Bot y asígnele el nombre «Investigador de la competencia». Los Bot personales ya no cuentan con Description; envíe las siguientes seis líneas en la conversación y pídale que las recuerde; para los Bot compartidos, escríbalas en la Description dentro de About en los detalles.
```text
Own: 负责监控目标清单的每周功能更新与定价变动
Sources: Notion 中的关注名单、目标官网 Changelog 页面
Output: 不超过 8 条核心动态，附带日期与原始链接，存入 /workspace/scan.md
Approval: 严禁对外发布任何内容，严禁主动发送任何邮件
Failure: 若目标页面无法打开，在报告中明确标为数据缺失，严禁推测或编造内容
Never: 在源系统可访问时，严禁依赖自身记忆给出概括
```
2. Envíe la instrucción de prueba en el cuadro de chat, especificando los cinco elementos: objetivo, fuente, restricciones, formato y puntos de confirmación.
```text
调研所附竞品清单中的前 3 个产品官网。
比对它们过去两周内的功能更新与价格调整。
跳过无任何变动的模块。
提取核心变动点，整理成 Markdown 表格，并直接保存到 /workspace/scan.md。
在对话框中仅回复处理状态与保存路径；不要对外发送任何通知，不要擅自更改系统设置。
```
3. **Observe la ventana de la computadora en la nube a la derecha**. El Bot abrirá automáticamente el navegador en la nube para extraer las páginas y escribirá el contenido en el archivo especificado.

### Configurar aprobaciones de seguridad y rutinas programadas

1. Vaya a Settings → General → Auto-review; **todas las operaciones de alto riesgo deben configurarse obligatoriamente en Ask first**.

   Bloquee estrictamente el envío de mensajes (`send`), publicaciones (`post`), pagos (`buy`), eliminación de archivos (`delete`, incluidos `/workspace` o archivos locales) y modificación de permisos (`permissions`); una vez activados, se desplegará una tarjeta para pausar el proceso a la espera de su aprobación manual.
2. Una vez que la tarea de extracción se ejecute de manera estable dos veces consecutivas, envíe la instrucción de consolidación en el cuadro de chat.
```text
把刚才已经跑通的竞品页面抓取与格式整理流程保存为一个 Skill，名称叫「竞品动态巡检」。
写清调用条件、所需权限、抓取步骤、异常报错逻辑与产出文件格式。
```
3. Cambie la dirección URL de la competencia e introduzca `/` para invocar y probar este Skill. Tras comprobar que es correcto, **configure un Routine programado** para que se ejecute automáticamente todos los lunes a las 9:00 de la mañana, enviando el informe de resultados en la conversación actual y guardando el informe detallado en `/workspace`.

## Errores comunes y precauciones

### Arquitectura y seguridad

- No siga ciegamente la tendencia al ver arquitecturas comunitarias de 29 Bot (declarado por Melvin Vivas, no verificado); los Bot homogeneizados generan confusión fácilmente y consumen cuota. **No cree un segundo puesto antes de que el primero funcione de manera fluida**.
- Todos los Bot comparten la computadora en la nube y el sistema de archivos; los rastreadores pueden leer `/workspace` y cookies. **El control de seguridad depende exclusivamente del control de aprobación manual Ask first**.
- No envíe nombres de usuario ni contraseñas en el cuadro de chat. Ante una pantalla de inicio de sesión, **abra la pantalla derecha y haga clic en el botón Take over para iniciar sesión manualmente**.

### Recursos y expectativas

- El nivel Plus de $8 al mes no cuenta con acceso a Bot; **debe recurrir obligatoriamente al nivel Premium a partir de $30 al mes**.
- Configurar una Routine con sondeo cada 5 o 10 minutos agotará el fondo de cuota semanal. **Debe ampliar el intervalo de las tareas programadas y añadir una lógica de salida cuando no haya actualizaciones**.
- No crea ciegamente en los mitos de rentabilidad de Alex Finn o de reducción de costos de 0xkvro (declaraciones propias, no verificadas); **guíe su negocio según métricas realmente validadas**.

## Cómo verificar tras completar la configuración

1. Haga clic en el Bot en la barra lateral para entrar al chat, envíe un mensaje para desplegar el **escritorio en tiempo real de 1920×1200**; vaya a Usage & Billing para confirmar que el plan sea Premium, Super o Ultra, y que la barra de progreso funcione con normalidad.
2. El contrato de seis líneas debe especificar claramente las responsabilidades, las fuentes de datos, los entregables, las líneas rojas de aprobación y la gestión ante falta de datos (**seis restricciones estrictas**). En los Bot personales, envíelo en la conversación para que lo recuerde; en los Bot compartidos, escríbalo en About en los detalles. Pruébelo enviando un enlace caído: **debe reportar la falta de datos con veracidad** sin inventar información.
3. En Settings → General → Auto-review, configure `send`, `post`, `buy`, `delete` y `permissions` en Ask first. Pruebe enviando un correo o eliminando un archivo: **debe mostrar obligatoriamente una tarjeta de aprobación a la espera de confirmación manual**.
4. Tras hacer clic derecho en Test run de la Routine y completarlo con éxito, cierre la tapa y la aplicación. Al llegar la hora programada, vuelva a abrir para revisar las notificaciones y acceda a `/workspace` en la computadora en la nube para **confirmar que el archivo Markdown o CSV se haya actualizado según la marca de tiempo más reciente**.

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 5 Computadora en la nube compartida: Archivos, navegador y control manual](/part1/05-computer)
- [Capítulo 6 Memoria: Haga que su Bot lo entienda mejor con el uso](/part1/06-memory)
- [Capítulo 7 Conectar aplicaciones: Extensiones, correo y Secrets](/part1/07-apps)
- [Capítulo 11 Permisos, seguridad y controles manuales](/part1/11-safety)
- [¿Qué diferencia hay entre Grok y Grok Bot?](/part1/grok-vs-grok-bot)
- [Capítulo 2 Planes y suscripciones: Elija el nivel adecuado](/part1/02-plans)

### Páginas y documentación oficiales

- [Guía de inicio rápido de Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started)
- [Uso de Grok Bot: Computadora, aplicaciones y tareas](https://cursor.com/cn/docs/grok-bot/work)
- [Casos de uso y roles típicos de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)
- [Grok Bot para equipos y empresas](https://cursor.com/cn/docs/grok-bot/teams)
- [Planes y facturación de Grok Bot](https://cursor.com/cn/help/grok-bot/plans)
- [Normas de uso para Bot de equipo](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- [Arquitectura de seguridad y reglas de Auto-review de Grok Bot](https://cursor.com/cn/docs/grok-bot/security)

### Prácticas de la comunidad y comparativas horizontales

- [«1.1 Qué es Grok Bot: Entiéndalo en una página»](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [«1.2 Cómo elegir entre Grok Bot, Muse, Hermes, dots y Cue»](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd)
- [«Colección de tweets de 铁柱 ④: Comunidad, ecosistema y comparativa con competidores»](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg)
- [«Artículo extenso | Grok Bot de cero a experto | 金尘马»](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
