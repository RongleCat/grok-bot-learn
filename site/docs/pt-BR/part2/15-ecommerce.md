# Capítulo 15 Casos Práticos: E-commerce e Vida Cotidiana

Abrir apenas uma janela de diálogo na web facilita a perda de histórico e exige alternar constantemente entre vários softwares para transferir informações. **Este capítulo vai guiá-lo no fluxo de trabalho completo usando soluções prontas**.

- Vida cotidiana e conteúdo: use prompts maduros para gerar textos para o Xianyu, diagramações para o Xiaohongshu e cards gráficos em SVG, sem precisar de alinhamento manual.
- E-commerce transfronteiriço: comece com inspeções em uma única máquina e monte uma **equipe de "1 Capitão + 12 Funções"**, usando listas de aprovação pendente para controle humano.

## Caso 1: Cadastrador do Xianyu (Painel de Dados de Itens Usados e Rascunhos de Atendimento)

Miles Ma (@miles_mazy, inspirado por @0xlangeai) criou este bot. Vender itens usados enviando tudo diretamente para a IA **facilita que ela invente configurações como se fossem novas**. Ele separa a condição real dos parâmetros oficiais, gerando um painel de dados em duas colunas e rascunhos de respostas.

### Passos e Critérios de Aceite

1. Tire fotos da frente, closes dos defeitos e da etiqueta de identificação, organizando acessórios, método de retirada em mãos e preço de venda.
2. Na barra lateral do Grok Bot, clique em `+`, selecione "Criar Bot" e dê o nome de "Cadastrador do Xianyu".
3. Envie as fotos reais e envie o prompt, usando como exemplo um teclado usado Logitech K380s anunciado por 89 yuans.

```text
帮我做一份闲鱼上架资料。商品是罗技 K380s，黑色，用了 8 个月，空格键有轻微磨痕，逐键输入正常，没拆过机；附两节在用电池，无包装，卖 89 元，支持自提，邮费待确认。查官方型号资料，整理标题、商品描述、需要补拍的照片和常见咨询回复，做成可打开的资料板，并附可复制的上架正文。没提供的信息标为待确认。
```

4. O bot acessa a internet para consultar os parâmetros oficiais e gera um painel de dados em HTML junto com um rascunho em texto puro.

