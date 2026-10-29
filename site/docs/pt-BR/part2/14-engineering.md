# Capítulo 14 Casos de Uso: Equipes de Engenharia e P&D

Não fique monitorando localmente; **delegue o trabalho para a nuvem**.

- Desligue o computador a qualquer momento enquanto tudo roda 24 horas por dia, evitando ter que acordar às duas da manhã para checar a CI.
- Codificação em ambiente isolado, pull requests acompanhados de evidências e logs reais, evitando que asserções sejam adulteradas apenas para passar os testes.

Pela manhã, **analise o relatório de entrega e valide o lançamento**.

## Arquitetura Central: Divisão de Tarefas entre Harness, Cérebro do Modelo e CLI Agent Local

![Arquitetura Central: Divisão de Tarefas entre Harness, Cérebro do Modelo e CLI Agent Local](/info/14-engineering-s1.png)

### Definição de Papéis e Divisão Tripartite
Em 7 de outubro de 2026, a plataforma introduziu modelos como o Claude Opus 5.5 para inferência. **O sistema agenda os modelos automaticamente e não oferece um seletor manual por execução**. Não dependa das particularidades de um único modelo; o fluxo de trabalho deve ser rigorosamente controlado por arquivos de estado e validações automatizadas.

| Papel | Host de Execução | Permissões e Responsabilidades |
| :--- | :--- | :--- |
| Grok Bot | Computador em nuvem (armazenamento compartilhado `/workspace`) | Executa inspeções e despacha tarefas; **gera apenas Draft PRs, sendo estritamente proibido fazer push direto para a branch padrão ou publicar em produção** |
| CLI Agent Local | Terminal local ou contêiner temporário | Baixa dependências, altera código em branch isolada e executa builds |
| Supervisor Humano | Estação de trabalho pessoal | **Detém as chaves de deploy e permissões de escrita em produção**, responsável por decisões de arquitetura e aprovação de merges |

### Configuração de Ambiente e Isolamento de Segurança
Todos os Bots sob a mesma conta compartilham o mesmo computador em nuvem, credenciais de linha de comando e sessões de navegador; **renomear um Bot não fornece isolamento de permissões**. Ao lidar com logins sensíveis, não cole textos em texto simples na caixa de diálogo; **é obrigatório usar o Take Control para autenticação manual na tela remota**, mantendo a sessão salva no navegador.

### Autoinspeção e Persistência do Ambiente de Execução
Antes de integrar um novo repositório, execute comandos de autoinspeção no Grok Bot para entender a configuração.

::: details Autoinspeção e persistência do ambiente de execução
```bash
echo "CPU 核心数:"
nproc

echo "内存分配:"
free -h

echo "工作区磁盘空间:"
df -h /workspace

echo "系统版本与 Git:"
cat /etc/os-release | head -n 3
git --version
```
:::

Durante atualizações, as dependências do sistema podem ser redefinidas; apenas o diretório `/workspace` é persistido. **Todos os estados essenciais devem ser sincronizados remotamente via Git ou salvos em arquivos estruturados**.

