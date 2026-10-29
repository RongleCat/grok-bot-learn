# Capítulo 21 Copia de seguridad y recuperación: sin pánico ante el reinicio del ordenador

Tras reiniciar el ordenador en la nube, el entorno se vacía por completo; teclear `apt-get` y `pip install` de memoria facilita que se omitan dependencias o variables de entorno, y la memoria del Bot entrenado tampoco tiene un botón de exportación. **La solución consiste en dividir la recuperación ante desastres en dos canalizaciones paralelas.**

1. **Servicios de la máquina virtual**: tomar el control de las dependencias del sistema mediante un libro mayor de registro y scripts de recuperación automatizados.
2. **Memoria del agente**: un gestor de memoria dedicado redacta la configuración y los hechos dinámicos en Markdown y los envía a un repositorio privado de Git.

Una vez completada la configuración, **incluso si el sistema se restablece o se migra, todos los servicios y memorias se pueden restaurar con la mínima intervención manual**.


![Copia de seguridad y recuperación: sin pánico ante el reinicio del ordenador](/info/21-backup.png)

## 21.1 Conocer a fondo el ordenador en la nube: qué diferencias hay entre actualizar, recuperar y restablecer

![21.1 Conocer a fondo el ordenador en la nube: qué diferencias hay entre actualizar, recuperar y restablecer](/info/21-backup-s1.png)

**Todos los Bots bajo la misma cuenta comparten la misma máquina virtual**, compartiendo el directorio `/workspace` y los procesos del sistema. Si en una máquina se instalan herramientas globales, los demás Bots pueden utilizarlas, pero una vez que la máquina se restablece, todos los entornos de dependencias dejarán de ser válidos al mismo tiempo.

