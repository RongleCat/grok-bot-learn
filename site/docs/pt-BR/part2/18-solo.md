# Capítulo 18 Estudo de Caso: Empresa de Uma Pessoa e Equipe de IA

**Todos os Bots sob a mesma conta compartilham o mesmo computador na nuvem**, com navegador, sistema de arquivos e terminal integrados.

Criar mais de uma dúzia de Bots de uma vez e entregar todas as contas facilmente leva a armadilhas.
- Páginas web externas seguindo caminhos errados, sobrescrevendo dados silenciosamente
- Aprovações frequentes acionadas no meio da noite, deixando você exausto de revisar

Ao alinhar os limites de funções, o isolamento de credenciais e as linhas vermelhas de aprovação, é possível **evoluir da configuração do primeiro funcionário de IA para o gerenciamento de 29 Agents**.

## O Primeiro Funcionário de IA: Definindo Funções e Permissões Como em um Processo de Contratação

![O primeiro funcionário de IA: Definindo funções e permissões como em um processo de contratação](/info/18-solo-s1.png)

Tratar um Bot como uma ferramenta ou como um funcionário depende se você está escrevendo um prompt único ou definindo responsabilidades de uma função. Um prompt único cuida apenas de uma tarefa imediata e, assim que a janela é fechada, o contexto desaparece. Uma descrição de função é um arquivo permanente que determina o limite comportamental e o modelo de raciocínio desse Bot ao lidar com tarefas diárias.

### Definição de Funções e Testes de Admissão

**Não conceda permissões irreversíveis no início**, comece com tarefas rotineiras, de alta frequência e fáceis de reverter.

Antes de deixar o Bot começar a operar, execute dois testes de admissão para solucionar problemas com antecedência.
1. **Teste de responsabilidade em uma frase**: explique com clareza em uma única frase o que será entregue. Inserir quatro ou cinco verbos não relacionados equivale a fazer uma pessoa executar o trabalho de três, tornando impossível localizar a causa raiz caso ocorra um erro.
2. **Simulação textual (Trial in text)**: leva menos de dois minutos; primeiro reporte as etapas, as URLs que planeja acessar e os julgamentos duvidosos.

A descrição da função é dividida em cinco campos para delimitar claramente as fronteiras.
- Owns: Entrega de entregáveis fixos.
- Inputs: Canais com permissão de leitura.
- May: Operações que podem ser realizadas de forma autônoma.
- Must ask before: Ações de alto risco, como gastar dinheiro ou alterar configurações, **devem aguardar aprovação humana**.
- Done when: Checklist de aceitação para verificação objetiva.

```text
先不要执行任何实际操作。请逐步向我推演你的完整执行方案：
1. 列出你准备依次打开的工具、网址与调用的插件。
2. 列出你在过程中需要做出的业务判断。
3. 标出你目前信息不足、存在疑虑或拿不准的决策点。
推演完毕后等待我的指令，严禁自行操作。
```

::: details Definição de função e teste de admissão
```text
岗位名称：收件箱管理员（Inbox Manager）
Owns：
每天上午梳理工作邮箱，归档垃圾邮件与订阅通讯，起草客户咨询的回复草稿，标出需要我决策的紧急邮件。
Inputs：
仅限于 Gmail 中收件箱的未读邮件与公司提供的常见问题回复模版。
May：
阅读邮件、按标签分类、打上处理标记、撰写回复草稿、归档无回复价值的宣传邮件。
Must ask before：
严禁直接点击发送任何邮件；严禁归档来自财务、法务或房东的邮件；如果邮件涉及转账、退款、重置密码或修改凭证，立即停下向我确认。
Done when：
工作日上午 9:00 前收件箱所有未读邮件分类完毕；生成的草稿不超过四句话，语气平实直接，不使用任何客套空话；所有待办事项单独列出截止日期。遇到不确定如何处理的邮件，保持未读并挂起询问，严禁自行猜测意图。
```
:::

A definição de função é completamente diferente de um prompt temporário.

