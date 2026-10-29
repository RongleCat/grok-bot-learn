# Capítulo 1 O que é o Grok Bot: Um colega de IA com computador próprio

As conversas tradicionais pela web não permitem acumular ativos, e **ao fechar o computador a tarefa é interrompida imediatamente**. Diante de chamadas entre múltiplos softwares e inspeções contínuas, as pessoas continuam presas à frente do computador clicando mecanicamente.

Este capítulo aborda quatro conteúdos principais:
- O mecanismo de funcionamento e os limites físicos do computador em nuvem compartilhado;
- Os tipos de tarefas adequados e inadequados para assumir;
- As diferenças de seleção entre ele e outros agentes residentes no mercado;
- **Como escrever uma descrição de cargo em conformidade e estabelecer portões de aprovação humana para evitar abusos de autorização**.

![O que é o Grok Bot: Um colega de IA com computador próprio](/info/01-what-is.png)

## Qual é o mecanismo de funcionamento subjacente do Grok Bot? {#产品机制-环境底座与思考模型拆分}

**O núcleo do Grok Bot é a separação entre a base Linux residente na nuvem e o modelo de pensamento agendado sob demanda, equipado com terminal, navegador e arquivos persistentes; mesmo se o computador for desligado ou fechado, as tarefas em segundo plano continuam rodando no computador em nuvem.**

![Mecanismo do produto: separação entre base de ambiente e modelo de pensamento](/info/01-what-is-s1.png)

A xAI e a Cursor lançaram o Grok Bot em 11 de agosto de 2026, **com o núcleo sendo a separação entre a base de ambiente e o modelo de pensamento**.

- **Base (Harness)**: Residente na nuvem, equipada com terminal Linux, navegador e arquivos persistentes. Ao desligar ou fechar a tampa, as tarefas em segundo plano rodam normalmente.
- **Modelo (Brain)**: Agendado sob demanda, sem vínculo a um modelo único, e não é possível visualizar ou especificar. A partir de 7 de outubro de 2026, as tarefas podem ser roteadas para modelos como Claude Opus 5.5, ou derivar um Cursor Agent para codificação colaborativa.

| Ferramenta | Ambiente de execução | Execução offline e colaboração |
| --- | --- | --- |
| Assistente de chat | Web temporária | Interrompido ao fechar a página, conversa única |
| Agente de linha de comando | Terminal local | Para ao sair, limitado ao repositório local |
| Grok Bot | Computador em nuvem persistente | **Continua rodando mesmo desligado**, transferência de arquivos entre tarefas |

Para detalhes do mecanismo, consulte [《1.1 Grok Bot 是什么：一页看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc).

## Como funciona o isolamento e a tomada de controle no computador em nuvem compartilhado do Grok Bot? {#共享云电脑的物理边界与接管机制}

**Todos os Bots da mesma conta compartilham o computador em nuvem e não podem isolar caminhos ou cookies; as transferências entre tarefas exigem salvar arquivos em /workspace, e em operações como digitar senhas ou pagamentos é possível clicar em Take over para assumir o controle manualmente.**

![Limites físicos e mecanismos de controle no computador em nuvem compartilhado](/info/01-what-is-s2.png)

Todos os Bots da mesma conta compartilham o computador em nuvem. Nos testes reais do plano Heavy foram medidos Xeon de 8 núcleos e 8 threads, 16 GB de RAM, 128 GB de disco (não verificado, prevalece o oficial), e a resolução subiu para 1920×1200 na v0.68.1.

