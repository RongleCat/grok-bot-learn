# Artigos práticos e tweets de Tiezhu

Ao colocar o Grok Bot em prática, é muito fácil cair em **três armadilhas comuns**:
1. Acumular todas as tarefas pesadas na conversa principal, esgotando a cota de uma semana inteira em dois ou três dias.
2. Perder todas as ferramentas e o ambiente configurado caso o computador em nuvem seja resetado.
3. Adicionar vários Bots em um mesmo grupo, gerando loops de ativação mútua que esgotam o consumo instantaneamente.

Aqui estão reunidos **9 artigos práticos e 4 coletâneas sistemáticas de tweets** de Tiezhu (@cgnot996), cobrindo quatro tópicos principais: cotas de assinatura e colaboração externa, backup e recuperação de desastres, e seleção de arquitetura. Cada artigo inclui um cartão de resumo elaborado manualmente e links diretos, facilitando a cópia direta de prompts, scripts e estratégias de roteamento de carga.

## Planos de assinatura e gestão minuciosa de cotas de computação

### Mecanismo de cotas e estratégias de roteamento de carga

A cobrança oficial é feita com base em um pool compartilhado semanal. **Cada rodada de interação relê todo o histórico na íntegra**; colar documentos longos ou códigos extensos diretamente na conversa principal fará o contexto explodir, fazendo você pagar repetidamente a cada alteração subsequente.

**Mantenha na conversa principal apenas conclusões essenciais e caminhos de arquivos**, salve materiais extensos no diretório de trabalho e delegue o trabalho pesado para o segundo plano:
- Deixe a escrita de código para a ferramenta de linha de comando Grok Build.
- Deixe o monitoramento diário para scripts agendados no nível do sistema.
- Processe imagens, áudios e vídeos gerando resumos em texto puro na linha de comando antes de retornar os resultados.

Acompanhe duas métricas na rotina diária:
- Manter mais de 20% do uso disponível antes da data de renovação semanal.
- **Desativar o pagamento por uso**, eliminando loops infinitos em segundo plano e consumo ocioso por polling contínuo.

| Nível | Mensalidade | Recomendações e cotas |
| :--- | :--- | :--- |
| Plus | US$ 8/mês | Não inclui Bot; adequado apenas para desenvolvimento leve |
| Premium | US$ 30/mês | Porta de entrada para Bots; cota semanal de 4x |
| Super | US$ 100/mês | Agendamento frequente de múltiplos Agents; cota semanal de 15x |
| Ultra | US$ 200/mês | Indicado para equipes profissionais; cota semanal de 50x |

Basta enviar as seguintes regras para o seu Bot principal para que entrem em vigor:

```text
以后长资料、排查日志和中间结果都存成 /workspace/ 下的文件，回我时只给结论和文件路径，不要把原文贴回聊天。给你自己建一个 notes.md 记录角色、正在做的事和做过的决定，每做完一段就更新。面对批量处理或长流程任务，先使用 1 到 2 个最小样本进行单步验证，完成单步后必须暂停等待我确认。
```

### Análise da assinatura unificada do X: como novos usuários devem escolher e se assinantes antigos devem migrar? Tudo explicado em um artigo

O novo plano é dividido em quatro níveis: Plus, Premium, Super e Ultra.

- Escolha do nível: Para usar o Grok Bot e a automação na nuvem, **comece com o nível Premium de US$ 30 por mês**; para usuários comuns, a assinatura mensal é suficiente.
- Como evitar armadilhas: A operação na interface web é unidirecional e irreversível; **mudar para a nova assinatura desvinculará permanentemente o plano antigo**. Antes de prosseguir, verifique a frequência de chamadas a modelos de terceiros para evitar aumentos repentinos de custos.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee)

### Coletânea de tweets de Tiezhu ①: Ativação, planos e cotas

Para iniciantes que querem evitar queimar toda a cota em poucos dias, lembre-se: **a gestão de cotas de uso está acima de tudo**.

