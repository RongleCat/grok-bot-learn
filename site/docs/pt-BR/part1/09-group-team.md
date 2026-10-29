# Capítulo 9 Chats em Grupo e Bots de Equipe: De Um Bot a Um Grupo de Bots

Não sobrecarregue um único Bot com todo o trabalho e **não adicione múltiplos Bots a um grupo**. Vários Bots podem facilmente começar a responder uns aos outros, acordar em loop e esgotar a cota de uma semana inteira, além de Bots pessoais no Slack não conseguirem colaborar.

1. Use um **Bot coordenador como ponto de entrada único**, contando com arquivos compartilhados entre a máquina local e o computador na nuvem para passar tarefas.
2. Quando precisar compartilhar experiências com toda a equipe, publique um Bot de equipe.
3. Controle o uso conforme o mecanismo de assinatura unificada The X Subscription, em vigor desde 12/10/2026.


![Chats em Grupo e Bots de Equipe: De Um Bot a Um Grupo de Bots](/info/09-group-team.png)

## Mecanismo de Chat em Grupo e Regras de Interação: Como Vários Bots Colaboram na Mesma Conversa

![Mecanismo de Chat em Grupo e Regras de Interação: Como Vários Bots Colaboram na Mesma Conversa](/info/09-group-team-s1.png)

Chats em grupo podem incluir vários Bots, mas **Bots de equipe não podem ficar no mesmo grupo que Bots locais**.

O envio de mensagens faz com que todos respondam por padrão; para especificar, use `@Bot名称`. Em tarefas complexas, as transferências de tarefas por chat privado do Bot não são sincronizadas no grupo.

Se estiver preocupado com chats privados muito dispersos, estabeleça regras diretamente:
- **Restrição temporária**: envie uma instrução no grupo.
```text
就在群里回复，这件事不要私信我。
```
- **Restrição de longo prazo**: faça-o registrar na memória de longo prazo.
```text
记住：在群组聊天中，要在群里回复。
```

O sistema não possui um botão para desativar conversas mútuas com um clique; para evitar chamadas em cascata que desperdiçam cotas, use estas dicas:
1. **Proibição temporária**: envie uma instrução no grupo.
```text
不要给其他 Bot 发消息，先问我。
```
2. **Regra de longo prazo**: exija que seja estritamente proibido acordar outros Bots em particular sem confirmação.
3. **Parada de emergência**: quando não for possível parar, **acesse o chat privado exclusivo dele para interromper**.
4. **Silenciamento auxiliar**: desative as notificações ou clique com o botão direito na barra lateral e selecione Hide from sidebar.

Gerenciamento e limitações:
- **Renomear e mudar de direção**: clique com o botão direito em Rename chat (no celular, toque no nome do grupo e selecione Edit name); para mudar de direção, explique diretamente no grupo.
- **Limitações de recursos**: **chats em grupo não oferecem nenhum suporte a voz** (apenas chats individuais), e não é possível ativar ou desativar notificações para um Bot individual.

Critérios de aceitação:
- No máximo 3 membros, sem sobreposição de responsabilidades.
- Perguntas feitas usando `@` para acionamento preciso.
- Saídas concentradas dentro do grupo, sem chats privados desnecessários.
- Nenhuma ativação em cascata entre Bots.

## Comunicação Entre Bots e Roteamento de Permissões no Slack

**Um Bot só pode enviar mensagens entre robôs quando estiver representando uma pessoa específica.** Bots pessoais não possuem representação em Threads públicas e não podem acordar outros Bots; Bots de equipe assumem a identidade de quem fez a pergunta quando são mencionados com @, repassam a tarefa para o Bot exclusivo dessa pessoa e depois enviam o resultado de volta para a mesma Thread.

| Tipo de Bot | Onde perguntar | Permissão entre Bots | Quem representa | Onde responde |
| --- | --- | --- | --- | --- |
| Bot pessoal | Chat privado no app / Mensagem direta no Slack | Pode enviar | Indivíduo | Janela de chat no app (não no Slack) |
| Bot pessoal | Thread pública no Slack | Não pode enviar (alerta que não pode ser executado) | Ninguém | Thread de mensagem original |
| Bot de equipe | Canal do Slack / Mensagem direta | Pode enviar (repassa ao Bot exclusivo de quem perguntou) | Membro que perguntou | Envia de volta para a mesma thread de mensagens do Slack |

