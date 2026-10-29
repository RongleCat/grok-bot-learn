# Capítulo 13 Estudo de caso: criação de conteúdo e operações no X

Escrever scripts diretamente para chamar a API de publicação em alta frequência aciona facilmente o controle de risco e banimentos, esgotando a cota de uma semana inteira em poucos dias.

- Monte um pipeline em máquina virtual na nuvem: envie uma única frase pelo WeChat para pesquisar pautas automaticamente e gerar o primeiro rascunho.
- Mantenha a regra de **apenas gerar rascunhos e clicar manualmente para publicar**, garantindo a segurança da conta enquanto elimina o trabalho mecânico.

## Recursos nativos da plataforma X: da busca somente leitura à delegação de tarefas nos comentários

![Recursos nativos da plataforma X: da busca somente leitura à delegação de tarefas nos comentários](/info/13-x-ops-s1.png)

Em 08/10/2026, o recurso somente leitura nativo foi lançado, com busca de posts e tendências de 7 dias consumindo o pool de assinaturas.

Em 11/10/2026, a v0.70.2 passou a permitir a busca de tweets públicos sem vincular uma conta; veja o [registro](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd).

|Tipo|Ação|Regras e controle de risco|
|---|---|---|
|Somente leitura nativo|Busca de posts, análise de post individual, tendências de 7 dias|Consome o pool de assinaturas, sem risco de banimento da conta|
|Gatilho externo|Extração e arquivamento via @bot nos comentários|Roteado para o Bot principal favoritado; estritamente proibido responder tweets automaticamente|
|Gravação na conta|Postar tweets, mensagens diretas, ler favoritos, curtir|Usa a API oficial, **estritamente proibido usar navegadores headless para postar**|

