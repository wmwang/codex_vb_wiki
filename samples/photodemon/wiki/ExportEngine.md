# ExportEngine

## 用途
- 影像匯出處理

## 輸入/輸出
- 輸入：輸入影像, 輸出格式
- 輸出：匯出檔案

## 依賴
- 資料表：無
- API：檔案系統
- 檔案：Exports/*.png

## 流程
1. 驗證輸出格式
2. 寫入影像與中繼資料

## 錯誤處理
- 格式不支援時回傳錯誤

## 效能/限制
- 大型影像需分段寫入

## 範例
```vb
Call ExportImage()
Call ValidateFormat()
Call WriteMetadata()
```

## 變更記錄
- 2025-01-01 初版

