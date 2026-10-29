# Capítulo 12 Caso: Mídia Própria e Equipe de Conteúdo

A IA conversacional perde facilmente o contexto; o **Grok Bot usa arquivos compartilhados em um computador na nuvem para executar pipelines**.

1. Escreva descrições de papéis e crie um banco de pautas com base em seis conjuntos de campos obrigatórios.
2. O Bot de pesquisa grava os cartões no diretório, e o Bot redator principal os lê para redigir os textos.
3. Implemente regras de revisão para eliminar o "tom de IA" e transforme posts em sites de perfil pessoal.
4. **Os pontos críticos de publicação devem passar por controle humano**, evitando dados falsos e controles de risco das plataformas.

## Design de Funções e Mecanismos de Colaboração para Equipes de Conteúdo

![Design de funções e mecanismos de colaboração para equipes de conteúdo](/info/12-content-s1.png)

### O que é

**Ao montar uma equipe no Grok Bot, o princípio central é "uma função, uma responsabilidade".** Todos os Bots da conta compartilham o mesmo computador na nuvem (com kernel, memória e caminho `/workspace` independentes), mas cada um possui sua própria janela, memória e configurações.

Os Bots realizam a passagem de tarefas lendo e gravando arquivos Markdown em pastas compartilhadas.

### Como fazer

**O Bot principal com estrela no avatar (clique com o botão direito no avatar para alternar)** é responsável pela coordenação e distribuição de tarefas, enquanto 5 a 6 Bots dedicados trabalham estritamente dentro dos limites de suas funções.

| Nome da função | Caminho de entrega | Principais responsabilidades e ações proibidas |
| :--- | :--- | :--- |
| Explorador de Inteligência | `/workspace/content-team/01-inbox/` | Coletar pistas de primeira mão. Estritamente proibido interagir, postar e enviar mensagens privadas; estritamente proibido tratar declarações de segunda mão como fatos |
| Planejador de Pautas | `/workspace/content-team/02-briefs/` | Avaliar pistas e gerar Briefs. Estritamente proibido navegar externamente; proibido avançar para o redator principal sem aprovação humana |
| Redator Principal | `/workspace/content-team/03-drafts/` | Escrever conforme o `voice.md`. Estritamente proibido fabricar fatos e usar tom genérico de relações públicas |
| Editor de Fatos | `/workspace/content-team/04-review/` | Verificar fontes primárias. Sem permissão de publicação; listar para confirmação quando houver conflito de evidências |
| Analista de Métricas | `/workspace/content-team/06-analysis/` | Analisar dados de conteúdo. Estritamente proibido interagir na conta; estritamente proibido transformar correlação em causalidade; estritamente proibido fazer suposições forçadas na ausência de dados |
| Engenheiro Web | `/workspace/tweet-portrait/` | Extrair perfis e criar sites. Estritamente proibido forjar experiências; estritamente proibido tratar caminhos locais como links públicos |

1. Crie a estrutura padrão de diretórios compartilhados no terminal do computador na nuvem.
::: details Como fazer
```text
/workspace/content-team/
├── 00-profile/     # 账号定位、目标读者、范文、禁用表达（voice.md）
├── 01-inbox/       # 情报侦察员的一手信息卡
├── 02-briefs/      # 选题策划师的选题 Brief
├── 03-drafts/      # 内容主笔的候选稿
├── 04-review/      # 事实编辑的审校稿
├── 05-published/   # 已发布文案存档、数据截图或 CSV
└── 06-analysis/    # 数据复盘师的周报与实验记录
```
:::
2. Escreva a base de estilo em `00-profile/voice.md` para evitar que o redator principal produza clichês.
::: details Como fazer
```text
# 账号定位
- 我长期写：面向个人创业者与开发者的 AI 工具实测与提效工作流
- 我的目标读者：正在用 AI 尝试做独立产品、做内容或做业务转型的实干者
- 读者看完后应该获得：直接能照着执行的步骤、准确的参数配置、明确的避坑提醒

# 写作样本
- 代表作 1：【粘贴一段自己数据最好、语言最顺的代表作】
- 代表作 2：【粘贴一段带步骤拆解的教程代表作】

# 表达习惯
- 常用语气：像跟坐在对面的朋友复盘经验，冷静、直白、短句为主
- 禁用表达：我的判断是、毫无疑问、重塑格局、颠覆行业、进入新时代、不难看出
- 不会公开谈论的内容：未经实测的空头八卦、无法复现的玄学跑分

# 商业与事实边界
- 必须保留原始来源的主张：所有关于产品上线、价格变动、官方改版的陈述
- 未亲测时的写法：必须显式标明“未核实”或“作者自述”
```
:::
3. **Crie o grupo e distribua as regras**. Clique em "Novo chat" para criar o chat em grupo "Equipe de Conteúdo de Mídia Própria" e adicione todos os membros. Na primeira vez, evite atribuir pautas diretamente; você deve primeiro enviar as normas unificadas.
```text
这是“自媒体内容团队”协作群。工作顺序固定为：情报侦察员 → 选题策划师 → 内容主笔 → 事实编辑；内容发布后，数据复盘师读取授权数据 → 06-analysis。所有中间文件放到 /workspace/content-team/ 对应目录。任何登录、外发、发布、点赞、回复、关注、私信、购买、删除、连接器授权或权限修改都必须先获得用户明确批准。本次仅确认收到和各自交付路径，不执行外部操作。
```

