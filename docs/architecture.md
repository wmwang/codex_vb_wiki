# 架構藍圖

## 核心元件

1. **來源擷取 (Ingestion)**
   - 來源：原始碼、規格、DB schema、批次作業、維運文件。
   - 抽取器：語法解析 + 規則式，輸出 inventory。
2. **內容生成 (Authoring)**
   - 依模板生成初稿。
   - LLM 補齊摘要、流程、依賴、錯誤處理等。
3. **索引與查詢 (Indexing & Query)**
   - 結構化索引：模組、依賴、流程、錯誤碼。
   - 向量索引：摘要與長文段落。
4. **展示與治理 (Delivery & Governance)**
   - Wiki UI + 搜尋/問答。
   - RBAC、審核流程、稽核記錄。

## 生產級關鍵點

- 可觀測性：Log/Metrics/Trace
- 安全：SSO + RBAC + 敏感資訊遮罩
- 可用性：多節點 + 備援 + 災難復原策略

