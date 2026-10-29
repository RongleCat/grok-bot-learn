# Capítulo 3: Instalação, Login e o Primeiro Bot

**Confirme se a assinatura inclui os benefícios do Bot**, caso contrário não haverá ponto de entrada; se o login entrar em loop, verifique as configurações de privacidade. Não crie um "assistente para tudo" sem restrições para não desperdiçar sua cota semanal à toa.

1. Instale o cliente desktop e o aplicativo móvel, eliminando erros de login
2. **Crie um Bot dedicado preenchendo o contrato de seis linhas**
3. Envie a primeira tarefa com salvamento em disco e faça a validação com base na lista de verificação


![Instalação, login e o primeiro Bot](/info/03-install.png)

## Verificação do Plano de Assinatura e Condições de Acesso

Antes de fazer o download, verifique a qualificação da sua conta: **o Grok Bot só pode ser usado com uma assinatura válida vinculada**.

| Nome do Plano | Preço | Inclui Grok Bot | Descrição da Cota |
| :--- | :--- | :--- | :--- |
| The X Plus | $8 / mês | Não | Apenas conversas com modelos comuns, sem acesso ao Bot |
| The X Premium | $30 / mês ($300 anual) | Sim | Cota de 4x, limite mínimo de entrada para uso individual |
| The X Super | $100 / mês ($1000 anual) | Sim | Cota de 15x |
| The X Ultra | $200 / mês ($2000 anual) | Sim | Cota de 50x |
| Cursor Pro / Pro+ / Ultra | Consulte os preços no site oficial | Sim | Cota semanal de acordo com o plano |
| Cursor Teams (assentos self-service) | Consulte os preços no site oficial | Sim | Membros compartilham a cota da equipe |

- **O plano Plus de $8 mensais não inclui os recursos do Bot**; comprar esse plano não dará acesso ao serviço.
- **A cota vinculada ao X e a cota da assinatura do Cursor não são cumulativas**; o faturamento do sistema adota automaticamente o limite mais alto entre os dois para o uso semanal.

Para entender os mecanismos básicos dos planos, consulte os artigos da comunidade [1.1 O que é o Grok Bot: Entenda em uma página](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc) e [Guia Extenso | Começando com o Grok Bot do Zero pela Primeira Vez](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg).

## Download e Instalação no Desktop

![Download e instalação no desktop](/info/03-install-s2.png)

O macOS é compatível com Apple Silicon (série M) e Intel; Windows e Linux são compatíveis com x64 e Arm64 (no Windows, recomenda-se ativar a aceleração de hardware).

1. Acesse `cursor.com/dashboard/bot` ou vá diretamente para `x.ai/bot` para baixar o instalador. **Se não tiver permissão no dispositivo da empresa, solicite ao administrador**.
2. No macOS, arraste o aplicativo baixado para a pasta `Applications`; no Windows e Linux, execute o assistente de instalação.
3. **Ao abrir o cliente e ver a tela de login, está pronto**. Para instruções detalhadas, consulte o documento [Início Rápido do Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started).

## Login na Conta e Configuração do Modo de Privacidade

1. Abra o cliente e clique em **Log In** (Entrar), autenticando-se no navegador diretamente com sua conta do Cursor; o SSO corporativo será aplicado automaticamente. Se você tiver um assento Grok Business, selecione **Sign in with Grok** para fazer login.
2. Concluída a autenticação, acesse as "Configurações" do cliente; se você conseguir ver o e-mail da conta e o status do plano, significa que deu certo.

**O modo de privacidade legado (Privacy Mode (Legacy)) precisa ser alternado para o Privacy Mode atual para continuar**. Usuários individuais só precisam confirmar na janela pop-up; membros de equipes precisam que o administrador faça a atualização em Team Settings.

