#!/usr/bin/env python3
"""Extract a basic inventory from VB source files.

Usage:
  python scripts/extract_vb_inventory.py /path/to/source > data/inventory.json
"""

import json
import re
import sys
from pathlib import Path

MODULE_RE = re.compile(r"^\s*(Module|Class)\s+(\w+)", re.IGNORECASE)
FUNC_RE = re.compile(r"^\s*(Public|Private|Friend)?\s*(Sub|Function)\s+(\w+)", re.IGNORECASE)


def extract_from_file(path: Path):
    module_name = None
    functions = []
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            module_match = MODULE_RE.match(line)
            if module_match:
                module_name = module_match.group(2)
            func_match = FUNC_RE.match(line)
            if func_match:
                functions.append(func_match.group(3))
    return {
        "file": str(path),
        "module": module_name,
        "functions": functions,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/extract_vb_inventory.py <source_dir>")
        return 1

    source_dir = Path(sys.argv[1])
    if not source_dir.exists():
        print(f"Source dir not found: {source_dir}")
        return 1

    vb_files = list(source_dir.rglob("*.vb")) + list(source_dir.rglob("*.bas")) + list(source_dir.rglob("*.frm"))
    inventory = [extract_from_file(path) for path in vb_files]
    print(json.dumps({"inventory": inventory}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
