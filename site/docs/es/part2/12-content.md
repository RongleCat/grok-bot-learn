# Capítulo 12 Caso práctico: Medios digitales y equipos de contenido

La IA conversacional suele perder contexto; **Grok Bot utiliza archivos compartidos en una computadora en la nube para ejecutar pipelines**.

1. Redactar descripciones de roles y construir un banco de temas basado en seis grupos de campos obligatorios.
2. El Bot de investigación escribe fichas en el directorio, y el Bot redactor principal las lee para redactar el borrador.
3. Implementar reglas de corrección para eliminar el tono robótico de IA y transformar publicaciones en un sitio web de perfil personal.
4. **Los puntos clave de publicación deben contar obligatoriamente con supervisión humana**, evitando datos falsos y controles de riesgo de las plataformas.

## Diseño de puestos y mecanismos de colaboración en el equipo de contenido

![Diseño de puestos y mecanismos de colaboración en el equipo de contenido](/info/12-content-s1.png)

### Qué es

**Al crear un equipo en Grok Bot, el núcleo es «un puesto, una sola responsabilidad».** Todos los Bots bajo la misma cuenta comparten la misma computadora en la nube (con kernel independiente, memoria y la ruta `/workspace`), pero cada uno cuenta con ventanas, memoria y configuraciones independientes.

Los Bots se traspasan tareas leyendo y escribiendo archivos Markdown en carpetas compartidas.

### Cómo hacerlo

El **Bot principal con una estrella en su avatar (clic derecho en el avatar para alternar)** se encarga de coordinar y asignar tareas, mientras que de 5 a 6 Bots dedicados trabajan estrictamente dentro de los límites de sus responsabilidades.

| Nombre del puesto | Ruta de entrega | Responsabilidades clave y acciones prohibidas |
| :--- | :--- | :--- |
| Explorador de inteligencia | `/workspace/content-team/01-inbox/` | Recopilar pistas de primera mano. Prohibido interactuar, publicar y enviar mensajes directos; estrictamente prohibido tratar comentarios de segunda mano como hechos |
| Planificador de temas | `/workspace/content-team/02-briefs/` | Evaluar pistas y generar Briefs. Prohibido navegar externamente; no avanzar al redactor principal sin aprobación humana |
| Redactor principal | `/workspace/content-team/03-drafts/` | Escribir según `voice.md`. Prohibido inventar hechos y usar tono genérico de relaciones públicas |
| Editor de hechos | `/workspace/content-team/04-review/` | Verificar fuentes de primera mano. Sin permisos de publicación; listar conflictos de evidencia como pendientes de confirmación |
| Analista de métricas | `/workspace/content-team/06-analysis/` | Analizar métricas de contenido. Prohibido interactuar desde la cuenta, convertir correlaciones en causalidad o hacer conjeturas ante la falta de datos |
| Ingeniero web | `/workspace/tweet-portrait/` | Sintetizar el perfil y crear el sitio. Prohibido falsificar experiencias o tratar rutas locales como enlaces públicos |

1. Crear la estructura estándar de directorios compartidos en la terminal de la computadora en la nube.
::: details Cómo hacerlo
```text
/workspace/content-team/
├── 00-profile/     # 账号定位、目标读者、范文、禁用表达（voice.md）
├── 01-inbox/       # 情报侦察员的一手信息卡
├── 02-briefs/      # 选题策划师的选题 Brief
├── 03-drafts/      # 内容主笔的候选稿
├── 04-review/      # 事实编辑的审校稿
├── 05-published/   # 已发布文案存档、数据截图或 CSV
└── 06-analysis/    # 数据复盘师的周报与实验记录
```
:::
2. Escribir la base de estilo en `00-profile/voice.md` para evitar que el redactor principal genere clichés.
::: details Cómo hacerlo
```text
# 账号定位
- 我长期写：面向个人创业者与开发者的 AI 工具实测与提效工作流
- 我的目标读者：正在用 AI 尝试做独立产品、做内容或做业务转型的实干者
- 读者看完后应该获得：直接能照着执行的步骤、准确的参数配置、明确的避坑提醒

# 写作样本
- 代表作 1：【粘贴一段自己数据最好、语言最顺的代表作】
- 代表作 2：【粘贴一段带步骤拆解的教程代表作】

# 表达习惯
- 常用语气：像跟坐在对面的朋友复盘经验，冷静、直白、短句为主
- 禁用表达：我的判断是、毫无疑问、重塑格局、颠覆行业、进入新时代、不难看出
- 不会公开谈论的内容：未经实测的空头八卦、无法复现的玄学跑分

# 商业与事实边界
- 必须保留原始来源的主张：所有关于产品上线、价格变动、官方改版的陈述
- 未亲测时的写法：必须显式标明“未核实”或“作者自述”
```
:::
3. **Crear el grupo y distribuir las reglas**. Haz clic en «Nuevo chat» para crear el grupo «Equipo de contenido digital» e incorpora a todos los miembros. La primera vez, evita asignar temas directamente; primero debes enviar las normas unificadas.
```text
这是“自媒体内容团队”协作群。工作顺序固定为：情报侦察员 → 选题策划师 → 内容主笔 → 事实编辑；内容发布后，数据复盘师读取授权数据 → 06-analysis。所有中间文件放到 /workspace/content-team/ 对应目录。任何登录、外发、发布、点赞、回复、关注、私信、购买、删除、连接器授权或权限修改都必须先获得用户明确批准。本次仅确认收到和各自交付路径，不执行外部操作。
```