| Dimensão | Prompt temporário | Definição de função |
|---|---|---|
| **Objetivo e formato** | Diálogo único, focado em uma ação pontual | Configuração de longo prazo, entregando resultados de negócio |
| **Fronteiras e permissões** | Instruções verbais facilitam excesso de autoridade; erros exigem reexecução | Ações reversíveis tratadas autonomamente; irreversíveis aguardam aprovação, com portão humano estrito |

### Período de Experiência de Três Execuções e Escada de Promoção

> Fonte: [Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> Autor: [distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

Assim que um novo Bot começar a funcionar, **nunca o deixe rodando em segundo plano sem supervisão logo de início**; primeiro teste-o de acordo com a "regra das três execuções" de distort.

1. 1ª vez (observação completa): fique de olho na tela acompanhando cada operação e anote instruções mal interpretadas, perda de contexto e adivinhações.
2. 2ª vez (correção de regras): use uma tarefa de dificuldade equivalente sem lembrar os erros anteriores. Concentre-se em verificar se as mudanças nas regras de função e permissões surtiram efeito, sem alterar os resultados por ele.
3. 3ª vez (teste prático autônomo): não interfira em nenhum momento; intervenha apenas em aprovações ou quando atingir o limite de tentativas, verificando o nível de conclusão, quantidade de intervenções, tempo gasto e cota consumida.

**Após passar nos três testes, entra-se na escada de promoção**, dividida em cinco níveis de permissão.

| Nível | Mecanismo | Limite |
| :--- | :--- | :--- |
| Level 0 | Apenas observação | Não altera nenhum dado |
| Level 1 | Apenas preparação | Trabalho reversível como pesquisa, resumo e formatação |
| Level 2 | Aprovação humana | Etapas críticas suspensas aguardando confirmação |
| Level 3 | Execução independente | Execução agendada ou por gatilho, gerando relatórios periódicos com cadeia de evidências |
| Level 4 | Colaboração multi-Bot | Atua como nó de distribuição e controle de qualidade |

Para subir para o próximo nível, é obrigatório atender a quatro **indicadores rígidos**:
- 5 execuções reais consecutivas sem falhas
- Todas as etapas de validação aprovadas
- Nenhum efeito colateral não resolvido
- Mecanismo de rollback validado e disponível

Para práticas de referência, consulte [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) e [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg).

## Do Zero a uma Empresa em Funcionamento: Chefe de Gabinete e Orquestração de Equipe Dedicada

Ao usar o Grok Bot sozinho para construir um sistema completo de operação de negócios, o beco sem saída mais comum é sobrecarregar um único Bot com habilidades demais. Um Bot encarregado simultaneamente de leads de vendas, redação de conteúdo, conciliação contábil e modificação de código terá sua janela de contexto rapidamente preenchida por inúmeras preferências irrelevantes, o que não só confunde o contexto de negócios, mas também acelera o consumo da cota.

### Arquitetura de Chefe de Gabinete e Divisão de Departamentos

Para montar a equipe, comece criando um Bot Chefe de Gabinete (Chief of Staff). No dia a dia, você **interage apenas com o Chefe de Gabinete**, cabendo a ele desmembrar tarefas, coordenar funções dedicadas e consolidar as entregas.

::: details Arquitetura de Chefe de Gabinete e divisão de departamentos
```text
你是一人公司的幕僚长（Chief of Staff），也是我日常沟通的唯一入口。
你的核心职责：
1. 接收我的业务目标，拆解为明确的工作阶段，派发给对应的专职 Bot（调研、内容、代码、运维）。
2. 在群聊中调度各岗位接力，跟踪各任务交付状态。
3. 检查专职 Bot 提交的产物是否符合完成标准，核对数据来源与执行录屏。
4. 每天晚上汇总团队进展，用不超过五行文字向我汇报核心结果、阻塞问题与需要我决策的审批项。
行为底线：
若无任何新进展或异常，保持静默；严禁越权代替专职 Bot 编写业务交付内容；严禁绕过人工审批直接执行外发、扣款或修改生产环境。
```
:::

- Bot de Pesquisa: afirmações devem conter data e URL; pontos duvidosos devem ser marcados proativamente, sem invenções forçadas.
- Bot de Conteúdo: formata de acordo com modelos; **é estritamente proibido publicar externamente de forma direta**.
- Bot de Vendas: salva todos os e-mails de prospecção na pasta de rascunhos, aguardando aprovação humana antes do envio.
- Bot Técnico: ao abrir PRs no GitHub, deve incluir capturas de tela comprovando a aprovação nos testes.
- Bot Financeiro: ajustes envolvendo fundos devem ser listados separadamente aguardando confirmação.

::: details Arquitetura de Chefe de Gabinete e divisão de departamentos
```text
团队总体目标：
在两周内针对新上线的知识库产品，完成竞品定价调研，产出一份对比简报，并根据简报结构生成 3 篇官网更新草稿。

协作规则：
1. 调研 Bot 先行检索 5 家竞品公开定价，生成包含引用网址的 Markdown 表格。
2. 调研完成后在群内移交给内容 Bot，内容 Bot 根据数据起草 3 篇文案，放入指定 Notion 页面。
3. 幕僚长全程跟进看板状态，若遇到数据缺失，要求责任 Bot 重新抓取或报错，不得擅自编造。
4. 全流程中所有涉及对外发布的操作全部挂起，等待我在看板中勾选通过。
```
:::

| Arquitetura | Individual generalista | Pipeline com Chefe de Gabinete |
|---|---|---|
| Colaboração | Memória mista e difícil de rastrear | **Memória independente por função**, atribuição precisa de responsabilidades |

### Revisão de Cadeia de Evidências e Transferência de Confiança em Quatro Semanas

> Fonte: [From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> Autor: [NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**Para poder fechar o computador com tranquilidade, o pré-requisito é ver as evidências (Show the tape).** A entrega do Bot deve vir acompanhada de três comprovantes:

- Gravação da tela de operação ou registros de chamadas: exibindo a trajetória completa da página web ou a sequência de chamadas de ferramentas.
- Fonte original dos dados e números: é proibida qualquer citação sem fonte.
- Explicação de itens ignorados devido a erros e conclusões especulativas.

**A confiança é transferida gradualmente ao longo de quatro semanas:**

1. 1ª semana (Fase de rascunho): o Bot apenas redige; o humano lê tudo e executa manualmente.
2. 2ª semana (Fase de aprovação): o Bot para em etapas críticas; o humano apenas confere a ação e aprova.
3. 3ª semana (Fase de escalonamento de anomalias): tarefas de baixo risco rodam de forma autônoma; pop-ups pedem ajuda somente diante de anomalias ou ações fora dos limites.
4. 4ª semana (Fase de inspeção de rotinas): operação totalmente autônoma seguindo rotinas; no fim de semana revisam-se apenas relatórios de auditoria.

Para práticas relacionadas, consulte [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) e [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Na Prática com Empresa de Uma Pessoa: Limites e Operação Independente em um Único Computador na Nuvem

### Limites Físicos

**Todos os Bots da mesma conta compartilham um único computador**, usando os mesmos diretórios e sessões. O aviso oficial é claro: não trate os Bots como limites de isolamento; Prompts não impedem injeção, e comandos executados por engano podem vazar Cookies e Sessions.

No dia a dia, mantenha três regras:
- Não faça login no internet banking principal nem em repositórios essenciais; não armazene drives em nuvem confidenciais.
- Use apenas subcontas com privilégios mínimos em plataformas externas.
- O login externo deve usar Handoff: o humano insere a senha e o Bot herda apenas a Session.

### Automação de Sistemas Sem API

**Sistemas sem API dependem de habilidades de computador para clicar e preencher formulários**; quatro categorias de trabalho são ideais para delegar primeiro:
- Pesquisa para aquisição de clientes: varrer diretórios de comunidades e redigir e-mails.
- Acompanhamento de atendimento de pedidos: conferir itens fora de estoque e acompanhar remessas atrasadas.
- Agendamento de conteúdo: inserir textos em rascunhos.
- Manutenção de código: investigar erros em sites independentes e gerar patches.

::: details Automação de sistemas sem API
```text
岗位名称：供应链履约跟踪员（Supplier Logistics Bot）
Owns：
每天上午 10:00 登录供应商门户，核对昨天未发货订单状态，提取物流单号，更新至运营表格。
Inputs：
供应商订货后台会话、本地待处理订单表格。
May：
在供应商后台查询订单状态、下载发货清单 CSV、更新本地表格对应列的运单号与发货时间。
Must ask before：
严禁点击「重新下单」或「取消订单」；严禁修改收货地址；若供应商后台提示账户欠款或商品缺货，停止处理并立即向我报警。
Done when：
所有处理过的运单在表格中均标注状态与回填时间；遇到后台页面改版导致按钮无法识别时，截取当前屏幕报错并退出，不得盲目重试。
```
:::

### Limiares e Pontuação

> Fonte: [One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> Autor: [ZER @zerqfer](https://x.com/zerqfer)

Adicione novos Bots somente quando a **revisão humana cair de forma estável para menos de 15 minutos por dia**, evitando sobrecarga. Preencha um scorecard mensalmente para prevenir a degradação silenciosa.

::: details Limiares e pontuação
```text
Bot 月度运行评分卡
评估周期：2026 年 10 月
岗位名称：[例如：订单跟进助理]
1. 实际工时节省：本月相比纯手工操作，实际节省了约多少小时？
2. 人工介入程度：产出草稿中，需要人工手动大幅修改的比例是多少（低于 10% 算达标）？
3. 信任度变化趋势：对该岗位的自主执行信任度处于上升、持平还是下滑？
4. 异常与回滚记录：本月出现过几次页面识别错误或越权报警？
5. 处置结论：[保留继续运行 / 降级为人工审批执行 / 彻底停用删除]
```
:::

Consulte [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg).

## Sistema de Entrega de AI Agency: Pipeline de Entregas Mensais e Portão Humano de Controle de Qualidade

![Sistema de entrega de AI Agency: Pipeline de entregas mensais e portão humano de controle de qualidade](/info/18-solo-s4.png)

Para agências de IA (AI Agency) que entregam para múltiplos clientes, a principal dificuldade reside na estabilidade de qualidade e no controle dos custos de cota sob concorrência de vários clientes.

O autor da comunidade maestro compartilhou a arquitetura de sistema que permite a uma única pessoa atender 5 clientes sob regime de retainer e manter a operação mensal dos negócios (relato do próprio autor da comunidade maestro afirmando faturar US$ 18 mil por mês e atender 5 clientes; não verificado).

### Os "Três Testes de Admissão" do Menu de Serviços

Não aceite projetos totalmente customizados a ponto de virar terceirização manual; **os serviços só entram no menu de entrega automatizada após passar por três crivos**:

1. O Brief pode ser estruturado em uma checklist.
2. O entregável possui critérios de aceitação objetivos de terceiros.
3. **Já foi entregue puramente à mão pelo menos 10 vezes antes**. Sem fazer pelo menos 10 vezes, você não conhecerá as linhas vermelhas, e repassar para os agentes só gerará conteúdo inútil.

Serviços qualificados incluem comparar 40 documentos com 500K de contexto para elaborar relatórios de pesquisa, redigir artigos em lote com base em amostras de tom de voz (Voice File) ou construir dashboards e ferramentas leves de scraping.

### Roteamento de Modelos e Bloqueio de Penhasco de Cobrança em 195.000 Tokens

Aloque os modelos de acordo com a tarefa, sem direcionar tudo para os topos de linha.
- Grok 4.1 Fast: contexto de 2M, executa limpeza e triagem inicial.
- Grok Build 0.1: responsável por 80% dos materiais de desenvolvimento.
- Grok 4.6: 500K, executa Agents de longo alcance e raciocínio.

**Entradas acima de 200.000 Tokens dobram diretamente a taxa de cobrança**. O gateway deve **fixar de forma rígida no código um limite de 195.000 Tokens**, emitindo erro para truncar ou podar caso exceda.

### Revisor Somente Leitura Independente e Portão Humano com Três Tentativas

> Fonte: [How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> Autor: [maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

Bots de produção tendem a achar seus próprios resultados coerentes, mascarando facilmente falhas de prompts. **A auditoria deve ser isolada em um circuito independente somente leitura**.

- Contexto independente: insira apenas o Brief original, especificações do cliente e o produto final, sem fornecer o raciocínio intermediário.
- Estritamente somente leitura: **ao encontrar falhas, reporte apenas FAIL e nunca reescreva**, evitando correções secretas que ocultem problemas.
- Análise crítica adversária: foque estritamente em falhas graves; números sem suporte de dados são sumariamente reprovados.

::: details Revisor somente leitura independente e portão humano com três tentativas
```text
# 独立审查者审核准则（reviewer.md）
你是一名独立质量审查员，负责评估一份并非由你生产的交付产物。
你的唯一任务是找出交付物不符合客户要求的地方。你绝不需要去赞美它的优点。

输入物料：
原始需求 Brief、服务核对清单、客户品牌声音规范文件、最终交付草稿。
你未被提供、也严禁索取生产 Bot 的思考草稿。

审查规则（按顺序严格执行）：
1. 逐条核对需求 Brief 中的清单项。指出任何未被完全覆盖的要点。
2. 检查全文，严禁残留任何占位符文字、TODO 标记或括号说明文本。
3. 全文中的每一个具体数字、引文、统计百分比与人名，必须能在客户资料库中找到对应出处。发现任何未注明来源的数字，必须直接判定为 FAIL。
4. 语言风格是否符合客户过往已批准作品的语气标准。

输出格式：
第一行必须且只能输出一个词：PASS 或 FAIL。
如果判定为 FAIL，按以下格式列出所有缺陷：[清单条款] - [出现位置] - [具体问题及修正要求]。第一行后严禁输出任何空洞的总结段落。
若因上下文缺少凭据导致无法核验某一项，直接判定为 FAIL。
```
:::

```text
单任务自动化生产循环规则：
1. 生产 Bot 基于需求与声音规范生成第 1 版草稿。
2. 独立审核 Bot 执行审查。若返回 PASS，记录日志并进入待交付队列。
3. 若返回 FAIL，系统将审查不通过的具体原因拼接入下一轮 Brief，由生产 Bot 进行针对性修复重试。
4. 重试上限（MAX_ATTEMPTS）严格设定为 3 次。
5. 若连续 3 次均无法通过审查，系统立即终止自动重试，触发报警将原始 Brief、草稿与审查报错完整推送到人工桌面由人工兜底接管。
```

**O limite de tentativas na transição é de no máximo 3 vezes**, evitando loops infinitos que gerem contas astronômicas de Tokens. Se a máquina tentar três vezes e ainda não atingir o padrão, isso indica conflito de requisitos, exigindo intervenção humana para avaliação.

Consulte [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf).

## 29 Agents na Prática: Como Expandir Suavemente de um Operador Solo para uma Legião

![29 Agents na prática: Como expandir suavemente de um operador solo para uma legião](/info/18-solo-s5.png)

Quando você estiver familiarizado com a configuração de um único funcionário e com o ciclo fechado de controle de qualidade de dois Bots, as necessidades do negócio o impulsionarão naturalmente a expandir a equipe.

O autor da comunidade Melvin Vivas registrou na íntegra como expandiu o Grok Bot passo a passo até 29 agentes dedicados (relato do próprio autor da comunidade Melvin Vivas afirmando possuir 29 Bots; não verificado).

### Distribuição de Funções e Evolução Progressiva de 29 Agents

**Todos esses 29 Bots surgiram conforme a demanda**: ao deparar com tarefas repetitivas no cotidiano, criava-se uma função dedicada; com o aumento de funções, a Chefe de Gabinete Emma assumiu a gestão centralizada. Os negócios são divididos em sete grandes blocos:

- Centro de coordenação: Emma é responsável pelo controle geral e distribuição de tarefas.
- P&D técnico: o CTO cuida da arquitetura; o **Coder mobiliza o Cursor para escrever código automaticamente, abrir PRs e corrigir erros**, sem precisar abrir o editor local em momento algum.
- Pesquisa de ponta: monitora 24 horas as novidades open-source na plataforma X e gera briefings.
- Matriz de conteúdo: responsável pela criação de textos e análises pós-publicação para diversos canais.
- Desenvolvimento de negócios: prospecção de oportunidades de negócios e leads de parceria.
- Operações e segurança: responsável por e-mails, backups e auditorias de segurança.
- Desenvolvimento pessoal: lida com check-ins, acompanhamento de mercado e fundamentação de decisões.

### Pipeline de Colaboração Multi-Agent: Exemplo da Conversão de Protótipo Técnico em Conteúdo

Os Bots passam o bastão entre si utilizando o computador compartilhado na nuvem e referências de sessão.

::: details Pipeline de colaboração multi-Agent: exemplo da conversão de protótipo técnico em conteúdo
```text
端到端跨团队协同案例：
1. 【情报捕获】：X 调研员监控到某大模型最新发布，抓取官方文档与代码仓库地址，整理为技术要点。
2. 【任务调度】：幕僚长 Emma 捕获该报告，根据设定规则判定该模型具备测试价值，自动将任务下发给技术团队。
3. 【工程交付】：编码员 Coder 接收技术说明，调起 Cursor Cloud coding agent 在云端编写 Google Colab 演示笔记本，推送到 GitHub 仓库并自动创建 Pull Request。
4. 【排错闭环】：执行测试出现依赖包版本冲突，终端 Traceback 自动返回 Coder，Coder 修复代码再次提交 PR 通过测试。
5. 【内容物料转译】：PR 合并后，Emma 将成功代码仓库与技术参数推送给内容创作团队，YouTube 脚本助手与 X 内容经理在半小时内完成多平台发布草稿，存入指定待审目录。
6. 【人闸闭环】：创始人全程不介入代码编写与格式排版，仅在最后核验 Colab 实际运行效果，并点击确认对外发布推文。
```
:::

**Você não precisa abrir 29 janelas uma a uma para fazer alterações**; uma única instrução transmitida pelo coordenador sincroniza tudo em segundos.

### Os Cinco Sinais para Divisão de Funções e o Método de Sete Etapas para Automação

Quando metas de avaliação, ferramentas chamadas, estilos de trabalho, limites de aprovação (rascunhos e comunicação externa jamais devem se misturar) ou ciclos de agendamento divergirem, é obrigatório **dividir em Bots independentes**.

1. Envie metas, fontes de dados, formatos e limites de parada para o Bot e faça com que ele memorize; para Bots compartilhados, registre no About de detalhes.
2. Selecione uma tarefa real e controlada para uma única execução.
3. Otimize manualmente até dispensar inspeção.
4. Consolide em uma Skill reutilizável.
5. Troque por novos dados para testar a capacidade de generalização.
6. **Defina o limite de tentativas e alertas de dados ausentes antes de ativar a Routine**.
7. Para envio de mensagens, pagamentos ou alterações, vincule compulsoriamente o portão humano de Require Approval.

| Fase | Escala | Arquitetura e gargalos |
| :-- | :-- | :-- |
| 1 Operador solo | 1 Bot | Ciclo fechado completo validado por portão humano; exige monitoramento constante |
| 2 Grupo | 2-3 Bots | Separação entre produção e auditoria; manutenção diária reduzida para 15 minutos |
| 3 Chefe de Gabinete | 4-6 Bots | Distribuição e kanban; **evite que o Chefe de Gabinete faça trabalhos triviais** |
| 4 Legião | 10-30 Bots | Standups em múltiplas frentes; poda periódica de rotinas ineficazes |

### Sistema de Kanban e Mecanismo de Reunião Matinal

> Fonte: [How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> Autor: [Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Se tiver mais de 5 Bots, pare de usar múltiplas janelas de chat; é humanamente impossível acompanhar. **A colaboração multi-Bot depende principalmente de duas coisas: kanban e inspeções periódicas**:

- **Kanban de status compartilhado**: não deixe tarefas espalhadas no histórico de chat; centralize-as no Notion ou em um kanban de banco de dados, definindo cinco estados: `Todo`, `Working`, `Blocked`, `Ready for Review` e `Done`.

  Ao deparar com erros desconhecidos ou falta de permissões, o Bot altera o status diretamente para `Blocked` e chama um humano; no dia a dia, basta observar o fluxo dos cartões.
- **Inspeções periódicas e conciliação**: configure no máximo 50 Routines por Bot, com frequência máxima de execução a cada 5 minutos.

  **Às 3h00 da madrugada, executa-se a checagem automática de links quebrados no código e tamanho de pacotes; às 5h00, o Bot coordenador (como Jenny) confere um a um os Playbooks dos Bots dedicados**, o que previne eficazmente o esquecimento do modelo com o passar do tempo.

```text
全体专职 Bot，开始进行本周团队回顾审计。请各岗位汇报：
1. 本周你实际执行了多少次任务，其中失败或异常的中断有多少次？
2. 在执行过程中，有哪些步骤存在推测行为、跳过行为或由于数据缺失强行拼凑的情况？
3. 有哪些挂起的审批事项我一直没有回应？有哪些生成的物料我从来没有打开查看过？
4. 请指出：在当前的工作流中，你发现哪两个 Bot 存在职责重叠或重复工作？
5. 给出客观建议：为了节省整体用量额度，我们下周最应该裁撤哪一个无效的 Routine 或岗位？
```

Para práticas relacionadas, consulte [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh), [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54) e [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Armadilhas Comuns

### Permissões e Aprovações
1. O computador compartilhado na nuvem divide Sessions sem isolamento; **nunca faça login em contas principais e sistemas sensíveis**.
2. Require Approval bloqueia apenas operações ainda não executadas e não pode reverter destruições; **estabeleça portões humanos rígidos desde o primeiro momento para ações de alto risco**.
3. Aprovações expiram (Lapse) se ignoradas por cerca de 10 minutos; durante a noite, **é obrigatório configurar listas de permissão (Allow rule) ou pausar em rascunhos**.

### Custos e Arquitetura
4. Entradas com mais de 200 mil (200.000) Tokens dobram o preço unitário: **a camada de roteamento deve configurar um bloqueio rígido e poda em 195.000 Tokens**.
5. Evite sobrecarregar um único Bot com tudo ou clonar 5 Bots genéricos; **a falta de clareza na divisão de tarefas apenas polui o contexto e desperdiça cotas**.
6. Não configure polling de 5 minutos nem escuta de todas as mensagens; **sem uma No-data policy, quedas de rede facilitam a invenção de dados, esgotando a cota**.

### Regras e Transições
7. Instruções dadas na caixa de chat perdem o efeito ao atualizar; **faça com que o Bot memorize a disciplina entre tarefas**; para Bots compartilhados, registre no About de detalhes (Bots pessoais não possuem mais Description).
8. Não transfira todo o histórico entre Bots; **o pacote de transição deve conter apenas o objetivo e o caminho dos entregáveis, acompanhados de conclusões e requisitos para as próximas etapas**.

## Como Fazer a Aceitação Após Concluir

1. **Verifique credenciais**: limpe credenciais bancárias e principais dos Plugins e navegadores, substituindo por subcontas ou Sessions; **nunca armazene senhas em texto puro nos registros de chat**.
2. **Valide a função**: o Bot deve conter Owns/Inputs/May/Must ask before/Done when, com uma declaração antidesvio no final: **reportar erro imediatamente em caso de ausência de dados, sendo estritamente proibido inventar**.
3. **Teste o portão humano**: envie instruções de cobrança ou exclusão, que devem **100% acionar a suspensão por Require Approval**.
4. **Teste a auditoria**: forneça um rascunho com dados falsificados; o Bot de controle de qualidade deve **retornar FAIL na primeira linha** sem realizar alterações arbitrárias; em caso de 3 falhas consecutivas, deve paralisar e emitir alerta.
5. **Estabilize as rotinas**: garanta o fluxo em tempo real do status no kanban e clique em Test run para validar antes de ativar; **tarefas agendadas não devem depender de aprovações noturnas superiores a 10 minutos**.

## Leituras Adicionais

### Documentação Oficial

- [Organizando negócios e trabalho no Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)
- [Colaboração e gerenciamento de permissões de Bots na versão Team](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Arquitetura de segurança e ambiente de execução do Grok Bot](https://cursor.com/cn/docs/grok-bot/security.md)
- [Planos, cotas e detalhes de cobrança](https://cursor.com/cn/help/grok-bot/plans.md)
- [Configuração de tarefas agendadas e rotinas acionadas](https://cursor.com/cn/help/grok-bot/routines.md)
- [Conectar aplicativos](https://cursor.com/cn/help/grok-bot/connect-apps.md)

### Fontes Práticas da Comunidade

> Fonte: [GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> Autor: [Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
