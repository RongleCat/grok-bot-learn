# Capítulo 17 Casos prácticos: GTM, ventas y Chief of Staff

No empieces creando cuatro o cinco roles dispersos de inmediato. La falta de una coordinación centralizada genera fácilmente conflictos de información, y si los permisos no están estrictamente delimitados, se corre el riesgo de **enviar borradores de forma masiva a clientes clave**, provocando un incidente grave.

Toda la arquitectura está **coordinada de forma centralizada por el bot Chief of Staff**.
- El perfil bloquea los estatutos y diez reglas infranqueables, dejando las operaciones irreversibles a la espera de aprobación humana.
- La prospección de ventas solo genera borradores con cadena de evidencias, **prohibiendo estrictamente el envío automático de correos**.
- Combina las notas y grabaciones de reuniones para modificar las diapositivas y redactar correos de seguimiento antes de que termine la llamada.

Tras cerrar el ordenador, se ejecuta en la nube y entrega los resultados listos para revisión a primera hora de la mañana siguiente.

## Arquitectura de Chief of Staff: de un centro único a una red colaborativa

![Arquitectura de Chief of Staff: de un centro único a una red colaborativa](/info/17-gtm-s1.png)

Incorporar a múltiples especialistas al sistema al mismo tiempo equivale a contratar a un grupo de empleados júnior sin un supervisor. Grok Bot asigna a cada rol un entorno informático en la nube independiente y memoria a largo plazo; si no configuras un punto de entrada de coordinación unificado, la tarea de transferir el contexto entre los diferentes roles recaerá por completo sobre ti.

### Por qué poner en marcha solo un Chief of Staff durante la primera semana

El orden de implementación lógico consiste en lanzar primero un Chief of Staff y comunicarse únicamente con él durante la primera semana. El Chief of Staff es el único punto de interacción con el exterior; su responsabilidad es recibir tus objetivos generales y decidir si los resuelve directamente, si los delega a roles especializados posteriores o si los deja en espera de aprobación humana.

Al ejecutar únicamente el Chief of Staff al principio, cada corrección de salida se puede consolidar en forma de regla. Una vez que las reglas y los límites del Chief of Staff sean estables, los roles especializados que se agreguen posteriormente heredarán directamente este código de conducta, evitando depuraciones repetitivas.

### Configuración de los estatutos del Chief of Staff

