# Capítulo 25 Perguntas Frequentes e Solução de Problemas

Ao encontrar erros ou travamentos, **nunca reinstale ou redefina às cegas**, pois isso apagará o ambiente recém-configurado e os scripts temporários.

1. **Primeiro verifique o status do serviço**.
2. Em seguida, investigue se o problema é de rede local, autorização de plugins, ambiente em nuvem ou cota semanal.


![Perguntas Frequentes e Solução de Problemas](/info/25-faq.png)

## O que fazer quando houver problemas no login e na vinculação de contas do Grok Bot? {#login-e-autenticacao}

**Usuários individuais vinculam e autorizam pela página de configurações ou link dedicado; assentos corporativos fazem login diretamente com o Grok; se vincular errado, é necessário contatar o suporte humano; se entrar em loop de redirecionamento, limpe os cookies e autentique em modo anônimo.**

### Limites de conta e assinatura
O Grok Bot é executado com base no Cursor e não tem relação com o paywall do aplicativo móvel do Grok nem com o limite semanal (Weekly SuperGrok Limit).

A versão individual oferece suporte ao SuperGrok e às versões Plus e Heavy, além do X Premium+; o SuperGrok Lite e o Grok Enterprise não podem ser vinculados a contas individuais, e os assentos corporativos são distribuídos de forma unificada pelos administradores.

**O e-mail da conta não pode ser alterado após o registro, e a vinculação com o Cursor é uma associação permanente e única**. Se vincular a conta errada, não será possível transferi-la por conta própria; é obrigatório entrar em contato com o suporte humano.

