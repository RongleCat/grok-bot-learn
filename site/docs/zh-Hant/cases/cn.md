# 中文長文精選

用 Grok Bot 跑業務流，常踩的坑主要是**賬號繫結、本地與雲端搞混、許可權越界以及例程空跑**，還要防著驗證碼、介面失效和額度消耗。要是多角色職責沒拆清，Bot 還會互相搶佔上下文。

這裡整理了社群實測跑通的 **15 篇長篇實踐**，覆蓋入門起步、自媒體運營、工程研發、電商生活和組織編排五大模組，可以直接對照查閱。

| 主題分類 | 文章標題 | 核心業務場景 | 關鍵機制與工具 |
| :--- | :--- | :--- | :--- |
| 入門與基礎 | 《萬文長｜Grok Bot 從零入門第一次上》 | 賬號開通與首條任務合同 | Linux 雲電腦、Take over 接管、Skill 沉澱 |
| 入門與基礎 | 《如何在一個小時內深入使用 Grok Bot》 | 規範化巡檢與做事方法固化 | 驗收標準編寫、Teach a task 錄製、例程去重 |
| 入門與基礎 | 《10 條必備經驗，讓你的 Grok Bot 變得更好用》 | 多 Bot 環境治理與防中斷 | 收件箱分流、CLI 排程、Wake on Done、App Nap 禁用 |
| 自媒體運營 | 《用Grok Bot搭建自媒體團隊：保姆級教程》 | 5 崗位全流程內容流水線 | 7 層共享目錄、voice.md 約束、全鏈路人工閘 |
| 自媒體運營 | 《做自媒體怎麼用好 Grok bot》 | 結構化選題庫與爆款拆解 | HKRR 框架、6 組硬欄位校驗、Notion 狀態流轉 |
| 自媒體運營 | 《如何把 Grok Bot 接入你的微信？》 | 移動端日常指揮入口打通 | 微信 ClawBot 外掛、iLink 長輪詢、Webhook 喚醒 |
| 自媒體運營 | 《把自己的推文做成個人畫像網站》 | 歷史發帖提煉與網站生成釋出 | 4 角色檔案流轉、原文依據核對、靜態站點生成 |
| 自媒體運營 | 《微信裡說一句，就能運營X》 | 5 專員路由與一句話微信分發 | 角色持久路由、主 Bot 排程、失敗不代寫 |
| 工程研發 | 《工程師如何用好 Grok bot?》 | 迷你研發艦隊與持續審查 | 5 研發 Bot + 1 運營 Bot、Notion 資料庫、截圖閉環 |
| 工程研發 | 《一天幾百個 PR 有什麼意義？》 | 多線併發研發與分級程式碼審查 | 九類工作拆解、PR 風險分級放行、工程 Harness |
| 電商與生活 | 《Grok Bot 應用指南實操案例》 | 閒魚資料板與圖文多場景交付 | 真實成色隔離、SVG 原始檔、可互動 HTML 資料板 |
| 電商與生活 | 《用 Grok Bot 做跨境電商的實戰分享》 | 亞馬遜買家視角前臺運營 | 買家號登入、Alexa 問答調研、調價待批清單 |
| 團隊與組織 | 《萬字長文｜Grok Bot 從入門到精通》 | 從單兵崗位到電商運營矩陣 | 崗位說明書八要素、/workspace 交接、審批規則 |
| 團隊與組織 | 《從一個 Bot 到一整個組織》 | 本地 Agent 資產遷移與 1+N 架構 | 本地 Skill 匯入、飛書 CLI、GBrain 知識庫 |
| 團隊與組織 | 《零基礎搭建全自動化Agent團隊》 | 爆款多平臺採集與全天候協作 | 關鍵詞成功率回溯、反向訪談提示詞、飛書多維表格 |

搭建前先把下面這段提示詞發給主 Bot，**讓它協助梳理崗位邊界與執行目錄**。

```text
我打算参考以下业务场景搭建一套 Grok Bot 工作流：【填入具体业务目标】。
请按以下步骤帮我拆解：
1. 列出该流程所需的 Bot 岗位清单，明确每个角色的输入文件、交付成果和绝对禁止动作。
2. 在 /workspace 下为我规划一套清晰的目录结构，规定上下游交接的文件格式。
3. 标出涉及外部发信、数据修改、敏感登录或支付的环节，单独列出必须等待人工审批的节点清单。
4. 给出该流程第一步的测试提示词，明确要求未确认信息标注为待确认，严禁编造数据。
```

## 入門上手與基礎機制

### 萬文長｜Grok Bot 從零入門第一次上

