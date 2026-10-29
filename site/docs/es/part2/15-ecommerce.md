# Capítulo 15 Casos prácticos: Comercio electrónico y vida cotidiana

Abrir diálogos en pestañas web individuales facilita la pérdida de registros y obliga a alternar constantemente entre varios programas para mover información. **Este capítulo te guiará para poner en marcha los flujos de trabajo con soluciones listas para usar**.

- Vida cotidiana y contenidos: Usa prompts probados para generar textos de Xianyu, maquetación de Xiaohongshu y tarjetas gráficas SVG, sin tener que alinear nada a mano.
- Comercio electrónico transfronterizo: Empieza con inspecciones en una sola máquina y construye un equipo de **«1 capitán + 12 puestos»**, usando listas de pendientes de aprobación para la supervisión humana.

## Caso 1: Gestor de publicaciones de Xianyu (panel de datos de artículos de segunda mano y borradores de consultas)

Miles Ma (@miles_mazy, inspirado en @0xlangeai) creó este Bot. Vender artículos de segunda mano pasándoselos directamente a una IA **suele provocar que invente configuraciones como si fueran nuevas**. Este bot separa las condiciones reales de las especificaciones oficiales, generando un panel de datos en dos columnas y borradores de respuestas.

### Pasos y verificación

1. Toma buenas fotos del frente, primeros planos de imperfecciones y la placa de identificación, y define con claridad los accesorios, métodos de recogida local y precio de venta.
2. En la barra lateral de Grok Bot, haz clic en `+`, selecciona «Crear Bot» y nómbralo «Gestor de publicaciones de Xianyu».
3. Sube las fotos reales y envía el prompt, tomando como ejemplo un teclado Logitech K380s de segunda mano a 89 yuanes.

```text
帮我做一份闲鱼上架资料。商品是罗技 K380s，黑色，用了 8 个月，空格键有轻微磨痕，逐键输入正常，没拆过机；附两节在用电池，无包装，卖 89 元，支持自提，邮费待确认。查官方型号资料，整理标题、商品描述、需要补拍的照片和常见咨询回复，做成可打开的资料板，并附可复制的上架正文。没提供的信息标为待确认。
```

4. El Bot busca en la web los parámetros oficiales y genera un panel de datos en HTML junto con borradores en texto plano.

