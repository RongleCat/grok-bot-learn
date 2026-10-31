# Capítulo 2 Planes y suscripciones: elige primero el nivel adecuado

**Ya puedes pagar directamente con Alipay.** Al suscribirte a X o Grok desde la web, si seleccionas China continental, Hong Kong, Macao o Taiwán como región de facturación, podrás elegir Alipay o UnionPay como método de pago, cobrándose en RMB al cambio del precio en USD (ambos comparten dicho sistema de pago). Por el momento no hay un anuncio oficial y algunas cuentas podrían seguir en fase de pruebas graduales; consulta la disponibilidad real según lo que se muestre en tiempo real en la página de pago.

Los principiantes a menudo se encuentran con tres problemas comunes al comprar:
- Comprar el plan inicial más económico y, al abrir el cliente, no encontrar el acceso a los agentes.
- **La suscripción de Cursor y la cuota semanal de SuperGrok no se acumulan; el sistema solo reconoce la más alta.**
- Hacer clic en actualizar dentro de la app móvil no permite cambiar de plan y, además, se pierde el uso previo de modelos de terceros.

Grok Bot funciona en base a cuotas. **Si se agota el uso semanal y no se ha configurado la protección bajo demanda, las tareas de automatización en la nube se detendrán de inmediato.**

Desde el 12 de octubre de 2026, se introdujo oficialmente la suscripción unificada The X Subscription, dividida en un nivel gratuito y cuatro niveles de pago.


![Planes y suscripciones: elige primero el nivel adecuado](/info/02-plans.png)

## ¿Qué plan de suscripción necesito comprar para usar Grok Bot? {#统一订阅全貌-the-x-subscription-的四档与免费档}

**La suscripción unificada se divide en cuatro niveles: Plus, Premium, Super y Ultra. Como el nivel Plus no incluye en absoluto Grok Bot, para ejecutar tareas de automatización es obligatorio empezar con el nivel Premium de $30 al mes.**

![Panorama de la suscripción unificada: los cuatro niveles y el nivel gratuito de The X Subscription](/info/02-plans-s1.png)

### Qué es

A partir del 12 de octubre de 2026 se unificó en The X Subscription, donde el pago anual equivale a 10 veces el pago mensual.

Calculado según el uso por dólar (tomando Plus como base 1, Premium aprox. 1.07, Super aprox. 1.2, Ultra aprox. 2.0; declaración del autor, no verificada), cuanto más alto sea el nivel, más rentables resultan los modelos propios.

| Plan | Pago mensual / anual en la web | Grok Bot |
| :--- | :--- | :--- |
| **Nivel gratuito** | $0 | Prueba de cuota de 7 días |
| **Plus** | $8/mes (aprox. $7 al mes prorrateado) / $80/año | No incluido |
| **Premium** | $30/mes / $300/año | Incluido (umbral de entrada) |
| **Super** | $100/mes / $1000/año | Incluido |
| **Ultra** | $200/mes / $2000/año | Incluido (cuota máxima) |

**El nivel Plus no incluye en absoluto Grok Bot ni Cloud agents**; para ejecutar tareas de automatización se debe elegir, como mínimo, el nivel Premium de $30 al mes. La prueba gratuita tiene una validez limitada de 7 días, y la cuota se descuenta según el tamaño de la tarea, los pasos y los tokens; una tarea pesada podría consumirla por completo de una sola vez y no se restablece tras agotarse.

### Cómo hacerlo

**Se recomienda activar la suscripción a través de la web y evitar pagar desde dispositivos móviles.**

