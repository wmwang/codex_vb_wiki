# 測試手冊（Testing Manual）

## 1. 目的
說明如何驗證 VB Deep Wiki 的抽取、模板生成與 Speaker 輸出流程。

## 2. 測試範圍
- Inventory 抽取（`scripts/extract_vb_inventory.py`）
- Wiki 生成（`scripts/generate_wiki.py`）
- Speaker YAML 輸出

## 3. 測試前置
- Python 3.10+（建議）
- 已準備可解析的 VB 專案（或使用 PhotoDemon sample）

## 4. 測試步驟

### 4.1 抽取 Inventory
```bash
python scripts/extract_vb_inventory.py /path/to/source > data/inventory.json
```
**驗證點**
- JSON 格式正確
- `inventory` 陣列中包含 `file/module/functions` 欄位

### 4.2 生成 Wiki 與 Speaker
```bash
python scripts/generate_wiki.py
```
**驗證點**
- `samples/photodemon/wiki/index.md` 生成
- `samples/photodemon/wiki/*.md` 生成
- `samples/photodemon/speaker/*.yaml` 生成

### 4.3 人工檢查
- 模組頁是否有 **用途/輸入輸出/依賴/流程/錯誤處理** 區段
- Speaker YAML 是否符合 `speaker/schema.yaml` 欄位

## 5. 驗證結果記錄
- 測試時間
- 測試人員
- 成功/失敗紀錄
- 失敗原因與修正建議

