# Capítulo 8 Habilidades e Rotinas: Transformando um Sucesso Único em Execução Automática Diária

Não configure agendamentos diretamente. **Sem supervisão humana, o processo pode travar facilmente ou rodar por engano às 3 da manhã, operando em falso e esgotando a cota de toda a semana.**

Consolide operações em habilidades (Skill) e monte-as em rotinas (Routine):
1. Calibre o fuso horário e padronize os Webhooks.
2. Restrinja o escopo de acionamento do Slack.
3. Adicione a detecção em duas etapas na máquina virtual.

**Defina limites claros para que as entregas continuem estáveis em segundo plano, mesmo fechando o computador.**


![Habilidades e Rotinas: Transformando um Sucesso Único em Execução Automática Diária](/info/08-skills-routines.png)

## Consolidação e Referência de Habilidades: Fixando Seu Procedimento Operacional Padrão

![Consolidação e Referência de Habilidades: Fixando Seu Procedimento Operacional Padrão](/info/08-skills-routines-s1.png)

Habilidades são instruções operacionais salvas na conta, e **todos os Bots vinculados a ela podem chamá-las diretamente**.

### Como consolidar habilidades

**Método 1: Resumo em texto após o diálogo**
Depois que a tarefa for concluída com sucesso, não feche a sessão imediatamente; peça diretamente ao Bot atual para sintetizá-la e salvá-la. O prompt deve especificar com clareza as fontes de entrada, o tratamento de exceções e os limites operacionais; envie diretamente este modelo.

::: details Como consolidar habilidades
```text
请把我们刚刚完成的这套流程保存为名为“每日工单异常审查”的技能。
技能内容必须包含以下要素：
1. 适用场景：工作日审查支持渠道中滞留超过 4 小时的工单。
2. 输入数据：从已连接的工单插件中读取状态为 Open 且优先级为 High 的列表。
3. 决策规则：若工单包含退款申请且金额大于 500 元，标记为一级风险；其余标记为二级跟进。
4. 交付格式：生成 Markdown 表格，列出工单编号、客户标识、滞留时长、风险等级与跟进建议。
5. 异常处理：若工单系统接口无响应或无符合条件的数据，输出明确说明，严禁使用历史缓存或伪造数据。
6. 安全边界：未经人工明确批准，严禁直接调用接口回复客户或变更工单状态。
```
:::

**Método 2: Ensinar por demonstração (Teach task)**
Quando a operação na interface for complexa, demonstrar diretamente é mais prático.
1. No lado direito da janela de chat, abra a visualização do computador e selecione "Ensinar tarefa" (Teach task).
2. Descreva brevemente o objetivo e execute as ações no computador em nuvem. **O sistema grava no máximo 10 minutos de tela e não grava áudio do microfone; nunca digite senhas ou outros dados confidenciais, use os cartões de segurança para credenciais confidenciais**.
3. Após a geração automática do rascunho, **é obrigatório preencher regras de decisão, tratamento de erros e limites de aprovação; nunca coloque diretamente em produção**. Se o botão de acesso não for exibido, o recurso ainda está em liberação gradual (gray release); use o Método 1.

### Como referenciar e gerenciar habilidades

- **Referência na caixa de entrada**: Digite a barra `/` na caixa de entrada para selecionar e carregar a habilidade.
- **Habilitar permissões**: Se ela não aparecer na lista, vá até a barra lateral do desktop em "Aplicativos Conectados" (Connected Apps), clique no número de aplicativos conectados e ative a chave em "Habilidades Privadas".

### Qual é o nível considerado qualificado

| Item de verificação | Redação não qualificada | Redação qualificada |
| :--- | :--- | :--- |
| Fonte de entrada | "Analise os dados recentes" | Especificar claramente plugins, endpoints de API, caminhos de arquivo ou views de banco de dados |
| Controle de limites | "Se tiver problemas, decida o que fazer" | Interromper e reportar erro imediatamente se faltarem dados; estritamente proibido inventar dados |
| Permissões de ação | "Ajude-me a enviar o relatório ao cliente" | Gerar um rascunho e aguardar no chat, **enviando apenas após a aprovação humana** |
| Estrutura de saída | Blocos extensos de texto livre | Lista com campos fixos, tabela Markdown ou caminho de gravação em disco |

