# Capítulo 5 Computadora en la nube compartida: archivos, navegador y toma de control

Los usuarios que recién comienzan con Grok Bot suelen tener algunos malentendidos comunes. Estos errores a menudo provocan obstáculos en el desarrollo y mantenimiento posteriores:

- Creer erróneamente que crear un nuevo Bot añadirá una máquina virtual independiente.
- Creer erróneamente que cuando varios Bot trabajan juntos, pueden leer directamente el historial de chat de los demás.
- Pegar directamente nombres de usuario, contraseñas o incluso API Tokens en la ventana de chat cuando se requiere iniciar sesión en herramientas de terceros.

Cuando la computadora en la nube se vacía repentinamente debido al mantenimiento del sistema o a actualizaciones subyacentes, los entornos y scripts instalados desaparecen por completo. Es en ese momento cuando todos descubren que no saben nada sobre el mecanismo subyacente de esta computadora en la nube.

Todos los Bot bajo la misma cuenta trabajan en la misma computadora en la nube, compartiendo el mismo disco y sistema de archivos. No pueden ver los registros de conversación de los demás; la colaboración depende enteramente del flujo de archivos en el disco.

Al encontrarse con una verificación de inicio de sesión, lo correcto es tomar el control de la pantalla directamente en el navegador en la nube para introducir las credenciales, en lugar de entregar la contraseña al modelo. Al mismo tiempo, esta computadora en la nube es en esencia un contenedor temporal que puede reconstruirse en cualquier momento; cuando la plataforma realiza actualizaciones subyacentes o los administradores ejecutan tareas de mantenimiento, los paquetes de software instalados manualmente se perderán.

Este capítulo te llevará a desglosar el funcionamiento real de esta computadora en la nube. Aprenderás a transferir archivos y pantallas de manera segura entre múltiples Bot, cómo enrutar el tráfico de red a través del escritorio local para hacer frente a restricciones de listas blancas y cómo utilizar un pipeline de respaldo ligero y estandarizado para que todo el entorno pueda recuperarse de forma rápida y ordenada tras un restablecimiento.


![Computadora en la nube compartida: archivos, navegador y toma de control](/info/05-computer.png)

## Mecanismo subyacente de la computadora compartida: una máquina y múltiples Bot

**Todos los Bot bajo tu cuenta comparten la misma computadora Linux administrada.** Sin importar a qué Bot cambies, tendrás delante el mismo directorio raíz `/workspace` y el mismo disco persistente.

El historial de chat se guarda de forma independiente en el exterior; incluso si ejecutas `rm -rf` dentro de la máquina para vaciarlo o si el sistema se bloquea y reinicia, las conversaciones y las listas siguen allí.

**Crear un nuevo Bot no equivale a un aislamiento de seguridad.** Cualquier Bot, con solo obtener permisos de línea de comandos, puede leer y escribir todos los datos en `/workspace`; jamás pongas información sensible sin cifrar allí dentro.

Evolución de versiones:
- v0.68.0: permite eliminar otras computadoras en la configuración
- v0.68.1 (publicado el 2026-10-07): la resolución de pantalla subió de 1280×800 a 1920×1200, con respuesta más rápida en operaciones y capturas de pantalla
- v0.70.2: se añade correo electrónico exclusivo y soporte para guardar páginas web directamente como PDF

