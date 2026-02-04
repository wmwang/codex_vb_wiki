# 開發者手冊（Developer Manual）

## 1. 目的
提供開發與維運人員了解專案架構、擴充方式、與產出規範。

## 2. 專案結構摘要
- `scripts/`：抽取與生成工具
- `docs/templates/`：內容模板
- `speaker/`：Speaker 規格與範例
- `samples/`：示範輸出

## 3. 核心流程
1. **抽取**：`extract_vb_inventory.py` 解析 VB 檔案 -> inventory。
2. **生成**：`generate_wiki.py` 以模板輸出 Wiki + Speaker。
3. **審核**：依 `docs/governance.md` 流程校正內容。

## 4. 擴充建議
- **解析器**：導入 VB AST 解析器提升準確度。
- **RAG/向量索引**：建立向量索引以支援語意查詢。
- **Speaker Schema**：依遷移需求擴充欄位。

## 5. 版本與發布
- 使用 Git 管理內容與變更。
- 與公司內部 CI/CD 整合，自動化產生最新 Wiki。