### Passos para vinculação e login
1. Vinculação individual: abra [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) ou acesse no aplicativo **Configurações** > **Uso e Faturamento** e, em **Gerenciar Planos**, clique em **Obter acesso via Grok** (exibido apenas se puder elevar o nível de uso atual).
2. Assentos corporativos: quem possui um assento Grok Business não precisa vincular manualmente na página de planos; basta sair completamente e clicar em **Sign in with Grok** na página de login.
3. Confirmação do serviço: ao encontrar anomalias, acesse primeiro [status.cursor.com](https://status.cursor.com) para verificar o status em tempo real do **Grok Bot**; para os requisitos de operação, consulte [Fazer login no Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

   **Em caso de falha no serviço, aguarde a correção oficial; nunca reinstale o aplicativo nem redefina o computador**.

### Solução de problemas e validação
Versões desatualizadas do aplicativo podem causar incompatibilidade de protocolo; para falhas repentinas de autenticação, recomenda-se aguardar de 30 a 60 minutos antes de tentar novamente. **O critério de aceitação é a correspondência unívoca entre o e-mail da conta, a titularidade da assinatura e o status de login do cliente**.

| Sintoma da falha | Procedimento correto | Ação estritamente proibida |
| :--- | :--- | :--- |
| Loop de retorno à página de login | Limpar os cookies de `cursor.com` e `x.ai`, autenticar usando o modo anônimo no desktop | Desinstalar e reinstalar o cliente repetidamente |
| Não encontra a entrada de vinculação | Confirmar se o nível da conta atual é inferior ao plano a ser vinculado e não atingiu o limite | Registrar uma nova conta e comprar novamente |
| Mensagem indicando Model provider is overloaded | Copiar o Request ID do erro, aguardar 2 minutos e reenviar | Clicar imediatamente em Reset para redefinir o computador |
| Mensagem indicando necessidade de alteração de e-mail | Registrar novamente uma conta e migrar os recursos | Tentar alterar forçadamente o e-mail vinculado nas configurações |

Envie um prompt ao Bot para confirmar o status de login.
```text
请检查当前运行环境的网络连通性与 Cursor 身份验证状态，汇报当前登录的用户环境标识，但不要输出任何敏感 Token。
```

## Como recuperar o Grok Bot quando ele não consegue se conectar ao computador em nuvem? {#computador-em-nuvem-e-recuperacao-de-ambiente}

**Se ocorrer desconexão, aguarde dois minutos para tentar novamente ou reinicie totalmente o aplicativo; se travar, clique em Recover para salvar o estado e reconstruir; já o Reset, que sobrescreve o snapshot e perde alterações não sincronizadas, deve ser apenas o último recurso.**

![Computador em nuvem e recuperação de ambiente](/info/25-faq-s2.png)

Todos os Bots compartilham o mesmo computador em nuvem. **O histórico de conversas fica armazenado separadamente no banco de dados**, não sendo perdido mesmo com falhas ou limpezas.

Quando for exibido Reconnecting, Couldn't Reach Grok Bot's Computer ou Bot failed to respond:
1. Aguarde de 1 a 2 minutos e clique em Retry.
2. Encerre totalmente o aplicativo. No Mac, pressione `Cmd+Q`; no Win/Linux, saia pela bandeja do sistema, não feche apenas a janela.
3. Vá em Configurações > Computador e clique em Atualizar. Nunca interrompa enquanto o backup não terminar ou enquanto o Bot estiver trabalhando.
4. Se travar, clique em Recover.
5. **Reset é o último recurso**. A sobreposição do snapshot causará perda de alterações não sincronizadas. Veja detalhes em [Computador do Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery).

|Operação|Preservação do estado|Impacto no ambiente|Cenário|
|---|---|---|---|
|Retry|Mantido intacto|Sem impacto|Instabilidade de rede|
|Update|Aguardar conclusão do backup|Mantém todos os softwares; limpa pacotes instalados pelo usuário em toda a máquina|Patches oficiais|
|Recover|Salva estado e recria máquina|Remove aplicativos e ambientes autoinstalados|Travamento ou corrupção|
|Reset|Sobrescreve snapshot|Perde alterações não sincronizadas|Último recurso se não conectar|

O reparo é considerado concluído quando o **status do computador ficar verde indicando conectado**, o terminal funcionar normalmente e as configurações estiverem intactas.

- Em caso de login por SSO, clique em Take over no card para autenticar manualmente; ao concluir, clique em I'm done.
- Chave de segurança e rede: ative Use hardware security keys em Configurações > General > Security Key e conecte a YubiKey; se encontrar CAPTCHA, marque "Rotear tráfego através deste computador" em Configurações > Computador.
- Execução local: ative "Executar neste computador" em Configurações > Computador (confirme antes de executar comandos). Veja detalhes em [Configurações do Grok Bot](https://cursor.com/cn/docs/grok-bot/settings).
- Alerta de disco: quando for exibido Computer is low on disk space, clique em Go to Disk Saver; **a exclusão só deve ocorrer após confirmação manual**.

```text
请检查当前云端计算机根目录与工作目录的磁盘占用情况，找出体积超过 200MB 的文件与缓存目录，列出清单供我确认，不要擅自执行任何删除命令。
```

## Como solucionar problemas quando as rotinas automatizadas do Grok Bot não são acionadas? {#gerenciamento-de-rotinas-e-solucao-de-problemas-de-automacao}

**Se a rotina não responder, confirme primeiro se o status não está pausado, ajuste o fuso horário e execute o teste com Test; o Webhook exige chave de autenticação e o código 200 indica apenas enfileiramento; o acionamento via Slack deve obrigatoriamente restringir canais por lista de permissões e palavras de filtro.**

![Gerenciamento de rotinas e solução de problemas de automação](/info/25-faq-s3.png)

As rotinas rodam automaticamente na nuvem, continuam ativas mesmo com a máquina desligada e oferecem suporte a agendamentos, Webhooks e notificações do Slack.

1. **Verificar status e fuso horário**: em Details, confirme se não está como **Paused** (no celular, verifique **Active**); selecione manualmente o fuso horário em "Configurações > Bot > Timezone"; evite usar Auto-detect em operações transfronteiriças.
2. **Momento do disparo agendado**: aguarda apenas o próximo ciclo (se configurar às 09:05 para as 09:00, rodará na manhã seguinte); para testar a lógica imediatamente, clique em **Test**.
3. **Validar Webhook**: envie POST com `Authorization: Bearer <key>`. **O código 200 indica apenas enfileiramento**, veja o resultado na janela de chat; status diferente de 200 indica chave incorreta ou rotina pausada.
4. **Restringir disparos no Slack**: **é obrigatório limitar canais e palavras de filtro** para evitar que conversas casuais consumam toda a sua cota em poucas horas. Veja detalhes em [Rotinas](https://cursor.com/cn/help/grok-bot/routines).

No celular, consulte o "Histórico de execuções" para ver **Running**, **Succeeded** e **Failed**; a exibição de **No runs yet** indica que não houve acionamento.

| Falha | Causa | Correção |
|---|---|---|
| Sem atividade | Paused/ainda não atingiu o horário/desvio de fuso horário | Verificar Active, clicar em Test, conferir Timezone |
| 401/403 | Token ausente/chave redefinida/rotina excluída | Copiar novamente o header e sobrescrever a configuração |
| Sem resposta no Slack | Mensagem antiga/canal ou palavra não correspondente | Reconhece apenas novas mensagens; conferir lista de canais permitidos e frases |
| Consumo rápido de cota | Intervalo muito curto/grupos grandes sem palavras de filtro | Pausar a rotina, aumentar o intervalo, restringir a canais de operações |

Prompt para criação e correção de rotinas automatizadas:
```text
请修改名为“工单同步”的例程：仅在 #ops-alert 频道出现包含“[P0-Error]”文字的新消息时才触发，忽略其他日常聊天，并列出更新后的 When to run 描述。
```

## Anomalias de Uso e Controle de Cotas

![Anomalias de uso e controle de cotas](/info/25-faq-s4.png)

A cota do Grok Bot é redefinida semanalmente. Quando a cota básica se esgota, as respostas são interrompidas; **isso se trata de um mecanismo normal de corte por limite de cota**. As cotas de avaliação única esgotadas em tarefas complexas não podem ser recuperadas.

### Operação e armadilhas a evitar
1. Recuperar cota: aguarde a renovação semanal, ative o uso sob demanda em **Configurações** > **Uso e Faturamento** ou faça upgrade da assinatura.
2. Definir limite: configure o limite no aplicativo ou no site [cursor.com/dashboard](https://cursor.com/dashboard). **Tarefas em execução não são interrompidas bruscamente, e é normal que a cobrança exceda ligeiramente em alguns pontos percentuais.**
3. Alinhamento de cotas: contas externas não acumulam benefícios e prevalece o nível mais alto (Pro corresponde a SuperGrok/X Premium+, Pro+ a SuperGrok Plus e Ultra a SuperGrok Heavy).
4. Cancelamento em dispositivos móveis: a assinatura é compartilhada entre várias plataformas. Pagamentos via loja devem ser cancelados no Apple ID ou no Google Play, pois a equipe oficial não faz reembolsos diretos; consulte [Planos e Faturamento](https://cursor.com/cn/help/grok-bot/plans).

### Critérios de aceitação
| Cenário | Operação | Limites e armadilhas |
| :--- | :--- | :--- |
| Prevenção de excesso | Definir limite mensal no cliente ou console | **O teto recusa novas solicitações; tarefas em execução param somente após terminar** |
| Consultar uso | Verificar saldo restante em tempo real nas configurações internas do Bot | O painel externo do Grok não se comunica com ele |
| Avaliação zerada | Verificar varreduras de grandes projetos ou refatorações | Cota única esgotada não é restaurada |

```text
请列出你当前账号下所有处于活跃状态的例程，评估它们各自的执行频率与触发条件，指出哪一个例程最容易引发高额用量消耗。
```

## Chats em Grupo, Colaboração e Governança de Bots Auxiliares

Bots auxiliares aparecem na barra lateral e exibem notificações; modificações em arquivos ou conexões com a rede externa acionam a aprovação do **Auto-review**.

### Operação e aprovação
1. Redução de ruído e ocultação: no desktop, clique com o botão direito e selecione Hide from sidebar ou envie um comando para desativar as notificações; no celular, acesse as configurações para desativar as notificações.
2. Restaurar bots ocultados por engano: no desktop, em **Robôs ocultos**, selecione Show in sidebar; no celular, selecione Unhide. **É estritamente proibido clicar em Recover ou Reset na nuvem apenas para localizar um Bot.**
3. Aprovação e lista de permissões: para operações de alta frequência, clique em **Sempre permitir** (armazenado em Configurações > Bot > Regras personalizadas); em caso de conflito, pergunte primeiro; itens exibidos como "Exigido pelo administrador" não podem ser ignorados.

   Para normas, consulte o [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to).

### Critérios de aceitação
Barra lateral sem Bots desnecessários, com operações rotineiras de alta frequência **aprovadas automaticamente sem interrupção**.

|Cenário|Tempo limite|Comportamento|Solução|
|---|---|---|---|
|Manual em primeiro plano|Espera permanente|Permanece suspenso|Permitir ou recusar após verificação|
|Segundo plano/Webhook|Cerca de 10 minutos|Muda para Expired e é cancelado|Configurar "Sempre permitir" ou ativar notificações|
|Obrigatório pelo administrador|Conforme o cenário|Não pode ser ignorado|Autorização manual obrigatória|

```text
请梳理我们在此会话中频繁执行的文件读取与构建指令，为它们生成一组最小权限的安全规则建议，以便我添加到 Auto-review 的自定义白名单中。
```

## Plugins e Conexão com Aplicativos Externos

### Solução de problemas de autorização
**Added indica apenas que foi instalado, não significa que o login foi feito**. Se o card não aparecer, vá até a barra lateral para autenticar manualmente. **A autorização deve ser concluída em 10 minutos**; se expirar, clique em Reopen; se os erros persistirem, clique em Remove para remover e reinstalar.

| Status | Ação |
| :-- | :-- |
| **Added / Needs auth** | Clicar em "Verificar identidade" para fazer login no navegador |
| **Erro em Connected** | Enviar comando com o nome do plugin para atualizar a sessão |
| **Disabled by team admin** | Solicitar o desbloqueio ao administrador da equipe |

### Múltiplas contas e validação
1. **Múltiplas contas**: em "Conectar aplicativos" > Plugin > Accounts, clique em **Add Another Account** (no celular, toque em Authorize new account) e adicione uma etiqueta. Indique a etiqueta na conversa para chamar; se o botão não existir, há suporte apenas para conta única.
2. **Validação**: **o status exibe Connected em verde com etiqueta clara**, e o envio de comandos consegue chamar com precisão logo na primeira tentativa.

Veja detalhes em [Conectar aplicativos](https://cursor.com/cn/help/grok-bot/connect-apps.md).

```text
请刷新当前已连接的插件列表，使用带有“工作”标签的账户连接，读取最近更新的 3 个页面，确认授权是否正常。
```

## Cancelamento de Conta e Limpeza de Dados

O Grok Bot compartilha a conta do Cursor; **a exclusão da conta é irreversível** e não é possível manter o Cursor isoladamente. Para usar em outro computador, basta sair da conta ou desinstalar.

### Etapas para encerramento de conta
Antes de encerrar a conta, cancele obrigatoriamente a renovação automática para evitar disputas de cobrança.
1. No celular (iOS/Android): toque no avatar para acessar "Configurações" > Informações da conta > "Excluir conta" e digite "**Excluir**" na validação da página web para confirmar.
2. Desktop e web: **não é possível encerrar diretamente pelo aplicativo**. Faça login em [cursor.com/dashboard](https://cursor.com/dashboard) > "Configurações" > "Mais" > "Excluir conta" para confirmar.
3. Assentos corporativos ou de equipe: indivíduos não podem encerrar de forma independente; é obrigatório contatar o administrador para desvincular ou abrir um chamado. Veja os termos em [Excluir sua conta do Grok Bot](https://cursor.com/cn/help/grok-bot/delete-account).

### Limpeza de recursos e armadilhas a evitar
| Ativos e assinaturas | Resultado do descarte | Ação obrigatória |
| :--- | :--- | :--- |
| Conversas e ambiente na nuvem | Eliminação física e destruição de snapshots **em até 30 dias** | Exportar códigos e conversas com antecedência, baixar arquivos |
| Arquivos locais | Permanecem intactos | Nenhuma ação necessária |
| Assinaturas avulsas nas lojas e no X | **Não serão canceladas automaticamente** | É necessário cancelar manualmente na Apple, Google ou x.ai |

## Obtenção de Suporte Oficial e Padrões para Abertura de Chamados

### Como fazer
Se a solução de problemas local não resolver, envie um e-mail para **hi@cursor.com**. **Não envie apenas descrições vagas como "meu Bot quebrou"**; inclua todos estes seis itens no e-mail:

1. Credenciais da conta: e-mail de registro.
2. Ambiente de execução: plataforma e número da versão do cliente. Acesse Menu da conta > Suporte > Sobre e clique em Copy version info para copiar.
3. Operação que pretendia executar: explique qual tarefa tentava rodar antes da falha.
4. Comprovante real do erro: pop-up completo de erro, logs do console ou capturas de tela do faturamento.
5. Registro de tentativas de solução: detalhe quais verificações já foram feitas para evitar que o suporte repita sugestões.
6. Request ID: clique com o botão direito na mensagem de erro ou passe o mouse sobre More message actions e selecione Copy request ID. Se essa opção não estiver disponível, é obrigatório anexar o texto original do erro e uma captura de tela completa.

No Linux, se aparecer Update required e a atualização automática falhar, execute o comando de atualização no terminal de acordo com a sua distribuição:
- Debian / Ubuntu: `sudo apt update && sudo apt install --only-upgrade grok-bot`
- Série Fedora / RPM: `sudo dnf upgrade --refresh grok-bot`

::: details Como fazer
```text
收件人：hi@cursor.com
主题：【Grok Bot 故障申报】云端电脑持续重连且 Recover 失败 - [你的账号邮箱]

支持团队：
我的账号遇到了云端电脑无法连通的故障，无法正常执行任务，以下是详细环境与排查信息：

1. 账号邮箱：developer@example.com
2. 版本信息：Version 1.2.4 (Channel: stable, OS: Darwin x64 23.4.0)
3. 故障发生场景：我尝试让 Bot 运行自动化部署脚本，终端在拉取镜像时中断。
4. 核心报错信息：界面持续提示“Couldn't Reach Grok Bot's Computer”，伴随“Bot failed to respond”。
5. 已尝试的排错操作：
   - 已彻底 Quit 应用并重启；
   - 尝试在“设置 > 计算机”执行 Update，提示备份未就绪；
   - 尝试点击 Recover，重试一次后依然在进度条处卡住报错；
   - 查看 status.cursor.com 确认官方各项服务状态正常。
6. 请求 ID (Request ID)：req_98af7c32e01b44d7a1
7. 附件：包含当前报错卡片截图及“设置 > 计算机”面板状态截图。

请协助在后台检查该实例的宿主节点状态，谢谢。
```
:::

### Critério de qualidade
**Após o envio, você recebe uma confirmação automática e a equipe técnica consegue acessar os logs sem precisar fazer perguntas adicionais**. Para padrões detalhados, consulte [Obter ajuda](https://cursor.com/cn/help/grok-bot/get-help.md).

## Casos Típicos de Solução de Problemas

### Caso 1: Loop de Reconnecting no computador em nuvem
Ao receber a mensagem Couldn't Reach Grok Bot's Computer, **nunca clique primeiro no destrutivo Reset**.
1. Acesse [status.cursor.com](https://status.cursor.com) para confirmar se os serviços estão normais e pressione `Cmd+Q` para reiniciar o aplicativo.
2. Acesse Configurações > Computador; se houver aviso de que a pausa não ocorreu a tempo, aguarde cerca de 5 minutos para que ocorra o tempo limite em segundo plano.
3. Quando a opção Recover do computador ficar disponível, clique para recuperar e execute novamente o script de instalação para **preservar os scripts anteriores e o estado de login**.

### Caso 2: Esgotamento repentino de cota por gatilhos do Slack
Devido ao monitoramento de conversas casuais no canal `#general` com mais de 3.000 pessoas, a cota semanal foi zerada em 24 horas.
1. **Defina primeiro um limite mensal rígido para o uso sob demanda no painel de gastos** para evitar cobranças no cartão de crédito.
2. Altere a rotina para Paused para estancar o consumo.
3. Restrinja a regra para "acionar apenas em `#bot-help` e quando mencionado com `@Grok`".
4. Clique em Test para fazer uma validação única antes de colocar novamente em produção.

### Caso 3: Falha de autenticação no Notion e login por controle manual
Quando o Notion exibir Action needed e houver interceptação pelo Okta SSO, **é obrigatório usar Take over para concluir a autenticação no navegador integrado**.
1. Ao ver o aviso Needs auth, clique em Take over no card para assumir o controle.
2. No navegador integrado da nuvem, insira as credenciais corporativas, conclua a autenticação em duas etapas e clique em I'm done.
3. Em Accounts, clique em Add Another Account para autorizar o espaço de trabalho pessoal e **adicione a etiqueta "Workspace Pessoal" para evitar conflito de credenciais**.

## Armadilhas Comuns

1. Se perder o chat, não clique em Reset, pois isso apagará seu código. Para recuperar, primeiro **saia e reinicie**, confira a conta do Cursor ou verifique os robôs ocultos.
2. Uma rotina das 14:00 configurada às 14:05 só rodará no dia seguinte; para testar a lógica, clique em **Test**.
3. Monitorar grupos grandes do Slack sem palavras de ativação fará com que cumprimentos rotineiros **queimem toda a cota da semana**.
4. Excluir o app não cancela a cobrança; para cancelar a assinatura, acesse a central de assinaturas no **Apple ID ou Google Play**.
5. Clicar em Reset durante o status Updating **corromperá o sistema de arquivos**, exigindo intervenção do suporte humano.
6. Ao ver Added no plugin, certifique-se de que ele esteja como **Connected**; se exibir Needs auth, é necessária autorização pelo navegador.
7. Update, Recover ou Reset limparão `node_modules` e `.venv`; declare as dependências em um **script de inicialização**.
8. Os cards de aprovação **expiram e são cancelados após 10 minutos (Expired)**; lembre-se de ativar as notificações ou configurar "Sempre permitir".

## Critérios de Validação Final

- Verifique se [status.cursor.com](https://status.cursor.com) não apresenta falhas e se o e-mail está correto.
- Acesse Configurações > Computador para verificar a luz verde e envie comandos Linux básicos ao Bot para testar a resposta.
- Mantenha as rotinas ativas, confira o fuso horário em When to run e clique em Test para validar a execução.
- Acesse Configurações > Uso e Faturamento e **defina obrigatoriamente um limite mensal para o uso sob demanda** para evitar faturas astronômicas.
- Certifique-se de que os aplicativos conectados exibam Connected, que operações de escrita acionem o Auto-review e que as notificações cheguem ao celular.
- No chamado, forneça apenas o Request ID e as informações de Copy version info; **nunca divulgue o cabeçalho de requisição com o Bearer Token**.

## Leituras Complementares

- Capítulo relacionado: [Capítulo 5 Computador em nuvem compartilhado: arquivos, navegador e controle](/part1/05-computer)
- Capítulo relacionado: [Capítulo 10 Cotas e custos: fazendo o uso semanal durar a semana toda](/part1/10-usage)
- [Respostas oficiais para perguntas frequentes do Grok Bot](https://cursor.com/cn/help/grok-bot/faqs)
- [Guia de operação e solução de problemas do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)
- [Gerenciamento de ambiente do computador do Grok Bot e recuperação de desastres](https://cursor.com/cn/help/grok-bot/computer-recovery)
- [Configuração detalhada de rotinas automatizadas e gatilhos](https://cursor.com/cn/help/grok-bot/routines)
- [Estrutura de contas e instruções de encerramento](https://cursor.com/cn/help/grok-bot/delete-account)
- [Contato com a equipe de suporte e padrões de chamados](https://cursor.com/cn/help/grok-bot/get-help)
- [Referência das configurações globais do sistema do Grok Bot](https://cursor.com/cn/docs/grok-bot/settings)