1. Na ativação, escolha a **assinatura de US$ 30**; defina um nome em chinês diretamente e o Bot responderá em chinês por padrão.
2. Para o modelo de inferência, selecione fixamente o **Grok 4.5**.
3. A colaboração entre múltiplos Bots deve ocorrer exclusivamente via comunicação ponto a ponto, evitando grupos permanentes para impedir que cada mensagem seja relida por várias partes e estoure a cota.

Fique longe destes três grandes buracos negros de consumo:
- Geração de vídeos
- Timers de alta frequência sem entregas substanciais
- Chats em grupo com múltiplos Bots

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc)

### Recapitulação do evento presencial de Hangzhou: Como fiz a cota do Grok Bot durar mais

> Fonte: [Recapitulação do evento presencial de Hangzhou: Como fiz a cota do Grok Bot durar mais](https://x.com/cgnot996/status/2096415217710461078)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Recapitulação do evento presencial de Hangzhou: Como fiz a cota do Grok Bot durar mais](/cases-img/fs09-1.jpg)

![Recapitulação do evento presencial de Hangzhou: Como fiz a cota do Grok Bot durar mais](/cases-img/fs09-2.jpg)

Para evitar que a cota semanal se esgote antes do tempo, é essencial **separar completamente a orquestração da execução**. O **Grok Bot fica responsável pelo detalhamento de requisitos e pela validação de resultados**, enquanto tarefas pesadas como escrever código são delegadas ao Grok Build em modo headless dentro da máquina virtual.

Se o login remoto na máquina virtual estiver travando, resolva em duas etapas:
1. Conclua o login normal e a autorização na máquina local primeiro.
2. Em seguida, importe as configurações que permitem migração para a máquina virtual.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/D04JwEvL7iss9UkDBvLcLuvyncf)

### Economizando ainda mais a cota do Grok Bot: Otimização extrema de tarefas agendadas

> Fonte: [Economizando ainda mais a cota do Grok Bot: Otimização extrema de tarefas agendadas](https://x.com/cgnot996/status/2107418115412046064)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Economizando ainda mais a cota do Grok Bot: Otimização extrema de tarefas agendadas](/cases-img/fs12-0.jpg)

![Economizando ainda mais a cota do Grok Bot: Otimização extrema de tarefas agendadas](/cases-img/fs12-1.jpg)

Routines agendadas que rodam ociosas com frequência quando acionadas consomem muita cota; a forma de economizar é **desacoplar completamente a verificação do julgamento**.

1. Separe as tarefas que "apenas aguardam mudanças" das Routines regulares, mantendo apenas aquelas que "devem entregar resultados no horário agendado".
2. Escreva scripts Shell leves dentro da máquina virtual e use o cron subjacente para checar **a cada meia hora**, fazendo apenas comparações básicas sem jamais chamar grandes modelos.
3. Acione o **Bot via Webhook** apenas quando uma alteração real for detectada, reduzindo o consumo ocioso de rotina a zero.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)

### Guia completo para iniciantes: Duração ultra-longa da cota do Grok Bot (envie diretamente para o Bot!)

