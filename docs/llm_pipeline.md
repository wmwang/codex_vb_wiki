# LLM 輔助流程

## 輸入
- 原始碼（VB 模組、類別、表單）
- 系統規格、變更單、批次作業定義
- 監控/告警與維運文件

## 輸出
- Wiki 模板內容（Markdown）
- Speaker 規格輸出（YAML/JSON）

## Pipeline
1. **抽取 (Extract)**
   - 解析函式、類別、參數與相依資訊。
2. **標準化 (Normalize)**
   - 依 `docs/templates` 產生草稿。
3. **補齊 (Enrich)**
   - LLM 生成摘要、流程與錯誤處理建議。
4. **審核 (Review)**
   - 依 `docs/governance.md` 完成人工審核。
5. **發佈 (Publish)**
   - 同步至 Wiki 與 Speaker 輸出。

## 注意事項
- LLM 建議需有人工校對。
- 針對敏感資訊可用遮罩或簡化描述。

