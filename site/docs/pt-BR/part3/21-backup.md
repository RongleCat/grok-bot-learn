# Capítulo 21 Backup e Restauração: Sem Pânico Mesmo com a Redefinição do Computador

Após a redefinição do computador em nuvem, o ambiente é completamente apagado; digitar `apt-get` e `pip install` de memória facilita o esquecimento de dependências ou variáveis de ambiente, e a memória refinada do Bot não possui um botão de exportação. **A solução é dividir a recuperação de desastres em dois pipelines paralelos.**

1. **Serviços da máquina virtual**: Assumir o controle das dependências do sistema com um registro geral e scripts de restauração automatizados.
2. **Memória do agente**: Um gerenciador de memória dedicado grava personas, regras e fatos dinâmicos em Markdown, enviando-os para um repositório Git privado.

Depois de concluída a configuração, **mesmo que o sistema seja redefinido ou migrado, todos os serviços e memórias podem ser recuperados com o mínimo de intervenção manual**.


![Backup e Restauração: Sem Pânico Mesmo com a Redefinição do Computador](/info/21-backup.png)

## 21.1 Entendendo o Computador em Nuvem: Quais as Diferenças entre Atualização, Recuperação e Redefinição

![21.1 Entendendo o Computador em Nuvem: Quais as Diferenças entre Atualização, Recuperação e Redefinição](/info/21-backup-s1.png)

**Todos os Bots sob a mesma conta compartilham a mesma máquina virtual**, compartilhando o diretório `/workspace` e os processos do sistema. Ferramentas globais instaladas em uma máquina podem ser chamadas por outros Bots; mas se a máquina for redefinida, todos os ambientes de dependência falharão simultaneamente.