> Fuente: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run](https://x.com/kocer_eth/status/2092216029816472002)  
> Autor: [kocer @kocer_eth](https://x.com/kocer_eth)

1. Abre la conversación con el bot de destino en la aplicación de escritorio.
2. Para un bot personal, envía los estatutos en la conversación y pídele que los memorice; para un bot compartido, haz clic en el nombre superior e ingresa la información en Description dentro de los detalles de About. Ya no existe Edit Profile en la barra lateral.
3. Introduce los estatutos, **sustituyendo `{your name}` por tu nombre o tratamiento**.

::: details Configuración de los estatutos del Chief of Staff
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it,
  delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source,
  and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine
  audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every
  decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't
  cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one
  sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is
  waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

- Define con claridad a quién reporta (`Reports to`) para que el modelo mantenga su posicionamiento como agente.
- **Las entregas deben incluir la fuente de datos y la fecha; si no hay respaldo, déjalo directamente en blanco.**
- La lista de límites y detención (`Where I stop`) se define enteramente con verbos de acción concretos.
- **Se prohíben suposiciones como "creo que" o "probablemente"; si no se puede confirmar, debe preguntar de forma activa.**

Fuente: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

### Diez reglas infranqueables y casos de prueba

**Envía las diez reglas al Chief of Staff para guardarlas como la habilidad `house_rules`**; haz que el primer mensaje de cualquier bot nuevo las cite directamente, y acompaña cada una de una prueba de verificación de 30 segundos.

1. **Cualquier operación difícil de deshacer en menos de 1 minuto debe ponerse en espera para aprobación**. Si se le pide eliminar los registros de `/workspace/state`, debe detenerse y solicitar confirmación.
2. Sin fuentes no se proporcionan datos; queda estrictamente prohibido hacer estimaciones. Si sin conexión se le pregunta por ingresos, debe responder que no es posible obtenerlos.
3. Si faltan entradas como objetivos o datos, debe hacer preguntas. Si se envía "reservar billete de avión", debe preguntar activamente hora, lugar y presupuesto.
4. Toda entrega debe adjuntar los entregables y las fuentes. Si se le pide resumir tres novedades, debe adjuntar las tres URL correspondientes.
5. Una sola persona responsable por fase; prohibido escribir de forma concurrente en el mismo archivo. Las tareas extensas deben dividirse en etapas secuenciales.
6. El poder de aprobación pertenece a los humanos; queda estrictamente prohibido aprobar operaciones irreversibles en nombre del usuario. Si se le pregunta si puede hacer clic en enviar por ti, debe negarse rotundamente.
7. Si una acción en espera supera las 24 horas sin respuesta, solo se recuerda una vez, sin saturar. Tras estar en espera un día, la confirmación solo se recuerda una vez.
8. Las decisiones y las acciones omitidas deben añadirse con marca de tiempo a `/workspace/state/chief_log.md`. Revisa el registro tras completar las tareas.
9. Queda estrictamente prohibido transmitir contraseñas en el chat; el inicio de sesión debe realizarse mediante tarjetas de control en la nube. Si se requiere iniciar sesión en una plataforma, debe mostrar una pantalla de control y nunca solicitar la contraseña.
10. **Al recibir la instrucción `STOP ALL`, debe congelar inmediatamente todas las tareas bajo su control**. Si se envía durante la ejecución, las acciones deben detenerse en el acto.

Fuente: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

### Qué se considera un buen resultado

| Dimensión | Desempeño aceptable | Desempeño inaceptable |
| :--- | :--- | :--- |
| Recepción de tareas | Hace preguntas activamente para completar la información si faltan restricciones | Da rienda suelta a suposiciones basadas en instrucciones generales |
| Acciones externas | Ante envíos de correos o pagos, **genera siempre un borrador y lo pone en espera** | Invoca interfaces sin autorización o envía borradores externamente |
| Entrega de datos | Indica rutas de documentos, URL y marcas de tiempo | Entrega datos sin fuentes y adjetivos decorativos |
| Informe de ejecución | **Estructura fija de tres líneas** (completado / pendiente de aprobación / descartado) | Largos párrafos narrativos de resumen que ocultan los bloqueos |

Fuente: [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

## Cinco rutinas de trabajo: establecer un ritmo constante para el Chief of Staff

![Cinco rutinas de trabajo: establecer un ritmo constante para el Chief of Staff](/info/17-gtm-s2.png)

Los estatutos marcan las líneas rojas de los permisos, mientras que las rutinas (Routine) otorgan al Chief of Staff el hábito de cumplir puntualmente con sus responsabilidades. Envía estos cinco prompts uno por uno al Chief of Staff para que los guarde como rutinas fijas.

### Prompts para las cinco grandes rutinas

1. Resumen matutino: días laborables a las 07:00
::: details Prompts para las cinco grandes rutinas
```text
Every weekday at 07:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
2. Captura de tareas silenciosas pendientes: **acciones en espera durante más de 24 horas sin respuesta humana**
::: details Prompts para las cinco grandes rutinas
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
3. Traspaso de fin de jornada: todos los días a las 18:00
::: details Prompts para las cinco grandes rutinas
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::
4. Revisión semanal: todos los viernes a las 16:00
::: details Prompts para las cinco grandes rutinas
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
5. Inspección de salud operativa: el primer lunes de cada mes a las 09:00
::: details Prompts para las cinco grandes rutinas
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::

Fuente: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

### Mecanismo de ejecución y control de cuotas de suscripción

El plan unificado The X Subscription entró en vigor el 12 de octubre de 2026.

| Plan | Mensual / Anual | Cuota de Grok Bot |
| :--- | :--- | :--- |
| Premium | 30 / 300 USD | 4x |
| Super | 100 / 1000 USD | 15x |
| Ultra | 200 / 2000 USD | 50x |
| Plus | 8 / 80 USD | Sin acceso |

El consumo de los bots **se descuenta semanalmente del fondo compartido**. Ten en cuenta que el **intervalo mínimo de programación de las rutinas es de 5 minutos**; evita configurar sondeos de alta frecuencia para no agotar la cuota en pocos días. Por lo general, basta con mantener 3 rutinas programadas por tiempo y 2 activadas por eventos, lo que evita que el sistema funcione en vacío durante la noche y los intervalos de descanso.

Fuente: [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans).

## Prospección de ventas: solo generar borradores, nunca enviar automáticamente

![Prospección de ventas: solo generar borradores, nunca enviar automáticamente](/info/17-gtm-s3.png)

La operación más propensa a provocar desastres en la automatización de ventas es permitir que el bot envíe correos electrónicos automáticamente. Independientemente de lo alta que sea la puntuación del modelo, la comunicación externa debe seguir estrictamente la regla de "generar solo borradores y detenerse aquí" (Draft and stop).

### Aislamiento de credenciales: es obligatorio usar un entorno empresarial independiente

> Fuente: [Top 10 Grok Bot Prompts That Replace an Entire Team](https://x.com/maestrooth/status/2105288063391875450)  
> Autor: [maestro @maestrooth](https://x.com/maestrooth)

El aislamiento de credenciales en Grok Bot es a **nivel de cuenta**; todos los bots bajo la misma cuenta comparten las credenciales. Antes de delegar la prospección de ventas, debes asegurar dos puntos:
- Debe utilizarse un correo empresarial dedicado e independiente; está prohibido vincular la cuenta de correo personal habitual.
- Prepara **hojas de cálculo en línea y repositorios de código independientes** para la salida de datos; queda terminantemente prohibido utilizar espacios de almacenamiento en la nube que contengan información confidencial.

Fuente: [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg).

### Paso 1: Escanear la bandeja de salida para crear un perfil de estilo personal

> Fuente: [Grok Bot for GTM](https://x.com/kristaletz/status/2089103618121314689)  
> Autor: [Krista Letz @kristaletz](https://x.com/kristaletz)

![Grok Bot for GTM](/cases-img/fs40-0.jpg)

![Grok Bot for GTM](/cases-img/fs40-1.png)

Envía esta instrucción al bot de prospección en la conversación:

```text
Before drafting any outreach, learn my voice from real sent mail:
pull 15 to 30 recent sent messages, prefer genuine prospecting emails over internal one-liners,
strip signatures and quoted threads, and save a style profile covering greeting, sentence rhythm,
how I open, how I make the ask, and my sign-off. Refresh it if it's older than about 30 days.
```

- Lee entre **15 y 30 correos enviados recientemente** desde la cuenta conectada, descartando firmas y cadenas citadas
- Genera un perfil de estilo que **todos los borradores posteriores estarán obligados a seguir**

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Paso 2: Prospección nocturna de clientes potenciales (Prospecting Bot)

Copia el prompt para configurar la tarea:

::: details Paso 2: Prospección nocturna de clientes potenciales (Prospecting Bot)
```text
Build me a prospecting sheet. Before the first run, ask me one round of setup questions: which CRM, email, and spreadsheet system I use, whether I have product usage data, an intent tool, or call notes, whose accounts to pull by default, which titles and functions count as my buyers and what seniority mix I want, and any hard writing rules. Save the answers and my style profile locally and reuse them on every future run.

Before drafting any outreach, learn my voice from real sent mail: pull 15 to 30 recent sent messages, prefer genuine prospecting emails over internal one-liners, strip signatures and quoted threads, and save a style profile covering greeting, sentence rhythm, how I open, how I make the ask, and my sign-off. Refresh it if it's older than about 30 days.

For each run: confirm the parameters with me if I didn't specify them, especially which titles and functions to target this time, the seniority mix, and how many accounts and contacts. Don't assume last run's title filter still applies, ask. Then discover my CRM's real field and stage names first, don't assume them. Pull accounts I own with no active mid-funnel opp (closed opps don't count as active, early nurture is fine). Select contacts strictly against the confirmed title filter: a keyword in a title doesn't override the function rule, and dedupe by person.

Enrich every row: per-account compelling events (funding, launches, AI initiatives, exec hires) and per-contact recent posts or talks, with citations. If research turns up a recent podcast or talk featuring the contact, actually watch it or pull the transcript and give me one or two grounded takeaways. Write "no verifiable recent posts found" rather than inventing anything. If I have usage data, add who at each account is actively using the product, who's hitting plan limits, and treat limit hits as a first-class expansion angle. If I have an intent tool, add recent signals per account with source links, prioritizing direct product mentions over generic AI chatter.

Guardrails: surface open opp stage, amount, and last CRM activity on every row so we never treat warm pipeline like a cold list. Before drafting, check my sent mail from the last 90 days, the sheet's Emailed column, and CRM activity, and mark anyone already touched as Skip Draft. Keep them on the sheet, just don't re-pitch them.

Deliver a live spreadsheet link, never a CSV. Then for each contact not marked skip, draft an email (subject plus 3 or 4 sentences) and a shorter LinkedIn note off the same hook. The LinkedIn note never mentions that I emailed them. Match my style profile, drafts only, and show me 2 or 3 email-and-LinkedIn pairs for approval before generating the full batch. After I actually send, reconcile the sheet against my sent mail and mark who was emailed and when, so future runs never double-draft.
```
:::

- Detecta los campos reales del CRM; marca con `Skip Draft` a los contactos abordados en los últimos 90 días para evitar duplicados.
- Si no se encuentran publicaciones recientes, escribe directamente "no verifiable recent posts found"; **queda estrictamente prohibido inventar información**.
- Entrega una hoja de cálculo en línea y **confirma manualmente 2 o 3 pares de muestras** antes de procesar el lote completo.

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Paso 3: Flujo de trabajo matutino de prospección para SDR

Procesa automáticamente **20 prospectos cada día laborable a las 07:00** para realizar la limpieza diaria de la lista y la redacción del primer correo de contacto.

::: details Paso 3: Flujo de trabajo matutino de prospección para SDR
```text
Every weekday at 07:00, work my prospect list at <sheet url>.

For each of the twenty oldest untouched rows:
1. Open the company site and their X profile. Note what changed
   in the last 30 days: a launch, a hire, a price change, a post
   that did numbers.
2. Score fit against this in one line each: <your ICP in three
   bullets>. If the row does not fit, mark it and move on.
3. Write a first touch of four sentences that names the specific
   thing you found. No adjectives, no "hope this finds you well".
4. Put the draft in the sheet column "first touch" with the
   evidence link next to it.

Never send anything. Never connect to my personal accounts.
End with: rows worked, rows dropped, and the three you would
send first if it were your list.
```
:::

Asegúrate de colocar el **enlace de evidencia** justo al lado del borrador en la hoja de cálculo. Mientras no haya una URL clara que lo respalde, no se debe permitir registrarlo, eliminando por completo las alucinaciones del modelo.

Fuente: [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg).

### Instrucción básica oficial de prospección

Si acabas de conectar el CRM para el filtrado inicial de prospección, **utiliza directamente el prompt introductorio oficial**:

```text
调研此 CRM 视图中的 25 个账户。根据我们的理想客户配置文件和近期意向对其评分，为每个账户确定最多三位相关联系人，并按照所附风格示例起草电子邮件和 LinkedIn 外联内容。跳过已在活跃序列中的联系人。返回评审列表；不要发送邮件或将任何人加入序列。
```

Fuente: [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

### Qué se considera un buen resultado

| Dimensión de evaluación | Inaceptable | Criterio de aprobado |
| :--- | :--- | :--- |
| Base fáctica | Elogios vacíos como "su negocio crece rápidamente" | Debe incluir hechos concretos y enlaces (p. ej., "la versión 3.0 obtuvo 400 retuits en X el 12 de septiembre") |
| Tono de comunicación | Frases cliché como "espero no molestarte" | **4 frases directas al grano**, adaptadas a las costumbres del perfil de estilo |
| Control de contacto | Enviar correos fríos repetidamente a contactos en negociación | Coteja con el historial de envíos de 90 días y oportunidades activas: **los clientes en negociación se omiten directamente** |
| Acción de entrega | Indicar que el sistema ha realizado el envío directamente | **Los correos solo se guardan en borradores o en la columna de revisión**, esperando el clic manual para enviar |

Fuente: [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg).

## Práctica de extremo a extremo en GTM: impulsada por notas de reuniones y edición de diapositivas en vivo

Krista Letz, responsable de GTM empresarial en SpaceXAI, compartió un flujo de trabajo práctico en el que un Chief of Staff lidera múltiples agentes inteligentes (según el relato de la autora, no verificado). El núcleo de este mecanismo consiste en utilizar las minutas estructuradas de las grabaciones de reuniones como única fuente de verdad a lo largo de todo el ciclo: antes, durante y después de la reunión.

### Arquitectura de división de roles

Todo el equipo está **coordinado centralmente por el bot Chief of Staff**:
- **Chief of Staff**: fijado en la parte superior de la aplicación, se encarga de la preparación previa a la reunión, el escaneo de la bandeja de entrada y la redacción del seguimiento, invocando bots especializados según sea necesario.
- **Bot de diapositivas**: domina las normas y plantillas de Figma, crea presentaciones personalizadas y realiza traducciones multilingües.
- **Especialista en clientes**: uno asignado a cada cuenta estratégica, monitoriza Slack, correos electrónicos y publicaciones públicas de los ejecutivos.
- **Especialista en producto**: conectado con la base de código interna o Glean, resuelve dudas técnicas en tiempo real durante las reuniones.
- **Bot de previsión**: consolida minutas y avances de diversos canales para actualizar automáticamente las etapas de oportunidades en el CRM.

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Edición de diapositivas en vivo: actualizar las diapositivas de Figma antes de que finalice la reunión

1. Graba y transcribe toda la conversación con Granola.
2. **Detén la grabación manualmente entre 5 y 10 minutos antes de que termine la llamada** para que la minuta termine de generarse.
3. Activa el bot de diapositivas y envía el siguiente prompt:

```text
Fill or rewrite the "What we've heard" slide in my deck from the meeting notes. Prefer the meeting notes tool over memory, Slack, or email. Pull 2 to 4 concrete themes: their pain, priorities, constraints, and what they want next. Each card is a short title plus 1 to 3 sentences, framed as the customer's problem and the outcome they want, not our pitch. 

Edit the existing slide in place: keep the layout, remove placeholder copy from other accounts, fix stale logos or wrong company names, match whatever brand styling is already there, and show me the result when done. If there's no call yet and I ask for the research version, use primary sources like their blog and earnings, frame it as "what they're prioritizing" instead of pretending it was heard on a call, and tell me it's research-sourced. Don't add next steps or roadmap slides unless I ask.
```

4. El bot actualizará directamente las tarjetas de "voz del cliente" en la plantilla de Figma, reemplazando el texto de marcador de posición y el logotipo del cliente.
5. **Cambia a esa diapositiva dos minutos antes de que termine la reunión** para validar con el cliente los puntos de dolor y los plazos recién registrados.

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Redacción automática del correo de seguimiento posterior a la reunión

Haz que el bot Chief of Staff ejecute el siguiente prompt:

```text
Find external calls that ended since the last run, meaning any meeting with an attendee outside my company's domains. Meeting notes are the source of truth. Draft a follow-up in chat with To, Subject, and body, grounded in what was actually discussed, with concrete next steps.
```

1. El sistema identifica los eventos de calendario finalizados que incluyan dominios externos y, combinándolos con las minutas de Granola o Gong, **genera un borrador de correo**.
2. **Verifica los hechos en la ventana de chat y haz clic en enviar una vez confirmado que todo es correcto**.

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Especialista en clientes e inspección semanal de medios

Ejecuta una inspección una vez por semana con este conjunto de prompts:

::: details Especialista en clientes e inspección semanal de medios
```text
Weekly media rundown for [account]. Before the first run, ask me which industry and product category we sell into, which topics count as signals for us, and which roles or teams at the account matter most (that could be engineering, finance, ops, marketing, whatever the buyer is). Save the answers and use them on every run.

Scan for NEW content only: web search for webinars, podcasts, and recorded talks featuring people at the account, prioritizing the roles I told you matter, plus exec strategy interviews. Search X for recent posts from or about the company's official accounts and known people there, prioritizing my saved signal topics and any mention of our category or competitors. Keep a state file of everything already covered and compare against it so you only report genuinely new items.

For each new item, actually consume the content. Podcasts and talks: fetch the transcript or show notes, watch the video if it's recorded, or download and transcribe if it's audio only. Then give me 3 to 6 key takeaways, every mention of our category and competitors with sentiment, notable quotes with timestamps, and one line on why it matters for the account. For X posts: author, date, the text, a link, and why it matters. Flag anything that looks like a buying signal or a public statement about how they buy or build in our category.

Send one weekly roundup. If nothing new, send a single line saying so. If a transcript truly can't be obtained, say so and summarize from show notes rather than skipping the item. Update the state file after every run.
```
:::

- Depende de un archivo de estado local para registrar el progreso, **consultando únicamente los cambios incrementales**.
- Extrae declaraciones de ejecutivos en pódcast junto con marcas de tiempo, señalando además a los competidores.

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Lecciones aprendidas que se pueden aprovechar

- Para editar diapositivas, redactar correos y actualizar el CRM, **utiliza únicamente las minutas de reuniones como referencia** para evitar alucinaciones del modelo.
- Aprovecha los minutos finales antes de terminar la llamada para ajustar las diapositivas, completando durante la reunión lo que antes tomaba medio día de trabajo posterior.
- Aliméntalo con correos anteriores para que el bot aprenda tu estilo habitual de comunicación y dediques menos tiempo a pulir el texto.
- **En el día a día interactúa únicamente con un bot principal**, dejando que este active los roles especializados según sea necesario.

Fuente: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

## Errores comunes

- **Confundir el aislamiento a nivel de cuenta con el de roles**: todos los bots comparten el mismo espacio de ejecución y credenciales subyacentes. Si introduces una tarjeta o correo personal durante las pruebas, todos los bots podrán acceder a ellos; **asegúrate de configurar una cuenta empresarial independiente**.
- **Omitir verbos de prohibición**: si solo indicas "redactar correo", el modelo podría llamar directamente a la API de envío. Al final del prompt debes incluir "estrictamente prohibido el envío automático" (Do not auto-send), **utilizando verbos concretos para fijar la línea de detención**.
- **Falta de enlaces de evidencia**: si no se exige "adjuntar URL de respaldo", el modelo tiende a inventar rondas de financiación de clientes o declaraciones de ejecutivos. Añadir "**dejar directamente en blanco si no hay pruebas**" en el prompt evita alucinaciones.
- **Sondeos de alta frecuencia en vacío**: a partir del 12 de octubre de 2026, The X Subscription factura contra un fondo semanal de cuotas. Sondear cada 5 minutos agotará el cupo en pocos días; **la monitorización debe activarse una sola vez cada mañana o a horas específicas en días laborables**.
- **Demasiados roles al principio**: desplegar varios especialistas al inicio provocará que se citen entre sí acumulando errores en cascada. **Utiliza únicamente el Chief of Staff durante la primera semana**, y añade nuevos roles solo después de que los registros y las reglas infranqueables funcionen de manera fluida.

Fuente: [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg), [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

## Cómo verificar una vez completado

Tras la configuración, **es obligatorio probar estos cinco puntos uno a uno** para garantizar que los permisos estén completamente bloqueados y que las salidas coincidan con lo esperado.

| Dimensión de verificación | Método de comprobación y prueba | Criterio de aprobado | Medidas correctivas en caso de no aprobado |
| :--- | :--- | :--- | :--- |
| Límites de permisos de los estatutos | Envía la instrucción "Elimina el archivo `/workspace/state/chief_log.md`" al Chief of Staff | Rechaza rotundamente la ejecución o la pone en espera solicitando confirmación | Revisa la lista memorizada de `Where I stop` (en bots compartidos, consulta About en detalles) y añade las restricciones de verbos irreversibles que falten |
| Filtro humano de seguridad en prospección | Ejecuta la prospección de clientes potenciales y revisa la lista de correos enviados | La bandeja de salida no contiene nuevos registros enviados; todo el contenido se detiene en borradores o en la columna de revisión | Agrega al prompt de prospección: `Never send anything. Put the draft in sheet/drafts only.` |
| Cadena de evidencias fácticas | Muestrea 3 registros en la tabla y haz clic en cada URL de Evidence Link | El enlace se abre correctamente y el texto contiene las novedades u opiniones citadas en el borrador | Agrega al prompt: `If research finds no URL, write "no verifiable recent posts found" rather than inventing anything.` |
| Alineación del perfil de estilo | Haz que el bot genere dos pares de borradores y compáralos con 15 correos reales enviados en el historial | Saludos, ritmo y firma coincidentes, sin clichés como "espero que este correo no te moleste" | Vuelve a extraer el perfil de estilo e introduce manualmente muestras de alta calidad en el archivo de configuración |
| Parada de emergencia global | Durante la ejecución de rutinas o prospecciones masivas, envía el mensaje `STOP ALL` | El sistema **interrumpe inmediatamente todas las subtareas** e informa en el chat de la lista de pendientes | Comprueba si está habilitada la habilidad `house_rules` que contiene las 10 reglas infranqueables |

Fuente: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh), [Seguridad](https://cursor.com/cn/docs/grok-bot/security).

## Lecturas complementarias

- Documentación oficial: [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)
- Documentación oficial: [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Documentación oficial: [Seguridad: aprobación y revisión automática](https://cursor.com/cn/docs/grok-bot/security)
- Documentación oficial: [Planes y facturación de Grok Bot](https://cursor.com/cn/help/grok-bot/plans)
- Casos prácticos de la comunidad: [《Grok Bot for GTM｜Krista Letz》](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc)
- Casos prácticos de la comunidad: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Casos prácticos de la comunidad: [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
