# Capítulo 22: Integração com Feishu e WeChat

Sem a necessidade de um IP público ou de um servidor próprio, é possível integrar o Grok Bot com segurança ao Feishu e ao WeChat.

O The X Subscription (em vigor a partir de 12 de outubro de 2026) deduz cotas semanalmente; **os chats em grupo devem ser configurados com filtragem de mensagens**, caso contrário, conversas casuais esgotarão a cota de toda a semana.

- **Colaboração com múltiplos bots no Feishu**: utiliza a conexão persistente oficial do Python SDK e o modelo do "Gerenciador de Aplicativos Feishu".
- **Conexão direta com o ClawBot do WeChat**: conta com o plugin oficial "WeChat ClawBot" e a interface iLink.
- **Captura via Atalhos do WeChat**: utiliza os Atalhos da Apple e Webhooks para arquivar registros.


![Integração com Feishu e WeChat](/info/22-feishu-wechat.png)

## Comparação de Canais de Acesso e Seleção Técnica

![Comparação de Canais de Acesso e Seleção Técnica](/info/22-feishu-wechat-s1.png)

**Nenhum dos três métodos de integração exige IP público**.

- Canal de múltiplos bots no Feishu: usado para trabalho em equipe e distribuição de tarefas em chats em grupo. Utiliza conexões persistentes WebSocket de saída oficiais, suporta rich text e cartões interativos, e responde apenas a @ no grupo para proteger a cota.
- Canal do ClawBot no WeChat: usado como assistente pessoal diário e orquestração. Utiliza long polling via iLink, suporta apenas texto puro e depende de whitelist em conversas individuais para evitar acionamentos desnecessários.
- Canal de Atalhos do WeChat: usado para catalogação de ativos multimídia e textos. Utiliza push unidirecional via Webhook com recibo de retorno, acionado sob demanda, sem consumo extra na ausência de mensagens.

## Integração de Equipe ao Feishu: Colaboração com Múltiplos Bots e Gerenciador de Aplicativos Feishu

![Integração de Equipe ao Feishu: Colaboração com Múltiplos Bots e Gerenciador de Aplicativos Feishu](/info/22-feishu-wechat-s2.png)

### Conexão Persistente no Feishu e Mecanismo de Gatilho por Campainha

Utilizando conexões persistentes de saída, **elimina-se a necessidade de IP público, certificados e portas abertas**.

1. Aplicativo personalizado do Feishu: responsável pelo envio e recebimento em chats em grupo e individuais.
2. Programa de encaminhamento na nuvem: monitora a conexão persistente em segundo plano e realiza o repasse.
3. Gatilho de campainha: desperta o bot e aciona o SDK para responder.

Para evitar configurações repetitivas, use o "Gerenciador de Aplicativos Feishu" para **criar aplicativos automaticamente via leitura de código QR**.

### Como Fazer: Da Execução com Bot Único à Colaboração com Múltiplos Bots

#### Escaneie o QR Code para Criar o Primeiro Bot (Editor-Chefe de Artigos)
1. Em uma conversa privada, solicite ao bot que chame o SDK do Feishu para gerar o link de criação de aplicativo via QR code. **Este link é uma credencial de uso único e restrito a administradores; nunca clique em links de terceiros nem os encaminhe.**
2. Abra o link no navegador, clique em "Criar", confirme as permissões e as credenciais serão transmitidas de volta automaticamente.
3. Após receber a mensagem de teste no Feishu, responda a ela; **o bot adicionará automaticamente seu Open ID à whitelist**.

#### Criar a Rotina de Campainha
1. Clique no nome do bot no topo da conversa e abra o painel **Details** nas informações. Consulte os passos em [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md).
2. Nas rotinas, crie uma campainha Webhook e obtenha o endereço POST to e a key.
3. **Você deve enviar as credenciais na caixa de diálogo criptografada exibida pelo bot**, evitando vazamento em texto simples. Envie um texto de teste na conversa individual; se o bot responder normalmente, a integração está concluída.