> Fonte: [Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos](https://x.com/miles_mazy/status/2098708209095819605)  
> Autor: [Miles Ma @miles_mazy](https://x.com/miles_mazy)

![Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos](/cases-img/fs27-0.jpg)

![Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos](/cases-img/fs27-1.jpg)

- O lado esquerdo exibe a condição real informada pelo vendedor; o lado direito mostra o preço anunciado, o estado de conservação e os acessórios.
- **Os parâmetros técnicos e o desgaste são listados separadamente; qualquer informação não fornecida deve ser marcada obrigatoriamente como "a confirmar", sendo proibido inventar dados.**
- A lista de fotos complementares aponta ângulos em falta, e as respostas de atendimento cobrem conexão, alternância entre dispositivos e retirada presencial.
- Caso baseado em [Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos | Miles Ma](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf).

## Caso 2: Editor do Xiaohongshu (Da Escolha do Tema a Seis Cards Informativos e Galeria)

![Caso 2: Editor do Xiaohongshu (Da Escolha do Tema a Seis Cards Informativos e Galeria)](/info/15-ecommerce-s2.png)

### Passos de Produção

1. Na barra lateral do Grok Bot, crie um novo bot e chame-o de "Editor do Xiaohongshu".
2. Defina o tema e os tópicos explicativos, estabeleça 6 cards, defina a resolução de 1080×1440 e as cores principal e secundária.
3. Acesse a interface de conversa e envie o prompt:

```text
给电脑新手做一套小红书图文，主题是“Windows 截图后，图片去哪了”。查微软官方资料，做 6 张 1080×1440 的图：封面、框选截图、整屏保存、当前窗口、剪贴板历史、快捷键对照表。用米白、深蓝和亮黄，文字清楚，配操作示意。直接交 PNG 成图、SVG 源文件和配套发布正文，再做一个能看全套图片的画廊。
```

4. **O bot consultará a documentação oficial para verificar os atalhos**, gerará os arquivos SVG, renderizará as imagens em PNG e integrará tudo em uma galeria HTML.

### Aceite e Cuidados Essenciais

| Card | Conteúdo e Diagramação |
| :--- | :--- |
| Card 1 | Capa, com texto grande centralizado destacando o problema comum com capturas de tela |
| Cards 2 a 5 | Cards de passos, ilustrando métodos de captura como seleção retangular, tela cheia, etc. |
| Card 6 | Card de resumo, com tabela de 4 métodos de captura e seus respectivos destinos |

- Toda a série de cards adota fundo off-white com texto em azul-escuro e detalhes em amarelo-vivo. **É obrigatório entregar 6 arquivos PNG em 1080×1440, o código-fonte em SVG, o texto de publicação com tags e a galeria online.**
- O salvamento automático da captura no disco depende das configurações da galeria/fotos do sistema; **a consulta do histórico com Win + V exige que a opção tenha sido ativada previamente** e que o registro não tenha sido sobrescrito.
- Para corrigir erros de digitação, altere o SVG diretamente em um editor de texto, **sem necessidade de gerar a imagem novamente**.

Caso de referência: [Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos | Miles Ma](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

## Caso 3: Analista de Ferramentas (Boletim de Análise de Software com Filtro por Finalidade)

O bot "Analista de Ferramentas", criado por Miles Ma, é especializado em coletar dados de repositórios de código aberto e documentações, gerando um boletim em cards web com suporte a filtros por categoria.

### Limitações das Ferramentas e Tarefas Recomendadas

| Ferramenta | Requisitos e Dependências | Principais Limitações | Tarefas Recomendadas |
| :--- | :--- | :--- | :--- |
| **PowerToys** | Execução direta via instalador do Windows | Exclusivo para Windows; alguns recursos experimentais apresentam instabilidade ocasional | Extração de texto por atalho ou fixação de janelas no topo |
| **MarkItDown** | Requer Python ou linha de comando | Taxa de reconhecimento limitada em layouts complexos de texto e imagem | Conversão em lote de Word e PDF para Markdown |
| **changedetection.io** | Requer ambiente Docker ou servidor | Exige conhecimentos básicos de infraestrutura/DevOps; sujeito a bloqueios anti-scraping | Monitoramento de alterações em etiquetas de preço de e-commerce |

### Passo a Passo

1. Na barra lateral do Grok Bot, crie um novo bot chamado "Analista de Ferramentas".
2. Defina o público-alvo da pesquisa e a lista de ferramentas a serem analisadas.
3. Acesse a interface de conversa e envie o prompt.

```text
帮内容工作室整理 PowerToys、MarkItDown 和 changedetection.io，查官方仓库和文档。每个工具写清能帮忙做什么、上手需要什么、主要限制，再给一个具体使用例子。做成能按用途筛选的网页简报，附来源链接。
```

4. O bot coleta as descrições e dependências dos repositórios e **desenvolve um boletim em HTML com scripts de filtragem**, salvando-o na área de trabalho.

### Critérios de Aceite e Cuidados Essenciais

- Cada card **contém 6 elementos essenciais**, cobrindo o posicionamento da ferramenta, os pré-requisitos para uso, as principais limitações, tarefas práticas e links oficiais.
- O topo da página web conta com botões de categoria que permitem filtrar os cards suavemente.
- A descrição das limitações deve ser rigorosamente objetiva, explicitando que o changedetection.io requer Docker ou servidor, sem exagerar dizendo que a ferramenta tem barreira zero.
- Trata-se de uma triagem preliminar de mesa; **o bot não realiza testes práticos do fluxo completo**, servindo principalmente para descartar rapidamente softwares candidatos que não atendam aos requisitos mínimos.

[Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos | Miles Ma](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

## Caso 4: Instrutor de Tutoriais em Vídeo (Ferramenta Didática Interativa e Vídeos Curtos com Legendas)

Esta é a abordagem de Miles Ma (@miles_mazy, inspirada por @0xlangeai / Lange AI). Explicar os giros horários e anti-horários de um cubo mágico e a restauração após quatro giros apenas por texto é muito difícil, e gravar vídeos manualmente consome tempo demais. **O Grok Bot consegue criar páginas interativas na nuvem e gravar a tela automaticamente incorporando legendas**.

### Como Fazer

1. Na barra lateral, crie um novo bot e dê o nome de "Instrutor de Tutoriais em Vídeo".
2. **Explique apenas um movimento básico por vez**, evitando o algoritmo completo de resolução.
3. Envie o prompt:

```text
给孩子做一个魔方入门小工具，能认识六个面、点按钮演示右面顺转和逆转，再展示右面连续转四次回到原位。把实际操作录成一分钟左右的教学视频，加中文配音和字幕，交付视频和工具文件。
```

4. O bot programa a página web automaticamente, simula os cliques e grava a tela, gerando um vídeo com legendas em chinês.

### O Que Define uma Boa Entrega

| Item Entregue | Critérios de Aceite |
| :--- | :--- |
| **Página web interativa** | Código-fonte HTML/JS preservado; clicar em R altera as cores, clicar em R' restaura, botão de redefinição retorna à posição original em 4 passos; abre offline |
| **Vídeo finalizado** | MP4 de aproximadamente 51 segundos com legendas em SRT, com sincronia perfeita entre ação visual e legendas |

Essa mesma estratégia pode ser aplicada em demonstrações de painéis administrativos ou no ensino de recursos pontuais.

Caso baseado em [Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos | Miles Ma](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf).

## Caso 5: Organizador de Favoritos (Transformando Salvos das Redes Sociais em Banco de Pautas)

![Caso 5: Organizador de Favoritos (Transformando Salvos das Redes Sociais em Banco de Pautas)](/info/15-ecommerce-s5.png)

Miles Ma (@miles_mazy) criou este bot para transformar itens salvos em um banco de pautas.

### Passo a Passo

1. Na barra lateral, crie um novo bot chamado "Organizador de Favoritos".
2. Escolha 5 tipos de links representativos (como episódio 115 de um podcast, conversão de imagem em texto).
3. Envie o prompt:

```text
整理这几条 X 收藏链接，按主题分类，每条留下作者、原链接、核心观点和可以借鉴的写法。再围绕“给新手的 AI 实操教程”提出三个具体选题，做成 Markdown 素材库和选题清单。
```

4. O bot organiza e gera **dois arquivos Markdown**: o "Banco de Conteúdos Salvos" e as "Sugestões de Pautas".

### Aceite e Restrições

- Aceite: **Preservar o autor original e o link da fonte**, decompor a lógica do texto e refinar as 3 pautas para que possam ser executadas diretamente em uma única tarefa.
- Restrições: **É terminantemente proibido falsificar práticas e dados de terceiros como experiência própria**, limitando-se a aprender a estrutura e a linha de raciocínio.

[Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos | Miles Ma](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

## Caso 6: Estruturação de Equipe para Amazon (Da Inspeção no Front-End à Colaboração Multifuncional "1+12")

![Caso 6: Estruturação de Equipe para Amazon (Da Inspeção no Front-End à Colaboração Multifuncional "1+12")](/info/15-ecommerce-s6.png)

### Contexto e Definição de Papéis

- **Quem**: Zach (@1999Zach22).
- **O que fez**: Migrou totalmente as Skills que rodavam localmente no Claude/Codex para o Grok Bot, montando em um computador na nuvem compartilhado uma equipe de operações de IA para e-commerce transfronteiriço na Amazon, composta por "1 Capitão de Operações Internacionais + 12 Funções de Negócio".

### O Que É

Ferramentas locais como a Codex CLI exigem que a máquina fique ligada o tempo todo, tornando impossível monitorar as operações fora de casa. **O Grok Bot inclui um computador na nuvem nos EUA disponível 24/7**, acessível de forma sincronizada pelo celular e pelo computador, além de permitir navegar e fazer perguntas no front-end da Amazon usando contas reais de compradores.

Zach adota uma arquitetura de **"1 Capitão + 12 Funções de Negócio"**. Você interage apenas com o Capitão de Operações Internacionais, e ele gerencia e distribui o trabalho entre todas as funções.

**Todas as funções são estritamente proibidas de realizar alterações diretas no painel administrativo da loja**, emitindo apenas listas de aprovação pendente para confirmação humana.

| Função | Responsabilidades | Limites Estritamente Proibidos |
| :--- | :--- | :--- |
| Capitão de Operações Internacionais | Coordenar e delegar tarefas aos subordinados; apresentar relatórios semanais e listas de pendências | Tomar decisões de negócios diretamente sem passar por humanos |
| Assistente / Pirata / VOC | Inspecionar hijackers (venda casada), pesquisar seleção de produtos e analisar avaliações negativas | Fazer login no painel do vendedor ou aprovar projetos por conta própria |
| Financeiro / Gestor de Tráfego | Calcular margem de lucro por item e emitir sugestões de anúncios | Fazer login no painel para alterar lances ou adicionar palavras-chave negativas |
| Redator / Designer / Guardião | Produzir textos publicitários, imagens e realizar revisão final de conformidade | Publicar anúncios diretamente ou tomar decisões finais no lugar de humanos |
| Bot de Retrospectiva | Consolidar entregas semanais e atualizar a base de conhecimento | Mascarar problemas operacionais ou inventar métricas de desempenho |

### Como Fazer

#### 1. Plano de assinatura e preparação do ambiente
- **Para começar, escolha o plano Premium de US$ 30/mês** (o plano Plus de US$ 8 não possui nenhum bot); faça upgrade para o plano Super de US$ 100 ou Ultra de US$ 200 conforme a necessidade.
- Conecte a mesma conta no computador e no celular e **certifique-se de que o computador na nuvem está funcionando normalmente**. Para mais detalhes, consulte o [Guia de Planos e Uso do Grok Bot](https://cursor.com/cn/help/grok-bot/plans).

#### 2. Primeiro, valide três tarefas usando um único bot
Utilize o IP dos EUA e o navegador do computador na nuvem para validar três tarefas:
1. **Inspeção diária dos seus próprios listings**: verifique a imagem principal, o preço, as variações e hijackers (anúncios vinculados/parasitas), relatando anomalias acompanhadas de provas comparativas.
2. **Teste de perguntas e respostas de compras com a Alexa**: faça login com uma conta de comprador para fazer perguntas; em testes práticos, avaliou 8 cenários e consultou 30 dias de histórico de preços em cerca de 8 minutos.
3. **Monitoramento programado da concorrência**: registre preços e cupons, **enviando notificações apenas se houver alterações**, sem incômodos caso não haja mudanças.

```text
每天固定时间去前台检查自家 Listing：主图和价格是否正确，变体是否正常挂载，核心关键词是否能搜索到，是否存在跟卖。只记录指定商品和关键词，有异常才发提醒，并附带与前一日的对比数据和页面截图证据。不登录店铺后台，不执行任何写操作。
```

```text
从消费者的角度，尽可能多地把 Alexa for Shopping 体验一遍，最后给我一份报告。
```

#### 3. Decomposição de funções e limites operacionais
- Após validar o fluxo, divida as tarefas entre as 12 funções de negócio.
- **Funções sensíveis, como gestão de anúncios e lançamento de produtos, são expressamente proibidas de gravar no painel**, devendo sempre entregar uma "lista de aprovação pendente" e definir claramente os limites de consulta prévia.

```text
你是合理烧钱的广告投手。负责分析广告效率、搜索词转化率、出价与预算建议。
边界约束：
1. 绝对不登录广告后台，不直接修改出价，不调整预算，不添加否定关键词，不新建广告活动；
2. 所有优化建议必须生成「待批清单」，每条建议必须附带调整依据和预期影响；
3. 待批清单单线交付给出海船长，由船长提报给业务负责人审核，严禁自主执行。
```

#### 4. Orquestração da cadeia de transição "1+N"
- **Nunca crie chats em grupo com múltiplos bots**; grupos recebem o contexto repetidamente e esgotam os tokens a uma velocidade extrema.
- **Adote a arquitetura 1+N**: os humanos lidam apenas com o "Capitão de Operações Internacionais", cabendo a ele distribuir tarefas e consolidar os resultados.

```text
你是出海船长，负责统筹 12 个业务岗位。日常接收业务负责人的目标，拆解为具体子任务派发给对应岗位。所有下属岗位向你单线汇报，由你汇总结果、审核质量；不达标的打回重做，需要人工决策的整理为带选项和依据的待批清单汇报给人。严格遵守交接链规则：
1. 巡检链：助理上报异常与证据，派给数据或广告岗位做归因分析；
2. 选品链：海盗提交机会报告，财务测算单品利润，由你整理为立项建议书提报给人；
3. 上新链：文案出草稿，设计出图，守门员审核，你做终检后交给人确认，由人工在后台发布；
4. 复盘链：收齐各岗位经验，复盘机器人写周报并更新经验库，据此编排下周计划。
所有岗位严禁直接登录店铺后台或执行未授权的修改操作。
```

#### 5. Compartilhamento de ativos e controle local
- Todos os bots **compartilham o mesmo computador na nuvem e o mesmo disco**; os scripts copiados para a área de trabalho ficam disponíveis para toda a equipe.
- Para ler arquivos locais, é necessário acessar a guia "Computador" nas configurações, **ativar "Execução neste computador"** (Execution on Local Computer) e especificar o diretório a ser copiado.

  Para detalhes, consulte a [Documentação de Computador e Aplicativos do Grok Bot](https://cursor.com/cn/docs/grok-bot/work) e as [Instruções de Configurações do Grok Bot](https://cursor.com/cn/docs/grok-bot/settings).

### O Que Define uma Boa Entrega

> Fonte: [Compartilhamento Prático de E-commerce Transfronteiriço com Grok Bot: Estruturando uma Equipe Completa para Amazon do Zero](https://x.com/1999Zach22/status/2110078772225667115)  
> Autor: [Zach @1999Zach22](https://x.com/1999Zach22)

![Compartilhamento Prático de E-commerce Transfronteiriço com Grok Bot: Estruturando uma Equipe Completa para Amazon do Zero](/cases-img/fs38-0.jpg)

![Compartilhamento Prático de E-commerce Transfronteiriço com Grok Bot: Estruturando uma Equipe Completa para Amazon do Zero](/cases-img/fs38-1.jpg)

- **Comunicação direta exclusivamente com o Capitão**, sem necessidade de alternar entre 12 bots.
- Alterações de preços e reposições de estoque tramitam por listas de aprovação pendente, **eliminando qualquer extrapolação de autoridade**.
- Recebimento de alertas de anomalias no celular, enquanto as inspeções continuam rodando mesmo com a tampa do notebook fechada.

Caso baseado em [Compartilhamento Prático de E-commerce Transfronteiriço com Grok Bot: Estruturando uma Equipe Completa para Amazon do Zero](https://jcng5q8n0f3z.feishu.cn/wiki/LG1twK03uiO00JkPk1ncQQNUnvt).

### O Que Podemos Aprender

- Primeiro valide e **alinhe o SOP com um único bot** antes de dividir as tarefas.
- Utilize a **distribuição mestre-subordinado "1+N"** para evitar o consumo descontrolado de tokens em chats em grupo.
- **Gere exclusivamente listas de aprovação pendente**, exigindo confirmação humana manual no painel administrativo.

## Armadilhas Comuns

- **Nunca conceda permissões de modificação no painel do vendedor**: tarefas sensíveis devem gerar uma "lista de aprovação pendente" para execução manual por humanos, evitando erros de precificação ou banimento da loja.
- **Evite que o bot invente o estado de conservação no Xianyu**: exija explicitamente que "as informações fornecidas pelo vendedor prevaleçam e dados não fornecidos sejam marcados como a confirmar", prevenindo a inclusão de parâmetros de produtos novos que resultem em devoluções.
- **Não coloque 12 bots no mesmo grupo**: poucas rodadas de conversa esgotarão a cota de uma semana inteira. Use a arquitetura mestre-subordinado "1+N", transferindo informações por meio de arquivos gravados no disco.
- **A coleta de concorrentes deve ser feita preferencialmente 1 vez ao dia**: fazer requisições a cada poucos minutos acarreta bloqueio de IP e consome toda a cota rapidamente; para alta frequência, utilize APIs oficiais ou MCP.
- **Escolha com certeza o plano Premium de US$ 30/mês**: o plano Plus de US$ 8/mês não dá acesso a bots; confirme a adesão a The X Subscription a partir de 12/10/2026.
- **O controle local deve ser restrito a caminhos específicos**: não deixe a permissão como "permitir sempre"; especifique o caminho dos arquivos antes da execução e mantenha as confirmações por janela pop-up para evitar alterações acidentais em arquivos pessoais.

## Como Fazer o Aceite após a Conclusão

**Após a entrega, confira item por item em relação aos critérios estabelecidos**; não se descuide.

- **Painel de dados do Xianyu**: listar defeitos e parâmetros oficiais separadamente, marcando itens desconhecidos como "a confirmar"; é terminantemente proibido inventar endereços de retirada presencial ou mentir sobre a vida útil da bateria.
- **Conteúdo para o Xiaohongshu**: entregar 6 cards gráficos em 1080×1440 com código-fonte SVG, destacando atalhos de teclado e pré-requisitos do sistema nas etapas; mantenha a harmonia da paleta de cores.
- **Boletim de ferramentas**: página HTML única obrigatória com filtros e links oficiais, informando fielmente as restrições de ambiente Docker; proibido divulgar a implantação como sendo de barreira zero.
- **Vídeo tutorial**: vídeo finalizado de aproximadamente 1 minuto com áudio e imagem sincronizados, acompanhado obrigatoriamente do código-fonte da ferramenta web; garanta que legendas e tela não se dessincronizem.
- **Banco de materiais**: preservar o autor original e o link da postagem original, afunilando as pautas para execução prática individual; evite resumos genéricos ou apresentar casos de terceiros como próprios.
- **Colaboração no e-commerce**: na arquitetura 1+N, interagir apenas com o Capitão; ajustes de preço e novas publicações devem obrigatoriamente gerar listas de aprovação pendente; é proibido alterar preços por conta própria ou entrar em loops infinitos que esgotem a cota de uso.

## Leituras Adicionais

- [Guia Prático de Casos de Uso do Grok Bot: Publicação no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Produção de Vídeos Curtos e Organização de Favoritos | Miles Ma](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)
- [Compartilhamento Prático de E-commerce Transfronteiriço com Grok Bot: Estruturando uma Equipe Completa para Amazon do Zero](https://jcng5q8n0f3z.feishu.cn/wiki/LG1twK03uiO00JkPk1ncQQNUnvt)
- [Documentação de Computador e Aplicativos do Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- [Guia de Planos e Uso do Grok Bot](https://cursor.com/cn/help/grok-bot/plans)
- [Guia de Configuração de Rotinas Agendadas do Grok Bot](https://cursor.com/cn/help/grok-bot/routines)
- [Instruções de Configurações do Grok Bot](https://cursor.com/cn/docs/grok-bot/settings)
- [Guia de Uso dos Recursos Principais do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)
