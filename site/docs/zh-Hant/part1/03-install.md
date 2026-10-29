# 第 3 章 安裝登入與第一個 Bot

**確認訂閱含 Bot 權益**，不然沒入口；登入跳迴圈查隱私設定。別建無約束的“全能助手”白耗周配額。

1. 裝好桌面與移動端，排除登入報錯
2. **建專屬 Bot 填六行合同**
3. 派發首條落盤任務，對照清單驗收


![安裝登入與第一個 Bot](/info/03-install.png)

## 訂閱方案核對與開通條件

下載前先看賬號資格，**Grok Bot 必須繫結有效訂閱才能用**。

| 方案名稱 | 價格 | 是否包含 Grok Bot | 額度說明 |
| :--- | :--- | :--- | :--- |
| The X Plus | $8 / 月 | 否 | 僅普通模型對話，無 Bot 許可權 |
| The X Premium | $30 / 月（年付 $300） | 是 | 4x 額度，個人入門最低門檻 |
| The X Super | $100 / 月（年付 $1000） | 是 | 15x 額度 |
| The X Ultra | $200 / 月（年付 $2000） | 是 | 50x 額度 |
| Cursor Pro / Pro+ / Ultra | 見官網定價 | 是 | 依檔位提供每週額度 |
| Cursor Teams (自助席位) | 見官網定價 | 是 | 成員共享團隊配額 |

- **每月 8 美元的 Plus 檔不包含 Bot 權益**，買了用不了。
- **X 關聯額度與 Cursor 訂閱額度不疊加**，系統結算自動按每週用量更高的一方算。

方案底座機制參考社群文章 [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc) 與 [《萬文長｜Grok Bot 從零入門第一次上》](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)。

## 桌面端下載與安裝

![桌面端下載與安裝](/info/03-install-s2.png)

macOS 支援 Apple silicon（M 系列）與 Intel，Windows 和 Linux 支援 x64 與 Arm64（Win 建議開硬體加速）。

