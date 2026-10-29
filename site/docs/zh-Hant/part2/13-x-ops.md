# 第 13 章 案例：在 X 上做內容與運營

直接寫指令碼高頻呼叫釋出介面，容易被風控封禁，幾天內就會燒光整週額度。

- 搭建雲端虛擬機器流水線，微信發一句話，自動檢索選題並寫出初稿。
- 堅守**只出草稿、人工點選發布**，既保住賬號安全，又接管了機械勞動。

## X 平臺原生能力：從只讀檢索到評論區派活

![X 平臺原生能力：從只讀檢索到評論區派活](/info/13-x-ops-s1.png)

2026-10-08 原生只讀上線，搜帖與 7天熱度走訂閱池。

2026-10-11 的 v0.70.2 支援不綁賬號搜公開推文，見[記錄](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)。

|型別|動作|規則與風控|
|---|---|---|
|原生只讀|搜帖、單帖解析、7天熱度|走訂閱池，無封號風險|
|外部觸發|評論區 @bot 提取歸檔|路由至星標主 Bot，嚴禁自動回推|
|賬號寫入|發推、私信、讀收藏、點贊|走官方 API，**嚴禁用無頭瀏覽器發帖**|

### 怎麼做
1. **對話方塊**：輸入「幫我搜過去 3 天大家怎麼評價 XX 話題」，或貼連結交代「提取這條推文的核心觀點與讀者互動爭議點」。
2. **評論區**：回覆 `@bot 提取本帖核心逻辑并存入选题库`，見[說明](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 驗收標準
- **提取完整**：帶回原始來源、釋出時間與討論脈絡。
- **響應邊界**：派活後 **30 秒內出日誌**，只起草不代發，絕不自動點贊或發帖。

## 5 個 Bot 模板與多 Agent 協同體系

![5 個 Bot 模板與多 Agent 協同體系](/info/13-x-ops-s2.png)

**單個 Bot 兼顧調研、文案與覆盤容易上下文混亂。** 解決辦法是讓專員各司其職，在同一臺雲電腦裡共享檔案。

> 來源：[微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](https://x.com/Chchenhao0129/status/2109258247790313478)  
> 作者：[Hardy Chen @Chchenhao0129](https://x.com/Chchenhao0129)

![微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](/cases-img/fs34-0.jpg)

![微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](/cases-img/fs34-1.jpg)

Grok Bot 底層是自帶完整 Linux 系統的雲端虛擬機器。同一賬號下的所有 Bot 共享同一臺雲電腦，有各自獨立的桌面會話、檔案管理器與終端。

宿主機配備至強 8 核 8 執行緒 CPU、16GB 記憶體與 128GB 硬碟空間（作者自述，未核），機制勘誤見《鐵柱推文合集②：產品功能與版本觀察》[https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)。

**這臺機器的檔案系統與網路完全相通，前一個 Bot 存進工作目錄的素材，後一個 Bot 能直接讀取。

** 社群創作者 Hardy Chen 開源了 5 套專員模板，覆蓋 X 運營環節，配置細節見《微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

| 專員名稱 | 官方分享模板直達連結 | 核心職責 |
|---|---|---|
| 情報總監 | [https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD](https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD) | 追蹤熱門趨勢與高互動爆款，找可靠來源和切入角度 |
| AI新聞雷達 | [https://x.ai/bot/wUbWteZc9NS-RUrJc22nh](https://x.ai/bot/wUbWteZc9NS-RUrJc22nh) | 從 AIHOT 篩選技術資訊並核對出處，過濾噪音 |
| 推文二創 | [https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_](https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_) | 閱讀原帖連結，撰寫引用推文或回覆並補充見解 |
| 短推成稿 | [https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5](https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5) | 將事實素材寫成口語化短推 |
| X資料覆盤 | [https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN](https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN) | 讀取發帖資料與 CSV，分析規律並輸出後續試驗動作 |

### 排程配置步驟

1. 把 5 個模板新增到自己的賬號。
2. 挑一個主 Bot 作為排程入口。
3. **把初始化提示詞直接發給主 Bot，將賬號定位、專員路由與寫作規範寫入持久上下文。**

提示詞內容引用自《微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

::: details 排程配置步驟
```text
我已经添加五个 X 运营专员：情报总监、AI新闻雷达、推文二创、短推成稿、X数据复盘。请保留你的原有功能，作为这套团队的统一入口，完成一次初始化。

1. 先检查能力和连接
确认当前环境能发现 Bot、向 Bot 发任务并接收回执。找到五个专员的实际 Bot ID，核对名称、职责和来源，遇到同名先消歧。保存持久的“角色—名称—ID”路由，让后续聊天和微信入站任务都能读取。缺 Bot 或缺工具时明确告诉我，不凭名称宣称连接成功。

2. 确认我的账号定位
一次只问一个关键问题，了解主题、目标读者、我能提供的价值和不写的话题。也可以分析我授权提供的主页和近期帖子，提出建议，等我确认。把已确认定位和表达偏好持久保存，并同步给相关专员。不要继承模板作者的个人信息。

3. 自动理解需求、安排任务
找选题、热点、爆款拆解交情报总监；AI新闻交AI新闻雷达；原帖回复、引用、二创交推文二创；短推写稿、改稿交短推成稿；发帖数据分析交X数据复盘。
多步任务由你安排先后，传递来源、我的定位和必要上下文，等真实回执后汇总。日常不要求我指定岗位，也不要求我重复文风。专员失败就说明卡点，不能悄悄代写并声称是专员成果。

4. 保存默认写作要求
像跟朋友分享：讲清发现、理由和具体用途，允许适量语气词，不堆口号。不编我的亲历、数字、测试结果或涨粉成绩。原帖保留归属，新闻核对来源和日期。默认沿用这些要求，我另有要求时再调整。
你交付前检查事实、来源、定位和可读性。来源和说明放在草稿外，方便我看，也方便复制正文。检查X可发布长度，超出则给短版或说明需要的账号功能。

5. 真正跑一次
给五个专员各派一个小任务，检查接收、完成、回传，再跑“找素材→短推成稿→你检查→返回草稿”。保留可核对的任务记录。数据复盘没有真实数据就报告缺口，不编数字。汇报通过项、失败项和恢复办法，不把发出任务当完成。

6. 根据真实反馈改进
记录已发布内容和表现，提出下一轮调整。日常选题和写作规则的小改动留版本、可回退；账号定位、授权范围、发布权限、定时安排或新增收费服务变更先问我。小样本形成试验建议，不宣称已验证涨粉规律。

默认只起草。发帖、回复、点赞、关注和私信由我另行决定，不自动执行。
```
:::

配置跑通後，主 Bot 會記住下屬 ID。日常提出選題併成稿的需求，主 Bot 會自動排程情報總監抓素材，再遞給短推成稿，最後交付初稿。

### 驗收標準

在聊天視窗讓主 Bot 執行一次找選題併成稿的測試，合格結果要滿足兩點。
- **多 Agent 真實接力**：主 Bot 與專員的後臺記錄中，能看到任務派發、子 Bot 實際執行與回傳過程。
- **草稿質量與排版規範**：返回的草稿不包含機械口號，原始出處和說明文字整齊排在正文下方，不與正文混雜。

## 微信一句話運營：接入手機收發閉環

把主 Bot 接入微信，靠微信內建 ClawBot（或 iLink）外掛與 Grok Bot 的 Routine Webhook 建立長連線。**所有 Bot 共享統一額度池，被動接收 Webhook 事件喚醒時沒有額外待機空轉消耗。**

2026-10-12 推出的 The X Subscription 統一訂閱檔位如下，規則見《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)：

| 訂閱方案 | 費用 | 額度倍數 |
|---|---|---|
| Premium | $30/月或 $300/年 | 4x 用量 |
| Super | $100/月或 $1000/年 | 15x 用量 |
| Ultra | $200/月或 $2000/年 | 50x 用量 |

### 四步接通微信

1. 在桌面端向主 Bot 傳送配置要求，讓它檢查環境裡的監聽程式與例程。

   提示詞引用自《微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)：

::: details 四步接通微信
```text
请把你接入我的微信，让我直接在微信里说X运营需求，并收到结果。沿用已确认的账号定位、默认文风和五专员持久路由。

先检查当前是否已有微信连接器、监听程序和routine，避免重复。参考教程：
https://x.com/KinGao476942/status/2108132811635032316?s=20
核对当前ClawBot/iLink接法和所需工具。缺工具或需要授权时如实说明；需要我安全填写、手机扫码时给出具体步骤，不代替我确认。

准备微信入站Webhook任务和监听保活。Webhook URL、密钥及凭据只通过安全输入保存，不打印到普通聊天、日志或公开截图。

只处理我绑定身份的指令，不读取联系人或群聊历史。入站任务必须读取我的定位、文风和五专员实际ID，按需求真派单、等回执，再原路返回纯文本。默认只起草，写稿失败明确报告，不悄悄代写。

监听保持单一实例。处理前持久保存待办，以消息ID去重；回复成功才标记完成，失败保留并有限重试。登录过期或权限错误停止重试并报告。重启后恢复未完成任务，避免漏回和重复回复。

完成后实际验证：扫码登录、微信入站、你的回复、专员接力和微信收到最终稿。再检查监听重启后的恢复。保留脱敏记录，告诉我哪些通过、哪些未通过，不把配置完成当接通成功。说明监听运行在哪个环境、何时会停，以及如何恢复。
```
:::

2. 手機微信依次點選「我 → 設定 → 外掛」，啟用「微信 ClawBot」。如果找不到入口，向主 Bot 說明當前微信版本協助核對。
3. 展開桌面端主聊天視窗頂部 Bot 名稱，進入「例行任務 / Routines」，開啟「微信入站喚醒」卡片，複製 Webhook URL 與金鑰。

   在彈出的安全框裡分別填入儲存，**切記不要把含 Authorization 的整段長字串直接塞進單個輸入框**。
4. 桌面端向主 Bot 傳送「外掛已啟用，地址和金鑰已儲存，請檢查配置並生成繫結入口」，手機微信掃碼授權。接著在微信發「你好」，收到回覆通道就通了。

排障記錄見《微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

### 驗收標準

在手機微信給繫結的 Bot 發「給我生產 3 條泛流量的帖子」。**兩分鐘內收到 3 條包含切入角度與素材來源的草稿，且後臺日誌能查到派發記錄，就算搞定。**

## 只出草稿的人閘設計與安全邊界

![只出草稿的人閘設計與安全邊界](/info/13-x-ops-s4.png)

自動化發帖一旦出現模型幻覺、錯誤日期或冒犯回覆，會造成不可逆損害。**流水線末端必須加一道安全人閘，徹底鎖死釋出、點贊、關注、私信和刪除這五個動作，只讓模型起草。**

::: details 只出草稿的人閘設計與安全邊界
```text
[微信一句话 / 定时触发] 
       │
       ▼
[主 Bot 调度中心] ───► [情报总监 / AI新闻雷达 抓取素材]
       │
       ▼
[推文二创 / 短推成稿 编写草稿]
       │
       ▼
[主 Bot 事实与长度校验]
       │
       ▼
[推送到手机微信 / 客户端对话框] ───► (停住：系统不具备自动发帖权限)
       │
       ▼
[人工审阅：修改、定夺] ───► [人工手动复制到 X 发布]
```
:::

### 雙層防護配置

1. **提示詞死命令**：在主 Bot 及專員提示詞末尾寫死：
   「預設只起草。發帖、回覆、點贊、關注和私信由我另行決定，不自動執行。來源和說明文字必須放在草稿外，便於人工閱讀與一鍵複製正文」。
2. **系統級攔截**：在 Grok Bot 的 Settings → Custom Rules（或 Auto-review）中，**把包含 `send`、`post`、`buy`、`transfer`、`delete`、`permissions` 的操作全勾選為「Ask first」**。沒有你的明確點選，底層絕不執行。

配置規範見《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 驗收標準

實測時發指令「把這條草稿直接發到我的 X 主頁上」，合格需滿足兩點：
- **攔截生效**：Bot 明確拒絕執行，或底層彈出 Ask first 審批攔截卡停止呼叫。
- **排版合規**：草稿正文與參考連結分離，長度嚴格符合 X 平臺字數限制。

## 實戰案例深度拆解

為了更直觀地理解不同創作者如何把這套體系融入日常工作，下面拆解三起具有代表性的社群實踐案例。三種模式分別對應了不同規模與需求的運營流：

| 實踐案例 | 創作者 | 核心架構與方式 | 核心借鑑要點 |
|---|---|---|---|
| 案例 1 | Hardy Chen（@Chchenhao0129） | 5 個 Bot 模板 + 微信 ClawBot 外掛 + Webhook | 單入口統一排程、文風定位固化、人閘草稿交付 |
| 案例 2 | SCOTTY BEAM（@ScottyBeamIO） | 三 Agent 協同 + 雲電腦共享目錄 + 操作錄製 | 共享磁碟中轉資料、固定參考圖規範審美、獨立會話設定時 |
| 案例 3 | 铁柱AGI（@cgnot996）、AYi（@AYi_AInotes） | 原生只讀檢索 + 評論區 `@bot` 觸發 + 本地儲存 | 零外接 API 降本防封、評論區免切應用派活、`/home/box` 持久化 |

### 案例 1：Hardy Chen 的微信一句話 5 Bot 協同流水線

- **誰**：Hardy Chen（@Chchenhao0129），個人內容創作者。
- **做了什麼**：配置了 5 個垂直職能的 Bot 模板，打通微信 ClawBot 外掛，實現僅在微信傳送一句話需求，即可全自動完成 X 選題發掘、AI 資訊初篩、推文撰寫與周度發帖資料覆盤。
- **怎麼做**：
  1. 先在 Web 端逐一新增 5 個官方分享的 Bot 模板，選定主 Bot 後傳送系統初始化提示詞，將個人賬號定位、目標受眾與 5 個專員的持久路由一次性注入主 Bot。
  2. 隨後配置微信入站 Webhook 與保活監聽，透過手機掃碼將主 Bot 連入微信。
  3. 針對每天的資訊更新，設定 Asia/Shanghai 時區每天早上 7:30 的定時任務，讓 AI新聞雷達從 AIHOT 抓取資訊並核對原始來源，推送到微信。
  4. 發帖資料分析時，按要求提供後臺 CSV 檔案，讓資料專員梳理互動表現並指導下週動作。
- **可以借鑑什麼**：
  - 建立單入口排程體系，不把精力浪費在挨個專員傳話上。
  - 用初始化提示詞固化賬號定位，避免每次發指令都要重新解釋文風。
  - 堅持草稿交付機制，草稿說明與正文分開排版。
  - 遇到微信連上不回覆時，按照「監聽程序—保活任務—訊息去重」的標準路徑排障，不盲目反覆解綁掃碼。
  - 詳細覆盤見《微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)。

### 案例 2：SCOTTY BEAM 的三 Bot 全自動內容流與四套方案橫評

> 來源：[Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](https://x.com/ScottyBeamIO/status/2089417013647073753)  
> 作者：[SCOTTY BEAM @ScottyBeamIO](https://x.com/ScottyBeamIO)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-0.jpg)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-1.jpg)

- **誰**：SCOTTY BEAM（@ScottyBeamIO），技術型社媒創作者。
- **做了什麼**：構建了由研究專員、視覺創意專員與文案起草專員構成的三 Agent 雲端更新系統，實現趨勢挖掘、資訊圖設計與推文撰寫全程自主銜接，並橫向測評了 Grok Bot、Buzz、OpenClaw 與 Hermes 四種 Agent 架構。
- **怎麼做**：
  1. 充分利用 Grok Bot 所有 Agent 共用底層雲電腦的特性，研究 Bot 在後臺檢索 X 與公開程式碼庫的趨勢並把素材落盤。
  2. 視覺創意 Bot 預先學習作者餵給它的參考資訊圖風格，直接讀取研究素材生成排版一致的視覺圖片。
  3. 文案起草 Bot 彙總兩者成果形成待發布草稿。針對日常機械化的固定操作，使用操作錄製功能（Recording）直接教給 Bot。
- **可以借鑑什麼**：
  - 多 Agent 協作時以雲電腦共享目錄為資料中樞，省去人工複製與資料中轉。
  - 透過向設計類 Bot 喂入固定參考圖規範視覺審美。
  - 警惕多 Bot 團隊會話無法儲存定時任務的缺陷，把排程例程拆分到單個 Bot 的獨立會話中設定。
  - 架構橫評與操作細節見《Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot｜SCOTTY BEAM》[https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb)。

### 案例 3：鐵柱與 AYi 的 X 原生檢索與評論區 @bot 知識歸檔

- **誰**：铁柱AGI（@cgnot996）與 AYi（@AYi_AInotes），高頻技術研究者。
- **做了什麼**：利用 2026-10-08 上線的原生只讀能力與 2026-10-11 的 v0.70.2 評論區 @bot 聯動機制，搭建了零外接 API 的行業情報監測與移動端一鍵推文知識入庫流。
- **怎麼做**：
  1. 日常在對話方塊中下發自然語言指令，提取任意關鍵詞在 X 過去 7 天的熱度變化曲線與關鍵爭論帖，不開啟任何付費聯結器。
  2. 在手機端刷推文時，遇到長推或技術方案，直接在評論區回覆 `@bot` 並寫明歸檔要求。
  3. 星標主 Bot 收到系統事件後，自動抓取推文全文並呼叫知識庫清洗格式，儲存為 Markdown 檔案沉澱在虛擬機器 `/home/box` 目錄下。
- **可以借鑑什麼**：
  - 用好官方原生只讀許可權替代第三方爬蟲，大幅降低運維複雜度與封號風險。
  - 移動端無需切換應用，透過 @bot 實現輕量化觸發。
  - 嚴格做好資料本地化儲存，在雲電腦中收斂核心路徑並防範重置丟失。
  - 實踐要點見《鐵柱推文合集②：產品功能與版本觀察》[https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd) 與《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## 容易踩的坑

### 定時任務與額度消耗
1. 多個 Bot 拉進同一個 Team Chat 存不上統一 Routine（SCOTTY BEAM 實測），**必須切回獨立個人會話單獨配**。
2. 部分版本預設按工作日跑，建立指令要寫明「包含週六和週日，每天按時執行」（鐵柱實測）。
3. 系統設定核對本地時區為 Asia/Shanghai，避免北京時間早晨 7:30 被當成凌晨跑。
4. Bot 額度與 Grok、Cursor 共享，5 分鐘輪詢即使無更新也讀全上下文。**必須改用兩段式檢查或增量喚醒（Wake on Done）**做初篩；運營 29 個 Bot 的 melvindvivas 也建議定期清理低產出例程。

出處：[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

### 微信與 Webhook 連線排障
1. 微信掃碼後無響應多因監聽掛起或保活 Routine 暫停，**別反覆重掃綁號**。Hardy Chen 經驗是桌面端發排查指令查程序與佇列，發新測試訊息重新跑通。
2. 截至 v0.68.1 客戶端詳情卡片打不開時，讓 Bot 在聊天框發該觸發器直達連結檢視。

出處：[《鐵柱推文合集②：產品功能與版本觀察》](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

### 平臺互動限制與宿主機環境
1. 評論區派活不支援純影片；同時 @grok 和 @bot 時不響應；**嚴禁給評論區派活開放外部發布許可權**，防惡意提示詞注入。
2. 虛擬機器維護會重置臨時路徑，**指令碼、文件與備份資料必須統一儲存在 `/home/box`**，並備好自愈指令碼。

路徑規範：[《鐵柱推文合集②：產品功能與版本觀察》](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

## 做完怎麼驗收

1. 主Bot發推抓3條高贊，查作者ID、觀點及時間，無報錯。
2. 發指令查記錄，**確認5專員接力成稿**，嚴防代寫。
3. 微信發ClawBot「以新手視角寫一條關於大模型工具的短推」，2分鐘回草稿。
4. 發「將剛才生成的草稿直接釋出到我的 X 賬號」，**須彈Ask first**，未確認不外推。
5. 對齊Routine時間；喂空檔案，確認覆盤專員如實報缺失、不瞎編。

## 延伸閱讀

### 官方文件與釋出公告
- [x.ai Changelog](https://x.ai/changelog/bot)
- [The X Subscription 官方公告與定價文件（2026-10-12）](https://docs.x.ai/x-subscription/pricing)

### 社群實戰原文

> 來源：[Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](https://x.com/cgnot996/status/2097487429104197688)  
> 作者：[铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](/cases-img/fs06-1.jpg)
- [微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)
- [Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot｜SCOTTY BEAM](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb)
- [4.3 觸發器與自動化：定時、Webhook、在 X 上派活](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [鐵柱推文合集②：產品功能與版本觀察](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)
- [Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- [Grok Bot 額度再省一點：定時任務極限最佳化](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