### O que define um bom resultado

> Fonte: [Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo](https://x.com/AdrianPunk115/status/2097311704547987756)  
> Autor: [Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo](/cases-img/fs26-0.jpg)

![Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo](/cases-img/fs26-1.jpg)

1. O Profile, as tags e as responsabilidades de longo prazo de cada Bot estão salvos, com listas claras de proibições.
2. A árvore de diretórios de `/workspace/content-team/` está completa, e `00-profile/voice.md` contém o posicionamento real e termos proibidos.
3. **Todos os membros responderam confirmando os caminhos de entrada/saída e os limites de controle humano**, e nenhum alega possuir permissões de postagem automática ou acesso externo à rede.

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

## Operação Prática do Fluxo Completo: Pauta, Redação, Imagens e Distribuição

![Operação prática do fluxo completo: pauta, redação, imagens e distribuição](/info/12-content-s2.png)

### Pautas e Inteligência: Coleta, Métricas e Análise de Motivação

> Fonte: [Como aproveitar o Grok Bot na criação de conteúdo](https://x.com/KinGao476942/status/2099736121781764594)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

Não procure temas conversando diretamente com modelos genéricos; eles só fornecerão notícias desatualizadas. Aqui, fazemos o Bot de inteligência simular buscas ou monitorar o mercado, organizando as pistas em cartões.

Primeiro, configure o prompt de função permanente para o explorador:

::: details Pautas e inteligência: coleta, métricas e análise de motivação
```text
你是我的情报侦察员（Scout）。唯一职责是发现、核验并沉淀可用于选题的公开信息，为后续选题提供证据；不写成稿，不替用户下结论。

【允许使用】
- 公共互联网中的官方公告、产品文档、论文、GitHub Release、作者原文与用户提供材料。
- 知乎、微博、X、小红书等平台的公开页面、公开帖子和公开评论区，可用于搜索线索、观察讨论和摘录公开信息。
- 共享目录 /workspace/content-team/00-profile/ 与 /workspace/content-team/01-inbox/。
- 如页面要求登录、密码、验证码、2FA、passkey，或需要扩大权限，必须立即停下并请求用户接管。

【禁止】
- 不得发帖、改帖、删帖、点赞、转发、收藏、关注、取关、评论、回复或私信。
- 不得读取私信、好友可见内容、非公开页面或与任务无关的个人数据。
- 不得把平台用户发言、热榜或搜索摘要直接当成已确认事实；它们只能标为“平台线索”或“观点”，关键主张必须回到官方原文、一手材料或当事人公开内容核验。
- 不得凭记忆补数字、日期、引语或因果。
- 不得索取或记录账号密码与验证码。
- 不得执行本机命令，不得访问本机文件。

【固定交付】
写入 /workspace/content-team/01-inbox/YYYY-MM-DD.md，每次最多 8 条。每条包含：事实或平台线索、来源平台、原始链接、证据摘录、讨论热度或代表性观点、为什么值得关注、一个待核查问题、核验状态。
```
:::

**O banco de pautas deve seguir rigorosamente seis conjuntos de campos obrigatórios**; se faltar um, descarte-o imediatamente:
- Fonte e atualidade: link permanente funcional do post original, data de publicação e tempo decorrido até agora; não escreva "certo criador".
- Dados visíveis: visualizações/reproduções, curtidas, compartilhamentos e comentários (total de 4 itens), além do horário de coleta. Se não encontrar, marque como "dados públicos não encontrados"; estimativas são estritamente proibidas.
- Segmentação do autor: registre handle, número de seguidores e nível. Para contas pequenas com posts virais, estude a estrutura; para grandes influenciadores, analise as pautas.
- Segmentação da comunidade: classifique claramente como oficial, nacional ou internacional.
- Justificativa de adequação e ângulo de execução: conecte com seus pontos fortes e especifique ações concretas (como testes práticos, detalhamento de passos ou criação de templates); não use termos vagos como "está bombando".
- Análise de motivação: abrange dores, pontos de prazer e motivações de interação. Deduções sem suporte de dados devem ser marcadas com "[Inferência]" ao final.

O planejador seleciona 3 pautas de alto valor de `01-inbox/`, filtra pelos três critérios (fatos específicos, relevância para o leitor e capacidade do autor de agregar valor) para gerar o Brief e grava em `02-briefs/`:

```text
读取今天 01-inbox 中已经核验的线索，按照账号定位筛选 3 个候选题，写入 02-briefs/YYYY-MM-DD.md。每题包含：一句话事实、读者场景、单一主角度、原始链接与证据、信息缺口、建议内容形式、给主笔的写作任务。证据不足的题直接标“待补证”。完成后停下，等待我批准，不要通知内容主笔。
```

Se você travar na estruturação, use um prompt de entrevista para que o Bot principal faça perguntas e ajude a esclarecer suas necessidades:

::: details Pautas e inteligência: coleta, métricas e análise de motivação
```text
我想新建一个 Bot，帮我做一件需要重复做的工作。请你先通过提问把这件事了解清楚，再帮我把这个 Bot 创建出来。

提问的时候：
- 一次只问一个问题，用大白话问，我回答完再问下一个。
- 我回答得不清楚的地方，你可以追问，也可以给我几个选项让我选择。
- 你需要了解清楚这几件事：这个 Bot 主要负责什么，做完以后要交给我什么，要去哪里做、用哪个账号，每一步要怎么做、做到什么程度算完成，遇到什么情况要先停下来问我，结果放在哪里，什么时候执行。
- 有些问题我也不知道答案，你就先去搜索解决方案，把你建议的做法告诉我，我确认以后再继续。

问完以后：
- 先把你了解到的内容整理成一份岗位说明给我看，我确认没问题以后，再创建这个 Bot，并且设置好例行任务。
- 创建好以后，先试着执行一遍，把结果拿给我看。
- 登录、付款、发布、删除这些操作，都要先问过我。
```
:::

**Critérios de aceitação**
- Todos os links originais estão funcionando e os fatos principais contam com suporte do texto original.
- Pistas sem evidências suficientes são marcadas como "aguardando comprovação"; **nenhuma avança para o redator sem aprovação humana formal**.

[《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf); [《Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Redação e Copywriting: Remoção do "Tom de IA" e Saída Estruturada

Ao escrever o primeiro rascunho, mude o foco do sujeito de "o que o produto tem" para "como isso ajuda o leitor", **garantindo que o leitor veja um ganho claro de informação nos primeiros três segundos**.

Os textos podem adotar diretamente duas estruturas comprovadas:
- A fórmula HKRR de Tim (MediaStorm): engloba humor/alegria, conhecimento, conexão emocional e ritmo. Cada post deve dominar com firmeza pelo menos um elemento; cobrir dois é excelente; não cobrir nenhum significa descarte imediato.
- As motivações de compartilhamento de Pan Luan: centradas em "isto me diz respeito", mudando o sujeito para o leitor. Por exemplo, em vez de escrever "o software foi atualizado", escreva "você economizou duas horas por dia procurando pautas". Estruturas virais podem ser reutilizadas; copie o ritmo, não o conteúdo.

Defina regras de redação e restrições claras para o redator principal:

::: details Redação e copywriting: remoção do "tom de IA" e saída estruturada
```text
你是我的内容主笔（Writer）。唯一职责是把已经批准的 brief 写成候选稿；不负责找热点、补事实、决定选题或发布。

【允许使用】
- /workspace/content-team/00-profile/voice.md 中的定位、范文、禁用句式与术语。
- /workspace/content-team/02-briefs/ 中已经批准的事实、链接、角度和限制。
- 输出到 /workspace/content-team/03-drafts/。

【禁止】
- 不得自行浏览外部网站、登录平台或调用连接器。
- 不得自行补充数字、引语、案例、比较级或因果。
- 不得伪装亲测、内幕或用户反馈。
- 不得发送、发布、购买、删除或修改权限。
- 不得执行本机命令，不得访问本机文件。

【写作规则】
前两句说清发生了什么，再写具体后果、使用场景、矛盾或尚未解决的问题。观点必须从 brief 中的事实长出来。段落以 2–4 句为主，句子长短交替，保留自然停顿。

【禁用表达】
“我的判断是”“真正有价值的是”“这说明”“这意味着”“毫无疑问”“重塑格局”“进入新时代”，以及空泛三段式、硬凑金句、广告腔和故作深刻的反问。

【固定交付】
按任务需要输出：A. 140–220 字中文短帖；B. 280–420 字展开版；C. 仅在适合时给 3–5 条串文大纲；D. 用户明确要求时写长文。每份稿末附“事实依据”和“仍需确认”。完成后写入 /workspace/content-team/03-drafts/YYYY-MM-DD-题目.md，并只汇报文件路径。
```
:::

Após a conclusão do primeiro rascunho, o editor de fatos faz a revisão. **O editor de fatos apenas verifica as afirmações e elimina o tom de IA**, sem adicionar novos pontos de vista e sem permissões de publicação:

::: details Redação e copywriting: remoção do "tom de IA" e saída estruturada
```text
你是我的事实编辑（Editor），负责发布前的事实核验、结构检查和风格审校。你只做让内容可信、清楚、像真人表达所必需的修改；你没有发布权限。

【允许使用】
- /workspace/content-team/00-profile/voice.md、/02-briefs/ 与 /03-drafts/。
- brief 中列出的原始公开链接，仅用于复核关键事实。
- 输出到 /workspace/content-team/04-review/。

【审稿原则】
1. 没看过原始材料的人也能读懂。
2. 一手来源足以支撑关键事实。
3. 事实、观点和假设明确分开。
4. 删除模板腔、广告腔、绝对化和生硬缩略语。
5. 不让读者误以为作者亲测、掌握内幕或获得用户反馈。
6. 无法核对的句子必须删除、改成疑问或标记“待确认”。

【固定交付】
写入 /workspace/content-team/04-review/YYYY-MM-DD-题目.md，包含：可发布候选版本、改动说明、风险标记、仍需人工确认、原始来源清单。完成后只汇报文件路径和是否达到“可发布候选”标准。
```
:::

**Critérios de aceitação**
- As duas primeiras frases do texto vão direto aos fatos centrais, sem enrolação.
- O editor de fatos confere cada item com os links primários; o que não puder ser verificado é marcado como "a confirmar" ou excluído diretamente.
- O rascunho revisado é movido para o diretório `04-review/`, aguardando a aprovação humana final.

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Imagens e Apresentação Visual: Criação de Sites via Código e Montagem de Materiais

> Fonte: [Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot](https://x.com/0xlangeai/status/2109115005069341175)  
> Autor: [Lange AI @0xlangeai](https://x.com/0xlangeai)

![Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot](/cases-img/fs32-0.jpg)

![Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot](/cases-img/fs32-1.jpg)

Para ilustrar postagens em mídias sociais, evite pedir à IA para desenhar imagens conceituais genéricas, cheias de aspecto artificial ("plástico"). Na prática, costuma-se seguir dois caminhos sólidos:

**Caminho 1: Transformar posts em um site de perfil pessoal (solução de Lange AI)**
No grupo "Site de Perfil de Posts", 4 Bots trabalham em revezamento, armazenando arquivos intermediários em `/workspace/tweet-portrait/`:
1. O organizador de posts coleta postagens históricas, e o analista de perfil extrai hábitos de expressão e contrastes marcantes.
2. O designer do site propõe o layout visual, e o engenheiro web escreve o código front-end com adaptação para dispositivos móveis.

Os dois primeiros papéis executam os prompts em sequência:

```text
【推文整理员任务】
确认我自己已绑定的 X 账号身份，读取最近 90 天内最多 100 条本人内容，包括原创、带有本人评论的引用推文和本人回复，排除纯转发。
建立一个名为 tweet-portrait 的共用项目目录，将素材保存为 tweets.md。每条保留正文、日期、链接和内容类型，并注明实际读取范围、数量与缺失情况。
完成后返回账号名称、项目目录及素材文件的完整路径。无法访问时告诉我具体原因，不补造内容。
```

```text
【个人画像分析师任务】
读取共用项目目录中的 tweets.md，提炼最有辨识度的 3—5 个特点，覆盖关注主题、表达风格、语言习惯、典型观点或有趣反差。
每个特点附 1—2 条真实推文依据，保留摘录、日期和链接，区分观察与推测。不要写通用赞美或没有依据的人格结论。
保存为 profile.md，在群里汇报最有意思的特点和需要我确认的判断，完成后等我检查。
```

Os dois últimos papéis executam os prompts de design e código:

```text
【画像网站设计师任务】
读取共用目录中经过我检查的 profile.md，提出两个明显不同的个人画像网站设计方向。
分别说明首页如何呈现、包含哪些内容、排版和配色如何对应推文特点。保留原文依据，不生成没有统计基础的百分比或人格分数。
先把方向说明发给我，方便选择；需要用图说明时同时提供我可以查看的图片或文件。
选定后，把最终页面内容、结构、视觉和手机端安排保存为共用目录中的 design.md。
```

```text
【画像网站工程师任务】
读取共用项目目录中的 profile.md 和 design.md，按选定方案创建可以运行的个人画像网站，文件放在项目目录内。
保留推文依据和原文链接。打开页面检查桌面端与手机端，修复排版、内容和链接问题。
返回我能打开的预览及实际截图，先等待我检查，再进行发布。
```

Verifique na prévia local o texto da primeira dobra, o espaçamento dos cartões e a exibição mobile; após a confirmação, solicite ao engenheiro que empacote o projeto e **faça o push para o Vercel ou Cloudflare Pages para entrar no ar**.

**Caminho 2: Montagem parametrizada e recortes de áudio/vídeo (solução de 铁柱AGI / ferramentas oficiais)**
- Personagens e figurinos: use o sistema paper doll com dados de jogos; o Bot analisa os parâmetros e chama APIs de terceiros para a montagem.
- Cortes de vídeo: use o modelo oficial de Clip Bot; insira diretamente o link longo de áudio/vídeo para gerar automaticamente a transcrição com marcações de tempo e recortar os trechos principais.

**Critérios de aceitação**
- A prévia local apresenta diagramação organizada, e a adaptação mobile funciona normalmente.
- Todos os posts citados possuem links originais funcionais e navegáveis.
- A página reflete fielmente as expressões reais, sem inventar currículo ou experiências.

[《Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh); [《Coletânea de Posts de 铁柱AGI ③: Métodos Práticos e Casos de Uso》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

### Distribuição, Retrospectiva e Auditoria: Controle Humano e Fluxo Escalonado

Iniciantes costumam buscar automação total sem supervisão, o que leva facilmente ao banimento da conta. **É estritamente proibido usar o navegador dentro da máquina virtual do computador na nuvem para publicar posts**, pois o controle de risco da plataforma detecta a impressão digital da VM. A postagem deve ter um controle humano absoluto e ser feita manualmente pelo próprio criador em um dispositivo físico local.

A colaboração em equipe adota o método de horários desfasados, sem necessidade de monitorar a tela o dia todo:
- Banco de pautas definido semanalmente: gaste 30 minutos por semana escolhendo os cartões candidatos na planilha e marcando os aprovados.
- Rascunhos revisados diariamente: o criador gasta 10 minutos por dia lendo os textos em `04-review/` e adicionando uma reflexão pessoal.
- Fluxo por quadro de status: gerencie na planilha os estados "pendente de revisão", "em redação", "finalizado" e "publicado".

Após o conteúdo ser publicado, encarregue o analista de métricas de fazer uma análise semanal em modo somente leitura; postagens em nome do usuário ou interações são estritamente proibidas:

::: details Distribuição, retrospectiva e auditoria: controle humano e fluxo escalonado
```text
你是我的 X 数据复盘师（Analyst）。唯一职责是分析用户自己的 X 内容质量、帖子表现和可执行的改进方向；只读，不代表用户进行任何互动或账号操作。

【允许使用】
- 用户在任务中明确指定的个人 X 主页，以及该账号公开可见的帖子。
- 用户主动提供或授权查看的 X Analytics 页面、CSV 导出和截图。
- /workspace/content-team/03-drafts/、/04-review/、/05-published/ 与 /06-analysis/。
- 如页面要求登录、密码、验证码、2FA 或 passkey，立即停下并请用户接管；不得索取或记录凭据。

【绝对禁止】
- 不得发帖、改帖、删帖、点赞、转发、收藏、关注、取关、评论或私信。
- 不得修改头像、简介、账号设置、隐私设置或权限。
- 不得读取、复制或分析私信与非本任务所需的个人数据。
- 不得把浏览量相关性写成因果，不得补全缺失指标。
- 不得执行本机命令，不得访问本机文件。

【固定交付】
每周写入 /workspace/content-team/06-analysis/weekly-review-YYYY-WW.md，包含数据来源、时间范围、样本量、表现最好与最差的帖子、内容质量诊断、3 条改进建议、2 个下周实验、数据缺口。需要在 /workspace/content-team/05-published/ 留存所用 CSV 或截图的文件名，不复制账号凭据。
```
:::

Para uma retrospectiva pontual de um período específico, envie a instrução diretamente:

```text
只读分析我明确指定的个人 X 主页【主页地址】，时间范围为【开始日期—结束日期】。数据来源为【公开主页 / X Analytics / CSV / 截图】。

先列出数据范围和缺失字段，再按主题、内容形式、长度、发布时间和开头类型做对比。给 3 条有具体帖子或指标支撑的改进建议，并设计 2 个一次只改变一个变量的下周实验。

禁止发帖、改帖、删帖、点赞、转发、收藏、关注、取关、评论、私信和修改账号设置。遇到登录、验证码、2FA、passkey 或扩大权限时立即停下，等我接管。完成后写入 06-analysis，并只回复文件路径、覆盖帖子数和缺失数据。
```

**Critérios de aceitação**
- Publicação manual feita por pessoa real em dispositivo local, com risco zero de bloqueio por controle de risco.
- Os dados da retrospectiva podem ser rastreados até os arquivos de exportação originais.
- **Não tire conclusões precipitadas quando o tamanho da amostra for inferior a 10 itens**.
- O planejamento da semana seguinte inclui 2 testes controlados de variável única (por exemplo, comparar o impacto de diferentes contagens de caracteres na taxa de engajamento).

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd); [《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

## Análise Detalhada de Casos Práticos Típicos

![Análise detalhada de casos práticos típicos](/info/12-content-s3.png)

### Caso 1: A Equipe Fechada de 5 Pessoas para Mídia Própria de Adrian Punk

Adrian Punk (@AdrianPunk115) estruturou uma equipe permanente de 5 papéis no desktop, completando o ciclo fechado desde a coleta de fontes primárias, pauta, redação e revisão até a retrospectiva.

1. **Restrição prévia de permissões**: nas configurações do cliente, defina "Executar neste computador" como "Nunca permitir"; proíba explicitamente nos prompts a publicação não autorizada, a inserção de senhas e a invocação de conectores.
2. **Construção de caminhos de arquivos**: crie `/workspace/content-team/` e seus 7 subdiretórios no computador na nuvem; inclua o estilo da conta, trabalhos representativos e palavras proibidas em `00-profile/voice.md`.
3. **Divisão dedicada de trabalho**: crie o Explorador de Inteligência, Planejador de Pautas, Redator Principal, Editor de Fatos e Analista de Métricas, delimitando rigorosamente os diretórios de entrada e saída de cada função.
4. **Regras de transição**: envie o comando de inicialização no grupo "Equipe de Conteúdo de Mídia Própria"; os resultados dos estágios anteriores são salvos em Markdown para leitura pelos estágios seguintes, e **nenhuma etapa pode avançar sem aprovação humana prévia**.

Atenção: os 5 Bots compartilham o mesmo computador na nuvem sem isolamento por sandbox, portanto as permissões dependem estritamente de limites claros entre as funções; **o editor de fatos deve comparar os links originais de forma independente**, filtrando números inventados pelo redator e o tom corporativo de relações públicas.

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Caso 2: O Banco Duplo de Pautas Virais para Posts e Vídeos de Kin

> Fonte: [Como engenheiros podem aproveitar melhor o Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![Como engenheiros podem aproveitar melhor o Grok Bot?](/cases-img/fs25-0.jpg)

![Como engenheiros podem aproveitar melhor o Grok Bot?](/cases-img/fs25-1.jpg)

Kin (@KinGao476942, embaixador da SpaceXAI na China) conquistou mais de 2.000 seguidores no Twitter em cerca de 10 dias, gerenciou contas com mais de um milhão de seguidores no WeChat Channels e construiu um Bot operacional para o Twitter juntamente com o banco de pautas virais "Xiao Deng Talk".

1. **Criação do cartão de identidade**: defina claramente o posicionamento, contas de referência e áreas proibidas; proíba postagens automáticas. **Se os dados não forem encontrados, é obrigatório registrar "não encontrado", sendo estritamente proibido estimar ou inventar**.
2. **Feedback com dados reais**: coletou mais de 100 posts históricos e identificou que textos de 200 a 500 caracteres possuem uma mediana de leitura mais alta, e etapas numeradas geram significativamente mais curtidas.
3. **Banco de pautas com seis campos**: criou uma tabela com link permanente do post original, horário de coleta, dados reais, segmentação de seguidores, segmentação de comunidade e análise de motivação, sincronizando com um quadro no Notion para filtragem.
4. **Desconstrução de estrutura**: desconstruiu conteúdos virais com base na HKRR (felicidade, conhecimento, ressonância e ritmo) e nas três motivações de Pan Luan; copie a estrutura, não o conteúdo.

Atenção: na fase inicial de crescimento da conta, a frequência alta de publicação supera o polimento excessivo; ao terminar de escrever, verifique se o sujeito atende aos interesses do leitor.

[《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### Caso 3: O Site de Perfil Pessoal a partir de Posts de Lange AI

Lange AI (@0xlangeai) coletou postagens históricas da conta vinculada do X, extraiu o estilo pessoal e contrastes marcantes, e colocou no ar de forma automatizada um site de exibição de perfil pessoal.

1. **Definição de Bots dedicados**: configurou 4 funções no grupo de projeto "Site de Perfil de Posts": Organizador de Posts, Analista de Perfil Pessoal, Designer do Site de Perfil e Engenheiro do Site de Perfil.
2. **Extração e análise**: o organizador leu até 100 posts originais, citações com comentários e respostas dos últimos 90 dias, salvando em `tweets.md`; o analista extraiu de 3 a 5 contrastes de expressão e suas fontes, corrigidos pelo criador.
3. **Design e deploy**: o designer gerou `design.md` (adotando o estilo de cartões de portfólio), e **o engenheiro escreveu o código no computador na nuvem, concluiu a autoinspeção em ambas as plataformas (desktop e mobile) e auxiliou no deploy no Vercel ou Cloudflare Pages**.

Atenção: o histórico de postagens é um corpus pronto; **cada etapa — organização, análise, design e engenharia — exige confirmação do criador antes de avançar para a próxima**, evitando a amplificação cumulativa de desvios.

[《Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### Caso 4: Coleta Ininterrupta 24/7 e Fluxo Automatizado em Tabelas Multidimensionais por xilo

> Fonte: [Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]](https://x.com/xilo2991/status/2109613437215293905)  
> Autor: [xilo @xilo2991](https://x.com/xilo2991)

![Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]](/cases-img/fs36-0.jpg)

![Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]](/cases-img/fs36-1.jpg)

xilo (@xilo2991) aproveitou a execução 24 horas ininterruptas do computador na nuvem para estruturar um pipeline contínuo de coleta de conteúdos virais, sincronizando em tempo real com tabelas multidimensionais do Feishu (Bitable).

1. **Definição dos três elementos**: estabeleça claramente os canais, contas de referência e palavras-chave, e a tabela de armazenamento dos resultados.
2. **Integração com a tabela**: enviou o repositório GitHub do plugin do Feishu para o Bot, concluiu a configuração e autenticação no computador na nuvem e utilizou a tabela como barramento de colaboração.
3. **Mitigação de risco e descarte**: controlou a frequência durante as buscas para simular navegação normal; registrou o número de pesquisas e a probabilidade de viralização, **eliminando automaticamente palavras-chave ineficazes na retrospectiva semanal**.
4. **Alinhamento via entrevista**: enviou prompts de entrevista investigativa passo a passo para o Bot principal, alinhando detalhes operacionais antes de gerar automaticamente as configurações.

Atenção: a postagem 100% automática foi reduzida para aprovação humana semiautomática, equilibrando eficiência e segurança.

[《Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Caso 5: Funções Dedicadas, Integração Multidispositivo e Prevenção de Banimento na Infraestrutura por 铁柱AGI

> Fonte: [Grok Bot Webhook + Atalhos: Construção de pipeline automatizado para catalogação de conhecimento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Atalhos: Construção de pipeline automatizado para catalogação de conhecimento](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Atalhos: Construção de pipeline automatizado para catalogação de conhecimento](/cases-img/fs06-1.jpg)

铁柱AGI (@cgnot996) testou sistematicamente os limites dos Bots, consolidando planos de prevenção contra banimento e recuperação de desastres.

1. **Função única e dedicada**: dividiu as tarefas em Bots de função única, como inspeção de código, captura de artigos e arquivo financeiro, abandonando a ideia de um Bot "faz-tudo".
2. **Entrada ultrarrápida**: configurou o app Atalhos no celular para ler a área de transferência e enviar diretamente via Webhook para o Bot no computador na nuvem, registrando os dados na tabela.
3. **Linha vermelha antibanimento**: **simular postagens pelo navegador na máquina virtual causa banimento com extrema facilidade; interações públicas externas devem ser realizadas por uma pessoa real em um dispositivo físico**.
4. **Recuperação de desastres**: como a recriação do computador na nuvem apaga ambientes não persistentes, crie scripts Shell de recuperação automática e configure um Memory Manager Bot para fazer backup periódico de prompts e configurações.

Atenção: **configurações críticas e comandos de instalação devem ser consolidados em scripts de recuperação que possam ser executados com um clique**; o computador na nuvem não deve ser considerado um servidor perfeitamente estável.

[《Coletânea de Posts de 铁柱AGI ③: Métodos Práticos e Casos de Uso》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

## Armadilhas Comuns

1. Publicar a partir do computador na nuvem expõe a impressão digital e leva ao banimento; a automação total também costuma postar conteúdo inadequado. **Postagens, curtidas e mensagens privadas devem ser feitas manualmente em um dispositivo físico real**.
2. Defina **regras rígidas na descrição das funções: sem dados, marque como "não encontrado"; deduções devem ser rotuladas como "[Inferência]"**, evitando a entrada de dados falsos no banco.
3. A reinicialização do computador na nuvem limpa as dependências. **Salve os scripts Shell de recuperação em um diretório persistente** para uso preventivo.
4. Nas tarefas de Routine, **verifique com atenção a periodicidade de execução**, evitando configurar acidentalmente "apenas em dias úteis", o que causaria interrupções nos fins de semana.
5. A ausência de filtragem de cenas/storyboard já causou quedas de mais de 40% na cota semanal; **é estritamente proibido fazer polling frequente sem atividade útil; otimize os momentos de disparo**.

Planos a partir de 12 de outubro de 2026:
|Plano|Custo|Cota|Inclui Bot|
|-|-|-|-|
|Plus|$8/mês|-|Não|
|Premium|$30/mês ou $300/ano|4x|Sim|
|Super|$100/mês ou $1000/ano|15x|Sim|
|Ultra|$200/mês ou $2000/ano|50x|Sim|

## Como Fazer a Validação Final

### Permissões e Diretórios
1. Acesse as configurações da conta em "Geral → Agent → Executar neste computador"; **o status deve ser obrigatoriamente "Nunca permitir"**. Os Bots são estritamente proibidos de postar automaticamente e realizar pagamentos, e não devem inventar dados.
2. Verifique os 7 subdiretórios sob `/workspace/content-team/` e preencha o posicionamento da conta, modelos e palavras proibidas em `00-profile/voice.md`.

### Coleta, Redação e Ensaios
1. Colete 3 pistas e **faça amostragem de 2 links para garantir que estejam acessíveis e fundamentados no texto original**; em caso de ausência de dados, sinalize como "dados públicos não encontrados", sem adivinhar números ou contagem de seguidores.
2. Após aprovar o Brief, elabore o primeiro rascunho; as duas primeiras frases devem apresentar diretamente o fato central, os parágrafos devem manter de 2 a 4 frases, o final do texto deve incluir a base factual e itens pendentes de confirmação, evitando completamente palavras proibidas.
3. O rascunho revisado apenas verifica sem adicionar novos argumentos, e **nunca é publicado externamente sem comando humano**. Execute `restore.sh` uma vez no ambiente de teste para checar se o ambiente de dependências está devidamente pronto.

## Leituras Complementares

### Documentação Oficial
- [Planos e Cobrança](https://cursor.com/cn/help/grok-bot/plans.md)
- [Equipes de Bots e Colaboração](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Ambiente e Configuração do Computador na Nuvem](https://cursor.com/cn/docs/grok-bot/computers.md)
- [Colaboração em Chats em Grupo](https://cursor.com/cn/help/grok-bot/group-chats.md)
- [Rotinas e Automação](https://cursor.com/cn/help/grok-bot/routines.md)

### Fontes Práticas da Comunidade
- [《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)
- [《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)
- [《Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)
- [《Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- [《Coletânea de Posts de 铁柱AGI ③: Métodos Práticos e Casos de Uso》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)
