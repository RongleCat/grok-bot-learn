# Seleção de Artigos Longos em Chinês

Ao executar fluxos de trabalho com o Grok Bot, as principais armadilhas costumam ser **vinculação de contas, confusão entre ambiente local e nuvem, limites de permissão extrapolados e rotinas rodando no vazio**, além da necessidade de se precaver contra captchas, falhas de API e consumo de cotas. Se as responsabilidades entre os papéis não forem bem divididas, os bots ainda podem disputar contexto entre si.

Reunimos aqui **15 práticas detalhadas**, testadas e comprovadas pela comunidade, cobrindo cinco grandes módulos: introdução e fundamentos, operação de mídias digitais, engenharia e P&D, e-commerce e cotidiano, e orquestração organizacional, prontas para consulta direta.

| Categoria Temática | Título do Artigo | Cenário Principal de Negócio | Mecanismos e Ferramentas-Chave |
| :--- | :--- | :--- | :--- |
| Introdução e Fundamentos | "Guia Completo \| Grok Bot do Zero: O Primeiro Passo" | Ativação de conta e primeiro contrato de tarefa | Computador em nuvem Linux, assumir controle com Take over, retenção de Skills |
| Introdução e Fundamentos | "Como Usar o Grok Bot a Fundo em Uma Hora" | Inspeções padronizadas e consolidação de metodologias | Elaboração de critérios de aceitação, gravação com Teach a task, desduplicação de rotinas |
| Introdução e Fundamentos | "10 Dicas Essenciais para Deixar seu Grok Bot Ainda Melhor" | Governança de ambiente multi-Bot e prevenção contra interrupções | Triagem na caixa de entrada, orquestração via CLI, Wake on Done, desativação do App Nap |
| Operação de Mídias Digitais | "Criando uma Equipe de Mídias Digitais com o Grok Bot: Tutorial Passo a Passo" | Pipeline de conteúdo ponta a ponta com 5 funções | Diretório compartilhado de 7 níveis, restrições com voice.md, validações humanas em toda a cadeia |
| Operação de Mídias Digitais | "Como Fazer um Bom Uso do Grok Bot na Produção de Conteúdo" | Banco de pautas estruturado e desconstrução de conteúdos virais | Framework HKRR, validação de 6 grupos de campos obrigatórios, fluxo de status no Notion |
| Operação de Mídias Digitais | "Como Conectar o Grok Bot ao seu WeChat?" | Ponto de comando diário via dispositivo móvel | Plugin ClawBot para WeChat, long-polling iLink, despertar via Webhook |
| Operação de Mídias Digitais | "Transforme seus Tweets em um Site de Perfil Pessoal" | Extração de postagens históricas e geração/publicação de site | Fluxo de arquivos entre 4 funções, conferência baseada no texto original, geração de site estático |
| Operação de Mídias Digitais | "Comande o X com Apenas Uma Frase no WeChat" | Roteamento com 5 especialistas e distribuição por frase via WeChat | Roteamento persistente de funções, orquestração pelo Bot principal, sem substituição em caso de falha |
| Engenharia e P&D | "Como os Engenheiros Podem Usar Bem o Grok Bot?" | Mini frota de P&D e revisão contínua | 5 Bots de desenvolvimento + 1 Bot de operações, banco de dados no Notion, ciclo fechado com capturas de tela |
| Engenharia e P&D | "Qual o Sentido de Fazer Centenas de PRs por Dia?" | Desenvolvimento concorrente em múltiplas frentes e revisão de código escalonada | Desdobramento em 9 tipos de tarefas, liberação de PRs por nível de risco, Harness de engenharia |
| E-commerce e Cotidiano | "Casos Práticos do Guia de Aplicação do Grok Bot" | Painel de informações para Xianyu e entregas em múltiplos cenários visuais e textuais | Isolamento do estado real de conservação, arquivos-fonte SVG, painel HTML interativo |
| E-commerce e Cotidiano | "Relato Prático de E-commerce Cross-Border com Grok Bot" | Operações na interface da Amazon sob a perspectiva do comprador | Login com conta de comprador, pesquisa via P&R da Alexa, lista de pendências para ajuste de preços |
| Equipes e Organização | "Guia Completo \| Grok Bot do Básico ao Avançado" | De posto individual a uma matriz de operações de e-commerce | Oito elementos da descrição de cargo, transferências via /workspace, regras de aprovação |
| Equipes e Organização | "De um Único Bot a uma Organização Inteira" | Migração de ativos de Agents locais e arquitetura 1+N | Importação de Skills locais, CLI do Feishu, base de conhecimento GBrain |
| Equipes e Organização | "Construindo uma Equipe de Agents Totalmente Automatizada do Zero" | Coleta multiplataforma de conteúdos virais e colaboração 24 horas | Rastreamento de taxa de sucesso de palavras-chave, prompts de entrevista reversa, tabelas multidimensionais do Feishu |

