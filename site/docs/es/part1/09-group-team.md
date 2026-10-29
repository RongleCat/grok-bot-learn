# Capítulo 9 Chats grupales y Team Bots: de un Bot a un grupo de Bots

No le cargues todo el trabajo a un solo Bot ni **metas varios Bots en un grupo**. Varios Bots tienden a responderse entre sí, provocando activaciones en bucle que pueden agotar la cuota de toda la semana; además, los Bots personales no pueden colaborar al entrar en Slack.

1. Utiliza un **Bot coordinador como punto único de entrada** y apóyate en el traspaso de tareas mediante archivos compartidos entre el equipo local y el ordenador en la nube.
2. Cuando necesites compartir experiencia con todo el equipo, publica un Team Bot.
3. Controla el consumo según el mecanismo de suscripción unificada The X Subscription, vigente desde el 12 de octubre de 2026.


![Chats grupales y Team Bots: de un Bot a un grupo de Bots](/info/09-group-team.png)

## Mecanismos de chat grupal y reglas de interacción: cómo colaboran múltiples Bots en una misma conversación

![Mecanismos de chat grupal y reglas de interacción: cómo colaboran múltiples Bots en una misma conversación](/info/09-group-team-s1.png)

Los chats grupales permiten agregar varios Bots, pero **los Team Bots no pueden estar en el mismo grupo que los Bots locales**.

Por defecto, al enviar un mensaje responderán todos; para especificar uno, usa `@Bot名称`. En tareas complejas, las transferencias entre Bots por chat privado no se sincronizan con el grupo.

Si te preocupa que los chats privados queden dispersos, establece reglas directas:
- **Restricción temporal**: envía una instrucción en el grupo.
```text
就在群里回复，这件事不要私信我。
```
- **Restricción a largo plazo**: pídele que lo guarde en la memoria a largo plazo.
```text
记住：在群组聊天中，要在群里回复。
```

El sistema no dispone de un interruptor para desactivar los diálogos entre Bots con un solo clic. Para evitar llamadas en cadena que desperdicien la cuota, recurre a estos métodos:
1. **Prohibición temporal**: envía una instrucción en el grupo.
```text
不要给其他 Bot 发消息，先问我。
```
2. **Regla a largo plazo**: exige que esté terminantemente prohibido activar a otros Bots en privado sin confirmación previa.
3. **Parada de emergencia**: si no se detiene, **entra a su chat privado exclusivo y ordénale parar**.
4. **Silenciamiento auxiliar**: desactiva las notificaciones o haz clic derecho en la barra lateral en Hide from sidebar.

Gestión y limitaciones:
- **Cambiar de nombre y redirigir el enfoque**: clic derecho en Rename chat (en el móvil, pulsa en el nombre del grupo y selecciona Edit name); para cambiar el enfoque, indícalo directamente en el grupo.
- **Limitaciones de funciones**: **los chats grupales no admiten voz en absoluto** (solo disponible en chats individuales), y no es posible activar o desactivar notificaciones para un Bot específico.

Criterios de aceptación:
- Menos de 3 miembros y sin solapamiento de responsabilidades.
- Para preguntar, usa `@` para invocar con precisión.
- Las respuestas se concentran dentro del grupo, sin chats privados innecesarios.
- No se producen activaciones en bucle entre Bots.

## Comunicación entre Bots y enrutamiento de permisos en Slack

**Un Bot solo puede enviar mensajes entre robots cuando actúa en representación de una persona específica.** Los Bots personales no tienen derechos de representación en un Thread público y no pueden despertar a otros Bots; cuando se menciona a un Team Bot con @, este asume la identidad de quien pregunta, transfiere la tarea a su propio Bot exclusivo y luego devuelve los resultados al mismo Thread.

| Tipo de Bot | Ubicación de la consulta | Permisos entre Bots | A quién representa | Ubicación de la respuesta |
| --- | --- | --- | --- | --- |
| Bot personal | Chat privado en la app / Mensaje directo en Slack | Puede enviar | Persona | Ventana de chat en la app (no en Slack) |
| Bot personal | Thread público de Slack | No puede enviar (avisa que no se puede ejecutar) | Nadie | Hilo del mensaje original |
| Team Bot | Canal / Mensaje directo de Slack | Puede enviar (transfiere al Bot exclusivo del consultante) | Miembro que pregunta | Devuelve al mismo hilo de Slack |

