# Capítulo 20 Automação Confiável: Agendamento, Webhook e Gatilhos de Eventos

Uma Routine acorda dezenas de vezes por dia apenas para responder "nenhuma alteração hoje", consumindo sua cota da mesma forma. **A falta de padronização nas tarefas leva facilmente a falhas silenciosas**.
- Desvios de fuso horário (agendado para as 9h da manhã, roda às 3h da madrugada)
- Erros de periodicidade (o padrão de dias úteis faz com que finais de semana fiquem de fora)
- Ausência de fallback (erros com dados vazios alteram o ambiente de produção sem controle)

**Uma arquitetura em duas etapas combinada com o cron do Linux pode eliminar mais de 80% das execuções ociosas**. Definir contratos de limites e travas de segurança humanas, além de integrar Atalhos e fluxos de eventos do X, é a chave para uma automação estável e econômica.


![Automação Confiável: Agendamento, Webhook e Gatilhos de Eventos](/info/20-automation.png)

## Escolha de Gatilhos: Entrega por Horário ou Espera por Mudanças

![Escolha de Gatilhos: Entrega por Horário ou Espera por Mudanças](/info/20-automation-s1.png)

Primeiro, diferencie se o objetivo é entregar resultados no horário agendado ou aguardar novos dados. **O Bot compartilha o pool de cota semanal com o Grok e o Cursor**, e a sondagem (polling) de alta frequência pode esgotá-lo em poucos dias.

### Assinaturas e Limites de Cota

No The X Subscription (12/10/2026), o plano Plus não inclui Bot; os planos compatíveis são Premium (US$ 30/mês ou US$ 300/ano, 4x), Super (US$ 100/mês ou US$ 1000/ano, 15x) e Ultra (US$ 200/mês ou US$ 2000/ano, 50x).

O limite é de 50 Routines por Bot, com histórico retido de 20 execuções, e o **intervalo mínimo de agendamento é de 5 minutos**.

### Modos de Disparo e Escolha

- Rotinas agendadas: cobram no horário agendado, havendo dados ou não; ideais para relatórios diários fixos.
- Webhook: consumo zero quando ocioso, **exclusivo para requisições POST com chave Bearer**.
- Eventos de terceiros (GitHub, Slack, etc.): ativam apenas quando há eventos; canais movimentados podem esgotar a cota rapidamente.
- Interações no X (responder @bot): não é possível analisar posts com vídeo; mencionar simultaneamente @grok e @bot não dispara o gatilho.

**Se o processamento depende da chegada de novos dados, mude sem exceção para Webhook ou eventos de terceiros.**

## Modelo de Design de Rotinas: Escreva Contratos, Não Cargos

Escrever apenas títulos ou cargos nos prompts facilita falhas de execução. **Rotinas em produção devem especificar claramente um contrato de execução**.

Fonte: [4.3 Gatilhos e Automação: Agendamento, Webhook e Atribuição de Tarefas no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg). É necessário reunir quatro elementos essenciais, abrangendo fontes de dados, formatos de saída e estratégias para erros por ausência de dados e aprovação humana.

### Redigindo o Contrato e Configurando a Rotina

1. **Envie o contrato que restringe entradas e saídas ao Bot e peça para ele memorizá-lo**; para Bots compartilhados, insira-o no campo Description em About dos detalhes.
```text
负责范围：监控指定数据源并生成标准化 Markdown 摘要。
允许读取的数据源：工作区目录下的 data/incoming/ 文件夹及指定公开 RSS 链接。
输出格式规范：必须输出包含“标题、核心要点（最多3条）、影响评估、原始链接”的 Markdown 结构，存入 docs/daily/ 目录。
数据异常策略：若数据源无更新或文件为空，仅在工作区追加一行日志“[时间戳] NO_NEW_DATA”，严禁编造或推测新闻内容，严禁在聊天窗口发送刷屏提示。
权限边界：只读外部内容与本地写入。禁止调用外部发帖、转账、发送邮件或删除文件操作。
```
2. No chat, salve o fluxo de trabalho como uma Skill com lógica de autoverificação e envie a instrução diretamente para criar a rotina agendada.
```text
每个工作日上午 8:30，运行“晨间资讯归档”Skill。如果数据源没有更新，记录日志后保持沉默。
```
3. Na lista de rotinas em Details, use o interruptor para alternar entre Pause ou Resume.

   Ao acessar o painel, é possível alterar Instruction, When to run e Webhook; a parte inferior oferece suporte a Pause/Resume, Test, Edit e Delete routine (ícone de lixeira).

