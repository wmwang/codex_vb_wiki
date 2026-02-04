# VB Deep Wiki

這是一個用於建立 VB 大型系統 Wiki/Deep Wiki 的生產級專案骨架，包含：

- 統一的內容模板與 Speaker 規格輸出
- LLM 輔助的抽取與標準化工作流程
- 可擴展的索引/問答/權限治理設計
- 以 PhotoDemon 作為示範專案的範例內容

## 專案結構

```
.
├── config
│   └── sources.yaml              # 程式碼/文件來源設定
├── docs
│   ├── architecture.md           # 架構藍圖
│   ├── governance.md             # 內容治理與審核流程
│   ├── llm_pipeline.md           # LLM 輔助流程
│   ├── llm_integration.md        # LLM 整合說明
│   ├── manuals                   # 使用/測試/開發者/成果文件
│   └── templates                 # 標準化模板
├── samples
│   └── photodemon                # PhotoDemon 範例輸出
├── site                           # 靜態站點輸出
├── speaker
│   ├── schema.yaml               # Speaker 規格欄位定義
│   └── examples                  # Speaker 範例輸出
└── scripts
    ├── extract_vb_inventory.py   # VB 程式碼抽取器 (示範)
    ├── generate_wiki.py          # 由 inventory 產生 wiki 與 Speaker 輸出
    └── build_site.py             # 產生靜態 HTML 站點
```

## 快速開始

1. 將目標專案加入 `config/sources.yaml`。
2. 使用 `scripts/extract_vb_inventory.py` 產生初始 inventory。
3. 使用 `scripts/generate_wiki.py` 產生 wiki 與 Speaker 輸出。
4. 使用 `scripts/build_site.py` 產生靜態站點。
5. 啟用 LLM 輔助流程與審核機制 (參考 `docs/llm_pipeline.md`)。

### 示範指令

```bash
python scripts/extract_vb_inventory.py /path/to/source > data/inventory.json
python scripts/generate_wiki.py
python scripts/build_site.py
python -m http.server --directory site 8000
```

## 測試專案：PhotoDemon

`/samples/photodemon` 提供一份以 PhotoDemon 為樣本的內容，展示模板與 Speaker 規格輸出格式。

- `samples/photodemon/inventory.json`
- `samples/photodemon/wiki/index.md`
- `samples/photodemon/speaker/*.yaml`

## 手冊

- 使用者手冊：`docs/manuals/user_manual.md`
- 測試手冊：`docs/manuals/testing_manual.md`
- 開發者手冊：`docs/manuals/developer_manual.md`
- 最後成果文件：`docs/manuals/final_deliverable.md`

## LLM 整合

詳見：`docs/llm_integration.md`

