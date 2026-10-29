# Capítulo 25 Preguntas frecuentes y resolución de problemas

Si encuentras errores o bloqueos, **nunca reinstales ni restablezcas a ciegas**, ya que esto borrará el entorno y los scripts temporales que acabas de configurar.

1. **Comprueba primero el estado del servicio**.
2. Luego investiga si se trata de un problema de la red local, autorización de complementos, entorno en la nube o límite semanal.


![Preguntas frecuentes y resolución de problemas](/info/25-faq.png)

## ¿Cómo solucionar problemas de inicio de sesión y vinculación de cuentas en Grok Bot? {#inicio-de-sesion-y-autenticacion}

**Los usuarios individuales vinculan la autorización a través de la página de configuración o un enlace dedicado; los puestos empresariales inician sesión directamente con Grok. Si se vincula por error, es necesario contactar al soporte humano; ante bucles de redirección, borra las cookies y autentícate en modo incógnito.**

### Límites de cuenta y suscripción
Grok Bot se ejecuta sobre Cursor y no tiene relación con el muro de pago móvil de Grok ni con los límites de cuota semanales (Weekly SuperGrok Limit).

La versión individual admite SuperGrok y las versiones Plus, Heavy, así como X Premium+; SuperGrok Lite y Grok Enterprise no se pueden vincular a cuentas individuales, y los puestos empresariales son asignados de forma centralizada por el administrador.

**El correo electrónico de la cuenta no se puede modificar tras el registro, y la vinculación con Cursor es permanente y de una sola vez**. Si se vincula la cuenta incorrecta, no se puede transferir por cuenta propia y se debe contactar con el soporte humano para solucionarlo.

