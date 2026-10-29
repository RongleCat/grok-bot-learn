# ui.json chrome 润色 STATUS

- **时间**：2026-10-29 03:10 (America/Los_Angeles)
- **范围**：`theme/ui.json`（zh-CN 真源）→ `theme/locales/{zh-Hant,en,ja,ko,es,pt-BR}/ui.json`
- **约束**：未 push / 未 deploy；读者文案用 agy / OpenCC
- **模型**：agy `--model gemini-3.8-flash-high`（en/ja/ko/es/pt-BR）；zh-Hant = OpenCC s2twp + 专名回写

## 产出文件

| locale | path |
|---|---|
| zh-Hant | `site/docs/.vitepress/theme/locales/zh-Hant/ui.json` |
| en | `site/docs/.vitepress/theme/locales/en/ui.json` |
| ja | `site/docs/.vitepress/theme/locales/ja/ui.json` |
| ko | `site/docs/.vitepress/theme/locales/ko/ui.json` |
| es | `site/docs/.vitepress/theme/locales/es/ui.json` |
| pt-BR | `site/docs/.vitepress/theme/locales/pt-BR/ui.json` |

## 关键文案抽检

| locale | nav.groupPill | footer.group | xiaotiezhu.title | join.qrAlt |
|---|---|---|---|---|
| zh-Hant | 付費答疑群 | 付費答疑群 | 小铁柱 | 铁柱的個人微信二維碼 |
| en | Paid Q&A Group | Paid Q&A Group | 小铁柱 | Personal WeChat QR code of 铁柱 |
| ja | 有料Q&Aグループ | 有料Q&Aグループ | 小铁柱 | 铁柱の個人WeChat QRコード |
| ko | 유료 Q&A방 | 유료 Q&A방 | 小铁柱 | 铁柱 개인 WeChat QR 코드 |
| es | Grupo Q&A de pago | Grupo Q&A de pago | 小铁柱 | Código QR del WeChat personal de 铁柱 |
| pt-BR | Grupo pago de dúvidas | Grupo pago de dúvidas | 小铁柱 | QR Code do WeChat pessoal de 铁柱 |

## 各语种改动要点

### zh-Hant（OpenCC s2twp）
- 全量字符串 OpenCC；强制专名回写：`铁柱AGI` / `小铁柱`（去掉鐵/鉄）
- `nav/footer.group`：付費答疑群（付費语义保留）
- `footer.friends`：友情連結；`note`：社群非官方…
- `changelog.tabMobile`：移動端

### en（agy 重译）
- `friends`：Friends → **Friend Links**
- `mpBtn`：WeChat OA → Official Account 「铁柱AGI」
- parts / changelog 标签更自然（User Manual / Case Studies / Our Take）
- 付费：Paid Q&A Group

### ja（agy 重译 + 专名）
- 专名：鉄柱/小鉄柱 → **铁柱AGI / 小铁柱**（汉字简体专名，不译）
- 有料Q&Aグループ；friends=リンク集；tabOurs=当サイトの解説

### ko（agy 重译 + 专名）
- 专名：철주AGI/소철주 → **铁柱AGI / 小铁柱**
- 유료 Q&A방；friends=추천 링크；tabOurs=자체 해설

### es（agy 重译）
- Grupo Q&A de pago；friends=Enlaces recomendados；chipOurs=Nuestro análisis
- 专名保持 铁柱AGI / 小铁柱

### pt-BR（agy 重译）
- Grupo pago de dúvidas；friends=Links parceiros；title=Histórico de Atualizações
- 专名保持 铁柱AGI / 小铁柱

## 专名修复摘要

| 错误形式 | 强制改回 | 命中语种 |
|---|---|---|
| 鐵柱AGI / 小鐵柱 | 铁柱AGI / 小铁柱 | zh-Hant（OpenCC 后回写） |
| 鉄柱AGI / 小鉄柱 | 铁柱AGI / 小铁柱 | ja（本轮 agy 已正确，无残留） |
| 철주AGI / 소철주 | 铁柱AGI / 小铁柱 | ko（本轮 agy 已正确，无残留） |

校验：六文件 `json.load` OK；key 结构与真源一致；bad 专名模式扫描 remaining=[]。

## group.md 抽检

| locale | 结果 |
|---|---|
| en | **PASS** |
| ja | **PASS** |
| ko | **PASS** |
| es | **PASS** |
| pt-BR | **PASS** |
| zh-Hant | **PASS** |

抽检短语：付费答疑 / 这是付费 / 加我个人 / 扫码添加 / 开通小铁柱 等 — 六语种正文与 JoinCard 插槽均无简体残留句；专名「铁柱AGI」按真源保留。未触发重译。

## 未做
- push / deploy
- Bot CloudAgent
