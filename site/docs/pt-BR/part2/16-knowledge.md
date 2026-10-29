# Capítulo 16 Estudo de caso: Ingestão automática de conhecimento e integração com o WeChat

Favoritos no celular viram uma bagunça facilmente, arquivos de grupos expiram toda hora e, quando você está fora, fica difícil aproveitar o Grok Bot rodando na nuvem **24/7**.

1. Páginas web e vídeos curtos: use Webhook com os Atalhos do iOS para **ingestão estruturada com um clique**.
2. Capturas de tela e gravações de áudio: o encaminhamento do WeChat não transfere anexos, então **use um trânsito temporário pela internet pública** para exportá-los.
3. Controle de conversas: use o plugin oficial "WeChat ClawBot" via long polling para **controlar o Grok Bot diretamente na janela do WeChat**.

## Comparação de capacidades e limites das três soluções de automação

![Comparação de capacidades e limites das três soluções de automação](/info/16-knowledge-s1.png)

| Solução e cenário | Mecanismo e autenticação | Armadilhas |
| :--- | :--- | :--- |
| Ingestão unidirecional (páginas web, contas oficiais e vídeos curtos) | Atalhos enviam POST com token Bearer para o Webhook para ingestão | Apenas recepção unidirecional |
| Ingestão multimodal (histórico do WeChat, gravações, capturas de tela e múltiplas imagens) | Texto direto; arquivos usam o armazenamento temporário filebin.net para gerar links públicos, e o Bot descompacta para ingestão | **O armazenamento em nuvem não tem senha, não envie conteúdo confidencial**; pacotes grandes com extração de quadros consomem muitos tokens |
| WeChat bidirecional (enviar comandos, consultar materiais, controlar o Bot) | Vinculação via QR Code no WeChat, iLink com script na nuvem monitorando e convertendo para Webhook retornando texto puro | **É necessário controlar a frequência para evitar consumo ocioso** |

A partir de 12/10/2026, tudo foi unificado como The X Subscription, com deduções por uso na cota semanal.

**O plano Plus de US$ 8/mês não inclui o Grok Bot**; é necessário escolher Premium (US$ 30/mês ou US$ 300/ano, 4x a cota), Super (US$ 100/mês ou US$ 1000/ano, 15x a cota) ou Ultra (US$ 200/mês ou US$ 2000/ano, 50x a cota).

