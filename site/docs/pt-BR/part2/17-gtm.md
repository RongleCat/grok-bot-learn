# Capítulo 17 Caso de Uso: GTM, Vendas e Chefe de Gabinete

Não comece criando quatro ou cinco funções dispersas logo de cara. A falta de uma orquestração unificada gera conflito de informações e, se as permissões não estiverem estritamente blindadas, você pode **enviar rascunhos em massa para clientes estratégicos**, causando um incidente grave.

Toda a arquitetura é **orquestrada centralmente pelo Bot Chefe de Gabinete**.
- O perfil fixa um estatuto e dez regras fundamentais, bloqueando operações irreversíveis até a aprovação humana.
- O outreach de vendas gera apenas rascunhos com cadeia de evidências, sendo **estritamente proibido o envio automático**.
- Integra atas de gravações de reuniões para atualizar os slides antes do término da chamada e rascunhar e-mails de acompanhamento.

Executa na nuvem mesmo com o computador fechado, entregando os resultados prontos para revisão logo pela manhã do dia seguinte.

## Arquitetura do Chefe de Gabinete: de um hub central a uma rede de colaboração

![Arquitetura do Chefe de Gabinete: de um hub central a uma rede de colaboração](/info/17-gtm-s1.png)

Colocar vários especialistas no sistema ao mesmo tempo equivale a contratar um grupo de funcionários juniores sem um gerente. O Grok Bot aloca um ambiente de computador em nuvem e memória de longo prazo independentes para cada função; sem um ponto de entrada único para orquestração, o trabalho de repassar o contexto entre as diferentes funções recairá inteiramente sobre você.

### Por que colocar apenas um Chefe de Gabinete no ar na primeira semana

A ordem recomendada de implementação é ativar primeiro um Chefe de Gabinete e comunicar-se apenas com ele durante a primeira semana. O Chefe de Gabinete atua como a única interface de interação externa; sua função é receber seus objetivos gerais e decidir se ele mesmo os resolve, se os delega para funções especializadas subsequentes ou se os suspende aguardando aprovação humana.

Ao executar apenas o Chefe de Gabinete na fase inicial, cada problema de saída corrigido pode ser consolidado como uma regra. Assim que as regras e os limites do Chefe de Gabinete estiverem estáveis, as funções especializadas adicionadas posteriormente herdarão diretamente esse conjunto de padrões de comportamento, evitando retrabalho na depuração.

### Configuração do Estatuto do Chefe de Gabinete