### Teste de Execução a Seco (Dry Run) Antes da Entrada em Produção

As rotinas executam operações reais em máquinas virtuais na nuvem; **por padrão, todos os Bots compartilham o ambiente de execução subjacente sem isolamento por sandbox**, e uma perda de controle pode alterar arquivos reais. Antes de ativar, envie uma instrução no chat para validar com uma execução a seco (dry run).
```text
针对即将上线的例程“晨间资讯归档”，进行一次干跑验证：
1. 复述你理解的执行触发条件与完整业务流程。
2. 列出本次执行涉及读写操作的路径，以及可能产生风险的 3 个最高风险步骤。
3. 说明如果源文件损坏或格式错误，你的具体兜底动作。
现在不要执行任何实际写文件和网络请求操作，仅输出分析报告。
```

### Bloqueio com Travas de Segurança Humanas

Acesse Custom Rules (ou Auto-review) em Settings e **configure obrigatoriamente a aprovação manual para ações irreversíveis**.

| Instrução interceptada | Escopo da ação |
|---|---|
| `send` / `post` | Envio de mensagens externas, e-mails ou redes sociais |
| `buy` / `transfer` | Interfaces de pagamento e transferência |
| `delete` / `permissions` | Exclusão de arquivos/banco de dados, alteração de permissões |

Após o disparo da instrução, o sistema exibirá um card de aprovação pausando a execução e aguardando a confirmação humana, sem nunca realizar envios externos automaticamente.

## Integração via Webhook: Conectando Dispositivos Móveis e Pipelines Externos

Fonte: [Grok Bot Webhook + Atalhos: Construção de Pipeline de Entrada Automática na Base de Conhecimento](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)

### Credenciais e Status

Ao selecionar "Quando o webhook for disparado" na rotina, **é obrigatório clicar em Save para gerar o endereço, a chave e o Header**. Na v0.68.1, se o card não exibir a URL completa, **peça ao Bot para enviar o link no chat** para copiar; nunca compartilhe a chave em grupos públicos.

**Um retorno 200 indica apenas que a nuvem iniciou a execução, não que ela foi concluída**. Verifique o resultado na janela de chat; em caso de status diferente de 200, verifique se a rotina está em Paused e confira a chave.

### Atalhos

Com painel de compartilhamento (navegador, etc.):
1. Marque "Mostrar no Compartilhamento" para receber links e textos.
2. Use a ação "Obter Conteúdo do URL" para enviar um POST, preenchendo o cabeçalho com `Authorization: Bearer <key>` e adicionando o campo `content` no corpo JSON com a entrada do Atalho.

```text
接收端 Bot 的配套 Instruction 模板：
收到 Webhook 传入的 JSON 数据后，提取 content 字段中的链接。
如果是普通网页，抓取正文，提炼核心结论与知识点。
整理完成后，以 Markdown 格式追加写入知识库目录下的 inbox.md，包含收录时间、原文链接、核心观点与分类标签。
处理完毕后在聊天中输出一句话确认回执。
```

Sem painel de compartilhamento (WeChat, etc.):
1. Use "Solicitar Entrada" seguido de "Executar Atalho" para encaminhar.
2. Vincule ao Botão de Ação do iPhone 15 Pro ou à Tela de Início para enviar via pop-up após copiar.