Antes de iniciar a configuração, envie o prompt abaixo para o Bot principal **para que ele ajude a definir os limites de cada função e a estrutura dos diretórios de execução**.

```text
我打算参考以下业务场景搭建一套 Grok Bot 工作流：【填入具体业务目标】。
请按以下步骤帮我拆解：
1. 列出该流程所需的 Bot 岗位清单，明确每个角色的输入文件、交付成果和绝对禁止动作。
2. 在 /workspace 下为我规划一套清晰的目录结构，规定上下游交接的文件格式。
3. 标出涉及外部发信、数据修改、敏感登录或支付的环节，单独列出必须等待人工审批的节点清单。
4. 给出该流程第一步的测试提示词，明确要求未确认信息标注为待确认，严禁编造数据。
```

## Primeiros Passos e Mecanismos Fundamentais

### Guia Completo | Grok Bot do Zero: O Primeiro Passo

> Fonte: [Guia Completo | Grok Bot do Zero: O Primeiro Passo](https://x.com/TodayKan/status/2104789484277473522)  
> Autor: [Today🦘 @TodayKan](https://x.com/TodayKan)
O acesso de vinculação do aplicativo para desktop só aparece na página inicial e, **após a vinculação, não pode ser migrado**. Ao encontrar logins na web, use diretamente o **Take over para inserir a senha manualmente** e assumir o controle.

Regras de longo prazo devem ser incluídas na descrição; instruções temporárias ficam na conversa. Informações não fornecidas devem ser marcadas como pendentes de confirmação, eliminando o hábito de adivinhação.

Ao elaborar a primeira tarefa, é preciso definir com clareza estes cinco pontos:
- Objetivos e materiais
- Limites e entregáveis
- Pontos de confirmação humana

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)

### Como Usar o Grok Bot a Fundo em Uma Hora

> Fonte: [Como Usar o Grok Bot a Fundo em Uma Hora](https://x.com/tspy/status/2109440690862342187)  
> Autor: [yishan @tspy](https://x.com/tspy)

![Como Usar o Grok Bot a Fundo em Uma Hora](/cases-img/fs33-0.jpg)

![Como Usar o Grok Bot a Fundo em Uma Hora](/cases-img/fs33-1.jpg)
As tarefas de inspeção salvam relatórios de forma unificada em `/workspace/site-check/`. Os relatórios devem registrar os links e horários da verificação, salvar capturas de tela como evidência e separar os fatos da página de suposições.

A consolidação de habilidades cotidianas segue dois passos:
1. Use o Teach a task para gravar as ações no navegador e gerar um rascunho.
2. Complete manualmente o tratamento de dados ausentes e os limites de aprovação.

Nas inspeções rotineiras, siga a regra: **sem novas anomalias, apenas registre sem enviar notificações**, economizando cotas e evitando a fadiga de alertas.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)

### 10 Dicas Essenciais para Deixar seu Grok Bot Ainda Melhor

> Fonte: [10 Dicas Essenciais para Deixar seu Grok Bot Ainda Melhor](https://x.com/eze_is_1/status/2109850538045264151)  
> Autor: [Yize Eze @eze_is_1](https://x.com/eze_is_1)

![10 Dicas Essenciais para Deixar seu Grok Bot Ainda Melhor](/cases-img/fs37-0.jpg)

![10 Dicas Essenciais para Deixar seu Grok Bot Ainda Melhor](/cases-img/fs37-1.jpg)
**Todos os Bots compartilham o mesmo computador em nuvem; criar novos Bots por si só não garante isolamento de permissões**. Para tarefas de monitoramento periódico com lógica fixa, usar scripts puros ou linhas de comando economiza mais cota.

Tarefas longas podem usar Webhooks com Wake on Done para despertar o sistema. Para o direcionamento de tarefas, use um Bot de caixa de entrada como filtro central para distribuir os itens de acordo com o tipo para as respectivas funções.

A suspensão do sistema local pode causar a desconexão das rotinas; **ajustar o pmset do macOS e desativar o App Nap** resolve esse problema.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)

## Operação de Mídias Digitais e Marca Pessoal

### Criando uma Equipe de Mídias Digitais com o Grok Bot: Tutorial Passo a Passo｜Adrian Punk

> Fonte: [Criando uma Equipe de Mídias Digitais com o Grok Bot: Tutorial Passo a Passo](https://x.com/AdrianPunk115/status/2097311704547987756)  
> Autor: [Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![Criando uma Equipe de Mídias Digitais com o Grok Bot: Tutorial Passo a Passo](/cases-img/fs26-0.jpg)

![Criando uma Equipe de Mídias Digitais com o Grok Bot: Tutorial Passo a Passo](/cases-img/fs26-1.jpg)

Crie uma estrutura de 7 níveis de diretórios em `/workspace/content-team/` no computador em nuvem, onde 5 especialistas operam sequencialmente no pipeline:

1. Investigador de Inteligência
2. Planejador de Pautas
3. Redator Principal (**a escrita deve basear-se estritamente no Brief aprovado e no `voice.md`**)
4. Editor de Checagem de Fatos
5. Analista de Métricas e Retrospectiva

Em relação à segurança, defina limites rígidos: **toda a cadeia deve passar por validação humana obrigatória**.

- Desative diretamente as permissões de execução no computador local nas configurações
- Fixe exigências inegociáveis na descrição de cada Bot, proibindo terminantemente postagens, curtidas e respostas não autorizadas
- Bloqueie o botão de publicação da conta e todos os logins sensíveis exclusivamente na etapa de validação humana

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Como Fazer um Bom Uso do Grok Bot na Produção de Conteúdo｜Kin

> Fonte: [Como Fazer um Bom Uso do Grok Bot na Produção de Conteúdo](https://x.com/KinGao476942/status/2099736121781764594)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)
Ideal para criadores que buscam tráfego de inicialização a frio para produtos e costumam ter escassez de pautas.

1. Crie um banco de pautas no Notion com o Bot, configurando seis grupos de campos obrigatórios (link permanente da fonte, métricas públicas e nível do autor, além de motivo de adequação, desconstrução da motivação e anotação de dados faltantes). **Se os dados não forem encontrados, é obrigatório marcar como "Não encontrado"**.
2. Desconstrua conteúdos virais seguindo o framework HKRR, com foco em quatro dimensões: entretenimento/alegria, conhecimento, empatia e senso de ritmo.
3. **Inspire-se apenas na estrutura de disseminação sem copiar o texto**, mantendo o controle total do botão de publicação em suas mãos.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### Como Conectar o Grok Bot ao seu WeChat? Guia Completo para Iniciantes (Com Prompts Detalhados)｜Kin

> Fonte: [Como Conectar o Grok Bot ao seu WeChat? Guia Completo para Iniciantes (Com Prompts Detalhados)](https://x.com/KinGao476942/status/2108132811635032316)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![Como Conectar o Grok Bot ao seu WeChat? Guia Completo para Iniciantes (Com Prompts Detalhados)](/cases-img/fs29-0.jpg)

![Como Conectar o Grok Bot ao seu WeChat? Guia Completo para Iniciantes (Com Prompts Detalhados)](/cases-img/fs29-1.jpg)

Para orquestrar o Agent no computador em nuvem diretamente do celular a qualquer momento, basta usar o plugin ClawBot para WeChat. **A implantação leva apenas três etapas**:
1. Envie o prompt estruturado para o Bot principal.
2. O Bot escreve o script no computador em nuvem usando o protocolo iLink e cria o Webhook de "Ponto de Entrada de Comandos do WeChat".
3. Insira a chave na janela pop-up criptografada e escaneie o QR code para vincular.

Valide a comunicação e a tolerância a falhas de acordo com estes três critérios de aceitação:
- Utilizar long-polling de saída, **dispensando IP público e tunelamento/NAT traversal**.
- Restringir rigidamente o Bot a **respostas apenas em texto puro**.
- Predefinir no prompt a **reconexão automática para o código de erro -14**.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)

### Transforme seus Tweets em um Site de Perfil Pessoal: Tutorial Passo a Passo com Grok Bot, da Análise de Características ao Lançamento

> Fonte: [Transforme seus Tweets em um Site de Perfil Pessoal: Tutorial Passo a Passo com Grok Bot, da Análise de Características ao Lançamento](https://x.com/0xlangeai/status/2109115005069341175)  
> Autor: [Lange AI @0xlangeai](https://x.com/0xlangeai)

![Transforme seus Tweets em um Site de Perfil Pessoal: Tutorial Passo a Passo com Grok Bot, da Análise de Características ao Lançamento](/cases-img/fs32-0.jpg)

![Transforme seus Tweets em um Site de Perfil Pessoal: Tutorial Passo a Passo com Grok Bot, da Análise de Características ao Lançamento](/cases-img/fs32-1.jpg)
Adicione quatro Bots ao chat em grupo do projeto para **um fluxo em revezamento via arquivos Markdown no computador em nuvem compartilhado**:

1. O organizador de tweets extrai o conteúdo dos últimos 90 dias e salva como `tweets.md`.
2. O analista de perfil resume de 3 a 5 características e as registra em `profile.md`.
3. O designer apresenta a proposta de layout em duas colunas em `design.md`.
4. O engenheiro escreve o código e fornece a pré-visualização em múltiplos dispositivos.

**Cada julgamento de estilo feito pelo analista deve incluir obrigatoriamente o link do tweet original e o carimbo de data/hora**, com cada etapa passando por correção humana antes de ser liberada.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### Comande o X com Apenas Uma Frase no WeChat: Meus 5 Modelos de Bot Revelados

> Fonte: [Comande o X com Apenas Uma Frase no WeChat: Meus 5 Modelos de Bot Revelados](https://x.com/Chchenhao0129/status/2109258247790313478)  
> Autor: [Hardy Chen @Chchenhao0129](https://x.com/Chchenhao0129)

![Comande o X com Apenas Uma Frase no WeChat: Meus 5 Modelos de Bot Revelados](/cases-img/fs34-0.jpg)

![Comande o X com Apenas Uma Frase no WeChat: Meus 5 Modelos de Bot Revelados](/cases-img/fs34-1.jpg)
Esse método integra o plugin ClawBot para WeChat: ao enviar uma frase pelo WeChat, o Bot principal delega a tarefa automaticamente e retorna o rascunho do post no X.

Os 5 modelos de Bot cobrem toda a operação:
- Diretor de Inteligência
- Radar de Notícias de IA
- Recriação de Conteúdo para Posts
- Redação Final de Posts Curtos
- Análise de Métricas do X

1. **A lógica de roteamento e distribuição fica totalmente encapsulada no Bot principal**, utilizando o prompt de inicialização para registrar o posicionamento da conta e os IDs dos especialistas.
2. **Caso uma tarefa trave, o especialista deve relatar fielmente o motivo da falha; é estritamente proibido que o Bot principal assuma a redação por conta própria**.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)

## Engenharia, P&D e Colaboração em Código

### Como os Engenheiros Podem Usar Bem o Grok Bot?

> Fonte: [Como os Engenheiros Podem Usar Bem o Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![Como os Engenheiros Podem Usar Bem o Grok Bot?](/cases-img/fs25-0.jpg)

![Como os Engenheiros Podem Usar Bem o Grok Bot?](/cases-img/fs25-1.jpg)

A equipe da SpaceXAI configurou 5 Bots de desenvolvimento (responsáveis por mobile, desktop e a infraestrutura Harness de CI/CD) e 1 Bot de operações, Jenny, responsável por reuniões e retrospectivas.

1. **Investigação automática**: o Bot aciona autonomamente o Cloud Agent e **faz polling a cada 30 minutos em um banco de dados compartilhado do Notion** para investigar erros de CI e conflitos de merge.
2. **Liberação escalonada**: **pequenas alterações de alta confiança são mescladas automaticamente, enquanto problemas complexos são encaminhados para revisão humana**.
3. **Aceitação em ciclo fechado**: exigência obrigatória de entrega de capturas de tela reais de antes e depois das alterações.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)

### Qual o Sentido de Fazer Centenas de PRs por Dia?

> Fonte: [Qual o Sentido de Fazer Centenas de PRs por Dia? Dividi Minhas Tarefas Seguindo a Lista de Nove Categorias da Engenheira da SpaceXAI Lauren (@poteto)](https://x.com/MaiYangAI/status/2108519046446727633)  
> Autor: [Mai Yang @MaiYangAI](https://x.com/MaiYangAI)

Diante da controvérsia sobre mesclar centenas de PRs em um único dia, o engenheiro decompôs o trabalho em uma lista de nove categorias que abrangem desempenho, correção de bugs, refatoração, cadeia de ferramentas e novos recursos.

No dia a dia, evite inflar commits às cegas: **concentre sua energia nas duas extremidades — restrições de entrada e validação de saída**. Durante o desenvolvimento do ContextEcho, o autor realizou 1.020 commits em seis meses, mas apenas 18 PRs.

A liberação de alterações é dividida por nível de risco, eliminando métricas de vaidade.

| Nível de Risco da Alteração | Mecanismo de Revisão e Liberação | Divisão de Responsabilidades: Humano vs. Agent |
| :--- | :--- | :--- |
| Tarefas de baixo risco | Liberação combinada com casos de teste | Revisão e liberação automáticas pelo Agent de code review |
| Tarefas críticas e de alto risco | Validação humana e definição de direção | O humano é responsável por definir a direção, os critérios de aceitação e a experiência real |

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## E-commerce e Aplicações do Cotidiano

### Casos Práticos do Grok Bot no Dia a Dia｜Miles Ma

> Fonte: [Casos Práticos do Guia de Aplicação do Grok Bot: Anúncios no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Vídeos Curtos e Organização de Favoritos](https://x.com/miles_mazy/status/2098708209095819605)  
> Autor: [Miles Ma @miles_mazy](https://x.com/miles_mazy)

![Casos Práticos do Guia de Aplicação do Grok Bot: Anúncios no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Vídeos Curtos e Organização de Favoritos](/cases-img/fs27-0.jpg)

![Casos Práticos do Guia de Aplicação do Grok Bot: Anúncios no Xianyu, Criação de Imagens para o Xiaohongshu, Busca de Ferramentas, Vídeos Curtos e Organização de Favoritos](/cases-img/fs27-1.jpg)
O autor aprimorou as entregas para painéis web e gráficos vetoriais, executando 5 cenários com sucesso:
- Xianyu: separou o estado real de conservação das especificações oficiais, fornecendo um painel em duas colunas com lista de fotos a serem adicionadas.
- Xiaohongshu: gerou lotes de 6 cards na mesma paleta de cores, entregando arquivos-fonte SVG.
- Vídeo: criou uma página web interativa de cubo mágico, gravada e editada como um vídeo curto de 51 segundos com locução.
- Favoritos: transformou tweets em uma biblioteca de recursos em Markdown.

Para evitar falhas, **o prompt deve exigir expressamente que "todas as informações não fornecidas sejam marcadas como pendentes de confirmação"**, impedindo o exagero no estado de conservação.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

### Montando uma Equipe para a Amazon com o Grok Bot｜Zach

> Fonte: [Compartilhamento Prático de E-commerce Cross-Border com Grok Bot: Construindo uma Equipe Completa para a Amazon do Zero](https://x.com/1999Zach22/status/2110078772225667115)  
> Autor: [Zach @1999Zach22](https://x.com/1999Zach22)

![Compartilhamento Prático de E-commerce Cross-Border com Grok Bot: Construindo uma Equipe Completa para a Amazon do Zero](/cases-img/fs38-0.jpg)

![Compartilhamento Prático de E-commerce Cross-Border com Grok Bot: Construindo uma Equipe Completa para a Amazon do Zero](/cases-img/fs38-1.jpg)
Como os dados de APIs comerciais sofrem com atrasos, o autor usou o navegador no computador em nuvem para fazer login com contas de comprador e montou uma arquitetura **"1 Capitão + 12 Funções"**, interagindo diariamente apenas com o Capitão.

O Bot de inspeção simula um comprador todos os dias para executar as seguintes rotinas:
- Verificar variações de Listing e imagens principais
- Monitorar preços de concorrentes
- Fazer perguntas na interface do Alexa for Shopping para compreender a lógica de recomendação

O limite estrito de permissões é a **proibição expressa do Bot de anúncios gravar no painel administrativo ou alterar lances**; ajustes de preços e publicações de anúncios passam integralmente por listas de aprovação pendente com validação humana.

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/LG1twK03uiO00JkPk1ncQQNUnvt)

## Orquestração de Equipes e Colaboração Organizacional

### Expansão Gradual

> Fonte: [Guia Completo | Grok Bot do Básico ao Avançado](https://x.com/jinchenma_ai/status/2094984812251746424)  
> Autor: [Jinchen Ma @jinchenma_ai](https://x.com/jinchenma_ai)

![Guia Completo | Grok Bot do Básico ao Avançado](/cases-img/fs24-0.jpg)

![Guia Completo | Grok Bot do Básico ao Avançado](/cases-img/fs24-1.jpg)
Dois Bots transferem arquivos por meio de `/workspace`. A descrição de cargo define oito elementos essenciais, esclarecendo entregáveis de responsabilidade, passos de trabalho e critérios de aceitação, além de configurar pontos de aprovação humana. **Para evitar a criação prematura de cargos ociosos**, a expansão é feita em três etapas:
1. Validar e concluir uma única tarefa
2. Consolidar na forma de habilidade (Skill)
3. Criar um novo Bot quando a divisão de tarefas estiver estável

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

### Integração em Camadas

> Fonte: [De um Único Bot a uma Organização Inteira, Compartilhamento de Uso Avançado do Grok Bot: Como Conectar Computador Local, Divisão de Trabalho com IA e Base de Conhecimento](https://x.com/1999Zach22/status/2109607405696983158)  
> Autor: [Zach @1999Zach22](https://x.com/1999Zach22)

![De um Único Bot a uma Organização Inteira, Compartilhamento de Uso Avançado do Grok Bot: Como Conectar Computador Local, Divisão de Trabalho com IA e Base de Conhecimento](/cases-img/fs35-0.png)

![De um Único Bot a uma Organização Inteira, Compartilhamento de Uso Avançado do Grok Bot: Como Conectar Computador Local, Divisão de Trabalho com IA e Base de Conhecimento](/cases-img/fs35-1.jpg)
No ambiente local, Claude/Codex usa o modo Plan para refinar os SOPs e sincronizá-los com o computador em nuvem. **Adote a entrada única "1+N"** para evitar o consumo excessivo de tokens em chats em grupo; use a CLI do Feishu para entrega de comentários/anotações; conecte à base de conhecimento GBrain. Ações críticas concluem com uma lista de pendências para aprovação:

| Tipo de Atividade | Nível do Modelo |
| :--- | :--- |
| Limpeza básica e formatação | Modelo padrão |
| Atribuição estratégica central | Modelo avançado |

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)

### Pipeline Automatizado

> Fonte: [Construindo uma Equipe de Agents Totalmente Automatizada do Zero: O Processo Completo do Grok Bot, da Ativação à Colaboração Multi-IA [Guia Completo]](https://x.com/xilo2991/status/2109613437215293905)  
> Autor: [xilo @xilo2991](https://x.com/xilo2991)

![Construindo uma Equipe de Agents Totalmente Automatizada do Zero: O Processo Completo do Grok Bot, da Ativação à Colaboração Multi-IA [Guia Completo]](/cases-img/fs36-0.jpg)

![Construindo uma Equipe de Agents Totalmente Automatizada do Zero: O Processo Completo do Grok Bot, da Ativação à Colaboração Multi-IA [Guia Completo]](/cases-img/fs36-1.jpg)
O Bot principal define as configurações por meio de entrevistas reversas. **Execução de trabalho pesado em segundo plano e revisões humanas em lote assíncronas** garantem a estabilidade. O pipeline de 24 horas segue quatro etapas:
1. Estruturação de buscas e inserção no banco de dados
2. Simulação de buscas no Xiaohongshu, Bilibili e YouTube
3. Eliminação semanal de palavras-chave e registro nas tabelas multidimensionais do Feishu
4. Complementação de pautas e redação de conteúdo

[Ler artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
