# 第 16 章 案例：知識自動入庫與微信打通

手機收藏容易亂，群檔案老過期，人在外頭也使不上雲端 **7×24 小時** 跑著的 Grok Bot。

1. 網頁與短影片：用 Webhook 配 iOS 快捷指令，**一鍵結構化入庫**。
2. 截圖與錄音：微信轉發帶不出附件，**走公網臨時中轉**匯出來。
3. 對話排程：用官方「微信ClawBot」外掛走長輪詢，**在微信視窗直接排程 Grok Bot**。

## 三種自動化方案的能力與邊界對照

![三種自動化方案的能力與邊界對照](/info/16-knowledge-s1.png)

| 方案與場景 | 機制與鑑權 | 坑點 |
| :--- | :--- | :--- |
| 單向入庫（網頁、公眾號與短影片） | 快捷指令帶 Bearer 金鑰向 Webhook 發 POST 入庫 | 僅單向接收 |
| 多模態入庫（微信記錄、錄音、截圖多圖） | 文字直傳；檔案走 filebin.net 臨時網盤生成公網連結，Bot 解壓入庫 | **網盤無密碼勿傳敏感內容**；大包抽幀多耗 token |
| 微信雙向（發指令、查資料、排程 Bot） | 微信掃碼繫結，iLink 配合雲端指令碼監聽並轉 Webhook 回推純文字 | **需控制頻次防空轉消耗** |

自 2026-10-12 起統一為 The X Subscription，均按次扣每週配額。

**$8/月的 Plus 檔不含 Grok Bot**，需選 Premium（$30/月或 $300/年，4x 額度）、Super（$100/月或 $1000/年，15x 額度）或 Ultra（$200/月或 $2000/年，50x 額度）。

