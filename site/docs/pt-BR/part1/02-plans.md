# Capítulo 2 Planos e Assinaturas: Escolha o Nível Certo Primeiro

Iniciantes costumam enfrentar três armadilhas comuns na hora da contratação:
- Comprar o plano de entrada mais barato e, ao abrir o cliente, não encontrar o acesso aos agentes.
- **A assinatura do Cursor e a cota semanal do SuperGrok não se acumulam; o sistema considera apenas o plano mais alto.**
- Clicar em fazer upgrade dentro do app mobile não permite a troca e ainda pode causar a perda do limite de uso existente para modelos de terceiros.

O funcionamento do Grok Bot depende de cotas. **Se o limite semanal se esgotar e a proteção sob demanda não estiver configurada, as tarefas automatizadas na nuvem são interrompidas imediatamente.**

A partir de 12 de outubro de 2026, a empresa passou a adotar a assinatura unificada The X Subscription, dividida em um nível gratuito e quatro níveis pagos.


![Planos e Assinaturas: Escolha o Nível Certo Primeiro](/info/02-plans.png)

## Qual plano de assinatura é necessário para usar o Grok Bot? {#统一订阅全貌-the-x-subscription-的四档与免费档}

**A assinatura unificada divide-se em quatro níveis: Plus, Premium, Super e Ultra. Como o plano Plus não inclui o Grok Bot de forma alguma, o ponto de partida para executar tarefas de automação deve ser o plano Premium de US$ 30/mês.**

![Visão geral da assinatura unificada: os quatro níveis do The X Subscription e o plano gratuito](/info/02-plans-s1.png)

### O que é

A partir de 12 de outubro de 2026, os planos foram consolidados no The X Subscription, onde o pagamento anual equivale a 10 vezes o valor mensal.

Calculado pelo uso por dólar (com Plus como base 1, Premium cerca de 1,07, Super cerca de 1,2 e Ultra cerca de 2,0; relato do autor, não verificado), quanto maior o nível, mais vantajoso é o uso dos modelos próprios.

| Plano | Mensal / Anual na Web | Grok Bot |
| :--- | :--- | :--- |
| **Plano Gratuito** | $0 | Teste de cota por 7 dias |
| **Plus** | $8/mês (aprox. $7 no anual) / $80/ano | Não incluso |
| **Premium** | $30/mês / $300/ano | Incluso (porta de entrada) |
| **Super** | $100/mês / $1000/ano | Incluso |
| **Ultra** | $200/mês / $2000/ano | Incluso (cota máxima) |

**O plano Plus não inclui o Grok Bot nem Cloud agents de forma alguma**, portanto, para executar tarefas automatizadas, o ponto de partida obrigatório é o plano Premium de US$ 30 por mês. O teste gratuito é limitado a 7 dias de validade; a cota é deduzida de acordo com a escala da tarefa, etapas e tokens. Tarefas pesadas podem esgotar a cota de uma só vez, e ela não se renova após o término.

### Como fazer

**Recomenda-se assinar pela versão web, evitando o pagamento em dispositivos móveis.**