Fonte: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)

## Mecanismo Central de Rotinas: Configuração, Visualização e Teste

![Mecanismo Central de Rotinas: Configuração, Visualização e Teste](/info/08-skills-routines-s2.png)

As rotinas são disparadores de fluxos de trabalho vinculados a um Bot, executados no diretório `/workspace` do Linux na nuvem. **Mesmo que você feche o computador ou saia do aplicativo, as tarefas na nuvem continuarão conforme o planejado.**

### Especificações e limites

- Cada Bot pode criar no máximo 50 rotinas, e o sistema retém os últimos 20 registros de execução.
- O intervalo mínimo de disparo para rotinas agendadas é de 5 minutos; não há suporte para agendamento em segundos.
- **A exclusão de uma rotina é irreversível**, e as execuções futuras serão permanentemente encerradas; excluir um Bot também removerá todas as suas rotinas vinculadas.

Fonte: [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Criação e gerenciamento de rotinas

No desktop, envie instruções diretamente na caixa de chat para criar:

```text
每个工作日上午 8:30，调用“每日工单异常审查”技能，在此对话中输出审查清单。如果未检索到高风险工单，只发一行“今日无高风险工单”即可，不要刷屏。
```

Gerenciamento no desktop:
1. Clique no nome do Bot na parte superior da janela de chat para entrar em Details; na lista de rotinas (Routines), é possível visualizar o tempo de execução ou se está Paused, e a chave à direita permite pausar (Pause) ou retomar (Resume) a qualquer momento.
2. Clique em uma rotina específica para verificar três propriedades: Instruction (prompt de execução), When to run (descrição do agendamento) e Webhook (URL exclusiva, chave secreta e cabeçalhos de requisição).
3. A barra de ferramentas inferior oferece Test, Edit e a lixeira vermelha (Delete routine). **Clicar em Edit preencherá previamente a caixa de diálogo com "Edit your routine: [nome da rotina]"**; basta complementar com as solicitações de alteração e enviar para atualizar.

Gerenciamento no celular:
1. Abra a página de perfil do Bot, localize as rotinas e clique em Add routine; isso preencherá previamente "Set up a routine to "; complete com a instrução e envie para criar.
2. Clique em uma rotina existente para visualizar Schedule, Next run e Instruction, bem como a chave Active e o histórico de execuções (Run history).
3. **Desative a chave Active para pausar, ou deslize a linha correspondente para a esquerda para excluir diretamente.** O status é sincronizado em tempo real nos dois sentidos com o desktop.

Fonte: [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md).

### Agendamento e configuração de fuso horário

Caminho para verificar o fuso horário: Settings -> Bot -> Timezone.

| Modo | Mecanismo de execução | Observações |
| :--- | :--- | :--- |
| Auto-detect | Segue automaticamente o fuso horário atual do computador | Adequado para locais fixos; viagens internacionais podem alterar facilmente os horários de execução |
| Especificação manual de fuso horário | Selecionar manualmente o fuso horário correspondente no menu suspenso | Recomendado especificar manualmente para regiões específicas (como Horário de Pequim UTC+8 ou Horário da Costa Leste dos EUA EST) |

- **A criação de uma rotina agendada não executa uma primeira rodada imediatamente**; ela deve aguardar o próximo horário agendado. Por exemplo, se às 8:05 você configurar para rodar diariamente às 8:00, a primeira execução será às 8:00 do dia seguinte.
- **Se for necessária uma inspeção contínua nos finais de semana, a instrução deve enfatizar explicitamente "executar todos os dias, incluindo finais de semana".** Sem uma declaração específica, o Bot opera por padrão de segunda a sexta-feira.

Fonte: [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md), [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Testando rotinas

Na página de detalhes do desktop, clique no botão Test na parte inferior para acionar manualmente. O status do botão mudará para Running…, e o retorno da execução será exibido diretamente na janela de chat.

**O teste executa operações reais**, iniciando o navegador do computador em nuvem, modificando arquivos no espaço de trabalho e consumindo cotas normalmente. Para operações que envolvem exclusões ou alterações, teste primeiro com dados em sandbox. **Se a mensagem Couldn't start a test run for exibida, verifique o status da conexão do computador em nuvem ou se há tarefas anteriores bloqueando.**

Fonte: [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md).

## Gatilhos de Webhook e Slack: Do Polling ao Acionamento Passivo

![Gatilhos de Webhook e Slack: Do Polling ao Acionamento Passivo](/info/08-skills-routines-s3.png)

O polling periódico em páginas web externas consome muitas cotas; operações ociosas e de alta frequência esgotarão rapidamente a capacidade computacional da semana inteira. **Em vez disso, use eventos para despertar o Bot**, mantendo-o totalmente em repouso normalmente e acionando-o de forma passiva apenas quando houver mudanças externas.

A partir de 12/10/2026, o Grok Bot foi incorporado ao sistema The X Subscription, compartilhando o pool de cotas com Grok e Cursor:

| Nível de assinatura | Preço | Multiplicador de uso | Suporte ao Bot |
| :--- | :--- | :--- | :--- |
| Premium | $30/mês ou $300/ano | 4x uso base | Inclui Bot |
| Super | $100/mês ou $1000/ano | 15x uso | Inclui Bot |
| Ultra | $200/mês ou $2000/ano | 50x uso | Inclui Bot |
| Plus | - | - | Não inclui Bot |

### Configuração de Webhook e validação assíncrona

Envie uma instrução na janela de chat para que o Bot crie um gatilho de Webhook.

```text
为当前 Bot 创建一个 Webhook 触发的例程，命名为“外部知识接收端”。
指令内容：读取请求体中的 JSON 数据，提取 url 和 note 字段，将其抓取整理为 Markdown 存入 /workspace/notes 目录。
```

Abra os detalhes da rotina no desktop e expanda o Webhook para conferir os campos principais:
1. POST to: URL pública exclusiva para receber requisições externas.
2. key: Chave privada de autenticação, que deve ser enviada no cabeçalho da requisição como `Authorization: Bearer <key>`.
3. header: Texto completo e concatenado dos cabeçalhos da requisição, pronto para copiar com um clique.

**A configuração deve ser salva clicando em Save para que entre em vigor no gateway e a chave seja gerada.** Se a página de detalhes travar e não abrir, peça ao Bot para enviar o link direto.

[4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

Sistemas externos enviam dados por meio de requisições POST, acompanhadas diretamente de um corpo JSON.

```json
{
  "url": "https://example.com/article/1024",
  "source": "ios_share",
  "note": "精读核心论点并归档"
}
```

O Bot utilizará o JSON como variável de contexto, enviando-o ao modelo junto com a Instruction pré-configurada. [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)

- **HTTP 200 significa apenas que o gateway recebeu a requisição com sucesso e iniciou a execução; não significa que a tarefa foi concluída com sucesso.** O sucesso ou falha da operação deve ser verificado na janela de chat ou nos arquivos gravados no espaço de trabalho.
- Um retorno diferente de 200 indica que a tarefa não foi criada, geralmente porque a rotina está pausada (Paused) ou a chave expirou. [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)

### Gatilhos do Slack e prevenção de estouro de cota

O plugin do Slack é uma ferramenta de leitura e gravação chamada em tempo real durante as conversas; o gatilho do Slack é uma condição de inicialização de rotina e requer autorização prévia nas integrações da conta do Cursor antes do uso.

Envie uma instrução em linguagem natural para configurar o monitoramento:

```text
创建一个 Slack 触发例程：当 #incident-response 频道中有人发消息提及 @bot 且包含短语 "needs repro" 时，在云电脑上拉取报错日志并尝试复现。不要监听其他频道，也不要在没有该短语时响应。
```

Há suporte para quatro tipos de monitoramento: menção ao Bot, correspondência de palavras/frases específicas, adição de reação com emoji ou recebimento de qualquer mensagem.

- **É estritamente proibido monitorar qualquer mensagem em canais públicos**; conversas informais e registros de ponto acionarão correspondências gerais, queimando a cota de toda a semana em um único dia.
- É obrigatório vincular a um único canal dedicado, sem selecionar "todo o espaço de trabalho".
- Mantenha as condições de filtragem o mais restritas possível, como limitar a prefixos específicos ou links de chamados.
- O gatilho só tem efeito sobre novas mensagens criadas após sua configuração; mensagens históricas não são retroativas. [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)

## Casos Práticos de Automação: Três Pipelines Típicos

### Caso 1: Armazenamento em um toque no celular para a base de conhecimento (Atalhos do iOS + Webhook)

O autor comunitário 铁柱 (@cgnot996) construiu um fluxo de arquivamento. Ao se deparar com artigos técnicos ou vídeos no celular, basta clicar no compartilhamento do sistema para que o Grok Bot capture automaticamente o texto completo, extraia os pontos principais e os formate em Markdown no arquivo `/workspace/knowledge/inbox.md`.

Siga estes passos para configurar:
1. **Criar nova rotina na nuvem**: No Grok Bot, crie uma rotina chamada "Arquivamento de Conhecimento Mobile", defina o gatilho como Webhook e obtenha a URL de POST exclusiva e o cabeçalho Authorization.
2. **Escrever a instrução de processamento**: Defina a instrução para receber a URL enviada e abri-la no navegador do computador em nuvem; se for um vídeo, transcrever o conteúdo; após a análise, extrair o título e as tags de acordo com a formatação, organizar os pontos principais e links relacionados, e anexá-los ao final de `/workspace/knowledge/inbox.md`.
3. **Criar o atalho no celular**: No iPhone, abra o app Atalhos, crie um novo atalho, ative "Mostrar no Compartilhamento" e selecione "Páginas da web e texto" como tipo de entrada.
4. **Adicionar o bloco de requisição**: Adicione a ação "Obter Conteúdo do URL", escolha o método `POST`, preencha o endereço de destino do Webhook no URL, adicione o cabeçalho `Authorization` com o valor `Bearer [sua chave privada]`, selecione `JSON` no corpo da requisição e vincule `url` à "Entrada do Atalho".
5. **Superar limitações de compartilhamento**: Aplicativos como o WeChat Official Accounts não conseguem abrir diretamente o painel de compartilhamento com Atalhos. **Crie um atalho adicional de "transmissão por caixa de diálogo" e vincule-o ao Botão de Ação (Action Button)** para colar o link em uma janela pop-up e encaminhá-lo ao Webhook.

**O celular realiza apenas a captura leve de parâmetros e o envio HTTP, deixando todo o trabalho pesado de extração e formatação para a nuvem de forma assíncrona.** Dessa forma, o celular não consome bateria nem exige espera, liberando a interface em poucos segundos.

Fonte: [Grok Bot Webhook + Atalhos: Construção de Pipeline de Entrada Automática de Conhecimento](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh), [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Caso 2: Inspeção em duas etapas na VM e otimização extrema de cotas

O autor comunitário 铁柱 (@cgnot996) otimizou 6 tarefas rotineiras do Bot "Diretor de Marketing". Ele transformou duas inspeções que apenas esperavam por alterações — monitorar respostas da xAI e revisar PRs diários — em verificações leves por comparação. O modelo só é acordado quando há um progresso substancial, economizando de 8 a 10 execuções ociosas por semana.

As tarefas são divididas em duas categorias:

| Tipo de tarefa | Exemplo típico | Estratégia de agendamento e características de execução |
| :--- | :--- | :--- |
| Entrega obrigatória no horário | Relatório diário de SEO, relatório mensal de autoridade | Gerar relatórios completos no horário agendado para consulta humana, mantendo o agendamento fixo nativo |
| Espera passiva por alterações no horário | Monitoramento de atualizações em páginas, verificação de novos PRs | A operação ociosa agendada consome cotas; deve ser convertida em detecção leve |

A implementação é dividida em quatro etapas:
1. **Implantar sentinela local**: Na máquina virtual Linux onde o Grok Bot está em execução, escreva um script extremamente simples em Python ou Bash que não faça chamadas a modelos de linguagem.
2. **Configurar comparação periódica**: Execute o script usando o temporizador `cron` nativo do Linux, a cada meia hora nos dias úteis. O script apenas compara o hash da página web ou consulta a API do GitHub para verificar a contagem de PRs, levando poucos segundos e sem consumir a cota de assinatura do Grok.
3. **Implementar despertar por diferença**: **O script só executa `curl` para fazer uma chamada POST ao Webhook após detectar uma alteração substancial na comparação.**
4. **Intervenção do modelo para tratamento**: Quando o Bot acorda, ele analisa o código do PR ou o conteúdo das respostas, organiza recomendações de decisão e envia notificações.

Deixe os julgamentos mecânicos para scripts locais e acorde os grandes modelos apenas quando for necessário raciocinar. Isso evita desperdiçar a janela de contexto do modelo apenas para dizer "nada aconteceu hoje".

Fonte: [Economize ainda mais cotas do Grok Bot: Otimização extrema de tarefas agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).

### Caso 3: Monitoramento diário do risco de churn de clientes

A equipe oficial e o autor melvindvivas, que opera 29 Bots, adotaram essa solução para monitorar anomalias de clientes. Todas as manhãs, métricas de uso e chamados são coletadas automaticamente para gerar uma lista de observação de alertas precoces, com controle estrito em todas as etapas.

A implementação é dividida em quatro etapas:
1. **Estabelecer o contrato de diretrizes da função**: Crie um Account Risk Bot dedicado, envie o contrato com as regras na conversa e faça com que ele o memorize (para Bots compartilhados, registre no About dos detalhes), definindo os limites de risco. Por exemplo, queda de mais de 40% no volume de chamadas de API por três dias consecutivos, acompanhada de chamados P1 não resolvidos.
2. **Configurar tarefa de coleta agendada**: Configure uma rotina para rodar às 8:00 nos dias úteis, coletando periodicamente métricas do sistema de origem.
3. **Configurar mecanismo de disjuntor de falhas**: **Se a conexão com o data warehouse expirar ou os dados não estiverem prontos, reporte diretamente o motivo da falha por ausência; é estritamente proibido fazer inferências com o snapshot de ontem ou produzir dados não confirmados.**
4. **Configurar barreira humana de aprovação de segurança**: Em Custom Rules dentro de Settings, defina envio de e-mails, alteração de campos de CRM e distribuição de listas como "Perguntar primeiro" (Ask first). A lista compilada pelo Bot será exibida silenciosamente na janela de chat, aguardando que o gerente de contas clique manualmente no cartão de aprovação após a verificação.

**Automações de alto valor não podem simplesmente conceder autonomia total ao modelo; ao conceder capacidade de execução, é obrigatório impor contratos de limites e travas humanas de segurança.**

Fonte: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md), [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

## Guia de Solução de Problemas em Rotinas

### O horário programado chegou, mas o Bot não reage
- No desktop, verifique em Details se não está Paused; no celular, confirme se Active está ativado. **Se você ficar muito tempo sem fazer login ou demorar para responder às confirmações do Bot, as tarefas serão pausadas automaticamente**.
- Confira o fuso horário e as configurações de fim de semana em When to run. Novos agendamentos aguardam apenas o próximo ciclo natural; clique antes em Test para testar o fluxo.
- Verifique o histórico de execuções no celular: **a exibição de No runs yet indica que o sinal não chegou ao gateway**; se exibir Failed, você pode clicar para ver o erro detalhado.

Fonte: [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)

### O Webhook externo disparou, mas a rotina não iniciou
- Ao chamar a API, verifique primeiro o código de retorno: **um código diferente de 200 indica que a requisição foi bloqueada pelo gateway**.
- Confira a chave Bearer no cabeçalho `Authorization`; após gerar uma nova chave, a anterior é invalidada imediatamente.
- Após criar um novo gatilho, **é obrigatório clicar em Save no canto inferior direito** para que o endpoint e a chave entrem em vigor no gateway.

Fonte: [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)

### O gatilho do Slack não dispara
- Os gatilhos **só têm efeito em novas mensagens enviadas após a ativação**; editar mensagens antigas não dispara a ação.
- Confirme se a mensagem não foi enviada no canal errado, se a conta possui permissão de leitura no canal de destino e se **as palavras-chave correspondem com precisão**.

Fonte: [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)

### A tarefa travou e foi interrompida no meio da execução
- Cartões de aprovação não supervisionados em segundo plano **aguardam apenas cerca de 10 minutos**; ao expirar (Expired), a tarefa será interrompida com falha.
- Ative notificações ou libere a execução automática de ações confiáveis em "Regras personalizadas" no modo Settings > Bot > Auto-review.
- Em caso de erro, clique com o botão direito no balão de mensagem em **Copy request ID** e envie o texto do erro para o suporte oficial consultar os logs.

Fonte: [Guia de Operações do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to.md)

### Após a atualização do computador em nuvem, os scripts locais e temporizadores sumiram
| Tipo de atualização | Retenção do ambiente |
| :--- | :--- |
| Atualização de software | O ambiente e os arquivos do computador em nuvem não são afetados |
| Atualização do computador ("Configurações" > "Computador" > "Atualizar Computador do Bot") | Reconstrói a imagem; preserva o `/workspace` e a sessão de login do navegador, **limpando pacotes globais do apt (como o cron)** |

Fonte: [Guia de Operações do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to.md), [Economize ainda mais cotas do Grok Bot: Otimização extrema de tarefas agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)

## Armadilhas Comuns

1. **Clicar em Test executa de verdade**: Ferramentas podem ser chamadas para excluir arquivos; **deixe pontos de interrupção para aprovação nas instruções antes de testar**. [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md).
2. **Mecanismo de polling vs. agendamento**: Fazer polling a cada 5 minutos consome a cota de uma semana inteira; **use scripts leves de comparação e acorde o modelo somente quando houver mudanças**. "Todos os dias às 9h" roda por padrão apenas em dias úteis; **especifique "incluindo finais de semana" e fixe o fuso horário em Settings**.

   [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).
3. **Não cole chaves de Webhook no chat**: Elas serão registradas no histórico em nuvem. **Credenciais devem ser inseridas no cartão seguro de solicitação de informações confidenciais**; se colar por engano, exclua imediatamente.

   [Economize ainda mais cotas do Grok Bot: Otimização extrema de tarefas agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).
4. **Evite falhas silenciosas por bloqueio de aprovação**: Ao configurar interceptações, é necessário ativar notificações no celular. **Após a exibição do pedido de aprovação, ele expira e é descartado se ficar 10 minutos sem resposta**. [Guia de Operações do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to.md).
5. **Ambiente compartilhado entre Bots**: Excluir arquivos em `/workspace/temp` afeta outros Bots; **ao gravar arquivos, especifique subdiretórios dedicados para cada projeto**.

   [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md).

## Como Validar Após a Conclusão

Siga estas quatro etapas em ordem; **deixe rodar sem supervisão apenas se passar em todas**:

1. Verificar horário: Na página de detalhes, confirme se o carimbo de data/hora de **Next run** corresponde com precisão ao fuso horário local.
2. Testar dados ausentes: Desconecte a rede ou envie um arquivo vazio e clique em Test; a rotina deve falhar e encerrar com erro, sem inventar informações.
3. Testar interceptação de aprovação: Envie deliberadamente instruções de exclusão ou envio externo; se executar diretamente sem exibir o cartão de aprovação, há uma brecha que deve ser corrigida em Settings.
4. Verificar logs gravados: Execute uma rodada normal e vá até `/workspace` para confirmar que os documentos foram gravados e que a janela de chat não foi inundada de mensagens.

Fonte: [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

## Leituras Complementares

### Capítulos Relacionados

- [Capítulo 20 Automação Confiável: Agendamento, Webhooks e Disparos por Eventos](/part3/20-automation)

### Documentação Oficial

- [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)
- [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)
- [Guia de Operações do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to.md)

### Práticas da Comunidade

- [4.3 Disparadores e Automação: Agendamentos, Webhooks e Delegação no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [Economize ainda mais cotas do Grok Bot: Otimização extrema de tarefas agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [Grok Bot Webhook + Atalhos: Construção de Pipeline de Entrada Automática de Conhecimento](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