> Fuente: [Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones](https://x.com/miles_mazy/status/2098708209095819605)  
> Autor: [Miles Ma @miles_mazy](https://x.com/miles_mazy)

![Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones](/cases-img/fs27-0.jpg)

![Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones](/cases-img/fs27-1.jpg)

- La columna izquierda muestra la condición real del vendedor, mientras que la derecha muestra el precio, el estado de conservación y los accesorios.
- **Los parámetros y el desgaste se enumeran por separado; cualquier dato no proporcionado se marca como «pendiente de confirmación», prohibiendo inventar información.**
- La lista de fotos adicionales detalla los ángulos faltantes, y las respuestas de atención al cliente cubren conexión, cambio de dispositivos y recogida local.
- Caso de referencia: [«Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones | Miles Ma»](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf).

## Caso 2: Editor de Xiaohongshu (de la selección de temas a seis tarjetas de conocimiento y galería)

![Caso 2: Editor de Xiaohongshu (de la selección de temas a seis tarjetas de conocimiento y galería)](/info/15-ecommerce-s2.png)

### Pasos de creación

1. En la barra lateral de Grok Bot, crea un nuevo Bot y nómbralo «Editor de Xiaohongshu».
2. Define el tema y los puntos clave de conocimiento, fija el número de tarjetas en 6, y establece el tamaño de 1080×1440 junto con la paleta de colores principal y secundaria.
3. Entra a la interfaz de conversación y envía el prompt:

```text
给电脑新手做一套小红书图文，主题是“Windows 截图后，图片去哪了”。查微软官方资料，做 6 张 1080×1440 的图：封面、框选截图、整屏保存、当前窗口、剪贴板历史、快捷键对照表。用米白、深蓝和亮黄，文字清楚，配操作示意。直接交 PNG 成图、SVG 源文件和配套发布正文，再做一个能看全套图片的画廊。
```

4. **El Bot consultará la documentación oficial para verificar los atajos de teclado**, generará los archivos SVG, renderizará las imágenes PNG y las integrará en una galería HTML.

### Verificación y errores comunes

| Tarjeta | Contenido y maquetación |
| :--- | :--- |
| Tarjeta 1 | Portada, texto grande centrado que señala el problema recurrente de las capturas |
| Tarjetas 2-5 | Tarjetas de pasos, diagramas que ilustran métodos como captura de área seleccionada, pantalla completa, etc. |
| Tarjeta 6 | Tarjeta de resumen, tabla con los 4 métodos de captura y la ubicación de destino |

- Todo el conjunto de tarjetas utiliza fondo blanco crema con texto azul marino y detalles en amarillo brillante. **Es obligatorio entregar 6 imágenes PNG de 1080×1440, código fuente SVG, texto con etiquetas para publicación y una galería en línea**.
- El guardado automático de capturas en disco depende de la configuración de fotos del sistema; **para consultar el historial con `Win + V`, el interruptor debe estar activado previamente** y los registros no deben haberse sobrescrito.
- Para corregir erratas, modifica directamente el archivo SVG en un editor de texto, **sin necesidad de volver a generar las imágenes**.

Caso de referencia: [«Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones | Miles Ma»](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

## Caso 3: Informador de herramientas (boletín de análisis de software filtrable por uso)

El Bot «Informador de herramientas», creado por Miles Ma, extrae repositorios de código abierto y documentación para generar un boletín de tarjetas web que permite el filtrado por categorías.

### Limitaciones de las herramientas y tareas recomendadas

| Herramienta | Requisitos y dependencias | Principales limitaciones | Tareas recomendadas |
| :--- | :--- | :--- | :--- |
| **PowerToys** | Se ejecuta directamente con el instalador de Windows | Exclusivo de Windows; algunas funciones experimentales pueden ser inestables ocasionalmente | Extraer texto mediante atajos de teclado o fijar ventanas en primer plano |
| **MarkItDown** | Depende de Python o de la línea de comandos | Tasa de reconocimiento limitada en diseños complejos con texto e imágenes | Conversión por lotes de Word y PDF a Markdown |
| **changedetection.io** | Requiere Docker o entorno de servidor | Requiere conocimientos de operaciones (DevOps); sujeto a restricciones antibot | Monitorear cambios en etiquetas de precios de comercio electrónico |

### Pasos de operación

1. En la barra lateral de Grok Bot, crea un nuevo Bot y nómbralo «Informador de herramientas».
2. Define la audiencia objetivo y la lista de herramientas a investigar.
3. Entra a la interfaz de conversación y envía el prompt.

```text
帮内容工作室整理 PowerToys、MarkItDown 和 changedetection.io，查官方仓库和文档。每个工具写清能帮忙做什么、上手需要什么、主要限制，再给一个具体使用例子。做成能按用途筛选的网页简报，附来源链接。
```

4. El Bot extraerá las descripciones y dependencias de los repositorios, **programará un informe HTML con scripts de filtrado** y lo guardará en el espacio de trabajo.

### Criterios de aceptación y errores comunes

- Cada tarjeta **debe incluir 6 elementos clave**: posicionamiento de la herramienta, dependencias iniciales, limitaciones principales, casos de uso prácticos y enlaces a sitios oficiales.
- La parte superior de la página web debe incluir botones de categoría para filtrar las tarjetas de manera fluida.
- La descripción de las limitaciones debe ser objetiva; aclara explícitamente que changedetection.io requiere Docker o un servidor, sin exagerar diciendo que no tiene barrera de entrada.
- Se trata de un filtrado preliminar; **el Bot no ejecuta pruebas prácticas completas**, sirviendo principalmente para descartar con rapidez el software candidato que no cumpla con los requisitos.

[«Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones | Miles Ma»](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

## Caso 4: Tutor de video (herramienta pedagógica interactiva y video corto con subtítulos)

Este es el método de Miles Ma (@miles_mazy, inspirado en @0xlangeai). Explicar por texto los giros en sentido horario/antihorario y el retorno al estado original tras cuatro giros de un cubo de Rubik es difícil, y grabarlo a mano consume mucho tiempo. **Grok Bot puede programar páginas interactivas en la nube, grabar la pantalla de forma automática e incrustar los subtítulos**.

### Cómo hacerlo

1. En la barra lateral, crea un nuevo Bot y nómbralo «Tutor de video».
2. **Explica solo un movimiento básico a la vez**, evitando los algoritmos de resolución completos.
3. Envía el prompt:

```text
给孩子做一个魔方入门小工具，能认识六个面、点按钮演示右面顺转和逆转，再展示右面连续转四次回到原位。把实际操作录成一分钟左右的教学视频，加中文配音和字幕，交付视频和工具文件。
```

4. El Bot programa la página automáticamente, simula los clics, graba la pantalla y genera el video con subtítulos en chino.

### Qué se considera un buen resultado

| Entregable | Criterios de aceptación |
| :--- | :--- |
| **Página web interactiva** | Conservar el código fuente HTML/JS; al hacer clic en R cambian los colores, en R' se revierten, y el botón de reinicio vuelve a la posición original tras cuatro giros; debe poder abrirse sin conexión |
| **Video final** | Archivo MP4 de unos 51 segundos con subtítulos SRT, con las acciones visuales sincronizadas con los subtítulos |

Este mismo enfoque puede aplicarse a demostraciones de paneles de control o tutoriales de funciones puntuales.

Caso de referencia: [«Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones | Miles Ma»](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf).

## Caso 5: Organizador de colecciones (convertir marcadores de redes sociales en un banco de temas)

![Caso 5: Organizador de colecciones (convertir marcadores de redes sociales en un banco de temas)](/info/15-ecommerce-s5.png)

Miles Ma (@miles_mazy) creó este Bot para transformar marcadores y favoritos en una biblioteca de temas.

### Pasos de operación

1. En la barra lateral, crea un nuevo Bot y nómbralo «Organizador de colecciones».
2. Elige 5 tipos de enlaces representativos (como el episodio 115 de un pódcast, conversiones de texto a imagen).
3. Envía el prompt:

```text
整理这几条 X 收藏链接，按主题分类，每条留下作者、原链接、核心观点和可以借鉴的写法。再围绕“给新手的 AI 实操教程”提出三个具体选题，做成 Markdown 素材库和选题清单。
```

4. El Bot procesa la información y genera **dos archivos Markdown**: «Banco de materiales de marcadores» y «Sugerencias de temas».

### Verificación y limitaciones

- Verificación: **Conservar los autores y enlaces originales**, desglosar la lógica de redacción y acotar los 3 temas para que puedan ejecutarse directamente como tareas únicas.
- Limitaciones: **Está estrictamente prohibido falsificar las prácticas y métricas de otros como experiencias propias**; apréndete únicamente la estructura y las ideas.

[«Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones | Miles Ma»](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

## Caso 6: Estructuración de un equipo para Amazon (de la inspección en la tienda a la colaboración multipuesto «1+12»)

![Caso 6: Estructuración de un equipo para Amazon (de la inspección en la tienda a la colaboración multipuesto «1+12»)](/info/15-ecommerce-s6.png)

### Contexto y definición de roles

- **Quién**: Zach (@1999Zach22).
- **Qué hizo**: Migró por completo las Skills que antes ejecutaba localmente en Claude/Codex a Grok Bot, estructurando en un ordenador en la nube compartido un equipo de operaciones de IA para comercio electrónico transfronterizo en Amazon compuesto por «1 capitán de comercio exterior + 12 puestos de operaciones».

### En qué consiste

Herramientas locales como Codex CLI requieren mantener la máquina siempre encendida y no se pueden consultar fuera de casa. **Grok Bot incluye un ordenador en la nube ubicado en EE. UU. disponible 24/7**, sincronizado entre móvil y ordenador, permitiendo además navegar y realizar preguntas en la tienda de Amazon con cuentas de comprador reales.

Zach adopta una arquitectura de **«1 capitán + 12 puestos de operaciones»**. El usuario solo se comunica con el capitán de comercio exterior, quien coordina y asigna tareas a los demás puestos.

**Todos los puestos tienen estrictamente prohibido realizar modificaciones directas en el panel de control de la tienda**; solo generan listas de pendientes de aprobación para la confirmación humana.

| Puesto | De qué se encarga | Límites estrictos |
| :--- | :--- | :--- |
| Capitán de comercio exterior | Coordina y gestiona a sus subordinados; presenta informes semanales y listas de pendientes | No toma decisiones comerciales directamente sin supervisión humana |
| Asistente / Explorador / VOC | Inspecciona secuestros de listings (piggybacking), investiga productos y analiza reseñas negativas | No inicia sesión en el panel del vendedor ni lanza proyectos por iniciativa propia |
| Finanzas / Gestor de publicidad | Calcula la rentabilidad de productos y emite sugerencias de publicidad | Bajo ninguna circunstancia entra al panel para modificar pujas o añadir palabras clave negativas |
| Redacción / Diseño / Supervisor de control de calidad | Genera textos, creatividades gráficas y realiza revisiones finales de conformidad | No publica contenido directamente ni toma decisiones finales en lugar del usuario |
| Bot de retrospectiva | Consolida los resultados semanales y actualiza la base de conocimientos | No maquilla problemas operativos ni inventa métricas de rendimiento |

### Cómo implementarlo

#### 1. Planes de suscripción y preparación del entorno
- **Para empezar, elige el plan Premium de 30 USD/mes** (el plan Plus de 8 USD no incluye Bot en absoluto); actualiza según tus necesidades al plan Super de 100 USD o al plan Ultra de 200 USD.
- Inicia sesión con la misma cuenta en el ordenador y en el móvil, y **confirma que el ordenador en la nube funcione con normalidad**. Consulta los detalles en [Guía de planes y límites de uso de Grok Bot](https://cursor.com/cn/help/grok-bot/plans).

#### 2. Poner en marcha tres tareas primero con un solo Bot
Utiliza la IP estadounidense y el navegador del ordenador en la nube para validar tres tareas:
1. **Inspección diaria de los listings propios**: Comprueba la imagen principal, el precio, las variantes y si hay secuestros de listing (piggybacking); si hay anomalías, reporta pruebas comparativas.
2. **Probar las consultas de compras de Alexa**: Inicia sesión con una cuenta de comprador y haz preguntas; en pruebas reales se completan 8 tipos de escenarios y se consulta el historial de precios de 30 días en unos 8 minutos.
3. **Monitorización programada de competidores**: Registra precios y cupones; **notifica solo si hay cambios**, sin enviar alertas si todo sigue igual.

```text
每天固定时间去前台检查自家 Listing：主图和价格是否正确，变体是否正常挂载，核心关键词是否能搜索到，是否存在跟卖。只记录指定商品和关键词，有异常才发提醒，并附带与前一日的对比数据和页面截图证据。不登录店铺后台，不执行任何写操作。
```

```text
从消费者的角度，尽可能多地把 Alexa for Shopping 体验一遍，最后给我一份报告。
```

#### 3. Desglosar funciones y límites de cada puesto
- Una vez validado el proceso, divide las tareas entre los 12 puestos de operaciones.
- Puestos sensibles como publicidad y lanzamiento de nuevos productos **tienen explícitamente prohibido escribir en el panel de control**; siempre deben entregar una «lista de pendientes de aprobación» y tener claramente delimitadas sus facultades de consulta.

```text
你是合理烧钱的广告投手。负责分析广告效率、搜索词转化率、出价与预算建议。
边界约束：
1. 绝对不登录广告后台，不直接修改出价，不调整预算，不添加否定关键词，不新建广告活动；
2. 所有优化建议必须生成「待批清单」，每条建议必须附带调整依据和预期影响；
3. 待批清单单线交付给出海船长，由船长提报给业务负责人审核，严禁自主执行。
```

#### 4. Diseñar la cadena de traspaso «1+N»
- **Nunca crees chats grupales con múltiples Bots**, ya que recibirán el contexto de forma redundante y consumirán tokens a gran velocidad.
- **Adopta una arquitectura 1+N**: el usuario solo interactúa con el «capitán de comercio exterior», quien delega el trabajo y recopila los resultados.

```text
你是出海船长，负责统筹 12 个业务岗位。日常接收业务负责人的目标，拆解为具体子任务派发给对应岗位。所有下属岗位向你单线汇报，由你汇总结果、审核质量；不达标的打回重做，需要人工决策的整理为带选项和依据的待批清单汇报给人。严格遵守交接链规则：
1. 巡检链：助理上报异常与证据，派给数据或广告岗位做归因分析；
2. 选品链：海盗提交机会报告，财务测算单品利润，由你整理为立项建议书提报给人；
3. 上新链：文案出草稿，设计出图，守门员审核，你做终检后交给人确认，由人工在后台发布；
4. 复盘链：收齐各岗位经验，复盘机器人写周报并更新经验库，据此编排下周计划。
所有岗位严禁直接登录店铺后台或执行未授权的修改操作。
```

#### 5. Compartición de recursos y control local
- Todos los Bots **comparten el mismo ordenador en la nube y el mismo disco**; los scripts copiados en el espacio de trabajo quedan disponibles para todos los integrantes.
- Para leer archivos locales, es necesario ir a la pestaña «Ordenador» en la configuración, **activar «Ejecutar en este ordenador»** (Execution on Local Computer) y especificar el directorio de copia.

  Para más detalles, consulta la [Documentación de Grok Bot sobre ordenadores y aplicaciones](https://cursor.com/cn/docs/grok-bot/work) y las [Instrucciones de configuración de Grok Bot](https://cursor.com/cn/docs/grok-bot/settings).

### Qué se considera un buen resultado

> Fuente: [Experiencia práctica de comercio electrónico transfronterizo con Grok Bot: construyendo un equipo completo de Amazon desde cero](https://x.com/1999Zach22/status/2110078772225667115)  
> Autor: [Zach @1999Zach22](https://x.com/1999Zach22)

![Experiencia práctica de comercio electrónico transfronterizo con Grok Bot: construyendo un equipo completo de Amazon desde cero](/cases-img/fs38-0.jpg)

![Experiencia práctica de comercio electrónico transfronterizo con Grok Bot: construyendo un equipo completo de Amazon desde cero](/cases-img/fs38-1.jpg)

- **Comunicación directa únicamente con el capitán**, sin tener que alternar entre 12 bots.
- El ajuste de precios y la reposición de stock se gestionan mediante listas de pendientes de aprobación, **evitando cualquier exceso de atribuciones**.
- Notificaciones de anomalías en el móvil mientras las inspecciones siguen corriendo con el portátil cerrado.

Caso de referencia: [«Experiencia práctica de comercio electrónico transfronterizo con Grok Bot: construyendo un equipo completo de Amazon desde cero»](https://jcng5q8n0f3z.feishu.cn/wiki/LG1twK03uiO00JkPk1ncQQNUnvt).

### Qué podemos aprender

- Usar primero un único Bot para **afinar el SOP** antes de dividir las tareas.
- Adoptar la **distribución maestro-esclavo «1+N»** para evitar que los chats grupales agoten los tokens.
- **Generar exclusivamente listas de pendientes de aprobación**, requiriendo confirmación manual en el panel de control.

## Errores comunes que debes evitar

- **Nunca otorgues permisos de modificación en el panel del vendedor**: Para acciones sensibles, haz que el Bot genere una «lista de pendientes de aprobación» para su ejecución manual, evitando errores en el etiquetado de precios o el cierre de la tienda.
- **Prevenir en Xianyu la invención del estado del artículo**: Exige «ceñirse a lo proporcionado por el vendedor y marcar lo no proporcionado como pendiente de confirmación», evitando que se cuelen especificaciones oficiales de artículos nuevos que provoquen devoluciones.
- **No metas 12 Bots en un solo grupo**: Agotará la cuota semanal en pocas rondas de diálogo. Cambia a una arquitectura maestro-esclavo «1+N» utilizando archivos guardados en disco como intermediarios.
- **El rastreo de competidores debe ser preferiblemente de 1 vez al día**: Hacer sondeos cada pocos minutos bloquea la IP fácilmente y agota la cuota; para alta frecuencia utiliza las API oficiales o MCP.
- **Asegúrate de elegir el plan Premium de 30 USD/mes**: El plan Plus de 8 USD/mes no tiene acceso a Bots; presta atención a The X Subscription a partir del 12-10-2026.
- **El control local debe tener rutas restringidas**: No actives «permitir siempre»; especifica las rutas de archivos antes de ceder el control y mantén la confirmación por ventana emergente para evitar tocar archivos personales por error.

## Cómo verificar el trabajo una vez terminado

**Tras la entrega, verifica punto por punto contra los criterios de aceptación**; no bajes la guardia.

- **Panel de datos de Xianyu**: Los defectos y las especificaciones oficiales deben figurar por separado, y los datos desconocidos deben marcarse como «pendiente de confirmación»; está estrictamente prohibido inventar direcciones de recogida local o falsear el estado de la batería.
- **Gráficos y textos de Xiaohongshu**: Entrega 6 tarjetas gráficas de 1080×1440 junto con el código fuente SVG, destacando en los pasos los atajos de teclado y los requisitos previos del sistema; no alteres la paleta de colores.
- **Boletín de herramientas**: El HTML de una sola página debe incluir filtrado y enlaces oficiales, detallando con veracidad las limitaciones del entorno Docker; queda prohibido presentar el despliegue como si no tuviera barrera de entrada.
- **Video tutorial**: El video terminado debe durar aproximadamente 1 minuto con audio y video sincronizados, acompañado obligatoriamente del código fuente de la herramienta web; los subtítulos y la imagen no deben desfasarse.
- **Banco de materiales**: Conserva el autor original y el enlace a la publicación original, acotando los temas a prácticas individuales concretas; no hagas resúmenes vagos ni te apropies de casos ajenos como si fueran propios.
- **Colaboración en comercio electrónico**: En la arquitectura 1+N, interactúa únicamente con el capitán; los cambios de precios y las publicaciones deben generar obligatoriamente una lista de pendientes de aprobación; está terminantemente prohibido modificar precios por cuenta propia o entrar en bucles infinitos que agoten el consumo de la cuota.

## Lecturas complementarias

- [«Casos prácticos de la guía de aplicación de Grok Bot: Publicación en Xianyu, creación de imágenes para Xiaohongshu, búsqueda de herramientas, vídeos cortos y organización de colecciones | Miles Ma»](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)
- [«Experiencia práctica de comercio electrónico transfronterizo con Grok Bot: construyendo un equipo completo de Amazon desde cero»](https://jcng5q8n0f3z.feishu.cn/wiki/LG1twK03uiO00JkPk1ncQQNUnvt)
- [Documentación de Grok Bot sobre ordenadores y aplicaciones](https://cursor.com/cn/docs/grok-bot/work)
- [Guía de planes y límites de uso de Grok Bot](https://cursor.com/cn/help/grok-bot/plans)
- [Guía de configuración de rutinas programadas de Grok Bot](https://cursor.com/cn/help/grok-bot/routines)
- [Instrucciones de configuración de Grok Bot](https://cursor.com/cn/docs/grok-bot/settings)
- [Guía de uso de funciones principales de Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)