[As regras detalhadas podem ser consultadas na documentação oficial](https://cursor.com/cn/help/grok-bot/group-chats).

### Integração e Solução de Problemas com Bots de Equipe

1. Após a publicação do Bot de equipe, o proprietário clica no nome do Bot no topo do chat e clica em Connect em Bring to your team's Slack (quando não publicado, exibe Connect after publishing em cinza).
2. Se a interface exibir Awaiting admin approval, isso significa que os controles de segurança estão ativados; entre em contato com o administrador para aprovação; quando o status mudar para Connected, a vinculação foi bem-sucedida.
3. **Antes de usar, os membros da equipe devem clicar em Link em Settings > General > Team Bots no cliente para vincular suas contas.** Se enviar mensagens diretamente no Slack sem vincular, o Bot apenas responderá com uma solicitação de vinculação.

### Critérios de Aceitação

- A colaboração de múltiplos Bots dentro do canal do Slack é coordenada centralmente pelo Bot de equipe.
- Os membros da equipe concluíram o Link de suas contas.
- **As tarefas são concluídas em ciclo fechado dentro da Thread, sem desconexões ou erros de permissão.**

## Configuração de Fluxo Completo de Bots de Equipe: Criação, Publicação e Compartilhamento Entre Pessoas

Os Bots de equipe são criados por membros e compartilhados com toda a equipe, com chats privados isolados entre si. **Eles rodam apenas na nuvem e não podem ser vinculados localmente**.[Consulte o guia oficial](https://cursor.com/cn/help/grok-bot/shared-bots.md).

### Criação e Conversão em Bot de Equipe

1. Na barra lateral, clique em New chat (+) e selecione Create new Team Bot.
2. Explique os requisitos e configure plugins públicos, Secrets e arquivos.
3. Renomeie e preencha About. **Se mantiver o nome padrão e a descrição estiver vazia, outros membros não conseguirão encontrar o Bot na lista**.
4. Clique em Publish to Team no card.

Bots pessoais existentes podem ser clonados como cópias independentes clicando em Share > Publicar na equipe na interface, gerando uma conta do Slack e migrando segredos, memórias e rotinas (Routines) conforme necessário.

### Localização e Invocação

- **Pesquisa e lista**: selecione Bots de equipe em New chat (+) para navegar ou insira os 3 primeiros caracteres do nome na caixa de busca.
- **Acesso direto por link**: clique com o botão direito e selecione Copy link. Toda a equipe compartilha a base e a memória, não se tratando de um modelo clonado.
- **Distribuição em lote**: os administradores marcam Auto-add no painel Manage Team Bots. **A barra lateral dos membros marcados será fixada no topo automaticamente e não poderá ser ocultada**.

### Permissões e Mecanismos de Execução

Ao invocar uma conta pessoal, a autorização Allow é disparada (Allow once apenas desta vez, Always allow sempre permitir, Skip ignorar). Para redefinir, acesse Settings > General > Team Bots e clique em Clear.

**Os cards de aprovação aparecem apenas no chat privado do proprietário**. Em chats em grupo e no Slack, o Bot só pode operar de forma autônoma.

| Cenário | Ambiente de Execução |
|---|---|
| Chat privado | Computador pessoal na nuvem por padrão (máquinas isoladas se a privacidade for rigorosa) |
| Slack / Chat em grupo | Máquina virtual compartilhada dedicada |

### Critérios de Aceitação

- Nome e descrição do cargo claros.
- Segredos do proprietário perfeitamente isolados.
- Acionável por busca de 3 caracteres ou por link.
- Chamadas entre pessoas disparam autorização Allow, sem riscos de escalonamento de privilégios.

## Modelo de Distribuição de Tarefas 1+N com Bot Principal: Entrada Única e Carta de Cumprimento

![Modelo de Distribuição de Tarefas 1+N com Bot Principal: Entrada Única e Carta de Cumprimento](/info/09-group-team-s4.png)

Não deixe todos os Bots interagirem diretamente com o usuário, para evitar que você fique repassando mensagens entre janelas e desperdiçando tokens no chat em grupo.

**Recomenda-se adotar o modelo 1+N, onde você se comunica apenas com o Bot principal coordenador**, que faz o desmembramento, a distribuição e a consolidação das tarefas. Para mais detalhes, consulte [《De um Bot a uma organização inteira, compartilhamento de uso avançado do Grok Bot: como conectar computador local, divisão de tarefas de IA e base de conhecimento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg).

### Estatuto de Seis Linhas do Bot Principal e Limites dos Especialistas

**O Bot principal é responsável apenas pelo roteamento e pela supervisão, e nunca deve escrever códigos longos ou textos extensos por conta própria.** Para Bots pessoais, envie o estatuto de seis linhas na conversa e faça-o memorizar; para Bots compartilhados, insira-o no campo Description dos detalhes em About. Fique em silêncio quando não houver nada a fazer, distribua tarefas quando necessário e salve relatórios muito longos como arquivos.

Para diretrizes de organização de equipe, consulte [《4.2 Orquestração de Equipe: Estatutos, Funções e Delegação》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh).

```text
Own: 负责需求的统一拆解、分派、汇总与五行简报汇报。
Sources: 人工下发的指令、项目看板文件。
Output: 纯文本状态摘要，超出五行时输出为指定文件路径。
Approval: 任何对外通信、采购、删除操作必须暂停等待确认。
Failure: 下游专职 Bot 报错时如实上报，不使用过期数据假装完成。
Never: 永远不直接编写业务代码，不擅自修改生产配置。
```

Os limites negativos devem ser enviados ao Bot especialista para memorização (para Bots compartilhados, escreva no About dos detalhes):
- Bot Gestor de Tráfego/Anúncios: analisa dados e emite uma lista de itens pendentes de aprovação, **nunca tocando no painel nem nos lances, não ajustando orçamentos, nem adicionando palavras-chave ou criando grupos de anúncios**.
- Bot Redator/Copywriter: produz apenas arquivos de rascunho; é estritamente proibido chamar APIs para publicar conteúdo publicamente de forma direta.
- Bot de Pesquisa de Concorrentes: apenas observa no front-end sem agir; é estritamente proibido fazer pedidos, adicionar ao carrinho, deixar avaliações ou fazer perguntas aos vendedores, evitando bloqueios anti-scraping.

Especialistas em veiculação de anúncios podem aplicar diretamente o modelo de prompt.

```text
Own: 负责广告投放数据诊断与策略输出。
Sources: 运营分析文件 /workspace/project/ad_data.json。
Output: 待批操作清单 /workspace/project/pending_actions.md，列出出价建议与预期影响。
Approval: 绝不直接写入广告后台，不修改出价，不修改预算，不加否定词，所有操作必须等待人工审批。
Failure: 数据缺失时明确标注缺失字段，不推测填充。
Never: 绝不执行任何后台写入与线上提交操作。
```

### Lista Pendente de Aprovação e Aceitação

**Os Bots especialistas geram apenas listas estruturadas pendentes de aprovação, deixando a tomada de decisão para humanos.** Por exemplo, se o Bot principal consolidar 5 conflitos de lances de anúncios, você responde "confirmar sugestões" ou anota alterações antes que a próxima etapa seja disparada.

Após o sistema atingir o padrão, a homologação é feita de acordo com três critérios:

| Item de Homologação | Critério de Aceitação |
| --- | --- |
| Interação e Bot principal | Operação clara com ponto de entrada único; o Bot principal não escreve códigos longos nem artigos extensos |
| Bots especialistas | Cada um cumpre sua função, gerando apenas listas estruturadas |
| Ações de alto risco | Operações irreversíveis contam com pontos claros de confirmação humana |

## Convenção de Arquivos de Transição: Substituindo o Histórico de Conversas pelo Sistema de Arquivos Compartilhado

![Convenção de Arquivos de Transição: Substituindo o Histórico de Conversas pelo Sistema de Arquivos Compartilhado](/info/09-group-team-s5.png)

Não faça o Bot A colar resultados na janela de chat para o Bot B ler. **A interação por janela estoura rapidamente a janela de contexto e perde facilmente o histórico**; as conversas de cada Bot são isoladas na camada lógica fundamental, sendo impossível pesquisar entre elas.

| Dimensão | Características e Conteúdo Incluído |
| :--- | :--- |
| **Camada de compartilhamento físico** | Todos os Bots sob a mesma conta compartilham a máquina virtual, o diretório `/workspace`, conectores e a biblioteca pública de Skills. |
| **Camada de isolamento lógico** | Os históricos de conversas são invisíveis entre si; o Bot A não consegue acessar as conversas privadas entre o Bot B e o usuário. |

Como o disco físico é compartilhado, a transferência de tarefas depende de arquivos estruturados locais; a caixa de diálogo serve apenas para sincronizar status e caminhos.

### Padrão de Pipeline para Transição de Arquivos

A transição padrão inclui a gravação em disco, envio do caminho, leitura e arquivamento.

::: details 文件交接流水线标准
```
[用户指令] ──> (主调度 Bot)
                   │
         1. 派发任务 (指定输出路径)
                   │
                   ▼
             [专职 Bot A] ──> 写入 /workspace/proj/data.json
                   │
         2. 交付：仅返回文件绝对路径
                   │
                   ▼
             (主调度 Bot)
                   │
         3. 调度下发 (附带输入路径)
                   │
                   ▼
             [专职 Bot B] ──> 读取 data.json ──> 写入 output.md
                   │
         4. 汇总简报至用户
```
:::

1. **Distribuição de tarefas**: o Bot principal especifica claramente o caminho absoluto de entrega, como `/workspace/project-alpha/data.json`.
2. **Persistência de dados em disco**: o Bot especialista A conclui a limpeza, grava no arquivo e responde na caixa de diálogo com apenas uma frase informando o caminho onde foi salvo.
3. **Passagem e leitura de caminhos**: o Bot principal acorda o Bot B e passa o caminho; o Bot B lê do disco, faz a análise e grava as conclusões em `/workspace/project-alpha/report.md`.
4. **Apresentação da entrega**: o Bot principal extrai o resumo e anexa o link do documento local ou na nuvem para revisão.

O pipeline de perfil de tweets também segue esse mesmo padrão: o organizador coleta e salva em `tweets.md`, o analista lê o arquivo, extrai tags e grava em `profile.md`, o designer gera `design.md`, e o engenheiro escreve o código com base nisso e fornece capturas de tela para pré-visualização.

Para a prática, consulte [《4.2 Orquestração de Equipe: Estatutos, Funções e Delegação》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh).

### Integração com Feishu Cloud Docs para Entrega Rastreável

Quando houver necessidade de colaboração em equipe ou comentários, configure o CLI do Feishu na máquina virtual para publicar o Markdown como um documento na nuvem. Ele possui um link independente conveniente para distribuição, oferece suporte a comentários parágrafo por parágrafo e também **garante a segurança dos dados corporativos**.

Um fluxo de trabalho em conformidade inclui estes requisitos:
- Cada Bot na cadeia pode ler e gravar de forma independente arquivos definidos em `/workspace`.
- **A caixa de diálogo transmite apenas notificações de status e caminhos absolutos de arquivos**.
- Ao ocorrer uma anomalia, basta verificar o arquivo correspondente no disco para reproduzir e isolar o problema.

## Impacto no Uso e Controle de Cotas: Governança de Múltiplos Bots sob a The X Subscription

A partir de 12/10/2026, o Grok Bot foi integrado à The X Subscription, **compartilhando cotas semanalmente de forma unificada**.

| Plano | Preço |
| :--- | :--- |
| Premium | $30/mês |
| Super | $100/mês |
| Ultra | $200/mês |

### Regras e Estratégias contra Consumo Excessivo

1. **Tanto respostas quanto mensagens de handshake são cobradas**. O chat privado com Bots de equipe deduz da sua própria cota; em chats em grupo, deduz da cota de quem iniciou; se esgotar no início da semana, as operações param durante toda a semana.
2. Mantenha os Bots em chats em grupo em no máximo 3 e **substitua rigorosamente chats em grupo livres pela execução serial 1+N**.
3. Use modelos básicos para tarefas leves, como limpeza, e use modelos de raciocínio de ponta apenas para deduções centrais.
4. Antes de estabilizar a execução, **não configure rotinas agendadas para rodar a cada meia hora ou a cada hora**, para evitar centenas de novas tentativas noturnas que esgotem a cota.

### Critérios de Aceitação

- **Consumo estável da cota semanal**, sem loops infinitos durante a noite.
- Camadas de modelos bem definidas, com custos distribuídos aos membros específicos que fazem as perguntas.

## Casos Práticos: Consolidação da Experiência de Especialistas Corporativos e Implementação 1+N em Equipes Transfronteiriças

### Bot de Equipe da SpaceXAI
A equipe de n2parko **fez com que especialistas de negócios configurassem pessoalmente as regras dos Bots**, transformando-os em assistentes compartilhados por toda a equipe.
1. Mapeamento de nós de alta frequência: a equipe de dados criou o Databot para consultar o data lake, evitando incomodar os especialistas repetidamente.
2. Expansão de cargos: configurou 10x Engineer, Marketing e Sales Assistant para consultar o Salesforce (auxiliando SDR/AE).
3. Memória em camadas: consolidação global de regras gerais mantendo preferências individuais; para mais detalhes, consulte [《Meet your Team Bots｜n2parko》](https://jcng5q8n0f3z.feishu.cn/wiki/KS9Cwan52idy1xkLbnTcSC3xnxb).

### Orquestração 1+12 Transfronteiriça
Zach (@1999Zach22) lidera 12 funções com 1 capitão, **o ciclo fechado automatizado deve estabelecer uma lista pendente de aprovação**, controlando rigorosamente as permissões de escrita.
1. Implantação local: após ajustar as Skills dedicadas localmente, implante-as de forma unificada no computador na nuvem.
2. Limites negativos: o gestor de tráfego é estritamente proibido de operar o painel, apenas fornecendo sugestões; a conta de comprador para pesquisa é estritamente proibida de adicionar ao carrinho, fazer perguntas e deixar avaliações.
3. Interação com entrada única: consolida relatórios diários; em caso de conflitos, emite uma lista com 5 itens em conflito pendentes de aprovação e executa após confirmação.
4. Consolidação de relatórios: usa o CLI do Feishu para converter relatórios em links persistentes de documentos na nuvem; para mais detalhes, consulte [《De um Bot a uma organização inteira, compartilhamento de uso avançado do Grok Bot: como conectar computador local, divisão de tarefas de IA e base de conhecimento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg).

## Armadilhas Comuns

1. Habilidades que não possam ser definidas em três palavras **devem ser consolidadas como Skills do Bot principal**. Não crie sete ou oito assistentes com funções vagas de uma só vez, para não passar o dia todo alternando entre janelas.
2. Todos os Bots da mesma conta compartilham a máquina virtual do computador na nuvem, caminhos locais e sessões de login do navegador; **nunca armazene credenciais privadas individuais em Bots compartilhados**.
3. Evite instruções muito amplas no grupo. Bots trocando gentilezas e confirmações entre si consom cotas desenfreadamente, **podendo esgotar o limite de chamadas de uma semana em meio dia**.
4. Não publique mantendo o nome padrão `New team bot` e deixando a descrição em branco, **pois outros membros não conseguirão vê-lo na lista de busca**.
5. Bots de equipe e Bots locais não podem entrar no mesmo grupo, e não há entrada de voz em grupos. **Se tiver esse tipo de necessidade, mude para o chat privado com um único Bot**.
6. Escrever milhares de linhas de código preencherá o contexto e fará perder a visão geral. **O Bot principal deve ser responsável apenas pelo agendamento e supervisão**, deixando as ações práticas para os Bots especialistas.

## Como Validar Após a Conclusão

1. **Roteamento do Bot principal**: ao enviar uma instrução de negócios intermodular, o Bot principal deve **recapitular com precisão o objetivo e listar os caminhos dos Bots especialistas**, permanecendo em silêncio quando não houver mudanças de estado externo.
2. **Prevenção de mensagens mútuas no chat em grupo**: ao ordenar "não envie mensagens para outros Bots", **o Bot responderá apenas dentro do grupo**, nunca abrindo mensagens na janela de chat privado nem acordando outros Bots em particular.
3. **Busca e autorização**: mude para a conta do Cursor de outro membro e busque pelos **primeiros 3 caracteres** em **New chat** > **Team Bots**; ao chamar um plugin, deve aparecer obrigatoriamente o card de autorização contendo **Allow once**, **Always allow** e **Skip**.
4. **Transição por arquivos**: A salva o arquivo intermediário em `/workspace`, e o **Bot B executa tudo de forma independente usando apenas o caminho absoluto**, sem qualquer necessidade de cópia manual durante todo o processo.
5. **Interrupção com trava humana**: ao dar comandos de publicação, modificação no painel ou exclusão, **o Bot deve interromper a execução e gerar uma lista pendente de aprovação**, nunca gravando online sem aprovação humana prévia.

## Leituras Complementares

### Capítulos Relacionados

- [第 22 章 接入飞书与微信](/part3/22-feishu-wechat)
- [第 24 章 按岗位组建你的 AI 团队](/part4/24-roles)

### Documentação Oficial
- [Chats em grupo e mensagens entre robôs](https://cursor.com/cn/help/grok-bot/group-chats)
- [Bots de equipe](https://cursor.com/cn/help/grok-bot/shared-bots.md)

### Fontes Práticas da Comunidade
- [《Meet your Team Bots｜n2parko》](https://jcng5q8n0f3z.feishu.cn/wiki/KS9Cwan52idy1xkLbnTcSC3xnxb)
- [《De um Bot a uma organização inteira, compartilhamento de uso avançado do Grok Bot: como conectar computador local, divisão de tarefas de IA e base de conhecimento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- [《4.2 Orquestração de Equipe: Estatutos, Funções e Delegação》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
