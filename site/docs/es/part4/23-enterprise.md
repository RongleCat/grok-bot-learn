# Capítulo 23: Edición Teams e Implementación Empresarial

Al implementar Grok Bot para un equipo, los principales puntos de fricción suelen ser los siguientes.

- La pasarela intercepta durante la fase de negociación (handshake), lo que provoca que **no se pueda conectar a la computadora en la nube**.
- La máquina virtual Linux no tiene instalado el cliente MDM, por lo que el IdP corporativo la considera un dispositivo no confiable.
- Existen riesgos de fuga de credenciales y de penetración en la red interna, además de carecer de medios de distribución silenciosa del cliente.

Si se configuran correctamente el **SSO y las excepciones en la pasarela de seguridad** según el flujo, y se habilita el acceso a la red privada, se podrá resolver la gestión del ciclo de vida a gran escala.


![Edición Teams e implementación empresarial](/info/23-enterprise.png)

## Controles de gestión de Teams y Enterprise: arquitectura y límites de capacidades

![Controles de gestión de Teams y Enterprise: arquitectura y límites de capacidades](/info/23-enterprise-s1.png)

### Qué es

**Cada usuario dispone en exclusiva de una microVM Firecracker en la nube**, donde se envían instrucciones y aprobaciones localmente, mientras que el código y el navegador se ejecutan en la nube.

Un detalle a tener en cuenta: **todos los bots bajo el mismo usuario comparten esta máquina virtual**, por lo que los archivos y el estado de inicio de sesión son completamente compartidos.

El plan The X Subscription del 12-10-2026 dividió los permisos en dos versiones:

- **Versión Teams**: habilitada por defecto para todos los miembros, utiliza una IP de salida estática compartida e incluye auditoría básica y reglas de equipo.
- **Versión Enterprise**: admite autorización por grupos y SCIM 2.0, permite el uso de sudo y listas blancas de red, e incluye grabación de operaciones y exportación a OpenTelemetry (con la etiqueta `cursor.surface=grok_bot`).