細節見官方[方案和計費](https://cursor.com/cn/help/grok-bot/plans)。

## 案例一：Webhook 與快捷指令構建知識自動入庫流水線

![案例一：Webhook 與快捷指令構建知識自動入庫流水線](/info/16-knowledge-s2.png)

**方案把抓取、音影片轉錄與總結全放在 Grok Bot 雲端，手機只發 URL 觸發。

** 铁柱AGI（@cgnot996）借[例程](https://cursor.com/cn/help/grok-bot/routines)的 Webhook 實現了發請求即刻啟動。

### 搭建步驟
1. 桌面端 Details 找到 Routines。讓 Bot 建立解析任務，**妥善儲存生成的 Webhook URL 與 key**。
2. 新建快捷指令“傳送給知識庫 Bot”，新增“獲取 URL 內容”並按表配置引數。

| 引數 | 設定值 |
|---|---|
| URL | Webhook 地址 |
| 方法 | POST |
| 頭部 | 鍵名 `Authorization`，值 `Bearer <key>` |
| 請求體 | 選 JSON，添入“快捷指令輸入” |

3. **針對封閉應用加裝輔助輸入框**。微信常禁用分享面板，需建第二條指令（“從選單中選取”加“請求文字”）中轉，繫結到 iPhone 操作按鈕，按鍵即可貼上傳送。

### 驗收標準
> 來源：[Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](https://x.com/cgnot996/status/2097487429104197688)  
> 作者：[铁柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](/cases-img/fs06-1.jpg)
點分享後，**幾秒內桌面端狀態會轉為執行中**。任務完成後，知識庫會自動生成標準化條目。
- 影片 ID 或網頁原始短鏈
- 雲端儲存路徑與關聯知識頁
- 核心提煉要點與作者標籤
- 單次解析消耗的積分成本

收錄《2026 我的 Obsidian 完整分享》等長文時能自動回鏈。

實測演示見[《Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)。

## 案例二：微信聊天記錄與多模態素材打通入庫

### 案例概況
- 微信合併轉發打包傳 Grok Bot 自動解壓出回執。
- **用 filebin.net 作跳板**排除本地路徑依賴。
- Mac 與 iPhone 部署 **五種收錄模式**快捷指令。

### 是什麼：為什麼需要引入臨時網盤中轉

跨裝置讀不到本地盤，微信大 ZIP 塞進請求體容易超時。

1. 文字直接走 JSON 傳送。
2. 圖片、錄音和 ZIP 先傳 filebin.net，再把連結發給 Bot 下載。
3. 圖床 ID 必須用**至少 8 位隨機字母數字**，防止撞名洩露。
4. 檔案預設存 7 天且未加密，**嚴禁傳隱私和商業機密**。

### 怎麼做：分步搭建步驟

#### 1. 配置 Webhook
在桌面端主會話發這段提示詞：

```text
帮我创建一个 Webhook 触发的例行任务。快捷指令会用 POST 请求发来一个 JSON，里面只有一个字段 info。info 可能是我输入的文字，也可能是一个文件下载链接，比如微信聊天记录压缩包、截图、录音。收到后：如果是链接就先下载文件再读取，压缩包先解压；然后整理出要点，收录进知识库，最后给我一份回执，写清楚收录了什么、存在哪里。
```

**傳送後在 Bot“例程”中記錄 Webhook URL 和 key。**

#### 2. 配置快捷指令
匯入連結：`https://www.icloud.com/shortcuts/2b77155d7c744110a0f0f9ef1bdc42bf`
編輯“【分享版】傳送給知識庫 Bot”，填入 URL、key 與**至少 8 位的複雜圖床 ID**（如 kb7x9m2q），標頭內建無需修改。

#### 3. 微信記錄收錄
- **Mac 端**：合併轉發到其他應用選該指令，點接收轉發；ZIP 傳網盤推連結，Bot 隨即處理。
- **手機端**：合併轉發選該指令點接收轉發；可在“編輯操作”固定到常用區。

#### 4. 獨立呼叫與採集
Mac 用 Raycast 或選單欄，手機綁操作按鈕。
- 截圖/錄音：確認或錄完傳網盤推連結。
- 輸入文字：**直接放進 JSON 傳送**，不經網盤。
- 選圖補充：選圖後輸說明，打包上傳。
- 接收轉發：未接收內容時讀剪貼簿傳送。

### 做到什麼程度算好

> 來源：[微信聊天記錄打通 Grok Bot：快捷指令進階版](https://x.com/cgnot996/status/2107039351519707602)  
> 作者：[铁柱AGI @cgnot996](https://x.com/cgnot996)

![微信聊天記錄打通 Grok Bot：快捷指令進階版](/cases-img/fs11-0.png)

![微信聊天記錄打通 Grok Bot：快捷指令進階版](/cases-img/fs11-1.jpg)

傳送後等幾秒到十幾秒，Bot 返回**標準化回執**：
- **群聊歸檔**：提取討論核心論點，給筆記與壓縮包路徑。
- **資源建檔**：發 13 個網站，自動分類建索引並給知識庫連結。

操作見[《微信聊天記錄打通 Grok Bot：快捷指令進階版》](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb)。

## 案例三：將 Grok Bot 直接接入微信進行雙向排程

![案例三：將 Grok Bot 直接接入微信進行雙向排程](/info/16-knowledge-s4.png)

### 案例概況
Kin 把 Grok Bot 接進微信，**手機發訊息即可遙控雲端 Bot**。

1. 讓 Grok 調 iLink 寫長輪詢指令碼
2. 建 Webhook 接收指令
3. 微信開「微信ClawBot」掃碼繫結

走純出站長輪詢，**無需開放公網埠**。

### 是什麼：微信ClawBot 與 iLink 長輪詢機制

方案走官方「微信ClawBot」外掛與 iLink 介面（`ilinkai.weixin.qq.com`），不改客戶端記憶體，**不存在封號風險**。

通訊全是出站請求，**無需開放公網埠**：
1. Grok Bot 後臺調 `getupdates` 輪詢拉取訊息，處理完畢調 `sendmessage` 回覆。
2. Webhook 接收文字後交接給各專職 Bot 協同執行，詳見文件[使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work)。

### 怎麼做：手把手操作步驟與完整提示詞

1. 電腦端主會話發提示詞，等它建好「微信下旨入口」例程。
::: details 怎麼做：手把手操作步驟與完整提示詞
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
2. 複製例程的 URL 和 key。**嚴禁在對話方塊發明文**，填入機密卡片並顯示“已安全儲存並保持私密”即可，見[安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets)。
3. 微信版本需在 **iOS 8.0.70 / Android 8.0.69 以上**。在“我”->“設定”->“外掛”啟用紅龍蝦圖示「微信ClawBot」。
4. 傳送“外掛開好了”，微信掃碼授權（二維碼 **5 分鐘有效**，超時用備用連結）。
5. **必須在微信主動發第一句話**（如“你好”）。介面需藉此截獲 `context_token` 建連，發完通道即正式就緒。

### 做到什麼程度算好

> 來源：[如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）](https://x.com/KinGao476942/status/2108132811635032316)  
> 作者：[Kin @KinGao476942](https://x.com/KinGao476942)

![如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）](/cases-img/fs29-0.jpg)

![如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）](/cases-img/fs29-1.jpg)

在微信測這四條，看**有沒有跑通**：
1. 發“你好”，**秒回純文字**確認。
2. 調推特專家 Bot，微信直接出選題清單。
3. 發影片連結調下載專家 Bot，回傳清洗文字。
4. 桌面端同步核對所有指令與記錄。

實操與截圖見[《如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)。

## 容易踩的坑

1. 轉發前**必須在本地點選下載附件**，否則匯出的 ZIP 只有佔位文字。
2. filebin.net 無密碼，別用 `test` 或 `123456`，**必須設 8 位以上隨機字串**，禁傳身份證、銀行卡與涉密合同。
3. 配 Webhook 別在聊天框貼 key，**用安全卡片儲存**；共享指令前清空個人 key 和 URL。
4. ClawBot 二維碼 5 分鐘失效，無響應或報 `-14` 說明**憑證過期，需重新生成掃碼**。
5. 雲電腦 Reset 或重啟後 Python 輪詢會掛，微信沒回復就去桌面端**讓 Bot 重新拉起指令碼**。
6. 微信不渲染 Markdown，**在 Instruction 強制純文字回復**，避免輸出 `**` 或 `#`。
7. **別同時跑多個 OpenClaw 監聽**，防 iLink 佇列搶訊息漏接指令。
8. The X Subscription 扣每週配額，**高頻觸發必須加過濾**，跑太快就暫停非必要例程或放寬條件。

## 做完怎麼驗收

1. **測 Webhook**：髮帶 `Authorization: Bearer <key>` 的 POST 請求。**返回 200 算搞定**，401 是金鑰錯，404 是 URL 錯。電腦端“例程”狀態變 Running… 且有日誌就行。
2. **測快捷指令**：發文字測幾十秒內出不出回執，轉發 2 張圖測歸檔。截圖必須彈授權預覽，點允許才傳。
3. **測微信與同步**：給「微信ClawBot」發訊息，**5 秒內收到回覆**算通。再去電腦端看眼，聊天記錄同步了就算徹底跑通。

## 延伸閱讀

### 官方文件
- [例程](https://cursor.com/cn/help/grok-bot/routines)
- [安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets)
- [使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- [方案和計費](https://cursor.com/cn/help/grok-bot/plans)

### 社群實戰原文
- [《Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- [《微信聊天記錄打通 Grok Bot：快捷指令進階版》](https://jcng5q8n0f3z.feishu.cn/wiki/IwrfwYt1ti0aDWk3YEdcGyQRnUb)
- [《如何把 Grok Bot 接入你的微信？保姆級新手指南來了（附詳細提示詞）｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/LehUwOhxAijkigkkVlDclVVunQg)