1. Acesse no navegador a página da assinatura unificada [grok.com/com/overlay/subscribe](https://grok.com/com/overlay/subscribe?from=/).
2. Faça login com a conta do X ou do Grok usada para trabalho.
3. Selecione o plano Premium (US$ 30/mês; a comunidade já viu promoções com 50% de desconto no primeiro mês por US$ 15, sujeito ao que constar na página de checkout).
4. **Escolha o pagamento mensal em vez de marcar o anual diretamente**, facilitando a troca de nível ou de ferramenta a qualquer momento.
5. Pague com um cartão de crédito ou débito internacional aceito, ou via Apple Pay / Google Pay na web.
6. Abra o cliente do Grok Bot, faça login e confirme se a tela inicial liberou as permissões para criar e executar agentes.

Para uma análise detalhada, consulte [Análise da Assinatura Unificada do X: Como Novos Usuários Devem Escolher e se Assinantes Antigos Devem Migrar? Tudo Explicado](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee) e [Coletânea de Posts do 铁柱 ①: Ativação, Planos e Cotas](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc).

### Critérios de sucesso

Abra o cliente desktop do Grok Bot: **se a criação de uma nova tarefa conseguir alocar um ambiente na nuvem para execução e a fatura exibir o status Premium com cobrança mensal**, a configuração foi concluída com sucesso.

## Como é calculado o pool de uso semanal do Grok Bot? {#每周共享用量池-额度结算与多端共用机制}

**A assinatura fornece um pool fixo de cotas semanalmente com sincronização em tempo real entre múltiplos dispositivos. Os modelos oficiais na web, no Bot e nas conclusões de código do Cursor compartilham o consumo de acordo com o volume de tarefas e o número de etapas; já os modelos de terceiros são cobrados separadamente conforme o preço de tabela da API.**

![Pool semanal compartilhado de uso: cálculo de cotas e mecanismo de compartilhamento entre múltiplos dispositivos](/info/02-plans-s2.png)

### O que é

O The X Subscription disponibiliza semanalmente um pool fixo de cotas, renovado automaticamente ao expirar. **A versão web do Grok, o Bot e as perguntas e respostas com autocompletar do Cursor compartilham esse mesmo pool.** Ao fazer login com a mesma conta no Mac e no iPhone, as cotas são sincronizadas em tempo real, sem descontos duplicados ao trocar de aparelho.

| Categoria do Modelo | Regra de Cobrança |
| :--- | :--- |
| Modelos oficiais | Contabilizados no pool compartilhado. Tanto a versão web quanto o Bot descontam dele; a velocidade de consumo depende apenas do volume de tarefas e etapas. |
| Modelos de terceiros | **Não entram no pool compartilhado**; são cobrados separadamente no Cursor conforme o preço de tabela da API. |

O sistema atribui automaticamente o modelo subjacente do Bot, rotulado de forma unificada como "Uso do Grok Bot", sem opção de seleção manual ou bloqueio. Para mais detalhes, consulte [Modelos do Grok Bot](https://cursor.com/cn/help/grok-bot/models.md).

### Como fazer

Para evitar esgotar as cotas nos três primeiros dias, planeje a rotina em três etapas:

1. **Execute as tarefas mais pesadas e essenciais no início da semana.** Dê prioridade à escrita de código fundamental, montagem da arquitetura e depuração de lógicas complexas.
2. **Evite operações de alto consumo.** Geração de vídeos em lote, polling de alta frequência e integração de múltiplos Bots são os fatores que mais consom cotas (relato do autor, não verificado); recomenda-se criar vídeos diretamente na versão web, em vez de incluí-los no fluxo de trabalho do Bot.
3. **Fique atento ao ciclo de renovação.** Memorize o dia da renovação semanal exibido no painel; se ainda houver sobra perto da data de renovação, concentre aí a organização de dados ou revisões aprofundadas.

### Critérios de sucesso

**Mantenha o consumo médio diário das automações de rotina estável entre 10% e 15%.** Deixar uma margem de reserva de cerca de 20% no dia anterior à renovação semanal, sem receber pop-ups de alerta de esgotamento de cota, indica que o ritmo está ideal.

## Como vincular o Cursor para compartilhar a cota do Grok? {#授权互通-cursor-套餐与-supergrok-关联规则}

**O Cursor pode ser vinculado diretamente à conta do Grok para mapear a cota. A vinculação não altera o plano original nem gera cobranças adicionais; a cota passa a valer pelo nível mais alto entre as duas contas, sem acúmulo, e o pareamento é permanente, sem possibilidade de desvinculação ou transferência.**

![Interoperabilidade de autorização: regras de associação entre planos do Cursor e SuperGrok](/info/02-plans-s3.png)

### O que é

Uma conta do Cursor pode ser diretamente vinculada a uma conta do Grok para compartilhar o uso. **Antes de vincular, atente-se a três regras fundamentais:**

- Apenas sincroniza cotas, sem alterar o plano: o limite de uso é mapeado diretamente, sem modificar o plano atual do Cursor e sem cobranças adicionais.
- As cotas não se acumulam, prevalece o nível mais alto: passa a valer a maior cota semanal entre ambos os lados. Por exemplo, vincular o Cursor Pro ao SuperGrok Plus eleva o limite para a cota do Plus.
- Bloqueio permanente após a vinculação, sem possibilidade de desvincular: uma vez feito o pareamento, **não é possível desvincular nem transferir a autorização, seja por conta própria ou entrando em contato com o suporte.**

| Nível de Assinatura do Cursor | Nível de Associação Equivalente | Uso Semanal do Grok Bot |
| :--- | :--- | :--- |
| Cursor Pro | SuperGrok / X Premium+ | Uso semanal básico |
| Cursor Pro+ | SuperGrok Plus | Uso semanal abundante |
| Cursor Ultra | SuperGrok Heavy | Uso semanal máximo |
| Sem plano do Cursor | SuperGrok Lite | Não inclui o Grok Bot (o nível Lite não tem permissão; requer upgrade antes de vincular) |

Se você recebeu um assento corporativo do Grok Business, a conta já conta com permissão para o Bot nativamente, **não sendo necessária nenhuma operação de vinculação na página.**

### Como fazer

A vinculação de contas individuais é realizada na web.

1. Acesse a versão web do Grok Bot no navegador com a conta do Cursor que receberá a cota, certificando-se de que a conta principal está correta.
2. Abra o link de início rápido [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding).
3. Clique em vincular conta do Grok (Link Grok Account); no celular, toque no botão de mesmo nome na página de assinaturas.
4. Após o redirecionamento, faça login e autorize com a conta detentora do SuperGrok, SuperGrok Plus, SuperGrok Heavy ou X Premium+.
5. Volte à página de configurações do cliente para confirmar o status. **A nova cota pode levar até 24 horas para sincronizar; durante esse período, não clique repetidamente em vincular nem tente desvincular.**

Para conhecer todas as regras, consulte a documentação oficial [Vincular o SuperGrok ao Grok Bot](https://cursor.com/cn/help/grok-bot/supergrok.md).

**Usuários com assento corporativo atribuído só precisam fazer login direto, sem necessidade de vinculação adicional.**

1. No cliente desktop, acesse Settings > General e clique em Sign Out para sair da conta atual (o mesmo vale para o aplicativo mobile).
2. Na tela de login, clique em Sign in with Grok.
3. Insira as credenciais do Grok com o assento Business atribuído para entrar; o sistema vinculará automaticamente a cota correspondente ao assento.

### Critérios de sucesso

Abra o cliente desktop em Settings > Usage & Billing.

**A vinculação foi bem-sucedida se a etiqueta do nível de associação correspondente for exibida abaixo do gerenciamento de planos, a barra de cota semanal indicar o ciclo de renovação e a conta não registrar cobranças duplicadas.**

## Assentos do Plano Team e Configuração de Pagamento Sob Demanda (On-demand)

### O que é

Os membros da equipe fazem login no Grok Bot diretamente com suas próprias contas do Cursor, e o consumo utiliza a cota do time. **Os administradores não precisam atribuir assentos individualmente, e os membros não dependem de aprovação.**

Quando a cota semanal se esgota, o sistema recorre automaticamente ao uso sob demanda (exibido na fatura como Billed through Cursor). O sistema conta com um mecanismo de proteção: **tarefas que ultrapassarem o limite mensal não são interrompidas no meio do caminho**, permitindo que a tarefa atual seja concluída por inteiro.

### Como fazer

1. No cliente, abra as **Configurações** (Settings) > **Usage & Billing**.
2. Localize "Limite mensal de uso sob demanda"; se estiver como Disabled, clique em **Enable** à direita para ativá-lo.
3. Na primeira configuração, é necessário cadastrar um cartão de crédito. Em [cursor.com/dashboard](https://cursor.com/dashboard), clique em **Gastos** (Spending).
4. No campo **Monthly Limit**, insira o teto de gastos mensal (por exemplo, defina 20 ou 50 dólares para evitar gastos excessivos) e salve.

**Os aplicativos móveis para iOS e Android não permitem configurar o limite diretamente**; é necessário acessar o console na web. Para detalhes sobre a cobrança, consulte a documentação oficial [Planos e Faturamento](https://cursor.com/cn/help/grok-bot/plans.md).

### Critérios de sucesso

Em Usage & Billing, deve ser possível verificar que o uso sob demanda está ativado e exibe o valor do limite configurado. **Quando a cota semanal se esgotar, as tarefas não devem apresentar erro nem ser interrompidas**, alternando tranquilamente para o canal sob demanda até a conclusão.

## Guia de Decisão e Operação para Migração de Assinaturas Antigas

![Guia de decisão e operação para migração de assinaturas antigas](/info/02-plans-s5.png)

### O que é

A assinatura unificada The X Subscription foi lançada em 12 de outubro de 2026. Para usuários que não realizarem a migração ativamente, os planos, preços e funcionalidades originais permanecerão inalterados. Os ciclos anuais são mantidos integralmente até a data natural de término; quaisquer alterações posteriores só entrarão em vigor no momento da renovação.

**Uma vez confirmada na web, a operação tem efeito permanente, e nem o suporte conseguirá reverter ou restaurar o plano antigo.** A assinatura anterior é encerrada automaticamente no fechamento com reembolso proporcional diário; o valor reembolsado não pode ser abatido do novo plano (que deve ser pago integralmente), e o ciclo de faturamento é reiniciado a partir daquele dia. No momento, o aplicativo mobile não oferece suporte à migração, devendo ser feita obrigatoriamente pela versão web.

| Canal de Pagamento e Produto de Assinatura | Meio de Reembolso e Ação do Usuário |
| :--- | :--- |
| Planos antigos adquiridos diretamente na web | A empresa processa automaticamente o estorno proporcional no cartão original, sem necessidade de intervenção manual. |
| Grok / X Premium assinado via Apple | A empresa auxilia no envio da solicitação, cabendo à Apple a decisão final sobre o valor a ser reembolsado. |
| Cursor assinado via Apple | **O usuário deve acessar pessoalmente「ID Apple → Assinaturas」no iOS para cancelar manualmente e solicitar o reembolso ao suporte da Apple.** |
| Serviços assinados via Google Play | **O usuário deve desativar manualmente a renovação automática em「Pagamentos e assinaturas」no Google Play.** |

### Estudo de caso: O relato de decisão de um autor da comunidade diante da assinatura unificada

Um desenvolvedor da comunidade possui um plano anual válido até 2027 (relato do autor, não verificado) e, após analisar seu consumo, decidiu **não migrar temporariamente sua assinatura antiga para a nova assinatura unificada**, desativando a renovação automática do plano original para continuar observando.

O plano antigo inclui descontos de longo prazo que seriam cancelados imediatamente caso a migração fosse forçada. O pool compartilhado semanal do novo plano cobre apenas os modelos oficiais; todas as chamadas de modelos de terceiros precisam ser pagas à parte, de acordo com o preço de tabela da API. Como o pool semanal do novo plano é compartilhado entre todos os produtos, a execução excessiva de Bots pode consumir a cota normal destinada à interface web e ao autocompletar de código.

| Perfil de Usuário | Características Típicas e Necessidades Centrais |
| :--- | :--- |
| Para quem a troca é recomendada | Quem paga separadamente por várias assinaturas avulsas com gasto mensal bem superior a US$ 30, utiliza principalmente modelos oficiais e precisa de forte integração com a automação do Grok Bot e gerenciamento de contas no X. |
| Para quem a troca não é recomendada | Quem mantém planos antigos com cotas adicionais para modelos de terceiros, ou quem programa pesadamente apenas no Cursor, sem interesse nos recursos sociais do X ou em geração de vídeo. |

Antes de migrar, abra o painel de uso para checar a distribuição real das chamadas e entender a proporção de uso entre modelos próprios e de terceiros. Sempre que possível, assine ferramentas de IA na modalidade mensal: as políticas de planos costumam ser reestruturadas a cada dois ou três meses, e comprometer-se com anuidades longas pode limitar sua flexibilidade (relato do autor, não verificado).

**Usuários que assinaram o Cursor pela Apple e decidirem migrar devem cancelar a renovação automática manualmente nos ajustes do celular**; a atualização pela web não fará isso por você.

Para mais detalhes sobre a análise da decisão, consulte [Análise da Assinatura Unificada do X: Como Novos Usuários Devem Escolher e se Assinantes Antigos Devem Migrar? Tudo Explicado](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee) e [Coletânea de Posts do 铁柱 ①: Ativação, Planos e Cotas](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc).

### Critérios de sucesso

Para usuários que mantiverem o plano antigo, certifique-se de que o status de renovação automática está como esperado e que as cotas dos modelos principais continuam intactas.

**Para usuários que decidirem migrar para o novo plano, certifique-se de que a assinatura antiga foi totalmente encerrada, que o reembolso no canal original foi recebido, que o novo plano está faturando normalmente no nível Premium e que não há cobranças duplicadas nem conflitos de canais entre ambos.**

## Visualização de Uso e Configuração de Prompts Antidesperdício

### O que é

**Primeiro, entenda a correspondência dos termos entre as plataformas para evitar que a cota se esgote sem você perceber:**

- Limite de uso semanal (Desktop) / Uso semanal (Mobile): Pool fixo da semana, renovado semanalmente. Estar vinculado via SuperGrok indica autorização associada, não incluindo o plano avulso do Cursor.
- Uso sob demanda (Billed through Cursor): Cobrança adicional após o esgotamento do pool fixo. O limite mensal na web fica em Monthly Limit, abaixo de Gastos (Spending).
- Como acessar: No desktop, vá em Configurações (Settings) > Uso e Faturamento (Usage & Billing); no mobile, toque em Uso Semanal; na web, acesse [cursor.com/dashboard](https://cursor.com/dashboard).

### Como fazer

**Insira as instruções de contenção de desperdício diretamente no prompt de sistema do Bot ou na primeira mensagem da conversa.**

Para um único Bot convencional, preencha o primeiro bloco para fixar um raciocínio de baixo consumo e aumentar o intervalo de polling, evitando que o Bot funcione à toa em segundo plano.

```text
你是一个自动化执行助手。在后续所有任务执行中，必须严格遵守以下资源控制规则：
1. 任务规划阶段必须输出极简执行步骤，禁止发起非必要的递归搜索与多轮冗余工具自检。
2. 在处理代码与文本分析任务时，保持适度推理强度，优先给出核心结果，不要输出冗长无关的修饰性文字。
3. 如果任务涉及定时轮询或周期监控，单次轮询时间间隔不得低于 30 分钟，严禁设置分钟级高频循环。
4. 严禁自行尝试调用外部视频生成或音频转换能力；如遇复杂多步骤任务，分步向我汇报进度并等待确认。
```

Para colaboração entre múltiplos Bots, preencha o segundo bloco. **A transmissão frequente (broadcast) de múltiplos Bots na mesma tarefa é a armadilha que mais consome cotas rapidamente (relato do autor, não verificado); é obrigatório adotar uma comunicação em cadeia ponto a ponto.**

```text
你在多智能体协同流水线中担任协同节点。必须严格执行以下通信约束：
1. 全面采用点对点（Agent-to-Agent）单向派活与回传，禁止向群聊或未指名的公共上下文广播全量数据。
2. 传递工作流结果时，只提取关键字段与结构化结果摘要，严禁将完整的历史对话日志重复打包转发。
3. 协助任务交付完毕后，立即输出任务终止状态，主动退出协作监听，切断后续消息的被动接收与重复解析。
```

Estratégia baseada na [Coletânea de Posts do 铁柱 ①: Ativação, Planos e Cotas](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc).

### Critérios de sucesso

Após injetar o prompt, **o Bot deve responder claramente confirmando a conformidade com as restrições de recursos.** Se, após executar scripts de automação por três dias seguidos, a curva de consumo em Usage & Billing no cliente permanecer suave, as tarefas agendadas rodarem nos intervalos definidos e não houver logs redundantes de autoverificação, o objetivo foi atingido.

## Armadilhas Comuns

### Escolha e Assinatura

- **Não compre o plano Plus de US$ 8 se quiser usar o Bot.** Ele não inclui o Grok Bot nem Cloud agents; para usar o Bot, você deve obrigatoriamente assinar o plano Premium de US$ 30.
- **As cotas do Cursor Pro e do SuperGrok não se acumulam.** Assinar ambos simultaneamente não fornecerá cota dupla; o sistema calculará apenas por um dos lados, o que é puro desperdício de dinheiro.
- **Modelos de terceiros são cobrados separadamente pelo preço de tabela da API.** O pool semanal compartilhado do The X Subscription cobre apenas os modelos oficiais.
- **Escolha o pagamento mensal, não contrate o anual.** Ferramentas e regras mudam com frequência, e a anuidade limitará sua flexibilidade para ajustes futuros.

### Vinculação e Cancelamento

- **A vinculação de contas é permanente e irreversível.** Após vincular o Cursor ao SuperGrok ou X Premium+, nem o suporte conseguirá desvincular. Jamais utilize contas secundárias de teste para autorizar.
- A migração de assinaturas antigas só pode ser realizada pelo navegador no computador; os aplicativos móveis não disponibilizam acesso para a troca.
- **É obrigatório cancelar manualmente a renovação do Cursor no iPhone.** Alterar para a assinatura unificada na web não cancelará automaticamente a cobrança da App Store; se não cancelar manualmente, você será cobrado duplamente.

### Cotas e Uso

- **Ative o uso sob demanda e defina um limite mensal.** Quando o pool semanal compartilhado se esgotar e o modo sob demanda não estiver ativo, o Bot deixará de responder imediatamente.
- **Utilize comunicação ponto a ponto na colaboração entre múltiplos Bots.** Cada mensagem em um chat em grupo é transmitida para todos os Bots, disparando computação em todos eles; adicioná-los a um grupo permanente esgotará a cota semanal em poucas rodadas.

## Como Validar Após a Configuração

1. **Permissões da conta**: Abra o cliente desktop, clique no avatar no canto inferior esquerdo e confirme se o plano é **Premium, Super ou Ultra**. Clique em criar novo Bot e confirme se é possível abrir o painel de configurações e se os Cloud agents são exibidos como prontos.
2. **Cotas em múltiplos dispositivos**: No cliente desktop, em **Settings > Usage & Billing**, anote a porcentagem de uso semanal. Em seguida, abra o app mobile e confira: os valores em ambos os lados devem ser estritamente idênticos.
3. **Proteção de gastos**: Acesse no navegador a página Spending em [cursor.com/dashboard](https://cursor.com/dashboard) e confirme se um teto em dólares foi preenchido em **Monthly Limit**, e se o canal sob demanda no cliente está com o status Enable.
4. **Chamada real**: Envie um prompt para o Bot executar uma tarefa curta e **verifique os logs para garantir que não há textos supérfluos nem chamadas desnecessárias de ferramentas**; se o consumo oscilar apenas minimamente, o teste foi aprovado.

## Leituras Complementares

- Capítulo relacionado: [Qual a diferença entre o Grok e o Grok Bot?](/part1/grok-vs-grok-bot)
- Capítulo relacionado: [Capítulo 10 Cotas e Custos: Fazendo o Limite Semanal Durar a Semana Toda](/part1/10-usage)
- Capítulo relacionado: [Capítulo 25 Perguntas Frequentes e Solução de Problemas](/part4/25-faq)
- Documentação oficial: [Planos e Faturamento](https://cursor.com/cn/help/grok-bot/plans.md)
- Documentação oficial: [Vincular o SuperGrok ao Grok Bot](https://cursor.com/cn/help/grok-bot/supergrok.md)
- Documentação oficial: [Assinar nos Aplicativos Móveis](https://cursor.com/cn/help/grok-bot/mobile-purchase.md)
- Documentação oficial: [Modelos do Grok Bot](https://cursor.com/cn/help/grok-bot/models.md)
- Análise prática da comunidade: [Análise da Assinatura Unificada do X: Como Novos Usuários Devem Escolher e se Assinantes Antigos Devem Migrar? Tudo Explicado](https://jcng5q8n0f3z.feishu.cn/wiki/Myw6wFW8EicOiRkoEAXcVJqinee)
- Coletânea prática da comunidade: [Coletânea de Posts do 铁柱 ①: Ativação, Planos e Cotas](https://jcng5q8n0f3z.feishu.cn/wiki/PCZIw5IqgiZLjTkXqNncpxannpc)