**Arquivos grandes não podem ser inseridos diretamente no corpo da requisição**. Faça upload de áudios, vídeos e imagens em um serviço de armazenamento em nuvem para obter uma URL pública antes de enviar ao Bot.

## Avaliação Incremental para Evitar Execuções Ociosas: Arquitetura de Verificação em Duas Etapas

![Avaliação Incremental para Evitar Execuções Ociosas: Arquitetura de Verificação em Duas Etapas](/info/20-automation-s4.png)

Executar o modelo de linguagem a cada verificação de rotina consome muita cota; **divida o processo diretamente em duas etapas**.

1. Use o cron nativo do Linux para realizar a verificação mecânica.
2. **Apenas quando houver alteração nos dados**, acione o Webhook para despertar o Bot e processá-los.

Fonte: [Economize Ainda Mais Cota do Grok Bot: Otimização Extrema de Tarefas Agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).

### 1. Princípio do Desacoplamento: Divisão entre Despertador e Cérebro

Por trás do Grok Bot há um computador em nuvem Linux sempre ativo.

1. **Verificação mecânica**: use o cron para executar scripts que comparam dados. Durante essa etapa, **nunca chame nenhum LLM**; ele finaliza em poucos segundos sem consumir cota.
2. **Despertar incremental**: havendo alterações, envie um POST para o Webhook local, acordando o Bot para análise e sumarização.

Modificar as rotinas de espera entre 6 rotinas levou cerca de 23 minutos, reduziu de 8 a 10 execuções ociosas por semana e baixou a latência de um dia para menos de meia hora.

### 2. Passo a Passo de Configuração na Máquina Virtual

1. Adicione uma rotina "Central de Processamento Incremental" no Bot, selecione Webhook como gatilho e **salve a URL do Webhook e a chave Bearer com segurança**.
2. Abra o terminal e crie o script `check_update.sh` no workspace:

::: details 2. Passo a Passo de Configuração na Máquina Virtual
```bash
   #!/bin/bash
   # 监测目标 API 或页面是否有增量变化，纯机械对比，严禁调用 LLM

   TARGET_URL="https://api.example.com/v1/feed"
   STATE_FILE="/home/user/workspace/last_state.hash"
   WEBHOOK_URL="https://your-bot-webhook-url.com/api/v1/run"
   WEBHOOK_KEY="Bearer YOUR_SECRET_KEY"

   # 获取最新数据的哈希值或时间戳
   CURRENT_HASH=$(curl -s "$TARGET_URL" | md5sum | awk '{print $1}')

   if [ ! -f "$STATE_FILE" ]; then
       echo "$CURRENT_HASH" > "$STATE_FILE"
       exit 0
   fi

   OLD_HASH=$(cat "$STATE_FILE")

   # 比对是否有变化
   if [ "$CURRENT_HASH" != "$OLD_HASH" ]; then
       echo "检测到数据更新，正在唤醒 Bot..."
       echo "$CURRENT_HASH" > "$STATE_FILE"
       
       # 叫醒 Bot 进行智能分析
       curl -X POST "$WEBHOOK_URL" \
            -H "Authorization: $WEBHOOK_KEY" \
            -H "Content-Type: application/json" \
            -d '{"event": "data_changed", "source": "feed_monitor"}'
   else
       # 无变化，保持沉默，零额度消耗
       echo "无新变化，退出。"
   fi
   ```
:::

3. Instale e inicie o serviço cron no terminal:

```bash
   sudo apt-get update && sudo apt-get install -y cron
   sudo service cron start
   ```

Execute `crontab -e` para configurar o agendamento (dias úteis das 9h às 19h, com verificação a cada 30 minutos):

```cron
   */30 9-19 * * 1-5 /bin/bash /home/user/workspace/check_update.sh >> /home/user/workspace/cron_check.log 2>&1
   ```