Consulte [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

O cliente oferece opções de controle em **Settings** > **Computador** sob **Bot's Computador**. As diferenças entre as três são as seguintes:

| Operação | Mecanismo | Conteúdo retido | Conteúdo perdido |
| :--- | :--- | :--- | :--- |
| **Atualização (Update)** | Atualiza a imagem do ambiente. Dividida em duas categorias: atualização de software e atualização do computador | A atualização de software mantém tudo; a atualização do computador retém robôs, arquivos e informações de login | A atualização de software não perde nada; a atualização do computador remove aplicativos globais e pacotes de software |
| **Recover** | Cria uma nova máquina na imagem mais recente com base nos dados salvos, tentando primeiro conectar-se à máquina antiga para salvar os dados | Robôs, arquivos e informações de login salvos | Aplicativos globais e pacotes de software; se a máquina antiga não puder ser conectada, alterações não sincronizadas serão perdidas |
| **Reset** | Cria diretamente uma nova máquina com base nos dados salvos mais recentes, interrompendo o trabalho em execução | Robôs, arquivos e informações de login salvos | Aplicativos globais e pacotes de software; alterações não sincronizadas serão perdidas |

O histórico de conversas é armazenado na nuvem e não é afetado por redefinições de máquina ou exclusões acidentais de arquivos. No entanto, **pacotes de aplicativos instalados globalmente, `node_modules` e ambientes virtuais Python não são salvos oficialmente** e serão limpos em caso de atualização do computador, Recover ou Reset.

Para mais detalhes, consulte [《Computador do Grok Bot》](https://cursor.com/cn/help/grok-bot/computer-recovery).

Quando a máquina virtual travar ou responder de forma anormal, a solução de problemas deve seguir esta ordem:

1. Exibindo **Reconnecting** ou **Couldn't Reach Grok Bot's Computador**: trata-se de oscilação na rede; aguarde um momento e clique em **Retry**. Os arquivos não são perdidos durante a reconexão; **é estritamente proibido clicar em Reset neste estágio**.
2. Reinicie o cliente. Usuários de Mac devem selecionar **Quit** na barra de menu superior; apenas clicar no "X" vermelho da janela não funciona.
3. Verifique se há atualizações. Acesse **Settings** > **Computador**; se houver atualizações disponíveis, clique primeiro em **Atualizar**. Se for avisado de que o agente não está pausado, espere a tarefa atual terminar antes de clicar.
4. Tente recuperar. Se ainda assim não conectar ou a atualização travar e exibir **Recuperar Computador**, clique em **Recover**. Se for exibido **Update ainda em execução**, selecione **Keep waiting**.
5. Execute **Reset**. Clique em Reset apenas se as quatro etapas anteriores falharem. Se falhar, use **Retry Recover** ou **Retry Reset** para tentar novamente; se continuar gerando erros, entre em contato com o suporte oficial.
6. Lidando com alertas de disco.

   Ao receber **Computer is low on disk space** ou **Computer is critically low on disk space**, não delete arquivos manualmente. Clique em **Go to Disk Saver** na barra lateral para ver as soluções; o sistema não excluirá arquivos sem confirmação.

   Para mais detalhes, consulte [《Computador do Grok Bot》](https://cursor.com/cn/help/grok-bot/computer-recovery).

**O computador em nuvem é apenas um contêiner descartável**; não ajuste o ambiente manualmente. Todo o processo de configuração deve ser feito por scripts, e as configurações e o código-fonte próprio devem ser armazenados em um repositório Git privado externo.

## 21.2 Registro Geral de Serviços da VM e Pipeline de Restauração Automatizada

![21.2 Registro Geral de Serviços da VM e Pipeline de Restauração Automatizada](/info/21-backup-s2.png)

[《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

Como o computador em nuvem não fornece snapshots subjacentes, **tornar o processo de reconstrução um script de um clique é a solução de menor custo**.

### Registro Geral de Serviços e Backup contra Contaminação

Crie um diretório `vm-services/` no repositório privado para colocar a tabela `REGISTRY.md` legível por humanos e o `registry.json` para ser analisado por scripts automatizados.

O registro geral e os backups devem seguir algumas regras rígidas:
- Os campos de registro incluem o ID do serviço, o Bot responsável, o caminho do código, as dependências de instalação (apt/pip/Docker/cron), os comandos de inicialização/parada e verificação de integridade, e se a restauração é obrigatória.
- **Para credenciais, registre apenas caminhos absolutos locais (como `~/.env`), sendo estritamente proibido armazenar texto simples**; destaque separadamente etapas manuais, como escaneamento de QR code e OAuth.
- Scripts próprios devem ser salvos separadamente em `service-src/`, excluindo `venv/`, `node_modules/` e logs; **é obrigatório executar uma varredura com regex para detectar chaves antes do commit**.

### Pipeline de Restauração Automatizada

Escreva sub-scripts individuais para cada serviço em `vm-services/restore/`. **Os scripts devem garantir idempotência**, sem falhar por diretório existente ou conflito de portas se executados duas vezes consecutivas.

O ponto de entrada principal `restore-all.sh` executa as tarefas em série, seguindo a ordem de dependência:
1. **Dependências básicas**: Instalar ferramentas do sistema como `cron`, `ffmpeg` e `yt-dlp`.
2. **Posicionamento do código-fonte**: Copiar os scripts próprios de volta a partir de `service-src/`, pulando arquivos existentes e preenchendo apenas os que faltam.
3. **Ambiente e pacotes**: Criar um ambiente virtual Python e executar `pip install -r requirements.txt`.
4. **Iniciar daemons**: Inicializar processos residentes em segundo plano.
5. **Montar agendamentos**: Restaurar o agendamento unificado do crontab.
6. **Verificação de integridade**: Verificar item por item se estão ativos; **em caso de falha, registrar o log de erro e continuar para o próximo item**, sem travar ou interromper o fluxo.

[《Todas as ferramentas sumiram após a redefinição da máquina virtual do Grok Bot? Tutorial de backup e restauração (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.3 Gerenciador de Memória: Guardando a Memória Central do Bot em um Repositório Privado

![21.3 Gerenciador de Memória: Guardando a Memória Central do Bot em um Repositório Privado](/info/21-backup-s3.png)

Não há um botão oficial para exportação completa de memória, tornando muito fácil perder preferências ao trocar de conta ou migrar de sistema. **Estabelecer um Bot dedicado como "Gerenciador de Memória" para transformar memórias intangíveis em snapshots de texto puro em um repositório Git privado é o caminho mais seguro.**

[《A Grande Evacuação do Grok Bot: Um Plano Completo de Backup para Sistemas de Agentes》](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Camadas de Memória e Princípios de Manutenção

| Camada | Conteúdo incluído | Descrição e permissões |
|---|---|---|
| **Camada compartilhada** | Memória compartilhada da conta, Skills públicas e configurações de plugins | Acessível para leitura por todos os Bots |
| **Camada exclusiva** | Contratos de regras de Description, memórias independentes exclusivas e tarefas Routine | Exclusivo para um único Bot |

- Fatos dinâmicos não devem ser acumulados no contexto a longo prazo; registre apenas o método de acesso e busque na fonte original quando necessário.
- Memórias compartilhadas devem passar por revisão humana ou validação por fluxo de trabalho padronizado para evitar contaminação cruzada.
- **Definições de negócios devem ser escritas na memória, enquanto processos operacionais fixos devem ser consolidados no código de Skills.**

[《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Especificação de Arquivamento e Fluxo de Trabalho

::: details Especificação de arquivamento e fluxo de trabalho
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

O `MEMORY.md` no diretório de cada Bot individual contém três camadas: permissões de identidade, responsabilidades de decisão e snapshot da cena atual.

1. **Enumerar a lista**: Delimitar os Bots principais que precisam de backup persistente.
2. **Agendar e despachar instruções**: Cada Bot lê suas próprias configurações e memórias e, após sintetizá-las, grava-as nos arquivos Markdown correspondentes em `/workspace`.
3. **Coletar, validar e armazenar**: **Fazer o commit unificado após escanear e confirmar que não há Tokens em texto simples**, aplicar uma tag de data (como `tag-2026-10-15`) e enviar (push) para o repositório privado remoto.

**O Bot é responsável pelos snapshots completos, enquanto o Git cuida do rastreamento incremental**. O Bot simplesmente sobrescreve o arquivo por completo a cada vez, deixando as alterações históricas sob responsabilidade do mecanismo do Git, sem a necessidade de calcular diferenças no prompt.

## 21.4 Estudo de Caso Prático: A Grande Evacuação e o Gerenciador de Serviços de 铁柱AGI

### Backup com o Gerenciador de Memória

铁柱AGI (@cgnot996) mantém 21 Bots sob sua gestão. Para evitar a perda de memória em caso de banimento da conta, ele configurou um Bot "Gerenciador de Memória", combinado a um repositório privado no Gitee para arquivamento.

1. **Delimitar os principais**: Dos 21 Bots, 7 principais foram selecionados inicialmente para testes.
2. **Exportação e conferência**: Notificar os 7 Bots para exportar configurações e memórias. **Alguns Bots ficam em silêncio após a exportação; a instrução deve exigir "reportar após a conclusão", enquanto o gerenciador verifica varrendo o diretório `/workspace`**.
3. **Armazenamento e tagueamento**: O primeiro lote de 73 KB foi arquivado no repositório, marcado com a tag `tag 2026-09-10` e aprovado na varredura de chaves.
4. **Estrutura de arquivo único**: Como no "Cyber Xiaowan", o `MEMORY.md` (cerca de 21 KB) armazena identidade e snapshots, e o `agent-spec.md` armazena o bot-id e a descrição.
5. **Ativar agendamento**: Configurar para arquivamento automático periódico.

Ao importar para uma nova conta, a taxa de restauração da memória é de cerca de 80%. **Arquivos locais sem backup, histórico de conversas e estados de login de terceiros não podem ser restaurados**.

Ao migrar para Hermes ou OpenClaw, basta colocar o `MEMORY.md` no diretório de memória e alterar a description do `agent-spec.md` para o prompt do sistema para que funcione.

[《A Grande Evacuação do Grok Bot: Um Plano Completo de Backup para Sistemas de Agentes》](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Gerenciador de Serviços da Máquina Virtual

O travamento e a consequente redefinição do computador em nuvem resultam na perda total das ferramentas. O autor registrou o ledger geral de reconstrução no diretório `vm-services` do repositório `grok-bot-memory` no Gitee.

1. **Registro no ledger**: Até 10/10/2026, foram registrados 20 itens de 10 Bots (4 residentes/daemons, 14 ferramentas sob demanda e 2 itens de chaves), dos quais 18 foram marcados como "restauração obrigatória".
2. **Classificação dos serviços**: Os serviços residentes incluem serviços de scraping, encapsulamento de API do Muse, além de motor de e-mail e túnel de saída; ferramentas sob demanda (ffmpeg, Chrome, etc.) registram apenas o comando de instalação; Metaso e TikHub registram apenas os caminhos das chaves.
3. **Backup limpo do código-fonte**: Cerca de 5,1 MB de código-fonte próprio, excluindo chaves, logs e fluxos de estado.
4. **Restauração encadeada**: O gerenciador mantém o diretório `restore/` e o `restore-all.sh`. **Em condições normais, o gerenciador não executa nada por conta própria; ele aguarda instruções humanas para iniciar os serviços de acordo com as dependências e entrega uma lista de verificação de aceitação**.

[《Todas as ferramentas sumiram após a redefinição da máquina virtual do Grok Bot? Tutorial de backup e restauração (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.5 Segurança de Credenciais e Ponto de Controle de Aprovação Humana: Entregue a Tela, Não a Senha

**Vários Bots compartilham o disco e as sessões de navegador da máquina virtual; criar novos Bots não isola dados confidenciais de forma alguma.** Se algo for escrito em texto simples em scripts ou conversas, outros Bots ou logs externos poderão lê-lo.

[《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Credenciais: Mantenha Apenas Caminhos, Nunca Texto Simples

- Tokens e chaves privadas são armazenados no `~/.env` (ignorado pelo Git) ou em um diretório global de chaves.
- No `REGISTRY.md`, no `registry.json` e nos arquivos de memória, **sempre que houver credenciais envolvidas, registre apenas o caminho absoluto no disco**.
- É estritamente proibido enviar senhas na caixa de diálogo; antes de fazer o push, é obrigatório executar uma varredura com regex para sanitização.

### Entregue a Tela, Não a Senha

1. Se o Bot encontrar pop-ups de 2FA, escaneamento de QR code ou verificação de dispositivo, ele pausará imediatamente e notificará você para assumir o controle.
2. Você abre o computador em nuvem em tela cheia no cliente e digita a senha ou escaneia o QR code você mesmo.
3. Uma vez concluído, devolva o controle; **o Bot herda os cookies da sessão e continua em execução, sem jamais tocar na senha em texto simples**.

### Configurar Ask-first para Operações de Alto Risco

- Operações irreversíveis, como postar, efetuar pagamentos, excluir dados ou alterar o ambiente subjacente, devem abrir um pop-up e aguardar aprovação humana. A versão v0.70.2 otimizou essa lógica de confirmação.
- **A autoridade autônoma do Bot limita-se a leitura, busca pública e leitura/escrita interna no `/workspace`**; em caso de conflito de regras, o Ask-first tem prioridade.

## 21.6 Três Conjuntos de Prompts Prontos para Uso

Abaixo estão três conjuntos de prompts comprovados na prática; basta copiá-los e enviá-los ao Bot correspondente para implantar e usar.

### Prompt 1: Configurar o "Gerenciador de Serviços da Máquina Virtual" para o Computador em Nuvem

Crie um Bot "Gerenciador de Serviços da Máquina Virtual" e **cole nas configurações**:

::: details Prompt 1: Configurar o "Gerenciador de Serviços da Máquina Virtual" para o computador em nuvem
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

### Prompt 2: Fazer o Bot Executar uma Restauração Completa Após a Redefinição do Computador

Configure o **token de acesso Git**, substitua o conteúdo entre parênteses e envie ao Bot.

::: details Prompt 2: Fazer o Bot executar uma restauração completa após a redefinição do computador
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

### Prompt 3: Instrução de Arquivamento Periódico para o Gerenciador de Memória

**Envie isto para Routine ou arquivamento manual:**

::: details Prompt 3: Instrução de arquivamento periódico para o Gerenciador de Memória
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

## 21.7 Armadilhas Comuns

1. Quando exibir Reconnecting, **não clique em Reset**; trata-se apenas de oscilação na rede ou manutenção, e clicar nisso sobrescreverá dados não salvos com um snapshot antigo.
2. Compartilhar a autorização do Codex em vários dispositivos fará com que eles desconectem uns aos outros; configure subcontas independentes ou credenciais fixas.
3. Tarefas agendadas devem ser centralizadas em um arquivo de configuração do crontab e adicionadas ao Git para evitar omissões na redefinição da máquina.
4. O ledger geral de serviços deve se basear em comandos práticos reais; se o Docker não estiver instalado no ambiente, o script de restauração poderá travar.
5. Os Bots frequentemente realizam exportações silenciosamente; o gerenciador deve verificar ativamente o disco, e as instruções devem impor estritamente: "é obrigatório reportar após escrever".
6. **O repositório de backup deve ser configurado como privado e incluir varredura com regex** para evitar que Tokens sejam enviados a repositórios públicos via git push.

## 21.8 Como Fazer a Validação e Aceitação

### Serviços e Scripts
1. Reconciliação: Compare com `vm-services/REGISTRY.md`, use `ps aux` para verificar processos, e `netstat` ou `ss` para verificar portas; **os caminhos não devem ser registrados a mais nem omitidos**.
2. Teste inicial: Execute individualmente `restore-<服务名>.sh`, observando se pode ser executado repetidamente sem erros.
3. Ensaio completo: Faça um clone em um diretório temporário e execute `bash restore/restore-all.sh`, **garantindo que todos os itens de "restauração obrigatória" sejam aprovados** e que as etapas que exigem intervenção humana estejam listadas.

### Repositório e Memória
1. Verificar a estrutura: Acesse `bots/` na interface web; cada Bot deve ter arquivos `agent-spec.md` e `MEMORY.md` independentes.
2. Amostragem: Abra o `MEMORY.md` e confirme se as três camadas ("profile de identidade", "decisões históricas e responsabilidades" e "snapshot da cena atual") estão completas, sem modelos vazios ou caracteres corrompidos.
3. Busca por segredos: Faça uma busca global por `sk-`, `Bearer` ou `password`; **mantenha apenas caminhos absolutos locais para credenciais, sendo estritamente proibidos Tokens em texto simples**.

## Leituras Complementares

- Guias de uso oficiais e páginas de suporte:
  - [《Computador do Grok Bot》](https://cursor.com/cn/help/grok-bot/computer-recovery)
  - [《Armazenamento Seguro de Informações Confidenciais》](https://cursor.com/cn/help/grok-bot/secrets)
  - [《Obter Ajuda》](https://cursor.com/cn/help/grok-bot/get-help)
  - [《Guia de Uso do Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to)
- Artigos de referência prática da comunidade:
  - 铁柱AGI @cgnot996: [《Todas as ferramentas sumiram após a redefinição da máquina virtual do Grok Bot? Tutorial de backup e restauração (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)
  - 铁柱AGI @cgnot996: [《A Grande Evacuação do Grok Bot: Um Plano Completo de Backup para Sistemas de Agentes》](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)
  - Organização integrada da base de conhecimento: [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
