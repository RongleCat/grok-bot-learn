# Capítulo 4 Delegando Tarefas: Mensagens, Anexos e um Bom Handoff

Quando a demanda é descrita de forma muito breve, ele tende a pesquisar dezenas de páginas irrelevantes e bagunçar arquivos. **Enviar mensagens é passar o trabalho para um computador na nuvem**.

- **Defina limites rígidos para a tarefa** e explique a utilidade dos anexos, evitando que ele tome decisões por conta própria
- Dê instruções claras para obter entregáveis que possam ser validados diretamente
- Intervenha a qualquer momento durante a execução para corrigir desvios ou use a voz para complementar o contexto


![Delegando tarefas: mensagens, anexos e um bom handoff](/info/04-handoff.png)

## Os Cinco Elementos de uma Boa Solicitação

![Os Cinco Elementos de uma Boa Solicitação](/info/04-handoff-s1.png)

Ao delegar tarefas ao Grok Bot, **as instruções devem deixar claros o objetivo e o escopo das ferramentas**; consulte as diretrizes na documentação do [Grok Bot](https://cursor.com/cn/docs/grok-bot).

1. **Ação específica e única**. Especifique "extrair e comparar" ou "redigir e-mail externo", não use "dê uma pesquisada"; quanto mais direto o caminho, menos etapas serão gastas.
2. **Delimite as fontes de dados**. Especifique uma página do Notion, o canal #sales-leads do Slack ou URLs exatas, evitando buscas desordenadas pela web.
3. **Trace uma linha vermelha para aprovação**. Leitura e comparação rodam automaticamente; **qualquer ação envolvendo envio de mensagens externas, pagamentos online ou alteração/exclusão de dados deve pausar obrigatoriamente para aguardar aprovação**.
4. **Fixe o formato da entrega**. **Recuse relatórios verbais**; exija a geração de relatórios em Markdown com links ou planilhas CSV em `/workspace/leads/`.
5. **Defina regras de erro e limites factuais**. Diferencie suposições de fatos objetivos; se o login expirar, pule e registre o ocorrido, **sendo proibido entrar em repetições infinitas (loop)**.

## Especificações de Anexos e Lista de Limitações

Consulte as regras de upload em [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

### Limites de Especificação

- No cliente desktop, o limite é de **até 6 arquivos** por mensagem (o excesso deve ser colocado no workspace); imagens, textos e áudios têm limite de 25MB, e vídeos de 200MB.
- Se houver bloqueios ou erros, converta localmente para PDF, CSV ou imagem antes de fazer o envio.

### Handoff e Chats em Grupo

1. **Não pressione Enter logo após arrastar os arquivos**; descreva claramente a identidade de cada arquivo, a lógica de relação entre eles e as instruções de proteção.

```text
上传的 PDF 是已经签署的标准采购合同模板。上传的 Excel 是本月供应商提交的实际报价清单。
请对照合同模板中第 4 条关于各类物料的基准单价，逐行核验 Excel 里的实际报价。
标出单价超出基准价的所有条目，在附带的备忘中引用合同中的对应条款编号。
将核验结果另存为一份新的 Excel 表格，并输出一份简短的异常摘要。
请勿改动原始上传文件。
```

2. Em chats em grupo, a comunicação entre Bots **suporta apenas texto puro**. Se um Bot subsequente precisar ver os anexos, envie-os em uma conversa privada.

## Biblioteca de Prompts Práticos para Entrega de Tarefas

Para cenários comuns, **use os modelos diretamente**; basta fazer pequenos ajustes e rodar.

1. **Pesquisa e prospecção**: coletar leads e preparar materiais, sem enviar diretamente.
```text
从我们的 CRM 系统中获取本周销售管道的重点评审列表。
请跳过当前已经处于活跃跟进序列中的联系人。
在指定公开网页和已授权的 Slack 相关频道中，深入调研排名前五的重点账户，找出负责采购或技术的对口联系人。
参考我在系统中历史邮件的口吻，为这五位联系人分别起草个性化的初次外联邮件。
将草稿保存在系统草稿箱中，并在明天上午 9 点前在此对话中列出清单供我审批。未经我的明确确认，绝不向外发送任何邮件。
```
2. **Verificação de anexos**: conciliar múltiplas planilhas e auditar receitas e despesas.
```text
附件中的 PDF 为《2026 年度差旅与报销政策细则》，CSV 表格为本月部门提交的待审批费用报销流水。
请逐项核对 CSV 中的每一笔申报项目：
1. 检查报销金额是否超过对应城市级别的住宿与餐饮标准。
2. 检查单笔超过 500 元的支出是否有对应的发票类别标记。
3. 提取所有不符合政策规定的异常申报，列明行号、申报人、金额、超标原因及违背的政策条款。
最后生成一份 Markdown 格式的核查报告，并列出通过与未通过的统计汇总。保持原始 CSV 文件不被改动。
```
3. **Inspeção de websites**: inspecionar páginas e registrar evidências.
::: details Biblioteca de prompts práticos para entrega de tarefas
```text
你负责检查我的网站运行状态。本次只访问我提供的以下三个页面：首页、最新更新日志页、用户注册页。
逐一核验各页面是否能正常打开、关键按钮是否响应、文本信息是否存在断链或明显过期内容。
排查过程中必须执行以下要求：
1. 发现任何显示异常或报错时，保存完整的页面 URL、检查时间戳以及当时的屏幕截图。
2. 区分页面直接看到的事实与你的推测，事实写在证据栏，分析写在备注栏。
3. 检查受阻或遇到需要验证码时，记录阻碍原因并继续检查下一个页面，不要重复尝试。
4. 检查结果报告保存在 /workspace/site-check/ 目录下，命名为 check-report.md。
你仅有只读检查与生成报告的权限，严禁更改后台设置或提交任何表单。
```
:::
4. **Validação de plano**: revisar a lógica antes de operações complexas para evitar desvios.
::: details Biblioteca de prompts práticos para entrega de tarefas
```text
我准备让你整理过去一个季度跨 Notion、Gmail 和 GitHub 的客户产品缺陷反馈。
在正式开始执行数据读取与整理之前，请先不要调用任何批量工具，先在对话中向我提交一份执行计划：
1. 列出你准备按顺序访问的系统、模块与具体检索词。
2. 说明你打算提取哪些关键字段，以及如何去重。
3. 标明整个流程中哪些环节可能涉及对外部状态的更改。
4. 说明你打算将阶段性文件保存在云电脑的哪个路径，以及遇到权限不足时如何处理。
我确认并批准你的计划后，你再开始执行。
```
:::
5. **Triagem de e-mails**: extrair pontos-chave e categorizar para encaminhamento.
::: details Biblioteca de prompts práticos para entrega de tarefas
```text
使用已连接的邮箱插件，读取收件箱过去 24 小时内收到的全部新邮件。
按照以下业务逻辑进行分类处理：
1. 属于系统续费、订阅扣款账单的邮件，提取服务商、扣款金额与下次续费时间。
2. 属于用户直接提问或反馈 Bug 的邮件，提取发件人邮箱、问题概括与紧急程度。
3. 属于营销推广、垃圾资讯的邮件，直接归入忽略清单。
在当前会话中输出一份分栏概览：仅展示需我关注的账单与紧急反馈，并在每条记录后附带邮件主题与时间。
所有邮件保持未读或已读原状，未经审批严禁归档、删除或起草回复。
```
:::

## Regras de Longo Prazo e Tarefas Únicas: Não Confunda Regras da Casa com Afazeres Domésticos

![Regras de Longo Prazo e Tarefas Únicas: Não Confunda Regras da Casa com Afazeres Domésticos](/info/04-handoff-s4.png)

**Diferencie com clareza regras de longo prazo de tarefas únicas** (consulte [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)); não registre parâmetros temporários nas configurações permanentes, nem redefina as regras básicas a cada interação.

| Tipo | Ciclo e Configuração | Exemplos e Limitações |
| --- | --- | --- |
| Regras de longo prazo | Valem entre diferentes sessões; configuradas em Bot Details ou enviando "Grave isso na sua memória como uma regra de longo prazo" | Limites de permissão, formato de data YYYY-MM-DD |
| Tarefas únicas | Valem para apenas uma rodada e não persistem; enviadas diretamente | Processar 12 contas ou 3 áudios, extrair a lista da reunião das dez horas |

Todos os Bots compartilham o `/workspace` (consulte [10 Experiências Essenciais para Tornar seu Grok Bot Ainda Mais Útil](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)).

**A memória não substitui sistemas de negócios**: saldos e estoques devem ser consultados diretamente na fonte de dados, sendo estritamente proibido inventar dados.

## Intervenção Durante a Execução: Parar, Interromper e Aprovar

![Intervenção Durante a Execução: Parar, Interromper e Aprovar](/info/04-handoff-s5.png)

### Interrupção e Parada
Se o Bot desviar do objetivo, basta enviar uma mensagem normal para **intervir em tempo real**, como: "Mude para a nova especificação atualizada de outubro de 2026 e verifique novamente".

Se houver um erro de operação ou uma chamada de alto risco, envie estes quatro caracteres na caixa de texto para parar imediatamente:
```text
立即停止
```

**A parada interrompe apenas ações ainda não executadas e nunca reverte arquivos já salvos ou requisições de API já enviadas**. Após parar, siga estas três etapas para diagnóstico:
1. Abra o painel de pré-visualização do computador na nuvem para verificar o status.
2. Limpe arquivos incompletos ou dados gravados incorretamente.
3. Reduza o escopo, defina limites claros e só então reinicie a execução.

### Aprovação e Tempo Limite (Timeout)
Ativar o Auto-review ou acionar operações de alto risco exibirá o card "Revisão de Ação" (consulte o [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)), contendo três opções:
- Permitir uma vez: aprova apenas esta ocorrência; ações semelhantes futuras continuarão solicitando autorização.
- Permitir sempre: adiciona à lista de permissões e não volta a perguntar.
- Rejeitar: bloqueia completamente a operação.

| Cenário | Mecanismo de Espera | Resultado por Tempo Limite |
| --- | --- | --- |
| Interação em tempo real | Em espera suspensa | Aguarda continuamente até haver uma ação/clique |
| Execução autônoma em segundo plano | Expira automaticamente em cerca de 10 minutos (Expired) | **A operação não é executada e a tarefa é finalizada** |

### Assumir o Controle de Credenciais (Action needed)
Ao lidar com senhas, 2FA, CAPTCHA ou pagamentos reais, um card de intervenção manual será exibido; siga três passos:
1. Clique em **Take over** e insira as informações manualmente no computador na nuvem.
2. Após concluir, clique em **I'm done** para devolver o controle ao Bot.
3. **Nunca digite senhas em texto puro na caixa de diálogo comum**.

## Interação por Voz: Uso Diferenciado entre Chamada de Voz em Tempo Real e Ditado por Voz

O Grok Bot inclui **dois recursos de voz distintos**: ditado e chamadas. Para mais detalhes, consulte [Chat de Voz com o Bot](https://cursor.com/cn/help/grok-bot/voice-chat) e o [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to).

### Comparativo entre os Dois Modos

| Modo | Acionamento e Atalhos | Saída e Cenários |
| --- | --- | --- |
| Entrada de voz (Ditado) | No desktop, clique em "Iniciar entrada de voz"; no Mac pressione Cmd+D, no Windows/Linux pressione Ctrl+D; no celular toque em "Iniciar ditado" | O texto é inserido na caixa de texto; ideal para refinar prompts ou complementar parâmetros |
| Chat de voz em tempo real | **Esvazie a caixa de entrada** e clique no ícone de onda sonora (Start voice chat) | Conversação bidirecional em tempo real; ideal para organizar ideias ou fazer um handoff rápido |

### Passo a Passo para Ativação e Dicas Importantes

1. Abra a conversa com um Bot individual.
2. **A caixa de texto deve ser completamente esvaziada**; espaços residuais ou rascunhos ocultarão o ícone de onda sonora.
3. Clique no ícone de onda sonora; no primeiro uso, conceda a permissão de acesso ao microfone.
4. A tela exibirá Connecting… (no celular, Calling…); assim que o Bot começar a falar, a conexão estará estabelecida.

### Controles e Limitações Rígidas

- Durante a chamada, é possível silenciar o microfone, visualizar legendas em rolagem contínua e ajustar a velocidade e o timbre da voz; se mudar de tela para consultar documentos, clique em "Voltar para o chat de voz" na barra superior para retornar.
- **Suporte exclusivo para conversas individuais (1 a 1)**; não é possível iniciar em grupos, chats com múltiplos Bots ou "Bots de equipe".
- **Apenas uma chamada ativa por vez**; ao alternar para um novo Bot, confirme em "Encerrar e conversar".
- Após desligar, um card de Voice chat é gerado automaticamente registrando a duração total; clique nele para consultar a transcrição completa e prossiga com as tarefas seguintes pelo fluxo de texto.

## Padrões Comuns de Erro vs. Otimizações Recomendadas

1. **Delimitação de caminho**: sem definir o escopo e os métodos, o Bot clicará desordenadamente no console e **poderá até modificar o código do ambiente de produção**.
```text
  帮我维护一下网站，看看有没有什么 Bug。
  ```
Corrija delimitando as páginas e as etapas de inspeção:
```text
  对站点清单（/workspace/sites.txt）中的三个静态展示页进行巡检。
  用云浏览器打开每个页面，检查控制台是否有 404 或 500 报错，检查顶部导航栏链接是否全部有效。
  将报错信息、对应页面 URL 及当时的屏幕截图写入 /workspace/logs/err-20261014.md。
  全程仅做只读检查，严禁点击任何带有提交或删除性质的表单按钮。
  ```

2. **Limites de aprovação**: não conceda permissão irrestrita de envio externo; se a interpretação falhar, **ele poderá facilmente enviar mensagens incorretas a clientes importantes**.
```text
  读取 Gmail 里的未读邮件，重要的直接帮我回一下。
  ```
Mantenha a aprovação humana em etapas críticas:
```text
  读取 Gmail 中过去 12 小时的未读邮件。
  仅筛选出发件人属于我们现有企业客户、且正文包含售后或咨询诉求的邮件。
  根据产品常见问题手册，为每封邮件起草回复草稿并存入 Gmail 草稿箱。
  在当前对话中列出客户名称、邮件摘要与草稿正文，等待我的审批。未经我的明确确认，绝不点击发送。
  ```

3. **Separação de fatos**: não inclua vieses no prompt, **evitando que o Bot valide suposições e confunda uma pequena promoção com uma guerra de preços**.
```text
  去看看竞品今天的动态，总结一下他们是不是要跟我们打价格战。
  ```
Separe os dados objetivos das suposições:
```text
  访问竞品官网的公开定价页与首页横幅，获取他们当下的方案价格表。
  对照我们在 /workspace/competitor/last-month-price.json 中记录的旧价格：
  1. 事实列：标出哪些 SKU 的标价发生了变动，变动金额是多少，附带页面截图与访问时间。
  2. 推测列：基于该降价是限时促销还是永久调价，给出你的分析理由。
  两部分内容必须分开分栏呈现，不得将分析推论当作已知事实。
  ```

4. **Proteção somente leitura**: se não indicar a tabela principal/secundária e os campos a preservar, **os dados originais poderão ser facilmente sobrescritos e corrompidos**.
```text
  （直接拖入三个 Excel 表格）把这几个表整理一下。
  ```
Deixe explícito qual tabela é a referência e configure-a como somente leitura:
```text
  上传的三个表格分别是 7 月、8 月和 9 月的销售明细。
  以「订单编号」为唯一主键进行数据去重合并：
  1. 字段统一保留：订单号、成交日期、客户名称、销售代表、成交金额。
  2. 生成一份全新的 Q3_sales_summary.csv 文件，保存在当前工作区。
  3. 保持我上传的原始 7、8、9 月表格内容与文件名完全不变。
  ```

5. **Missão única**: não acumule múltiplas tarefas em um único Bot; além de poluir a memória, **isso consumirá rapidamente sua cota semanal**.
```text
  你帮我写一篇关于新产品的推文，顺便把昨天的账目算了，然后再帮我看看竞品推特。
  ```
Divida em tarefas únicas com fluxos dedicados:
```text
  遵循一个 Bot 负责一项核心任务的原则。当前 Bot 仅承担社媒文案起草职责：
  依据 /workspace/product/spec.md 中的新功能说明，为 X 平台起草三条不同风格的发布文案。
  要求突出性能提升数据，字数控制在 280 字符以内。
  账目核算与竞品调研交由对应的专用 Bot 负责，不要在此会话中处理。
  ```

## Casos Reais de Handoff em Negócios

### Inspeção Diária de Websites e Registro de Evidências
O webmaster yishan transformou os requisitos de inspeção diretamente em critérios de aceitação. O diretório de trabalho foi estritamente limitado a `/workspace/site-check/`, permitindo inspecionar apenas a página inicial, os artigos mais recentes e o formulário de inscrição, sendo terminantemente proibida a navegação indiscriminada (crawling).
- O relatório deve registrar links completos, carimbos de data/hora (timestamps) e capturas de tela do momento. **Erros visíveis diretamente contam como fatos; causas investigadas contam como suposições, devendo ser registradas separadamente.**
- Se encontrar logins expirados ou links quebrados, registre a pendência e pule imediatamente, sendo proibido insistir repetidamente. Para o procedimento detalhado, consulte [Como Usar o Grok Bot a Fundo em Uma Hora](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg).

### Central de Entrada e Roteamento de Demandas
一泽Eze configurou um Bot dedicado à caixa de entrada para gerenciar o Gmail, sem conceder acesso direto ao e-mail para os Bots downstream.
- Ao receber e-mails de feedback, ele os encaminha via chat privado para o "Bot de Feedback do Produto", e faturas para o "Bot de Gestão de Assinaturas".
- A comparação puramente numérica é delegada diretamente a scripts de linha de comando. **Sincronizar apenas dados incrementais com o Bot ajuda a economizar a cota semanal de uso.**
- Não conecte ferramentas de alta permissão em todos os lugares; usar um ponto de entrada dedicado para a triagem inicial é a abordagem mais segura.

  Para um resumo das experiências, consulte [10 Experiências Essenciais para Tornar seu Grok Bot Ainda Mais Útil](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc).

### Diagnóstico pelo Chief of Staff e Criação de Bots
CyrilXBT primeiro colocou um Bot Chief of Staff para ler o Notion e o Slack da equipe, mapeando as três tarefas que consumiam mais tempo, apresentavam maior repetição e geravam mais gargalos, avançando em três etapas:
1. O Bot Chief of Staff executa manualmente, com supervisão humana da qualidade das entregas.
2. Após a validação, consolida o fluxo como uma habilidade (skill) e cria um Bot exclusivo e independente.
3. Por fim, configura a execução automática programada.
**Etapas que envolvam envio, compras, publicação ou alteração em sistemas online devem reter rigorosamente a aprovação humana.
** Tutorial completo em [How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd).

## Armadilhas Comuns e Como Evitá-las

1. **Envie anexos com explicações**: ao enviar várias imagens ou mais de duas planilhas, **descreva sempre a finalidade**, caso contrário ele poderá inverter a relação principal/secundária.
2. **Grave regras de longo prazo na memória**: instruções avulsas são perdidas ao trocar de sessão; regras fundamentais devem ser **inseridas no campo Sobre/Responsabilidades dos Detalhes do Bot** ou salvas na memória.
3. **Evite a suspensão na integração local**: tarefas 100% em nuvem rodam mesmo com a tampa do notebook fechada, mas a integração com um computador local será interrompida se ele suspender; lembre-se de **verificar as configurações de energia e suspensão**.
4. **Compartilhe imagens entre Bots via caminho de arquivo**: a comunicação entre Bots em grupos suporta apenas texto simples; para enviar imagens, **salve-as no caminho compartilhado `/workspace/`** para que o outro Bot possa acessá-las.
5. **Se o botão de voz sumir, limpe o campo**: se restarem caracteres ou espaços na caixa de texto, o botão de onda sonora ficará oculto; **limpe totalmente a caixa de texto** para restaurá-lo.
6. **Para operações de alto risco, escolha Permitir uma vez**: ao enviar e-mails ou alterar/excluir dados, não escolha "Permitir sempre"; antes de o fluxo rodar de forma estável por semanas, **faça questão de escolher "Permitir uma vez"**.

## Como Fazer a Validação da Entrega

1. Acesse `/workspace/` ou o diretório especificado para inspecionar os arquivos, **confirmando que abrem normalmente e sem caracteres corrompidos**; não se baseie apenas no texto temporário da conversa.
2. Faça uma amostragem de 2 a 3 dados essenciais abrindo os links ou capturas de tela para evitar alucinações ou invenções do modelo.
3. Verifique os logs de execução para **confirmar que não houve envios de mensagens não autorizados, alterações de configuração ou sobrescrita de arquivos originais**.
4. Separe fatos de suposições: o conteúdo original da página deve ficar na seção de fatos, enquanto inferências e sugestões devem ficar nas observações; corrija imediatamente qualquer confusão.
5. Verifique a lista de anomalias: **ao encontrar páginas inativas ou campos faltantes, o motivo deve ser registrado e a tarefa deve ser concluída até o fim**, sem interromper a execução no primeiro erro.

## Leituras Recomendadas

- Documentação oficial: [Grok Bot](https://cursor.com/cn/docs/grok-bot)
- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Suporte oficial: [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)
- Suporte oficial: [Chat de Voz com o Bot](https://cursor.com/cn/help/grok-bot/voice-chat)
- Artigo da comunidade: [Como Usar o Grok Bot a Fundo em Uma Hora](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)
- Artigo da comunidade: [10 Experiências Essenciais para Tornar seu Grok Bot Ainda Mais Útil](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)
- Artigo da comunidade: [How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
