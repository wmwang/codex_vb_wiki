# LLM 整合說明

## 目的
本專案目前提供完整的資料抽取與 Wiki/Speaker 生成流程，但 LLM 查詢/補齊功能仍屬於「可插拔」的擴充項目。

## 為什麼需要 API Key
LLM 服務需經過授權呼叫，因此需提供對應的 API Key 或內部模型端點。

## 建議整合方式（範例架構）
1. 於 `scripts/` 新增 `llm_enrich.py` 模組。
2. 統一入口點：從 inventory 讀取資料 → 呼叫 LLM → 回寫至模板。
3. 使用環境變數配置：
   - `LLM_PROVIDER`
   - `LLM_API_KEY`
   - `LLM_MODEL`
   - `LLM_ENDPOINT`（可選）

## 介面範例（Pseudo）
```python
provider = os.getenv("LLM_PROVIDER")
api_key = os.getenv("LLM_API_KEY")
model = os.getenv("LLM_MODEL")

if not api_key:
    raise RuntimeError("Missing LLM_API_KEY")

response = client.generate(model=model, prompt=prompt)
```

## 下一步
若提供 API Key 或內部模型端點，即可在此專案中完整實作 LLM enrichment 與 RAG 查詢功能。