> 來源：[萬文長｜Grok Bot 從零入門第一次上](https://x.com/TodayKan/status/2104789484277473522)  
> 作者：[Today🦘 @TodayKan](https://x.com/TodayKan)
桌面端繫結入口只在初始頁出現，**繫結後無法遷移**。遇到網頁登入，直接用 **Take over 手動輸入密碼**接管。

長期規則寫進描述，臨時要求放對話。沒提供的資訊標為待確認，切斷瞎猜習慣。

寫第一條任務要理清這五項。
- 目標與材料
- 邊界與交付
- 人工確認節點

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)

### 如何在一個小時內深入使用 Grok Bot

> 來源：[如何在一個小時內深入使用 Grok Bot](https://x.com/tspy/status/2109440690862342187)  
> 作者：[yishan @tspy](https://x.com/tspy)

![如何在一個小時內深入使用 Grok Bot](/cases-img/fs33-0.jpg)

![如何在一個小時內深入使用 Grok Bot](/cases-img/fs33-1.jpg)
巡檢任務統一在 `/workspace/site-check/` 儲存報告。報告必須記下連結和檢查時間，存下截圖證據，並把頁面事實與推測分開。

固化日常技能按兩步走。
1. 用 Teach a task 錄製瀏覽器操作生成草稿。
2. 人工補齊缺失資料處理和審批邊界。

平時巡檢堅持**無新異常只存記錄不彈通知**，省額度也避免通知疲勞。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)

### 10 條必備經驗，讓你的 Grok Bot 變得更好用

> 來源：[10 條必備經驗，讓你的 Grok Bot 變得更好用](https://x.com/eze_is_1/status/2109850538045264151)  
> 作者：[一澤Eze @eze_is_1](https://x.com/eze_is_1)

![10 條必備經驗，讓你的 Grok Bot 變得更好用](/cases-img/fs37-0.jpg)

![10 條必備經驗，讓你的 Grok Bot 變得更好用](/cases-img/fs37-1.jpg)
**所有 Bot 共用同一臺雲電腦，單靠新建 Bot 無法實現許可權隔離**。邏輯固定的定時監測任務，改用純指令碼或命令列承接更省額度。

長任務可以用 Webhook 配合 Wake on Done 喚醒。分流用收件箱 Bot 當總閘，按型別分配給對應角色。

本地休眠會導致例程斷連，**修改 macOS 的 pmset 並關閉 App Nap** 就能解決。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)

## 自媒體運營與個人 IP

### 用Grok Bot搭建自媒體團隊：保姆級教程｜Adrian Punk

> 來源：[用Grok Bot搭建自媒體團隊：保姆級教程](https://x.com/AdrianPunk115/status/2097311704547987756)  
> 作者：[Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![用Grok Bot搭建自媒體團隊：保姆級教程](/cases-img/fs26-0.jpg)

![用Grok Bot搭建自媒體團隊：保姆級教程](/cases-img/fs26-1.jpg)

在雲電腦 `/workspace/content-team/` 建 7 層目錄，5 位專員按流水線順次流轉。

1. 情報偵察員
2. 選題策劃師
3. 內容主筆（**寫作只能依賴已批准的 Brief 和 `voice.md`**）
4. 事實編輯
5. 資料覆盤師

安全上設定嚴格紅線，**全鏈路必須人工把關**。

- 設定中直接關閉本地電腦執行許可權
- 每個 Bot 描述焊死要求，嚴禁擅自發帖、點贊與回覆
- 賬號釋出鍵與敏感登入全部鎖死在人工環節

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### 做自媒體怎麼用好 Grok bot｜Kin

> 來源：[做自媒體怎麼用好 Grok bot](https://x.com/KinGao476942/status/2099736121781764594)  
> 作者：[Kin @KinGao476942](https://x.com/KinGao476942)
適合帶產品找冷啟動流量、常缺選題的創作者。

1. 用 Bot 建立 Notion 選題庫，配齊六組硬欄位（來源永久鏈、公開資料和作者分層，以及適合理由、動機拆解與缺失標註）。**找不到資料必須標註「未找到」**。
2. 按 HKRR 框架解構爆款，重點拆解快樂、知識，以及共鳴和節奏感四個維度。
3. **只借鑑傳播結構而不照搬文字**，最終釋出鍵死死控在自己手中。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### 如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）｜Kin

> 來源：[如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）](https://x.com/KinGao476942/status/2108132811635032316)  
> 作者：[Kin @KinGao476942](https://x.com/KinGao476942)

![如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）](/cases-img/fs29-0.jpg)

![如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）](/cases-img/fs29-1.jpg)

想在手機隨時排程雲電腦 Agent，用微信 ClawBot 外掛就能打通，**部署只需三步**：
1. 把整理好的提示詞發給主 Bot。
2. Bot 在雲電腦透過 iLink 協議寫指令碼，建好「微信下旨入口」Webhook。
3. 在加密彈窗填金鑰並掃碼繫結。

通訊與容錯按這三條標準驗收：
- 走出站長輪詢，**免公網 IP 和內網穿透**。
- 嚴格限制 Bot **僅純文字回復**。
- 提示詞預設 **錯誤碼 -14 自動重連**。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)

### 把自己的推文做成個人畫像網站, 用 Grok Bot 從分析特點到上線分享保姆級教程

> 來源：[把自己的推文做成個人畫像網站,  用 Grok Bot 從分析特點到上線分享保姆級教程](https://x.com/0xlangeai/status/2109115005069341175)  
> 作者：[藍哥AI @0xlangeai](https://x.com/0xlangeai)

![把自己的推文做成個人畫像網站,  用 Grok Bot 從分析特點到上線分享保姆級教程](/cases-img/fs32-0.jpg)

![把自己的推文做成個人畫像網站,  用 Grok Bot 從分析特點到上線分享保姆級教程](/cases-img/fs32-1.jpg)
在專案群聊拉入四個 Bot，**透過共享雲電腦裡的 Markdown 檔案接力流轉**：

1. 推文整理員抓取近 90 天內容存為 `tweets.md`。
2. 畫像分析師提煉 3 到 5 個特點寫入 `profile.md`。
3. 設計師提供雙欄排版方案 `design.md`。
4. 工程師編寫程式碼並反饋多端預覽。

**分析師每個風格判斷都必須附帶推文原文連結與時間戳**，每個節點由人工校正偏差後再放行。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### 微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了

> 來源：[微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](https://x.com/Chchenhao0129/status/2109258247790313478)  
> 作者：[Hardy Chen @Chchenhao0129](https://x.com/Chchenhao0129)

![微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](/cases-img/fs34-0.jpg)

![微信裡說一句，就能運營X：我的 5 個 Bot 模板公開了](/cases-img/fs34-1.jpg)
這套玩法打通了微信 ClawBot 外掛，微信發一句話，主 Bot 就能自動分派任務並回傳短推草稿。

5 套 Bot 模板覆蓋全鏈路。
- 情報總監
- AI新聞雷達
- 推文二創
- 短推成稿
- X 資料覆盤

1. **路由分發邏輯完全封裝在主 Bot 內部**，用初始化提示詞記錄賬號定位與專員 ID。
2. **專員任務卡死必須如實報告失敗原因，嚴禁主 Bot 私自代寫冒充**。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)

## 工程研發與程式碼協同

### 工程師如何用好 Grok bot?

> 來源：[工程師如何用好 Grok bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> 作者：[Kin @KinGao476942](https://x.com/KinGao476942)

![工程師如何用好 Grok bot?](/cases-img/fs25-0.jpg)

![工程師如何用好 Grok bot?](/cases-img/fs25-1.jpg)

SpaceXAI 團隊配置了 5 個研發 Bot（分管移動端、桌面端與 CI/CD 基建 Harness）與 1 位負責開會覆盤的運營 Bot Jenny。

1. **自動排查**：Bot 自主調起 Cloud Agent，**每 30 分鐘輪詢共享 Notion 資料庫**排查 CI 報錯與合併衝突。
2. **分級放行**：**高置信小改動自動合併，疑難問題交人工複核**。
3. **閉環驗收**：強制要求交付改動前後的真實對比截圖。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)

### 一天幾百個 PR 有什麼意義？

> 來源：[一天幾百個 PR 有什麼意義？我照著 SpaceXAI 工程師 Lauren（@poteto）的九類清單，把自己的活拆了一遍](https://x.com/MaiYangAI/status/2108519046446727633)  
> 作者：[Mai Yang @MaiYangAI](https://x.com/MaiYangAI)

面對單日合併上百個 PR 的爭議，工程師把活拆成了涵蓋效能、Bug 修復、重構、工具鏈與新特性的九類清單。

平時別盲目刷提交數，**要把精力放在輸入約束與輸出校驗兩端**。作者開發 ContextEcho 時，半年 1020 次提交也只有 18 次 PR。

改動放行按風險等級分流，杜絕虛榮指標。

| 改動風險級別 | 審查與放行機制 | 人工與 Agent 職責分工 |
| :--- | :--- | :--- |
| 低風險任務 | 結合測試用例放行 | 由程式碼審查 Agent 自動稽核放行 |
| 核心與高風險任務 | 人工把關定方向 | 人工負責定方向、定驗收標準和實際體驗 |

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## 電商經營與日常實操

### Grok Bot 日常實操案例｜Miles Ma

> 來源：[Grok Bot 應用指南實操案例：閒魚上架、小紅書做圖、找工具、做短影片、整理收藏](https://x.com/miles_mazy/status/2098708209095819605)  
> 作者：[Miles Ma @miles_mazy](https://x.com/miles_mazy)

![Grok Bot 應用指南實操案例：閒魚上架、小紅書做圖、找工具、做短影片、整理收藏](/cases-img/fs27-0.jpg)

![Grok Bot 應用指南實操案例：閒魚上架、小紅書做圖、找工具、做短影片、整理收藏](/cases-img/fs27-1.jpg)
作者把交付升級成網頁資料板和向量圖，跑通了 5 個場景。
- 閒魚：拆開真實成色與官網引數，給帶補圖清單的雙欄資料板。
- 小紅書：批次做 6 張同色卡片，交 SVG 原始檔。
- 影片：做可互動魔方網頁，錄剪為 51 秒帶配音短片。
- 收藏：把推文轉成 Markdown 素材庫。

想防翻車，**提示詞裡必須強制約定「未提供的資訊一律標為待確認」**，成色才不會被誇大。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/TV5UwDLTIiTT4vkpY8qcm33fnSf)

### 用 Grok Bot 搭建亞馬遜團隊｜Zach

> 來源：[用 Grok Bot 做跨境電商的實戰分享，從 0 到 1 搭建起一整個亞馬遜團隊](https://x.com/1999Zach22/status/2110078772225667115)  
> 作者：[Zach @1999Zach22](https://x.com/1999Zach22)

![用 Grok Bot 做跨境電商的實戰分享，從 0 到 1 搭建起一整個亞馬遜團隊](/cases-img/fs38-0.jpg)

![用 Grok Bot 做跨境電商的實戰分享，從 0 到 1 搭建起一整個亞馬遜團隊](/cases-img/fs38-1.jpg)
商業介面資料滯後，作者用雲電腦瀏覽器登買家號，搭出**「1 船長 + 12 崗位」**架構，日常只跟船長對接。

巡檢 Bot 每天模擬買家跑這幾項。
- 檢查 Listing 變體與主圖
- 監控競品價格
- 向前臺 Alexa for Shopping 提問摸推薦邏輯

許可權底線是**明令禁止廣告 Bot 寫入後臺或改出價**，調價與刊登全走待批清單人工確認。

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/LG1twK03uiO00JkPk1ncQQNUnvt)

## 團隊編排與組織協同

### 漸進擴編

> 來源：[萬字長文｜Grok Bot 從入門到精通](https://x.com/jinchenma_ai/status/2094984812251746424)  
> 作者：[金塵馬 @jinchenma_ai](https://x.com/jinchenma_ai)

![萬字長文｜Grok Bot 從入門到精通](/cases-img/fs24-0.jpg)

![萬字長文｜Grok Bot 從入門到精通](/cases-img/fs24-1.jpg)
兩名 Bot 借 `/workspace` 傳檔案。崗位說明書定好八項要素，明確負責結果、工作步驟與驗收標準，設好人工審批點。**防過早設空崗**，擴編分三步：
1. 單任務跑通
2. 沉澱為技能
3. 分工穩定建新 Bot

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

### 接駁分層

> 來源：[從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來](https://x.com/1999Zach22/status/2109607405696983158)  
> 作者：[Zach @1999Zach22](https://x.com/1999Zach22)

![從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來](/cases-img/fs35-0.png)

![從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來](/cases-img/fs35-1.jpg)
本地 Claude/Codex 用 Plan 模式磨好 SOP 同步雲電腦。**推「1+N」單入口**防群聊燒 token；飛書 CLI 交付批註；接 GBrain 知識庫。關鍵動作以待批清單收尾：

| 業務型別 | 模型級別 |
| :--- | :--- |
| 基礎清洗與排版 | 預設模型 |
| 核心戰略歸因 | 高階模型 |

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)

### 自動化流水線

> 來源：[零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】](https://x.com/xilo2991/status/2109613437215293905)  
> 作者：[xilo @xilo2991](https://x.com/xilo2991)

![零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】](/cases-img/fs36-0.jpg)

![零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】](/cases-img/fs36-1.jpg)
主 Bot 反向訪談定配置。**後臺跑粗活、人工錯位批次審**保穩定。24 小時流水線分四步走：
1. 梳理檢索與落庫
2. 模擬檢索小紅書、B站和 YouTube
3. 關鍵詞周度淘汰入多維表格
4. 補齊選題與撰稿

[閱讀原文](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