> Fonte: [Guia completo para iniciantes: Duração ultra-longa da cota do Grok Bot (envie diretamente para o Bot!)](https://x.com/cgnot996/status/2108504325609984233)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Guia completo para iniciantes: Duração ultra-longa da cota do Grok Bot (envie diretamente para o Bot!)](/cases-img/fs13-0.jpg)

![Guia completo para iniciantes: Duração ultra-longa da cota do Grok Bot (envie diretamente para o Bot!)](/cases-img/fs13-1.jpg)

Como o Bot relê todo o histórico em cada conversa, a cota se esgota em dois ou três dias. Estas 12 regras testadas na prática podem conter o consumo imediatamente:

1. **Para imagens, áudios e vídeos, converta primeiro em resumos textuais na linha de comando**, em vez de enviar dados multimodais diretamente.
2. Escreva documentos extensos e logs de depuração em arquivos; envie de volta no chat apenas conclusões breves e caminhos de arquivo.
3. **Desative proativamente o pagamento por uso na conta ou reduza o limite**, evitando faturas fora de controle.
4. **Defina um limite máximo de 2 tentativas em caso de erro**; interrompa imediatamente em caso de falhas consecutivas e acione intervenção humana, eliminando loops infinitos e processamento ocioso.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Ingestão automatizada e redes de colaboração externa

### Pipelines de automação e configurações de colaboração

Com Webhooks configurados, o Grok Bot atua como um **nó de automação 24/7**.

1. Crie uma tarefa de rotina no Bot, escolha "Quando um Webhook for disparado" como gatilho, salve e obtenha a URL da API e a chave Bearer.
2. No celular, use o aplicativo Atalhos para configurar "Obter conteúdo do URL", enviando texto ou links em JSON via método POST.
3. No WeChat, se não houver painel de compartilhamento, leia a área de transferência; para anexos grandes ou várias imagens, salve em um drive em nuvem temporário para obter links públicos, permitindo que o Bot baixe e descompacte na nuvem.
4. Para o Feishu, utilize conexões persistentes (long connection), dispensando IP público e servidores próprios, configurando gatilhos de campainha para despachar tarefas direcionadas.

**Critérios de aceitação**:
- No celular, envie e saia sem precisar esperar.
- O Bot realiza captura assíncrona na nuvem, extração de frames, transcrição, armazenamento no banco de conhecimento e fornece um recibo de ingestão.
- Em chats de grupo, responder apenas quando for mencionado diretamente (@) ou quando for uma mensagem para todos.

Envie o prompt abaixo para **gerar automaticamente um endpoint de recebimento**:

```text
帮我创建一个 Webhook 触发的例行任务。快捷指令会用 POST 请求发来一个 JSON，里面包含一个字段 info。info 可能是我输入的文字，也可能是一个文件下载链接，比如微信聊天记录压缩包、截图、录音。收到后：如果是链接就先下载文件再读取，压缩包先解压；然后整理出要点，收录进知识库，最后给我一份回执，写清楚收录了什么、存在哪里。
```

### Grok Bot Webhook + Atalhos: Construção de pipeline de ingestão automática de conhecimento

> Fonte: [Grok Bot Webhook + Atalhos: Construção de pipeline de ingestão automática de conhecimento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Atalhos: Construção de pipeline de ingestão automática de conhecimento](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Atalhos: Construção de pipeline de ingestão automática de conhecimento](/cases-img/fs06-1.jpg)

Ideal para usuários Apple arquivarem textos, imagens e vídeos a qualquer momento: **envie pelo celular e saia, enquanto a nuvem cuida da transcrição, extração de frames e organização**.

1. Crie uma tarefa de rotina no Grok Bot para obter a URL exclusiva do Webhook e a chave Bearer.
2. No app Atalhos do celular, configure uma requisição POST para empacotar e enviar links ou textos.
3. Para aplicativos como o WeChat que não possuem painel de compartilhamento do sistema, **crie um atalho com pop-up que lê a área de transferência** para acionar a coleta.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)

### Integrando o histórico do WeChat ao Grok Bot: Versão avançada com Atalhos

> Fonte: [微信聊天记录打通 Grok Bot：快捷指令进阶版](https://x.com/cgnot996/status/2107039351519707602)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Integrando o histórico do WeChat ao Grok Bot: Versão avançada com Atalhos](/cases-img/fs11-0.png)

![Integrando o histórico do WeChat ao Grok Bot: Versão avançada com Atalhos](/cases-img/fs11-1.jpg)

Esta solução utiliza a cadeia "Atalhos + drive em nuvem temporário + Webhook".

1. Mescle e encaminhe mensagens no WeChat para gerar um ZIP, e o atalho faz o upload automático para um armazenamento temporário na rede pública.
2. O Webhook notifica o Bot para baixar e descompactar, extrair os pontos principais, armazenar no banco de conhecimento e retornar um recibo estruturado.

**Antes de registrar, é obrigatório abrir e carregar manualmente todas as imagens e arquivos no WeChat** para evitar o envio de pacotes vazios e perda de dados. Essa ponte pela rede pública também elimina as diferenças de caminhos de armazenamento entre celulares e computadores.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb)

### Tutorial completo de integração do Grok Bot da equipe ao Feishu (com template de gerenciador do Feishu)

