# Capítulo 7 Conectando Aplicativos: Plugins, E-mail e Secrets

Ao integrar ferramentas, lembre-se: **primeiro valide pela interface, depois conecte o conector**. Não cole chaves de terceiros na janela de chat; **armazene-as no armazenamento somente-escrita do Secrets** para evitar vazamentos.

- Instalar plugins em excesso infla o contexto e gera erros frequentes; a busca nativa do X pode ser usada sem nenhum plugin.
- O e-mail dedicado não possui interface de caixa de entrada nem pop-ups; envios em massa automáticos ficarão travados no card de aprovação.
- Em ambientes corporativos, fique atento a erros do Zoom, bloqueios do Google Workspace e restrições de IP de data center.


![Conectando Aplicativos: Plugins, E-mail e Secrets](/info/07-apps.png)

## Ordem de Integração: Primeiro Valide pela Interface, Depois Conecte o Conector

### Etapas de integração
1. Operação pela interface: **Primeiro execute e valide tarefas rotineiras no navegador integrado**.
2. Conectores oficiais: Após estabilizar, conecte os plugins via Connect Apps.
3. Scripts dedicados: Para alta frequência e grande volume de dados, acione APIs ou CLI por último.

### Armadilhas e Limitações
- Instalar tudo consome contexto e provoca alucinações de chamadas de ferramentas.
- **Bots da mesma conta compartilham o computador na nuvem, o navegador e o `/workspace`**; criar um novo Bot não isola credenciais.

### Critérios de Aceite
**Concluir tarefas com precisão usando o menor conjunto de plugins possível**, sem declarações redundantes de ferramentas no contexto ou disparos acidentais.