Para especificações, consulte a [Documentação de Computador e Aplicativos do Grok Bot](https://cursor.com/cn/docs/grok-bot/work#the-computer-and-apps).

- Criar um novo Bot **não isola permissões**. Caminhos e estados de login são compartilhados, e todos podem ler cookies.
- A colaboração entre Bots depende da persistência de arquivos em disco. Os chats privados são naturalmente isolados; a passagem de tarefas deve salvar arquivos em `/workspace`.
- Para digitar senhas, autenticação de dois fatores ou pagamentos, clique em Take over para gerenciar; **nunca envie senhas em texto puro no chat**.
- Controlar o computador local requer autorização separada. Isolado do local, ative em Settings → General → Agent → Execution on Local Computer, com pop-up de confirmação na execução.

## Para quais tarefas o Grok Bot é adequado e inadequado? {#适合与不适合的任务类型}

**O Grok Bot é adequado para tarefas de processos fixos, alta frequência de repetição e que exigem chamadas entre ferramentas, como monitoramento de inteligência e reprodução de bugs, mas não é adequado para perguntas e respostas imediatas, codificação local e operações de alto risco sem aprovação humana.**

![Tipos de tarefas adequados e inadequados](/info/01-what-is-s3.png)

### Critérios de filtragem de tarefas
**Para saber se uma tarefa deve ou não ser entregue ao Grok Bot, basta avaliar três critérios de filtragem.**
- Pode ser executada completamente via web, terminal ou API;
- Arquivos intermediários ou relatórios finais podem ser verificados diretamente por humanos;
- Ações sensíveis e de alto risco podem pausar para aguardar aprovação humana via pop-up.

### Tarefas adequadas
**Adequado para tarefas de processos fixos, altamente repetitivas e que exigem chamadas entre ferramentas.**
- Monitoramento de inteligência: Acessar periodicamente sites oficiais fixos para gerar tabelas de resumo.
- Limpeza de leads: Obter contas-alvo no CRM e redigir e-mails de prospecção para revisão com base em informações públicas.
- Reconciliação financeira: Conferir faturas semanalmente, sinalizar notas faltantes e solicitar cobrança.
- Reprodução de bugs: Ler Issues, reproduzir no ambiente de pré-produção e extrair logs e capturas de tela.
- Relatório matinal operacional: Consolidar métricas de estoque diariamente e apontar anomalias.

### Tarefas inadequadas
**Não force tarefas incompatíveis; isso consome à toa a cota semanal e pode sair do controle.**
- Perguntas e respostas imediatas: Consultar erros leva poucos segundos com modelos comuns na web, sem necessidade de computador em nuvem.
- Codificação local: Depuração com breakpoints e conflitos de Git devem ser feitos localmente no Codex CLI ou Claude Code.
- Tarefas rotineiras do dia a dia: Gerenciar calendários sem fontes de dados corporativas soa forçado e inadequado.
- Polling sem verificação incremental: Atualizar incondicionalmente a cada 5 minutos desperdiçará cota de inferência.
- Operações de alto risco: Disparo de e-mails em massa e exclusão de bancos de dados exigem obrigatoriamente um portão de aprovação humana.

Para métodos de planejamento, consulte [《1.2 Grok Bot 和 Muse、Hermes、dots、Cue 怎么选》](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd).

## Comparativo de seleção: Confronto horizontal entre o Grok Bot e os principais agentes residentes

### Formatos de máquina integrada e máquina montada

A escolha de um agente residente depende de preferir praticidade ou gostar de configurar tudo sozinho. **As máquinas integradas prontas para uso** (Grok Bot, Muse) eliminam as dores de cabeça da implantação, mas ficam sujeitas aos limites de cota da plataforma; já os sistemas montados (Hermes) conectados a modelos de código aberto não têm restrições de cotas comerciais, mas qualquer erro de ambiente precisa ser corrigido por você mesmo.

### Características dos principais agentes residentes e comparativo de seleção

| Produto | Base e requisitos | Características e cenários aplicáveis |
| --- | --- | --- |
| Grok Bot | Computador em nuvem Linux compartilhado. A partir de 12/10/2026 aplica-se o plano unificado The X Subscription (Premium $30/mês, Super $100/mês, Ultra $200/mês), **o plano Plus não inclui o Bot**; o cliente v0.70.2 suporta e-mail independente e cartões de conexão | Residente 24/7, suporta rotinas e habilidades, entrega assíncrona de arquivos entre múltiplos Bots e buscas na plataforma X. Ideal para zero manutenção, colaboração em múltiplos cargos e conciliação de inspeções |
| OpenAI dots | Computador em nuvem residente pessoal; ChatGPT Pro e Business Premium incluem o primeiro dot | Baseado no GPT-6 Astra (dots lançado em 29/09/2026), residente em segundo plano conectado a mais de 4.000 aplicativos, focado em acompanhamento diário e tarefas leves |
| Manus Cue | Computador em nuvem independente, em fase de acesso antecipado | Experimentado por 铁柱 em 29/09/2026; inclui nativamente e-mail colaborativo independente, telefone e carteira, executando cadastros e compras de forma autônoma, com altíssima autonomia e riscos operacionais associados |
| Meta Muse | Agente em nuvem gerenciado pela Meta, avaliado pelo Capitão Nuoya como voltado ao ecossistema doméstico | Fortemente integrado à rede social e ao hardware da Meta, adequado para o cotidiano familiar e assistência social |
| Hermes | Servidor local ou privado, código aberto auto-hospedado | Liberdade para trocar modelos de código aberto sem restrições de cotas comerciais. Ideal para pipelines de dados sensíveis locais, **mas requer configurar o ambiente e solucionar erros manualmente** |

Para um comparativo detalhado em posts, consulte [《铁柱推文合集④：社区、生态与竞品对照》](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg).

## Análise de casos práticos típicos

### O Diretor de Inteligência do 金尘马 (Cargo de pesquisa pessoal)

金尘马 (@jinchenma_ai) já escreveu regras de cargo de longo prazo no Description do Edit Profile (este menu foi removido; veja o Capítulo 3 para a prática atual), definindo-o como pesquisador de inteligência. As atribuições estabelecem os cinco elementos: resultados e fontes, restrições e formatos, e pontos de confirmação; pesquisa artigos longos na plataforma X distinguindo postagens de vídeo, indicando dados de visualização, sendo **estritamente proibido inventar dados na ausência de fontes primárias**.

Após corrigir o formato pela primeira vez, instruiu o Bot a consolidar o fluxo como a Skill "Coleta de Inteligência sobre Tutoriais de IA".

Após testar com sucesso um segundo conjunto de entradas, configurou uma Routine para executar relatórios automaticamente todas as manhãs de dias úteis às 8:10; criou um novo "Diretor de Conteúdo" para revisar pautas, com rascunhos salvos em `/workspace/grokbot-demo/`.

**A descrição de cargo consolida regras de longo prazo, enquanto demandas temporárias seguem via mensagens**, desacoplando múltiplos Bots por meio de arquivos gravados no `/workspace`.

Para mais detalhes, consulte [《万字长文｜Grok Bot 从入门到精通｜金尘马》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee).

### A equipe de operações de e-commerce do 金尘马 (Pipeline com divisão de papéis)

A equipe é composta por 4 Bots trabalhando em colaboração. Primeiro, foi criado o "Plantonista de Operações da Loja" para ler tabelas de produtos, estoque e pedidos a fim de enviar o relatório matinal, **estabelecendo uma linha vermelha estrita de somente leitura: estritamente proibido alterar preços e estoque, bem como enviar mensagens ou emitir reembolsos**.

O plantonista original foi promovido a "Supervisor de Operações de E-commerce", desmembrando-se em Especialista de Crescimento de Conteúdo, Analista de Estoque de Produtos e Assistente de Pós-venda de Pedidos, com os dados salvos em `/workspace/ecommerce-ops/日期/`. Ao detectar um produto de alta demanda com estoque para apenas 3 dias, o especialista de conteúdo pausa a promoção, o assistente de pós-venda prepara o roteiro de atraso e o supervisor consolida a lista de tomada de decisão.

Não comece construindo uma equipe enorme imediatamente; **todas as operações envolvendo finanças, estoque e envios externos devem ser bloqueadas com aprovação humana**.

### O Bot administrador de repositório open source do 铁柱 (Inspeção e manutenção automatizadas)

铁柱AGI (@cgnot996) criou um Bot residente para manter a base de conhecimento awesome-grok-bot. O sistema inspeciona periodicamente posts na plataforma X, logs de atualização oficiais e comunidades técnicas, categorizando e indexando novos casos de uso, tutoriais, documentações oficiais e eventos.

Os materiais relevantes já haviam sido incluídos automaticamente antes do anúncio oficial, **ultrapassando 130+ Stars em agosto de 2026 (relato do autor, não verificado)**, além de receber um convite com formulário de inscrição da equipe oficial.

## Primeiros passos: Da ativação ao primeiro Bot dedicado

![Primeiros passos: Da ativação ao primeiro Bot dedicado](/info/01-what-is-s6.png)

### Confirmar o plano de assinatura e instalar o cliente

Escolha o plano de acordo com o plano unificado The X Subscription em vigor a partir de 12 de outubro de 2026:
- **Plano Premium**: $30/mês ($300 faturamento anual), pool de cotas 4x, ideal para o uso pessoal diário inicial.
- **Plano Super**: $100/mês ($1000 faturamento anual), pool de cotas 15x, adequado para pesquisa intensiva e múltiplas rotinas.
- **Plano Ultra**: $200/mês ($2000 faturamento anual), pool de cotas 50x, indicado para equipes de alta frequência.
- **O plano Plus de $8/mês ($80 faturamento anual) não inclui recursos de Bot**, preste muita atenção para não errar. Quem já possui planos pagos do Cursor (Individual ou Team), assinatura do SuperGrok ou assento do Grok Business também pode usar diretamente.

  O aplicativo para desktop suporta macOS, Windows e Linux; em dispositivos móveis suporta iPhone, iPad e Android. Após a instalação, faça login na sua conta.

### Criar um Bot e despachar uma tarefa de teste

1. Na barra lateral, clique em **+** (ou Cmd+N) para criar um Bot, nomeando-o como "Monitor de Inteligência Competitiva". Bots individuais não possuem mais Description; envie as seis linhas abaixo no chat e peça para ele memorizar; para Bots compartilhados, escreva no Description da seção About dos detalhes.
```text
Own: 负责监控目标清单的每周功能更新与定价变动
Sources: Notion 中的关注名单、目标官网 Changelog 页面
Output: 不超过 8 条核心动态，附带日期与原始链接，存入 /workspace/scan.md
Approval: 严禁对外发布任何内容，严禁主动发送任何邮件
Failure: 若目标页面无法打开，在报告中明确标为数据缺失，严禁推测或编造内容
Never: 在源系统可访问时，严禁依赖自身记忆给出概括
```
2. Envie o comando de teste na caixa de diálogo, especificando claramente os cinco elementos: objetivo, fontes, restrições, formato e pontos de confirmação.
```text
调研所附竞品清单中的前 3 个产品官网。
比对它们过去两周内的功能更新与价格调整。
跳过无任何变动的模块。
提取核心变动点，整理成 Markdown 表格，并直接保存到 /workspace/scan.md。
在对话框中仅回复处理状态与保存路径；不要对外发送任何通知，不要擅自更改系统设置。
```
3. **Observe a janela do computador em nuvem à direita**. O Bot acionará automaticamente o navegador em nuvem para extrair a página e salvar o conteúdo no arquivo especificado.

### Configurar aprovações de segurança e rotinas agendadas

1. Acesse Settings → General → Auto-review; **todas as operações de alto risco devem ter o Ask first ativado**.

   Bloqueie estritamente envio de mensagens (`send`), postagens (`post`), cobranças/compras (`buy`), exclusão de arquivos (`delete`, incluindo `/workspace` ou arquivos locais) e alteração de permissões (`permissions`); quando acionadas, um cartão pop-up pausará a execução aguardando sua aprovação manual.
2. Após a tarefa de scraping rodar de forma estável por duas vezes consecutivas, envie a instrução de consolidação no chat.
```text
把刚才已经跑通的竞品页面抓取与格式整理流程保存为一个 Skill，名称叫「竞品动态巡检」。
写清调用条件、所需权限、抓取步骤、异常报错逻辑与产出文件格式。
```
3. Troque por outra URL de concorrente e digite `/` para acionar e testar esta Skill. Após validar, **configure o agendamento da Routine**, definindo para rodar automaticamente toda segunda-feira às 9:00, enviando o resumo no chat atual e salvando o relatório detalhado em `/workspace`.

## Armadilhas comuns

### Arquitetura e segurança

- Ao ver arquiteturas da comunidade com 29 Bots (relato de Melvin Vivas, não verificado), não siga cegamente; Bots redundantes geram confusão e esgotam cotas. **Não crie um segundo Bot antes que o primeiro esteja funcionando perfeitamente no seu posto**.
- Todos os Bots compartilham o computador em nuvem e o sistema de arquivos; scrapers podem ler o `/workspace` e cookies. **O controle de segurança depende exclusivamente do portão de aprovação humana Ask first**.
- Nunca envie usuário e senha na caixa de diálogo. Diante de uma tela de login, **abra a tela à direita e clique no botão Take over para fazer o login manualmente**.

### Recursos e expectativas

- O plano Plus de $8/mês não dá acesso ao Bot; **certifique-se de escolher o plano Premium a partir de $30/mês**.
- Configurar uma Routine com polling a cada 5 ou 10 minutos esgotará o pool de cotas semanais. **Aumente o intervalo entre tarefas agendadas e adicione uma lógica para sair caso não haja atualizações**.
- Não acredite cegamente nos mitos de lucro de Alex Finn ou de redução de custos de 0xkvro (relatos próprios, não verificados); **baseie seu negócio em métricas reais que foram efetivamente validadas**.

## Como validar após a conclusão

1. Clique no Bot na barra lateral para entrar no chat e envie uma mensagem para expandir o **desktop em tempo real de 1920×1200**; acesse Usage & Billing para confirmar se o plano é Premium, Super ou Ultra e se a barra de progresso está normal.
2. O contrato de seis linhas deve conter responsabilidades, fontes de dados, entregáveis, linhas vermelhas de aprovação e contingência para dados ausentes (**restrições rígidas de seis linhas**). Em Bots individuais, envie na conversa para memorizar; em Bots compartilhados, registre no About dos detalhes. Envie um link quebrado para testar: **ele deve relatar a ausência fielmente**, sem inventar dados.
3. Em Settings → General → Auto-review, configure `send`, `post`, `buy`, `delete` e `permissions` como Ask first. Teste o envio de mensagens ou exclusão de arquivos: **deve obrigatoriamente exibir um cartão de aprovação aguardando confirmação humana**.
4. Clique com o botão direito na Routine, selecione Test run e, após a execução bem-sucedida, feche a tampa e encerre o software. No horário agendado, reabra para checar as notificações e acesse o `/workspace` no computador em nuvem, **confirmando que o Markdown ou CSV foi atualizado com o timestamp mais recente**.

## Leituras complementares

### Capítulos relacionados

- [第 5 章 共享云电脑：文件、浏览器与接管](/part1/05-computer)
- [第 6 章 记忆：让 Bot 越用越懂你](/part1/06-memory)
- [第 7 章 连接应用：插件、邮箱与 Secrets](/part1/07-apps)
- [第 11 章 权限、安全与人闸](/part1/11-safety)
- [Grok 和 Grok Bot 有什么区别](/part1/grok-vs-grok-bot)
- [第 2 章 方案与订阅：先选对档位](/part1/02-plans)

### Páginas e documentação oficiais

- [Grok Bot 快速入门指南](https://cursor.com/cn/docs/grok-bot/get-started)
- [使用 Grok Bot：计算机、应用与任务](https://cursor.com/cn/docs/grok-bot/work)
- [Grok Bot 使用场景与典型角色](https://cursor.com/cn/docs/grok-bot/use-cases)
- [面向团队版和企业版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- [Grok Bot 方案与计费说明](https://cursor.com/cn/help/grok-bot/plans)
- [团队 Bot 使用规范](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- [Grok Bot 安全架构与 Auto-review 规则](https://cursor.com/cn/docs/grok-bot/security)

### Práticas da comunidade e comparativos horizontais

- [《1.1 Grok Bot 是什么：一页看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [《1.2 Grok Bot 和 Muse、Hermes、dots、Cue 怎么选》](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd)
- [《铁柱推文合集④：社区、生态与竞品对照》](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg)
- [《万字长文｜Grok Bot 从入门到精通｜金尘马》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