[Consulta las reglas detalladas en la documentación oficial](https://cursor.com/cn/help/grok-bot/group-chats).

### Integración de Team Bots y resolución de problemas comunes

1. Tras publicar el Team Bot, el propietario debe hacer clic en el nombre del Bot en la parte superior del chat y, en Bring to your team's Slack, pulsar en Connect (si aún no se ha publicado, se mostrará atenuado Connect after publishing).
2. Si la interfaz muestra Awaiting admin approval, significa que el control de seguridad está habilitado; contacta al administrador para su aprobación. Cuando el estado cambie a Connected, la vinculación se habrá completado con éxito.
3. **Antes de usarlo, los miembros del equipo deben vincular su cuenta haciendo clic en Link en el cliente bajo Settings > General > Team Bots.** Si envías un mensaje directamente en Slack sin haber vinculado la cuenta, el Bot solo responderá con un recordatorio de vinculación.

### Criterios de aceptación

- La colaboración de múltiples Bots dentro del canal de Slack es programada y coordinada de forma unificada por el Team Bot.
- Los miembros del equipo completan el Link de sus cuentas.
- **Las tareas se completan en un ciclo cerrado dentro del Thread, sin desconexiones ni errores de permisos.**

## Configuración de flujo completo para Team Bots: creación, publicación y uso compartido entre personas

Los Team Bots son creados por los miembros y compartidos con todo el equipo, manteniendo los chats privados aislados entre sí. **Solo se ejecutan en la nube y no pueden vincularse localmente**.[Consulta la guía oficial](https://cursor.com/cn/help/grok-bot/shared-bots.md).

### Creación y conversión a Team Bot

1. Haz clic en la barra lateral en New chat (+), y selecciona Create new Team Bot.
2. Explica los requerimientos y configura los plugins públicos, Secrets y archivos.
3. Cambia el nombre y completa About. **Si mantienes el nombre predeterminado y la descripción está vacía, los demás miembros no podrán encontrar este Bot en la lista**.
4. Haz clic en Publish to Team en la tarjeta.

Para un Bot personal ya existente, puedes hacer clic en la interfaz en Share > Publicar en el equipo para clonar una copia independiente, generar una cuenta de Slack y migrar secretos, memoria y rutinas (Routines) según lo requieras.

### Búsqueda e invocación

- **Búsqueda y lista**: explora seleccionando Team Bots en New chat (+), o escribe los primeros 3 caracteres del nombre en el cuadro de búsqueda.
- **Acceso directo mediante enlace**: haz clic derecho y selecciona Copy link. Todo el equipo comparte la base y la memoria subyacente; no es una plantilla clonada.
- **Distribución por lotes**: los administradores pueden marcar Auto-add en el panel de control Manage Team Bots. **Para los miembros marcados, el Bot se fijará automáticamente en la parte superior de la barra lateral y no se podrá ocultar**.

### Permisos y mecanismos de ejecución

Al invocar una cuenta personal, se activa la autorización Allow (Allow once solo para esta vez, Always allow para permitir siempre, Skip para omitir). Para restablecerlo, ve a Settings > General > Team Bots y pulsa Clear.

**La tarjeta de aprobación solo aparece en el chat privado del propietario**. En los chats grupales y en Slack, el Bot únicamente puede operar de forma autónoma.

| Escenario | Entorno de ejecución |
|---|---|
| Chat privado | Ordenador en la nube personal por defecto (si la privacidad es estricta, se asigna una máquina aislada) |
| Slack / Chat grupal | Máquina virtual compartida dedicada |

### Criterios de aceptación

- El nombre y la descripción del puesto son claros.
- Los secretos del propietario están debidamente aislados.
- Se puede invocar mediante búsqueda de 3 caracteres o enlace.
- Las invocaciones entre distintos usuarios activan la autorización Allow, sin riesgos de escalada de privilegios.

## Modelo de asignación de tareas 1+N con Bot principal: punto único de entrada y estatutos de cumplimiento

![Modelo de asignación de tareas 1+N con Bot principal: punto único de entrada y estatutos de cumplimiento](/info/09-group-team-s4.png)

No dejes que todos los Bots interactúen directamente con el usuario, para no tener que andar transmitiendo mensajes entre ventanas ni desperdiciar tokens en el chat grupal.

**Se recomienda adoptar el modelo 1+N, donde solo te comunicas con el Bot principal coordinador**, y este se encarga de desglosar, asignar tareas y consolidar los resultados; consulta para más detalles [«De un solo Bot a toda una organización: uso avanzado de Grok Bot para conectar ordenadores locales, división de tareas de IA y bases de conocimiento»](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg).

### Estatutos de seis líneas del Bot principal y límites especializados

**El Bot principal solo se encarga del enrutamiento y la supervisión; nunca debe escribir código largo ni textos extensos por sí mismo.** En el caso de un Bot personal, envía los estatutos de seis líneas en el diálogo y pídele que los recuerde; en el caso de un Bot compartido, escríbelos en el campo Description de los detalles About. Debe mantenerse en silencio cuando no haya tareas, delegar cuando haya trabajo pendiente y guardar los informes excesivamente largos como archivos.

Para consultar las normas de organización del equipo, revisa [«4.2 Orquestación de equipos: estatutos, roles y delegación de autoridad»](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh).

```text
Own: 负责需求的统一拆解、分派、汇总与五行简报汇报。
Sources: 人工下发的指令、项目看板文件。
Output: 纯文本状态摘要，超出五行时输出为指定文件路径。
Approval: 任何对外通信、采购、删除操作必须暂停等待确认。
Failure: 下游专职 Bot 报错时如实上报，不使用过期数据假装完成。
Never: 永远不直接编写业务代码，不擅自修改生产配置。
```

Para los Bots especializados, debes enviarles sus límites negativos para que los recuerden (en Bots compartidos, escríbelos en el About de detalles):
- Bot de gestión de anuncios: analiza datos y genera listas pendientes de aprobación; **nunca toca el panel de administración ni las pujas, no ajusta presupuestos ni añade palabras clave ni crea grupos**.
- Bot de redacción publicitaria: solo genera archivos de borrador, con prohibición estricta de llamar a APIs para publicar contenido directamente.
- Bot de investigación de la competencia: en el frontend solo mira sin interactuar; tiene estrictamente prohibido realizar pedidos, añadir al carrito, dejar reseñas o hacer preguntas a los vendedores, para evitar bloqueos por medidas antirrastreo.

Los especialistas en publicidad pueden aplicar directamente la plantilla de prompt.

```text
Own: 负责广告投放数据诊断与策略输出。
Sources: 运营分析文件 /workspace/project/ad_data.json。
Output: 待批操作清单 /workspace/project/pending_actions.md，列出出价建议与预期影响。
Approval: 绝不直接写入广告后台，不修改出价，不修改预算，不加否定词，所有操作必须等待人工审批。
Failure: 数据缺失时明确标注缺失字段，不推测填充。
Never: 绝不执行任何后台写入与线上提交操作。
```

### Listas pendientes de aprobación y aceptación

**Los Bots especializados solo generan listas estructuradas pendientes de aprobación, dejando el poder de decisión al ser humano.** Por ejemplo, si el Bot principal resume 5 conflictos de pujas publicitarias, el siguiente paso solo se activará después de que respondas "confirmar sugerencias" o anotes modificaciones.

Una vez que el sistema cumpla con los estándares, se evalúa conforme a tres criterios de aceptación:

| Elemento de aceptación | Criterio de cumplimiento |
| --- | --- |
| Interacción y Bot principal | Funcionamiento claro con un único punto de entrada; el Bot principal no escribe código largo ni textos extensos |
| Bots especializados | Cada uno cumple su función y solo genera listas estructuradas |
| Acciones de alto riesgo | Todas las operaciones irreversibles cuentan con un punto de control explícito para confirmación humana |

## Convenciones de archivos de traspaso: sustituir el historial de diálogo por un sistema de archivos compartido

![Convenciones de archivos de traspaso: sustituir el historial de diálogo por un sistema de archivos compartido](/info/09-group-team-s5.png)

No permitas que el Bot A pegue resultados en la ventana de chat para que el Bot B los lea. **La interacción mediante ventanas satura rápidamente el contexto y provoca fácilmente la pérdida de historial**; además, las conversaciones de cada Bot están aisladas lógicamente a bajo nivel y no pueden consultarse entre sí.

| Dimensión | Características y contenido incluido |
| :--- | :--- |
| **Capa física compartida** | Todos los Bots bajo la misma cuenta comparten la máquina virtual, el directorio `/workspace`, los conectores y la biblioteca pública de Skills. |
| **Capa de aislamiento lógico** | Los historiales de diálogo son mutuamente invisibles; el Bot A no puede acceder a las conversaciones privadas entre el Bot B y el usuario. |

Puesto que el disco físico es compartido, la transmisión de tareas se realiza mediante archivos estructurados locales, y las ventanas de chat solo se utilizan para sincronizar estados y rutas.

### Estándar del pipeline de traspaso de archivos

El traspaso estándar abarca el guardado en disco, la transmisión de la ruta y, finalmente, la lectura y el archivado.

::: details Estándar del pipeline de traspaso de archivos
```
[用户指令] ──> (主调度 Bot)
                   │
         1. 派发任务 (指定输出路径)
                   │
                   ▼
             [专职 Bot A] ──> 写入 /workspace/proj/data.json
                   │
         2. 交付：仅返回文件绝对路径
                   │
                   ▼
             (主调度 Bot)
                   │
         3. 调度下发 (附带输入路径)
                   │
                   ▼
             [专职 Bot B] ──> 读取 data.json ──> 写入 output.md
                   │
         4. 汇总简报至用户
```
:::

1. **Asignación de tareas**: el Bot principal especifica claramente la ruta absoluta de entrega, como `/workspace/project-alpha/data.json`.
2. **Guardado de datos en disco**: el Bot especializado A completa la limpieza, escribe los datos en el archivo y, en la ventana de chat, responde con una sola frase notificando la ruta de guardado.
3. **Transmisión y lectura de ruta**: el Bot principal activa al Bot B y le pasa la ruta; tras leer el disco y realizar el análisis, el Bot B escribe las conclusiones en `/workspace/project-alpha/report.md`.
4. **Presentación de la entrega**: el Bot principal extrae un resumen y adjunta el enlace al documento local o en la nube para su revisión.

El pipeline de perfilado de tuits también sigue este modelo: el recopilador captura y guarda en `tweets.md`, el analista lee el archivo para extraer etiquetas y las escribe en `profile.md`, el diseñador genera `design.md`, y el ingeniero escribe código basándose en este y proporciona capturas de pantalla de vista previa.

Para la práctica operativa, consulta [«4.2 Orquestación de equipos: estatutos, roles y delegación de autoridad»](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh).

### Integración con documentos en la nube de Feishu para entregas con trazabilidad

Cuando se requiera colaboración en equipo o anotaciones, configura la CLI de Feishu en la máquina virtual para publicar Markdown como documentos en la nube. Incluye un enlace independiente que facilita la distribución, permite comentarios párrafo por párrafo y además **garantiza la seguridad de los datos empresariales**.

El cumplimiento del flujo de trabajo incluye los siguientes requisitos:
- Cada Bot en la cadena puede leer y escribir de forma independiente en los archivos designados dentro de `/workspace`.
- **La ventana de chat solo transmite avisos de estado y rutas absolutas de archivos**.
- Ante cualquier anomalía, basta con revisar el archivo correspondiente en el disco para reproducir y localizar el problema.

## Impacto en el consumo y control de cuotas: gobernanza de múltiples Bots bajo The X Subscription

A partir del 12 de octubre de 2026, Grok Bot se integra en The X Subscription, con **una cuota compartida unificada de forma semanal**.

| Nivel | Precio |
| :--- | :--- |
| Premium | $30/mes |
| Super | $100/mes |
| Ultra | $200/mes |

### Reglas y estrategias para evitar el consumo desmedido

1. **Tanto las respuestas como los mensajes de saludo/apretón de manos (handshake) se facturan**. En los chats privados con Team Bots se descuenta de tu propia cuota, mientras que en los chats grupales se descuenta de la del iniciador; si se agota a principios de semana, todo queda paralizado durante el resto de la semana.
2. Mantén los Bots en chats grupales en menos de 3 y **sustituye decididamente el chat grupal libre por el modelo serial 1+N**.
3. Usa modelos básicos para tareas ligeras como la limpieza de datos, y reserva los modelos de razonamiento de primer nivel para deducciones clave.
4. Antes de que el flujo funcione de manera estable, **no configures rutinas programadas cada media hora o cada hora**, para evitar que cientos de reintentos nocturnos agoten la cuota.

### Criterios de aceptación

- **Consumo equilibrado de la cuota semanal**, sin bucles infinitos nocturnos.
- Estratificación clara de modelos y distribución del gasto asignada a cada persona que pregunta.

## Casos prácticos: consolidación de la experiencia de expertos empresariales e implementación de 1+N en equipos transfronterizos

### Team Bots de SpaceXAI
El equipo de n2parko **hizo que los propios expertos del negocio configuraran las reglas del Bot**, convirtiéndolos en asistentes compartidos para todo el equipo.
1. Captura de nodos de alta frecuencia: el equipo de datos creó Databot para consultar el lago de datos (data lake), evitando interrumpir repetidamente a los expertos.
2. Expansión de puestos: configuraron 10x Engineer, Marketing y Sales Assistant para consultar Salesforce (asistencia a SDR/AE).
3. Estratificación de memoria: consolidación global de reglas generales manteniendo las preferencias individuales; consulta para más detalles [«Meet your Team Bots｜n2parko»](https://jcng5q8n0f3z.feishu.cn/wiki/KS9Cwan52idy1xkLbnTcSC3xnxb).

### Orquestación 1+12 transfronteriza
Zach (@1999Zach22) organizó 1 capitán al frente de 12 puestos: **el ciclo cerrado automatizado debe contar obligatoriamente con listas pendientes de aprobación**, controlando estrictamente los permisos de escritura.
1. Despliegue local: una vez optimizada y calibrada la Skill dedicada en el entorno local, se despliega de manera unificada en el ordenador en la nube.
2. Límites negativos: los gestores de campañas tienen estrictamente prohibido operar en el panel de control y solo pueden hacer sugerencias; las cuentas de compradores para investigación tienen estrictamente prohibido añadir al carrito, hacer preguntas o dejar valoraciones.
3. Interacción con punto único de entrada: consolidación diaria en informes breves; si surgen discrepancias, se genera una lista de 5 puntos de conflicto pendientes de aprobación para ejecutar tras su confirmación.
4. Consolidación de informes: uso de la CLI de Feishu para convertir informes en enlaces permanentes de documentos en la nube; consulta [«De un solo Bot a toda una organización: uso avanzado de Grok Bot para conectar ordenadores locales, división de tareas de IA y bases de conocimiento»](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg).

## Errores y trampas comunes

1. Si no puedes definir una habilidad distintiva en tres palabras, **intégrala como una Skill del Bot principal**. No crees siete u ocho asistentes de funciones difusas de golpe, para no pasarte el día saltando entre ventanas.
2. Todos los Bots bajo la misma cuenta comparten la máquina virtual en la nube, las rutas locales y la sesión iniciada del navegador; **nunca almacenes credenciales privadas personales en un Bot compartido**.
3. No des instrucciones demasiado genéricas en el grupo. Los Bots intercambiando cortesías y confirmaciones consumirán cuota masivamente, **pudiendo agotar en medio día el volumen de llamadas de toda la semana**.
4. No publiques manteniendo el nombre predeterminado `New team bot` y sin redactar una descripción, **pues los demás miembros no podrán verlo en absoluto en la lista de búsqueda**.
5. Los Team Bots y los Bots locales no pueden unirse al mismo grupo, y los grupos no disponen de acceso de voz. **Si tienes tales necesidades, debes cambiar obligatoriamente a un chat privado individual con el Bot**.
6. Escribir miles de líneas de código llenará el contexto y hará que se pierda la visión global. **El Bot principal debe encargarse únicamente de la programación y supervisión**, delegando las acciones de ejecución a los Bots especializados.

## Cómo verificar tras finalizar

1. **Enrutamiento del Bot principal**: al enviar una instrucción de negocio multimodular, el Bot principal debe **repetir con precisión el objetivo y listar las rutas de los Bots especializados**, manteniéndose en silencio cuando no haya cambios de estado externos.
2. **Prevención de mensajes cruzados en chats grupales**: al ordenar "no envíes mensajes a otros Bots", **el Bot solo debe responder dentro del grupo**, sin enviar mensajes emergentes en ventanas de chat privado ni activarse mutuamente en privado.
3. **Búsqueda y autorización**: cambia a la cuenta de Cursor de otro miembro y en **New chat** > **Team Bots** busca por los **primeros 3 caracteres**; al invocar plugins debe mostrarse obligatoriamente la tarjeta de autorización con **Allow once**, **Always allow** y **Skip**.
4. **Traspaso de archivos**: el Bot A almacena los archivos intermedios en `/workspace`, y **el Bot B completa la ejecución de forma independiente solo mediante la ruta absoluta**, sin requerir copias manuales en ningún momento.
5. **Control de compuerta humana**: al emitir instrucciones de publicación, modificación en el panel o eliminación, **el Bot debe detener la ejecución y generar una lista pendiente de aprobación**, sin escribir nunca en producción sin aprobación humana.

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 22 Integración con Feishu y WeChat](/part3/22-feishu-wechat)
- [Capítulo 24 Construye tu equipo de IA según los puestos](/part4/24-roles)

### Documentación oficial
- [Chats grupales y mensajería entre robots](https://cursor.com/cn/help/grok-bot/group-chats)
- [Team Bots](https://cursor.com/cn/help/grok-bot/shared-bots.md)

### Fuentes prácticas de la comunidad
- [«Meet your Team Bots｜n2parko»](https://jcng5q8n0f3z.feishu.cn/wiki/KS9Cwan52idy1xkLbnTcSC3xnxb)
- [«De un solo Bot a toda una organización: uso avanzado de Grok Bot para conectar ordenadores locales, división de tareas de IA y bases de conocimiento»](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- [«4.2 Orquestación de equipos: estatutos, roles y delegación de autoridad»](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