Para explicações detalhadas, consulte os documentos oficiais [Introdução](https://cursor.com/cn/help/grok-bot/onboarding) e [Fazer Login no Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

## Problemas Comuns de Login e Resolução de Falhas

Reinstalar sem critério não resolve; a maioria dos casos decorre de problemas de cache ou de atualização de sessão.

1. Atualize o cliente para a versão mais recente e faça login novamente.
2. Limpe os cookies de `cursor.com` e `x.ai` ou use o modo anônimo.
3. Acesse `x.ai/bot` para confirmar se a versão web consegue estabelecer uma sessão.
4. Se acabou de alterar a assinatura, **aguarde de 30 a 60 minutos**; o erro desaparecerá após a atualização.

Erros consecutivos na verificação por telefone acionarão o bloqueio de controle de risco, o qual não se resolve sozinho. Se a resolução de problemas falhar ou você encontrar erros de OAuth, **abra um chamado na página de suporte**, anexando seu e-mail e capturas de tela, além de detalhar a versão e as etapas seguidas.

Para mais detalhes, consulte [Fazer Login no Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

## Instalação no iOS e Sincronização entre Dispositivos

### Instalação e Login
1. O sistema operacional deve ser o **iOS 18 ou superior**.
2. Pesquise por Grok Bot na App Store e instale. Faça login com a mesma conta do Cursor para sincronizar automaticamente, **sem necessidade de pagar novamente**.

### Divisão de Trabalho entre Dispositivos
- O celular é ideal para monitoramento rotineiro: permite visualizar a tela em tempo real, assumir o controle (Take over) para inserir códigos de verificação, conceder aprovações (Allow / Deny) ou iniciar e parar Routines.
- **Operações aprofundadas precisam ser feitas no desktop**: tutoriais em gravação de tela de até 10 minutos (Teach a task), testes de Routine (Test run) e manutenção do computador na nuvem (Update / Recover).

### Gerenciamento de Notificações
- **Silenciar um Bot específico**: na tela de chat, clique no nome no topo e desative **Notifications**; também é possível desativar enviando uma mensagem pelo desktop.
- **Desativação global**: desative a permissão de notificações do Grok Bot nos "Ajustes" do sistema.

Para mais detalhes, consulte [Grok Bot para Dispositivos Móveis](https://cursor.com/cn/help/grok-bot/mobile).

## Conhecendo a Infraestrutura Compartilhada e Criando o Primeiro Bot

![Conhecendo a infraestrutura compartilhada e criando o primeiro Bot](/info/03-install-s6.png)

Cada usuário pagante tem uma máquina virtual dedicada e persistente na nuvem, equipada com Linux independente, navegador, terminal e disco persistente (a configuração de testes iniciais era de cerca de 8 núcleos e 16 GB de RAM, não confirmada oficialmente; consulte as informações oficiais para dados exatos).

Esta máquina tem três limites físicos que impactam diretamente a operação:
- **Todos os Bots compartilham a mesma máquina**: compartilham o `/workspace` e a mesma sessão ativa do navegador; criar Bots separados serve apenas para dividir funções, sem isolamento de segurança.
- **A colaboração entre Bots exige gravação de arquivos em disco**: os históricos de chat não se comunicam entre si; o Bot A precisa gravar os resultados em arquivos no `/workspace` para que o Bot B possa lê-los e continuar a tarefa.
- **Suporte para visualização a qualquer momento e intervenção em tempo real**: o lado direito pode expandir a tela do computador na nuvem para que você assuma o controle sempre que houver senhas, captchas ou autenticações de pagamento; nunca digite credenciais na caixa de texto.

No primeiro login, um **Grok Bot** padrão será gerado automaticamente. As etapas para criar e configurar manualmente são as seguintes:

1. **Criar novo**: clique no **+** no topo da barra lateral (ou Cmd+N) e selecione **Create new Bot** (Criar novo Bot). Digitar o nome diretamente no campo de texto também permite clicar e criar.
2. **Renomear e definir etiqueta**: clique com o botão direito e selecione **Rename Bot** (Renomear robô), ou clique no nome no topo para abrir o painel e alterar. Abaixo, é possível configurar a etiqueta de cargo (Label; no celular, Title (optional)).
3. **Alterar o avatar**: clique no nome no topo para acessar os detalhes e clique no avatar; é possível escolher figuras geométricas integradas, gerar uma imagem por meio de uma descrição em texto ou enviar uma imagem local de até 25 MB (no celular, é possível escolher fotos da biblioteca, gerar ou remover).
4. **Definir atribuições**: **os Bots individuais não contam mais com uma página de configurações própria; as regras de longo prazo devem ser explicadas diretamente na primeira mensagem, solicitando que ele as memorize**. Os Bots de equipe ainda mantêm uma área fixa de descrição na seção "Sobre" (About) dos detalhes.

- [Alterar Nome, Avatar e Responsabilidades do Bot](https://cursor.com/cn/help/grok-bot/edit-bot)
- [Artigo Completo | Grok Bot do Iniciante ao Avançado | Jin Chenma](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

## Definindo Responsabilidades: O Contrato Padrão de Seis Linhas

### Estrutura do Contrato e Modelo

Iniciantes não devem fornecer títulos vagos: **escreva as seis restrições centrais diretamente na primeira mensagem**, instruindo-o a memorizá-las como regras permanentes.

1. Own (Responsabilidade por resultados): defina claramente os indicadores específicos sob sua responsabilidade a longo prazo, evitando transformá-lo em um assistente genérico.
2. Sources (Fontes confiáveis): restrinja a consulta exclusivamente a sites oficiais ou links especificados, proibindo o uso de fontes não verificadas.
3. Output (Formato de entrega): determine o caminho de salvamento, regras de nomenclatura e limite de palavras do resumo.
4. Approval (Linha vermelha de aprovação): ações de alto risco, como envio de e-mails, submissão de formulários ou exclusão de arquivos, devem aguardar a aprovação humana via pop-up.
5. Failure (Tratamento de exceções): ao encontrar páginas fora do ar ou dados ausentes, deve registrar isso explicitamente, sendo estritamente proibido supor ou inventar informações.
6. Never (Restrições absolutas): proibido modificar arquivos de origem, proibido resumir com base em memórias do próprio treinamento e proibido clicar em botões de pagamento.

Após nomear o Bot, substitua os campos do modelo e envie diretamente.

::: details Estrutura do contrato e modelo
```text
请牢记你的长期工作职责，在今后的工作中始终遵循以下要求：

Own: 负责监控目标清单的每周功能与定价变动，输出结构化对比材料。
Sources: 仅限使用目标官方网站的定价页、Changelog 页面以及我通过附件提供的官方说明文档。
Output: 提炼核心动态，附带核对日期与原始出处链接，长文本与数据表格必须保存至 /workspace/research/ 下的 Markdown 文件中，对话框中只发简要完成汇报。
Approval: 涉及发送任何邮件、对外发帖、提交表单、删除文件或进行任何费用支付前，必须停下来等待我的人工批准。
Failure: 若目标页面无法访问或内容缺失，在报告中明确标注为“未取得一手数据”，严禁推测或编造任何功能与价格。
Never: 严禁修改我上传的任何源文件，在源系统可访问时严禁依赖自身训练记忆进行主观概括。

今后的工作中请记住这些要求。
```
:::

### Casos Práticos

- Jin Chenma, em [Artigo Completo | Grok Bot do Iniciante ao Avançado | Jin Chenma](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee), **separa rigorosamente as responsabilidades de longo prazo das demandas pontuais**.

  As regras permanentes controlam fontes e entregas, enquanto as mensagens da sessão apenas atribuem tópicos específicos de pesquisa; caso faltem dados primários, isso é declarado diretamente, sendo estritamente proibido tentar adivinhar números.
- Today, em [Guia Extenso | Começando com o Grok Bot do Zero pela Primeira Vez](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg), estabeleceu limites de segurança, **isolando operações somente leitura daquelas com consequências externas**.

  Pesquisa apenas um concorrente por vez, anexando links de fontes públicas e distinguindo com clareza fatos de suposições; qualquer ação que envolva login ou pagamento é pausada aguardando confirmação.

Para regras de evolução, consulte [1.1 O que é o Grok Bot: Entenda em uma página](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc).

## Enviando a Primeira Tarefa Real

![Enviando a primeira tarefa real](/info/03-install-s8.png)

**Comece com tarefas pequenas**. Ao elaborar uma tarefa, lembre-se dos 5 elementos essenciais: explique claramente o objetivo e as entradas, mantenha estritamente como somente leitura (proibido alterar arquivos-fonte, registrar contas e efetuar pagamentos), defina as especificações de salvamento em disco e indique os pontos de intervenção manual.

Para o resumo de anexos, envie:
```text
用五个要点总结这份文档。
在单独的部分列出每个日期、决策和未解决的问题，并为每项注明对应章节出处。
不要更改源文件。
```

Para pesquisar preços de concorrentes e salvar em disco, envie:
::: details Enviando a primeira tarefa real
```text
【目标】
调研 3 款主流代码编辑器（Cursor、VS Code、Zed）在 2026 年的最新公开定价方案与核心 AI 功能，产出一份选型对比参考材料。

【材料】
1. 仅限使用上述三款产品官方网站的定价页、功能介绍页与官方文档；第三方博客仅作为辅助索引，必须找到官方页面核实。
2. 记录每一项数据的原始官方 URL 与数据核对日期。

【边界】
1. 纯只读检索，严禁注册任何账号，严禁开启任何试用，严禁输入任何支付信息。
2. 遇到需要登录才能查看的页面，直接跳过并记录在未核实清单中。
3. 严禁改动 /workspace 下已有的其他项目文件。

【交付规格】
1. 在 /workspace/editor-research/ 目录下生成对比报告文件 comparison.md。
2. 报告内包含一张 Markdown 数据表格，表头列定义为：产品名称、方案档位、月付价格、年付价格、核心功能特征、官网来源链接、核对日期。
3. 表格下方附带一份 400 字以内的中文总结，指出各产品主要差异，并单独开辟一节列出“未核实或存在矛盾的信息”。
4. 对话框中仅需回复已完成落盘的简短提示及文件绝对路径。

【暂停确认节点】
1. 遇到必须登录、验证码拦截或点击付费的操作时，立刻停下并提示我接管。
2. 官网信息前后出现明显矛盾且无法核实时，停下说明情况由我判断。
```
:::

Ao encontrar logins, 2FA ou captchas deslizantes:
1. **Clique em Take over para resolver manualmente**; após concluir, clique em I'm done para continuar, ou em Skip para ignorar.
2. Após a execução, **confirme se `/workspace/editor-research/comparison.md` foi salvo integralmente**.

Para diretrizes, consulte [Como Usar o Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started) e [Primeiros Passos](https://cursor.com/cn/help/grok-bot/onboarding).

## Armadilhas Comuns

1. O plano Plus de $8 não inclui o Bot; **é obrigatório escolher o plano Premium de $30/mês**.
2. Todos os Bots compartilham o computador na nuvem e a cota; faça um funcionar primeiro antes de criar dezenas que entrem em conflito entre si.
3. Nunca envie senhas ou API Keys na janela de chat; utilize o Take over para assumir a digitação ou preencha os cartões de segurança.
4. Textos longos **devem ser sempre salvos em arquivos Markdown no `/workspace`**, evitando poluir o contexto.
5. Se houver erro de login, não reinstale: limpe os cookies de `cursor.com` e `x.ai` ou aguarde de 30 a 60 minutos.
6. **Diferentes Bots compartilham a máquina virtual e as sessões do navegador**, não havendo isolamento de permissões.
7. Teach a task, Test run e a recuperação do sistema são recursos exclusivos do cliente desktop, não estando disponíveis no iOS.

## Como Fazer a Validação Final

1. Acesse Usage & Billing: o plano pago deve estar ativo e o consumo dentro da normalidade.
2. A tela do lado direito no desktop abre normalmente, sem erros de Reconnecting.
3. No iPhone (iOS 18+), acesse a mesma conta do Cursor: não deve haver solicitação para uma nova compra.
4. Envie o contrato de seis linhas: o Bot deve responder expressamente que memorizou as regras de longo prazo.
5. O computador na nuvem gera os arquivos solicitados no `/workspace` de acordo com as instruções.
6. Ao encontrar ações como login, o Bot pausa ativamente e exibe o cartão **Action needed**.
7. Ao fornecer intencionalmente links quebrados, o relatório indica claramente **Dados primários não obtidos** sem inventar informações.

## Leituras Complementares

### Capítulos Relacionados

- [Capítulo 4: Delegando Tarefas: Mensagens, Anexos e uma Boa Passagem de Bastão](/part1/04-handoff)
- [Capítulo 25: Perguntas Frequentes e Solução de Problemas](/part4/25-faq)

### Páginas Oficiais
- [Início Rápido do Grok Bot (Get Started)](https://cursor.com/cn/docs/grok-bot/get-started)
- [Primeiros Passos (Onboarding)](https://cursor.com/cn/help/grok-bot/onboarding)
- [Fazer Login no Grok Bot (Sign In)](https://cursor.com/cn/help/grok-bot/sign-in)
- [Grok Bot Mobile (Mobile)](https://cursor.com/cn/help/grok-bot/mobile)
- [Alterar Nome, Avatar e Responsabilidades do Bot (Edit Bot)](https://cursor.com/cn/help/grok-bot/edit-bot)

### Práticas da Comunidade
- [1.1 O que é o Grok Bot: Entenda em uma página](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [Artigo Completo | Grok Bot do Iniciante ao Avançado | Jin Chenma](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
- [Guia Extenso | Começando com o Grok Bot do Zero pela Primeira Vez](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)