> Fonte: [Tutorial completo de integração do Grok Bot da equipe ao Feishu (com template de gerenciador do Feishu)](https://x.com/cgnot996/status/2109247903785198076)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Tutorial completo de integração do Grok Bot da equipe ao Feishu (com template de gerenciador do Feishu)](/cases-img/fs15-0.jpg)

![Tutorial completo de integração do Grok Bot da equipe ao Feishu (com template de gerenciador do Feishu)](/cases-img/fs15-2.jpg)

**Sem necessidade de IP público ou servidores próprios**, conecte 3 Bots ao Feishu usando conexões persistentes (long connection) do Feishu e o Python SDK oficial via leitura de QR code, sem precisar configurar backends. Cada Bot possui um gatilho de campainha independente, com o gerenciador de aplicativos mantendo o registro geral.

- **Restrinja rigorosamente o encaminhamento apenas a menções diretas (@) a si mesmo ou a todos**, evitando que conversas paralelas no grupo causem consumo ocioso do modelo.
- **Envie cartões interativos diretamente nos nós críticos de confirmação**, permitindo a aprovação com um clique em botões e eliminando o incômodo de alternar entre interfaces.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/F2VXw4hVbirRUjk5QgFcWS0jnJg)

## Recuperação de desastres na máquina virtual e backup de ativos de memória

### Mecanismo de recuperação de desastres e classificação de ativos

Todos os Bots compartilham a mesma base Linux (Xeon 8 núcleos 8 threads, 16 GB de RAM e 128 GB de disco, segundo o autor, não verificado). **Diferentes sessões de Bot são independentes, mas o sistema de arquivos subjacente é compartilhado**; não há exportação nativa oficial.

| Cenário | O que é preservado | O que é perdido e impactos |
|---|---|---|
| Atualização do sistema | Diretório de trabalho e algumas credenciais | Processos residentes, tarefas agendadas e pacotes globais são apagados |
| Reset completo da máquina | Nada é preservado | Disco do sistema é formatado e todos os dados não persistentes são perdidos |

Backups manuais não são viáveis; **é fundamental transformar a lógica de reconstrução em código**. Após um desastre, execute o script de entrada principal no novo ambiente e restaure a operação por meio de verificações de integridade (health checks).

| Ativo | Caminhos e arquivos | Estratégia de recuperação e armadilhas |
|---|---|---|
| Configurações de memória | Git privado: agent-spec.md, profile.md, MEMORY.md | Carregadas no novo Bot conforme a lista; fidelidade de restauração de cerca de 80% (segundo o autor, não verificado) |
| Serviços residentes | Git privado vm-services/: REGISTRY.md, registry.json, código-fonte | Reinstalação idempotente via restore-*.sh e validação por health checks |
| Credenciais de acesso | Local ~/.agents/secrets/: .env (chmod 600) | **Terminantemente proibido adicionar ao Git ou a logs**; preenchimento manual pelo operador após o desastre com base no registro geral |

Configure o prompt a seguir em um Bot dedicado de operações para manter o registro geral de serviços e os scripts de recuperação:

```text
你是「虚拟机服务管家」，负责维护这台机器部署的所有第三方服务。你维护一份登记总账（REGISTRY.md 与 registry.json）、每个服务的独立恢复脚本（restore/restore-<服务>.sh，必须幂等可重复运行）、总入口 restore/restore-all.sh，以及一份排除日志和密钥的自写源码备份 service-src/。总账记录服务 ID、用途、安装方式、启停命令、健康检查命令和密钥存放路径。仓库严禁存入明文密钥。收到恢复指令后，按依赖顺序跑脚本并逐项交出健康检查验收清单。
```

### A grande evacuação do Grok Bot: Uma solução completa de backup de sistema Agent

