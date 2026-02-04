# PhotoDemonCore

## 用途
- 核心流程與初始化

## 輸入/輸出
- 輸入：啟動參數, 設定檔路徑
- 輸出：初始化狀態

## 依賴
- 資料表：無
- API：Windows GDI+
- 檔案：Config/PhotoDemon.ini

## 流程
1. 讀取設定並初始化
2. 啟動處理核心

## 錯誤處理
- 初始化失敗時回傳錯誤碼

## 效能/限制
- 避免同步 I/O

## 範例
```vb
Call LoadConfig()
Call InitializeGraphicsCore()
Call Shutdown()
```

## 變更記錄
- 2025-01-01 初版

