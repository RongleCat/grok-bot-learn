# Capítulo 10 Cota e Custos: Fazendo o Consumo Semanal Durar a Semana Inteira

Ficar sem cota na terça-feira e ser cobrado em centenas de dólares geralmente acontece porque a capacidade computacional roda em falso. **O Bot relê todo o histórico a cada ativação**, inflando para centenas de milhares de tokens em poucas horas.

Para aguentar a semana toda com tranquilidade, faça estas três coisas:
1. Desative o pagamento sob demanda em segundo plano.
2. Reduza o polling de alta frequência e a conversa cruzada entre múltiplos Bots.
3. Enxugue as sessões e evite enviar arquivos grandes no chat.


![Cota e Custos: Fazendo o Consumo Semanal Durar a Semana Inteira](/info/10-usage.png)

## Como funciona a cobrança de cota do Grok Bot? {#扣费原理-额度是怎么被花掉的}

**O Grok Bot é cobrado por tokens consumidos em chamadas. Seu mecanismo central baseia-se em conversas longas de sessão única: a cada resposta ou ativação, todo o contexto do histórico é relido integralmente. O consumo total é igual ao número de ativações multiplicado pelo tamanho do contexto relido a cada vez.**

![Princípio de cobrança: como a cota é consumida](/info/10-usage-s1.png)

O Grok Bot cobra pelos tokens reais utilizados pelo modelo. **Seu mecanismo central baseia-se em conversas longas de sessão única: a cada resposta ou ativação agendada, todo o histórico é relido do início ao fim.**

```
每周总消耗 = Bot 唤醒的总次数 × 每次唤醒时重读的上下文长度
```

Quando a conversa acumula grandes volumes de logs ou páginas web, uma única releitura pode atingir centenas de milhares de tokens; mesmo uma resposta de uma linha será calculada sobre o total.

Para ver a análise da comunidade, consulte [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).

A partir de 12 de outubro de 2026, entrou em vigor o plano unificado The X Subscription, com os seguintes padrões para cada nível:

| Nível do Plano | Preço da Assinatura Individual | Preço por Assento de Equipe | Multiplicador de Cota e Permissões do Grok Bot |
| :--- | :--- | :--- | :--- |
| **Free** | $0 | Não aplicável | Limited, não inclui Bot completo |
| **Plus** | $8/mês ($80/ano) | Não aplicável | Base, **explicitamente sem Grok Bot** |
| **Premium** | $30/mês ($300/ano) | $30/assento/mês | 4x, inclui Grok Bot |
| **Super** | $100/mês ($1000/ano) | $100/assento/mês | 15x, inclui Grok Bot |
| **Ultra** | $200/mês ($2000/ano) | $200/assento/mês | 50x, inclui Grok Bot |