Para más documentación, consulte [Grok Bot para Teams y Enterprise](https://cursor.com/cn/docs/grok-bot/teams).

### Cómo hacerlo

La configuración diaria se gestiona en la [página de Grok Bot del panel de control de Cursor](https://cursor.com/dashboard/bot), y se divide principalmente en cuatro pasos.

1. División de permisos e interruptores básicos
- Durante la fase gradual (canary/piloto), haga clic en **Manage Group Access** para seleccionar a los usuarios piloto; si no se utiliza la codificación en la nube, desactive Cloud Agents; mantenga desactivado el uso compartido de plantillas públicas para evitar fugas.
- **Se recomienda configurar la ejecución local en Never allow**, desactivando al mismo tiempo el enrutamiento de salida local para evitar el reenvío indebido.
- Para fijar bots en la barra lateral, seleccione All team o grupos específicos en la columna Auto-add.

2. Configuración de bloqueos de aprobación y reglas
- Al activar el **modo Enforce Auto-review**, los miembros no podrán desactivar la revisión por su cuenta en el cliente.
- Configure las operaciones de alto riesgo (como despliegues en producción o envío de correos salientes) como Ask first, y limite las de solo lectura a Allow automatically.
- **En caso de conflicto entre las reglas de equipo y las individuales, el sistema impondrá obligatoriamente Ask first**.

3. Configuración de red y secretos
- En la configuración de red, elija la lista de permitidos del equipo únicamente o agregue valores predeterminados, ingresando nombres de dominio y rangos de IP; para evitar la manipulación del sistema, puede deshabilitar sudo (que está activado de forma predeterminada).
- **En Team Secrets, el equipo puede agregar hasta 100 elementos**, con un límite de 32 KB por elemento y una capacidad total de 96 KB; el texto sin formato no se muestra tras guardar.
- Los nombres de variables de secretos tienen prohibido el uso de nombres reservados del sistema como `PATH`, `HOME` o que comiencen con `SAND_` o `LD_`.

4. Configuración de directivas a nivel de grupo
- Acceda a los grupos desde [Members > Groups](https://cursor.com/dashboard/members?subtab=groups); **el principio de configuración es que solo se puede flexibilizar, no hacer más estricto**.
- Marcar Don't enforce for this group permite desbloquear la restricción de revisión automática.
- La directiva de red es una excepción: el grupo sobrescribirá directamente la del equipo; si un miembro pertenece a varios grupos, la red se aplicará según la regla más estricta, mientras que los permisos se otorgarán según la más permisiva.

### Criterios de éxito

- El panel de control distingue claramente entre los grupos piloto y los grupos no autorizados; el personal no autorizado no puede activar el bot en el cliente.
- Las reglas de equipo y las reglas de Auto-review están bloqueadas; los miembros pueden ver las reglas de equipo en la página de configuración del cliente, pero los botones de edición y eliminación aparecen deshabilitados.
- Las operaciones de alto riesgo (comunicación externa, destrucción de archivos, comandos privilegiados) activan la intercepción de aprobación al cien por cien.

---

## Identidad y SSO: habilitación de acceso universal y compatibilidad con la confianza de dispositivos

### Qué es

Grok Bot utiliza el sistema de cuentas de Cursor, por lo que **no es necesario crear una aplicación independiente en el IdP**. Documentación de referencia: [Configurar identidad y acceso](https://cursor.com/cn/docs/grok-bot/identity).

El bot se ejecuta en una máquina virtual Linux en la nube sin MDM instalado, por lo que no puede cumplir con FastPass o Hybrid Join. **Recuerde que no debe desactivar el cumplimiento de dispositivos a nivel global**; en su lugar, configure una directiva de excepción para el grupo objetivo antes de las reglas de intercepción.

### Cómo hacerlo

- **Ampliar asignación en Okta**: ingrese en la aplicación de Cursor a **Assignments** > **Assign to Groups** y seleccione los grupos comerciales; al habilitar SCIM, sincronice la asignación y envíelos (Push Groups).

  **SAML SSO y SCIM deben asignarse simultáneamente**; si se omite SSO, el inicio de sesión será interceptado.
- **Ampliar asignación en Entra ID**: en **Users and groups** dentro de la aplicación de Cursor, haga clic en **Add user/group** para añadir grupos (requiere licencias P1/P2, no admite grupos anidados); asigne simultáneamente los mismos grupos en la aplicación de aprovisionamiento.
- **Permitir Linux en Okta**: antes de la regla de bloqueo de la directiva de autenticación, cree una nueva regla `Grok Bot computer (Linux)`.

  Limite los usuarios al grupo de Cursor, en **Device platform seleccione Other Desktop** (no existe una opción independiente para Linux) y en Device state elija Any; para la verificación, seleccione Password + Another factor, sin marcar restricciones resistentes al phishing.
- **Permitir Linux en Entra ID**: cree una directiva de alta prioridad, especificando el grupo de Cursor y las aplicaciones de destino; incluya Linux en Device platforms y excluya Windows y macOS; en Grant marque Require multifactor authentication; **debe excluir este grupo o la plataforma Linux de la directiva de cumplimiento original**.

### Criterios de éxito

- Los usuarios de la empresa inician sesión en el cliente de escritorio mediante SSO corporativo sin recibir el error `User is not assigned to this application`.
- En el navegador del bot se puede acceder a la red interna mediante contraseña y autenticación de dos factores, sin que aparezcan avisos de FastPass o bloqueos por incumplimiento del dispositivo.
- **Cuando los empleados acceden desde sus computadoras personales, FastPass y el cumplimiento del dispositivo original siguen aplicándose estrictamente**.

## Acceso a redes privadas: enrutamiento de escritorio y automatización con scripts de Team Setup

![Acceso a redes privadas: enrutamiento de escritorio y automatización con scripts de Team Setup](/info/23-enterprise-s3.png)

### Qué es

Grok Bot se ejecuta en la nube, por lo que **para acceder a la red interna es necesario habilitar la red privada**.

- Enrutamiento del cliente de escritorio: adecuado para depuración temporal. Active `Settings > Computer > Route traffic through this computer` en el cliente para que el tráfico pase por la tarjeta de red local; los administradores pueden deshabilitarlo con un solo clic desde el panel de control.
- Instalación de cliente mediante Team Setup: para acceso regular y **exclusivo de la versión Enterprise**. El departamento de TI mantiene un script unificado que se inicia y se conecta automáticamente a la red interna cuando el bot arranca o se actualiza.

Para más detalles, consulte [Conectarse a redes privadas](https://cursor.com/cn/docs/grok-bot/private-networks).

### Cómo hacerlo

Los scripts de configuración de entorno del equipo se encuentran en el panel de control en **Bot Computers**, y se ejecutan como un usuario normal con `sudo` en una máquina virtual Debian Linux. **El script se ejecuta al iniciar y se actualiza periódicamente alrededor de una vez al día, con un tiempo límite de espera de 30 minutos**.
- Si el código de salida de `check` es 0, se omite la instalación; una vez instalado, se volverá a ejecutar `check` para verificar.
- **Los fallos de ejecución no bloquean el inicio de la computadora** y se reintentarán en la siguiente actualización periódica.

#### Solución de conexión con Tailscale

1. Abra **Team Secrets**, agregue la clave de autenticación de Tailscale `TS_AUTHKEY` (con el valor `tskey-auth-...`) y vincule una etiqueta ACL exclusiva (como `tag:grok-bot`) en la consola de Tailscale para **restringir estrictamente los permisos de acceso**.
2. Ingrese a los scripts de configuración de entorno del equipo, haga clic en **+** para crear un nuevo manifiesto, ingrese `private-network-tailscale` en Manifest ID y cambie al modo JSON o formulario para ingresar la configuración:

::: details Solución de conexión con Tailscale
```json
{
  "manifestId": "private-network-tailscale",
  "entries": [
    {
      "id": "install-tailscale",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://tailscale.com/install.sh | sh\nsudo tailscale up --authkey=\"$TS_AUTHKEY\" --accept-routes --hostname=\"grok-vm-${USER}\"",
      "check": "command -v tailscale && tailscale status"
    }
  ]
}
```
:::

#### Solución de conexión con Cloudflare Tunnel

- Servicios HTTP privados: acceda directamente al dominio de enrutamiento del túnel; Cloudflare Access se encargará de la autenticación e interactuará en el navegador del bot para completarla.
- Servicios TCP privados (como bases de datos o SSH): instale `cloudflared` en el manifiesto; cuando necesite conectarse, ejecute el comando en la Shell para **abrir un puerto de reenvío local**:

`cloudflared access tcp --hostname db-internal.corp.com --url localhost:5432`

::: details Solución de conexión con Cloudflare Tunnel
```json
{
  "manifestId": "private-network-cftunnel",
  "entries": [
    {
      "id": "install-cloudflared",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null\necho 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared bullseye main' | sudo tee /etc/apt/sources.list.d/cloudflared.list\nsudo apt-get update && sudo apt-get install -y cloudflared",
      "check": "command -v cloudflared"
    }
  ]
}
```
:::

#### Habilitar extremos del plano de control junto con las directivas de red

Si el equipo activa el control de red **Solo lista de permitidos del equipo**, **debe agregar el plano de control de las herramientas de red a la lista de permitidos**; de lo contrario, el cliente no podrá completar la autenticación. Por ejemplo, al usar Tailscale, se deben autorizar en la directiva los dominios del servidor de coordinación y de los servidores de retransmisión DERP; los cambios de directiva tardan aproximadamente 1 minuto en propagarse a la máquina virtual.

### Criterios de éxito

- Las computadoras del bot recién creadas o reconstruidas aparecen automáticamente en la lista de dispositivos de la consola de administración de Tailscale o Cloudflare tras completar el inicio, con estado en línea.
- El script `check` del manifiesto devuelve de forma estable 0 en las actualizaciones periódicas diarias posteriores, sin ejecutar de nuevo la lógica de instalación.
- Los tokens confidenciales se inyectan íntegramente a través de Team Secrets, sin ninguna credencial en texto sin formato en el texto del manifiesto ni en los registros de ejecución.

---

## Prevención de problemas con proxies y pasarelas corporativas: reglas de admisión y exención de inspección TLS

Las pasarelas corporativas (como Zscaler o Palo Alto) a menudo permiten que el chat funcione normalmente pero **impiden tomar capturas de pantalla o controlar el terminal**.

La causa raíz radica en que el plano de control utiliza conexiones persistentes de transmisión HTTP/2 o SSE con dominios anidados de segundo nivel `<computer>.<cluster>.cursorvm.com`, las cuales no pueden coincidir con reglas simples de un solo nivel.

Consulte la explicación oficial en [Configurar proxies de inspección TLS](https://cursor.com/cn/docs/grok-bot/proxies).

### Puntos clave de configuración

La pasarela debe autorizar los siguientes dominios, además de **desactivar el almacenamiento en búfer de respuestas y estar exenta de la inspección TLS**, para evitar fallos de enlace (handshake) de extremo a extremo y tiempos de espera agotados en la transmisión en flujo continuo:
- `*.cursor.sh`: API principal
- `*.cursorvm.com` y **`*.*.cursorvm.com`**: canal de control, debe admitir comodines de doble nivel
- `*.cursor-cdn.com`, `*.cursorapi.com`, `downloads.cursor.com` y el sitio principal: recursos estáticos y descargas de actualizaciones

Una vez configuradas las directivas, **asegúrese de sincronizarlas con la configuración de itinerancia (Off-Network)** para evitar que los empleados no puedan conectarse cuando estén fuera de la red o trabajando desde casa.

### Resolución de problemas y verificación en dispositivos

Siga estos pasos de diagnóstico en el terminal de la computadora del empleado:

1. Verifique si el certificado ha sido alterado; el emisor normal debe ser **Amazon RSA**:
```bash
   curl -v https://api2.cursor.sh |& grep -C1 issuer:
   ```
2. Verifique la resolución DNS multinivel; si falla, compárela con `nslookup test.us9.cursorvm.com 1.1.1.1`:
```bash
   nslookup test.us9.cursorvm.com
   ```
3. Compruebe la transmisión en flujo: los datos deben mostrarse línea por línea; si se detiene durante varios segundos y de repente se imprime todo junto, significa que el almacenamiento en búfer de la pasarela no está desactivado.

Criterios de aceptación: **conexión con la computadora en la nube en menos de 5 segundos tanto en la red de la oficina como en itinerancia doméstica**, certificado directo con Amazon RSA y conexiones persistentes en flujo sin latencia por búfer.

## Distribución del cliente de escritorio y control de versiones

### Plataformas y mecanismos de actualización

| Plataforma | Formato de instalación | Lógica de actualización |
| --- | --- | --- |
| macOS | `.dmg` (Apple Silicon / Intel) | Comprobación automática de actualizaciones al iniciar, **no se puede desactivar por directiva** |
| Windows | Setup `.exe` (x64 / Arm64) | Comprobación automática de actualizaciones al iniciar, no se puede desactivar por directiva |
| Linux | `.deb`, `.rpm`, AppImage | deb y rpm son gestionados por el administrador de paquetes; AppImage comprueba actualizaciones automáticamente |
| iOS | App Store | Requiere iOS 18 o superior |
| Android | Google Play | Requiere Android 9 o superior, admite distribución administrada |

Para las instrucciones oficiales de despliegue, consulte [Desplegar Grok Bot en su organización](https://cursor.com/cn/docs/grok-bot/deployment).

### Despliegue y control de versiones

1. **Obtención del paquete de instalación**
   No descargue el paquete de instalación manualmente desde la web; llame directamente al feed JSON oficial: `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`.
   `{platform}` admite macOS (`darwin-arm64`, `darwin-x64`), Windows (`win32-x64-user`, `win32-arm64-user`) y Linux (`linux-x64`, `linux-arm64`).
```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand
```
   La interfaz devuelve `version`, `commitSha`, `downloadUrl`, así como `debUrl` y `rpmUrl` para Linux. Para macOS y Windows, también se puede construir directamente la URL del instalador según el formato:
   - Windows: `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`
   - macOS: `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`

2. **Distribución mediante MDM**
   - Windows (Intune / SCCM): agregue `/S` a los parámetros para la instalación silenciosa. El instalador escribe por defecto en `%LOCALAPPDATA%\Programs` del usuario actual, por lo que **debe ejecutarse en el contexto de usuario (User Context)**.

     Nunca use la cuenta SYSTEM local, de lo contrario se instalará en una ruta incorrecta y los empleados no encontrarán la aplicación.
```cmd
  Grok_Bot_1.0.0_Setup.exe /S
  ```
   - macOS (Jamf / Kandji / Intune): basta con desplegar el archivo `.dmg` correspondiente a la arquitectura en el directorio `/Applications`.
   - Linux (Ansible / Puppet): instale el paquete de software `.deb` o `.rpm`, y el sistema configurará automáticamente los repositorios oficiales de software.

3. **Control y bloqueo de versiones**
   En macOS y Windows no es posible desactivar por completo la actualización automática mediante directivas.

En Linux se puede bloquear la versión mediante el gestor de paquetes, o establecer `Enabled: no` en `/etc/apt/sources.list.d/grok-bot.sources` o `enabled=0` en `/etc/yum.repos.d/grok-bot.repo` para pausar la sincronización:
```bash
  sudo apt-mark hold grok-bot
  ```
   Cursor establece un periodo de soporte para las versiones antiguas. **Si el cliente cae por debajo del umbral mínimo de soporte, aparecerá una ventana emergente a pantalla completa con Update required bloqueando el uso**, y en Linux una versión bloqueada que expire también será bloqueada. El equipo de operaciones debe **desplegar gradualmente una nueva versión estable probada cada dos a cuatro semanas**.

### Criterios de aceptación

- Los dispositivos de trabajo completan la instalación silenciosa mediante MDM, por lo que **el escritorio está listo cuando los nuevos empleados inician su computadora**.
- El equipo de TI mantiene un ritmo fijo de rotación de versiones, completando la transición de versiones dentro de la organización antes de que ocurra el bloqueo forzado oficial.

## Gestión de computadoras Bot: operaciones masivas y ciclo de vida

![Gestión de computadoras Bot: operaciones masivas y ciclo de vida](/info/23-enterprise-s6.png)

### Operaciones principales y permisos

El acceso se encuentra en la sección **Bot Computers** de la [página de Grok Bot del panel de control de Cursor](https://cursor.com/dashboard/bot); haga clic en **Manage Bot Computers** para ingresar.

**Esta función es exclusiva para los administradores de la organización (Organization Admins) en la versión Enterprise**; los administradores de equipo estándar no verán este acceso.

Consulte la documentación en [Administrar computadoras Grok Bot](https://cursor.com/cn/docs/grok-bot/computers).

| Nombre de la operación | Comportamiento subyacente | Estado de retención de datos y archivos | Escenarios de aplicación |
| --- | --- | --- | --- |
| **Recrear VMs (Recreate VMs)** | Reinstala con la imagen más reciente y vuelve a ejecutar los scripts de entorno | **Conservados**. El disco permanece intacto; los bots, archivos personales y cookies se conservan; solo se eliminan los paquetes de software del sistema instalados manualmente | Aplicar cambios en los scripts de entorno, pruebas graduales de nuevas imágenes |
| **Terminar VMs (Terminate VMs)** | Destruye de inmediato las instancias en ejecución o en suspensión, interrumpiendo el cómputo actual | **Conservados**. Se conserva el disco; el próximo mensaje enviado desde el cliente levantará una nueva máquina virtual limpia | Resolver bloqueos de instancias, liberar recursos en la nube |
| **Eliminar máquina virtual y datos** | Destruye la máquina virtual y elimina por completo el almacenamiento persistente vinculado | **No conservados**. Los datos se borran por completo; el próximo uso inicializará una computadora en blanco desde cero | Baja de empleados, restablecimiento completo por corrupción de datos |

### Operaciones en la consola y resolución de problemas

1. Ingrese a la página y haga clic en **Manage** (Administrar), busque por nombre o correo electrónico para filtrar miembros; admite selección individual, múltiple o **Select all**.
2. En el menú desplegable **Manage selected**, elija la operación de destino, confirme la cantidad de usuarios afectados y comience la ejecución.
3. Una vez finalizada la ejecución, **es imprescindible hacer clic en el botón Done de la tarjeta**. Cada equipo solo puede ejecutar una operación masiva a la vez; si no hace clic en Done, los botones posteriores permanecerán bloqueados.

Si encuentra estados omitidos o fallidos, proceda según el acuse de recibo:
- **Omitido (sin VM / no se puede completar la operación)**: no hay ninguna máquina virtual asociada al usuario o este abandonó el equipo durante la espera en cola; no requiere acción.
- **Fallido (otra recreación en curso / escaneo de VM incompleto)**: otra actualización no ha finalizado o el backend aún no ha obtenido el estado; espere unos minutos y vuelva a intentarlo.
- **Fallido (no se puede completar la operación)**: el bot está ejecutando tareas de alta intensidad, lo que provoca un tiempo de espera agotado; notifique al miembro que deje el bot inactivo temporalmente y vuelva a intentarlo.

### Automatización y criterios de aceptación

Active la opción **Terminate Inactive Computers** sobre los botones de operación. **Las computadoras de miembros que permanezcan inactivas durante 30 días seguidos se terminarán automáticamente**, liberando únicamente la instancia de cómputo y conservando el disco, con una limpieza periódica continua del sistema.

Para la administración y mantenimiento masivo de múltiples equipos, se puede invocar la [API de Admin de la Organización](https://cursor.com/docs/account/organizations/organization-admin-api.md#grok-bot-computers).

Al invocarla, debe proporcionar una clave de API de la organización con permisos `admin:*`, pasando el ID del equipo, un array con los correos de los miembros y el tipo de acción (`recreate` o `terminate`), y realizar un sondeo del progreso; también está sujeta al límite de una única operación concurrente por equipo.

Al momento de la verificación, preste especial atención a dos indicadores:
- Las instancias se pueden reconstruir masivamente sin problemas y sin pérdida de datos.
- Se ha habilitado la terminación automática tras 30 días de inactividad, evitando que las máquinas virtuales zombi consuman la cuota de la organización en la nube.

## Configuración de referencia de seguridad empresarial y prompts prácticos

### Configuración para administradores
1. Bloquee la red en "Solo lista de permitidos del equipo", y desactive las plantillas públicas y los canales de correo electrónico.
2. Habilite **Enforce Auto-review** y configure la ejecución local en **Never allow** para evitar degradaciones no autorizadas.
3. Cualquier llamada a APIs de producción, modificación de bases de datos, envío de correos salientes, firma de acuerdos o fusión en main debe configurarse obligatoriamente como **Ask first**; las consultas de registros y compilaciones se permiten directamente.

### Reglas para empleados
1. Las credenciales deben transmitirse mediante variables de entorno; **está estrictamente prohibido pegar contraseñas en texto sin formato en el cuadro de diálogo**.
2. Para autorizaciones sensibles, elija **Allow once** en lugar de permitir siempre, y cierre la sesión puntualmente tras su uso.

### Prompts prácticos
::: details Prompts prácticos
```text
你现在负责对内部服务进行接口与架构调研。
请遵循以下严格的安全限制：
1. 本次任务为纯只读模式，严禁对目标服务发起任何 POST、PUT、DELETE 请求。
2. 检查网络连通性：尝试向内部端点 http://api-monitor.corp.internal/health 发起 GET 请求并打印状态码。
3. 如果遇到证书问题或连接被重定向，记录错误日志，不要尝试使用任何提权手段。
4. 将调研结果汇总输出为 Markdown 表格，包含服务名称、响应耗时、健康状态。
5. 完成后暂停执行，等待我的进一步指令，不要擅自读取其他网段资产。
```
:::

::: details Prompts prácticos
```text
请按规范完成本周发版代码的对比检查与 PR 草稿创建：
1. 切换到工作区代码目录，拉取 origin/main 最新分支。
2. 比对 feature/sso-login 分支与 main 分支的改动差异，列出所有变动的文件列表。
3. 检查是否有硬编码的密钥、密码或私钥文件被提交。如果发现任何形如 'AKIA...' 或 'BEGIN PRIVATE KEY' 的文本，立即中断任务并向我告警。
4. 在本地运行静态检查脚本：npm run lint 和 npm run test。
5. 准备 PR 描述文本草稿，包含变更摘要与测试结果。
6. 注意：严禁直接推送到远程仓库。把 PR 描述保存为 local-pr-draft.md 后向我申请确认。得到明确授权前不得执行 git push。
```
:::

::: details Prompts prácticos
```text
请处理今天未分配的内部支持工单：
1. 打开浏览器，访问内部工单控制台 https://tickets.corp.internal。
2. 过滤出状态为 'New' 且优先级为 'High' 的所有工单。
3. 逐条提取工单的核心问题，按照以下类别打标签：[账号登录]、[权限申请]、[网络故障]。
4. 为每条工单生成标准回复模版，存入草稿区。
5. 涉及权限开通的工单，一律在回复中注明：'需直属主管在 OA 提交审批流，当前仅作信息预审'。
6. 严格要求：所有邮件和系统回复只保留在草稿状态，严禁点击 'Send' 或 'Submit'。生成处理清单供我逐条审查。
```
:::

## Errores y problemas comunes

1. **Omitir comodines multinivel en la pasarela**: el nombre de host es `<vm-id>.<cluster-id>.cursorvm.com`; si solo se configura `*.cursorvm.com`, se quedará bloqueado en el 99%, **es necesario añadir `*.*.cursorvm.com`**.
2. **El proxy activa el almacenamiento en búfer y corta la transmisión**: habilitar Response Buffering en Zscaler provocará desconexiones. **Debe desactivar el almacenamiento en búfer para los dominios de Cursor y permitir el paso transparente de Server-Sent Events**.
3. **Omitir la lista blanca en la directiva de itinerancia**: la imposibilidad de conectarse desde casa se debe a que Zscaler cambia a la directiva Off-Network. Recuerde sincronizar la lista blanca de dominios y las exenciones de TLS con la directiva fuera de la red.
4. **Activar accidentalmente el modo de privacidad heredado**: activar "Modo de privacidad (heredado)" en el backend deshabilitará por completo el bot; desactívelo en la configuración del equipo.
5. **El IdP exige dispositivos conformes**: la máquina virtual Linux en la nube no está gestionada por MDM y no puede ejecutar FastPass. **Agregue una regla de alta prioridad en Okta/Entra ID para Linux (Other Desktop)** y permita el paso utilizando contraseña más autenticación secundaria en el teléfono móvil.
6. **Guardar secretos en texto sin formato en los scripts**: Team Setup es un JSON en texto sin formato. Guarde los tokens en **Team Secrets** y léalos en el script mediante `"$TS_AUTHKEY"`.
7. **No encontrar la aplicación tras instalar con permisos SYSTEM**: el programa se instala en `%LOCALAPPDATA%\Programs`. **Debe ejecutar el comando de instalación `/S` en el contexto del usuario actual**.
8. **Confundir la terminación con la revocación de permisos**: Terminate solo detiene el proceso y conserva el disco; al enviar un mensaje se volverá a iniciar. **Para revocar permisos por completo, cancele la asignación en el IdP o elimine al usuario mediante Manage Group Access**.
9. **Pérdida de secretos entre múltiples equipos**: unirse a más de dos equipos configurados con Team Setup provocará el **rechazo de cualquier Team Secrets**; basta con salir de los equipos sobrantes.
10. **La versión bloqueada cae por debajo del límite mínimo**: si la versión bloqueada con `apt-mark hold` es inferior al límite del ciclo de vida, será bloqueada por "Update required"; simplemente desbloquee y actualice.

## Cómo verificar tras completar la configuración

### Red y pasarela
- Ejecute `curl -v https://api2.cursor.sh |& grep -C1 issuer:` en el equipo de la oficina y verifique que el emisor del certificado sea **Amazon RSA**.
- Ejecute `nslookup test.us9.cursorvm.com` para probar la resolución de nombres de dominio multinivel; cambie a un punto de acceso móvil para conectarse a la computadora en la nube y compruebe que **no haya alertas de certificados**.

### Identidad y SSO
- Inicie sesión en Grok Bot con una cuenta que no sea de desarrollo para confirmar que el SSO de Cursor funcione correctamente al primer intento.
- Inicie sesión en el inicio de sesión único interno a través del navegador del bot usando "contraseña + código de verificación móvil", **sin ventanas emergentes de intercepción de FastPass**, y asegurando que las directivas de cumplimiento en los equipos de oficina sigan funcionando con normalidad.

### Red privada y scripts de entorno
- Confirme en la consola de Tailscale o Cloudflare que las nuevas máquinas se unen automáticamente a la red y tienen las etiquetas correctas.
- Ejecute ping o curl en el terminal hacia los hosts privados para verificar la conectividad; compruebe que los registros de Team Setup no muestren tiempos de espera agotados y que **los secretos aparezcan enmascarados**.

### Cliente y estándares de seguridad
- En Windows, la instalación silenciosa con una cuenta de usuario normal se realiza en `%LOCALAPPDATA%\Programs` y genera accesos directos en el escritorio.
- En "Settings > General > Auto-review", las reglas globales están bloqueadas y no se pueden modificar; al probar la eliminación de archivos en el directorio raíz o la invocación de webhooks no autorizados, el sistema **muestra obligatoriamente una solicitud de aprobación emergente**.

### Ciclo de vida de las computadoras
- El administrador ejecuta **Recreate VMs** en la consola y confirma que los archivos originales y el historial se conservan intactos.
- Una vez completada la tarea masiva, haga clic en **Done** para que el sistema pueda iniciar con normalidad la siguiente ronda.

## Lecturas recomendadas

- Documentación oficial: [Grok Bot para Teams y Enterprise](https://cursor.com/cn/docs/grok-bot/teams)
- Documentación oficial: [Configurar identidad y acceso](https://cursor.com/cn/docs/grok-bot/identity)
- Documentación oficial: [Conectarse a redes privadas](https://cursor.com/cn/docs/grok-bot/private-networks)
- Documentación oficial: [Configurar proxies de inspección TLS](https://cursor.com/cn/docs/grok-bot/proxies)
- Documentación oficial: [Desplegar Grok Bot en su organización](https://cursor.com/cn/docs/grok-bot/deployment)
- Documentación oficial: [Administrar computadoras Grok Bot](https://cursor.com/cn/docs/grok-bot/computers)
- Ayuda oficial: [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans)
- Ayuda oficial: [Bots de equipo](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- Ayuda oficial: [Conectar aplicaciones](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- Guía oficial: [Descripción de la arquitectura de seguridad de Grok Bot](https://cursor.com/cn/docs/grok-bot/security)