### Como fazer
1. **Caixa de diálogo**: digite "Pesquise para mim como as pessoas avaliaram o tópico XX nos últimos 3 dias", ou cole um link e instrua "Extraia o ponto de vista central deste tweet e as controvérsias nas interações dos leitores".
2. **Seção de comentários**: responda com `@bot 提取本帖核心逻辑并存入选题库`, veja as [instruções](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Critérios de aceitação
- **Extração completa**: retorna a fonte original, data/hora de publicação e o contexto da discussão.
- **Limites de resposta**: gera logs em **até 30 segundos** após a delegação da tarefa; apenas elabora rascunhos sem publicar no lugar do usuário, jamais curtindo ou postando automaticamente.

## 5 templates de Bot e sistema de colaboração multi-Agent

![5 templates de Bot e sistema de colaboração multi-Agent](/info/13-x-ops-s2.png)

**Um único Bot tentando cuidar de pesquisa, redação e análise retrospectiva causa facilmente confusão de contexto.** A solução é fazer com que especialistas atuem em suas respectivas funções, compartilhando arquivos no mesmo computador em nuvem.

> Fonte: [Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público](https://x.com/Chchenhao0129/status/2109258247790313478)  
> Autor: [Hardy Chen @Chchenhao0129](https://x.com/Chchenhao0129)

![Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público](/cases-img/fs34-0.jpg)

![Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público](/cases-img/fs34-1.jpg)

A base do Grok Bot é uma máquina virtual na nuvem que vem com um sistema Linux completo. Todos os Bots sob a mesma conta compartilham o mesmo computador em nuvem, com sessões de desktop, gerenciadores de arquivos e terminais próprios e independentes.

A máquina host conta com CPU Xeon de 8 núcleos e 8 threads, 16 GB de memória e 128 GB de espaço em disco (relatado pelo autor, não verificado); para erratas de mecanismos, veja "Coleção de Tweets de 铁柱AGI ②: Observações de Recursos e Versões do Produto" [https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd).

**O sistema de arquivos e a rede desta máquina são totalmente interconectados: os materiais salvos pelo Bot anterior no diretório de trabalho podem ser lidos diretamente pelo Bot seguinte.

** O criador da comunidade Hardy Chen disponibilizou em código aberto 5 templates de especialistas, cobrindo as etapas de operações no X; para detalhes de configuração, veja "Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público" [https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

| Nome do especialista | Link direto para o template compartilhado oficial | Principais responsabilidades |
|---|---|---|
| Diretor de Inteligência | [https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD](https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD) | Monitorar tópicos em alta e posts virais de alto engajamento, encontrar fontes confiáveis e ângulos de abordagem |
| Radar de Notícias de IA | [https://x.ai/bot/wUbWteZc9NS-RUrJc22nh](https://x.ai/bot/wUbWteZc9NS-RUrJc22nh) | Filtrar notícias técnicas do AIHOT, verificar as fontes e eliminar ruídos |
| Recriação de Tweets | [https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_](https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_) | Ler os links dos posts originais, redigir tweets com citação ou respostas e adicionar novos insights |
| Redação de Tweets Curtos | [https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5](https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5) | Transformar materiais factuais em tweets curtos e coloquiais |
| Análise Retrospectiva de Dados do X | [https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN](https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN) | Ler dados de postagens e arquivos CSV, analisar padrões e sugerir ações de testes subsequentes |

### Etapas de configuração da orquestração

1. Adicione os 5 templates à sua própria conta.
2. Escolha um Bot principal como ponto de entrada para a orquestração.
3. **Envie o prompt de inicialização diretamente ao Bot principal para gravar o posicionamento da conta, o roteamento dos especialistas e as diretrizes de redação no contexto persistente.**

O conteúdo do prompt é citado de "Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público" [https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

::: details Etapas de configuração da orquestração
```text
我已经添加五个 X 运营专员：情报总监、AI新闻雷达、推文二创、短推成稿、X数据复盘。请保留你的原有功能，作为这套团队的统一入口，完成一次初始化。

1. 先检查能力和连接
确认当前环境能发现 Bot、向 Bot 发任务并接收回执。找到五个专员的实际 Bot ID，核对名称、职责和来源，遇到同名先消歧。保存持久的“角色—名称—ID”路由，让后续聊天和微信入站任务都能读取。缺 Bot 或缺工具时明确告诉我，不凭名称宣称连接成功。

2. 确认我的账号定位
一次只问一个关键问题，了解主题、目标读者、我能提供的价值和不写的话题。也可以分析我授权提供的主页和近期帖子，提出建议，等我确认。把已确认定位和表达偏好持久保存，并同步给相关专员。不要继承模板作者的个人信息。

3. 自动理解需求、安排任务
找选题、热点、爆款拆解交情报总监；AI新闻交AI新闻雷达；原帖回复、引用、二创交推文二创；短推写稿、改稿交短推成稿；发帖数据分析交X数据复盘。
多步任务由你安排先后，传递来源、我的定位和必要上下文，等真实回执后汇总。日常不要求我指定岗位，也不要求我重复文风。专员失败就说明卡点，不能悄悄代写并声称是专员成果。

4. 保存默认写作要求
像跟朋友分享：讲清发现、理由和具体用途，允许适量语气词，不堆口号。不编我的亲历、数字、测试结果或涨粉成绩。原帖保留归属，新闻核对来源和日期。默认沿用这些要求，我另有要求时再调整。
你交付前检查事实、来源、定位和可读性。来源和说明放在草稿外，方便我看，也方便复制正文。检查X可发布长度，超出则给短版或说明需要的账号功能。

5. 真正跑一次
给五个专员各派一个小任务，检查接收、完成、回传，再跑“找素材→短推成稿→你检查→返回草稿”。保留可核对的任务记录。数据复盘没有真实数据就报告缺口，不编数字。汇报通过项、失败项和恢复办法，不把发出任务当完成。

6. 根据真实反馈改进
记录已发布内容和表现，提出下一轮调整。日常选题和写作规则的小改动留版本、可回退；账号定位、授权范围、发布权限、定时安排或新增收费服务变更先问我。小样本形成试验建议，不宣称已验证涨粉规律。

默认只起草。发帖、回复、点赞、关注和私信由我另行决定，不自动执行。
```
:::

Após concluir a configuração, o Bot principal lembrará os IDs dos subordinados. No dia a dia, ao solicitar a busca de pautas e redação de posts, o Bot principal coordenará automaticamente o Diretor de Inteligência para coletar materiais, repassará para a Redação de Tweets Curtos e, por fim, entregará o primeiro rascunho.

### Critérios de aceitação

Na janela de chat, solicite ao Bot principal que execute um teste para encontrar um tema e redigir o post; o resultado aprovado deve atender a dois pontos:
- **Revezamento real multi-Agent**: nos registros em segundo plano do Bot principal e dos especialistas, é possível ver o processo de envio de tarefas, a execução real pelos sub-Bots e o retorno dos resultados.
- **Qualidade do rascunho e padrões de formatação**: o rascunho retornado não contém slogans artificiais; a fonte original e as notas explicativas ficam organizadas logo abaixo do texto principal, sem se misturar a ele.

## Operações com uma frase no WeChat: integrando o ciclo completo de envio e recebimento pelo celular

Conecte o Bot principal ao WeChat usando o plugin nativo ClawBot (ou iLink) do WeChat para estabelecer uma conexão persistente com o Routine Webhook do Grok Bot. **Todos os Bots compartilham um pool de cotas unificado; não há consumo extra com ociosidade em espera ao ser despertado passivamente por eventos de Webhook.**

Os planos de assinatura unificados do The X Subscription, lançados em 12/10/2026, são apresentados abaixo; para as regras, veja "4.3 Gatilhos e automação: agendamentos, Webhooks e delegação de tarefas no X" [https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg):

| Plano de assinatura | Custo | Multiplicador de cota |
|---|---|---|
| Premium | $30/mês ou $300/ano | 4x de uso |
| Super | $100/mês ou $1000/ano | 15x de uso |
| Ultra | $200/mês ou $2000/ano | 50x de uso |

### Quatro passos para conectar o WeChat

1. No desktop, envie os requisitos de configuração ao Bot principal para que ele verifique os listeners e rotinas no ambiente.

   O prompt é citado de "Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público" [https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye):

::: details Quatro passos para conectar o WeChat
```text
请把你接入我的微信，让我直接在微信里说X运营需求，并收到结果。沿用已确认的账号定位、默认文风和五专员持久路由。

先检查当前是否已有微信连接器、监听程序和routine，避免重复。参考教程：
https://x.com/KinGao476942/status/2108132811635032316?s=20
核对当前ClawBot/iLink接法和所需工具。缺工具或需要授权时如实说明；需要我安全填写、手机扫码时给出具体步骤，不代替我确认。

准备微信入站Webhook任务和监听保活。Webhook URL、密钥及凭据只通过安全输入保存，不打印到普通聊天、日志或公开截图。

只处理我绑定身份的指令，不读取联系人或群聊历史。入站任务必须读取我的定位、文风和五专员实际ID，按需求真派单、等回执，再原路返回纯文本。默认只起草，写稿失败明确报告，不悄悄代写。

监听保持单一实例。处理前持久保存待办，以消息ID去重；回复成功才标记完成，失败保留并有限重试。登录过期或权限错误停止重试并报告。重启后恢复未完成任务，避免漏回和重复回复。

完成后实际验证：扫码登录、微信入站、你的回复、专员接力和微信收到最终稿。再检查监听重启后的恢复。保留脱敏记录，告诉我哪些通过、哪些未通过，不把配置完成当接通成功。说明监听运行在哪个环境、何时会停，以及如何恢复。
```
:::

2. No WeChat do celular, toque sucessivamente em "Eu → Configurações → Plugins" e ative o "WeChat ClawBot". Se não encontrar a opção, informe a versão atual do WeChat ao Bot principal para obter assistência na verificação.
3. Expanda o nome do Bot no topo da janela principal de chat no desktop, acesse "Tarefas de rotina / Routines", abra o card "Despertar de entrada do WeChat" e copie a URL do Webhook e a chave secreta.

   Insira e salve cada uma nos campos correspondentes da caixa de segurança que aparecer; **lembre-se de nunca colar toda a sequência longa contendo Authorization diretamente em um único campo de entrada**.
4. No cliente desktop, envie ao Bot principal: "Plugin ativado, endereço e chave salvos; verifique a configuração e gere o acesso de vinculação", e faça a leitura do código QR no WeChat pelo celular para autorizar. Em seguida, envie "Olá" pelo WeChat; se receber uma resposta, o canal estará configurado.

Para o registro de resolução de problemas, veja "Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público" [https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

### Critérios de aceitação

Envie "Produza para mim 3 posts focados em alcance amplo" para o Bot vinculado no WeChat pelo celular. **Se receber em até dois minutos 3 rascunhos contendo ângulos de abordagem e fontes de material, e os logs em segundo plano registrarem o envio das tarefas, o processo está concluído com sucesso.**

## Design de barreira humana com entrega exclusiva de rascunhos e limites de segurança

![Design de barreira humana com entrega exclusiva de rascunhos e limites de segurança](/info/13-x-ops-s4.png)

Se a postagem automatizada apresentar alucinações do modelo, datas incorretas ou respostas ofensivas, causará danos irreversíveis. **Uma barreira humana de segurança deve ser adicionada ao final do pipeline para bloquear completamente cinco ações: publicar, curtir, seguir, enviar mensagens diretas e excluir, permitindo apenas que o modelo elabore rascunhos.**

::: details Design de barreira humana com entrega exclusiva de rascunhos e limites de segurança
```text
[微信一句话 / 定时触发] 
       │
       ▼
[主 Bot 调度中心] ───► [情报总监 / AI新闻雷达 抓取素材]
       │
       ▼
[推文二创 / 短推成稿 编写草稿]
       │
       ▼
[主 Bot 事实与长度校验]
       │
       ▼
[推送到手机微信 / 客户端对话框] ───► (停住：系统不具备自动发帖权限)
       │
       ▼
[人工审阅：修改、定夺] ───► [人工手动复制到 X 发布]
```
:::

### Configuração de proteção em duas camadas

1. **Comando rígido no prompt**: insira de forma imutável no final dos prompts do Bot principal e dos especialistas:
   "Por padrão, elabore apenas rascunhos. Postar, responder, curtir, seguir e enviar mensagens diretas serão decididos por mim separadamente e não serão executados automaticamente. Fontes e notas explicativas devem ficar fora do rascunho, facilitando a leitura humana e a cópia do texto com um clique".
2. **Interceptação no nível do sistema**: em Grok Bot > Settings → Custom Rules (ou Auto-review), **marque como "Ask first" todas as operações que contenham `send`, `post`, `buy`, `transfer`, `delete`, `permissions`**. Sem o seu clique explícito, a camada subjacente jamais executará a ação.

Para especificações de configuração, veja "4.3 Gatilhos e automação: agendamentos, Webhooks e delegação de tarefas no X" [https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Critérios de aceitação

No teste prático, envie o comando "Publique este rascunho diretamente na página inicial do meu X"; a aprovação requer atender a dois pontos:
- **Interceptação eficaz**: o Bot recusa explicitamente a execução, ou o sistema exibe um card de interceptação para aprovação "Ask first" e interrompe a chamada.
- **Conformidade de formatação**: o texto do rascunho é separado dos links de referência e o tamanho respeita rigorosamente os limites de caracteres da plataforma X.

## Análise aprofundada de casos práticos

Para entender com mais clareza como diferentes criadores integram esse sistema ao trabalho diário, analisamos a seguir três casos práticos representativos da comunidade. Os três modelos correspondem a fluxos operacionais com diferentes escalas e necessidades:

| Caso prático | Criador | Arquitetura principal e método | Pontos-chave de aprendizado |
|---|---|---|---|
| Caso 1 | Hardy Chen (@Chchenhao0129) | 5 templates de Bot + plugin ClawBot do WeChat + Webhook | Orquestração unificada de ponto de entrada único, consolidação do estilo e posicionamento, entrega de rascunhos com barreira humana |
| Caso 2 | SCOTTY BEAM (@ScottyBeamIO) | Colaboração de três Agents + diretório compartilhado no computador em nuvem + gravação de operações | Disco compartilhado para transferência de dados, imagens de referência fixas para padronizar a estética, agendamentos definidos em sessões independentes |
| Caso 3 | 铁柱AGI (@cgnot996), AYi (@AYi_AInotes) | Busca nativa somente leitura + acionamento por `@bot` nos comentários + armazenamento local | Zero APIs externas para reduzir custos e evitar banimentos, delegação de tarefas nos comentários sem trocar de app, persistência em `/home/box` |

### Caso 1: O pipeline colaborativo de 5 Bots com uma frase no WeChat de Hardy Chen

- **Quem**: Hardy Chen (@Chchenhao0129), criador de conteúdo individual.
- **O que fez**: configurou 5 templates de Bot com funções verticais e integrou o plugin ClawBot do WeChat, permitindo que o envio de apenas uma frase de instrução no WeChat execute automaticamente a descoberta de pautas no X, a triagem inicial de notícias de IA, a redação de tweets e a análise retrospectiva semanal de dados de postagens.
- **Como fez**:
  1. Primeiro, adicionou um a um na interface Web os 5 templates de Bot compartilhados oficialmente; após selecionar o Bot principal, enviou o prompt de inicialização do sistema para injetar de uma só vez o posicionamento da conta pessoal, o público-alvo e o roteamento persistente dos 5 especialistas.
  2. Em seguida, configurou o Webhook de entrada do WeChat e o listener de keep-alive, vinculando o Bot principal ao WeChat via escaneamento de código QR pelo celular.
  3. Para as atualizações diárias de notícias, configurou uma tarefa agendada às 7:30 da manhã no fuso horário Asia/Shanghai para que o Radar de Notícias de IA colete informações do AIHOT, verifique as fontes originais e envie tudo para o WeChat.
  4. Para a análise de dados de postagens, forneceu o arquivo CSV do painel conforme solicitado, permitindo que o especialista em dados avalie o desempenho de engajamento e oriente as ações da semana seguinte.
- **O que podemos aprender**:
  - Estabelecer um sistema de orquestração de ponto de entrada único, sem desperdiçar energia repassando mensagens para cada especialista individualmente.
  - Consolidar o posicionamento da conta por meio de um prompt de inicialização, evitando ter que reexplicar o estilo de escrita a cada nova instrução.
  - Manter o mecanismo de entrega exclusiva de rascunhos, separando claramente as notas explicativas do corpo do texto.
  - Ao se deparar com a falta de resposta após a conexão com o WeChat, siga o fluxo padrão de solução de problemas ("processo de escuta — tarefa de keep-alive — desduplicação de mensagens"), em vez de desvincular e ler o código QR repetidamente de forma cega.
  - Para a análise retrospectiva detalhada, veja "Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público" [https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

### Caso 2: O fluxo de conteúdo totalmente automatizado com 3 Bots e comparação de quatro soluções por SCOTTY BEAM

> Fonte: [Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](https://x.com/ScottyBeamIO/status/2089417013647073753)  
> Autor: [SCOTTY BEAM @ScottyBeamIO](https://x.com/ScottyBeamIO)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-0.jpg)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-1.jpg)

- **Quem**: SCOTTY BEAM (@ScottyBeamIO), criador de conteúdo técnico para redes sociais.
- **O que fez**: construiu um sistema de atualização na nuvem com três Agents composto por especialista em pesquisa, especialista em criação visual e especialista em redação de conteúdo, permitindo a integração totalmente autônoma entre mineração de tendências, design de infográficos e redação de tweets, além de avaliar comparativamente quatro arquiteturas de Agent: Grok Bot, Buzz, OpenClaw e Hermes.
- **Como fez**:
  1. Aproveitou ao máximo o fato de todos os Agents do Grok Bot compartilharem o mesmo computador em nuvem subjacente: o Bot de pesquisa busca tendências no X e em repositórios de código públicos em segundo plano, salvando os materiais no disco.
  2. O Bot de criação visual aprendeu previamente o estilo de infográficos de referência fornecido pelo autor, lendo diretamente o material da pesquisa para gerar imagens visuais com diagramação consistente.
  3. O Bot de redação reúne os resultados de ambos para compor o rascunho a ser publicado. Para operações rotineiras mecânicas e fixas, utilizou o recurso de gravação de operações (Recording) para ensiná-las diretamente ao Bot.
- **O que podemos aprender**:
  - Utilizar o diretório compartilhado do computador em nuvem como hub central de dados na colaboração multi-Agent, eliminando a cópia manual e transferências intermediárias de dados.
  - Padronizar a estética visual fornecendo imagens de referência fixas ao Bot de design.
  - Ficar atento à limitação em que chats de equipe com múltiplos Bots não conseguem salvar tarefas agendadas, separando as rotinas de agendamento em sessões individuais de cada Bot.
  - Para a comparação de arquitetura e detalhes operacionais, veja "Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot ｜ SCOTTY BEAM" [https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb).

### Caso 3: Busca nativa no X e arquivamento de conhecimento via @bot nos comentários por 铁柱AGI e AYi

- **Quem**: 铁柱AGI (@cgnot996) e AYi (@AYi_AInotes), pesquisadores de tecnologia de alta frequência.
- **O que fizeram**: utilizando os recursos nativos somente leitura lançados em 08/10/2026 e o mecanismo de integração com @bot nos comentários da v0.70.2 de 11/10/2026, construíram um fluxo de monitoramento de inteligência do setor sem APIs externas e entrada de conhecimento de tweets com um clique no celular.
- **Como fizeram**:
  1. No dia a dia, enviam comandos em linguagem natural na caixa de diálogo para extrair a curva de variação de tendências e os principais posts de debate de qualquer palavra-chave no X nos últimos 7 dias, sem habilitar nenhum conector pago.
  2. Ao navegar pelos tweets no celular, ao encontrar posts longos ou propostas técnicas, respondem diretamente na seção de comentários com `@bot` especificando os requisitos de arquivamento.
  3. O Bot principal favoritado recebe o evento do sistema, captura automaticamente o texto completo do tweet, aciona a base de conhecimento para limpar a formatação e salva tudo como arquivo Markdown no diretório `/home/box` da máquina virtual.
- **O que podemos aprender**:
  - Fazer bom uso das permissões somente leitura nativas oficiais para substituir scrapers de terceiros, reduzindo drasticamente a complexidade de manutenção e os riscos de banimento.
  - Sem necessidade de alternar entre aplicativos no celular, utilizando @bot para acionamento leve.
  - Implementar rigorosamente o armazenamento local de dados, consolidando os caminhos principais no computador em nuvem para evitar perdas causadas por redefinições.
  - Para os pontos práticos essenciais, veja "Coleção de Tweets de 铁柱AGI ②: Observações de Recursos e Versões do Produto" [https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd) e "4.3 Gatilhos e automação: agendamentos, Webhooks e delegação de tarefas no X" [https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

## Armadilhas comuns

### Tarefas agendadas e consumo de cota
1. Ao adicionar múltiplos Bots ao mesmo Team Chat, não é possível salvar uma Routine unificada (comprovado nos testes de SCOTTY BEAM); **é necessário retornar à sessão individual de cada um para configurar separadamente**.
2. Algumas versões executam por padrão apenas em dias úteis; a instrução de criação deve explicitar "incluindo sábados e domingos, executar diariamente no horário agendado" (testado por 铁柱AGI).
3. Verifique nas configurações do sistema se o fuso horário local está definido como Asia/Shanghai, para evitar que as 7:30 da manhã no horário de Pequim sejam executadas na madrugada.
4. A cota dos Bots é compartilhada com Grok e Cursor; um polling a cada 5 minutos lê todo o contexto mesmo sem nenhuma atualização. **É obrigatório mudar para checagem em duas etapas ou despertar incremental (Wake on Done)** para fazer a triagem inicial; melvindvivas, que opera 29 Bots, também recomenda limpar periodicamente rotinas de baixo rendimento.

Fonte: ["4.3 Gatilhos e automação: agendamentos, Webhooks e delegação de tarefas no X"](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

### Solução de problemas de conexão do WeChat e Webhook
1. A falta de resposta após ler o código QR no WeChat geralmente se deve a listeners travados ou à pausa da Routine de keep-alive; **não fique desvinculando e lendo o código repetidamente**. A experiência de Hardy Chen mostra que o ideal é enviar comandos de diagnóstico pelo desktop para verificar processos e filas, enviando uma nova mensagem de teste para restabelecer o fluxo.
2. Até a v0.68.1, se o card de detalhes do cliente não abrir, peça ao Bot para enviar o link direto para o gatilho na caixa de chat para visualizá-lo.

Fonte: ["Coleção de Tweets de 铁柱AGI ②: Observações de Recursos e Versões do Produto"](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

### Limitações de interação com a plataforma e ambiente do host
1. A delegação de tarefas nos comentários não oferece suporte a vídeos puros; não há resposta quando @grok e @bot são marcados simultaneamente; **é estritamente proibido conceder permissões de publicação externa a tarefas delegadas nos comentários**, a fim de evitar injeções maliciosas de prompt.
2. A manutenção da máquina virtual redefine caminhos temporários; **scripts, documentos e dados de backup devem ser salvos unificadamente em `/home/box`**, com scripts de autorrecuperação preparados.

Especificação de caminhos: ["Coleção de Tweets de 铁柱AGI ②: Observações de Recursos e Versões do Produto"](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

## Como validar após a conclusão

1. O Bot principal busca 3 posts com muitas curtidas, verifica o ID do autor, opiniões e horário, sem apresentar erros.
2. Envie um comando para verificar os registros e **confirmar o revezamento real dos 5 especialistas na elaboração do rascunho**, evitando a todo custo que o Bot principal escreva sozinho no lugar deles.
3. Envie pelo WeChat ao ClawBot: "Escreva um tweet curto sobre ferramentas de LLM sob a perspectiva de um iniciante", recebendo o rascunho em 2 minutos.
4. Envie "Publique diretamente o rascunho gerado agora na minha conta do X"; **deve exibir o pop-up Ask first**, não publicando externamente sem confirmação.
5. Alinhe os horários das Routines; forneça um arquivo vazio e confirme que o especialista de análise retrospectiva relata fielmente as ausências, sem inventar dados.

## Leitura adicional

### Documentação oficial e anúncios de lançamento
- [x.ai Changelog](https://x.ai/changelog/bot)
- [Anúncio oficial e documentação de preços do The X Subscription (12/10/2026)](https://docs.x.ai/x-subscription/pricing)

### Artigos originais de práticas da comunidade

> Fonte: [Grok Bot Webhook + Atalhos: construção de pipeline de arquivamento automático de conhecimento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Atalhos: construção de pipeline de arquivamento automático de conhecimento](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Atalhos: construção de pipeline de arquivamento automático de conhecimento](/cases-img/fs06-1.jpg)
- [Basta uma frase no WeChat para gerenciar o X: meus 5 templates de Bot foram abertos ao público](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)
- [Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot ｜ SCOTTY BEAM](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb)
- [4.3 Gatilhos e automação: agendamentos, Webhooks e delegação de tarefas no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [Coleção de Tweets de 铁柱AGI ②: Observações de Recursos e Versões do Produto](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)
- [Grok Bot Webhook + Atalhos: construção de pipeline de arquivamento automático de conhecimento](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- [Economize ainda mais cota do Grok Bot: otimização máxima de tarefas agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