1. 登入 `cursor.com/dashboard/bot` 或直接去 `x.ai/bot` 下載安裝包。**若公司裝置無許可權，找管理員索取**。
2. macOS 把下載的應用拖進 `Applications` 資料夾，Windows 和 Linux 跑安裝嚮導。
3. **啟動客戶端看到登入介面就成了**。具體操作可參考文件 [Grok Bot 快速入門](https://cursor.com/cn/docs/grok-bot/get-started)。

## 賬號登入與隱私模式配置

1. 啟動客戶端點 **登入**，在瀏覽器直接用 Cursor 賬號認證，企業 SSO 會自動生效；如果是 Grok Business 席位，選 **Sign in with Grok** 登入。
2. 認證完成後進客戶端“設定”，能看到賬號郵箱和方案狀態就說明成功了。

**舊版隱私模式（Privacy Mode (Legacy)）必須切到現行 Privacy Mode 才能繼續**。個人使用者在彈窗點確認即可；團隊成員需要讓管理員去 Team Settings 裡更新。

詳細說明參考官方文件 [入職](https://cursor.com/cn/help/grok-bot/onboarding) 與 [登入 Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in)。

## 常見登入問題與故障排查

盲目重灌沒用，多是快取或會話重新整理問題。

1. 客戶端升至最新並重登。
2. 清 `cursor.com` 與 `x.ai` 的 Cookie 或用無痕模式。
3. 登 `x.ai/bot` 確認網頁端能建立會話。
4. 剛改訂閱**靜置等 30 至 60 分鐘**，重新整理後報錯消除。

手機驗證連錯會觸發風控鎖定，無法自愈。排查無效或遇 OAuth 報錯，**去支援頁提工單**，附郵箱與截圖，寫明版本及步驟。

詳見 [登入 Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in)。

## iOS 移動端安裝與雙端協同

### 安裝與登入
1. 系統需 **iOS 18 或更高版本**。
2. App Store 搜 Grok Bot 安裝，登入同個 Cursor 賬號自動同步，**無需重複付費**。

### 雙端分工
- 手機端適合日常監控，能看實時螢幕，支援接管控制（Take over）輸驗證碼、審批（Allow / Deny）或啟停 Routine。
- **深度操作必須回桌面端**：最長 10 分鐘錄屏教學（Teach a task）、測試 Routine（Test run）與維護雲電腦（Update / Recover）。

### 通知管理
- **單個 Bot 靜音**：聊天頁點頂部名字關閉 **Notifications**，桌面端發訊息也能關。
- **全域性關閉**：在系統“設定”中關閉 Grok Bot 的通知許可權。

詳見 [移動端 Grok Bot](https://cursor.com/cn/help/grok-bot/mobile)。

## 認識共享底座與建立第一個 Bot

![認識共享底座與建立第一個 Bot](/info/03-install-s6.png)

每個付費使用者都有一臺常駐雲端虛擬機器，配置獨立 Linux、瀏覽器、終端與持久磁碟（早期測試配置約 8 核 16GB 記憶體，未核實，具體以官方為準）。

這臺機器有三個直接影響操作的物理邊界：
- **所有 Bot 共享同一臺機器**：共用 `/workspace` 與一套瀏覽器登入態，分設 Bot 只是劃分崗位，沒有安全隔離。
- **跨 Bot 協作必須檔案落盤**：聊天記錄互不相通，Bot A 必須把產物寫進 `/workspace` 檔案，Bot B 才能讀取接力。
- **支援隨時檢視與實時接管**：右側可展開雲電腦畫面，遇到密碼、人機驗證或支付認證隨時接管，不要把憑證打在輸入框裡。

首次登入會自動生成預設的 **Grok Bot**，手動新建與設定步驟如下：

1. **新建**：點側邊欄頂部 **+**（或 Cmd+N），選 **建立新 Bot**（Create new Bot）。在輸入框先輸名字也能直接點選建立。
2. **改名與標籤**：右鍵選 **重新命名機器人**，或點頂部名稱展開面板修改。下方可設職務標籤（Label，手機端為 Title (optional)）。
3. **換頭像**：點選頂部名稱進詳情並點選頭像，支援選擇內建幾何圖形、輸入描述詞生成，或上傳 25 MB 以內的本地圖片（手機端可選相簿、生成或移除）。
4. **設職責**：**個人 Bot 已取消獨立設定頁，長期規則直接在首條訊息說明並要求它記住**。團隊 Bot 在詳情“關於”欄仍保留固定描述區。

- [更改 Bot 的名稱、頭像和職責](https://cursor.com/cn/help/grok-bot/edit-bot)
- [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

## 編寫職責：標準六行合同

### 合同結構與模板

新手別給空泛頭銜，**把六項核心約束直接寫進第一條訊息**，讓它當成長期規則記住。

1. Own（負責結果）：明確長期負責的具體指標，不做泛用助手。
2. Sources（權威來源）：限定只看官網或指定連結，禁止使用不明信源。
3. Output（交付格式）：規定儲存路徑、命名規則和摘要字數。
4. Approval（審批紅線）：發信、提交表單或刪檔案等高危操作，必須等人工彈窗批准。
5. Failure（異常兜底）：遇到網頁失效或資料缺失，必須明確標註，嚴禁腦補推測。
6. Never（絕對禁區）：禁止改動原始檔，禁止憑記憶概述，禁止點選付款按鈕。

Bot 命名好後，替換模版欄位直接傳送。

::: details 合同結構與模板
```text
请牢记你的长期工作职责，在今后的工作中始终遵循以下要求：

Own: 负责监控目标清单的每周功能与定价变动，输出结构化对比材料。
Sources: 仅限使用目标官方网站的定价页、Changelog 页面以及我通过附件提供的官方说明文档。
Output: 提炼核心动态，附带核对日期与原始出处链接，长文本与数据表格必须保存至 /workspace/research/ 下的 Markdown 文件中，对话框中只发简要完成汇报。
Approval: 涉及发送任何邮件、对外发帖、提交表单、删除文件或进行任何费用支付前，必须停下来等待我的人工批准。
Failure: 若目标页面无法访问或内容缺失，在报告中明确标注为“未取得一手数据”，严禁推测或编造任何功能与价格。
Never: 严禁修改我上传的任何源文件，在源系统可访问时严禁依赖自身训练记忆进行主观概括。

今后的工作中请记住这些要求。
```
:::

### 實踐案例

- 金塵馬在 [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee) 中，**把長期職責與單次需求嚴格分開**。

  長期規則管信源和交付，當次訊息只派具體調研主題；缺一手資料直接說明，嚴禁猜數字。
- Today 在 [《萬文長｜Grok Bot 從零入門第一次上》](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg) 中設定了安全邊界，**將只讀與有外部後果的操作隔離開**。

  每次只調研一個競品並附帶公開來源連結，分清事實與推測；涉及登入付款一律停下等確認。

演化規則參閱 [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)。

## 派發第一條真實任務

![派發第一條真實任務](/info/03-install-s8.png)

**先從小任務上手**。寫任務記好 5 要素：講清目標與輸入，嚴格只讀（禁改原始檔、註冊與支付），定好落盤規格，標明接管節點。

附件總結髮：
```text
用五个要点总结这份文档。
在单独的部分列出每个日期、决策和未解决的问题，并为每项注明对应章节出处。
不要更改源文件。
```

查競品定價落盤發：
::: details 派發第一條真實任務
```text
【目标】
调研 3 款主流代码编辑器（Cursor、VS Code、Zed）在 2026 年的最新公开定价方案与核心 AI 功能，产出一份选型对比参考材料。

【材料】
1. 仅限使用上述三款产品官方网站的定价页、功能介绍页与官方文档；第三方博客仅作为辅助索引，必须找到官方页面核实。
2. 记录每一项数据的原始官方 URL 与数据核对日期。

【边界】
1. 纯只读检索，严禁注册任何账号，严禁开启任何试用，严禁输入任何支付信息。
2. 遇到需要登录才能查看的页面，直接跳过并记录在未核实清单中。
3. 严禁改动 /workspace 下已有的其他项目文件。

【交付规格】
1. 在 /workspace/editor-research/ 目录下生成对比报告文件 comparison.md。
2. 报告内包含一张 Markdown 数据表格，表头列定义为：产品名称、方案档位、月付价格、年付价格、核心功能特征、官网来源链接、核对日期。
3. 表格下方附带一份 400 字以内的中文总结，指出各产品主要差异，并单独开辟一节列出“未核实或存在矛盾的信息”。
4. 对话框中仅需回复已完成落盘的简短提示及文件绝对路径。

【暂停确认节点】
1. 遇到必须登录、验证码拦截或点击付费的操作时，立刻停下并提示我接管。
2. 官网信息前后出现明显矛盾且无法核实时，停下说明情况由我判断。
```
:::

遇登入、2FA 或滑塊驗證時：
1. **點 Take over 手動處理**，弄完點 I'm done 繼續，跳過點 Skip。
2. 跑完**確認 `/workspace/editor-research/comparison.md` 完整儲存**。

規範見 [使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started) 與 [入職](https://cursor.com/cn/help/grok-bot/onboarding)。

## 容易踩的坑

1. 8 美元 Plus 檔沒 Bot，**必須選每月 30 美元的 Premium 檔**。
2. 所有 Bot 共享雲電腦與配額，先跑通一個，別建十幾個互相打架。
3. 別在聊天框發密碼或 API Key，用 Take over 接管輸入或填安全卡片。
4. 長文字**一律存入 `/workspace` 的 Markdown 檔案**，防汙染上下文。
5. 登入報錯別重灌，清理 `cursor.com` 和 `x.ai` 的 Cookie，或等 30 至 60 分鐘。
6. **不同 Bot 共享虛擬機器和瀏覽器會話**，不能隔離許可權。
7. Teach a task、Test run 和系統恢復是桌面端獨有，iOS 端沒有。

## 做完怎麼驗收

1. 進 Usage & Billing，付費檔有效、用量正常。
2. 桌面端右屏能拉起，無 Reconnecting 報錯。
3. iPhone（iOS 18+）登相同 Cursor 賬號，無二次購買提示。
4. 發六行合同，Bot 明確回覆已記住長期規則。
5. 雲電腦 `/workspace` 按指令生成目標檔案。
6. 遇登入等操作，Bot 主動暫停並彈 **Action needed** 卡片。
7. 故意喂死鏈，報告明確標註 **未取得一手資料**、不瞎編。

## 延伸閱讀

### 相關章節

- [第 4 章 交代任務：訊息、附件與一次好的交接](/part1/04-handoff)
- [第 25 章 常見問題與排錯](/part4/25-faq)

### 官方頁面
- [Grok Bot 快速入門 (Get Started)](https://cursor.com/cn/docs/grok-bot/get-started)
- [入職 (Onboarding)](https://cursor.com/cn/help/grok-bot/onboarding)
- [登入 Grok Bot (Sign In)](https://cursor.com/cn/help/grok-bot/sign-in)
- [移動端 Grok Bot (Mobile)](https://cursor.com/cn/help/grok-bot/mobile)
- [更改 Bot 的名稱、頭像和職責 (Edit Bot)](https://cursor.com/cn/help/grok-bot/edit-bot)

### 社群實戰
- [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
- [《萬文長｜Grok Bot 從零入門第一次上》](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)