> Fonte: [A grande evacuação do Grok Bot: Uma solução completa de backup de sistema Agent](https://x.com/cgnot996/status/2098222795847315967)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![A grande evacuação do Grok Bot: Uma solução completa de backup de sistema Agent](/cases-img/fs10-0.jpg)

![A grande evacuação do Grok Bot: Uma solução completa de backup de sistema Agent](/cases-img/fs10-1.jpg)

Como a plataforma oficial não oferece exportação de memória com um clique, esta solução aciona o Bot para ler o contexto, gravar personas, decisões e snapshots de tarefas em Markdown e fazer push em camadas para um repositório Git privado.

- Os backups armazenam apenas texto puro, deixando o controle de versão para o Git.
- **O repositório deve ser verificado contra vazamento de chaves, registrando apenas caminhos de tokens sem manter texto simples**.
- **A reconstrução em uma nova conta atinge cerca de 80% de fidelidade**, permitindo também a migração direta para sistemas locais.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Ferramentas sumiram após reset da máquina virtual do Grok Bot? Tutorial de backup e recuperação (com prompts inclusos)

> Fonte: [Ferramentas sumiram após reset da máquina virtual do Grok Bot? Tutorial de backup e recuperação (com prompts inclusos)](https://x.com/cgnot996/status/2108874629163229628)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Ferramentas sumiram após reset da máquina virtual do Grok Bot? Tutorial de backup e recuperação (com prompts inclusos)](/cases-img/fs14-0.jpg)

![Ferramentas sumiram após reset da máquina virtual do Grok Bot? Tutorial de backup e recuperação (com prompts inclusos)](/cases-img/fs14-1.jpg)

Após o reset de um computador em nuvem, **transformar a lógica de reconstrução de serviços em código** é a abordagem mais tranquila. Crie o registro geral de serviços `REGISTRY.md` em um repositório Git privado, documentando dependências de 20 projetos, comandos de inicialização/parada e código-fonte livre de credenciais, além de elaborar scripts de restauração idempotentes.

1. Distinga claramente os limites de perda entre atualizações do sistema e reset completo da máquina.
2. Execute os scripts de restauração na ordem correta: pacotes básicos do sistema, ferramentas CLI e, por fim, processos residentes.
3. **Faça uma verificação de integridade imediatamente após cada etapa**; ao encontrar uma falha, pule-a temporariamente e anote-a na lista, **evitando resets cegos e desnecessários**.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## Evolução de arquitetura, prática de negócios e seleção de ecossistema

### Divisão de trabalho em matriz e avaliação de seleção

Ao trabalhar com Agents no dia a dia, mantenha o princípio de "uma função por integrante". **Evite empilhar escrita de código, scraping de dados, arquivamento pessoal e postagens no mesmo Bot**; os prompts entrarão facilmente em conflito e o contexto excessivamente longo desvirtuará o comportamento do modelo.

Para a escolha de plataformas, você pode consultar a analogia de Tiezhu comparando "computadores prontos de marca" e "PCs montados (DIY)":

| Abordagem | Produtos representativos | Vantagens | Cenários aplicáveis e limitações |
| :--- | :--- | :--- | :--- |
| Computador pronto de marca | Grok Bot, Muse | Computador em nuvem pronto para uso (out-of-the-box), sem necessidade de gerenciar sessões remotas ou integrações de aplicativos | Sujeito a limites e cotas semanais oficiais; ideal para quem depende fortemente de distribuição em redes sociais e hospedagem em nuvem |
| PC montado (DIY) | Hermes de código aberto local, DS Bot | Liberdade para integrar modelos de código aberto, sem limites de cota, privacidade máxima de dados | Exige construir o sistema e ajustar scripts por conta própria; indicado para desenvolvimento de código puro e fine-tuning de modelos personalizados |

Para a implementação prática nos negócios, mantenha os limites de segurança e automação:
- Torne totalmente automáticas as tarefas mecânicas de scraping de dados e preenchimento de planilhas.
- Para operações sociais públicas ou movimentações financeiras, mantenha obrigatoriamente um portão de aprovação humana.
- **Publicações devem usar estritamente a API oficial; é terminantemente proibido simular login via navegadores headless no computador em nuvem**, prevenindo o banimento de contas.

Referência de divisão de funções e prevenção de armadilhas:

| Função de negócio | Bot dedicado | Responsabilidades | Limites de segurança e configurações preventivas |
| :--- | :--- | :--- | :--- |
| Código e operações | Administrador de repositório, Monitor de SEO | Monitorar projetos diariamente, fazer merge automático de PRs, completar diretrizes | **Verifique o calendário das tarefas agendadas**, evitando configurar por engano a execução apenas em dias úteis, o que paralisaria as operações no fim de semana |
| Vida pessoal e arquivamento | Gerenciador financeiro, Ingestor de base de conhecimento | Receber imagens e textos enviados por Atalhos e inseri-los em tabelas multidimensionais | Defina IDs aleatórios de alta entropia para hospedagem temporária de imagens; não trafegue dados confidenciais ou privados por intermediários públicos |
| Colaboração e orquestração | Editor-chefe de artigos, Gerenciador de máquina virtual | Decompor pautas, coordenar múltiplos Bots, gerenciar o registro geral de backend | Utilize autorização por código de dispositivo (Device Code) para ferramentas externas, impedindo que duas máquinas derrubem a sessão de login uma da outra |

### Coletânea de tweets de Tiezhu ②: Recursos do produto e observações de versão

Autor: 铁柱AGI (coletânea de tweets) | Para quem é recomendado: Exploradores técnicos interessados em mecanismos de ambiente subjacentes e que desejam dominar a integração multidispositivo e a solução de problemas de rede

A coletânea documenta a evolução da infraestrutura do Grok Bot. **Todos os Bots sob a mesma conta compartilham o mesmo computador em nuvem Linux**, com configuração de 8 núcleos, 16 GB de RAM e disco rígido de 128 GB, com sessões de desktop independentes entre si. O texto também aborda como solicitar caixas de correio exclusivas, invocar a busca nativa do X e diagnosticar redes de saída.

Guarde dois pontos fundamentais na resolução de problemas do ambiente:
- **Se o painel de Webhook não responder ao clique, envie diretamente uma instrução para que o Bot responda com o link direto.**
- As configurações essenciais do ambiente e os scripts personalizados devem convergir para caminhos persistentes, evitando perdas com a substituição do sistema subjacente.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

### Coletânea de tweets de Tiezhu ③: Casos de uso e práticas reais

Autor: 铁柱AGI (coletânea de tweets) | Para quem é recomendado: Praticantes em busca de inspiração para implementação em negócios e que desejam evitar banimento de contas em automações e loops infinitos

Tiezhu registrou mais de dez funções de Bot em operação real, incluindo inspeção de repositórios e relatórios diários de SEO, além de coleta no WeChat, contabilidade em tabelas multidimensionais e chamadas de API para montagem de imagens, fornecendo uma regra de implementação em quatro etapas, desde a configuração de função única até o backup de recuperação de desastres persistente.

Para uma operação estável, duas normas de manutenção devem ser seguidas:
- **A publicação de conteúdo deve ser feita estritamente pela API oficial; é terminantemente proibido simular postagens com navegadores headless dentro da máquina virtual**, prevenindo restrições na conta.
- **Ferramentas externas de linha de comando devem ser autorizadas uniformemente com código de dispositivo (Device Code)**, evitando quedas de conexão causadas pela disputa de credenciais entre duas máquinas.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

### Coletânea de tweets de Tiezhu ④: Comunidade, ecossistema e comparação com concorrentes

Autor: 铁柱AGI (coletânea de tweets) | Para quem é recomendado: Arquitetos avaliando escolhas entre múltiplos frameworks de Agent e procurando recursos de código aberto

Tiezhu comparou horizontalmente os principais frameworks de Agent com o Grok Bot. O Grok Bot segue a abordagem de máquina pronta, vindo com computador em nuvem pronto para uso, mas limitado por cotas; computadores montados (DIY), como o Hermes, oferecem alto controle, mas exigem manutenção própria.

O texto também resume a experiência do repositório awesome-grok-bot, que utiliza inspeção autônoma por Bot para catalogar eventos e documentações.

Um truque prático para expandir a base de conhecimento da equipe: **envie diretamente frameworks de código aberto de alta qualidade e tutoriais externos como contexto para o Bot estudar**, alinhando o Agent perfeitamente ao seu fluxo de trabalho.

[Ler o artigo original](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg)