#### Criação em Lote de Aplicativos e Colaboração em Grupo
1. Importe o modelo `https://x.ai/bot/AJpUlCwa8tyMX7L5UHnuY`. Salve a tabela de registros e os scripts de recuperação em um repositório privado do Git, sem armazenar chaves em texto simples.
2. Comande o bot gerenciador a gerar em lote os links de escaneamento de QR code (**cada link é válido por 1 hora**), escaneie-os, preencha a key na janela criptografada, e o gerenciador iniciará o encaminhamento automaticamente.
3. Crie um grupo e adicione os bots, **envie `@所有人` para confirmar o escopo de atuação de cada um**; `@文章主编` aciona `虚拟机服务管家`, e o gerenciador de serviços envia a tabela de registros ao grupo para concluir a colaboração.

#### Segurança de Interação
- **Validação da origem dos comandos**: responde apenas a comandos diretos de administradores na whitelist do grupo.
- **Confirmação via cartões do Feishu**: operações de alto risco como alteração de configurações, escrita em banco de dados ou reinicialização enviam cartões com botões "Aprovar" e "Rejeitar", **permitindo autorização secundária com um clique dentro do Feishu**.

### Critérios de Qualidade e Sucesso

- **Latência ponta a ponta inferior a 1 segundo**: o envio de mensagens tem resposta praticamente instantânea.
- **Roteamento preciso de mensagens no chat em grupo**: silêncio em conversas casuais; respondendo apenas a quem for diretamente mencionado (@); e menções a todos relatam conforme as atribuições de cada um, sem respostas sobrepostas.
- **Alta disponibilidade e autorrecuperação**: reinicia em até 5 segundos após encerramento, realiza verificações de travamento a cada 5 minutos e se recupera em cerca de 9 segundos se o processo for finalizado abruptamente.