A documentação de referência inclui o [Guia Oficial de Uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/work) e a [Documentação de Conexão com Computador em Nuvem e Aplicativos](https://cursor.com/cn/docs/grok-bot/computers).

## Caso 1: Inspeção de PRs e Orquestração Multi-Bot da Equipe SpaceXAI

Lingxi Li (@lingxi), da SpaceXAI, lidera 5 Bots de P&D mais 1 Bot de fluxo de trabalho, operando 24 horas por dia com o Cursor cloud agent.

@poteto, na mesma equipe, fez o merge de mais de 2.000 PRs em um único mês, e o próprio Lingxi levou apenas 3 semanas para concluir a versão v0 do iOS.

Os 5 Bots de P&D têm seus contextos isolados, cada um cuidando de uma parte do código e executando comandos correspondentes de acordo com a tarefa:
- Baltata é responsável pelo iOS e pela camada compartilhada mobile; Craig é responsável pelo Android.
- Shaoruru cuida do desktop e de CI/CD; Quill mantém a toolchain do Harness.
- Hogan foca em infraestrutura básica e bugs sem atribuição definida.
- O aspecto visual segue `/lingxi-design`, a qualidade de código segue `/react-native-best-practices` e a arquitetura segue `/lingxi-review`.

O Bot supervisor Jenny não escreve código; todos os dias, às 5h da manhã, ele alinha os manuais um a um. **Se algum Bot de P&D relaxar na revisão ou entregar sem validação completa, Jenny o flagra para fazer uma RCA e atualizar as regras**.

Sessões longas tendem a estourar o limite de contexto, por isso a equipe armazena os estados em uma base de dados do Notion, fechando o ciclo por meio de polling periódico:
1. **Polling a cada meia hora**: a cada 30 minutos, varre os PRs abertos, verificando os resultados do Bugbot, erros de CI e conflitos do Git.

   Se houver problemas, aciona o Cursor para corrigir e retorna ao status Working; quando tudo estiver verde, muda para Ready for Review; o merge automático só ocorre quando a confiança é extremamente alta e o impacto da alteração é mínimo. **O volume de agendamento concorrente por pessoa aumentou de 15 para mais de 200**.
2. **Alinhamento com capturas de tela em dispositivos reais**: asserções de código costumam deixar passar falhas visuais de exibição; a equipe usa um Mac mini ocioso como worker privado para rodar o iOS Simulator, **comparando capturas de tela reais de antes e depois via visão multimodal**; se o visual estiver incorreto, é rejeitado imediatamente.
3. **Auditoria noturna às 3h da manhã**: limpa código morto para reduzir o tamanho do pacote, verifica segurança de dependências e tempo de execução da CI, completa a internacionalização, checa a paridade de recursos entre plataformas e resume os PRs das últimas 24 horas.

> Fonte: [Como engenheiros podem aproveitar bem o Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![Como engenheiros podem aproveitar bem o Grok Bot?](/cases-img/fs25-0.jpg)

![Como engenheiros podem aproveitar bem o Grok Bot?](/cases-img/fs25-1.jpg)

**Não deixe um único Bot carregar uma sessão longa**. Dividir os papéis por domínio de negócio, definir responsáveis para revisar regras e armazenar o estado em um kanban para conferência de diferenças poupa muitas dores de cabeça.

- ["Como engenheiros podem aproveitar bem o Grok Bot? | Kin"](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- ["Grok Bot for Engineering | Lingxi Li"](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## Caso 2: Decomposição do Trabalho de P&D e a Lista de 9 Categorias de Lauren

### Como Fazer na Prática
Lauren (@poteto) fez o merge de 2.500 PRs de produção em um único mês, e Jacob Gold (@jacobgold) alcançou uma média de quase 250 por dia; os dois dividiram a engenharia em nove frentes em paralelo.

| Nível de Risco | Escopo Típico e Regras | Método de Revisão |
| :--- | :--- | :--- |
| Baixo a médio | Limpeza de código morto, testes unitários e correções de tipos | Merge automático |
| Alto risco | Negócio principal, autenticação e migração de dados | Revisão humana obrigatória |

**Sempre que o diff ultrapassar a intenção do prompt original, o sistema encaminha imediatamente para decisão humana.**

### O que Podemos Aprender
Mai Yang (@MaiYangAI) gerou 1.020 commits no ContextEcho ao longo de seis meses, recorrendo a PRs apenas 18 vezes. **Em projetos solo, a superfície de impacto é mínima; forçar a criação de PRs sem uma necessidade real não tem nenhum valor.**

> Fonte: [Qual o sentido de centenas de PRs por dia? Segui a lista de 9 categorias da engenheira Lauren (@poteto) da SpaceXAI e dividi todo o meu trabalho](https://x.com/MaiYangAI/status/2108519046446727633)  
> Autor: [Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
Comece selecionando duas frentes: correção de bugs e refatoração de padronização, definindo restrições de entrada e critérios de aceitação. **Poupe a energia gasta revisando código a olho nu e concentre-se na definição de diretrizes, restrições de limites e testes.**

["Qual o sentido de centenas de PRs por dia? Segui a lista de 9 categorias da engenheira Lauren (@poteto) da SpaceXAI e dividi todo o meu trabalho"](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## Caso 3: Mesa de Operações de Repositório 24/7 (Repo Ops Desk)

![Caso 3: Mesa de Operações de Repositório 24/7 (Repo Ops Desk)](/info/14-engineering-s3.png)

### Quem Está Fazendo e o que Foi Feito
O desenvolvedor independente Gipp 🦅 (@gippp69), ao manter múltiplos projetos open source e repositórios de negócios, projetou uma mesa de operações de repositório 24/7. Na camada inferior, esse sistema combina sub-agents concorrentes para monitorar anomalias; na camada superior, implanta 6 papéis nomeados via Grok Bot para lidar com issues e erros de CI.

Segundo o autor, uma pessoa manualmente costuma conseguir acompanhar apenas de 2 a 3 repositórios. Já a mesa de operações automatizada consegue monitorar centenas de pontos de alteração simultaneamente em múltiplos repositórios.

### Como Fazer na Prática

::: details Como fazer na prática
```
[GitHub 事件 / CI 报警]
          │
          ▼
    ┌───────────┐
    │Triage Bot │ ── 识别严重度与类别
    └─────┬─────┘
          │
   ┌──────┴───────────────────────────┐
   ▼                                  ▼
[偶发测试 / 格式问题]             [业务逻辑缺陷 / CVE 安全问题]
   │                                  │
   ▼                                  ▼
┌─────────┐                      ┌─────────────────────────┐
│ Fix Bot │                      │ Dependency / Alert Bot  │
└────┬────┘                      └────────────┬────────────┘
     │                                        │
     ▼                                        ▼
[生成修复 Patch]                   [严重漏洞即时呼叫人类]
     │                                        │
     ▼                                        ▼
[提交 Draft PR (严禁合并)]           [其余汇总至次日晨报]
```
:::

1. **Implantar 6 Bots dedicados**
   - Triage Bot: categoriza issues por gravidade e tipo.
   - Fix Bot: assume bugs leves, escreve patches e abre Draft PRs.
   - Test Bot: executa testes para capturar testes intermitentes (flaky tests) e registra o contexto das falhas.
   - Dependency Bot: monitora vulnerabilidades CVE e dependências desatualizadas.
   - Release Bot: organiza o changelog conforme instruções e gera os pacotes.
   - Alert Bot: envia notificações imediatas quando é necessária intervenção humana.

2. **Bloquear permissões de acordo com a tabela de roteamento**

| Nível de Permissão | Escopo de Monitoramento | Papel e Ação |
| :--- | :--- | :--- |
| `auto-fix` | Testes flaky, erros de lint e formatação | Fix Bot submete patches |
| `triage` | Defeitos complexos e demandas não categorizadas | Triage Bot encaminha para humanos |
| `security` | Vulnerabilidades CVE de médio e alto risco | Dependency aciona o Alert assim que detectado |
| `release` | Mudanças de versão e notas de lançamento | Release Bot executa sob comando |

3. **Manter três linhas vermelhas rígidas**
   - Nunca tocar na lógica de negócios: as alterações de `auto-fix` são limitadas ao próprio arquivo de teste com falha ou a suas referências diretas, sendo estritamente proibido alterar o código central.
   - Nunca fazer merge automático: o Fix Bot apenas abre Draft PRs com a tag `auto-fix`, nunca realizando merge automático.
   - Teste gradual por uma semana: execute primeiro em um repositório secundário de baixo risco por uma semana para avaliar a taxa de adoção (quantidade de merges em comparação com descartes) antes de expandir para o repositório principal.

### O que Podemos Aprender

> Fonte: [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> Autor: [Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**A mesa de operações investiga erros na calada da noite, sem tomar decisões**. Com prompts e permissões travados em "apenas abrir Draft PRs e nunca modificar a lógica de negócios", o sistema opera com segurança mesmo sem supervisão humana.

Para o esquema detalhado de configuração, consulte ["How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) | Gipp 🦅"](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh).

## Caso 4: Harness de Engenharia Baseado em Máquina de Estados e Colaboração Multi-Bot

![Caso 4: Harness de Engenharia Baseado em Máquina de Estados e Colaboração Multi-Bot](/info/14-engineering-s4.png)

### Quem Está Fazendo e o que Foi Feito
Os desenvolvedores Mori (@0xjmori), Morlex (@0xMorlex) e o arquiteto de empresa unipessoal beamnxw criaram um pipeline padronizado de colaboração em P&D. Ao estabelecer um contrato de máquina de estados na nuvem, uma estrutura de diretórios unificada e um kanban de tarefas de seis campos, implementaram uma linha de correção de ponta a ponta onde 1 coordenador gerencia 4 especialistas.

Todo o sistema decompõe mudanças complexas de código em transições de estado acompanhadas de evidências verificáveis. Esse design garante que todas as passagens de bastão entre etapas sejam devidamente comprovadas.

### Como Fazer na Prática

1. **Criar uma estrutura organizada de diretórios no workspace**
Inicialize o projeto no computador em nuvem do Grok Bot em `/workspace`, direcionando cada issue para um diretório independente `/workspace/devdesk/issues/<issue-id>/`.

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**Cada diretório deve conter obrigatoriamente 6 arquivos padrão**:
- `task.md`: entrada original e critérios de aceitação de conclusão
- `status.json`: estado legível por máquina atual e responsável
- `evidence/`: armazena logs de falha, scripts de reprodução e capturas de tela
- `implementation.md`: lista de arquivos alterados e plano de implementação mínima
- `review.md`: conclusão da revisão independente
- `handoff.md`: relatório de liberação entregue ao humano

2. **Contrato de transição da máquina de estados**
**O pipeline avança estágio por estágio de acordo com os estados predefinidos, sendo estritamente proibido pular etapas**.

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage (`NEW` ──> `REPRODUCED`)**: deve fornecer etapas estáveis de reprodução e um caso de teste com falha funcional.
- **Builder (`BUILDING` ──> `TESTED`)**: despacha o Cursor agent para modificar o código em uma nova branch e garante que os testes de regressão originais passem.
- **Reviewer (`REVIEWING` ──> `REVIEW_PASSED`)**: analisa independentemente o diff e os logs para emitir uma avaliação. **Em caso de FAIL, retorna para `BUILDING` para retrabalho, com limite de até 2 tentativas**.
- **Release (`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`)**: após a aprovação de todos os itens de verificação, submete um Draft PR com comprovação completa aos engenheiros humanos.

3. **Classificação de reversibilidade das ações**
**O sistema define as permissões de aprovação com base na reversibilidade de cada ação**.

| Categoria da Operação | Política de Permissão | Comportamentos Abrangidos e Escopo |
| :--- | :--- | :--- |
| **Ações reversíveis** | Execução autônoma | Realizar análise de código, escrever patches e rodar testes unitários em branch local, gerar casos de teste com falha, abrir Draft PRs e gerar relatórios de log |
| **Ações irreversíveis** | Pausa para revisão humana | Fazer merge de código na branch padrão, realizar deploy em produção, modificar bancos de dados de produção, alterar variáveis de ambiente ou chaves, chamar serviços externos pagos |

4. **Kanban e consolidação de Skills**
Os campos do kanban são fixados como `Task | Owner | Source | Status | Deliverable | Next action`.
Os status das tarefas são estritamente limitados a cinco: `ready`, `working`, `blocked`, `awaiting approval` e `complete`.
**Assim que um tipo de tarefa for concluído com sucesso uma vez, execute o comando para consolidá-lo como uma Skill privada**, facilitando sua reutilização por rotinas agendadas.

### O que Podemos Aprender

> Fonte: [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> Autor: [Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

Não deixe múltiplos Agents conversando aleatoriamente em chats em grupo não estruturados.

1. **Se a etapa anterior não salvou evidências de teste, a próxima nunca é iniciada**. Trave o progresso usando diretórios em disco e máquinas de estado.
2. **Diferencie a reversibilidade das ações**, equilibrando a velocidade da automação enquanto protege o limite de segurança da produção.

Para práticas detalhadas, consulte ["Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps"](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf), ["Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps | Morlex"](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh) e ["Grok Bot Engineering: Set Up a Harness for Your One-Person Company | beamnxw ./"](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm).

## Pronto para Uso: Biblioteca de Prompts para Engenharia e P&D

Todos os prompts abaixo foram validados na prática em ambientes de produção. Copie e envie diretamente para o Bot, solicitando que ele memorize; para Bots compartilhados, insira no campo About dos detalhes:

### 1. Estatuto de Controle Geral de Arquitetura (Chief)
**Envie para o Bot supervisor e peça para ele memorizar** (para Bots compartilhados, insira no campo About dos detalhes), usado para controlar o fluxo e registrar os estados.

::: details 1. Estatuto de Controle Geral de Arquitetura (Chief)
```text
你是 Chief，负责管理 /workspace/devdesk 工作区内的 AI 工程团队。
你的职责是将每一个接到的 Issue 推进至可供人工复审的 Draft PR 状态。

工作原则：
1. 为每个处理阶段指派且仅指派一名专职 Bot。
2. 实时维护状态账本（status.json），防止任务重复分配。
3. 严格检查各阶段交付证据，绝不能仅凭下游 Bot 的口头回复判定任务完成。
4. 发生异常时记录阻塞点与失败尝试，连续失败两次立即终止重试。
5. 严禁亲自编写业务生产代码，严禁合并代码至默认分支，严禁触发生产部署。
```
:::

### 2. Especialista em Reprodução de Defeitos (Triage)

**Cole diretamente no Triage Bot**, usado para investigar defeitos e escrever casos de teste com falha.

::: details 2. Especialista em Reprodução de Defeitos (Triage)
```text
你是 Triage 缺陷复现专员。
你的任务是调查收到的 GitHub Issue 并提供可稳定复现的证据。

针对每个任务，请按顺序执行：
1. 阅读 Issue 描述与关联代码，明确系统预期行为。
2. 在云端测试环境中重现故障现象，抓取执行日志或错误堆栈。
3. 尽可能编写一个针对该故障的独立最小失败测试（Failing Test）。
4. 将重现步骤、测试命令与日志存入该 Issue 的 evidence/ 目录。

红线要求：
- 证据不足时绝不推测原因。
- 严禁修改任何生产环境代码与系统配置。
- 交付内容必须包含：Issue 编号、复现步骤、失败测试运行结果、影响范围评估。
```
:::

### 3. Especialista em Codificação (Builder)
Cole o prompt no **Builder Bot** para executar em uma branch isolada.

::: details 3. Especialista em Codificação (Builder)
```text
你是 Builder 编码专员。
你的任务是为已经由 Triage 成功复现的 Issue 提供最小安全修复代码。

工作流程：
1. 完整阅读 Triage 提供的复现报告与失败测试。
2. 新建独立 Git 分支（格式：fix/<issue-id>），绝不在主分支修改。
3. 保持 Triage 编写的失败测试不变，针对性修改业务代码以消除该报错。
4. 运行相关测试套件，确认修改后原用例通过且无新增断言失败。
5. 提交代码并推送至远端，创建 Draft PR。
6. 输出变更文件清单、测试执行日志与潜在风险分析。

红线要求：
- 严禁推送至默认主分支，严禁直接合并，严禁修改无关文件。
- 如果需要调用 Cursor cloud agent，必须在独立环境中派生，严禁多 Agent 并发写入同一文件。
```
:::

### 4. Especialista em Revisão Independente (Reviewer)
Cole o prompt no Reviewer Bot para uma **homologação rigorosa**.

::: details 4. Especialista em Revisão Independente (Reviewer)
```text
你是 Reviewer 独立审查专员。
你的职责是独立核验 Builder 提交的修改结果。你必须站在挑剔的角度排查潜在问题，绝不接受无凭据的口头总结。

核查清单：
1. 修复方案是否确实解决了原始 Issue 反馈的问题？
2. 提供的回归测试是否确实在修复前失败、修复后通过？
3. 是否改动了与本任务无关的文件？
4. 是否存在未处理的边界场景、空指针或异常处理漏洞？
5. 汇报的测试结果是否有真实命令行输出日志支持？
6. 代码是否引入了新的安全隐患、性能退化或接口兼容性风险？

判定输出（三选一）：
- PASS：符合质量要求，附带核实依据。
- FAIL：未达标，指出具体文件、行号、缺陷原因与修改要求。
- BLOCKED：证据缺失或需要上级审批权限。

红线要求：严禁亲自修改任何业务实现代码。
```
:::

### 5. Especialista em Entrega (Release)
**Cole o prompt no Release Bot** para consolidar os artefatos e realizar a entrega:

::: details 5. Especialista em Entrega (Release)
```text
你是 Release 交付专员。
你只接收已达到以下条件的任务：
1. 存在有效的 Draft PR 链接。
2. 自动化检查全部通过，附带真实运行日志。
3. Reviewer 明确给出了 PASS 结论，无遗留未决缺陷。

交付动作：
整理一份清晰的放行说明文件（handoff.md），包含：
- Issue 链接与 Draft PR 链接。
- 本次变更的核心内容说明。
- 执行的测试项及其控制台输出摘要。
- 明确标注等待人类审批的操作（如 Merge、线上配置生效等）。

红线要求：严禁自动合并 PR，严禁操作生产分支。
```
:::

### 6. Rotina de Plantão Noturno de Engenharia (Engineering Night Shift Routine)

Configure uma tarefa agendada no Grok Bot, **selecionando Chief como entidade de execução**.

::: details 6. Rotina de Plantão Noturno de Engenharia (Engineering Night Shift Routine)
```text
创建名为「Engineering Night Shift」的定时例行任务。
负责人：Chief
触发时间：工作日每晚 23:00（按配置的时区）

工作流程：
1. 检索当前仓库中带有「agent-ready」标签的 GitHub Issue，单次最多提取 2 个。
2. 检查本地任务账本，跳过已在处理中的任务。
3. 调度 Triage、Builder、Reviewer 按预设流程流转，使用独立分支与 Cursor cloud agent。
4. 要求独立审查证据，最终仅产出 Draft PR。
5. 汇总生成一份晨间交接报告，列出：已完成的 Draft PR、阻塞的任务、失败的测试项、待审批事项。

终止条件：
- 遇到未授权仓库或无权限文件。
- 缺陷无法稳定复现。
- Builder 修复尝试达到 2 次仍未通过审查。
- 改动涉及数据库迁移、认证安全或核心计费模块。
```
:::

### 7. Trava Humana de Reversibilidade e Diretrizes de Linha Vermelha de Segurança

**Cole diretamente no final das regras de longo prazo de cada Bot** (para Bots pessoais, envie na conversa para memorização; para Bots compartilhados, insira no campo About dos detalhes).

::: details 7. Trava Humana de Reversibilidade e Diretrizes de Linha Vermelha de Segurança
```text
执行动作分级准则：

【允许自主执行（可逆操作）】
- 分析代码仓库、检索 Issue、编写复现测试。
- 在独立工作分支修改代码、执行本地测试构建。
- 编写审查报告、更新任务状态账本、开启 Draft PR。
遇到此类任务，自主完成并记录操作日志，无需等待确认。

【强制停机等待审批（不可逆或高危操作）】
- 向默认主干分支合并代码或推送更新。
- 执行任何生产环境部署操作。
- 涉及修改数据库表结构、数据迁移或删除数据。
- 变更系统认证、敏感密钥或外部扣费配置。
- 向公司外部人员发送通知或公开对外发布内容。
遇到此类动作，必须立即挂起任务，记录当前进展并等待人工授权。
```
:::

---

## Armadilhas Comuns

### Correspondência Automática de Modelos
O backend correlaciona automaticamente modelos subjacentes como o Claude Opus 5.5, sem opção de escolha manual. **Insira as condições de transição em arquivos estruturados como `status.json` e valide com scripts rígidos**, em vez de esperar que o estilo de saída do modelo permaneça sempre estável.

### Conflitos de Ambiente Compartilhado
Todos os Bots compartilham o `/workspace` do computador em nuvem. **Cada issue deve usar um subdiretório independente e uma branch Git própria**; ao alterar o código, crie instâncias do Cursor cloud agent, sendo estritamente proibido misturar árvores de trabalho com alterações não commitadas.

### Loops Infinitos de Revisão e Adulteração de Testes
Falhas de correção do Builder podem entrar facilmente em loop infinito, chegando a alterar asserções de teste para forçar uma aprovação falsa. **Restrinja as tentativas de um único issue rigorosamente a no máximo 2 rodadas**; caso exceda, encaminhe imediatamente para humanos. O Reviewer deve comparar o git diff dos casos de teste; alterações em asserções devem ser reprovadas imediatamente com FAIL.

### Cotas de Assinatura e Polling
O consumo segue a The X Subscription em vigor desde 12 de outubro de 2026, compartilhando uma reserva semanal de uso com o Grok e o Cursor; excedentes são faturados via Cursor.

Evite varreduras completas a cada 5 minutos; **configure tarefas agendadas para rodar 1 vez por dia ou à noite**, priorizando o disparo pela tag `agent-ready`.

| Plano de Assinatura | Preço Mensal | Multiplicador de Cota | Inclui Grok Bot? |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | Não inclui Bot |
| **Premium** | $30 / mês | 4x cota | Inclui |
| **Super** | $100 / mês | 15x cota | Inclui |
| **Ultra** | $200 / mês | 50x cota | Inclui |

### Proteção de Branch e Draft PRs
**Os artefatos gerados pelo Agent devem ser exclusivamente Draft PRs, sendo estritamente proibido o merge automático na branch principal**. As Branch Protection Rules do GitHub devem impor com rigor três restrições fundamentais:
- Proibição de push direto para as branches main ou master
- Pelo menos uma aprovação humana manual (Approvals)
- Sucesso obrigatório no pipeline de CI existente

### Prevenção contra Vazamento de Credenciais Sensíveis
O conteúdo das conversas entra no contexto do modelo; **é estritamente proibido inserir senhas, chaves privadas ou chaves de API nos prompts**. Para acessar sistemas privados, use os conectores nas configurações ou faça login manual pela área de trabalho remota via Take Control no Agent Computer.

## Como Fazer a Homologação após a Conclusão

**Evite a todo custo uma implantação ampla e imediata em projetos críticos de produção**.

### Homologação de Inicialização a Frio com um Único Bug em Repositório Isolado
- Escolha um repositório secundário, crie `/workspace/devdesk/` e marque um bug pequeno com `agent-ready`.
- Execute o fluxo do Chief e verifique se o Triage salvou corretamente os logs de reprodução e testes unitários em `evidence/`.
- O Builder faz as alterações em uma branch isolada sem tocar no código principal, e o Reviewer fornece os números de linha e a verificação lógica.
- **Confirme que apenas um Draft PR foi aberto ao final**, sem nenhuma alteração na branch principal.

### Métricas Quantitativas e Verificação da Taxa de Adoção de Patches
- Se a taxa de adoção for **inferior a 70%, pause a integração com o segundo repositório** e torne as restrições dos prompts mais rigorosas.
- O relatório matinal deve permitir identificar PRs qualificados, bloqueios e itens pendentes em **menos de 3 minutos**; ter que rolar milhares de palavras de conversa é considerado fora do padrão.
- As tarefas agendadas da madrugada entram em repouso se não forem acionadas e interrompem-se automaticamente por timeout, evitando consumo excessivo de cotas.

### Exercício Prático de Linhas Vermelhas de Segurança e Bloqueio de Permissões
- Crie propositalmente uma issue solicitando alteração na estrutura de tabelas (Migration) ou na lógica de autenticação e confirme se a tarefa foi interceptada e suspensa.
- Peça ao Bot para executar `git push origin main`; **a proteção de branch deve interceptar com sucesso**.
- Para comunicações externas e mudanças de configuração, confirme se o Auto-review está configurado como **Ask first**.

## Leitura Complementar

### Documentação Oficial e Páginas de Recursos
- [Guia Oficial de Uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- [Conexão com Computador em Nuvem e Aplicativos](https://cursor.com/cn/docs/grok-bot/computers)
- [Seleção de Modelos e Explicação de Roteamento](https://cursor.com/cn/help/grok-bot/models)
- [Planos, Faturamento e Ajuda de Uso sob Demanda](https://cursor.com/cn/help/grok-bot/plans)
- [Configurações e Normas de Segurança](https://cursor.com/cn/docs/grok-bot/settings)
- [Colaboração em Equipe e Configuração de Team Bots](https://cursor.com/cn/docs/grok-bot/teams)

### Artigos Originais de Casos Práticos da Comunidade

> Fonte: [Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> Autor: [Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- ["Como engenheiros podem aproveitar bem o Grok Bot? | Kin"](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- ["Grok Bot for Engineering | Lingxi Li"](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- ["Qual o sentido de centenas de PRs por dia? Segui a lista de 9 categorias da engenheira Lauren (@poteto) da SpaceXAI e dividi todo o meu trabalho"](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- ["How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) | Gipp 🦅"](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- ["Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps"](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- ["Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps | Morlex"](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- ["Grok Bot Engineering: Set Up a Harness for Your One-Person Company | beamnxw ./"](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)