### Pasos de vinculación e inicio de sesión
1. Vinculación individual: abre [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) o accede en el cliente a **Configuración** > **Uso y facturación**, y en **Administrar planes** haz clic en **Obtener acceso a través de Grok** (solo se muestra si puede mejorar tu nivel de uso actual).
2. Puestos empresariales: si dispones de un puesto Grok Business, no necesitas vincularlo manualmente en la página de planes; simplemente cierra sesión por completo y haz clic en **Sign in with Grok** en la página de inicio de sesión.
3. Confirmación del servicio: ante cualquier anomalía, visita primero [status.cursor.com](https://status.cursor.com) para verificar el estado en tiempo real de **Grok Bot**. Para conocer los requisitos operativos, consulta [Iniciar sesión en Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

   **En caso de interrupción del servicio, espera a la solución oficial; nunca reinstales la aplicación ni restablezcas el ordenador**.

### Resolución de problemas y verificación
Una versión desactualizada del cliente puede provocar discrepancias de protocolo; ante fallos repentinos de autenticación, se recomienda esperar de 30 a 60 minutos antes de volver a intentarlo. **El criterio de aceptación es que el correo de la cuenta, la pertenencia de la suscripción y el estado de inicio de sesión del cliente coincidan exactamente**.

| Síntoma del fallo | Procedimiento correcto | Acción estrictamente prohibida |
| :--- | :--- | :--- |
| Bucle de redirección a la página de inicio de sesión | Limpiar las cookies de `cursor.com` y `x.ai`, y autenticarse con el modo incógnito de la versión de escritorio | Desinstalar y reinstalar continuamente el cliente |
| No se encuentra el acceso de vinculación | Confirmar que el nivel de cuenta actual es inferior al plan a vincular y no ha alcanzado el límite | Registrar una nueva cuenta para realizar compras repetidas |
| Mensaje Model provider is overloaded | Copiar el Request ID del error y esperar 2 minutos antes de reenviar | Hacer clic inmediatamente en Reset para restablecer el ordenador |
| Mensaje de que se debe cambiar el correo electrónico | Registrar una nueva cuenta y migrar los activos | Intentar forzar el cambio de correo vinculado en Configuración |

Envía un prompt al Bot para confirmar el estado de inicio de sesión.
```text
请检查当前运行环境的网络连通性与 Cursor 身份验证状态，汇报当前登录的用户环境标识，但不要输出任何敏感 Token。
```

## ¿Cómo recuperar Grok Bot si no se puede conectar al ordenador en la nube? {#ordenador-en-la-nube-y-recuperacion-del-entorno}

**Ante una desconexión, espera dos minutos para reintentar o reinicia por completo la aplicación; si se congela, haz clic en Recover para guardar el estado y reconstruir, mientras que Reset, que sobrescribirá la instantánea y perderá los cambios no sincronizados, solo debe usarse como último recurso.**

![Ordenador en la nube y recuperación del entorno](/info/25-faq-s2.png)

Todos los Bots comparten el mismo ordenador en la nube. **El historial de conversaciones se almacena de forma independiente en la base de datos**, por lo que no se pierde aunque ocurra un bloqueo o vaciado.

Cuando aparezcan los mensajes Reconnecting, Couldn't Reach Grok Bot's Computer o Bot failed to respond:
1. Espera de 1 a 2 minutos y haz clic en Retry.
2. Sal por completo de la aplicación. En Mac presiona `Cmd+Q`, en Win/Linux sal desde la bandeja del sistema; no te limites a cerrar la ventana.
3. Ve a Configuración > Ordenador y haz clic en actualizar. No interrumpas el proceso mientras la copia de seguridad no haya finalizado o el Bot esté trabajando.
4. Si se queda bloqueado, haz clic en Recover.
5. **Reset es el último recurso**. La sobrescritura de instantáneas provocará la pérdida de modificaciones no sincronizadas. Para más información, consulta [Ordenador de Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery).

| Operación | Preservación del estado | Impacto en el entorno | Escenario |
|---|---|---|---|
| Retry | Se conserva tal cual | Sin impacto | Fluctuación de red |
| Update | Espera a que termine la copia de seguridad | Conserva todo el software; limpia paquetes autoinstalados en toda la máquina | Parches oficiales |
| Recover | Guarda el estado y reconstruye la máquina | Elimina aplicaciones y entornos autoinstalados | Bloqueo o corrupción |
| Reset | Sobrescribe con la instantánea | Pierde modificaciones no sincronizadas | Último recurso si no conecta |

Se considera solucionado cuando el **estado del ordenador cambia a verde mostrando conectado**, el terminal funciona con normalidad y la configuración está completa.

- Si encuentras un inicio de sesión SSO, haz clic en Take over en la tarjeta para verificar manualmente; una vez listo, haz clic en I'm done.
- Claves de seguridad y red: en Configuración > General > Security Key activa Use hardware security keys e inserta tu YubiKey; si aparece un CAPTCHA, marca "Enrutar tráfico a través de este ordenador" en Configuración > Ordenador.
- Ejecución local: en Configuración > Ordenador activa "Ejecutar en este ordenador" (confirma antes de ejecutar comandos). Para más detalles, consulta [Configuración de Grok Bot](https://cursor.com/cn/docs/grok-bot/settings).
- Alerta de disco: cuando aparezca el aviso Computer is low on disk space, haz clic en Go to Disk Saver; **requiere confirmación manual obligatoria antes de eliminar**.

```text
请检查当前云端计算机根目录与工作目录的磁盘占用情况，找出体积超过 200MB 的文件与缓存目录，列出清单供我确认，不要擅自执行任何删除命令。
```

## ¿Cómo solucionar problemas si las rutinas automatizadas de Grok Bot no se activan? {#gestion-de-rutinas-y-resolucion-de-problemas-de-automatizacion}

**Si una rutina no responde, confirma primero que su estado no esté en pausa, coteja la zona horaria y realiza una prueba con Test; los webhooks deben incluir la clave de autenticación y un código 200 solo indica que se ha encolado; las activaciones por Slack deben limitarse obligatoriamente a una lista blanca de canales y palabras clave de filtrado.**

![Gestión de rutinas y resolución de problemas de automatización](/info/25-faq-s3.png)

Las rutinas se ejecutan automáticamente en la nube y siguen funcionando incluso con el equipo apagado; admiten programación temporizada, Webhook y notificaciones push de Slack.

1. **Comprobar estado y zona horaria**: en Details confirma que no esté en **Paused** (en el móvil verifica que esté en **Active**); selecciona manualmente la zona horaria en "Configuración > Bot > Timezone", y evita usar Auto-detect si operas entre diferentes países.
2. **Momento de activación programada**: solo espera al siguiente ciclo (si a las 09:05 se configuran las 09:00, se ejecutará a la mañana siguiente); para probar la lógica de inmediato, haz clic en **Test**.
3. **Verificar Webhook**: la solicitud POST debe incluir `Authorization: Bearer <key>`. **Un código 200 solo indica que se ha encolado**, revisa la ventana de chat para ver los resultados; si no es 200, se debe a una clave incorrecta o a que la rutina está en pausa.
4. **Restringir la activación de Slack**: **es obligatorio limitar los canales y las palabras clave de filtrado** para evitar que las conversaciones casuales agoten la cuota en pocas horas. Consulta más detalles en [Rutinas](https://cursor.com/cn/help/grok-bot/routines).

En el móvil, revisa el "Historial de ejecuciones" para ver **Running**, **Succeeded** o **Failed**; si muestra **No runs yet**, significa que no se ha activado.

| Fallo | Causa | Solución |
|---|---|---|
| Sin respuesta | Paused / Fuera de hora / Desviación de zona horaria | Verificar Active, hacer clic en Test, cotejar Timezone |
| 401/403 | Falta de Token / Clave restablecida / Rutina eliminada | Copiar de nuevo el header y sobrescribir la configuración |
| Slack sin respuesta | Mensaje antiguo / Canal o palabra clave no coincidente | Solo procesa mensajes nuevos; cotejar la lista blanca de canales y frases |
| Consumo rápido de cuota | Intervalo demasiado corto / Canal grande sin palabras de filtrado | Pausar la rutina, ampliar el intervalo, limitar a canales de operaciones |

Prompt para crear y corregir rutinas automatizadas:
```text
请修改名为“工单同步”的例程：仅在 #ops-alert 频道出现包含“[P0-Error]”文字的新消息时才触发，忽略其他日常聊天，并列出更新后的 When to run 描述。
```

## Anomalías de uso y control de cuotas

![Anomalías de uso y control de cuotas](/info/25-faq-s4.png)

La cuota de Grok Bot se restablece semanalmente. Si se agota la cuota básica, se interrumpirán las respuestas, **lo cual es un mecanismo normal de corte por cuota**. Una vez agotada la cuota de prueba de un solo uso en tareas complejas, no se puede recuperar.

### Operaciones y precauciones
1. Recuperar cuota: espera a la renovación semanal, activa el uso bajo demanda en **Configuración** > **Uso y facturación**, o bien actualiza tu suscripción.
2. Establecer un límite máximo: define un límite en el cliente o en la web [cursor.com/dashboard](https://cursor.com/dashboard). **Las tareas en ejecución no se cortan abruptamente, por lo que un ligero exceso de facturación de unos pocos puntos porcentuales es normal.**
3. Alineación de cuotas: las cuentas externas no se acumulan y se toma la de mayor nivel (Pro corresponde a SuperGrok/X Premium+, Pro+ corresponde a SuperGrok Plus, Ultra corresponde a SuperGrok Heavy).
4. Cancelación en dispositivos móviles: la suscripción se comparte entre múltiples plataformas. Los pagos realizados en tiendas de aplicaciones deben cancelarse en Apple ID o Google Play, ya que el soporte oficial no reembolsa directamente; consulta [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans).

### Criterios de aceptación
| Escenario | Operación | Límites y advertencias |
| :--- | :--- | :--- |
| Prevenir sobrecostos | Establecer un límite mensual en el cliente o la consola | **El tope rechaza nuevas solicitudes; las tareas en ejecución se completan antes de detenerse** |
| Consultar uso | Consultar el remanente en tiempo real en la configuración interna del Bot | No se comunica con el panel de control externo de Grok |
| Cuota de prueba a cero | Revisar escaneos o refactorizaciones de proyectos grandes | Agotamiento de un solo uso sin recuperación |

```text
请列出你当前账号下所有处于活跃状态的例程，评估它们各自的执行频率与触发条件，指出哪一个例程最容易引发高额用量消耗。
```

## Chats grupales, colaboración y gobernanza de Bots asistentes

Los Bots asistentes aparecerán en la barra lateral y enviarán notificaciones; modificar archivos o conectarse a redes externas activará la aprobación de **Auto-review**.

### Operaciones y aprobaciones
1. Reducir ruido y ocultar: en el escritorio haz clic derecho y selecciona Hide from sidebar o envía un comando para desactivar las notificaciones; en el móvil, ve a la configuración para desactivarlas.
2. Restaurar elementos ocultados por error: en el escritorio, dentro de **Bots ocultos**, selecciona Show in sidebar; en el móvil, selecciona Unhide. **Está estrictamente prohibido hacer clic en Recover o Reset en la nube para buscar un Bot.**
3. Aprobación y lista blanca: para operaciones de alta frecuencia, haz clic en **Permitir siempre** (se guardará en Configuración > Bot > Reglas personalizadas); ante conflictos se preguntará primero, y las que muestren "Requerido obligatoriamente por el administrador" no se pueden omitir.

   Consulta las pautas en la [Guía de uso de Grok Bot](https://cursor.com/cn/help/grok-bot/how-to).

### Criterios de aceptación
Barra lateral sin Bots innecesarios y operaciones cotidianas de alta frecuencia **aprobadas automáticamente sin interrupciones**.

| Escenario | Tiempo de espera | Comportamiento | Medida |
|---|---|---|---|
| Manual en primer plano | Espera indefinida | Suspendido continuamente | Verificar y permitir o rechazar |
| En segundo plano / Webhook | Aprox. 10 minutos | Pasa a Expired y se cancela | Configurar "Permitir siempre" o activar notificaciones |
| Obligatorio por el administrador | Según el caso | No se puede omitir | Autorización manual obligatoria |

```text
请梳理我们在此会话中频繁执行的文件读取与构建指令，为它们生成一组最小权限的安全规则建议，以便我添加到 Auto-review 的自定义白名单中。
```

## Complementos y conexión con aplicaciones externas

### Resolución de problemas de autorización
**Added solo indica que está instalado, no significa que se haya iniciado sesión**. Si no aparece la tarjeta, dirígete a la barra lateral para verificar manualmente. **La autorización debe completarse en un plazo de 10 minutos**; si expira, haz clic en Reopen; si los errores persisten, haz clic en Remove para eliminar y reinstalar.

| Estado | Tratamiento |
| :-- | :-- |
| **Added / Needs auth** | Haz clic en "Verificar identidad" para iniciar sesión en el navegador |
| **Error en Connected** | Envía un comando con el nombre del complemento para actualizar la sesión |
| **Disabled by team admin** | Contacta al administrador del equipo para habilitarlo |

### Múltiples cuentas y verificación
1. **Múltiples cuentas**: en "Conectar aplicaciones" > Complementos > Accounts haz clic en **Add Another Account** (en el móvil pulsa en Authorize new account) y asigna una etiqueta. Especifica la etiqueta en la conversación para invocarla; si no hay botón, solo admite una cuenta.
2. **Verificación**: **el estado muestra Connected en verde con una etiqueta clara**, y al enviar un comando se invoca con precisión a la primera.

Para más detalles, consulta [Conectar aplicaciones](https://cursor.com/cn/help/grok-bot/connect-apps.md).

```text
请刷新当前已连接的插件列表，使用带有“工作”标签的账户连接，读取最近更新的 3 个页面，确认授权是否正常。
```

## Cancelación de cuenta y limpieza de datos

Grok Bot comparte la cuenta con Cursor; **la eliminación de la cuenta es irreversible** y no es posible conservar Cursor por separado. Para cambiar de ordenador, simplemente cierra sesión o desinstala la aplicación.

### Pasos para la cancelación de cuenta
Antes de cancelar la cuenta, asegúrate de desactivar la renovación automática para evitar disputas de facturación.
1. En móviles (iOS/Android): toca el avatar para entrar en "Configuración" > Información de la cuenta > "Eliminar cuenta", e introduce la palabra "**eliminar**" en la verificación web para confirmar.
2. En escritorio y web: **no se puede cancelar directamente desde el cliente**. Inicia sesión en [cursor.com/dashboard](https://cursor.com/dashboard) > "Configuración" > "Más" > "Eliminar cuenta" para confirmar.
3. Puestos de empresa o equipo: los usuarios individuales no pueden cancelar de forma independiente; deben contactar al administrador para desvincular o enviar un ticket de soporte. Consulta los términos en [Eliminar tu cuenta de Grok Bot](https://cursor.com/cn/help/grok-bot/delete-account).

### Limpieza de activos y precauciones
| Activos y suscripciones | Resultado del tratamiento | Acción obligatoria |
| :--- | :--- | :--- |
| Conversaciones y entornos en la nube | Borrado físico en un plazo de **30 días**, destrucción de instantáneas | Exportar previamente código y conversaciones, descargar archivos |
| Archivos locales | Intactos | No requiere ninguna acción |
| Suscripciones independientes de tiendas y X | **No se cancelarán automáticamente** | Es necesario cancelar la suscripción manualmente en Apple, Google o x.ai |

## Obtención de soporte oficial y directrices para tickets

### Cómo proceder
Si la resolución local no funciona, envía un correo a **hi@cursor.com**. **Evita enviar descripciones vagas como "mi Bot no funciona"** e incluye estos seis elementos en el correo:

1. Credenciales de la cuenta: correo electrónico de registro.
2. Entorno de ejecución: plataforma y número de versión del cliente. Desde el menú de cuenta > Soporte > Acerca de, haz clic en Copy version info para copiarlo.
3. Operación que se iba a ejecutar: explica qué tarea querías realizar antes del fallo.
4. Evidencia real del error: ventana emergente de error completa, errores de consola o capturas de pantalla de facturación.
5. Registro de resolución: detalla qué comprobaciones has realizado para evitar que el soporte dé sugerencias repetidas.
6. Request ID: haz clic derecho en el mensaje de error o pasa el cursor sobre More message actions y selecciona Copy request ID. Si no aparece, es obligatorio adjuntar el texto original del error y una captura de pantalla completa.

En Linux, si aparece Update required y la actualización automática falla, ejecuta el comando de actualización en la terminal según tu distribución:
- Debian / Ubuntu: `sudo apt update && sudo apt install --only-upgrade grok-bot`
- Fedora / Familia RPM: `sudo dnf upgrade --refresh grok-bot`

::: details Cómo proceder
```text
收件人：hi@cursor.com
主题：【Grok Bot 故障申报】云端电脑持续重连且 Recover 失败 - [你的账号邮箱]

支持团队：
我的账号遇到了云端电脑无法连通的故障，无法正常执行任务，以下是详细环境与排查信息：

1. 账号邮箱：developer@example.com
2. 版本信息：Version 1.2.4 (Channel: stable, OS: Darwin x64 23.4.0)
3. 故障发生场景：我尝试让 Bot 运行自动化部署脚本，终端在拉取镜像时中断。
4. 核心报错信息：界面持续提示“Couldn't Reach Grok Bot's Computer”，伴随“Bot failed to respond”。
5. 已尝试的排错操作：
   - 已彻底 Quit 应用并重启；
   - 尝试在“设置 > 计算机”执行 Update，提示备份未就绪；
   - 尝试点击 Recover，重试一次后依然在进度条处卡住报错；
   - 查看 status.cursor.com 确认官方各项服务状态正常。
6. 请求 ID (Request ID)：req_98af7c32e01b44d7a1
7. 附件：包含当前报错卡片截图及“设置 > 计算机”面板状态截图。

请协助在后台检查该实例的宿主节点状态，谢谢。
```
:::

### Qué define un buen resultado
**Tras enviar el correo, se recibe un acuse de recibo automático y el equipo técnico puede consultar los registros sin necesidad de repreguntar**. Para normas detalladas, consulta [Obtener ayuda](https://cursor.com/cn/help/grok-bot/get-help.md).

## Casos típicos de resolución de problemas

### Caso 1: Bucle de Reconnecting en el ordenador en la nube
Cuando se muestre Couldn't Reach Grok Bot's Computer, **nunca hagas clic primero en el destructivo Reset**.
1. Visita [status.cursor.com](https://status.cursor.com) para confirmar que el servicio funcione con normalidad y presiona `Cmd+Q` para reiniciar la aplicación.
2. Ve a Configuración > Ordenador; si se indica que no se pausó a tiempo, espera unos 5 minutos para que expire el tiempo de espera en segundo plano.
3. Cuando se habilite la opción de Recover del ordenador, haz clic en recuperar y vuelve a ejecutar los scripts de instalación, **preservando los scripts históricos y el estado de inicio de sesión**.

### Caso 2: Avalancha de consumo de cuota por activador de Slack
Al escuchar todas las conversaciones casuales de más de 3000 personas en `#general`, la cuota semanal se redujo a cero en 24 horas.
1. **Primero fija un límite mensual bajo demanda en el panel de gastos** para evitar cargos en la tarjeta de crédito.
2. Cambia la rutina a Paused para detener el consumo.
3. Restringe la regla a "activar solo en `#bot-help` y cuando se mencione a `@Grok`".
4. Haz clic en Test para realizar una validación única antes de volver a ponerlo en línea.

### Caso 3: Fallo de autenticación en Notion y toma de control del inicio de sesión
Cuando Notion muestre Action needed y sea bloqueado por Okta SSO, **se debe usar Take over obligatoriamente para completar la autenticación en el navegador integrado**.
1. Tras ver el aviso Needs auth, haz clic en Take over en la tarjeta para tomar el control.
2. Introduce tu número de empleado en el navegador integrado en la nube para superar la autenticación en dos pasos y haz clic en I'm done.
3. En Accounts, haz clic en Add Another Account para autorizar tu espacio personal, **asignándole la etiqueta "Biblioteca personal" para evitar conflictos de credenciales**.

## Errores comunes que debes evitar

1. Si se pierden las conversaciones, no hagas clic en Reset, ya que borrará el código. Para recuperarlas, primero **cierra y reinicia**, coteja la cuenta de Cursor o revisa los bots ocultos.
2. Si configuras a las 14:05 una rutina para las 14:00, se ejecutará al día siguiente; para probar la lógica, haz clic en **Test**.
3. Escuchar grupos grandes de Slack sin palabras clave de activación hará que los simples saludos **quemen la cuota de toda la semana**.
4. Eliminar la app seguirá generando cargos; para cancelar la suscripción, dirígete al centro de suscripciones de **Apple ID o Google Play**.
5. Hacer clic en Reset mientras está en Updating **dañará el sistema de archivos**, y solo podrá resolverse mediante soporte humano.
6. Cuando un complemento muestre Added, debes confirmar que pase a **Connected**; si muestra Needs auth, requiere autorización en el navegador.
7. Actualizar, Recover o Reset vaciarán `node_modules` y `.venv`; incluye las dependencias en el **script de inicialización**.
8. Las tarjetas de aprobación **expirarán y se cancelarán tras 10 minutos (Expired)**; recuerda activar las notificaciones o configurar "Permitir siempre".

## Cómo verificar una vez terminado

- Comprueba [status.cursor.com](https://status.cursor.com) para verificar que no haya incidencias y que el correo sea el correcto.
- Accede a Configuración > Ordenador para ver el indicador en verde y envía comandos básicos de Linux al Bot para probar la respuesta.
- Mantén las rutinas activas, coteja la zona horaria en When to run y haz clic en Test para comprobar su funcionamiento.
- Entra en Configuración > Uso y facturación; **es obligatorio definir un límite mensual para el uso bajo demanda** a fin de evitar facturas desorbitadas.
- Las aplicaciones conectadas deben mostrar Connected, las operaciones de escritura deben activar la ventana de Auto-review y enviar una notificación push al móvil.
- En los tickets incluye únicamente el Request ID y Copy version info; **nunca reveles el encabezado de solicitud con el Bearer Token**.

## Lecturas complementarias

- Capítulo relacionado: [Capítulo 5 Ordenador en la nube compartido: archivos, navegador y toma de control](/part1/05-computer)
- Capítulo relacionado: [Capítulo 10 Cuotas y costes: cómo hacer que el uso semanal dure toda la semana](/part1/10-usage)
- [Preguntas frecuentes oficiales sobre Grok Bot](https://cursor.com/cn/help/grok-bot/faqs)
- [Guía de uso y resolución de problemas de Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)
- [Gestión del entorno del ordenador y recuperación ante desastres de Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery)
- [Configuración detallada de rutinas automatizadas y activadores](https://cursor.com/cn/help/grok-bot/routines)
- [Sistema de cuentas e instrucciones de cancelación](https://cursor.com/cn/help/grok-bot/delete-account)
- [Contacto con el equipo de soporte y directrices para tickets](https://cursor.com/cn/help/grok-bot/get-help)
- [Referencia de configuración global del sistema Grok Bot](https://cursor.com/cn/docs/grok-bot/settings)
