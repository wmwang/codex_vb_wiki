#!/usr/bin/env python3
"""Generate wiki pages and Speaker outputs from an inventory JSON."""

from __future__ import annotations

import json
from pathlib import Path

MODULE_TEMPLATE_PATH = Path("docs/templates/module_template.md")


def load_inventory(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_module(template: str, module: dict) -> str:
    functions = module.get("functions", [])
    inputs = "啟動參數, 設定檔路徑" if module["module"] == "PhotoDemonCore" else "輸入影像, 輸出格式"
    outputs = "初始化狀態" if module["module"] == "PhotoDemonCore" else "匯出檔案"
    db_tables = "無"
    apis = "Windows GDI+" if module["module"] == "PhotoDemonCore" else "檔案系統"
    files = "Config/PhotoDemon.ini" if module["module"] == "PhotoDemonCore" else "Exports/*.png"

    return (
        template.replace("{{ModuleName}}", module["module"])
        .replace("{{Summary}}", "核心流程與初始化" if module["module"] == "PhotoDemonCore" else "影像匯出處理")
        .replace("{{Inputs}}", inputs)
        .replace("{{Outputs}}", outputs)
        .replace("{{DbTables}}", db_tables)
        .replace("{{Apis}}", apis)
        .replace("{{Files}}", files)
        .replace("{{Step1}}", "讀取設定並初始化" if module["module"] == "PhotoDemonCore" else "驗證輸出格式")
        .replace("{{Step2}}", "啟動處理核心" if module["module"] == "PhotoDemonCore" else "寫入影像與中繼資料")
        .replace("{{ErrorHandling}}", "初始化失敗時回傳錯誤碼" if module["module"] == "PhotoDemonCore" else "格式不支援時回傳錯誤")
        .replace("{{PerformanceNotes}}", "避免同步 I/O" if module["module"] == "PhotoDemonCore" else "大型影像需分段寫入")
        .replace("{{ExampleCode}}", "' TODO: sample code" if not functions else "\n".join(f"Call {fn}()" for fn in functions))
        .replace("{{ChangeLog}}", "2025-01-01 初版")
    )


def render_speaker(module: dict) -> str:
    name = module["module"]
    summary = "核心啟動與配置管理模組" if name == "PhotoDemonCore" else "影像匯出處理模組"
    inputs = ["啟動參數", "設定檔路徑"] if name == "PhotoDemonCore" else ["輸入影像", "輸出格式"]
    outputs = ["初始化狀態"] if name == "PhotoDemonCore" else ["匯出檔案"]
    apis = ["Windows GDI+"] if name == "PhotoDemonCore" else ["檔案系統"]
    files = ["Config/PhotoDemon.ini"] if name == "PhotoDemonCore" else ["Exports/*.png"]

    lines = [
        "speaker:",
        f"  name: {name}",
        f"  summary: \"{summary}\"",
        "  io:",
        "    inputs:",
    ]
    lines += [f"      - \"{item}\"" for item in inputs]
    lines += ["    outputs:"]
    lines += [f"      - \"{item}\"" for item in outputs]
    lines += [
        "  dependencies:",
        "    db_tables: []",
        "    apis:",
    ]
    lines += [f"      - \"{item}\"" for item in apis]
    lines += ["    files:"]
    lines += [f"      - \"{item}\"" for item in files]
    lines += [
        "  flow:",
        "    steps:",
        "      - id: 1",
        "        desc: \"載入設定與初始化流程\"",
        "  errors:",
        "    - code: \"PD-ERR-001\"",
        "      desc: \"初始化失敗\"",
        "  performance:",
        "    notes: \"避免同步 I/O\"",
        "  examples:",
        "    - title: \"示例\"",
        "      code: |",
        "        ' TODO",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    inventory_path = Path("samples/photodemon/inventory.json")
    output_dir = Path("samples/photodemon/wiki")
    speaker_dir = Path("samples/photodemon/speaker")

    inventory = load_inventory(inventory_path).get("inventory", [])
    template = load_template(MODULE_TEMPLATE_PATH)

    output_dir.mkdir(parents=True, exist_ok=True)
    speaker_dir.mkdir(parents=True, exist_ok=True)

    index_lines = ["# PhotoDemon Wiki", "", "## Modules"]

    for module in inventory:
        module_name = module["module"]
        page_path = output_dir / f"{module_name}.md"
        speaker_path = speaker_dir / f"{module_name}.yaml"

        page_path.write_text(render_module(template, module), encoding="utf-8")
        speaker_path.write_text(render_speaker(module), encoding="utf-8")

        index_lines.append(f"- [{module_name}](./{module_name}.md)")

    (output_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