1. Accede desde el navegador a la página de suscripción unificada [grok.com/com/overlay/subscribe](https://grok.com/com/overlay/subscribe?from=/).
2. Inicia sesión con la cuenta de X o Grok que utilices para trabajar.
3. Elige el nivel Premium ($30/mes; la comunidad ha visto promociones del 50% de descuento en el primer mes a $15, sujeto a la página de pago).
4. **Elige el pago mensual en lugar de marcar directamente el anual**, lo que facilita cambiar de nivel o de herramienta en cualquier momento.
5. Paga con tarjetas de crédito o débito internacionales compatibles, o con Apple Pay y Google Pay en la web; si seleccionas China continental, Hong Kong, Macao o Taiwán como región de facturación, también aparecerán las opciones de pago de Alipay y UnionPay en la página de pago.
6. Abre el cliente de Grok Bot, inicia sesión y confirma que en la interfaz principal ya se hayan desbloqueado los permisos para crear y ejecutar agentes.

Para un análisis detallado, consulta [«Análisis de la suscripción unificada de X: ¿cómo eligen los nuevos usuarios y deberían cambiarse los antiguos suscriptores? Explicado con claridad»](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee) y [«Colección de tuits de 铁柱 ①: Apertura, planes y cuota»](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc).

### Cuándo se considera correcto

Al abrir el cliente de escritorio de Grok Bot, **se considera apto si las nuevas tareas pueden asignarse a un entorno en la nube para ejecutarse y la facturación muestra el estado Premium con cobro mensual**.

## ¿Cómo se liquida el fondo de uso semanal de Grok Bot? {#每周共享用量池-额度结算与多端共用机制}

**La suscripción proporciona un fondo de cuota fija semanal que se sincroniza en tiempo real entre múltiples dispositivos; los modelos oficiales se descuentan de forma compartida en la web, Bot y el autocompletado de Cursor según el volumen de tareas y los pasos, mientras que los modelos de terceros se cobran por separado según el precio de catálogo.**

![Fondo de uso compartido semanal: liquidación de cuota y mecanismo compartido multidispositivo](/info/02-plans-s2.png)

### Qué es

The X Subscription ofrece un fondo de cuota fija cada semana que se renueva automáticamente al vencer. **La versión web de Grok, Bot y las preguntas y respuestas con autocompletado de Cursor comparten este fondo**. Al iniciar sesión con la misma cuenta en Mac e iPhone, la cuota se sincroniza en tiempo real, sin cobros duplicados al cambiar de dispositivo.

| Categoría de modelo | Regla de liquidación |
| :--- | :--- |
| Modelos oficiales | Se incluyen en el fondo compartido; tanto la web como Bot descuentan cuota de aquí. La velocidad de consumo solo depende del volumen de tareas y los pasos. |
| Modelos de terceros | **No se incluyen en el fondo compartido**; en Cursor se cobran por separado según el precio oficial de la API. |

El sistema asigna automáticamente el modelo subyacente de Bot, etiquetado uniformemente como "Uso de Grok Bot", sin posibilidad de selección manual o bloqueo. Para más detalles, consulta [Modelos de Grok Bot](https://cursor.com/cn/help/grok-bot/models.md).

### Cómo hacerlo

Para evitar agotar la cuota en los primeros tres días, planifica la rutina diaria en tres pasos:

1. **Ejecuta primero las tareas pesadas clave al inicio de la semana**. Prioriza la redacción de código central, la creación de arquitectura y la depuración de lógica compleja.
2. **Evita operaciones de alto consumo**. La generación masiva de vídeo, el sondeo de alta frecuencia y la coordinación entre múltiples Bot consumen la cuota más rápido (declaración del autor, no verificada); se recomienda generar vídeos en la versión web y no incluirlos en el flujo de trabajo de Bot.
3. **Presta atención al ciclo de reinicio**. Ten clara la fecha de reinicio semanal indicada en el panel; cuando se acerque el reinicio y aún quede saldo disponible, aprovecha para realizar tareas concentradas de organización de datos o revisión exhaustiva.

### Cuándo se considera correcto

**En automatizaciones habituales, mantén el consumo diario estable entre el 10% y el 15%**. Si reservas un margen de amortiguación de alrededor del 20% el día anterior al reinicio semanal y no recibes ventanas emergentes de advertencia por cuota crítica, el ritmo se considera adecuado.

## ¿Cómo vincular Cursor para compartir la cuota de Grok? {#授权互通-cursor-套餐与-supergrok-关联规则}

**Cursor se puede vincular directamente con una cuenta de Grok para mapear la cuota; la vinculación no modifica el plan original ni genera cargos adicionales, la cuota toma vigencia según el nivel más alto de ambos sin acumularse, y una vez emparejados queda bloqueada de por vida sin posibilidad de desvincularse o transferirse.**

![Interconexión de autorizaciones: reglas de vinculación entre planes de Cursor y SuperGrok](/info/02-plans-s3.png)

### Qué es

Una cuenta de Cursor puede vincularse directamente con una cuenta de Grok para compartir el uso. **Antes de realizar la vinculación, ten en cuenta tres reglas estrictas:**

- Solo sincroniza la cuota, no modifica el plan: el uso se mapea directamente, no cambia el plan actual de Cursor y no genera cobros adicionales.
- La cuota no se acumula, solo reconoce el nivel más alto: se aplica la cuota semanal mayor entre ambas; por ejemplo, si Cursor Pro se vincula a SuperGrok Plus, se elevará a la cuota de Plus.
- Bloqueo de por vida tras la vinculación, no se puede desvincular: una vez completado el emparejamiento con éxito, **ni mediante operaciones propias ni contactando a soporte técnico será posible desvincular o transferir la autorización.**

| Nivel de suscripción de Cursor | Nivel equivalente vinculado | Uso semanal de Grok Bot |
| :--- | :--- | :--- |
| Cursor Pro | SuperGrok / X Premium+ | Cuota semanal básica |
| Cursor Pro+ | SuperGrok Plus | Cuota semanal abundante |
| Cursor Ultra | SuperGrok Heavy | Cuota semanal máxima |
| Sin plan de Cursor | SuperGrok Lite | No incluye Grok Bot (el nivel Lite no tiene permisos, requiere actualizar antes de vincular) |

Si se tiene asignado un asiento empresarial de Grok Business, la cuenta ya incluye permisos de Bot por defecto, **por lo que no es necesario realizar ninguna operación de vinculación en la página.**

### Cómo hacerlo

La vinculación de cuentas individuales se realiza en la web:

1. Inicia sesión en la versión web de Grok Bot desde el navegador con la cuenta de Cursor que recibirá la cuota, asegurándote primero de que la cuenta principal sea correcta.
2. Abre el enlace de inicio rápido [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding).
3. Haz clic en vincular cuenta de Grok (Link Grok Account); en el móvil, pulsa el botón con el mismo nombre en la página de suscripción.
4. Tras la redirección, inicia sesión con la cuenta que disponga de SuperGrok, SuperGrok Plus, SuperGrok Heavy o X Premium+ para otorgar la autorización.
5. Vuelve a la página de configuración del cliente para confirmar el estado. **La nueva cuota puede tardar hasta 24 horas en sincronizarse; durante este periodo, evita hacer clic repetidamente en vincular o intentar desvincular.**

Consulta las reglas completas en la documentación oficial [Vincular SuperGrok para Grok Bot](https://cursor.com/cn/help/grok-bot/supergrok.md).

**Los usuarios con un asiento empresarial asignado solo necesitan iniciar sesión directamente, sin necesidad de vinculación adicional:**

1. En la versión de escritorio, abre Settings > General y haz clic en Sign Out para cerrar la sesión actual; haz lo mismo en la app móvil.
2. Vuelve a la página de inicio de sesión y haz clic en Sign in with Grok.
3. Introduce las credenciales de Grok que tienen asignado el asiento de Business para iniciar sesión; el sistema montará automáticamente la cuota de dicho asiento.

### Cuándo se considera correcto

Abre Settings > Usage & Billing en la aplicación de escritorio.

**Si debajo de la gestión de planes se muestra la etiqueta del nivel vinculado correspondiente, la barra de cuota semanal indica el ciclo de reinicio y no hay cobros duplicados en la cuenta, la vinculación habrá sido exitosa.**

## Asientos de la versión de equipo y configuración de pago bajo demanda (On-demand)

### Qué es

Los miembros del equipo inician sesión en Grok Bot directamente con sus propias cuentas de Cursor y el consumo se descuenta de la cuota del equipo. **Los administradores no necesitan asignar asientos individualmente y los miembros no requieren aprobación previa**.

Una vez agotada la cuota semanal, se pasará automáticamente al uso bajo demanda (en la factura figurará como Billed through Cursor). El sistema cuenta con un mecanismo de protección: **las tareas que superen el límite mensual no se interrumpirán a mitad de camino**, lo que permite que la tarea actual finalice por completo.

### Cómo hacerlo

1. En el cliente, abre **Configuración** (Settings) > **Usage & Billing**.
2. Busca "Límite mensual de uso bajo demanda"; si aparece como Disabled, haz clic a la derecha en **Enable** para activarlo.
3. Para la primera configuración se requiere vincular una tarjeta de crédito; en [cursor.com/dashboard](https://cursor.com/dashboard), haz clic en **Gastos** (Spending).
4. En **Monthly Limit**, introduce un límite máximo de sobregiro mensual (por ejemplo, establece 20 o 50 dólares para evitar sobrecostos) y guarda los cambios.

**Las aplicaciones móviles de iOS y Android no permiten configurar los límites directamente**, por lo que es obligatorio acceder a la consola web. Para consultar los detalles de facturación, revisa la documentación oficial [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans.md).

### Cuándo se considera correcto

En Usage & Billing se puede ver que el uso bajo demanda está en estado activado y muestra el valor del límite configurado. **Cuando se agota la cuota semanal, las tareas no fallan ni se interrumpen con errores**, pasando de forma fluida al canal bajo demanda para completarse.

## Guía de toma de decisiones y operaciones para cambiar suscripciones antiguas

![Guía de toma de decisiones y operaciones para cambiar suscripciones antiguas](/info/02-plans-s5.png)

### Qué es

La gran suscripción unificada The X Subscription se lanzó el 12 de octubre de 2026. Para los usuarios que no cambien voluntariamente, su plan, precio y funciones originales se mantendrán sin cambios. El ciclo de pago anual se conservará íntegro hasta su vencimiento natural, y cualquier cambio posterior solo entrará en vigor en el momento de la renovación.

**Una vez confirmada la operación en la web, tendrá efecto permanente; ni siquiera contactando a soporte será posible revertirla o recuperar el plan antiguo**. La suscripción anterior se cancela automáticamente en el momento de la liquidación y se emite un reembolso prorrateado por días; este reembolso no se puede deducir del nuevo plan, el cual debe pagarse en su totalidad, y el ciclo de facturación se reinicia desde ese mismo día. Actualmente, las aplicaciones móviles no admiten el cambio; es obligatorio realizarlo desde la web.

| Canal de pago y producto de suscripción | Vía de reembolso y acción del usuario |
| :--- | :--- |
| Planes antiguos adquiridos directamente en la web | La plataforma emite automáticamente un reembolso prorrateado a la tarjeta de pago original, sin requerir intervención manual adicional. |
| Grok / X Premium suscrito a través de Apple | La plataforma asiste en la solicitud y Apple toma la decisión final sobre el monto a reembolsar. |
| Cursor suscrito a través de Apple | **El usuario debe acudir personalmente en el sistema iOS a «Apple ID → Suscripciones» para cancelar manualmente y solicitar el reembolso al soporte de Apple**. |
| Servicios suscritos a través de Google Play | **El usuario debe cancelar manualmente la renovación automática en «Pagos y suscripciones» de Google Play**. |

### Caso práctico: crónica de la decisión de un autor de la comunidad ante la suscripción unificada

Un desarrollador de la comunidad que cuenta con un plan anual válido hasta 2027 (declaración del autor, no verificada), tras analizar su consumo, decidió **no cambiar por el momento su suscripción antigua a la nueva versión unificada**, al tiempo que desactivó la renovación automática del plan original para seguir evaluando la situación.

El plan antiguo incluía descuentos a largo plazo que quedarían anulados de inmediato si se forzara el cambio. El nuevo fondo compartido semanal solo cubre los modelos propios; cualquier llamada a modelos de terceros debe pagarse por separado según el precio de catálogo de la API. Además, el fondo de uso semanal del nuevo plan se comparte entre todos los productos, por lo que ejecutar Bot en exceso restará cuota normal para el uso web y el autocompletado de código.

| Perfil de usuario | Características típicas y necesidades clave |
| :--- | :--- |
| A quién se recomienda cambiar | Quienes compran múltiples suscripciones dispersas por separado con un gasto mensual muy superior a $30, usan principalmente modelos oficiales y tienen una fuerte necesidad vinculada a la automatización de Grok Bot y la gestión de cuentas de X. |
| A quién NO se recomienda cambiar | Quienes disponen de planes antiguos con cuota adicional para modelos de terceros, o programan intensivamente solo en Cursor sin requerir beneficios sociales en X ni generación de vídeo. |

Antes de realizar el cambio, abre el panel de uso para comprobar la distribución real de llamadas y tener clara la proporción entre modelos propios y de terceros. En la medida de lo posible, suscríbete a las herramientas de IA mes a mes; las políticas de planes se reestructuran cada dos o tres meses y atarse a planes anuales de largo plazo suele dejarte en desventaja (declaración del autor, no verificada).

**Los usuarios que se hayan suscrito a Cursor a través de Apple deben cancelar manualmente la renovación automática en los ajustes del móvil tras decidir migrar**, ya que la actualización web no lo gestionará de forma automática.

Para más detalles sobre el análisis de decisiones, consulta [«Análisis de la suscripción unificada de X: ¿cómo eligen los nuevos usuarios y deberían cambiarse los antiguos suscriptores? Explicado con claridad»](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee) y [«Colección de tuits de 铁柱 ①: Apertura, planes y cuota»](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc).

### Cuándo se considera correcto

Los usuarios que mantengan el plan antiguo deben confirmar que el estado de renovación automática sea el deseado y que la cuota de los modelos principales esté intacta.

**Los usuarios que decidan cambiar al nuevo plan deben confirmar que la suscripción anterior se haya cancelado por completo y se haya recibido el reembolso por el canal original, que el nuevo plan facture con normalidad como Premium y que no existan cobros duplicados ni conflictos de canales en ninguno de los extremos.**

## Consulta de uso y configuración de prompts de prevención de pérdidas

### Qué es

**Ten clara primero la correspondencia de términos en ambas plataformas para evitar que la cuota se agote sin darte cuenta**:

- Límite de uso semanal (escritorio) / Uso semanal (móvil): fondo fijo de esta semana, se reinicia semanalmente. Si aparece asociado a SuperGrok, indica que la autorización ya está vinculada, sin incluir planes independientes de Cursor.
- Uso bajo demanda (Billed through Cursor): facturación adicional una vez agotado el fondo fijo. El límite mensual en la web se encuentra en Monthly Limit dentro de Gastos (Spending).
- Ruta de acceso: en el cliente de escritorio ve a Configuración (Settings) > Uso y facturación (Usage & Billing); en la app móvil pulsa en Uso semanal; en la web inicia sesión en [cursor.com/dashboard](https://cursor.com/dashboard).

### Cómo hacerlo

**Escribe las instrucciones de prevención de pérdidas directamente en el prompt del sistema de Bot o en el primer mensaje de la conversación**.

Para un solo Bot estándar, introduce el primer fragmento para fijar un razonamiento de bajo consumo y alargar los ciclos de sondeo, evitando la ejecución ociosa en segundo plano.

```text
你是一个自动化执行助手。在后续所有任务执行中，必须严格遵守以下资源控制规则：
1. 任务规划阶段必须输出极简执行步骤，禁止发起非必要的递归搜索与多轮冗余工具自检。
2. 在处理代码与文本分析任务时，保持适度推理强度，优先给出核心结果，不要输出冗长无关的修饰性文字。
3. 如果任务涉及定时轮询或周期监控，单次轮询时间间隔不得低于 30 分钟，严禁设置分钟级高频循环。
4. 严禁自行尝试调用外部视频生成或音频转换能力；如遇复杂多步骤任务，分步向我汇报进度并等待确认。
```

Para la coordinación de múltiples Bot, introduce el segundo fragmento. **La difusión frecuente entre múltiples Bot en la misma tarea es la trampa que consume cuota más rápidamente (declaración del autor, no verificada); es obligatorio forzar la comunicación en cadena punto a punto**.

```text
你在多智能体协同流水线中担任协同节点。必须严格执行以下通信约束：
1. 全面采用点对点（Agent-to-Agent）单向派活与回传，禁止向群聊或未指名的公共上下文广播全量数据。
2. 传递工作流结果时，只提取关键字段与结构化结果摘要，严禁将完整的历史对话日志重复打包转发。
3. 协助任务交付完毕后，立即输出任务终止状态，主动退出协作监听，切断后续消息的被动接收与重复解析。
```

Estrategia basada en [«Colección de tuits de 铁柱 ①: Apertura, planes y cuota»](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc).

### Cuándo se considera correcto

Tras inyectar el prompt, **el Bot debe responder explícitamente confirmando que cumplirá con las restricciones de recursos**. Si tras ejecutar scripts automatizados durante tres días consecutivos la curva de consumo en Usage & Billing del cliente se mantiene estable y las tareas programadas se ejecutan en intervalos puntuales sin registros de autocomprobación redundantes, se considera alcanzado el objetivo.

## Errores comunes

### Selección y suscripción

- **No compres el nivel Plus de $8 si quieres usar Bot**. No incluye Grok Bot ni Cloud agents; para usar Bot es obligatorio elegir el nivel Premium de $30.
- **Las cuotas de Cursor Pro y SuperGrok no se acumulan**. Activar ambos al mismo tiempo no otorgará el doble de cuota; el sistema solo contabilizará una de ellas, lo que supone un gasto innecesario.
- Los modelos de terceros se facturan por separado según el precio de catálogo de la API. El fondo compartido semanal de The X Subscription solo cubre los modelos propios.
- **Elige el pago mensual y no compres la suscripción anual**. Las herramientas y las reglas cambian con frecuencia; el pago anual bloqueará la flexibilidad para realizar ajustes posteriores.

### Vinculación y cancelación

- **La vinculación de cuentas es irreversible de por vida**. Una vez vinculado Cursor a SuperGrok o X Premium+, el servicio de atención al cliente no podrá desvincularlo; bajo ninguna circunstancia utilices cuentas secundarias de prueba para la autorización.
- La migración de suscripciones antiguas solo puede gestionarse desde la web en un ordenador; la app móvil no cuenta con opción de cambio.
- **Es obligatorio cancelar manualmente la renovación de Cursor en el iPhone**. Cambiar a la suscripción unificada desde la web no cancelará automáticamente los cobros de la App Store; si no se cancela manualmente, se cobrará por duplicado en ambas vías.

### Cuota y uso

- **Activa el uso bajo demanda y define un límite mensual**. Si se agota el fondo compartido semanal y no está activado el uso bajo demanda, el Bot dejará de responder de inmediato.
- **Utiliza la comunicación punto a punto en la colaboración de múltiples Bot**. Cada mensaje en un chat grupal se difunde a todos los Bot para su procesamiento; agregarlos a chats grupales permanentes consumirá la cuota semanal en pocas rondas.

## Cómo verificar la configuración final

1. **Permisos de la cuenta**: abre el cliente de escritorio, haz clic en el avatar de la esquina inferior izquierda y confirma que el plan sea **Premium, Super o Ultra**. Haz clic en crear nuevo Bot y verifica que se pueda abrir el panel de configuración y que Cloud agents figure como listo.
2. **Cuota multidispositivo**: en el cliente de escritorio, anota el porcentaje de uso semanal en **Settings > Usage & Billing** y luego abre la app móvil para cotejarlo; los valores en ambos lados deben coincidir con exactitud.
3. **Protección de gastos**: accede en el navegador a la página Spending en [cursor.com/dashboard](https://cursor.com/dashboard), confirma que se haya indicado un límite máximo en dólares en **Monthly Limit** y que el canal bajo demanda en el cliente esté en estado Enable.
4. **Llamada real de prueba**: envía un prompt para que el Bot ejecute una tarea breve, **revisa los registros para confirmar que no haya contenido superfluo ni llamadas innecesarias a herramientas**; si el consumo apenas varía mínimamente, se considera superada la prueba.

## Lecturas complementarias

- Capítulo relacionado: [¿Cuál es la diferencia entre Grok y Grok Bot?](/part1/grok-vs-grok-bot)
- Capítulo relacionado: [Capítulo 10 Cuota y costes: cómo hacer que el uso semanal rinda toda la semana](/part1/10-usage)
- Capítulo relacionado: [Capítulo 25 Preguntas frecuentes y resolución de problemas](/part4/25-faq)
- Documentación oficial: [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans.md)
- Documentación oficial: [Vincular SuperGrok para Grok Bot](https://cursor.com/cn/help/grok-bot/supergrok.md)
- Documentación oficial: [Suscribirse en aplicaciones móviles](https://cursor.com/cn/help/grok-bot/mobile-purchase.md)
- Documentación oficial: [Modelos de Grok Bot](https://cursor.com/cn/help/grok-bot/models.md)
- Análisis práctico de la comunidad: [«Análisis de la suscripción unificada de X: ¿cómo eligen los nuevos usuarios y deberían cambiarse los antiguos suscriptores? Explicado con claridad»](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee)
- Recopilación práctica de la comunidad: [«Colección de tuits de 铁柱 ①: Apertura, planes y cuota»](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc)
- Verificación de medios: [Tras la adquisición de Cursor por parte de SpaceXAI de Musk, Grok ya admite pagos con UnionPay y Alipay de China (IT Home, 2026-10-31)](https://www.ithome.com/1/020/504.htm)
