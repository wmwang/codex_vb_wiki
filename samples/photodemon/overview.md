# PhotoDemon Wiki Sample

## 專案概述
PhotoDemon 是以 Visual Basic 為主的影像處理專案，這裡提供 Wiki 的示範輸出格式。

## 內容範例
- 模組摘要：`PhotoDemonCore`, `ExportEngine`
- Speaker 規格輸出：`samples/photodemon/speaker/*.yaml`
- Wiki 頁面：`samples/photodemon/wiki/index.md`

## 模組摘要（示例）

### PhotoDemonCore
- **用途**：負責啟動流程、載入設定與初始化影像處理核心。
- **輸入**：啟動參數、設定檔路徑。
- **輸出**：初始化狀態與錯誤碼。
- **依賴**：GDI+、設定檔。

### ExportEngine
- **用途**：影像匯出處理與格式驗證。
- **輸入**：影像資料、輸出格式。
- **輸出**：匯出檔案。
- **依賴**：檔案系統。