### Criterios de éxito

> Fuente: [Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso](https://x.com/AdrianPunk115/status/2097311704547987756)  
> Autor: [Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso](/cases-img/fs26-0.jpg)

![Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso](/cases-img/fs26-1.jpg)

1. El perfil, las etiquetas y las responsabilidades a largo plazo de cada Bot están guardados, y la lista de prohibiciones es clara.
2. El árbol de directorios de `/workspace/content-team/` está completo, y en `00-profile/voice.md` se han registrado el posicionamiento real y las palabras prohibidas.
3. **Todos los miembros han respondido confirmando sus rutas de entrada/salida y los límites de supervisión humana**, y ninguno afirma tener permisos para publicar automáticamente o acceder a redes externas.

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

## Práctica de todo el flujo: Selección de temas, redacción, imágenes y distribución

![Práctica de todo el flujo: Selección de temas, redacción, imágenes y distribución](/info/12-content-s2.png)

### Selección de temas e inteligencia: Extracción, métricas y desglose de motivaciones

> Fuente: [Cómo aprovechar Grok Bot para creadores de contenido](https://x.com/KinGao476942/status/2099736121781764594)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

Para buscar temas, no converses directamente con un modelo generalista: solo arrojará noticias desactualizadas. En su lugar, haz que el Bot explorador simule búsquedas o monitoree tendencias y organice las pistas en fichas.

Configura primero el prompt de rol permanente para el explorador:

::: details Selección de temas e inteligencia: Extracción, métricas y desglose de motivaciones
```text
你是我的情报侦察员（Scout）。唯一职责是发现、核验并沉淀可用于选题的公开信息，为后续选题提供证据；不写成稿，不替用户下结论。

【允许使用】
- 公共互联网中的官方公告、产品文档、论文、GitHub Release、作者原文与用户提供材料。
- 知乎、微博、X、小红书等平台的公开页面、公开帖子和公开评论区，可用于搜索线索、观察讨论和摘录公开信息。
- 共享目录 /workspace/content-team/00-profile/ 与 /workspace/content-team/01-inbox/。
- 如页面要求登录、密码、验证码、2FA、passkey，或需要扩大权限，必须立即停下并请求用户接管。

【禁止】
- 不得发帖、改帖、删帖、点赞、转发、收藏、关注、取关、评论、回复或私信。
- 不得读取私信、好友可见内容、非公开页面或与任务无关的个人数据。
- 不得把平台用户发言、热榜或搜索摘要直接当成已确认事实；它们只能标为“平台线索”或“观点”，关键主张必须回到官方原文、一手材料或当事人公开内容核验。
- 不得凭记忆补数字、日期、引语或因果。
- 不得索取或记录账号密码与验证码。
- 不得执行本机命令，不得访问本机文件。

【固定交付】
写入 /workspace/content-team/01-inbox/YYYY-MM-DD.md，每次最多 8 条。每条包含：事实或平台线索、来源平台、原始链接、证据摘录、讨论热度或代表性观点、为什么值得关注、一个待核查问题、核验状态。
```
:::

**El banco de temas debe incluir obligatoriamente seis grupos de campos fijos**; si falta uno, se descarta de inmediato:
- Fuente y frescura: Enlace permanente accesible a la publicación original, hora de publicación y tiempo transcurrido desde entonces; no escribir «cierto blogger».
- Métricas visibles: 4 datos consistentes en visualizaciones/reproducciones, «me gusta», compartidos y comentarios, junto con la hora de extracción. Si no se encuentran, marcar como «datos públicos no encontrados»; estrictamente prohibido estimar.
- Nivel del autor: Registrar handle, recuento de seguidores y categoría. De cuentas pequeñas con publicaciones virales se aprende la estructura; de los grandes referentes se analizan las temáticas.
- Segmento de la comunidad: Clasificar explícitamente en oficial, nacional o internacional.
- Motivo de idoneidad y ángulo de ejecución: Vincular con fortalezas propias y detallar acciones concretas (como hacer pruebas reales, añadir pasos o proporcionar plantillas), evitando adjetivos vacíos como «es muy popular».
- Desglose de motivaciones: Abarcar puntos de dolor, gratificaciones inmediatas e incentivos de interacción. Las deducciones sin respaldo de datos deben marcarse al final como «inferencia».

El planificador selecciona 3 temas de alto valor desde `01-inbox/`, filtrándolos a través de tres filtros: hechos concretos, relevancia para el lector y propuesta de valor del autor, generando un Brief que se guarda en `02-briefs/`:

```text
读取今天 01-inbox 中已经核验的线索，按照账号定位筛选 3 个候选题，写入 02-briefs/YYYY-MM-DD.md。每题包含：一句话事实、读者场景、单一主角度、原始链接与证据、信息缺口、建议内容形式、给主笔的写作任务。证据不足的题直接标“待补证”。完成后停下，等待我批准，不要通知内容主笔。
```

Si te bloqueas al estructurar las ideas, utiliza un prompt de entrevista para que el Bot principal te haga preguntas y te ayude a aclarar tus necesidades:

::: details Selección de temas e inteligencia: Extracción, métricas y desglose de motivaciones
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

**Criterios de aceptación**
- Todos los enlaces originales son accesibles y los hechos principales están respaldados por el texto original.
- La falta de evidencia se clasifica como «pendiente de verificación»; **sin confirmación y firma humana, jamás pasa a la fase del redactor principal**.

[《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)；[《Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Redacción y textos: Eliminación del tono de IA y salida estructurada

Al redactar el primer borrador, cambia el enfoque de «qué tiene el producto» a «para qué le sirve al lector», **asegurando que el lector perciba un valor informativo claro en los primeros tres segundos**.

Puedes aplicar directamente dos estructuras ampliamente comprobadas:
- La fórmula HKRR de Tim (MediaStorm): abarca felicidad (Happiness), conocimiento (Knowledge), resonancia (Resonance) y ritmo (Rhythm). Cada publicación debe dominar sólidamente al menos un elemento; dos elementos es excelente; si no tiene ninguno, descártala.
- Los motivos de reenvío de Pan Luan: centrados en el «tiene que ver conmigo», situando al lector como protagonista. Por ejemplo, en lugar de «El software se ha actualizado», escribe «Ahorra dos horas al día buscando temas». Las estructuras virales se pueden reutilizar: copia el ritmo, no el contenido.

Configura en el redactor principal reglas de escritura y prohibiciones explícitas:

::: details Redacción y textos: Eliminación del tono de IA y salida estructurada
```text
你是我的内容主笔（Writer）。唯一职责是把已经批准的 brief 写成候选稿；不负责找热点、补事实、决定选题或发布。

【允许使用】
- /workspace/content-team/00-profile/voice.md 中的定位、范文、禁用句式与术语。
- /workspace/content-team/02-briefs/ 中已经批准的事实、链接、角度和限制。
- 输出到 /workspace/content-team/03-drafts/。

【禁止】
- 不得自行浏览外部网站、登录平台或调用连接器。
- 不得自行补充数字、引语、案例、比较级或因果。
- 不得伪装亲测、内幕或用户反馈。
- 不得发送、发布、购买、删除或修改权限。
- 不得执行本机命令，不得访问本机文件。

【写作规则】
前两句说清发生了什么，再写具体后果、使用场景、矛盾或尚未解决的问题。观点必须从 brief 中的事实长出来。段落以 2–4 句为主，句子长短交替，保留自然停顿。

【禁用表达】
“我的判断是”“真正有价值的是”“这说明”“这意味着”“毫无疑问”“重塑格局”“进入新时代”，以及空泛三段式、硬凑金句、广告腔和故作深刻的反问。

【固定交付】
按任务需要输出：A. 140–220 字中文短帖；B. 280–420 字展开版；C. 仅在适合时给 3–5 条串文大纲；D. 用户明确要求时写长文。每份稿末附“事实依据”和“仍需确认”。完成后写入 /workspace/content-team/03-drafts/YYYY-MM-DD-题目.md，并只汇报文件路径。
```
:::

Una vez terminado el borrador, el editor de hechos toma el control. **El editor de hechos solo verifica afirmaciones y elimina el tono robótico de IA**, sin añadir nuevos puntos de vista ni tener permisos de publicación:

::: details Redacción y textos: Eliminación del tono de IA y salida estructurada
```text
你是我的事实编辑（Editor），负责发布前的事实核验、结构检查和风格审校。你只做让内容可信、清楚、像真人表达所必需的修改；你没有发布权限。

【允许使用】
- /workspace/content-team/00-profile/voice.md、/02-briefs/ 与 /03-drafts/。
- brief 中列出的原始公开链接，仅用于复核关键事实。
- 输出到 /workspace/content-team/04-review/。

【审稿原则】
1. 没看过原始材料的人也能读懂。
2. 一手来源足以支撑关键事实。
3. 事实、观点和假设明确分开。
4. 删除模板腔、广告腔、绝对化和生硬缩略语。
5. 不让读者误以为作者亲测、掌握内幕或获得用户反馈。
6. 无法核对的句子必须删除、改成疑问或标记“待确认”。

【固定交付】
写入 /workspace/content-team/04-review/YYYY-MM-DD-题目.md，包含：可发布候选版本、改动说明、风险标记、仍需人工确认、原始来源清单。完成后只汇报文件路径和是否达到“可发布候选”标准。
```
:::

**Criterios de aceptación**
- Las dos primeras frases van directo al grano con los hechos clave, sin rodeos ni relleno.
- El editor de hechos coteja uno por uno los enlaces de primera mano; lo que no pueda verificarse se marca como «pendiente de confirmación» o se elimina directamente.
- El borrador corregido se traslada al directorio `04-review/` a la espera de la revisión humana final.

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Imágenes y presentación visual: Creación de sitios mediante código y ensamblaje de materiales

> Fuente: [Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación](https://x.com/0xlangeai/status/2109115005069341175)  
> Autor: [蓝哥AI @0xlangeai](https://x.com/0xlangeai)

![Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación](/cases-img/fs32-0.jpg)

![Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación](/cases-img/fs32-1.jpg)

Al ilustrar contenidos, evita pedirle a la IA ilustraciones conceptuales al azar, que suelen verse genéricas y artificiales. En la práctica se suele optar por dos vías sólidas:

**Vía 1: Convertir publicaciones en un sitio web de perfil personal (solución de 蓝哥AI)**
En el grupo «Sitio web de perfil de publicaciones», 4 Bots se turnan en relevos, almacenando los archivos intermedios en `/workspace/tweet-portrait/`:
1. El recopilador de publicaciones extrae publicaciones históricas y el analista de perfil sintetiza los hábitos de expresión y contrastes.
2. El diseñador web propone el diseño visual y el ingeniero web escribe el código frontend adaptándolo para dispositivos móviles.

Los dos primeros roles ejecutan sus prompts en orden:

```text
【推文整理员任务】
确认我自己已绑定的 X 账号身份，读取最近 90 天内最多 100 条本人内容，包括原创、带有本人评论的引用推文和本人回复，排除纯转发。
建立一个名为 tweet-portrait 的共用项目目录，将素材保存为 tweets.md。每条保留正文、日期、链接和内容类型，并注明实际读取范围、数量与缺失情况。
完成后返回账号名称、项目目录及素材文件的完整路径。无法访问时告诉我具体原因，不补造内容。
```

```text
【个人画像分析师任务】
读取共用项目目录中的 tweets.md，提炼最有辨识度的 3—5 个特点，覆盖关注主题、表达风格、语言习惯、典型观点或有趣反差。
每个特点附 1—2 条真实推文依据，保留摘录、日期和链接，区分观察与推测。不要写通用赞美或没有依据的人格结论。
保存为 profile.md，在群里汇报最有意思的特点和需要我确认的判断，完成后等我检查。
```

Los dos últimos roles ejecutan los prompts de diseño y código:

```text
【画像网站设计师任务】
读取共用目录中经过我检查的 profile.md，提出两个明显不同的个人画像网站设计方向。
分别说明首页如何呈现、包含哪些内容、排版和配色如何对应推文特点。保留原文依据，不生成没有统计基础的百分比或人格分数。
先把方向说明发给我，方便选择；需要用图说明时同时提供我可以查看的图片或文件。
选定后，把最终页面内容、结构、视觉和手机端安排保存为共用目录中的 design.md。
```

```text
【画像网站工程师任务】
读取共用项目目录中的 profile.md 和 design.md，按选定方案创建可以运行的个人画像网站，文件放在项目目录内。
保留推文依据和原文链接。打开页面检查桌面端与手机端，修复排版、内容和链接问题。
返回我能打开的预览及实际截图，先等待我检查，再进行发布。
```

Comprueba en la vista previa local el texto inicial, el espaciado de las tarjetas y la visualización móvil; tras confirmarlo, haz que el ingeniero empaquete el proyecto y **lo suba a Vercel o Cloudflare Pages para su publicación**.

**Vía 2: Ensamblaje parametrizado y clips de audio/video (solución de 铁柱 / herramientas oficiales)**
- Personajes y atuendos: utilizando un sistema de muñeca de papel basado en datos de juego, el Bot analiza los parámetros y llama a una API de terceros para el ensamblado.
- Clips de video: utilizando la plantilla oficial Clip Bot, introduce directamente el enlace largo de audio/video para generar automáticamente una transcripción con marcas de tiempo y recortar los segmentos destacados.

**Criterios de aceptación**
- La maquetación en la vista previa local es ordenada y la adaptación móvil responde correctamente.
- Todas las publicaciones citadas incluyen su enlace original y se pueden abrir.
- La página refleja fielmente las expresiones reales sin inventar trayectorias ni historiales.

[《Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)；[《Colección de tweets de 铁柱 ③: Métodos prácticos y casos》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

### Distribución, revisión y moderación: Control humano y flujo asíncrono

Los principiantes a menudo buscan una automatización total sin intervención humana, lo que conduce fácilmente a la suspensión de cuentas. **Está terminantemente prohibido publicar mediante navegadores dentro de la máquina virtual en la nube**, ya que los sistemas de control de riesgo de las plataformas identifican las huellas digitales de las máquinas virtuales. La publicación debe contar con un control humano absoluto, realizándose de forma manual por el propio creador desde un dispositivo físico local.

La colaboración en equipo utiliza un enfoque asíncrono, evitando tener que estar pegado a la pantalla todo el día:
- Banco de temas semanal: dedica 30 minutos a la semana a seleccionar fichas candidatas en una hoja de cálculo y márcalas como aprobadas.
- Revisión diaria de borradores: el creador dedica 10 minutos al día a revisar los textos en `04-review/` y añadir una reflexión personal.
- Flujo en tablero kanban: gestiona en la tabla los estados de pendiente de revisión, en redacción, finalizado y publicado.

Tras publicar el contenido, asigna al analista de métricas una revisión semanal en modo de solo lectura, prohibiendo estrictamente publicaciones o interacciones en tu nombre:

::: details Distribución, revisión y moderación: Control humano y flujo asíncrono
```text
你是我的 X 数据复盘师（Analyst）。唯一职责是分析用户自己的 X 内容质量、帖子表现和可执行的改进方向；只读，不代表用户进行任何互动或账号操作。

【允许使用】
- 用户在任务中明确指定的个人 X 主页，以及该账号公开可见的帖子。
- 用户主动提供或授权查看的 X Analytics 页面、CSV 导出和截图。
- /workspace/content-team/03-drafts/、/04-review/、/05-published/ 与 /06-analysis/。
- 如页面要求登录、密码、验证码、2FA 或 passkey，立即停下并请用户接管；不得索取或记录凭据。

【绝对禁止】
- 不得发帖、改帖、删帖、点赞、转发、收藏、关注、取关、评论或私信。
- 不得修改头像、简介、账号设置、隐私设置或权限。
- 不得读取、复制或分析私信与非本任务所需的个人数据。
- 不得把浏览量相关性写成因果，不得补全缺失指标。
- 不得执行本机命令，不得访问本机文件。

【固定交付】
每周写入 /workspace/content-team/06-analysis/weekly-review-YYYY-WW.md，包含数据来源、时间范围、样本量、表现最好与最差的帖子、内容质量诊断、3 条改进建议、2 个下周实验、数据缺口。需要在 /workspace/content-team/05-published/ 留存所用 CSV 或截图的文件名，不复制账号凭据。
```
:::

Para revisiones puntuales de periodos específicos, envía una instrucción directa:

```text
只读分析我明确指定的个人 X 主页【主页地址】，时间范围为【开始日期—结束日期】。数据来源为【公开主页 / X Analytics / CSV / 截图】。

先列出数据范围和缺失字段，再按主题、内容形式、长度、发布时间和开头类型做对比。给 3 条有具体帖子或指标支撑的改进建议，并设计 2 个一次只改变一个变量的下周实验。

禁止发帖、改帖、删帖、点赞、转发、收藏、关注、取关、评论、私信和修改账号设置。遇到登录、验证码、2FA、passkey 或扩大权限时立即停下，等我接管。完成后写入 06-analysis，并只回复文件路径、覆盖帖子数和缺失数据。
```

**Criterios de aceptación**
- Publicación manual local por parte de una persona real, con riesgo cero de suspensión por controles de seguridad.
- Las métricas de análisis pueden rastrearse hasta los archivos de exportación originales.
- **No sacar conclusiones precipitadas si el tamaño de la muestra es menor a 10 publicaciones**.
- La planificación para la semana siguiente incluye 2 experimentos controlados de variable única (por ejemplo, comparar el impacto de diferentes longitudes de texto en la tasa de interacción).

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)；[《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

## Desglose en profundidad de casos prácticos representativos

![Desglose en profundidad de casos prácticos representativos](/info/12-content-s3.png)

### Caso 1: El equipo cerrado de 5 personas para medios de Adrian Punk

Adrian Punk (@AdrianPunk115) configuró en la versión de escritorio un equipo permanente de 5 roles, completando un ciclo cerrado que abarca desde la captura de fuentes primarias, selección de temas, redacción y corrección hasta el análisis posterior.

1. **Restricción preventiva de permisos**: en la configuración del cliente, ajusta «Ejecutar en esta computadora» a «Nunca permitir»; el prompt prohíbe explícitamente publicar por cuenta propia, introducir contraseñas y llamar a conectores.
2. **Configuración de rutas de archivos**: crea `/workspace/content-team/` y sus 7 subdirectorios en la computadora en la nube, y añade en `00-profile/voice.md` el estilo de la cuenta, trabajos representativos y palabras prohibidas.
3. **División especializada del trabajo**: crea los roles de explorador de inteligencia, planificador de temas, redactor principal, editor de hechos y analista de métricas, limitando estrictamente los directorios de entrada y salida de cada puesto.
4. **Transferencia reglamentada**: envía la instrucción de inicio en el grupo «Equipo de contenido digital»; los entregables de las etapas previas se escriben en Markdown para que las etapas posteriores los lean; **queda prohibido avanzar de fase sin aprobación humana**.

Nota: Los 5 Bots comparten la computadora en la nube sin aislamiento sandbox, por lo que los permisos deben apoyarse en límites de roles bien definidos; **el editor de hechos debe cotejar de forma independiente los enlaces originales**, filtrando cifras inventadas por el redactor y el tono de relaciones públicas.

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Caso 2: El banco de contenido viral dual de Kin (tweets y videos)

> Fuente: [¿Cómo pueden los ingenieros aprovechar Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![¿Cómo pueden los ingenieros aprovechar Grok Bot?](/cases-img/fs25-0.jpg)

![¿Cómo pueden los ingenieros aprovechar Grok Bot?](/cases-img/fs25-1.jpg)

Kin (@KinGao476942, embajador de SpaceXAI para China) consiguió más de 2000 seguidores en Twitter en unos 10 días y ha gestionado canales de video con más de un millón de seguidores, creando un Bot de operaciones en Twitter y el banco de temas virales para «小邓Talk».

1. **Ficha de identidad**: define con claridad el enfoque, las cuentas de referencia y las áreas prohibidas, inhabilitando la publicación automática de tweets. **Si no se encuentran datos, debe indicarse «no encontrado», prohibiéndose terminantemente estimar o inventar**.
2. **Retroalimentación con datos reales**: analizó más de 100 publicaciones históricas y comprobó que los textos de entre 200 y 500 caracteres tenían una mediana de lectura superior, y aquellos con pasos numerados recibían muchos más «me gusta».
3. **Banco de temas de seis campos**: diseñó una tabla con enlace permanente original, hora de captura, métricas reales, niveles de seguidores, segmento de comunidad y análisis de motivaciones, sincronizándola con un tablero de Notion para el filtrado.
4. **Desglose de estructuras**: descompone publicaciones virales según HKRR (felicidad, conocimiento, resonancia, ritmo) y las tres motivaciones de Pan Luan, replicando la estructura pero no el contenido.

Nota: Durante la fase inicial de crecimiento de la cuenta, la alta frecuencia de publicación es más efectiva que un perfeccionamiento excesivo; al terminar, revisa siempre que el sujeto apele directamente a los intereses del lector.

[《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### Caso 3: El sitio web de perfil de publicaciones de 蓝哥AI

蓝哥AI (@0xlangeai) extrajo publicaciones históricas de su cuenta vinculada de X, sintetizó su estilo personal y contrastes, y puso en línea de forma automatizada un sitio web de exhibición de perfil personal.

1. **Configurar Bots especializados**: en el grupo del proyecto «Sitio web de perfil de publicaciones», configuró 4 roles: recopilador de publicaciones, analista de perfil personal, diseñador web de perfil e ingeniero web de perfil.
2. **Extracción y análisis**: el recopilador leyó hasta 100 publicaciones originales, citas comentadas y respuestas de los últimos 90 días, guardándolas en `tweets.md`; el analista extrajo de 3 a 5 contrastes expresivos con sus referencias, las cuales fueron revisadas por el creador.
3. **Diseño y despliegue**: el diseñador generó `design.md` (adoptando un formato de tarjetas estilo portafolio), y **el ingeniero redactó el código en la computadora en la nube, realizó pruebas en móvil y escritorio, y colaboró en el despliegue en Vercel o Cloudflare Pages**.

Nota: El historial de publicaciones es un corpus de datos ya disponible; **cada paso (recopilación, análisis, diseño e ingeniería) requiere la confirmación del creador antes de pasar a la siguiente etapa**, evitando que los desvíos se magnifiquen.

[《Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### Caso 4: Captura ininterrumpida 24/7 y flujo automatizado con tablas multidimensionales de xilo

> Fuente: [Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]](https://x.com/xilo2991/status/2109613437215293905)  
> Autor: [xilo @xilo2991](https://x.com/xilo2991)

![Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]](/cases-img/fs36-0.jpg)

![Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]](/cases-img/fs36-1.jpg)

xilo (@xilo2991) aprovechó el funcionamiento continuo 24 horas de la computadora en la nube para crear un pipeline de recolección de contenido viral activo en todo momento, sincronizándolo en tiempo real con hojas de cálculo multidimensionales de Feishu.

1. **Definir los tres elementos clave**: precisar los canales, las cuentas de referencia y palabras clave, y la hoja de cálculo de destino para los resultados.
2. **Integrar la tabla**: enviar el repositorio de GitHub del plugin de Feishu al Bot, completar la configuración y autenticación en la computadora en la nube, y utilizar la tabla como bus de colaboración.
3. **Mitigar riesgos y descartar variables**: controlar la frecuencia de búsqueda simulando una navegación normal; registrar el recuento de búsquedas y la probabilidad de viralidad, y **descartar automáticamente las palabras clave ineficaces en la revisión semanal**.
4. **Aclarar mediante entrevista**: enviar un prompt de entrevista con preguntas progresivas al Bot principal para pulir los detalles operativos antes de generar la configuración automáticamente.

Nota: Cambiar la publicación totalmente automática a una semiautomática con aprobación humana para equilibrar la eficiencia con la seguridad.

[《Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Caso 5: Especialización de roles, coordinación multidispositivo y prevención de baneos en la base por 铁柱AGI

> Fuente: [Webhook de Grok Bot + Atajos: Creación de un pipeline automatizado de ingesta de conocimiento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Webhook de Grok Bot + Atajos: Creación de un pipeline automatizado de ingesta de conocimiento](/cases-img/fs06-0.jpg)

![Webhook de Grok Bot + Atajos: Creación de un pipeline automatizado de ingesta de conocimiento](/cases-img/fs06-1.jpg)

铁柱AGI (@cgnot996) probó sistemáticamente los límites de los Bots, consolidando soluciones contra bloqueos y para recuperación ante desastres.

1. **Especialización de puesto único**: dividir en Bots con una sola función como inspección de código, captura de artículos y archivo contable, descartando el concepto de un Bot todoterreno.
2. **Ingesta ultra rápida**: configurar Atajos en el móvil para leer el portapapeles y enviarlo directamente mediante Webhook al Bot en la computadora en la nube para consolidarlo en una tabla.
3. **Línea roja contra suspensiones**: **la simulación de publicaciones con navegadores en máquinas virtuales provoca fácilmente el bloqueo de la cuenta; toda interacción externa debe ser realizada por una persona real en un dispositivo físico**.
4. **Recuperación ante desastres**: reconstruir la computadora en la nube borra los entornos no persistentes; redacta scripts de recuperación automática en Shell y utiliza un Bot administrador de memoria para respaldar periódicamente prompts y configuraciones.

Nota: **Las configuraciones y comandos de instalación clave deben estructurarse en scripts de recuperación reproducibles con un solo clic**; la computadora en la nube no debe considerarse un servidor infaliblemente estable.

[《Colección de tweets de 铁柱 ③: Métodos prácticos y casos》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

## Errores comunes que debes evitar

1. Publicar desde la computadora en la nube expone huellas digitales que provocan bloqueos, y la automatización total suele publicar contenido errático. **Publicar, dar «me gusta» y enviar mensajes directos debe hacerse manualmente en un dispositivo real**.
2. En la descripción de roles, **establece reglas estrictas: marcar «no encontrado» si no hay datos y etiquetar como «inferencia» toda deducción**, evitando la ingesta de datos falsos.
3. El reinicio de la computadora en la nube borra las dependencias. **Guarda scripts de recuperación en Shell dentro de directorios persistentes** como respaldo.
4. En las tareas Routine, **verifica minuciosamente el ciclo de ejecución** para evitar configurar por error «ejecutar solo en días laborables», lo que provocaría desconexiones los fines de semana.
5. No filtrar tomas previamente causó una reducción de cuota de más del 40% en una sola semana; **queda terminantemente prohibido el sondeo frecuente e innecesario, optimiza los momentos de activación**.

Planes a partir del 12 de octubre de 2026:
| Plan | Costo | Cuota | Incluye Bot |
| - | - | - | - |
| Plus | $8/mes | - | No |
| Premium | $30/mes o $300/año | 4x | Sí |
| Super | $100/mes o $1000/año | 15x | Sí |
| Ultra | $200/mes o $2000/año | 50x | Sí |

## Cómo verificar el resultado

### Permisos y directorios
1. Ve a Configuración de la cuenta en «General → Agent → Ejecutar en esta computadora»; **el estado debe ser obligatoriamente «Nunca permitir»**. Se prohíbe terminantemente a los Bots publicar o realizar pagos automáticamente, así como falsear datos.
2. Verifica los 7 subdirectorios bajo `/workspace/content-team/` y asegúrate de haber completado en `00-profile/voice.md` el posicionamiento de la cuenta, los ejemplos y las palabras prohibidas.

### Recopilación, redacción y simulacro
1. Extrae 3 pistas y **comprueba aleatoriamente que 2 de los enlaces sean accesibles y cuenten con respaldo en el texto original**; si faltan datos, marca «datos públicos no encontrados», sin conjeturar cifras ni números de seguidores.
2. Tras confirmar el Brief, genera el borrador inicial: las dos primeras oraciones deben presentar directamente los hechos clave, los párrafos deben mantenerse entre 2 y 4 oraciones, adjuntar al final la base fáctica y los puntos pendientes de confirmación, y evitar por completo las palabras prohibidas.
3. El texto revisado solo verifica sin añadir nuevos argumentos; **jamás se envía al exterior automáticamente sin una instrucción humana**. Ejecuta `restore.sh` una vez en el entorno de prueba para comprobar que las dependencias estén listas con normalidad.

## Lecturas complementarias

### Documentación oficial
- [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans.md)
- [Equipos de Bots y colaboración](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Entorno y configuración de computadoras en la nube](https://cursor.com/cn/docs/grok-bot/computers.md)
- [Colaboración en chats grupales](https://cursor.com/cn/help/grok-bot/group-chats.md)
- [Tareas rutinarias y automatización](https://cursor.com/cn/help/grok-bot/routines.md)

### Fuentes prácticas de la comunidad
- [《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)
- [《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)
- [《Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)
- [《Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- [《Colección de tweets de 铁柱 ③: Métodos prácticos y casos》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)