Para mais detalhes, consulte os [Planos e preços](https://cursor.com/cn/help/grok-bot/plans) oficiais.

## Caso 1: Criação de um pipeline de ingestão automática de conhecimento com Webhook e Atalhos

![Caso 1: Criação de um pipeline de ingestão automática de conhecimento com Webhook e Atalhos](/info/16-knowledge-s2.png)

**A solução coloca a captura, transcrição de áudio e vídeo e resumo totalmente na nuvem do Grok Bot; o celular só envia a URL para disparar.

** 铁柱AGI（@cgnot996）utilizou o Webhook de [Rotinas](https://cursor.com/cn/help/grok-bot/routines) para conseguir o disparo imediato ao enviar a requisição.

### Passos de configuração
1. No cliente para desktop, acesse Details e localize Routines. Peça ao Bot para criar uma tarefa de análise e **salve com cuidado a Webhook URL e a key geradas**.
2. Crie um novo atalho chamado "Enviar para o Bot da base de conhecimento", adicione "Obter conteúdo do URL" e configure os parâmetros conforme a tabela.

| Parâmetro | Valor de configuração |
|---|---|
| URL | Endereço do Webhook |
| Método | POST |
| Cabeçalho | Chave `Authorization`, valor `Bearer <key>` |
| Corpo da requisição | Selecione JSON, adicione "Entrada do Atalho" |

3. **Adicione uma caixa de entrada auxiliar para aplicativos fechados**. O WeChat frequentemente desativa o painel de compartilhamento, por isso é necessário criar um segundo atalho ("Escolher no Menu" com "Solicitar Texto") como intermediário, vinculado ao Botão de Ação do iPhone para colar e enviar com um único toque.

### Critérios de validação
> Fonte: [Grok Bot Webhook + Atalhos: Criação de um pipeline de ingestão automática de conhecimento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Atalhos: Criação de um pipeline de ingestão automática de conhecimento](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Atalhos: Criação de um pipeline de ingestão automática de conhecimento](/cases-img/fs06-1.jpg)
Após clicar em compartilhar, **o status no desktop mudará para Em execução em poucos segundos**. Quando a tarefa for concluída, a base de conhecimento gerará automaticamente uma entrada padronizada com:
- ID do vídeo ou link curto original da página web
- Caminho de armazenamento na nuvem e página de conhecimento vinculada
- Principais pontos resumidos e tags do autor
- Custo de créditos consumidos por análise individual

Ao catalogar artigos longos como "2026: Meu compartilhamento completo sobre o Obsidian", ele consegue criar backlinks automaticamente.

Para a demonstração prática, veja ["Grok Bot Webhook + Atalhos: Criação de um pipeline de ingestão automática de conhecimento"](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh).

## Caso 2: Integração e ingestão de histórico de conversas do WeChat e materiais multimodais

### Visão geral do caso
- Encaminhamento combinado do WeChat empacotado e enviado ao Grok Bot, que descompacta automaticamente e emite um comprovante.
- **Uso do filebin.net como ponte** para eliminar a dependência de caminhos locais.
- Atalhos com **cinco modos de captura** implantados no Mac e iPhone.

### O que é: por que é necessário introduzir um trânsito por armazenamento temporário

Entre dispositivos diferentes não é possível ler o disco local, e colocar arquivos ZIP grandes do WeChat no corpo da requisição frequentemente causa timeout.

1. O texto é enviado diretamente via JSON.
2. Imagens, gravações de áudio e arquivos ZIP são enviados primeiro ao filebin.net, e depois o link é enviado para o Bot baixar.
3. O ID do repositório deve ter **pelo menos 8 caracteres alfanuméricos aleatórios** para evitar vazamentos por colisão de nomes.
4. Os arquivos ficam armazenados por padrão durante 7 dias e não são criptografados; **é estritamente proibido enviar dados privados e segredos comerciais**.

### Como fazer: passo a passo de configuração

#### 1. Configurar o Webhook
Envie este prompt na conversa principal do cliente desktop:

```text
帮我创建一个 Webhook 触发的例行任务。快捷指令会用 POST 请求发来一个 JSON，里面只有一个字段 info。info 可能是我输入的文字，也可能是一个文件下载链接，比如微信聊天记录压缩包、截图、录音。收到后：如果是链接就先下载文件再读取，压缩包先解压；然后整理出要点，收录进知识库，最后给我一份回执，写清楚收录了什么、存在哪里。
```

**Após o envio, anote a Webhook URL e a key em "Rotinas" do Bot.**

#### 2. Configurar o Atalho
Link de importação: `https://www.icloud.com/shortcuts/2b77155d7c744110a0f0f9ef1bdc42bf`
Edite "[Versão de Compartilhamento] Enviar para o Bot da base de conhecimento", preencha a URL, a key e um **ID de repositório complexo com pelo menos 8 dígitos** (como kb7x9m2q); os cabeçalhos são integrados e não precisam de alteração.

#### 3. Captura de conversas do WeChat
- **No Mac**: faça o encaminhamento combinado para outros aplicativos, selecione esse atalho e clique em receber encaminhamento; o ZIP é enviado para a nuvem temporária com o link disparado, e o Bot processa em seguida.
- **No celular**: faça o encaminhamento combinado, selecione o atalho e toque em receber encaminhamento; é possível fixá-lo na área de ações frequentes em "Editar Ações".

#### 4. Chamada independente e coleta
No Mac, use o Raycast ou a barra de menus; no celular, vincule ao Botão de Ação.
- Captura de tela/Gravação: confirme ou termine de gravar para enviar ao armazenamento temporário e enviar o link.
- Digitar texto: **envie diretamente no JSON**, sem passar pelo armazenamento temporário.
- Selecionar imagens adicionais: selecione as imagens, insira uma descrição e envie o pacote.
- Receber encaminhamento: quando nenhum conteúdo for recebido, lê a área de transferência e envia.

### O que esperar de um resultado satisfatório

> Fonte: [Integração do histórico de conversas do WeChat com o Grok Bot: Versão avançada de Atalhos](https://x.com/cgnot996/status/2107039351519707602)  
> Autor: [铁柱AGI @cgnot996](https://x.com/cgnot996)

![Integração do histórico de conversas do WeChat com o Grok Bot: Versão avançada de Atalhos](/cases-img/fs11-0.png)

![Integração do histórico de conversas do WeChat com o Grok Bot: Versão avançada de Atalhos](/cases-img/fs11-1.jpg)

Após o envio, aguarde de alguns segundos a cerca de dez segundos, e o Bot retornará um **comprovante padronizado**:
- **Arquivamento de conversas em grupo**: extrai os principais argumentos da discussão e fornece os caminhos das notas e do arquivo compactado.
- **Catalogação de recursos**: envie 13 sites e ele classificará e indexará automaticamente, fornecendo os links da base de conhecimento.

Para instruções de operação, consulte ["Integração do histórico de conversas do WeChat com o Grok Bot: Versão avançada de Atalhos"](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb).

## Caso 3: Conectar o Grok Bot diretamente ao WeChat para controle bidirecional

![Caso 3: Conectar o Grok Bot diretamente ao WeChat para controle bidirecional](/info/16-knowledge-s4.png)

### Visão geral do caso
Kin conectou o Grok Bot ao WeChat: **basta enviar uma mensagem pelo celular para controlar remotamente o Bot na nuvem**.

1. Pedir ao Grok para usar a iLink e escrever um script de long polling
2. Criar um Webhook para receber comandos
3. Ativar o "WeChat ClawBot" no WeChat e escanear o QR Code para vincular

Funciona exclusivamente com long polling de saída, **sem necessidade de abrir portas na internet pública**.

### O que é: o mecanismo de long polling do WeChat ClawBot e iLink

A solução utiliza o plugin oficial "WeChat ClawBot" e a interface iLink (`ilinkai.weixin.qq.com`), sem modificar a memória do cliente, **sem risco de banimento da conta**.

Toda a comunicação consiste em requisições de saída, **sem necessidade de abrir portas na internet pública**:
1. O Grok Bot executa em segundo plano chamando `getupdates` para buscar mensagens por polling e, após o processamento, chama `sendmessage` para responder.
2. O Webhook recebe o texto e o repassa para Bots especializados colaborarem na execução; para detalhes, consulte a documentação [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

### Como fazer: passo a passo prático e prompt completo

1. Envie o prompt na conversa principal do computador e aguarde a criação da rotina "Entrada de Comandos do WeChat".
::: details Como fazer: passo a passo prático e prompt completo
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
2. Copie a URL e a key da rotina. **É estritamente proibido enviar em texto simples na conversa**; preencha o cartão de segredos até exibir "Salvo com segurança e mantido em sigilo", consulte [Armazenamento seguro de informações confidenciais](https://cursor.com/cn/help/grok-bot/secrets).
3. A versão do WeChat deve ser superior a **iOS 8.0.70 / Android 8.0.69**. Em "Eu" -> "Configurações" -> "Plugins", ative o ícone da lagosta vermelha "WeChat ClawBot".
4. Envie "O plugin já está ativo", e escaneie o QR Code no WeChat para autorizar (o QR Code é **válido por 5 minutos**; se expirar, use o link alternativo).
5. **É obrigatório enviar ativamente a primeira mensagem no WeChat** (como "Olá"). A interface precisa disso para capturar o `context_token` e estabelecer a conexão; após o envio, o canal estará pronto para uso.

### O que esperar de um resultado satisfatório

> Fonte: [Como conectar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes chegou (com prompts detalhados)](https://x.com/KinGao476942/status/2108132811635032316)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![Como conectar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes chegou (com prompts detalhados)](/cases-img/fs29-0.jpg)

![Como conectar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes chegou (com prompts detalhados)](/cases-img/fs29-1.jpg)

Teste estes quatro pontos no WeChat para verificar **se o fluxo está funcionando**:
1. Envie "Olá" e receba uma **confirmação em texto puro instantaneamente**.
2. Chame o Bot especialista em Twitter e receba uma lista de temas diretamente no WeChat.
3. Envie o link de um vídeo para acionar o Bot especialista em download e receba de volta o texto limpo.
4. Verifique e sincronize todos os comandos e registros no cliente desktop.

Para a prática e capturas de tela, veja ["Como conectar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes chegou (com prompts detalhados) | Kin"](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg).

## Armadilhas comuns

1. Antes de encaminhar, **é obrigatório clicar localmente para baixar os anexos**; caso contrário, o ZIP exportado conterá apenas textos de marcação de posição.
2. O filebin.net não tem senha, então não use `test` ou `123456`; **é necessário definir uma sequência aleatória de mais de 8 caracteres**, sendo proibido o envio de documentos de identidade, cartões bancários e contratos confidenciais.
3. Ao configurar o Webhook, não cole a key na conversa, **salve-a usando o cartão seguro**; antes de compartilhar o atalho, limpe sua key e URL pessoais.
4. O QR Code do ClawBot expira em 5 minutos; a falta de resposta ou o erro `-14` indica que as **credenciais expiraram e é necessário gerar novamente para escanear**.
5. Após um Reset ou reinicialização do computador na nuvem, o polling em Python cairá; se não houver resposta no WeChat, acesse o cliente desktop e **peça ao Bot para reiniciar o script**.
6. O WeChat não renderiza Markdown, portanto **force respostas em texto puro nas Instruction**, evitando a saída de `**` ou `#`.
7. **Não execute múltiplos listeners do OpenClaw simultaneamente**, para evitar que a fila do iLink dispute mensagens e perca comandos.
8. O The X Subscription deduz da cota semanal; **disparos de alta frequência precisam ter filtros**, e se o consumo for rápido demais, pause rotinas desnecessárias ou flexibilize as condições.

## Como validar após a conclusão

1. **Testar o Webhook**: envie uma requisição POST com `Authorization: Bearer <key>`. **Retornar 200 significa sucesso**; 401 indica chave incorreta e 404 indica URL incorreta. Basta o status de "Rotinas" no computador mudar para Running… e exibir logs.
2. **Testar o Atalho**: envie texto e verifique se o comprovante é gerado em dezenas de segundos; encaminhe 2 imagens para testar o arquivamento. Capturas de tela devem exibir a pré-visualização de permissão e só ser enviadas após clicar em permitir.
3. **Testar o WeChat e a sincronização**: envie uma mensagem para o "WeChat ClawBot"; **receber uma resposta em até 5 segundos** significa sucesso. Depois, confira no computador: se o histórico do chat estiver sincronizado, o fluxo estará completamente funcional.

## Leituras complementares

### Documentação oficial
- [Rotinas](https://cursor.com/cn/help/grok-bot/routines)
- [Armazenamento seguro de informações confidenciais](https://cursor.com/cn/help/grok-bot/secrets)
- [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- [Planos e preços](https://cursor.com/cn/help/grok-bot/plans)

### Artigos práticos da comunidade
- ["Grok Bot Webhook + Atalhos: Criação de um pipeline de ingestão automática de conhecimento"](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- ["Integração do histórico de conversas do WeChat com o Grok Bot: Versão avançada de Atalhos"](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb)
- ["Como conectar o Grok Bot ao seu WeChat? O guia definitivo para iniciantes chegou (com prompts detalhados) | Kin"](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)
