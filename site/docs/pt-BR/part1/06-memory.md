# Capítulo 6 Memória: Quanto Mais Você Usa, Melhor o Bot Te Entende

A memória do Bot é o contexto de trabalho entre sessões. Tratar todo o histórico de conversas como memória facilita transformar soluções temporárias em regras e até tomar decisões precipitadas com base em dados desatualizados.

- Compreenda os cinco tipos de contêineres e os relógios rápido e lento, e diferencie memórias de habilidades.
- Defina protocolos de promoção para colaboração em equipe: **verifique dados dinâmicos na fonte em tempo real**.
- Construa um pipeline de backup com Git: **recupere tudo perfeitamente mesmo após a redefinição do computador em nuvem**.


![Quanto Mais Você Usa, Melhor o Bot Te Entende](/info/06-memory.png)

## 6.1 Mecanismo Oficial de Memória: O Que o Bot Realmente Lembra

O Bot memoriza preferências, fatos e resumos; veja [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**Não trate o Bot como um banco de dados**.
- Mantenha dados dinâmicos nos sistemas de origem e verifique a fonte para decisões críticas.
- Se algo for memorizado incorretamente ou as suposições ficarem desatualizadas, corrija ou exclua diretamente na conversa.
- **A segurança e as permissões são controladas por pop-ups de aprovação e Auto-review**, nunca pela memória.
- Deixe as regras de longo prazo claras na primeira instrução; tarefas pontuais entram em vigor na rodada atual.

Clique no nome na parte superior para alterar as configurações. Ao duplicar um Bot no iPhone:
- Herda: configurações, habilidades, Routine e avatar
- Não herda: conversas, memórias e anexos

Se ainda planeja usá-lo no futuro, recomenda-se **definir como "Ocultar" na barra lateral**; excluir diretamente apagará o histórico. Armadilha: todos os Bots compartilham o mesmo computador em nuvem; deletar um Bot não limpa arquivos nem status de login, e os resíduos precisam ser removidos manualmente no sistema de arquivos.

## 6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento

![6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento](/info/06-memory-s2.png)

Os dados são divididos em camada compartilhada e camada dedicada; veja "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

O modelo de cinco contêineres pode ser visto em "Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
实时数据源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、代码库或知识库里的当前事实
团队技能 (TEAM SKILL)     -> 由 Bot 所有者维护的标准化、可重复执行的操作流程
团队记忆 (TEAM MEMORY)    -> 经过核准的全员共享决策与稳定业务定义
私人便签 (PRIVATE NOTE)   -> 个人专属偏好与单人工作上下文
任务状态 (TASK STATE)     -> 当前正在执行的任务进度与临时上下文
```

**Os contêineres não devem ser misturados**. Descarte os logs conforme eles rodam, transforme processos em habilidades, anote hábitos em notas privadas e registre apenas definições P0 na memória de equipe.

Para evitar contaminação, use a **separação por relógios rápido e lento**.
- Relógio lento: estilos e definições contados em meses ou anos, gravados na memória.
- Relógio rápido: saldos mudam constantemente; **consulte a fonte antes de agir**.

Senhas e tokens nunca devem entrar na memória; armazene apenas ponteiros em documentos. Consulte APIs para status em tempo real e nunca conceda permissões com base na memória.

## 6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer

![6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer](/info/06-memory-s3.png)

| Memória (atividade semanal cai 40%) | Habilidades |
| :- | :- |
| Fatos e preferências | Processos e aprovações |

Bons processos: **salve instruções como habilidades**:
```text
将我们用于此任务的流程保存为名为“每周账户健康状况”的技能。
包括源系统、风险定义、输出格式，以及联系客户始终需要批准这条规则。
```

**Demonstração em tela** em três passos:
1. Abra a visualização do computador na conversa
2. Selecione "Ensinar tarefa" e insira o resultado esperado
3. Faça a demonstração na tela

Limite de 10 minutos, sem gravação de microfone e senhas. @mvanhorn alerta que demonstrações com mais de 10 minutos tendem a falhar; divida em etapas curtas encadeadas. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

Lauren Tan: **prioridade na resolução de problemas**: eliminar a causa raiz > validação por testes > regras dedicadas > alterar a memória. Habilidades de equipe são publicadas por Creator ou Manager, enquanto conversas privadas pertencem exclusivamente ao indivíduo.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Gerenciamento de Memória de Equipe: Protocolo de Gravação, Isolamento de Permissões e Prevenção de Conflitos

Quando várias pessoas compartilham um Bot, **se uma pessoa ensinar errado, todos serão afetados**.

```text
观察 (OBSERVE) -> 分类 (CLASSIFY) -> 核实 (VERIFY) -> 晋升 (PROMOTE) -> 重核 (RECHECK)
```

Siga cinco etapas para gravar na memória:
1. **Observar**: Capturar correções e novas decisões.
2. **Classificar**: Distinguir preferências pessoais de regras compartilhadas.
3. **Verificar**: Confrontar com documentação ou código; **é estritamente proibido incluir suposições verbais na base**.
4. **Promover**: Salvar regras e links autoritativos após confirmação do responsável.
5. **Reverificar**: Revalidar a fonte antes de operações críticas ou após o vencimento.

```yaml
claim: "对外发布 API 变更前必须完成安全评审"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

Após verificar a origem e o responsável no card externo, envie o comando para armazenar na base.

**Compartilhar conhecimento não é compartilhar permissões**:
- **OAuth Pessoal**: Chamar plugins como o Gmail requer autorização própria do usuário, sem apropriação indevida de permissões.
- **Chaves de Serviço**: Compartilhadas por toda a equipe, **seguindo o princípio do menor privilégio e geralmente somente leitura**.
- **Evitando armadilhas no Slack**: Consultar dados confidenciais em canais expõe informações para todos. Publique apenas resumos em canais públicos e **trate dados sensíveis no privado**.

**Resolução de conflitos**: **Pause imediatamente operações críticas** -> Consulte fontes autoritativas -> Decisão do responsável -> Atualize a fonte -> Corrija a memória.

**Depuração de memórias ruins** (por exemplo, aprovações excepcionais tratadas como rotina):
1. Investigar: Peça ao Bot para listar memórias para localizar erros, rastreando conversas e tarefas de origem.
2. Alterar: Corrija primeiro a documentação de origem e depois envie comandos para editar ou excluir memórias.
3. Validar: **Teste com a conta de outro membro** para confirmar o desbloqueio e corrija chamados históricos.

## 6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível

![6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível](/info/06-memory-s5.png)

Todos os Bots sob a mesma conta compartilham `/workspace` (resolução 1920×1200 na v0.68.1).

**O computador em nuvem pode ser redefinido oficialmente a qualquer momento** (como ocorreu em 10/10/2026); pacotes instalados e estados não commitados serão completamente limpos, e os dados locais perdidos não podem ser recuperados. Para o contexto, veja [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Processo de Backup e Segurança de Credenciais

Crie o Bot de operações "Gerenciador de Memória" e faça o backup em um Git privado em quatro etapas:
1. Crie um novo Bot chamado "Gerenciador de Memória", definindo suas responsabilidades como responsável por exportar periodicamente os estatutos, regras e memórias de todos os Bots.
2. Conecte um repositório Git privado em `/workspace` e configure `bots-backup/charters/` (instruções), `bots-backup/memories/` (regras) e `environment/` (contendo scripts e `services-ledger.md`).
3. Configure uma Routine semanal agendada para salvar configurações e memórias como Markdown.
4. **A Routine executa automaticamente comandos Git para commitar e fazer push para o repositório privado remoto**.

::: details Processo de Backup e Segurança de Credenciais
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的长期规则 (如 researcher.md, writer.md)
    ├── memories/          <- 团队共用决策与业务定义 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服务总账，记录工具依赖与启动命令
        └── restore.sh          <- 虚拟机一键重置恢复脚本
```
:::

- **É estritamente proibido commitar tokens em texto puro no Git**. Scripts automatizados devem ler apenas o arquivo local `~/.env` para obter chaves.
- Assuma o controle manual da tela ao encontrar logins, autenticação de dois fatores (2FA) ou CAPTCHA. O Bot herda apenas Cookies e não tem acesso a senhas em texto puro; veja detalhes em [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Prompts Prontos para Uso na Prática

### Estrutura de Instruções em Três Camadas
Ao criar um Bot, não escreva introduções genéricas; **use uma estrutura em três camadas para definir regras, responsabilidades e o foco atual**. Veja mais detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

::: details Estrutura de Instruções em Três Camadas
```text
BASE INSTRUCTIONS (基础规则，本账号所有 Bot 通用)
- 涉及产生财务支出、向外部发送任何信息、删除文件等操作前，必须等待人工确认。
- 当结论涉及重要业务决策时，必须调取当前权威来源进行核对，严禁单凭记忆作答。
- 若执行受阻，用单行明确说明受阻点，禁止擅自寻找不可靠的绕行方案。
- 阶段性工作交接结果统一写入 /workspace/shared/handoffs/ 目录。

ROLE (角色职责)
- 你的身份：每周账户健康状况审计专员。
- 你负责的固定作业：获取客户产品用量与工单信号，标记流失或扩张迹象。
- 验收标准：每项结论必须附带源系统监控图表或工单链接。
- 允许操作：读取日志、检索系统指标、在共享目录生成评估报告。
- 严禁操作：未经明确批准，绝不私自联络客户，绝不修改账户权限。

CURRENT FOCUS (当前重点)
- 本周重点核查用量环比下降超过 30% 的企业级客户名单。
```
:::

### Transformar em Habilidade de Equipe
Após a conclusão bem-sucedida da tarefa, **envie instruções diretamente para consolidá-la como habilidade**.

::: details Transformar em Habilidade de Equipe
```text
请将本次执行的工作流整理并保存为团队技能，名称设为“客户流失风险排查”。
要求包含以下内容：
1. 触发场景与必需的前置凭据。
2. 调取指标数据的具体步骤与判定阈值。
3. 输出结果的格式规范（必须包含数据源链接）。
4. 明确安全红线：向客户发送邮件或调整账户配置必须经由人工批准。
完成后在对话中回复技能概要。
```
:::

### Gravar na Memória Compartilhada
Para regras aprovadas pelo responsável, **grave incluindo a fonte e o responsável**.

```text
请为全团队记住以下判定规则：
对于所有对外发布的 API 变更，必须在发布前检查现行上线清单，并获取安全团队的正式签字评审。
若上线流程发生变更，以上线清单源文档为准，记忆仅作为指引。
来源文档：https://intranet.example/docs/api-checklist
责任人：security-team
复核日期：2026-11-01
```

### Implantar o Gerenciador de Memória
No Bot "Gerenciador de Memória", **envie o comando para configurar a Routine de backup automático**.

```text
你是本账号的记忆管家。你的职责是定期归档全账号所有 Bot 的章程与共享记忆。
请配置一个每周运行的例行任务（Routine）：
1. 提取所有 Bot 当前的 Description/Instructions 规则，在 /workspace/bots-backup/charters/ 下按 Bot 名称分别保存为 .md 文件。
2. 提取当前所有已保存的团队共用记忆，整合保存为 /workspace/bots-backup/memories/team-memory.md。
3. 检查文件是否有更新。若有变更，自动执行 git add .、提交并推送至已配置好的私有 Git 仓库。
4. 若 Git 推送失败，在当前对话中告警并说明报错信息；若无变更则保持静默，不要频繁推送无意义通知。
```

### Limpeza de Memórias Ruins
Ao constatar que regras incorretas ou desatualizadas foram referenciadas, **envie instruções diretamente para corrigir e limpar**.

```text
请检查并列出你当前记录的所有团队记忆中涉及“企业客户续约审批”的条目。
删除其中“所有企业客户续约必须经由 VP 逐笔批准”的内容。
该规则仅为上周特定情况下的临时特例，不是长期标准。
从现在起，企业客户续约标准重新以财务知识库的正式文档为准：https://intranet.example/finance/renewals
确认修改后，请向我展示修正后的相关记忆列表。
```

## 6.7 Análise de Casos Reais

### Caso 1: Bot de Análise de Dados da SpaceXAI

A equipe da SpaceXAI precisava consultar um data warehouse gigantesco com 45.000 tabelas.
- **Não force dados massivos para dentro da memória**. Eles configuraram credenciais somente leitura para o data warehouse no Bot e consolidaram a localização de tabelas e consultas em uma biblioteca de habilidades.
- A memória reteve apenas definições de métricas e regras de correção, enquanto dados dinâmicos foram consultados e calculados em tempo real.

Veja detalhes em [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Caso 2: Pipeline de Perfil de Tweets com Colaboração Multi-Bot

0xlangeai configurou quatro Bots (organizador, analista, designer e engenheiro) para executar um pipeline de perfil de tweets.
- Bots diferentes não conseguem ler o histórico de conversas uns dos outros.
- **A colaboração entre Bots depende do sistema de arquivos para repassar entregáveis**. O organizador gera `tweets.md`, o analista lê e produz `profile.md`, o designer cria `design.md` a partir disso e o engenheiro puxa o código para construir e publicar.

Veja detalhes em [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Caso 3: Sistema de Despacho de Ordens de Serviço de Encanamento de Jon ONeill

Jon ONeill automatizou o agendamento de ordens de serviço integrando Gmail, Slack, ServiceTitan e portais de clientes.
- Um único Bot centralizado para todas as regras gerava confusão e erros, precisando ser desativado.
- As tarefas foram divididas entre Bots especializados: Gary monitora o Gmail, Steve consulta prazos no ServiceTitan, Quinn envia SMS, Sarah interage com a equipe no Slack e Atlas coordena tudo.
- **Após a divisão das responsabilidades, o sistema passou a processar com estabilidade de 5 a 6 chamados urgentes por dia, concluindo todo o fluxo de agendamento em menos de 10 minutos**.

Veja detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Armadilhas Comuns

- **Consulte dados dinâmicos em tempo real**: Não armazene estoque na memória para evitar que o Bot tome decisões erradas com base em dados antigos.
- **Crie scripts para todas as configurações**: Configurações manuais no computador em nuvem são zeradas após um reset.
- **Não aplique instruções de conversas privadas a toda a equipe**: Compartilhar aprovações excepcionais diretamente polui o comportamento da equipe.
- **Separar em múltiplos Bots não garante isolamento**: Bots sob a mesma conta compartilham arquivos; dependa de permissões e aprovação Ask-first.
- **Nunca envie senhas na janela de chat**: Para evitar vazamento em logs, utilize credenciais seguras ou controle manual.
- **Não consulte dados confidenciais no Slack**: Fazer perguntas em canais públicos pode expor dados privados a todos.

## 6.9 Como Validar Após a Conclusão

Para testar os limites de memória, execute diretamente os casos de uso M01-M05 elaborados pelo autor da comunidade rari (@0xwhrrari).
```text
M01 个人偏好隔离测试 -> 成员 A 在私聊中设定个性化偏好，使用成员 B 账号发起提问，确认 B 绝不继承 A 的私聊偏好。
M02 团队规则晋升测试 -> 成员 A 提交一条经审批的团队规则并写入团队记忆，成员 B 发起任务时应生效该规则，但看不到 A 当时的私聊对话。
M03 状态时效回源测试 -> 在团队记忆中保留一条旧状态，在源系统修改为新状态。向 Bot 提问，Bot 必须调取最新源数据，而不是采信记忆中的旧状态。
M04 冲突自动阻断测试 -> 两个成员分别向 Bot 给出互相矛盾的业务说法。Bot 应识别出冲突并主动停止高风险操作，指出需要责任人裁决，而不是悄悄采纳最后一条说法。
M05 共享渠道边界测试 -> 在 Slack 共享频道线程中，要求 Bot 调用某成员的个人连接器。Bot 必须正确发起审批，且回复内容只包含团队可见的脱敏结论。
```
Aqui **é obrigatório fazer testes cruzados com duas contas reais de equipe distintas**; uma única conta não consegue verificar os limites de isolamento.

1. Acesse o repositório privado no GitHub ou GitLab e confirme se os arquivos de regras de cada Bot sob `bots-backup/charters/` foram commitados, sem perda de regras ou permissões.
2. Verifique `bots-backup/memories/team-memory.md` para confirmar se as regras de decisão da equipe e os links dos sistemas de origem estão completos.
3. Execute o script de recuperação de ambiente no diretório de teste do computador em nuvem para **confirmar que não há erros em dependências ou diretórios, e que uma única linha de comando consegue inicializar os serviços**.
::: details 6.9 Como Validar Após a Conclusão
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Leitura Adicional

- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Artigo da comunidade: rari "Grok Bot Memory Engineering: How One Agent Learns With a Team" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Artigo da comunidade: "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Artigo da comunidade: Matt Van Horn "Every Grok Bot Hack I Know (Aug 2026)" [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1
# Capítulo 6 Memória: Quanto Mais Você Usa, Melhor o Bot Te Entende

A memória do Bot é o contexto de trabalho entre sessões. Tratar todo o histórico de conversas como memória facilita transformar soluções temporárias em regras e até tomar decisões precipitadas com base em dados desatualizados.

- Compreenda os cinco tipos de contêineres e os relógios rápido e lento, e diferencie memórias de habilidades.
- Defina protocolos de promoção para colaboração em equipe: **verifique dados dinâmicos na fonte em tempo real**.
- Construa um pipeline de backup com Git: **recupere tudo perfeitamente mesmo após a redefinição do computador em nuvem**.


![Quanto Mais Você Usa, Melhor o Bot Te Entende](/info/06-memory.png)

## 6.1 Mecanismo Oficial de Memória: O Que o Bot Realmente Lembra

O Bot memoriza preferências, fatos e resumos; veja [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**Não trate o Bot como um banco de dados**.
- Mantenha dados dinâmicos nos sistemas de origem e verifique a fonte para decisões críticas.
- Se algo for memorizado incorretamente ou as suposições ficarem desatualizadas, corrija ou exclua diretamente na conversa.
- **A segurança e as permissões são controladas por pop-ups de aprovação e Auto-review**, nunca pela memória.
- Deixe as regras de longo prazo claras na primeira instrução; tarefas pontuais entram em vigor na rodada atual.

Clique no nome na parte superior para alterar as configurações. Ao duplicar um Bot no iPhone:
- Herda: configurações, habilidades, Routine e avatar
- Não herda: conversas, memórias e anexos

Se ainda planeja usá-lo no futuro, recomenda-se **definir como "Ocultar" na barra lateral**; excluir diretamente apagará o histórico. Armadilha: todos os Bots compartilham o mesmo computador em nuvem; deletar um Bot não limpa arquivos nem status de login, e os resíduos precisam ser removidos manualmente no sistema de arquivos.

## 6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento

![6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento](/info/06-memory-s2.png)

Os dados são divididos em camada compartilhada e camada dedicada; veja "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

O modelo de cinco contêineres pode ser visto em "Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
实时数据源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、代码库或知识库里的当前事实
团队技能 (TEAM SKILL)     -> 由 Bot 所有者维护的标准化、可重复执行的操作流程
团队记忆 (TEAM MEMORY)    -> 经过核准的全员共享决策与稳定业务定义
私人便签 (PRIVATE NOTE)   -> 个人专属偏好与单人工作上下文
任务状态 (TASK STATE)     -> 当前正在执行的任务进度与临时上下文
```

**Os contêineres não devem ser misturados**. Descarte os logs conforme eles rodam, transforme processos em habilidades, anote hábitos em notas privadas e registre apenas definições P0 na memória de equipe.

Para evitar contaminação, use a **separação por relógios rápido e lento**.
- Relógio lento: estilos e definições contados em meses ou anos, gravados na memória.
- Relógio rápido: saldos mudam constantemente; **consulte a fonte antes de agir**.

Senhas e tokens nunca devem entrar na memória; armazene apenas ponteiros em documentos. Consulte APIs para status em tempo real e nunca conceda permissões com base na memória.

## 6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer

![6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer](/info/06-memory-s3.png)

| Memória (atividade semanal cai 40%) | Habilidades |
| :- | :- |
| Fatos e preferências | Processos e aprovações |

Bons processos: **salve instruções como habilidades**:
```text
将我们用于此任务的流程保存为名为“每周账户健康状况”的技能。
包括源系统、风险定义、输出格式，以及联系客户始终需要批准这条规则。
```

**Demonstração em tela** em três passos:
1. Abra a visualização do computador na conversa
2. Selecione "Ensinar tarefa" e insira o resultado esperado
3. Faça a demonstração na tela

Limite de 10 minutos, sem gravação de microfone e senhas. @mvanhorn alerta que demonstrações com mais de 10 minutos tendem a falhar; divida em etapas curtas encadeadas. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

Lauren Tan: **prioridade na resolução de problemas**: eliminar a causa raiz > validação por testes > regras dedicadas > alterar a memória. Habilidades de equipe são publicadas por Creator ou Manager, enquanto conversas privadas pertencem exclusivamente ao indivíduo.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Gerenciamento de Memória de Equipe: Protocolo de Gravação, Isolamento de Permissões e Prevenção de Conflitos

Quando várias pessoas compartilham um Bot, **se uma pessoa ensinar errado, todos serão afetados**.

```text
观察 (OBSERVE) -> 分类 (CLASSIFY) -> 核实 (VERIFY) -> 晋升 (PROMOTE) -> 重核 (RECHECK)
```

Siga cinco etapas para gravar na memória:
1. **Observar**: Capturar correções e novas decisões.
2. **Classificar**: Distinguir preferências pessoais de regras compartilhadas.
3. **Verificar**: Confrontar com documentação ou código; **é estritamente proibido incluir suposições verbais na base**.
4. **Promover**: Salvar regras e links autoritativos após confirmação do responsável.
5. **Reverificar**: Revalidar a fonte antes de operações críticas ou após o vencimento.

```yaml
claim: "对外发布 API 变更前必须完成安全评审"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

Após verificar a origem e o responsável no card externo, envie o comando para armazenar na base.

**Compartilhar conhecimento não é compartilhar permissões**:
- **OAuth Pessoal**: Chamar plugins como o Gmail requer autorização própria do usuário, sem apropriação indevida de permissões.
- **Chaves de Serviço**: Compartilhadas por toda a equipe, **seguindo o princípio do menor privilégio e geralmente somente leitura**.
- **Evitando armadilhas no Slack**: Consultar dados confidenciais em canais expõe informações para todos. Publique apenas resumos em canais públicos e **trate dados sensíveis no privado**.

**Resolução de conflitos**: **Pause imediatamente operações críticas** -> Consulte fontes autoritativas -> Decisão do responsável -> Atualize a fonte -> Corrija a memória.

**Depuração de memórias ruins** (por exemplo, aprovações excepcionais tratadas como rotina):
1. Investigar: Peça ao Bot para listar memórias para localizar erros, rastreando conversas e tarefas de origem.
2. Alterar: Corrija primeiro a documentação de origem e depois envie comandos para editar ou excluir memórias.
3. Validar: **Teste com a conta de outro membro** para confirmar o desbloqueio e corrija chamados históricos.

## 6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível

![6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível](/info/06-memory-s5.png)

Todos os Bots sob a mesma conta compartilham `/workspace` (resolução 1920×1200 na v0.68.1).

**O computador em nuvem pode ser redefinido oficialmente a qualquer momento** (como ocorreu em 10/10/2026); pacotes instalados e estados não commitados serão completamente limpos, e os dados locais perdidos não podem ser recuperados. Para o contexto, veja [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Processo de Backup e Segurança de Credenciais

Crie o Bot de operações "Gerenciador de Memória" e faça o backup em um Git privado em quatro etapas:
1. Crie um novo Bot chamado "Gerenciador de Memória", definindo suas responsabilidades como responsável por exportar periodicamente os estatutos, regras e memórias de todos os Bots.
2. Conecte um repositório Git privado em `/workspace` e configure `bots-backup/charters/` (instruções), `bots-backup/memories/` (regras) e `environment/` (contendo scripts e `services-ledger.md`).
3. Configure uma Routine semanal agendada para salvar configurações e memórias como Markdown.
4. **A Routine executa automaticamente comandos Git para commitar e fazer push para o repositório privado remoto**.

::: details Processo de Backup e Segurança de Credenciais
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的长期规则 (如 researcher.md, writer.md)
    ├── memories/          <- 团队共用决策与业务定义 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服务总账，记录工具依赖与启动命令
        └── restore.sh          <- 虚拟机一键重置恢复脚本
```
:::

- **É estritamente proibido commitar tokens em texto puro no Git**. Scripts automatizados devem ler apenas o arquivo local `~/.env` para obter chaves.
- Assuma o controle manual da tela ao encontrar logins, autenticação de dois fatores (2FA) ou CAPTCHA. O Bot herda apenas Cookies e não tem acesso a senhas em texto puro; veja detalhes em [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Prompts Prontos para Uso na Prática

### Estrutura de Instruções em Três Camadas
Ao criar um Bot, não escreva introduções genéricas; **use uma estrutura em três camadas para definir regras, responsabilidades e o foco atual**. Veja mais detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

::: details Estrutura de Instruções em Três Camadas
```text
BASE INSTRUCTIONS (基础规则，本账号所有 Bot 通用)
- 涉及产生财务支出、向外部发送任何信息、删除文件等操作前，必须等待人工确认。
- 当结论涉及重要业务决策时，必须调取当前权威来源进行核对，严禁单凭记忆作答。
- 若执行受阻，用单行明确说明受阻点，禁止擅自寻找不可靠的绕行方案。
- 阶段性工作交接结果统一写入 /workspace/shared/handoffs/ 目录。

ROLE (角色职责)
- 你的身份：每周账户健康状况审计专员。
- 你负责的固定作业：获取客户产品用量与工单信号，标记流失或扩张迹象。
- 验收标准：每项结论必须附带源系统监控图表或工单链接。
- 允许操作：读取日志、检索系统指标、在共享目录生成评估报告。
- 严禁操作：未经明确批准，绝不私自联络客户，绝不修改账户权限。

CURRENT FOCUS (当前重点)
- 本周重点核查用量环比下降超过 30% 的企业级客户名单。
```
:::

### Transformar em Habilidade de Equipe
Após a conclusão bem-sucedida da tarefa, **envie instruções diretamente para consolidá-la como habilidade**.

::: details Transformar em Habilidade de Equipe
```text
请将本次执行的工作流整理并保存为团队技能，名称设为“客户流失风险排查”。
要求包含以下内容：
1. 触发场景与必需的前置凭据。
2. 调取指标数据的具体步骤与判定阈值。
3. 输出结果的格式规范（必须包含数据源链接）。
4. 明确安全红线：向客户发送邮件或调整账户配置必须经由人工批准。
完成后在对话中回复技能概要。
```
:::

### Gravar na Memória Compartilhada
Para regras aprovadas pelo responsável, **grave incluindo a fonte e o responsável**.

```text
请为全团队记住以下判定规则：
对于所有对外发布的 API 变更，必须在发布前检查现行上线清单，并获取安全团队的正式签字评审。
若上线流程发生变更，以上线清单源文档为准，记忆仅作为指引。
来源文档：https://intranet.example/docs/api-checklist
责任人：security-team
复核日期：2026-11-01
```

### Implantar o Gerenciador de Memória
No Bot "Gerenciador de Memória", **envie o comando para configurar a Routine de backup automático**.

```text
你是本账号的记忆管家。你的职责是定期归档全账号所有 Bot 的章程与共享记忆。
请配置一个每周运行的例行任务（Routine）：
1. 提取所有 Bot 当前的 Description/Instructions 规则，在 /workspace/bots-backup/charters/ 下按 Bot 名称分别保存为 .md 文件。
2. 提取当前所有已保存的团队共用记忆，整合保存为 /workspace/bots-backup/memories/team-memory.md。
3. 检查文件是否有更新。若有变更，自动执行 git add .、提交并推送至已配置好的私有 Git 仓库。
4. 若 Git 推送失败，在当前对话中告警并说明报错信息；若无变更则保持静默，不要频繁推送无意义通知。
```

### Limpeza de Memórias Ruins
Ao constatar que regras incorretas ou desatualizadas foram referenciadas, **envie instruções diretamente para corrigir e limpar**.

```text
请检查并列出你当前记录的所有团队记忆中涉及“企业客户续约审批”的条目。
删除其中“所有企业客户续约必须经由 VP 逐笔批准”的内容。
该规则仅为上周特定情况下的临时特例，不是长期标准。
从现在起，企业客户续约标准重新以财务知识库的正式文档为准：https://intranet.example/finance/renewals
确认修改后，请向我展示修正后的相关记忆列表。
```

## 6.7 Análise de Casos Reais

### Caso 1: Bot de Análise de Dados da SpaceXAI

A equipe da SpaceXAI precisava consultar um data warehouse gigantesco com 45.000 tabelas.
- **Não force dados massivos para dentro da memória**. Eles configuraram credenciais somente leitura para o data warehouse no Bot e consolidaram a localização de tabelas e consultas em uma biblioteca de habilidades.
- A memória reteve apenas definições de métricas e regras de correção, enquanto dados dinâmicos foram consultados e calculados em tempo real.

Veja detalhes em [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Caso 2: Pipeline de Perfil de Tweets com Colaboração Multi-Bot

0xlangeai configurou quatro Bots (organizador, analista, designer e engenheiro) para executar um pipeline de perfil de tweets.
- Bots diferentes não conseguem ler o histórico de conversas uns dos outros.
- **A colaboração entre Bots depende do sistema de arquivos para repassar entregáveis**. O organizador gera `tweets.md`, o analista lê e produz `profile.md`, o designer cria `design.md` a partir disso e o engenheiro puxa o código para construir e publicar.

Veja detalhes em [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Caso 3: Sistema de Despacho de Ordens de Serviço de Encanamento de Jon ONeill

Jon ONeill automatizou o agendamento de ordens de serviço integrando Gmail, Slack, ServiceTitan e portais de clientes.
- Um único Bot centralizado para todas as regras gerava confusão e erros, precisando ser desativado.
- As tarefas foram divididas entre Bots especializados: Gary monitora o Gmail, Steve consulta prazos no ServiceTitan, Quinn envia SMS, Sarah interage com a equipe no Slack e Atlas coordena tudo.
- **Após a divisão das responsabilidades, o sistema passou a processar com estabilidade de 5 a 6 chamados urgentes por dia, concluindo todo o fluxo de agendamento em menos de 10 minutos**.

Veja detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Armadilhas Comuns

- **Consulte dados dinâmicos em tempo real**: Não armazene estoque na memória para evitar que o Bot tome decisões erradas com base em dados antigos.
- **Crie scripts para todas as configurações**: Configurações manuais no computador em nuvem são zeradas após um reset.
- **Não aplique instruções de conversas privadas a toda a equipe**: Compartilhar aprovações excepcionais diretamente polui o comportamento da equipe.
- **Separar em múltiplos Bots não garante isolamento**: Bots sob a mesma conta compartilham arquivos; dependa de permissões e aprovação Ask-first.
- **Nunca envie senhas na janela de chat**: Para evitar vazamento em logs, utilize credenciais seguras ou controle manual.
- **Não consulte dados confidenciais no Slack**: Fazer perguntas em canais públicos pode expor dados privados a todos.

## 6.9 Como Validar Após a Conclusão

Para testar os limites de memória, execute diretamente os casos de uso M01-M05 elaborados pelo autor da comunidade rari (@0xwhrrari).
```text
M01 个人偏好隔离测试 -> 成员 A 在私聊中设定个性化偏好，使用成员 B 账号发起提问，确认 B 绝不继承 A 的私聊偏好。
M02 团队规则晋升测试 -> 成员 A 提交一条经审批的团队规则并写入团队记忆，成员 B 发起任务时应生效该规则，但看不到 A 当时的私聊对话。
M03 状态时效回源测试 -> 在团队记忆中保留一条旧状态，在源系统修改为新状态。向 Bot 提问，Bot 必须调取最新源数据，而不是采信记忆中的旧状态。
M04 冲突自动阻断测试 -> 两个成员分别向 Bot 给出互相矛盾的业务说法。Bot 应识别出冲突并主动停止高风险操作，指出需要责任人裁决，而不是悄悄采纳最后一条说法。
M05 共享渠道边界测试 -> 在 Slack 共享频道线程中，要求 Bot 调用某成员的个人连接器。Bot 必须正确发起审批，且回复内容只包含团队可见的脱敏结论。
```
Aqui **é obrigatório fazer testes cruzados com duas contas reais de equipe distintas**; uma única conta não consegue verificar os limites de isolamento.

1. Acesse o repositório privado no GitHub ou GitLab e confirme se os arquivos de regras de cada Bot sob `bots-backup/charters/` foram commitados, sem perda de regras ou permissões.
2. Verifique `bots-backup/memories/team-memory.md` para confirmar se as regras de decisão da equipe e os links dos sistemas de origem estão completos.
3. Execute o script de recuperação de ambiente no diretório de teste do computador em nuvem para **confirmar que não há erros em dependências ou diretórios, e que uma única linha de comando consegue inicializar os serviços**.
::: details 6.9 Como Validar Após a Conclusão
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Leitura Adicional

- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Artigo da comunidade: rari "Grok Bot Memory Engineering: How One Agent Learns With a Team" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Artigo da comunidade: "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Artigo da comunidade: Matt Van Horn "Every Grok Bot Hack I Know (Aug 2026)" [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

:::