Para a prática, consulte o [Tutorial Completo de Integração de Equipe do Grok Bot ao Feishu (com modelo de gerenciador Feishu)](https://jcng5q8n0f3z.feishu.cn/wiki/F2VXw4hVbirRUjk5QgFcWS0jnJg).

## Integração Pessoal ao WeChat: Conexão Direta com o Plugin WeChat ClawBot

![Integração Pessoal ao WeChat: Conexão Direta com o Plugin WeChat ClawBot](/info/22-feishu-wechat-s3.png)

Utiliza a interface oficial iLink (`ilinkai.weixin.qq.com`), com long polling puramente de saída, **sem portas públicas abertas, em total conformidade e sem risco de banimento de conta**.

### Três Passos para Concluir a Integração

1. **Envie o prompt**: envie o comando abaixo para o bot principal no computador e aguarde a geração automática dos componentes de comunicação.
::: details Três passos para concluir a integração
```text
我想把你接到我的微信上，让我能在微信里直接给你发消息、收到你的回复。请按下面的思路做，每做完一步告诉我结果，需要我操作的地方停下来等我。

1、先调研方案：腾讯「微信ClawBot」插件用的是 iLink 接口（ilinkai.weixin.qq.com）。请确认怎么用 getupdates 长轮询收消息、怎么用 sendmessage 回消息。整个程序只走出站请求，不要开公网端口。

2、在 Grok Bot 里建一个由 webhook 触发的 routine，名字可以叫「微信下旨入口」。建好后告诉我去 routine 面板复制 Webhook URL 和 key，然后弹出加密弹框让我填进去，不要让我在聊天里发明文。

3、在你的云端电脑上写一个小转发程序：收到微信消息后 POST 给这个 routine；你处理完以后，用一个 reply 脚本把回复发回微信，同时在我们的主聊天里同步一份。

4、等我在手机微信里启用 ClawBot 插件以后，生成二维码让我用手机扫码确认，同时给我一个可以在微信里直接打开的备用链接。二维码大约 5 分钟有效。

5、绑定成功后，提醒我先在 ClawBot 对话里发一句话，因为回复要用到这条消息带的 context_token。

6、规则：只认绑定的这一个人，别人的消息不处理；回复一律用纯文本，不要用 Markdown，因为微信不渲染 Markdown。

7、最后告诉我：云端电脑重启以后，怎么把转发程序重新拉起来；如果遇到错误码 -14（凭证过期），提醒我重新扫码。
```
:::
2. **Configuração de chaves**: abra a rotina "Entrada de Comandos do WeChat" do bot principal, copie o endereço **POST to** e a **key** do Webhook e envie-os na caixa criptografada.
3. **Vinculação e ativação**:
   - A versão do WeChat deve atender a **iOS ≥ 8.0.70, Android ≥ 8.0.69**; em "Configurações > Plugins", ative o "WeChat ClawBot".
   - Envie "Plugin ativado" para o bot no computador e escaneie o código QR com o WeChat para autorizar (o QR code é válido por 5 minutos).
   - **Você deve enviar proativamente uma primeira mensagem para o WeChat ClawBot** (como "olá") para obter o `context_token` e ativar as respostas.

### Critérios de Aceitação

- **Sincronização bidirecional**: respostas em segundos no WeChat e arquivamento em tempo real no computador.
- **Orquestração de subagentes**: despache tarefas de busca no Twitter e transcrição de vídeo diretamente pelo WeChat.
- **Isolamento de segurança**: contas do WeChat não vinculadas não conseguem despertar o bot.

Para mais detalhes, consulte [Como integrar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes (com prompts detalhados) | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg).

## Catalogação de Conteúdo do WeChat: Atalhos Conectando Histórico de Chat e Multimídia

Envie pacotes ZIP mesclados e encaminhados para uma nuvem temporária por meio de Atalhos, **e depois encaminhe-os para o Webhook do Grok Bot para arquivamento automático**.

### Configuração e Operação

1. Na janela de conversa do Grok Bot, envie o prompt para criar a rotina:
```text
帮我创建一个 Webhook 触发的例行任务。快捷指令会用 POST 请求发来一个 JSON，里面只有一个字段 info。info 可能是我输入的文字，也可能是一个文件下载链接，比如微信聊天记录压缩包、截图、录音。收到后：如果是链接就先下载文件再读取，压缩包先解压；然后整理出要点，收录进知识库，最后给我一份回执，写清楚收录了什么、存在哪里。
```
Na lista de Routine na página de detalhes, **copie o endereço POST to e a chave secreta key do Webhook**.

2. Importe o Atalho: `https://www.icloud.com/shortcuts/2b77155d7c744110a0f0f9ef1bdc42bf`.

3. Preencha o POST to, a key e o ID do serviço de hospedagem. Os arquivos no `filebin.net` ficam salvos por 7 dias; **o ID deve ter 8 ou mais caracteres aleatórios** (como `kb7x9q2m`) para evitar sobregravação e vazamentos; **certifique-se de limpar esses três itens antes de compartilhar**.

4. No WeChat, selecione múltiplas mensagens do histórico de conversa, escolha o encaminhamento combinado para outros aplicativos e selecione "Receber encaminhamento" no Atalho "Enviar para o bot da base de conhecimento". Quando nenhum encaminhamento for recebido, ele lerá a área de transferência; você também pode selecionar "Captura de tela" ou "Gravação de áudio" para envio direto.

### Critérios de Aceitação

- **Processamento multimídia completo**: descompacta e categoriza imagens, documentos e áudios (por exemplo, 13 sites de inspiração de design indexados por site completo, aplicativo e componentes).
- **Recibo padronizado**: identifica claramente os pontos principais do tópico, o caminho de armazenamento da nota e o caminho de arquivamento do ZIP original.

Referência: [Conectando o Histórico de Conversas do WeChat ao Grok Bot: Versão Avançada de Atalhos](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb).

## Problemas Comuns e Soluções de Diagnóstico

### 1. Falha no Recebimento de Mensagens de Grupo Devido a Permissões Insuficientes no Feishu

- **Problema**: As conversas individuais funcionam normalmente, mas menções com `@` no grupo não respondem e não geram logs, pois na seleção inicial de 7 permissões faltou a de "Obter todas as mensagens com @menção ao bot em grupos".
- **Solução**: Gere o link de concessão de permissões adicionais escaneando o QR code pelo SDK; o administrador confirma a expansão para 14 permissões, **sem necessidade de lançar uma nova versão**.

### 2. Julgamento Incorreto nas Regras de Filtragem do Chat em Grupo do Feishu e Reenvio após Queda de Conexão Persistente

1. Mensagens perdidas e respostas concorrentes: no Feishu, `@所有人` não fica no array de menções; sem validação de ID, todos os bots tentarão responder simultaneamente. **O script deve filtrar rigorosamente o ID de destino, respondendo apenas a "`@自己`" ou "`@所有人`"**.
2. Respostas duplicadas: após o restabelecimento da rede, a plataforma reenvia os eventos pendentes automaticamente; **nunca faça reenvios manuais secundários**.

### 3. Falta de Cadeia de Confiança e Cartões de Autorização em Chamadas entre Bots

1. Se as chamadas mútuas entre bots no grupo não responderem, é porque **mensagens entre bots não são confiáveis por padrão**, ficando travadas aguardando confirmação no chat privado.
2. Configure uma whitelist na camada de encaminhamento para reconhecer o Open ID do administrador; operações de alto risco devem enviar **cartões do Feishu com botões de aprovar/rejeitar** para confirmação.

### 4. Caminho Incorreto do Ambiente Python na Máquina Virtual

- Se o script apresentar erro informando que `lark-oapi` não foi encontrado, geralmente é porque o daemon foi configurado **usando erroneamente o `/usr/bin/python3` padrão do sistema**.
- Nos scripts de inicialização, no Supervisor e nos cron jobs, **você deve fixar o caminho absoluto do ambiente virtual** (como `/home/user/venv/bin/python3`), evitando chamar diretamente o ambiente global do sistema.

### 5. Expiração do Código QR do WeChat ClawBot e Código de Erro -14

- O código QR **tem apenas 5 minutos de validade** e expirará após esse prazo; escaneie-o imediatamente com o celular assim que for gerado.
- Quando o backend relata o código de erro **`-14`**, significa que as credenciais expiraram; basta gerar um novo código QR e pedir para o administrador escanear novamente.

### 6. Formatação de Mensagens Desconfigurada no WeChat e Falha na Renderização de Markdown

- O WeChat **não renderiza Markdown**; asteriscos, crases e marcadores de título serão exibidos diretamente como texto bruto.
- Adicione uma filtragem no prompt de integração ou no script de encaminhamento para **converter tudo de forma padronizada em texto simples com quebras de linha** antes de enviar para o WeChat.

### 7. Pacote ZIP de Encaminhamento Combinado do WeChat sem Anexos Multimídia Não Carregados

O WeChat não armazena arquivos originais permanentemente; itens não abertos e carregados previamente não serão incluídos no arquivo compactado, resultando na perda de imagens ao descompactar.

1. Antes de encaminhar, **abra individualmente cada imagem e arquivo que deseja salvar**.
2. Aguarde o carregamento completo localmente antes de compactar e encaminhar.

### 8. Conflito de Nomes em Nuvens Temporárias e Riscos de Vazamento de Privacidade

O `filebin.net` não possui sistema de contas; se o ID for muito simples, haverá colisões de nomes, causando erros ou o download de arquivos de outras pessoas. Ao utilizá-lo, fique atento a:

- O ID do repositório **deve ser configurado com uma sequência aleatória de 8 ou mais caracteres**.
- Não envie senhas, documentos de identidade ou outros conteúdos confidenciais.
- Antes de compartilhar o Atalho, **remova seu ID exclusivo e a chave secreta do Webhook**.

### 9. Controle de Consumo de Cota sob a Assinatura Unificada The X Subscription

Conversas casuais dos membros do grupo acionam execuções ociosas da rotina, **esgotando a cota semanal em um ou dois dias e fazendo o bot parar de responder**.

A partir de 12 de outubro de 2026, o The X Subscription deduz cotas semanalmente de um pool compartilhado.

O plano Plus ($8/mês) não inclui o Grok Bot; ele está presente apenas no Premium ($30/mês, 4x de cota), Super ($100/mês, 15x de cota) e Ultra ($200/mês, 50x de cota).

O controle de consumo concentra-se em dois pontos:
1. **Acione o Webhook apenas em menções diretas (`@自己`) ou comandos específicos de administradores**.
2. É terminantemente proibido o monitoramento indiscriminado de todo o grupo; evite configurar sondagens de alta frequência e ciclos curtos.

Para regras detalhadas, consulte [Planos e Preços](https://cursor.com/cn/help/grok-bot/plans.md) e [Rotinas](https://cursor.com/cn/help/grok-bot/routines.md).

## Análise de Casos Reais

### Colaboração com Múltiplos Bots no Feishu (铁柱AGI)
É possível executar a colaboração sem IP público; **o segredo é usar conexões persistentes de saída para dispensar o redirecionamento de portas**.
1. **Registro em lote**: autorização via QR code pelo Python SDK do Feishu; o bot gerenciador lê a tabela de backup do Git e gerencia as chaves e Webhooks dos três bots: editor-chefe, contabilidade e máquina virtual.
2. **Confirmação de segurança**: responde no grupo apenas a `@自己` ou `@所有人`. **Operações de alta sensibilidade exigem que o bot envie cartões com botões para autorização humana**.

### Painel Portátil WeChat ClawBot (Kin)
Agende bots de operações do Twitter e extração de copywriting diretamente pelo WeChat; **usar o long polling do plugin oficial evita o banimento de contas**.
1. Envie o prompt para o computador na nuvem 24/7, acionando o Tencent iLink (`ilinkai.weixin.qq.com`) para executar o polling `getupdates` e o script `sendmessage`.
2. Envie o Webhook e a chave secreta pela janela popup, escaneie o QR code e envie a primeira mensagem para obter o `context_token` inicial.
3. **Ponto de atenção**: **as respostas do WeChat devem ser convertidas obrigatoriamente para texto simples**, removendo toda a formatação Markdown.

### Pipeline de Catalogação de Conteúdo Multimídia do WeChat
O sandbox do WeChat impede o envio direto de pacotes completos; **usar uma nuvem temporária como intermediária permite contornar essa restrição**.
1. **Upload intermediário**: no Mac ou iPhone, use o "Encaminhamento Combinado" para exportar o pacote ZIP do chat, e o Atalho fará o upload automático para o `filebin.net`.
2. **Arquivamento automático**: o Atalho monta o JSON e o envia para o Webhook do Grok Bot, descompactando e arquivando imagens e textos como os "13 sites de inspiração de design".
3. **Critérios de aceitação**: **deve gerar um recibo estruturado contendo o caminho e o resumo**.

## Como Homologar após a Conclusão

### Feishu
1. **Resposta a mensagens**: resposta em até 1 segundo no chat privado; mensagens de texto comuns no chat em grupo permanecem em silêncio, respondendo individualmente a `@文章主编`, enquanto com `@所有人` cada bot relata em sequência.
2. **Permissões e autorrecuperação**: ative todas as 14 permissões de eventos no console e certifique-se de que a autorização por cartões funciona; finalize o processo manualmente e verifique se ele reinicia automaticamente entre 5 e 10 segundos.

### WeChat
1. **Ambiente e handshake**: WeChat em versão superior a iOS 8.0.70 ou Android 8.0.69 com o plugin ativado; escaneie o código QR e certifique-se de que a primeira mensagem responda usando `context_token` sem caracteres Markdown corrompidos.
2. **Interceptação e erros**: contas não vinculadas são ignoradas diretamente; reinicia automaticamente após reboot e **exibe aviso para escanear novamente caso ocorra o código de erro `-14`**.

### Atalhos
1. **Operação de catalogação**: preencha o Webhook, a chave Bearer e o ID do serviço de hospedagem com mais de 8 caracteres; no WeChat, abra e carregue previamente os anexos antes do encaminhamento combinado; o fluxo também pode ser acionado de forma independente.
2. **Saída e conciliação**: **o recibo deve conter o resumo, o caminho da nota e o caminho de retenção do arquivo**; verifique o consumo na página de planos para evitar cobranças por processamento ocioso contínuo.

## Leitura Adicional

- [Como Usar o Grok Bot](https://cursor.com/cn/docs/grok-bot/work) (Guia oficial de fluxos de trabalho e habilidades do Grok Bot)
- [Guia de Uso de Rotinas](https://cursor.com/cn/help/grok-bot/routines) (Documentação oficial sobre configuração de rotinas, chamadas de Webhook e tarefas agendadas)
- [Planos e Preços](https://cursor.com/cn/help/grok-bot/plans) (Instruções de níveis de assinatura e uso do The X Subscription)
- [Gerenciamento de Segredos e Chaves](https://cursor.com/cn/help/grok-bot/secrets) (Mecanismos de variáveis de ambiente seguras e caixas de diálogo criptografadas)
- [Tutorial Completo de Integração de Equipe do Grok Bot ao Feishu (com modelo de gerenciador Feishu)](https://jcng5q8n0f3z.feishu.cn/wiki/F2VXw4hVbirRUjk5QgFcWS0jnJg) (Artigo original do autor da comunidade 铁柱AGI)
- [Como integrar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes (com prompts detalhados) | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg) (Artigo original do autor da comunidade Kin)
- [Conectando o Histórico de Conversas do WeChat ao Grok Bot: Versão Avançada de Atalhos](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb) (Artigo original do autor da comunidade 铁柱AGI)