- **Clicar em "Update computer" no cliente redefinirá o sistema**: embora os scripts do workspace permaneçam, o cron instalado via `apt-get` será apagado; após a atualização, é obrigatório reinstalar e iniciá-lo novamente.
- **Não chame APIs de LLM no script**: faça apenas verificações leves; delegar a avaliação ao modelo não reduz custos e apenas transfere os gastos para a cobrança da API.

## Eventos de Terceiros e Integração com a Plataforma X

### Gatilhos do Slack

Os gatilhos do Slack pertencem ao sistema de Routines; antes de usar, é necessário vincular o Slack à sua conta. Consulte a [Ajuda sobre Routines](https://cursor.com/cn/help/grok-bot/routines).

- **Nunca configure o gatilho "ao receber qualquer mensagem" em canais públicos**; conversas casuais de um único dia esgotarão a cota da semana inteira.
- Monitore apenas canais dedicados a notificações, como `#alerts-p0` ou `#deploy-status`.
- Exija obrigatoriamente um prefixo de ativação, como `!bot review` ou `@bot summary`.
- Responde apenas a novas mensagens geradas após a criação, sem retroagir ao histórico.

### Limites da Integração com a Plataforma X

A partir da v0.70.2, é possível buscar posts no X sem vincular uma conta pessoal.

Comentar @bot abaixo de um post notificará o Bot principal marcado com estrela para triagem. Consulte [4.3 Gatilhos e Automação: Agendamento, Webhook e Atribuição de Tarefas no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

- Limitações: não é possível analisar posts com vídeo; comentários contendo simultaneamente `@grok` e `@bot` entrarão em conflito e não acionarão o gatilho.
- Prevenção de injeção: **o Bot principal só tem permissão para resumir, categorizar e indexar; é estritamente proibido postar, curtir ou alterar o computador em nuvem automaticamente**, e todas as ações externas devem retornar ao cliente desktop para confirmação humana.

## Estratégias de Fallback e Tolerância a Falhas

![Estratégias de Fallback e Tolerância a Falhas](/info/20-automation-s6.png)

Timeouts de interface ou retornos vazios induzem facilmente a alucinações; a **Instruction deve conter uma declaração explícita de interrupção por exceção**:

```text
前置校验步骤：
1. 检查抓取到的内容体积。如果内容为空、包含 HTTP 错误码（如 403、404、500）或少于 50 个字符，判定为源不可用。
2. 源不可用时，立刻终止后续分析流程。
3. 在 workspace/logs/routine_errors.log 中追加一行错误记录，格式：[ISO时间戳] [任务名] SOURCE_UNAVAILABLE [原因]。
4. 不得在公开聊天窗口发送报警消息，不得使用过往缓存伪造新数据，直接以退出状态结束本次 run。
```

Solução de problemas em Webhook:
1. **401**: Verifique se o Header contém `Authorization: Bearer <key>`, evitando espaços ou quebras de linha adicionais ou o uso de uma chave antiga.
2. **404**: Confirme a integridade da URL, evitando exclusões acidentais no cliente desktop.
3. **429**: Limite de concorrência excedido; **é obrigatório implementar fila de novas tentativas com recuo exponencial (exponential backoff)**.
4. **Não executou**: Verifique se está em **Paused** ou se a chave **Active** no aplicativo móvel foi desativada.

**Gravação de logs em disco para evitar poluição visual**: notificações em cards só aparecem em interceptações para aprovação; os resumos são gravados em `docs/reports/YYYY-MM-DD.md`, e os logs de linha única são anexados a `workspace/run.log`.

## Monitoramento e Manutenção de Rotina

Visualize as rotinas em **Details** no cliente desktop ou no arquivo de configuração no celular; status **Failed** pode ser clicado para visualizar a pilha de erros (stack trace).

Consulte semanalmente **Usage & Billing** (a v0.70.2 corrigiu a exibição de consumo); aumentos repentinos de consumo indicam que há rotinas em execução ociosa ou em loop de repetição.

Dedique 15 minutos fixos toda sexta-feira para limpar as rotinas.
1. Abra `workspace/run.log` para verificar as saídas reais.
2. Coloque em **Pause** as rotinas sem atualizações incrementais por 7 dias consecutivos.
3. Após duas semanas pausada e sem dependências, use **Delete routine**; **a exclusão é irreversível e o Webhook correspondente é invalidado imediatamente**.

## Armadilhas Comuns

- **Comportamento em dias úteis**: definir "todo dia às 8h" é frequentemente interpretado apenas como dias úteis. Para tarefas ininterruptas (24/7), **o prompt deve especificar expressamente "incluindo sábado e domingo"**.
- **Desvio de fuso horário**: antes de criar uma Routine, acesse Settings -> Bot -> Timezone para conferir o fuso horário. A nuvem usa UTC por padrão, logo agendar para as 9h pode executar na madrugada.
- **Falha ao criar Bot pelo botão de adição**: criar via botão (+) na barra lateral costuma travar; se não funcionar, **faça com que um Bot maduro derive um novo Bot via diálogo**.
- **Credenciais não salvas**: ao configurar um Webhook, **é obrigatório clicar em Save na parte inferior para emitir as credenciais**; sair da página diretamente fará com que a chave não seja gerada.
- **Redefinição por atualização do sistema**: "Update computer" reinicializa a imagem do sistema e o cron instalado via `apt-get` será perdido; **acesse o terminal após a atualização para verificar o cron**.
- **Vazamento de chaves**: nunca cole a chave do Webhook em chats convencionais. Se enviar por engano, **apague a mensagem imediatamente e redefina a chave na rotina**.
- **Execução real com Test**: clicar em **Test** consome cota e altera arquivos; **é terminantemente proibido testar sobre dados de produção**.

## Como Homologar após a Conclusão

1. No cliente desktop, verifique a programação em inglês em When to run (por exemplo, "Every day at 8:00 AM CST"), alinhando-a ao fuso horário local e aos finais de semana.
2. Novas rotinas só rodam no ciclo seguinte; verifique se o horário em Next run está correto.
3. Renomeie a fonte de dados ou deixe-a vazia, clique em Test para rodar uma vez e confirme se o log registra "anomalia na fonte de dados" e para com segurança, sem alucinar informações.
4. Injete instruções para envio de e-mail, publicação de posts ou exclusão de diretórios e **confirme se a operação foi interceptada com a exibição de um card**, sem disparar pacotes externos diretamente.
5. No terminal, use o curl para enviar uma requisição POST ao Webhook:
```bash
   curl -i -X POST "你的_WEBHOOK_URL" \
        -H "Authorization: Bearer 你的_KEY" \
        -H "Content-Type: application/json" \
        -d '{"test": "ping"}'
   ```
Verifique se o **código de status 200 é recebido em até 1 segundo** e se, em até 30 segundos, o status do Bot muda para Running no cliente, retornando um recibo de confirmação e resultados estruturados.

## Leituras Complementares

- Capítulo relacionado: [Capítulo 8 Skills e Rotinas: Transforme um Sucesso Pontual em Execução Diária Automática](/part1/08-skills-routines)
- Capítulo relacionado: [Capítulo 10 Cotas e Custos: Fazendo o Consumo Semanal Durar a Semana Toda](/part1/10-usage)
- Documentação oficial: [Cursor Help: Routines](https://cursor.com/cn/help/grok-bot/routines)
- Artigo da comunidade: [4.3 Gatilhos e Automação: Agendamento, Webhook e Atribuição de Tarefas no X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- Artigo da comunidade: [Grok Bot Webhook + Atalhos: Construção de Pipeline de Entrada Automática na Base de Conhecimento](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- Artigo da comunidade: [Economize Ainda Mais Cota do Grok Bot: Otimização Extrema de Tarefas Agendadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