Consulta [«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

El cliente ofrece opciones de control en **Settings** > **Ordenador** bajo **Ordenador del Bot**. Las diferencias entre las tres son las siguientes:

| Operación | Mecanismo | Contenido conservado | Contenido perdido |
| :--- | :--- | :--- | :--- |
| **Actualización (Update)** | Actualiza la imagen del entorno. Se divide en dos tipos: actualización de software y actualización del ordenador | La actualización de software conserva todo; la actualización del ordenador conserva los bots, los archivos y la información de inicio de sesión | La actualización de software no pierde nada; la actualización del ordenador elimina las aplicaciones y paquetes globales |
| **Recover** | Crea una nueva máquina en la imagen más reciente basándose en los datos guardados, intentando primero conectarse a la máquina antigua para guardar datos | Bots, archivos e información de inicio de sesión guardados | Aplicaciones y paquetes de software globales; si no se puede conectar a la máquina antigua, se perderán las modificaciones no sincronizadas |
| **Reset** | Crea directamente una nueva máquina según los datos guardados más recientemente, interrumpiendo el trabajo en ejecución | Bots, archivos e información de inicio de sesión guardados | Aplicaciones y paquetes de software globales; se perderán las modificaciones no sincronizadas |

El historial de conversaciones se almacena en la nube, por lo que el reinicio de la máquina o la eliminación accidental de archivos no le afectan. Sin embargo, **los paquetes de aplicaciones instalados globalmente, `node_modules` y los entornos virtuales de Python no son guardados oficialmente**, y se eliminarán si se produce una actualización del ordenador, un Recover o un Reset.

Para más detalles, consulta [«Ordenador de Grok Bot»](https://cursor.com/cn/help/grok-bot/computer-recovery).

Cuando la máquina virtual se congele o responda de forma anómala, realiza la resolución de problemas en el siguiente orden:

1. Si muestra **Reconnecting** o **Couldn't Reach el ordenador de Grok Bot**: pertenece a fluctuaciones de la red; espera un momento y haz clic en **Retry**. Durante la reconexión los archivos no se perderán; **está estrictamente prohibido hacer clic en Reset en esta etapa**.
2. Reinicia el cliente. Los usuarios de Mac deben seleccionar **Quit** en la barra de menú superior; simplemente hacer clic en la cruz roja de la ventana no surte efecto.
3. Comprueba las actualizaciones. Ve a **Settings** > **Ordenador**; si hay una actualización disponible, haz clic primero en **Actualizar**. Si se indica que el agente no está en pausa, espera a que termine la tarea actual antes de hacer clic.
4. Intenta recuperar. Si sigues sin poder conectarte o la actualización se queda bloqueada mostrando **Recuperar ordenador**, haz clic en **Recover**. Si aparece el aviso **Update aún en ejecución**, selecciona **Keep waiting**.
5. Ejecuta **Reset**. Si los cuatro pasos anteriores no funcionan, haz clic en Reset. En caso de fallo, puedes reintentar con **Retry Recover** o **Retry Reset**; si los errores continúan, contacta con el soporte oficial.
6. Gestiona las alertas de disco.

   Cuando recibas **Computer is low on disk space** o **Computer is critically low on disk space**, no elimines archivos manualmente; haz clic en **Go to Disk Saver** en la barra lateral para ver las soluciones. El sistema no eliminará ningún archivo sin tu confirmación.

   Para más detalles, consulta [«Ordenador de Grok Bot»](https://cursor.com/cn/help/grok-bot/computer-recovery).

**El ordenador en la nube es solo un contenedor desechable**; no ajustes el entorno manualmente. Todo el proceso de configuración debe realizarse mediante scripts, y la configuración junto con el código fuente propio deben guardarse en un repositorio Git privado externo.

## 21.2 Libro mayor de servicios de la máquina virtual y canalización de recuperación automatizada

![21.2 Libro mayor de servicios de la máquina virtual y canalización de recuperación automatizada](/info/21-backup-s2.png)

[«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

El ordenador en la nube no proporciona instantáneas subyacentes, por lo que **convertir el proceso de reconstrucción en un script de un solo clic es lo más rentable**.

### Libro mayor de servicios y copias de seguridad anticontaminación

Crea un directorio `vm-services/` en el repositorio privado y coloca en él la tabla `REGISTRY.md` para lectura humana y el archivo `registry.json` para el análisis de los scripts automatizados.

El libro mayor y las copias de seguridad deben cumplir varias reglas estrictas.
- Los campos de registro incluyen: ID del servicio, Bot responsable, ruta del código, dependencias de instalación (apt/pip/Docker/cron), comandos de inicio/parada y comprobación de estado (health check), y si la recuperación es obligatoria.
- **Las rutas de las credenciales solo deben registrarse como rutas absolutas locales (como `~/.env`), quedando estrictamente prohibido almacenar texto en claro**; los pasos manuales como el escaneo de códigos QR y OAuth deben destacarse por separado.
- Los scripts de desarrollo propio se guardan por separado en `service-src/`, excluyendo `venv/`, `node_modules/` y los registros; **antes de confirmar (commit), se debe ejecutar un escaneo por expresiones regulares en busca de claves secretas**.

### Canalización de recuperación automatizada

En `vm-services/restore/`, escribe scripts secundarios individuales para cada servicio. **Los scripts deben ser idempotentes**: ejecutarlos dos veces consecutivas no debe arrojar errores de que el directorio ya existe o conflictos de puertos.

El punto de entrada principal, `restore-all.sh`, se ejecuta en serie según el orden de dependencias.
1. **Dependencias básicas**: instalar herramientas del sistema como `cron`, `ffmpeg` y `yt-dlp`.
2. **Colocación del código fuente**: copiar de vuelta los scripts propios desde `service-src/`, omitiendo los archivos existentes y reponiendo solo los faltantes.
3. **Entorno y paquetes**: crear el entorno virtual de Python y ejecutar `pip install -r requirements.txt`.
4. **Levantar procesos residentes**: iniciar los procesos residentes en segundo plano.
5. **Montar tareas programadas**: restaurar la programación unificada de crontab.
6. **Comprobación de estado**: verificar la actividad elemento por elemento; **si falla, registrar el log de errores y continuar con el siguiente elemento**, sin interrumpir ni bloquear.

[«¿Se perdieron todas las herramientas tras reiniciar la máquina virtual de Grok Bot? Tutorial de copia de seguridad y recuperación (con prompts incluidos)»](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.3 Gestor de memoria: guarda la memoria central de los Bots en un repositorio privado

![21.3 Gestor de memoria: guarda la memoria central de los Bots en un repositorio privado](/info/21-backup-s3.png)

De forma oficial no se proporciona un botón de exportación completa de la memoria, por lo que las preferencias se pierden fácilmente al cambiar de cuenta o migrar de sistema. **La forma más segura es establecer un Bot dedicado como "gestor de memoria" que transforme la memoria intangible en instantáneas de texto plano dentro de un repositorio privado de Git.**

[«Grok Bot Gran Evacuación: una solución completa de copia de seguridad para sistemas de agentes»](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Estratificación de la memoria y principios de mantenimiento

| Nivel | Contenido incluido | Descripción y permisos |
|---|---|---|
| **Capa compartida** | Memoria compartida a nivel de cuenta, Skill comunes y configuración de complementos | Todos los Bots pueden leerla |
| **Capa exclusiva** | Contrato de reglas de Description, memoria independiente exclusiva y tareas de Routine | Exclusivo de un solo Bot |

- Los hechos dinámicos no se acumulan a largo plazo en el contexto; solo se registra el método de acceso y se consultan en la fuente cuando se necesitan.
- La memoria compartida debe someterse a una revisión manual o a la validación de flujos de trabajo estandarizados para evitar la contaminación cruzada.
- **Las definiciones del negocio se escriben en la memoria, mientras que los flujos operativos fijos deben quedar consolidados en el código de Skill.**

[«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Estándar de archivado y flujo de trabajo

::: details Estándar de archivado y flujo de trabajo
```text
├── bots/                     # 各 Bot 独立配置与记忆
│   ├── cyber-xiaowan/        # 单个 Bot 文件夹
│   │   ├── agent-spec.md     # 身份设定、名称、bot-id、slug、description
│   │   ├── MEMORY.md         # 核心记忆全量快照
│   │   ├── profile.md        # 角色信息与权限边界
│   │   └── archive/          # 历史版本与过往日志
│   └── ...                   # 其他 Bot 目录
├── meta/                     # 全局元数据与多 Bot 拓扑关系
├── shared-user-memory/       # 账号级共享记忆
├── vm-services/              # 虚拟机服务总账与恢复脚本（见 21.2 节）
├── README.md                 # 仓库使用说明与最新状态
├── RESTORE.md                # 跨环境恢复操作 SOP
└── registry.md               # 登记索引
```
:::

El archivo `MEMORY.md` bajo el directorio de un Bot individual contiene tres niveles: permisos de identidad, responsabilidades de decisión e instantánea del estado actual.

1. **Enumerar la lista**: delimitar los Bots principales que requieren una copia de seguridad persistente.
2. **Programar y enviar instrucciones**: cada Bot lee su propia configuración y memoria, las sintetiza y las escribe en el archivo Markdown correspondiente dentro de `/workspace`.
3. **Captura, validación y almacenamiento**: **realizar un escaneo para confirmar que no haya tokens en texto claro y enviar de forma unificada**, asignando una etiqueta de fecha (por ejemplo, `tag-2026-10-15`) y subiéndola al repositorio privado remoto.

**El Bot se encarga de la instantánea completa, mientras que Git se encarga del seguimiento incremental**. El Bot sobrescribe completamente el archivo en cada ocasión, dejando el registro histórico de los cambios al motor de Git, sin necesidad de calcular las diferencias en el prompt.

## 21.4 Casos prácticos: La gran evacuación y el gestor de servicios de 铁柱AGI

### Copia de seguridad con el gestor de memoria

铁柱AGI (@cgnot996) mantiene 21 Bots. Para evitar perder la memoria en caso de bloqueo de la cuenta, configuró un Bot «gestor de memoria» complementado con un repositorio privado de Gitee para el archivado.

1. **Delimitar el núcleo**: seleccionar primero 7 Bots principales de los 21 para una prueba piloto.
2. **Exportación y verificación**: notificar a los 7 Bots que exporten sus configuraciones y memorias. **Algunos Bots se quedan en silencio tras la exportación; es imprescindible exigir en las instrucciones «informar al terminar», al tiempo que el gestor escanea el directorio `/workspace` para cotejar**.
3. **Almacenamiento y etiquetado**: el primer lote de 73 KB se archiva y almacena, etiquetándose con `tag 2026-09-10` y superando el escaneo de claves secretas.
4. **Estructura de archivo individual**: como en «Cyber Xiaowan», `MEMORY.md` (aprox. 21 KB) almacena la identidad y las instantáneas, mientras que `agent-spec.md` guarda el bot-id y la descripción.
5. **Activar la programación**: configurar el archivado automático periódico.

Al importar a una nueva cuenta, la tasa de restauración de la memoria es de aproximadamente el 80 %. **Los archivos locales no respaldados, el historial de conversaciones y las sesiones de inicio de sesión de terceros no se pueden restaurar**.

Al migrar a Hermes u OpenClaw, basta con colocar `MEMORY.md` en el directorio de memoria y cambiar la description de `agent-spec.md` por el prompt del sistema para empezar a funcionar.

[«Grok Bot Gran Evacuación: una solución completa de copia de seguridad para sistemas de agentes»](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Gestor de servicios de la máquina virtual

El bloqueo y reinicio del ordenador en la nube provoca la pérdida de todas las herramientas. El autor registra el libro mayor de reconstrucción en el directorio `vm-services` del repositorio `grok-bot-memory` en Gitee.

1. **Registro en el libro mayor**: a fecha de 2026-10-10, se han registrado 20 elementos de 10 Bots (4 residentes, 14 herramientas bajo demanda y 2 elementos de claves), de los cuales 18 están marcados como «recuperación obligatoria».
2. **Clasificación de servicios**: los servicios residentes incluyen servicios de raspado web (scraping), el encapsulamiento de la API de Muse, así como el motor de correo y los túneles de salida; para las herramientas bajo demanda (ffmpeg, Chrome, etc.) solo se registran los comandos de instalación; para Metaso y TikHub solo se registran las rutas de las claves.
3. **Copia de seguridad limpia del código fuente**: unos 5.1 MB de código fuente propio, excluyendo claves, registros y flujos de estado.
4. **Recuperación encadenada**: el gestor mantiene el directorio `restore/` y `restore-all.sh`. **El gestor no ejecuta nada por iniciativa propia en circunstancias normales; espera instrucciones manuales para levantar los servicios según las dependencias y entrega una lista de verificación de aceptación**.

[«¿Se perdieron todas las herramientas tras reiniciar la máquina virtual de Grok Bot? Tutorial de copia de seguridad y recuperación (con prompts incluidos)»](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.5 Seguridad de credenciales y compuerta de aprobación manual: cede la pantalla, no la contraseña

**Varios Bots comparten el disco y las sesiones de navegador de la máquina virtual; crear un nuevo Bot no aísla en absoluto los datos confidenciales.** Si se escribe texto en claro en un script o en el chat, otros Bots o los registros externos podrán leerlo.

[«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Conserva solo rutas de credenciales, nunca texto en claro

- Almacena los tokens y las claves privadas en `~/.env` (que no entra en Git) o en un directorio global de claves.
- En `REGISTRY.md`, `registry.json` y los archivos de memoria, **todo lo relacionado con credenciales solo registra la ruta absoluta del disco**.
- Queda estrictamente prohibido enviar contraseñas en el cuadro de diálogo; antes de hacer push, se debe ejecutar un escaneo de desensibilización por expresiones regulares.

### Cede la pantalla, no la contraseña

1. Cuando el Bot se encuentre con una ventana emergente de 2FA, escaneo de código QR o verificación de dispositivo, se detiene de inmediato y te notifica para que tomes el control.
2. Abres la pantalla completa del ordenador en la nube en el cliente e introduces la contraseña o escaneas el código QR tú mismo.
3. Una vez completado, devuelves el control; **el Bot hereda la cookie de sesión y continúa ejecutándose sin tocar nunca la contraseña en texto claro**.

### Configurar Ask-first para operaciones de alto riesgo

- Las operaciones irreversibles como publicar, pagar, eliminar datos o modificar el entorno subyacente deben mostrar una ventana emergente a la espera de la aprobación manual. La versión v0.70.2 optimizó esta lógica de confirmación.
- **Los permisos autónomos del Bot se limitan únicamente a la lectura, búsqueda pública y lectura/escritura dentro de `/workspace`**; en caso de conflicto entre reglas, Ask-first tiene prioridad.

## 21.6 Tres conjuntos de prompts listos para usar

A continuación, se ofrecen tres conjuntos de prompts verificados en la práctica; basta con copiarlos y enviarlos al Bot correspondiente para desplegarlos y utilizarlos.

### Prompt 1: Configurar un «gestor de servicios de la máquina virtual» para el ordenador en la nube

Crea un Bot «gestor de servicios de la máquina virtual» y **pégalo en la configuración**:

::: details Prompt 1: Configurar un «gestor de servicios de la máquina virtual» para el ordenador en la nube
```text
你是「虚拟机服务管家」，只管一件事：记下这台虚拟机上部署过的所有第三方服务，并在电脑更新或换账号之后，按记录把它们原样恢复。

你维护的东西
1. 一份登记总账，人和机器各读一份：REGISTRY.md（表格）和 registry.json（给脚本读）。
2. 每个服务一个恢复脚本 restore/restore-<服务>.sh，必须幂等，重复跑也不会出错。
3. 一个总入口 restore/restore-all.sh，按依赖顺序调用各个恢复脚本，最后汇总哪些失败了。
4. 一份源码备份 service-src/：各 Bot 自己写的服务代码和脚本，同步时排除密钥、日志、运行状态、虚拟环境和个人数据，并先扫一遍明文密钥，命中就停。
5. 以上全部跟着一个私有 Git 仓库存（「你的备份仓库地址」）。总账、恢复脚本、源码都在仓库里，密钥永远不进仓库。

登记规则（其他 Bot 部署任何服务都必须来找你登记）
每项必须包含：
- 名称和短 id、用途、负责的 Bot
- 路径：代码、配置、数据分别在哪
- 安装方式和依赖（apt / pip / npm / Docker / 系统定时任务）
- 启停命令、健康检查命令
- 更新后的恢复步骤，或者对应的恢复脚本
- 是否必恢复：是 / 否
- 密钥：只写存放路径，绝不写明文
- 需要真人完成的步骤（OAuth 登录、扫码、导入 cookie）单独标出来

你的工作方式
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

### Prompt 2: Hacer que el Bot ejecute una recuperación completa tras el reinicio del ordenador

Configura el **token de acceso de Git**, reemplaza el contenido entre corchetes/paréntesis y envíalo al Bot.

::: details Prompt 2: Hacer que el Bot ejecute una recuperación completa tras el reinicio del ordenador
```text
这台电脑刚重置过（或者是换了新账号），之前部署的服务都没了。请按我的备份把它们恢复到可用状态，规则如下。

备份在哪
- 备份仓库：<你的备份仓库地址>，分支 <分支名>
- 仓库里有：登记总账（REGISTRY.md 和 registry.json）、每个服务的恢复脚本（restore/）、自写服务的源码备份（service-src/）
- 仓库里没有密钥，这是故意的

请按这个顺序做
1. 把备份仓库拉到工作目录，先读总账，告诉我一共登记了几项、哪些标了「必恢复」、哪些只留密钥不用恢复。先列出来，不要动手。
2. 把自写服务的源码从 service-src/ 放回总账写的原位置。只补缺失的，已经存在的目录不要覆盖。
3. 按总账的依赖顺序逐项恢复：先装系统依赖（比如 cron、ffmpeg），再装命令行工具，最后拉起常驻服务和定时任务。每项都用它自己的恢复脚本，脚本要能重复跑。
4. 每装完一项就跑它登记的健康检查。失败了先看日志、试着修一次；修不好就记下原因，接着做下一项，不要卡住。
5. 把需要我本人做的事汇总成一张清单：要重新提供的密钥（只说放哪个路径、叫什么名字，别让我把密钥贴进聊天）、要重新登录授权的工具（OAuth、扫码、设备码）。然后一项一项带我做，每做完一项马上复查。
6. 故意暂停的任务保持暂停，总账里写了原因和重开条件的照办。别因为“看起来漏装了”就自作主张打开。
7. 最后交验收清单，每项一行：服务名、结果（成功 / 失败 / 等我处理）、健康检查输出摘要、花了多久。再告诉我总共用了多少时间、成功了几项。

不要做的事
- 不要把任何密钥写进仓库、日志或聊天
- 不要跑总账没登记的安装
- 不要用“重置电脑”当修复手段
- 恢复完如果有任何改动（路径变了、版本升级了），更新总账，提交推回备份仓库
```
:::

### Prompt 3: Instrucción de archivado periódico para el gestor de memoria

**Envía esto para Routine o archivado manual:**

::: details Prompt 3: Instrucción de archivado periódico para el gestor de memoria
```text
请开始执行本周的智能体记忆与设定归档任务。

执行步骤：
1. 枚举当前工作区内所有处于活跃状态的 Bot 名单，核对 bots/ 目录下的已有目录。
2. 逐个通知名单内的 Bot：读取各自的 Description、人设规则与当前核心记忆，按三层结构（身份profile、历史决策与职责、当前现场快照）提炼并覆盖写入 /workspace/bots/<bot-slug>/MEMORY.md。同时将身份元数据更新至 agent-spec.md。
3. 检查各 Bot 回执，并在 /workspace 目录核对文件生成情况，确保所有目标 Bot 的 Markdown 均已写出。
4. 提取账号级共享记忆，更新至 shared-user-memory/ 目录下的 Markdown 文件中。
5. 对本次生成的所有 Markdown 文件进行敏感信息正则扫描，检查是否存在明文 API Token、密码或私钥。如果发现疑似凭证，立即中断并报警。
6. 扫描无异常后，执行 Git 操作：将所有更新文件暂存，提交信息标记为「memory snapshot YYYY-MM-DD」，推送到远端私有 Git 仓库，并打上对应日期的 Git Tag。
7. 完成后向我汇报：本次归档了哪几个 Bot、总文件大小、是否有失败或超时的 Bot。
```
:::

## 21.7 Errores comunes y precauciones

1. Cuando aparezca el aviso Reconnecting, **no hagas clic en Reset**; se trata solo de fluctuaciones de la red o mantenimiento. Si haces clic, se sobrescribirán los datos no guardados con una instantánea antigua.
2. Compartir la autorización de Codex entre varios dispositivos provocará desconexiones mutuas; es necesario configurar subcuentas independientes o credenciales fijas.
3. Las tareas programadas deben consolidarse de forma unificada en el archivo de configuración de crontab e incluirse en Git para evitar omisiones tras el reinicio de la máquina.
4. El libro mayor de servicios debe basarse en comandos operativos reales; si el entorno no tiene instalado Docker, el script de recuperación se quedará bloqueado.
5. Los Bots suelen quedarse en silencio tras exportar; el gestor debe inspeccionar activamente el disco y restringir estrictamente las instrucciones con «es obligatorio informar al terminar de escribir».
6. **El repositorio de copias de seguridad debe ser privado e incluir escaneo por expresiones regulares**, para evitar que los tokens se suban a un repositorio público con un Git push.

## 21.8 Cómo realizar la aceptación tras completarlo

### Servicios y scripts
1. Cotejo: comprueba con `vm-services/REGISTRY.md`, utiliza `ps aux` para inspeccionar procesos y `netstat` o `ss` para verificar puertos; **no debe haber rutas de más ni de menos en el registro**.
2. Prueba de ejecución: ejecuta por separado `restore-<服务名>.sh` para comprobar si se puede ejecutar repetidamente sin errores.
3. Simulacro completo: clona en un directorio temporal y ejecuta `bash restore/restore-all.sh`, **asegurándote de que todos los elementos marcados como «recuperación obligatoria» pasen con éxito** y que los pasos que requieran intervención manual estén listados.

### Repositorio y memoria
1. Inspeccionar la estructura: revisa `bots/` en la interfaz web; cada Bot debe tener sus propios `agent-spec.md` y `MEMORY.md` independientes.
2. Muestreo: abre `MEMORY.md` y confirma que los tres niveles («profile de identidad», «decisiones históricas y responsabilidades» y «captura del estado actual») estén completos, sin plantillas vacías ni caracteres corruptos.
3. Búsqueda de secretos: busca globalmente `sk-`, `Bearer` o `password`; **las credenciales solo deben conservar rutas absolutas locales, quedando estrictamente prohibidos los tokens en texto claro**.

## Lecturas complementarias

- Guías de uso oficiales y páginas de soporte:
  - [«Ordenador de Grok Bot»](https://cursor.com/cn/help/grok-bot/computer-recovery)
  - [«Almacenar información confidencial de forma segura»](https://cursor.com/cn/help/grok-bot/secrets)
  - [«Obtener ayuda»](https://cursor.com/cn/help/grok-bot/get-help)
  - [«Guía de uso de Grok Bot»](https://cursor.com/cn/help/grok-bot/how-to)
- Artículos de referencia y casos prácticos de la comunidad:
  - 铁柱AGI @cgnot996: [«¿Se perdieron todas las herramientas tras reiniciar la máquina virtual de Grok Bot? Tutorial de copia de seguridad y recuperación (con prompts incluidos)»](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)
  - 铁柱AGI @cgnot996: [«Grok Bot Gran Evacuación: una solución completa de copia de seguridad para sistemas de agentes»](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)
  - Recopilación estructurada de la base de conocimientos: [«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