Para detalles subyacentes, consulta [《4.6 Máquinas virtuales, memoria y respaldos》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

## Monitoreo de pantallas y estado de trabajo de múltiples Bot

### Estados y configuración

**La barra lateral muestra permanentemente tres tipos de estados**:
- Requiere atención: esperando respuesta, aprobación o traspaso.
- Actividad no leída: tarea completada, esperando revisión de resultados.
- Estado de trabajo: ejecutando scripts, extrayendo páginas web o invocando herramientas.

Haz clic en el nombre superior para acceder a "Ver detalles de la conversación", donde puedes cambiar el nombre, las etiquetas y el avatar del Bot actual. Los Bot personales no tienen un cuadro de descripción independiente; **basta con enviar un mensaje directamente** para ajustar su enfoque.

### Monitoreo y notificaciones

Las operaciones en la nube admiten **ver la pantalla en tiempo real**.

**Las notificaciones se suprimen automáticamente cuando está en foco**, marcándose como no leídas únicamente en la barra lateral y en el Dock; cuando estés sin conexión, puedes habilitar las notificaciones en el archivo de configuración para enviarlas al escritorio o al móvil.

## Toma de control del navegador: ceder la pantalla, no la contraseña

![Toma de control del navegador: ceder la pantalla, no la contraseña](/info/05-computer-s3.png)

No envíes credenciales a la ventana de chat. Tú y el Bot comparten el navegador: **cede la pantalla, no la contraseña**.

### Pasos para tomar el control

1. Activar la pausa: el Bot abre la página de inicio de sesión y se pausa ante credenciales, escaneo de código o 2FA.
2. Tomar el control de la entrada: haz clic en pantalla completa para tomar el control del teclado y el ratón.
3. Inicio de sesión manual: ingresa las credenciales tú mismo o escanea el código para verificar.
4. Ceder la ejecución: **tras iniciar sesión, notifica al Bot para que reutilice las cookies y continúe**, sin tocar contraseñas en texto claro.

### Filtros de aprobación

Presiona `Cmd+,` para configurar en "General" - "Bot".

- **En caso de conflicto de reglas, prevalece "Preguntar primero" (Ask first)**.
- Las reglas corporativas muestran `Required by your admin. You can't edit or delete this rule.` y no se pueden modificar.
- v0.70.2 reforzó las confirmaciones previas al envío de correos y publicaciones, pagos y cambios en entornos de producción.

Para más detalles, consulta [Configuración y notificaciones](https://cursor.com/cn/docs/grok-bot/settings).

## Convenciones de traspaso de archivos y planificación de directorios para múltiples Bot

### Modo de colaboración por archivos

Los Bot no pueden leer el historial de chat entre sí; **el único canal de colaboración entre múltiples Bot son los archivos del disco compartido**.

El prompt solo necesita recibir la ruta del archivo del paso anterior; consulta para más detalles [《4.6 Máquinas virtuales, memoria y respaldos》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

1. El recolector extrae y genera `tweets.md`
2. El analista sintetiza y genera `profile.md`
3. El diseñador crea `design.md` a partir del perfil
4. El ingeniero lee el diseño y construye el código

### Planificación de directorios

Establece los directorios desde la creación de la máquina para evitar que múltiples Bot desordenen los archivos al escribir.

| Ruta del directorio | Contenido almacenado | Convención de escritura |
| --- | --- | --- |
| `/workspace/handoff/` | Productos intermedios | Markdown o JSON unificado, con prefijo de tarea |
| `/workspace/projects/` | Código y recursos del proyecto | Subdirectorios independientes por proyecto, vinculados a repositorios Git |
| `/workspace/tools/` | Scripts locales de autoría propia | Conservar solo código fuente sin claves; sincronizar con el repositorio de respaldo tras la revisión |
| `~/.env` o archivos locales | Claves API | Guardar únicamente en local; **queda estrictamente prohibido confirmarlas en el repositorio de código o imprimirlas en la sesión** |

### Limpieza de disco y Disk Saver

Si el sistema emite una advertencia de `Computer is low on disk space` o `Computer is critically low on disk space`, ve a la barra lateral y haz clic en "Go to Disk Saver" de **Disk Saver** para ver las sugerencias de limpieza.

**Nunca eliminará archivos por su cuenta sin confirmación previa**; si rechazas la limpieza, los archivos existentes se conservarán tal como están.

## Salida de red local: enrutamiento y acceso a redes privadas

![Salida de red local: enrutamiento y acceso a redes privadas](/info/05-computer-s5.png)

Para resolver listas blancas de IP de cuentas oficiales de WeChat o intranets empresariales, o bien el acceso a redes locales, **basta con retransmitir el tráfico a través del dispositivo local**.

### Pasos para habilitarlo
1. Presiona `Cmd+,` para acceder a la configuración y haz clic en **Computadoras**.
2. En **Tus computadoras**, busca la computadora actual y activa **Enrutar el tráfico a través de la computadora actual**.

### Limitaciones y errores comunes a evitar
- Limitado a una sola máquina por vez. Externamente se identifica como la IP local y el Bot también puede acceder directamente a la red local.
- **Solo surte efecto para nuevas solicitudes**; las conexiones TCP persistentes existentes continuarán por la ruta original.
- Si el administrador desactiva `Allow Local Egress Routing`, el interruptor se mostrará deshabilitado con el mensaje `Disabled by your admin. You can't turn this on.`, desconectándose obligatoriamente en un plazo de 5 minutos; consulta [Configuración y notificaciones](https://cursor.com/cn/docs/grok-bot/settings).
- `Execution on this computer` controla la Shell local; por defecto requiere confirmación paso a paso, **nunca lo dejes en modo totalmente automático a la ligera**.

## Reconstrucción, actualización y terminación: el ciclo de vida de la computadora en la nube

![Reconstrucción, actualización y terminación: el ciclo de vida de la computadora en la nube](/info/05-computer-s6.png)

La reconstrucción **vacía el entorno instalado manualmente**, pero conserva el disco y los estados de inicio de sesión.

Consulta [Computadoras Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery) y [Administrar computadoras Grok Bot](https://cursor.com/cn/docs/grok-bot/computers).

| Operación | Se conserva | Eliminaciones y advertencias |
| - | - | - |
| Actualización de software | Todo | Ninguno |
| Actualizar/Reconstruir | Disco y archivos | Limpia el entorno instalado manualmente; requiere volver a ejecutar scripts |
| Terminar VMs | Disco | Se apaga tras 30 días de inactividad, perdiendo el progreso |
| Recover/Reset | Datos guardados | Interrumpe tareas y pierde código no guardado |

Cuando aparezca `Reconnecting`, **no pulses Reset a ciegas**; revisa en este orden:

1. **Haz clic en Retry**. Durante la reconexión el disco permanece intacto; hacer clics al azar arruina el estado actual.
2. **Salir por completo**. En macOS debes usar `Cmd+Q` para salir antes de reiniciar; no te limites a hacer clic en la cruz roja.
3. **Buscar actualizaciones**. Ve a "Configuración" > "Computadoras" y actualiza cuando el Bot esté inactivo.
4. **Priorizar Recover**. Si aparece la opción emergente, elígela primero para intentar guardar una instantánea.
5. **Reset como último recurso**. Restablece únicamente tras confirmar que no hay código sin guardar y que todo lo demás ha fallado.

## Pipeline de recuperación ante desastres: registro general de servicios y scripts de restauración idempotentes

![Pipeline de recuperación ante desastres: registro general de servicios y scripts de restauración idempotentes](/info/05-computer-s7.png)

Las actualizaciones o restablecimientos vacían el entorno. 铁柱AGI (@cgnot996) propuso una solución el 2026-10-10: **respaldar únicamente el método de inicialización, sin guardar la máquina completa**.

Utiliza un repositorio privado de 5.1 MB para gestionar 20 servicios de 10 Bot (18 elementos de recuperación obligatoria, incluidos 4 permanentes, 14 bajo demanda y 2 rutas de claves); consulta el [tutorial](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye) para más detalles.

### Estructura estandarizada y registro

El repositorio `vm-services` contiene cuatro partes:
- `REGISTRY.md` y `registry.json`: registro general y configuración.
- `restore/restore-<服务名>.sh`: script para un único servicio, **debe ser idempotente**.
- `restore/restore-all.sh`: instala bibliotecas y CLI en orden, inicia servicios en segundo plano y registra los fallos.
- `service-src/`: archivo de código fuente, excluyendo `.env`, registros y entornos virtuales.

El registro de nuevos servicios incluye estos elementos: ID corto y Bot responsable; rutas de código y datos; método de instalación (apt/pip/npm/Docker) y dependencias del sistema; comandos de inicio y verificación (--version o puerto); si la recuperación es obligatoria; ruta absoluta de claves (**queda estrictamente prohibido registrar texto claro**); pasos como escaneo de código QR o OAuth.

### Dos conjuntos de prompts

Envíalo al Bot "Administrador de servicios de máquinas virtuales"; el despliegue de los demás Bot se reportará según esto.

::: details Prompt de despliegue y registro
```text
你是「虚拟机服务管家」，只管一件事：记下这台虚拟机上部署过的所有第三方服务，并在电脑更新或换账号之后，按记录把它们原样恢复。

你维护的东西：
1. 一份登记总账，人和机器各读一份：REGISTRY.md（表格）和 registry.json（给脚本读）。
2. 每个服务一个恢复脚本 restore/restore-<服务>.sh，必须幂等，重复跑也不会出错。
3. 一个总入口 restore/restore-all.sh，按依赖顺序调用各个恢复脚本，最后汇总哪些失败了。
4. 一份源码备份 service-src/：各 Bot 自己写的服务代码和脚本，同步时排除密钥、日志、运行状态、虚拟环境和个人数据，并先扫一遍明文密钥，命中就停。
5. 以上全部跟着一个私有 Git 仓库存（「你的备份仓库地址」）。总账、恢复脚本、源码都在仓库里，密钥永远不进仓库。

登记规则（其他 Bot 部署任何服务都必须来找你登记）：
每项必须包含：
- 名称和短 id、用途、负责的 Bot
- 路径：代码、配置、数据分别在哪
- 安装方式和依赖（apt / pip / npm / Docker / 系统定时任务）
- 启停命令、健康检查命令
- 更新后的恢复步骤，或者对应的恢复脚本
- 是否必恢复：是 / 否
- 密钥：只写存放路径，绝不写明文
- 需要真人完成的步骤（OAuth 登录、扫码、导入 cookie）单独标出来

你的工作方式：
- 先弄清哪些会丢、哪些能留：电脑更新一般保留工作目录，但系统包、常驻进程、全局安装的命令行工具会丢；重置则什么都不留。所以要记的是“怎么重建”，不是去拷整台机器。
- 能从公开渠道重装的（apt、pip、npm、上游 Git 仓库）只记安装命令；自己写的代码必须进源码备份，否则重置后就找不回来。
- 收到登记先核对：路径是否真实存在、健康检查能不能过。登记写的和实际不一样时，以实际为准，并告诉负责的 Bot。
- 多个定时任务合并成一份 crontab 真源时，检查每一条是不是都在真源里，不在的要靠恢复脚本补回去。
- 故意停掉的服务要写清楚“为什么停、什么条件下重开”，免得被当成漏装。
- 只有主人说“电脑更新完了”才跑总恢复，不盲跑。跑完交验收：每项是成功、失败，还是要真人处理。
- 每次有服务新增、删除或源码大改，先重新同步源码备份，再把总账、脚本、源码一起提交推送到备份仓库。换账号或重置时，就靠这份备份把整套设定带走。
- 删掉的服务要彻底清除：总账只反映现在真实的状态。
```
:::

Tras el restablecimiento, configura las credenciales de Git y envíalo al Bot de recuperación. **Los criterios de aceptación consisten en informar los resultados, el tiempo empleado y el estado de verificación según la lista**.

::: details Prompt de recuperación en un clic tras el restablecimiento
```text
这台电脑刚重置过（或者是换了新账号），之前部署的服务都没了。请按我的备份把它们恢复到可用状态，规则如下。

备份在哪：
- 备份仓库：<你的备份仓库地址>，分支 <分支名>
- 仓库里有：登记总账（REGISTRY.md 和 registry.json）、每个服务的恢复脚本（restore/）、自写服务的源码备份（service-src/）
- 仓库里没有密钥，这是故意的

请按这个顺序做：
1. 把备份仓库拉到工作目录，先读总账，告诉我一共登记了几项、哪些标了「必恢复」、哪些只留密钥不用恢复。先列出来，不要动手。
2. 把自写服务的源码从 service-src/ 放回总账写的原位置。只补缺失的，已经存在的目录不要覆盖。
3. 按总账的依赖顺序逐项恢复：先装系统依赖（比如 cron、ffmpeg），再装命令行工具，最后拉起常驻服务和定时任务。每项都用它自己的恢复脚本，脚本要能重复跑。
4. 每装完一项就跑它登记的健康检查。失败了先看日志、试着修一次；修不好就记下原因，接着做下一项，不要卡住。
5. 把需要我本人做的事汇总成一张清单：要重新提供的密钥（只说放哪个路径、叫什么名字，别让我把密钥贴进聊天）、要重新登录授权的工具（OAuth、扫码、设备码）。然后一项一项带我做，每做完一项马上复查。
6. 故意暂停的任务保持暂停，总账里写了原因和重开条件的照办。别因为“看起来漏装了”就自作主张打开。
7. 最后交验收清单，每项一行：服务名、结果（成功 / 失败 / 等我处理）、健康检查输出摘要、花了多久。再告诉我总共用了多少时间、成功了几项。

不要做的事：
- 不要把任何密钥写进仓库、日志或聊天
- 不要跑总账没登记的安装
- 不要用“重置电脑”当修复手段
- 恢复完如果有任何改动（路径变了、版本升级了），更新总账，提交推回备份仓库
```
:::

## Errores comunes a evitar

### Credenciales y permisos
- **No pegues claves en la ventana de chat**: ingrésalas manualmente en la interfaz web; escribe los Token de la CLI en `~/.env`, y los scripts leerán las variables de entorno.
- **Sin aislamiento entre Bot**: comparten `/workspace` y permisos. Los recursos confidenciales dependen de repositorios privados y aprobación humana; abrir múltiples Bot no sirve de nada.

### Colaboración y dependencias
- **Los traspasos deben guardarse en disco**: los Bot no leen las conversaciones entre sí. Guarda los resultados de A como Markdown o JSON; depender solo de palabras hará que B sufra alucinaciones.
- **Las dependencias no son persistentes**: una actualización, Recover o Reset vaciará el contenido de `apt install` y `npm install -g`, y tampoco se respaldan `node_modules` ni `.venv`.

  **El script de restauración debe incluir** `npm install` y `pip install -r requirements.txt`.

### Operaciones y red
- **Al ver Reconnecting no pulses Reset**: perderás los cambios no guardados en disco y forzarás una reconstrucción; **prueba a reintentar o reiniciar el cliente primero**.
- **Gestión centralizada de tareas programadas**: crontab debe mantenerse de forma unificada en un repositorio Git.
- **Es necesario reiniciar tras activar el enrutamiento local**: si tras activar "Enrutar el tráfico a través de la computadora actual" la IP no cambia, reinicia dicho proceso.

## Cómo verificar tras completar la configuración

1. El Bot A escribe una marca de tiempo en `/workspace/handoff/test.json`. Si el **Bot B lo lee y lo comunica con precisión**, el flujo funciona correctamente.
2. En "Configuración" > "Computadoras", activa "Enrutar el tráfico a través de la computadora actual" y ejecuta `curl -s https://api.ipify.org` en la terminal. **La IP pública debe coincidir con la local**, no con la IP del centro de datos.
3. Haz que el Bot abra la página de inicio de sesión de GitHub; **debe pausarse antes del campo de contraseña y solicitar la cesión de control**. Continúa tras iniciar sesión manualmente y confirma que no haya contraseñas en texto claro en los registros.
4. Confirma que el repositorio Git privado ya tiene confirmados `REGISTRY.md`, `registry.json` y los scripts. Clónalo en un directorio de prueba y ejecuta:
```bash
bash restore/restore-all.sh
```
**Todas las comprobaciones de estado deben superarse**, sin errores de conflicto y con los servicios del registro general escuchando normalmente.

## Lecturas complementarias

### Documentación oficial y base de conocimiento

- [Administrar computadoras Grok Bot](https://cursor.com/cn/docs/grok-bot/computers): reglas oficiales completas sobre reconstrucción por lotes, terminación y limpieza por 30 días de inactividad de múltiples computadoras en la versión Enterprise.
- [Configuración y notificaciones](https://cursor.com/cn/docs/grok-bot/settings): instrucciones oficiales sobre la configuración del cliente de escritorio, ejecución de comandos locales, enrutamiento por retransmisión de tráfico y el modo Auto-review.
- [Computadoras Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery): lista oficial de verificación y diagnóstico sobre las diferencias entre Update, Recover y Reset.

### Referencias prácticas de la comunidad

- [《4.6 Máquinas virtuales, memoria y respaldos》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg): desglose detallado de la arquitectura subyacente de la computadora en la nube, mapa de organización del contexto y colaboración de archivos entre múltiples Bot.
- [《¿Se perdieron todas las herramientas tras restablecer la máquina virtual de Grok Bot? Tutorial de respaldo y recuperación (con prompts incluidos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye): diseño del administrador de servicios de máquinas virtuales, tabla de registro general y práctica de recuperación en un clic compartida por el autor de la comunidad 铁柱AGI (@cgnot996).