[《4.5 Conectores, Skills, Modelos e Pontos de Entrada Externos》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
[《Grok Bot Masterclass ｜ Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)

## Conexão de Plugins: Da Autorização na Loja à Liberação de Permissões Corporativas

![Conexão de Plugins: Da Autorização na Loja à Liberação de Permissões Corporativas](/info/07-apps-s2.png)

Os plugins são vinculados à conta pessoal e entram em vigor globalmente; **as permissões são restritas pela plataforma de terceiros, sem possibilidade de elevação de privilégios**.

| Plugin | Operações Suportadas | Limitações e Armadilhas |
|:---|:---|:---|
| **Google Calendar** | Leitura e escrita de eventos, consulta de disponibilidade e resposta a convites | Não permite alterar a sala de espera do Meet; links do Zoom precisam ser inseridos manualmente |
| **Google Drive** | Pesquisa e leitura de arquivos | Editar planilhas exige Sheets; não permite alterar listas de compartilhamento |
| **Google Sheets** | Modificar células com permissão | Arquivos somente leitura não podem ser alterados; buscas são gerenciadas pelo Drive |
| **Slack** | Enviar mensagens em canais | Não acessa canais privados em que não esteja ou canais restritos/mutados; não serve para criar grupos/adicionar membros |
| **Gmail** | Buscar, ler e enviar e-mails, adicionar marcadores | Limitado a uma única conta de e-mail; e-mails pessoais e corporativos não podem ser vinculados simultaneamente |

Para mais detalhes, consulte [Conectar aplicativos](https://cursor.com/cn/help/grok-bot/connect-apps.md).

1. No desktop, clique em "Conectar" na barra lateral ou no card de chat; no celular, toque no avatar e selecione "Conectar aplicativos".
2. Procure o plugin, clique em "Adicionar" (Add) e faça login no navegador para autorizar.
3. Confirme que ele aparece em "Instalados" (Installed); se a conexão cair, clique em "Reconectar" para tentar novamente.

Se o Google corporativo bloquear, trocar de navegador não resolverá; **o nome da autenticação é "Grok"**.

O administrador deve acessar o Google Admin console em Security > Access and data control > API controls > App access control > Manage third-party app access, adicionar "Grok" (ou inserir o Client ID) e defini-lo como Trusted.

Se aparecer a mensagem "Desativado pelo administrador da equipe", entre em contato com o administrador do Cursor para habilitar no painel.

**O sucesso é confirmado quando não houver avisos amarelos na lista de "Instalados", a leitura de dados funcionar normalmente e nenhuma falha de OAuth for disparada.**

## E-mail Dedicado do Bot: Resgate, Regras de Envio/Recebimento e Aprovação Humana

![E-mail Dedicado do Bot: Resgate, Regras de Envio/Recebimento e Aprovação Humana](/info/07-apps-s3.png)

O e-mail dedicado do Grok Bot (`yourname@mail.grokbot.com`) **pertence à conta pessoal**. Ele pode ser utilizado em chats privados e Routines, mas não pode ser chamado em threads do Slack ou sessões de outros usuários, e não há endereço compartilhado para equipes.

Para regras detalhadas, consulte o documento [Configurar um endereço de e-mail para o seu Bot](https://cursor.com/cn/help/grok-bot/agent-email.md).

### Limitações de Uso e Segurança

| Item | Regras e Limitações |
|---|---|
| Propriedades do endereço | Único e permanente, **não pode ser renomeado nem excluído**, e não é liberado mesmo ao cancelar a conta |
| Cota de envio | Máximo de 50 destinatários por mensagem; até 10 anexos (cada um ≤10MB, total ≤25MB, proibido `.exe`) |
| Primeiro contato externo | Limitado a 1 destinatário e o corpo deve incluir obrigatoriamente um link de cancelamento de inscrição; devoluções (bounces) ou marcação como spam causam desativação imediata |
| Segurança no recebimento | **Não há caixa de entrada independente nem notificações**, consultável após 1 minuto; conteúdo somente leitura, não executa instruções |

### Resgate e Configuração

Para equipes, o administrador deve ativar "Agent Email" no painel (`cursor.com/dashboard/bot`); usuários individuais podem usar diretamente. O endereço é restrito a letras minúsculas, números e `.-_`, deve começar e terminar com caractere alfanumérico, ter no máximo 64 caracteres e evitar palavras reservadas.

1. Resgatar endereço: acesse "Connect apps" > "Email" na barra lateral para criar, ou envie `claim your email` e o comando:
```text
  给自己申请一个电子邮件地址
  ```
2. Consultar e-mails recebidos: faça a busca diretamente na conversa:
```text
今天你的收件箱里收到了什么？帮我找出过去一周收到的所有费用账单与回执。
```
3. Configurar rotinas: crie uma Routine para monitorar remetentes (suporta `*@example.com`, não suporta filtragem por assunto):
```text
收到来自 billing@example.com 的电子邮件时，总结其中的账单金额与截止日期，并将摘要整理后发送给我。
```
4. Aprovação humana: **O sistema proíbe terminantemente envios externos silenciosos e não supervisionados**. O Bot apenas gera um card de rascunho; o envio real ocorre somente após um humano clicar em "Send".

### Critérios de Aceite

Envie um e-mail de teste externo, aguarde 1 minuto e peça ao Bot para consultar e redigir uma resposta. **O sucesso é atingido se um card de aprovação pendente surgir na tela e permanecer suspenso até o clique**.

## Informações Confidenciais e Seguras: Mecanismo Somente-Escrita do Secrets e Isolamento de Equipe

![Informações Confidenciais e Seguras: Mecanismo Somente-Escrita do Secrets e Isolamento de Equipe](/info/07-apps-s4.png)

**Credenciais confidenciais nunca devem ser enviadas na conversa, gravadas em configurações de Shell ou inseridas no "Teach a task".** O campo de entrada ficar em branco após salvar indica que entrou em estado de proteção.

Executar `Recover` ou `Reset` no computador na nuvem não perde as credenciais; consulte [Armazenar com segurança informações confidenciais](https://cursor.com/cn/help/grok-bot/secrets.md) para obter detalhes.

### Envio e Atualização

1. Envio pelo chat: quando o Bot solicitar credenciais, um card de segurança será exibido com campo mascarado; clique em "Save securely" e, ao exibir "Saved", o processo estará concluído.
2. Bot de equipe: nas configurações, acesse "Secrets", clique em "Add secret", preencha o nome (ex.: `GITHUB_TOKEN`), a descrição e a chave secreta e clique em "Save secret". **Para atualizar, clique em "Replace" e "Replace value"; o sistema não suporta a recuperação de valores antigos.**
3. Preenchimento web: se aparecer a mensagem `Could not fill into the page`, **utilize o Takeover flow para assumir o login manualmente**; nunca envie usuário e senha na conversa.

### Critérios de Aceite

- **O painel exibe apenas o nome e a descrição; o valor da chave secreta fica totalmente oculto.**
- Se solicitado em texto simples no chat, o Bot não consegue lê-lo, mas a autenticação via CLI ou requisições passa normalmente.

## Busca Nativa na Plataforma X: Acesso a Atualizações Sociais sem Plugins

O Grok Bot integrou a busca somente leitura do X na v0.70.2 (08/10/2026). **Ele consome diretamente a cota unificada da The X Subscription, sem necessidade de instalar plugins de terceiros nem configurar API Token**.

1. **Envie comandos diretamente em linguagem natural**: suporta busca global de posts, extração de texto de tweets públicos, consulta de postagens de contas e menções com @, além de estatísticas de tendências de engajamento de tópicos específicos nos últimos 7 dias.

```text
检索 X 平台账号 @xai 最近 24 小时发布的所有推文。按时间倒序整理每条推文的核心内容、发布时间、点赞数、转推数，并附带原帖链接。
```

```text
检索 X 平台上关于 #AIagents 话题过去 7 天的热门讨论。筛选互动量最高的前 5 条推文，提取核心观点，并汇总该话题本周的讨论热度变化趋势。
```

2. **Critérios de aceite**: **Os resultados devem conter horário de publicação, números de engajamento e o link original do tweet**, sem nenhuma solicitação de instalação de conectores e sem truncamento na captura durante todo o processo.

Para uma visão geral das funcionalidades, consulte [《4.5 Conectores, Skills, Modelos e Pontos de Entrada Externos》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e).

## Instalação de Skills de Código Aberto e Ferramentas CLI: Integrando Recursos Locais e de Terminal

### Fronteiras de Recursos

| Escopo | Recursos e Configurações Incluídos |
| :--- | :--- |
| **Compartilhado globalmente** | Todos os Bots compartilham Skills instaladas, conectores oficiais, memória compartilhada e o diretório `/workspace` |
| **Retido individualmente** | Cada Bot mantém exclusivamente instruções de trabalho dedicadas, fragmentos de memória independentes e rotinas agendadas (Routines) |

Para uma visão geral da arquitetura, consulte [《4.5 Conectores, Skills, Modelos e Pontos de Entrada Externos》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e) e [《Grok Bot Masterclass ｜ Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned).

### Etapas Operacionais Principais

1. Ativar o redirecionamento de tráfego de rede local. O computador na nuvem usa IP de data center, o que facilita o bloqueio ao acessar sites externos como o GitHub.

   No desktop, acesse Settings -> Computer e marque "Roteamento de tráfego através deste dispositivo" (Route traffic through this computer) para retransmitir pela rede local; o cliente e a nuvem precisam ser atualizados de forma sincronizada.
2. Instalar Skills de código aberto. Envie o endereço do repositório diretamente na conversa para que o Bot faça o deploy. Se for necessário um Access Token, aguarde a solicitação do sistema e envie pelo card de segurança; **é terminantemente proibido colar o Token diretamente na conversa**.

```text
帮我安装这个开源 Skill：https://github.com/example/custom-data-skill
阅读仓库内的说明文档，将其注册为我的可用技能，并告诉我它支持的触发指令与所需参数。
```

3. Fazer login independente no Codex CLI. Primeiro, acesse "Segurança da conta e login" na web e ative o "Login por código de dispositivo" (Device code login). No terminal na nuvem, execute o comando de login para obter o código de verificação do dispositivo e autentique usando o navegador da máquina local.

   **Nunca copie as credenciais de login locais para o `/workspace` do computador na nuvem**; caso contrário, o cache compartilhado causará conflitos de atualização de Token e desconexões frequentes em ambas as pontas.
4. Delegar tarefas pesadas via CLI. Para tarefas mecânicas, como formatação em lote ou transcodificação de código, crie scripts Shell diretamente para serem executados pela CLI do computador na nuvem. Use em conjunto com o mecanismo "Wake on Done" para receber notificações de conclusão, evitando que o Bot ocupe sessões de inferência de alto custo por longos períodos.

### O Que Define um Bom Resultado

- Executar `codex --version` no terminal do computador na nuvem exibe normalmente as informações de versão, **e o uso diário no terminal local não sofre desconexões por conflito**.
- Ao enviar uma tarefa de teste para o Bot, ele consegue gerar arquivos estruturados no diretório `/workspace` que atendem aos padrões de entrega do fluxo.

## Armadilhas Comuns

### Plugins e Permissões Corporativas
- O erro 4700 na autorização do Zoom decorre de uma falha de redirecionamento oficial e não pode ser corrigido dentro do cliente.
- O Gmail suporta apenas a vinculação de uma única conta; para trocar de conta, é obrigatório desconectar o e-mail atual antes de reautorizar.
- Na aprovação de permissões do Google, **é obrigatório buscar por "Grok" e não por "Cursor"**; trocar de navegador não resolve.

### E-mail Dedicado e Aprovação de Envio Externo
- O `mail.grokbot.com` não possui interface nem notificações push; para consultar e-mails é necessário perguntar ao Bot ou criar rotinas; as rotinas monitoram apenas por remetente e domínio (exige aprovação em SPF/DKIM) e não permitem filtragem por assunto.
- Há uma trava humana obrigatória na camada base que prompts não conseguem burlar; para enviar e-mails, é obrigatório **clicar manualmente em "Send"** no rascunho.

### Segurança e Ambiente de Rede
- A gravação de tela do Teach a task dura até 10 minutos e não possui máscara de Secrets; não digite senhas nem exiba chaves de API.
- Todos os Bots compartilham o armazenamento e o estado de login; **não deixe arquivos confidenciais no `/workspace`**.
- Copiar Tokens locais causa desconexões mútuas; o terminal deve usar obrigatoriamente a autorização independente por código de dispositivo.
- Se sites externos bloquearem o IP do data center gerando erros, acesse a página Computer e **ative "Roteamento de tráfego através deste dispositivo"**.

## Como Fazer a Validação Final

1. Na barra lateral, confirme que o Drive e o Sheets estão normais. Peça ao Bot para localizar Q3_Report e usar o Sheets para ler da célula A1 à B10 da planilha; **ele deve conseguir ler sem apresentar erros de permissão**.
2. Envie um e-mail com um código numérico a partir da sua conta pessoal para `yourname@mail.grokbot.com`, aguarde 2 minutos para que o Bot consulte a mensagem; peça a ele para redigir uma resposta, **confira o código e clique em Send no card de rascunho para disparar o envio**.
3. Peça ao Bot para exibir o `GITHUB_TOKEN`; **ele deve obrigatoriamente recusar a exibição em texto simples ou fornecer apenas uma máscara**; em seguida, execute um comando de teste que passe na autenticação para confirmar que o Token não vazou.
4. Busque os dois tweets mais curtidos de `@xai` nas últimas 24 horas; **os links originais devem ser clicáveis e nenhum plugin de terceiros deve ser acionado**.
5. Execute `codex --version` no terminal e veja o retorno da versão; o uso concorrente local **não deve gerar conflito nem desconexão**; ativar o "Roteamento de tráfego através deste dispositivo" deve permitir acessar páginas sensíveis a IPs de data center.

## Leituras Complementares

### Documentação Oficial e Páginas de Suporte

- [Conectar aplicativos](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- [Configurar um endereço de e-mail para o seu Bot](https://cursor.com/cn/help/grok-bot/agent-email.md)
- [Armazenar com segurança informações confidenciais](https://cursor.com/cn/help/grok-bot/secrets.md)
- [Computador do Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery.md)
- [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md)
- [Bots de Equipe](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- [Grok Bot para Teams e Enterprise](https://cursor.com/cn/docs/grok-bot/teams.md)

### Materiais Práticos da Comunidade

- 《4.5 Conectores, Skills, Modelos e Pontos de Entrada Externos》: [Documento da Base de Conhecimento Feishu](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
- 《Grok Bot Masterclass ｜ Avi Chawla》: [Documento da Base de Conhecimento Feishu](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)