Para detalhes sobre as regras de cota, consulte o [Guia Oficial do Cursor: Planos e Faturamento](https://cursor.com/cn/help/grok-bot/plans). No uso diário, existem algumas restrições rígidas:

- **Os pools de cota não se acumulam**: em caso de múltiplas assinaturas, vigora apenas a que tiver a maior cota semanal, sem soma acumulativa.
- **Escopo do pool compartilhado**: a cota semanal cobre o Grok Bot e o Grok no Cursor, além da versão web, mobile, Imagine e Voice, com redefinição periódica fixa.
- **Modelos de terceiros cobrados separadamente**: chamadas a modelos que não sejam Grok dentro do Cursor são cobradas diretamente sob demanda.
- **Pagamento sob demanda e limite mensal**: após esgotar a cota semanal, ativar o On-demand computará os gastos no limite mensal (Monthly Limit); tarefas que excederem o limite ainda serão concluídas. Se estiver desativado, ele interrompe as respostas aguardando a renovação da cota.

**Foi confirmado oficialmente que não há seletor de modelos (there is no model picker), sendo impossível alternar para um modelo mais básico.** Para controlar os custos, resta apenas reduzir a frequência de ativação, truncar o tamanho do contexto ou desviar a computação pesada para o ambiente externo.

## Quais são as armadilhas comuns de alto consumo de cota no Grok Bot? {#高耗操作清单-坚决避开的六大陷阱}

**É indispensável evitar conversas em grupo com múltiplos Bots, envio direto de imagens e vídeos no chat, polling de alta frequência 24/7, sessões longas levadas até o fim, loops infinitos de repetição desprotegidos e ativação cega de pagamento sob demanda sem definir um limite mensal.**

![Lista de operações de alto consumo: seis armadilhas para evitar com firmeza](/info/10-usage-s2.png)

Fontes de referência: [《4.1 Cota e Custos: Checklist de Economia de Cota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [《Guia Definitivo para Iniciantes de Autonomia Estendida de Cota do Grok Bot (Envie Diretamente para o Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf).

| Operação de Alto Consumo | Por Que Consome Cota | Como Evitar |
| :--- | :--- | :--- |
| Conversas em grupo com múltiplos Bots | Ativações mútuas causam multiplicação e desperdício de tokens | Use um único Bot principal coordenando Subagents, ou converse individualmente |
| Envio direto de imagens e vídeos no chat | Quadros permanecem no histórico e são pagos integralmente a cada releitura | Processe via linha de comando no terminal; o Bot só recebe texto estruturado curto |
| Polling de alta frequência 24/7 | A cada 15 minutos são 672 execuções por semana, quase sempre sem mudanças | Restrinja ao horário comercial ou use scripts de sistema com Webhook |
| Usar a mesma sessão indefinidamente | Após dezenas de turnos, cada releitura consome centenas de milhares de tokens | Uma sessão por tarefa; faça resumos periódicos e redefina com Duplicate |
| Loop infinito de repetição desprotegido | Dezenas de tentativas automáticas consecutivas após erros | **Defina limite rígido de 2 tentativas no prompt**; bloqueie e chame um humano se falhar |
| Ativação cega de pagamento sob demanda | Loops infinitos podem gerar faturas altíssimas da noite para o dia | **Mantenha o On-demand desativado no dia a dia**; se ligar, defina um limite mensal baixo e rigoroso |

## Fluxo de trabalho em quatro etapas para economizar cota: da contenção de danos ao desvio de carga

![Fluxo de trabalho em quatro etapas para economizar cota: da contenção de danos ao desvio de carga](/info/10-usage-s3.png)

### Bloquear o faturamento e fixar a linha de base de segurança
1. Acesse Settings > Usage & Billing para conferir o plano (Premium $30/mês ou Super $100/mês), o consumo e a contagem regressiva; se travar, clique em Stop para encerrar forçadamente.
2. **Durante a depuração, desative Additional Usage / On-demand**; caso ative, vá em cursor.com/dashboard > Gastos > Monthly Limit para definir um limite mensal ($10-$20).
3. Acesse Settings > General > Auto-review e **defina send, post, buy, transfer, delete e permissions como Ask first para aprovação manual**.

### Padronizar sessões e interações
- **Uma sessão por tarefa**: arquive imediatamente ao concluir.
- Salve textos longos e logs em `/workspace/`; retorne apenas a conclusão e o caminho, sendo estritamente proibido colá-los de volta no chat.
- A busca no X é limitada a 30 vezes por minuto e 1.000 vezes por dia (não consome cota semanal); **restrinja o Bot com: "extraia os fatos centrais e responda em 3 a 5 tópicos principais"**.
- Quando a sessão estiver inchada, use Duplicate para redefini-la: primeiro peça ao Bot antigo para redigir um resumo de até 10 linhas, copie e envie para o novo Bot assumir, e oculte o Bot antigo.

### Roteamento e desvio de capacidades
- O Bot principal só deve desmembrar tarefas, despachar e consolidar resultados, sem escrever códigos longos ou converter arquivos grandes.
- **Para programar, utilize o Cursor Cloud Agent** (utiliza a cota do Cursor e não desconta da cota semanal), ou execute em modo headless o Grok Build CLI / Codex CLI na máquina virtual.
- Capturas de tela, áudio e vídeo devem ser processados pela linha de comando no computador em nuvem, ou convertidos em texto usando modelos gratuitos antes de serem entregues ao Bot.

### Reformulação de tarefas agendadas
1. Em Details > Routines, **pause ou exclua as rotinas que passaram a última semana inteira relatando "sem alterações"**.
2. Migre para scripts Linux para realizar polling de baixo custo, disparando um Webhook para acordar o Bot apenas se houver alterações.
3. **Adicione uma instrução de silêncio às rotinas mantidas**: "Se não houver alterações após a verificação, encerre a tarefa imediatamente; é estritamente proibido emitir qualquer texto".

Referência: [《4.1 Cota e Custos: Checklist de Economia de Cota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## Otimização aprofundada de rotinas e polling: diga adeus ao consumo inútil

As rotinas são buracos negros silenciosos de cota; o polling de alta frequência **pode consumir o uso de uma semana inteira em um único dia**.

### Redução de frequência e controle da janela de execução

Primeiro, verifique no cliente se o Timezone do Bot coincide com o horário local. O consumo de diferentes configurações de agendamento é o seguinte:

| Configuração de Agendamento | Execuções Semanais | Casos de Uso Apropriados |
| :--- | :--- | :--- |
| A cada 15 minutos (24/7) | 672 vezes | Esgota a cota com facilidade em 1 ou 2 dias; raramente necessário |
| A cada hora (24/7) | 168 vezes | Monitoramento de falhas em infraestrutura crítica |
| Dias úteis das 9h às 17h, a cada hora | 45 vezes | Acompanhamento de quadros (Kanban), triagem de tickets e e-mails |
| 3 vezes por dia útil | 15 vezes | Triagem da caixa de entrada de manhã/tarde/noite, acompanhamento de progresso |
| 1 vez por semana | 1 vez | Relatórios semanais do setor, resumo de tendências técnicas e arquivamento de documentos |

Para restringir ao horário comercial, utilize o formato cron padrão:

```text
CRON_TZ=Asia/Shanghai 0 9-17 * * 1-5
```

**Esta regra reduz o volume de ativações em 93%**. Executando nos horários cheios das 9:00 às 17:00 nos dias úteis (fuso horário de Shanghai), ela é acionada apenas 45 vezes por semana.

### Apontar para habilidades e aplicar estritamente a regra do silêncio

Os prompts das rotinas devem apontar apenas para habilidades (skills), sem detalhamentos extensos:
- Use comandos de barra para especificar o nome da habilidade e o objeto de verificação
- Defina limiares de avaliação, condições de parada e limite de repetição única
- **Mantenha silêncio absoluto quando não houver mudanças, sem enviar mensagem alguma**

O silêncio total pode mascarar falhas no meio do processo. Para uma solução equilibrada, consulte o [Guia Oficial do Cursor: Rotinas](https://cursor.com/cn/help/grok-bot/routines): mantenha as rotinas de alta frequência em silêncio; para rotinas de baixa frequência, envie um log de heartbeat em linha única diariamente às 18:00 para confirmar a execução normal no último dia.

### Separação em dois papéis: inspeção por script cron do Linux mais ativação via Webhook

Enquanto o Bot está ocioso, o computador em nuvem Linux subjacente continua rodando; **não use LLMs para fazer comparações mecânicas**.
- Papel de verificação: o cron nativo do sistema agenda scripts Python ou Shell para comparação, levando poucos segundos e consumindo zero de cota.
- Papel de decisão: o script detecta alterações e dispara um Webhook para acordar o Bot para avaliação lógica e emissão de relatório.

Etapas de ativação por Webhook e critérios de aceitação:
1. Obtenha o endereço `POST to` e a `key` na área de Webhook da rotina.
2. Envie uma requisição POST para a URL com o cabeçalho `Authorization: Bearer <key>`.
3. Verifique o código de status da resposta: retornar 200 significa que a ativação foi bem-sucedida.

### Casos práticos e armadilhas a evitar

- **铁柱 reformulou 6 rotinas do Bot de Diretor de Marketing**: 4 rotinas de entrega foram mantidas inalteradas; 2 tarefas ociosas que apenas aguardavam respostas e revisões de PR foram substituídas por scripts cron do sistema com Webhook. O script verifica a cada meia hora durante o expediente nos dias úteis, ativando o Bot somente quando há novas alterações.

  **A reformulação levou cerca de 23 minutos e eliminou de 8 a 10 ativações desnecessárias por semana**, aumentando a velocidade de descoberta de novas atualizações para um intervalo de meia hora.

  Fonte do caso: [《Economize um pouco mais da cota do Grok Bot: otimização extrema de tarefas agendadas》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).
- **Craig Hewitt esgotou a cota semanal do Ultra em 24 horas**: assinante do plano Cursor Ultra de $200/mês, ele consumiu toda a cota semanal em um único dia em 23 de agosto de 2026.

  Ele tentou arquivar 10 anos de e-mails antigos no Bot supervisor que usava diariamente; a API puxava o corpo das mensagens e as anexava continuamente à conversa, fazendo o contexto inchar para centenas de milhares de tokens e provocando uma tempestade de releituras completas.

  Fonte do caso: [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).
- **Principais pontos para evitar armadilhas em tarefas pesadas**: **tarefas pontuais de alta carga jamais devem ser executadas no Bot principal usado diariamente**; crie um Bot dedicado ou gere uma réplica via Duplicate; use filtros de regras de e-mail para eliminar spams antes do processamento; e sempre valide processos em lote com 1 ou 2 amostras antes de iniciá-los.

## Controle de chats em grupo e múltiplos Bots: elimine ativações mútuas

**Nunca adicione vários Bots ao mesmo chat em grupo.** Mensagens novas são transmitidas para todos os participantes, fazendo com que cada Bot relpermissione todo o histórico e envie uma resposta. 铁柱 relatou que 4 Bots conversando entre si consumiram rapidamente 25% da cota semanal (não verificado).

A colaboração com múltiplos Bots deve seguir o modelo **hub-and-spoke (radial), proibindo conexões horizontais diretas**.

- Líder único: mantenha apenas um Bot principal como ponto de interação.
- Delegação unidirecional: o Bot principal aciona Subagents ou realiza handoffs pontuais A2A; os subagentes concluem a execução e encerram automaticamente, sem bater papo no grupo.
- Persistência em disco: o fluxo anterior grava os dados em arquivos dentro de `/workspace/`, e o fluxo seguinte os lê diretamente, sem debater no chat.
- Limpeza de ociosos: após confirmar que não há rotinas vinculadas, exclua os Bots inativos prontamente para evitar ativações acidentais.

Fonte: [《4.1 Cota e Custos: Checklist de Economia de Cota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## Como fazer auditoria de uso e contenção emergencial no Grok Bot? {#用量审计与应急机制-守住每周节奏}

**Dedique 15 minutos no dia anterior à renovação semanal para verificar o histórico de rotinas e cobranças; se a cota esgotar e a interface travar, o computador em nuvem Linux subjacente não será destruído, permitindo abrir o terminal diretamente para assumir o código e fazer commit e push manuais.**

### Processo de auditoria semanal de 15 minutos

Recomenda-se dedicar 15 minutos no dia anterior à redefinição semanal para verificar:
1. Abra Settings > Usage & Billing para conferir a porcentagem utilizada. Se o consumo estiver acima do previsto, revise as tarefas dos dias anteriores para identificar a data anômala.
2. Acesse Details > Routines para verificar as últimas 20 execuções (Running, Succeeded ou Failed), identificando rotinas com tentativas de erro ou execuções ociosas frequentes.
3. Para Bots principais com estrela a partir da v0.66.0, **proíba expressamente na descrição que assumam tarefas por conta própria**, evitando que puxem demandas triviais sozinhos.
4. Acesse cursor.com/dashboard, confira o Monthly Limit e as cobranças sob demanda reais para garantir que não haja cobranças indevidas.

### Pontos cegos de monitoramento e como lidar com eles

O sistema não fornece detalhamento de consumo por Bot individual, rotina, conversa ou modelo, e o histórico de 20 execuções também não registra tokens nem valores. **Para testar novos fluxos, use obrigatoriamente o método de controle de variáveis**:
1. Crie ou modifique apenas um Bot ou rotina por vez.
2. Verifique a porcentagem em Usage & Billing antes e depois da execução para comparar o incremento; nunca lance várias rotinas novas simultaneamente.

### Plano de contingência: assumindo o computador em nuvem quando a cota acabar

Quando 100% da cota semanal é consumida e o chat na interface é bloqueado, o computador em nuvem Linux subjacente não é destruído. Você pode assumir o controle abrindo o desktop ou o terminal do sistema pelo cliente:
1. Verifique os códigos e arquivos não entregues no diretório `/workspace/`.
2. Execute manualmente `git commit` e `git push` para enviar ao repositório remoto.
3. Use ferramentas de linha de comando locais no terminal para continuar a depuração — **não é necessário gastar dinheiro comprando uso adicional**.

Fontes: [《4.1 Cota e Custos: Checklist de Economia de Cota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [《Guia Definitivo para Iniciantes de Autonomia Estendida de Cota do Grok Bot (Envie Diretamente para o Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Biblioteca de prompts de economia de cota para enviar diretamente ao Bot

### Prevenção de inchaço de contexto
- Faça o Bot sintetizar e memorizar as regras, **evitando repeti-las no chat**; para Bots compartilhados, insira-as no campo About dos detalhes.
```text
请回顾我们至今的协作流程，执行两项沉淀工作：
1. 把你需要长期遵守的行为边界、汇报格式与约束规矩，提炼成一段不超过 300 字的精简文本，我将直接粘贴到你的描述（Description）中；
2. 把我们刚才已经跑通的标准操作流程，封装为一个可复用的技能（Skill），供后续例程直接调用。
完成提取后直接在对话中给出文本，不要展开多余闲聊。
```
- Force o salvamento de logs brutos e materiais longos em disco, sem colá-los diretamente na conversa.
```text
从现在起执行上下文瘦身规则：
所有抓取的长篇网页、接口调试日志、大批原始数据和阶段性中间产物，一律直接保存为 /workspace/ 目录下的文本文件。在聊天窗口中回复我时，严格只提供核心结论、关键变动要点以及对应的文件绝对路径。严禁将大段原始文本或日志代码贴回对话。
```
- Converta imagens multimodais para análise via linha de comando, **evitando o alto consumo no chat**.
```text
遇到查看多张截图、分析视频画面、逐帧拉片、音频转写或处理长扫描件的任务时，严禁在当前对话框中直接读取原始多模态文件。
你应当在云电脑终端中调用系统已配置的命令行工具（如 Grok Build 或相关转录 CLI）在后台执行，并输出简明的结构化文字摘要；你只需阅读生成的文字结论。如果当前环境无法执行命令行解析，请停下提醒我先在网页端转换成文字后再发给你。
```

### Desvio de tarefas e de código
- Rotinas de monitoramento devem encerrar silenciosamente quando não houver alterações.
```text
请列出当前你名下的全部例行任务（Routines），注明每条任务的触发频率、每周预计运行次数以及没有变化时的处理逻辑。
找出其中运行最频繁、消耗最大的任务，向我提出降低频率的具体建议；同时为所有监控类例程添加硬性约束：执行检查后若目标无实质变动，立刻静默退出，严禁向我发送「一切正常」或「没有新消息」等无有效信息的通报。
```
- Despache tarefas em chats individuais; **é expressamente proibido aos Bots criar grupos e conversar entre si por conta própria**.
```text
严格执行独立单聊工作模式：
只接收并执行我本人下达的直接指令。严禁在没有得到我明确授权的情况下，主动在会话中唤醒、提及或联络其他 Bot 开展群聊协同；如果任务涉及多个专业环节，请将结果写成文件并由我来负责跨 Bot 调度，或者将其派发给云电脑内的后台 CLI 工具独立运行。
```
- Deixe o Bot focado na orquestração; a escrita e depuração de códigos longos devem ser **desviadas para a CLI de segundo plano do Grok Build**.
```text
明确你的角色定位是任务调度主管，核心职责是理解目标、拆解方案、组织逻辑和验收结果。
不要在聊天窗口中直接编写整段的长篇代码，也不要通读整个大型仓库做全量重构。涉及代码编写、项目调试和环境排查的工作，统一在后台调用云电脑内已经授权的 Grok Build 命令行工具执行。执行完毕后，你仅需检查其退出状态码并将最终结论同步给我。
```

### Busca, controle de riscos e transição
- Salve os resultados de buscas na plataforma X em disco; reporte no chat apenas os pontos essenciais sintetizados.
```text
在检索 X 平台的推文、观点或动态时，使用你自带的免费搜索能力。
搜索到的批量推文原文，请直接写入 /workspace/ 下的对应 markdown 文件中保存。在聊天框中向我汇报时，严格限制为 3 到 5 条提炼后的核心事实与推文对应链接，严禁把多条推文的大段原文搬运回聊天中。
```
- Automações e chamadas de API devem ter limite de repetição; **em caso de anomalia, interrompa obrigatoriamente para aprovação humana**.
```text
在执行自动化任务、网络请求或文件排查时，严格执行防死循环规则：
同一操作或相似接口调用的重试上限为 2 次。如果连续 2 次重试均未成功，或者对下一步执行动作存在疑问，立刻中断自动化流程并向我发起提问，详细说明遇到的错误原因，严禁自行无限重试或在后台空转。
```
- Antes de duplicar com Duplicate, faça o Bot antigo organizar um cartão de transição, **estritamente limitado a 10 linhas**.
::: details Busca, controle de riscos e transição
```text
当前会话历史较长，需要进行交接重置。请为我梳理一份 10 行以内的结构化交接总结，严格包含以下五项内容：
1. 你的角色设定与核心职责；
2. 当前正在进行的任务目标；
3. 已经达成的关键结论与做过的核心决定；
4. 下一步必须立刻执行的动作；
5. 新会话需要优先读取的关键文件绝对路径。
输出完毕后不要执行任何新任务，等待我启动新会话。
```
:::
- Preencha o campo de chave com uma chave gratuita do OpenRouter para desviar diretamente tarefas leves.
```text
请协助配置 OpenRouter 免费模型调用环境，严格遵循以下安全执行流程：
1. 在聊天框中调出系统的密钥输入弹窗向我收取 API Key，严禁让我把密钥明文发送在普通对话中；
2. 将获取到的 Key 保存到 ~/.agents/secrets/openrouter.env 文件中，环境变量名指定为 OPENROUTER_API_KEY；
3. 对该密钥文件执行 chmod 600 设置安全权限；
4. 执行全程严禁在终端标准输出或聊天消息中打印该 Key 的明文内容；
5. 使用 curl 调用一个以 :free 结尾的免费模型进行一次最小文本测试，确认调用成功且费用为 0，并将测试结果告诉我。
```

Referência original: [《Guia Definitivo para Iniciantes de Autonomia Estendida de Cota do Grok Bot (Envie Diretamente para o Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Armadilhas comuns

- Clicar em Test em Details > Routines executará o fluxo real na máquina, **descontando cota real a cada vez**.
- As cotas do Cursor e do SuperGrok **não se acumulam**; considera-se apenas a de maior limite semanal, enquanto a outra fica ociosa.
- O faturamento de grok.com e do Grok Bot são independentes; créditos adicionados na versão web **não são dedutíveis nem reembolsáveis**.
- Colar API Key ou Webhook no chat consome tokens e é perigoso; **use obrigatoriamente a janela segura para configurar variáveis de ambiente**.
- Clicar em "Atualizar computador" limpará o cron do Linux, mantendo o `/workspace/`; **será necessário reinstalar o cron após a atualização**.
- O Duplicate descarta a conversa, learned memory e anexos; **é necessário fornecer o contexto manualmente para o novo Bot**.
- O Monthly Limit não encerra os processos ao ser atingido; **tarefas longas continuarão até o fim**, e loops infinitos podem gerar custos extras.

## Como validar após a configuração

1. Acesse Settings > Usage & Billing e cursor.com/dashboard para verificar a fatura, conferir a porcentagem utilizada e a contagem regressiva para renovação, **desativando o Additional Usage ou definindo o Monthly Limit em um valor baixo e seguro**.
2. Peça ao Bot para simular a exclusão de arquivos ou o envio de requisições de rede externas; ele deve obrigatoriamente exibir o card de aprovação **Ask first** e ficar em espera, jamais executando silenciosamente.
3. Verifique a sessão atual e dispare uma busca no X de múltiplos posts: a barra lateral não deve acumular dezenas de turnos de conversas longas; devem ser retornados apenas 3 a 5 pontos de síntese, com os textos longos salvos em `/workspace/`, sem despejar o conteúdo bruto no chat.
4. Acesse Details > Routines e clique em Test em uma rotina de monitoramento sem alterações: ela deve encerrar silenciosamente após a verificação, sem enviar mensagens desnecessárias como "sem atualizações".
5. Peça ao Bot para escrever códigos com dependência de múltiplos arquivos e certifique-se de que ele chame o Grok Build ou o Cloud Agent em segundo plano, **gerando apenas o status final e o resumo de execução**, sem colar telas inteiras de código no chat.

## Leituras complementares

### Capítulos relacionados

- [Capítulo 2 Planos e Assinaturas: Escolha o Nível Certo Primeiro](/part1/02-plans)
- [Capítulo 8 Habilidades e Rotinas: Transformando um Sucesso Pontual em Execução Automática Diária](/part1/08-skills-routines)
- [Capítulo 20 Automação Confiável: Agendamento, Webhook e Gatilhos de Eventos](/part3/20-automation)
- [Capítulo 25 Perguntas Frequentes e Solução de Problemas](/part4/25-faq)

### Documentação oficial e central de ajuda
- [Guia Oficial do Cursor: Planos e Faturamento](https://cursor.com/cn/help/grok-bot/plans)
- [Guia Oficial do Cursor: Rotinas](https://cursor.com/cn/help/grok-bot/routines)

### Práticas da comunidade e resumos de otimização
- [《4.1 Cota e Custos: Checklist de Economia de Cota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)
- [《Gravação do Evento Presencial de Hangzhou: Como Fiz a Cota do Grok Bot Render Mais》](https://jcng5q8n0f3z.feishu.cn/wiki/D04JwEvL7iss9UkDBvLcLuvyncf)
- [《Economize um pouco mais da cota do Grok Bot: otimização extrema de tarefas agendadas》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [《Guia Definitivo para Iniciantes de Autonomia Estendida de Cota do Grok Bot (Envie Diretamente para o Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)
- [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi)