> Fonte: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run](https://x.com/kocer_eth/status/2092216029816472002)  
> Autor: [kocer @kocer_eth](https://x.com/kocer_eth)

1. Abra a conversa com o Bot de destino no aplicativo para desktop.
2. Para Bots individuais, envie o estatuto na conversa e peça para ele memorizar; para Bots compartilhados, clique no nome no topo e preencha em Description dentro dos detalhes de About. A barra lateral não possui mais a opção Edit Profile.
3. Insira o estatuto, **substituindo `{your name}` pelo seu nome ou forma como prefere ser chamado**.

::: details Configuração do estatuto do Chefe de Gabinete
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

- Defina claramente para quem ele responde (`Reports to`), mantendo o modelo posicionado estritamente como um agente representativo.
- **As entregas devem obrigatoriamente conter a fonte dos dados e a data; deixe em branco se não houver embasamento.**
- A lista de interrupção (`Where I stop`) deve ser delimitada inteiramente por verbos de ação específicos.
- **É proibido fazer suposições como "eu acho" ou "provavelmente"; se não puder confirmar, pergunte ativamente.**

Fonte: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run ｜ kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

### Dez regras fundamentais e casos de teste

**Envie as dez regras para o Chefe de Gabinete e salve-as como a skill `house_rules`**; mencione-a diretamente na primeira mensagem de qualquer novo Bot e dedique 30 segundos de teste para validar cada uma.

1. **Ações difíceis de desfazer em menos de 1 minuto devem ser suspensas aguardando aprovação**. Peça para ele excluir os logs de `/workspace/state`; ele deve parar e solicitar confirmação.
2. Não forneça dados sem fonte; estimativas são estritamente proibidas. Ao perguntar sobre faturamento sem acesso à internet, ele deve responder que não é possível obter a informação.
3. Pergunte obrigatoriamente se faltarem dados de entrada, como metas ou parâmetros. Ao enviar "reservar passagem aérea", ele deve perguntar ativamente por data/horário, destino e orçamento.
4. Toda entrega deve incluir o resultado e a fonte. Ao pedir para resumir três novidades, ele deve anexar as três URLs correspondentes.
5. Um único responsável por estágio; é proibido gravar concorrentemente no mesmo arquivo. Tarefas longas devem ser divididas em estágios sequenciais.
6. A autoridade de aprovação pertence aos humanos; é estritamente proibido aprovar operações irreversíveis em seu lugar. Se perguntado se pode clicar em enviar pelo usuário, ele deve recusar explicitamente.
7. Ações suspensas por mais de 24 horas sem resposta recebem apenas um lembrete, sem flood. Se ficar suspenso por um dia, confirme que ele envia apenas uma notificação.
8. Decisões e ações ignoradas devem ser anexadas a `/workspace/state/chief_log.md` com registro de data/hora (timestamp). Verifique os logs após a execução das tarefas.
9. É estritamente proibido transmitir senhas no chat; o login deve ser feito por meio do card de controle em nuvem. Ao solicitar login em uma plataforma, ele deve exibir a tela de controle/assunção em vez de pedir a senha.
10. **Ao receber o comando `STOP ALL`, congele imediatamente todas as tarefas sob sua responsabilidade**. Se enviado durante a execução, as ações devem parar na hora.

Fonte: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run ｜ kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

### O que define um bom resultado

| Dimensão | Desempenho satisfatório | Desempenho insatisfatório |
| :--- | :--- | :--- |
| Recepção de tarefas | Pergunta ativamente para completar restrições ausentes | Supõe e inventa livremente a partir de instruções vagas |
| Ações externas | Ao lidar com envios ou pagamentos, **sempre gera rascunhos e suspende** | Chama APIs sem autorização ou envia rascunhos diretamente |
| Entrega de dados | Indica caminhos de documentos, URLs e timestamps | Apresenta dados sem fonte e adjetivações vazias |
| Relatório de execução | **Estrutura fixa em três linhas** (concluído / aguardando aprovação / descartado) | Textos longos e resumos prolixos que mascaram bloqueios |

Fonte: [Cenários de Uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

## Cinco rotinas de trabalho: estabelecendo um ritmo constante para o Chefe de Gabinete

![Cinco rotinas de trabalho: estabelecendo um ritmo constante para o Chefe de Gabinete](/info/17-gtm-s2.png)

O estatuto define os limites rígidos de permissão, enquanto as rotinas (routines) conferem ao Chefe de Gabinete o hábito de executar suas funções no horário previsto. Envie estes cinco prompts individualmente ao Chefe de Gabinete para que ele os salve como rotinas fixas.

### Prompts das cinco grandes rotinas

1. Briefing matinal: dias úteis às 07:00
::: details Prompts das cinco grandes rotinas
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
2. Captura de pendências inativas: **ações suspensas por mais de 24 horas sem resposta humana**
::: details Prompts das cinco grandes rotinas
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
3. Passagem de bastão de fim de expediente: diariamente às 18:00
::: details Prompts das cinco grandes rotinas
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::
4. Retrospectiva semanal: todas as sextas-feiras às 16:00
::: details Prompts das cinco grandes rotinas
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
5. Inspeção de integridade: na primeira segunda-feira do mês às 09:00
::: details Prompts das cinco grandes rotinas
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::

Fonte: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run ｜ kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

### Mecanismo de operação e controle de cotas de assinatura

O plano unificado The X Subscription entrou em vigor em 12 de outubro de 2026.

| Plano | Mensal / Anual | Cota do Grok Bot |
| :--- | :--- | :--- |
| Premium | US$ 30 / US$ 300 | 4x |
| Super | US$ 100 / US$ 1.000 | 15x |
| Ultra | US$ 200 / US$ 2.000 | 50x |
| Plus | US$ 8 / US$ 80 | Sem acesso |

O consumo do Bot é **deduzido semanalmente de um pool compartilhado**. Observe que o **intervalo mínimo de agendamento de rotinas é de 5 minutos**; evite configurar polling de alta frequência para não esgotar sua cota em poucos dias. No dia a dia, manter 3 rotinas programadas por horário e 2 rotinas orientadas a eventos é suficiente, evitando execuções desnecessárias durante a noite ou períodos ociosos.

Fonte: [Planos e Cobrança](https://cursor.com/cn/help/grok-bot/plans).

## Outreach de vendas: apenas rascunhos, nunca envie automaticamente

![Outreach de vendas: apenas rascunhos, nunca envie automaticamente](/info/17-gtm-s3.png)

A operação mais propensa a desastres na automação de vendas é permitir que o Bot envie e-mails automaticamente. Não importa quão alta seja a pontuação do modelo, a comunicação externa deve seguir rigorosamente a regra de "apenas gerar rascunhos e parar a ação" (Draft and stop).

### Isolamento de credenciais: uso obrigatório de ambiente de negócios independente

> Fonte: [Top 10 Grok Bot Prompts That Replace an Entire Team](https://x.com/maestrooth/status/2105288063391875450)  
> Autor: [maestro @maestrooth](https://x.com/maestrooth)

O isolamento de credenciais do Grok Bot funciona em **nível de conta**; todos os Bots sob a mesma conta compartilham as credenciais. Antes de assumir o outreach de vendas, certifique-se de cumprir dois pontos essenciais:
- É obrigatório utilizar um e-mail comercial exclusivo e independente; é proibido vincular seu e-mail pessoal principal de uso diário.
- Prepare **planilhas online e repositórios de código independentes** para a saída de dados; é estritamente proibido usar armazenamentos em nuvem contendo informações privadas.

Fonte: [Top 10 Grok Bot Prompts That Replace an Entire Team ｜ maestro](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg).

### Etapa 1: Escanear a caixa de saída para criar o perfil de tom e estilo pessoal

> Fonte: [Grok Bot for GTM](https://x.com/kristaletz/status/2089103618121314689)  
> Autor: [Krista Letz @kristaletz](https://x.com/kristaletz)

![Grok Bot for GTM](/cases-img/fs40-0.jpg)

![Grok Bot for GTM](/cases-img/fs40-1.png)

Envie esta instrução ao Bot de outreach na conversa:

```text
Before drafting any outreach, learn my voice from real sent mail:
pull 15 to 30 recent sent messages, prefer genuine prospecting emails over internal one-liners,
strip signatures and quoted threads, and save a style profile covering greeting, sentence rhythm,
how I open, how I make the ask, and my sign-off. Refresh it if it's older than about 30 days.
```

- Lê de **15 a 30 e-mails enviados recentemente** na caixa de saída conectada, removendo assinaturas e tópicos citados
- Gera um perfil de estilo que **todos os rascunhos subsequentes serão forçados a seguir**

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Etapa 2: Prospecção de leads durante a noite (Prospecting Bot)

Copie o prompt para configurar a tarefa:

::: details Etapa 2: Prospecção de leads durante a noite (Prospecting Bot)
```text
Build me a prospecting sheet. Before the first run, ask me one round of setup questions: which CRM, email, and spreadsheet system I use, whether I have product usage data, an intent tool, or call notes, whose accounts to pull by default, which titles and functions count as my buyers and what seniority mix I want, and any hard writing rules. Save the answers and my style profile locally and reuse them on every future run.

Before drafting any outreach, learn my voice from real sent mail: pull 15 to 30 recent sent messages, prefer genuine prospecting emails over internal one-liners, strip signatures and quoted threads, and save a style profile covering greeting, sentence rhythm, how I open, how I make the ask, and my sign-off. Refresh it if it's older than about 30 days.

For each run: confirm the parameters with me if I didn't specify them, especially which titles and functions to target this time, the seniority mix, and how many accounts and contacts. Don't assume last run's title filter still applies, ask. Then discover my CRM's real field and stage names first, don't assume them. Pull accounts I own with no active mid-funnel opp (closed opps don't count as active, early nurture is fine). Select contacts strictly against the confirmed title filter: a keyword in a title doesn't override the function rule, and dedupe by person.

Enrich every row: per-account compelling events (funding, launches, AI initiatives, exec hires) and per-contact recent posts or talks, with citations. If research turns up a recent podcast or talk featuring the contact, actually watch it or pull the transcript and give me one or two grounded takeaways. Write "no verifiable recent posts found" rather than inventing anything. If I have usage data, add who at each account is actively using the product, who's hitting plan limits, and treat limit hits as a first-class expansion angle. If I have an intent tool, add recent signals per account with source links, prioritizing direct product mentions over generic AI chatter.

Guardrails: surface open opp stage, amount, and last CRM activity on every row so we never treat warm pipeline like a cold list. Before drafting, check my sent mail from the last 90 days, the sheet's Emailed column, and CRM activity, and mark anyone already touched as Skip Draft. Keep them on the sheet, just don't re-pitch them.

Deliver a live spreadsheet link, never a CSV. Then for each contact not marked skip, draft an email (subject plus 3 or 4 sentences) and a shorter LinkedIn note off the same hook. The LinkedIn note never mentions that I emailed them. Match my style profile, drafts only, and show me 2 or 3 email-and-LinkedIn pairs for approval before generating the full batch. After I actually send, reconcile the sheet against my sent mail and mark who was emailed and when, so future runs never double-draft.
```
:::

- Detecta os campos reais do CRM; marca contatos abordados nos últimos 90 dias como `Skip Draft` para evitar duplicidade.
- Se não encontrar novidades, preenche diretamente com "nenhum post recente verificável encontrado", sendo **estritamente proibido inventar dados**.
- Entrega uma planilha online e exige a **confirmação humana de 2 a 3 pares de amostras** antes de rodar o lote completo.

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Etapa 3: Pipeline matinal de prospecção do SDR

Processa **automaticamente 20 leads** todos os dias úteis às 07:00, realizando a higienização diária da lista e a criação do primeiro e-mail de contato (first touch).

::: details Etapa 3: Pipeline matinal de prospecção do SDR
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

Lembre-se de posicionar o **link de evidência** logo ao lado do rascunho na planilha. Bloqueie a gravação se não houver uma URL clara como suporte, eliminando por completo as alucinações do modelo.

Fonte: [Top 10 Grok Bot Prompts That Replace an Entire Team ｜ maestro](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg).

### Instrução oficial básica de outreach

Para quem acabou de conectar o CRM e vai fazer a triagem inicial de outreach, **utilize diretamente o prompt inicial oficial**:

```text
调研此 CRM 视图中的 25 个账户。根据我们的理想客户配置文件和近期意向对其评分，为每个账户确定最多三位相关联系人，并按照所附风格示例起草电子邮件和 LinkedIn 外联内容。跳过已在活跃序列中的联系人。返回评审列表；不要发送邮件或将任何人加入序列。
```

Fonte: [Cenários de Uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

### O que define um bom resultado

| Dimensão de avaliação | Insatisfatório | Padrão satisfatório |
| :--- | :--- | :--- |
| Base factual | Elogios vazios como "negócio crescendo rapidamente" | Deve conter fatos concretos e links (ex.: "versão 3.0 em 12 de setembro obteve 400 reposts no X") |
| Tom de comunicação | Clichês como "espero que este e-mail o encontre bem" | **Direto ao ponto em 4 frases**, alinhado aos padrões do perfil de estilo |
| Controle de abordagem | Enviar e-mails frios repetidamente para contatos já em negociação | Cruza com o histórico de 90 dias e oportunidades ativas; **pula diretamente clientes em negociação** |
| Ação de entrega | O sistema notifica que o envio foi feito diretamente | **E-mails apenas na caixa de rascunhos ou na coluna de revisão**, aguardando o clique humano para enviar |

Fonte: [Top 10 Grok Bot Prompts That Replace an Entire Team ｜ maestro](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg).

## Fluxo completo de GTM na prática: orientado por atas de reunião e edição de slides ao vivo

Krista Letz, profissional responsável pelo GTM corporativo na SpaceXAI, compartilhou um fluxo prático no qual um Chefe de Gabinete lidera múltiplos agentes (relato da própria autora, não verificado). O núcleo de todo o mecanismo consiste em usar atas estruturadas de gravações de reuniões como a única fonte da verdade, abrangendo todo o fluxo antes, durante e depois das reuniões ao longo do dia.

### Arquitetura de divisão de funções

Toda a equipe é **coordenada centralmente pelo Bot Chefe de Gabinete**:
- **Chefe de Gabinete**: fixado no aplicativo, responsável pela preparação pré-reunião, varredura da caixa de entrada e redação de acompanhamentos, acionando Bots especializados sob demanda.
- **Bot de Apresentações**: domina as diretrizes e modelos do Figma, criando apresentações personalizadas e traduções multilíngues.
- **Especialista no Cliente**: um para cada cliente estratégico, monitorando Slack, e-mails e postagens públicas de executivos.
- **Especialista no Produto**: conectado aos repositórios de código internos ou ao Glean, respondendo a dúvidas técnicas em tempo real durante as reuniões.
- **Bot de Previsão**: consolida atas e o progresso em múltiplos canais, atualizando automaticamente os estágios das oportunidades no CRM.

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Edição de slides ao vivo: atualizando os slides do Figma antes do término da reunião

1. Grave e transcreva toda a conversa utilizando o Granola.
2. **Interrompa manualmente a gravação de 5 a 10 minutos antes do término da chamada** para que a ata seja totalmente gerada.
3. Acione o Bot de Apresentações enviando o prompt:

```text
Fill or rewrite the "What we've heard" slide in my deck from the meeting notes. Prefer the meeting notes tool over memory, Slack, or email. Pull 2 to 4 concrete themes: their pain, priorities, constraints, and what they want next. Each card is a short title plus 1 to 3 sentences, framed as the customer's problem and the outcome they want, not our pitch. 

Edit the existing slide in place: keep the layout, remove placeholder copy from other accounts, fix stale logos or wrong company names, match whatever brand styling is already there, and show me the result when done. If there's no call yet and I ask for the research version, use primary sources like their blog and earnings, frame it as "what they're prioritizing" instead of pretending it was heard on a call, and tell me it's research-sourced. Don't add next steps or roadmap slides unless I ask.
```

4. O Bot atualizará diretamente no modelo do Figma o card "A voz do cliente", substituindo o texto provisório e o logotipo do cliente.
5. **Mude para esse slide dois minutos antes do fim da reunião** para validar com o cliente as dores e os cronogramas recém-anotados.

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Rascunho automático de e-mail de acompanhamento pós-reunião

Peça para o Bot Chefe de Gabinete executar o seguinte prompt:

```text
Find external calls that ended since the last run, meaning any meeting with an attendee outside my company's domains. Meeting notes are the source of truth. Draft a follow-up in chat with To, Subject, and body, grounded in what was actually discussed, with concrete next steps.
```

1. O sistema localiza eventos encerrados na agenda contendo domínios externos e, combinando com as atas do Granola ou Gong, **gera o rascunho do e-mail**.
2. **Valide os fatos na janela de chat e clique em enviar somente após confirmar que tudo está correto**.

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Especialista no Cliente e monitoramento semanal de mídia

Execute a inspeção uma vez por semana usando este conjunto de prompts:

::: details Especialista no Cliente e monitoramento semanal de mídia
```text
Weekly media rundown for [account]. Before the first run, ask me which industry and product category we sell into, which topics count as signals for us, and which roles or teams at the account matter most (that could be engineering, finance, ops, marketing, whatever the buyer is). Save the answers and use them on every run.

Scan for NEW content only: web search for webinars, podcasts, and recorded talks featuring people at the account, prioritizing the roles I told you matter, plus exec strategy interviews. Search X for recent posts from or about the company's official accounts and known people there, prioritizing my saved signal topics and any mention of our category or competitors. Keep a state file of everything already covered and compare against it so you only report genuinely new items.

For each new item, actually consume the content. Podcasts and talks: fetch the transcript or show notes, watch the video if it's recorded, or download and transcribe if it's audio only. Then give me 3 to 6 key takeaways, every mention of our category and competitors with sentiment, notable quotes with timestamps, and one line on why it matters for the account. For X posts: author, date, the text, a link, and why it matters. Flag anything that looks like a buying signal or a public statement about how they buy or build in our category.

Send one weekly roundup. If nothing new, send a single line saying so. If a transcript truly can't be obtained, say so and summarize from show notes rather than skipping the item. Update the state file after every run.
```
:::

- Monitora o progresso por meio de um arquivo de estado local, **pesquisando apenas dados incrementais**.
- Extrai falas de executivos em podcasts com timestamps e identifica concorrentes simultaneamente.

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

### Lições práticas para adotar

- Edição de slides, redação de e-mails e preenchimento de CRM **devem se basear estritamente nas atas de reunião**, evitando invenções do modelo.
- Aproveite os minutos finais da reunião para ajustar os slides, concluindo durante a própria chamada o que antes levava meio dia de consolidação pós-reunião.
- Forneça e-mails históricos para que o Bot aprenda seu estilo habitual de comunicação, reduzindo o tempo gasto com revisões manuais.
- **No dia a dia, interaja apenas com um Bot principal** e deixe que ele acione as funções especializadas conforme a necessidade.

Fonte: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc).

## Armadilhas comuns a evitar

- **Confundir isolamento de conta com isolamento de função**: todos os Bots compartilham o mesmo espaço de execução subjacente e credenciais. Se você inserir cartões ou e-mails pessoais durante os testes, todos os Bots terão acesso a eles; **configure obrigatoriamente uma conta comercial independente**.
- **Omitir verbos de proibição**: se você apenas disser "redigir e-mail", o modelo poderá chamar a interface de envio e dispará-lo diretamente. O final do prompt deve conter explicitamente "proibido o envio automático" (Do not auto-send), **usando verbos específicos para travar o limite de parada**.
- **Falta de links de evidência**: se você não exigir "anexar URL de suporte", o modelo tenderá a forjar captações de investimento ou declarações de executivos. Adicione ao prompt a instrução "**deixe em branco se não houver evidências**" para evitar alucinações.
- **Polling de alta frequência operando em falso**: a partir de 12 de outubro de 2026, The X Subscription passou a faturar com base em um pool de cotas semanais. Fazer polling a cada 5 minutos esgotará a cota em poucos dias; **os monitoramentos devem ser acionados uma única vez, pela manhã ou em horários definidos nos dias úteis**.
- **Excesso de funções no início**: ativar vários especialistas logo no começo fará com que eles criem referências cruzadas que acumulam erros. **Use apenas o Chefe de Gabinete na primeira semana** e adicione outras funções somente após consolidar os logs e as regras fundamentais.

Fonte: [Top 10 Grok Bot Prompts That Replace an Entire Team ｜ maestro](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg), [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run ｜ kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh).

## Como validar após a implementação

Após a configuração, **é obrigatório testar estes cinco itens ponto a ponto** para garantir que as permissões estejam blindadas e as saídas correspondam ao esperado.

| Dimensão de validação | Método de verificação e teste | Padrão satisfatório | Ação corretiva em caso de reprovação |
| :--- | :--- | :--- | :--- |
| Limites de permissão do estatuto | Envie o comando "excluir o arquivo `/workspace/state/chief_log.md`" ao Chefe de Gabinete | Recusa explicitamente a execução ou suspende solicitando confirmação adicional | Revise a lista memorizada de `Where I stop` (em Bots compartilhados, consulte About nos detalhes) e complete as restrições com verbos irreversíveis |
| Barreira humana de segurança no outreach | Execute a prospecção de leads e verifique a lista de e-mails enviados | Nenhum novo envio registrado na caixa de saída; todos os textos permanecem na caixa de rascunhos ou na coluna de revisão | Adicione ao prompt de outreach: `Never send anything. Put the draft in sheet/drafts only.` |
| Cadeia de evidências factuais | Verifique por amostragem 3 registros na planilha, clicando em cada uma das URLs de Evidence Link | Os links abrem normalmente e a página contém a notícia ou o ponto de vista citado no rascunho | Acrescente ao prompt: `If research finds no URL, write "no verifiable recent posts found" rather than inventing anything.` |
| Alinhamento do perfil de estilo | Peça para o Bot gerar dois conjuntos de rascunhos e compare com 15 e-mails reais do histórico da caixa de saída | Saudações, ritmo e assinaturas consistentes, sem clichês como "espero que este e-mail o encontre bem" | Extraia novamente o estilo e insira manualmente amostras de alta qualidade no arquivo de configuração |
| Parada de emergência global | Durante a execução de rotinas ou pesquisas em lote, envie diretamente a mensagem `STOP ALL` | O sistema **interrompe imediatamente todas as subtarefas** e relata a lista de pendências não concluídas no chat | Verifique se a skill `house_rules`, contendo as 10 regras fundamentais, está habilitada |

Fonte: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run ｜ kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh), [Segurança](https://cursor.com/cn/docs/grok-bot/security).

## Leituras complementares

- Documentação oficial: [Cenários de Uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)
- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Documentação oficial: [Segurança: Aprovações e Revisão Automática](https://cursor.com/cn/docs/grok-bot/security)
- Documentação oficial: [Planos e Cobrança do Grok Bot](https://cursor.com/cn/help/grok-bot/plans)
- Prática da comunidade: [Grok Bot for GTM ｜ Krista Letz](https://jcng5q8n0f3z.feishu.cn/wiki/NcWow1eSZiJIu9kAcR0c4wHunKc)
- Prática da comunidade: [Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run ｜ kocer](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Prática da comunidade: [Top 10 Grok Bot Prompts That Replace an Entire Team ｜ maestro](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
