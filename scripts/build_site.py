#!/usr/bin/env python3
"""Build a static HTML site from markdown wiki pages."""

from __future__ import annotations

import json
from pathlib import Path

SOURCE_DIR = Path("samples/photodemon/wiki")
OUTPUT_DIR = Path("site")
ASSETS_DIR = OUTPUT_DIR / "assets"


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    html_lines = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            if not in_code:
                html_lines.append("<pre><code>")
                in_code = True
            else:
                html_lines.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            html_lines.append(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            continue
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("- "):
            if not html_lines or not html_lines[-1].startswith("<ul>"):
                html_lines.append("<ul>")
            html_lines.append(f"<li>{line[2:]}</li>")
        elif line.strip() == "":
            if html_lines and html_lines[-1].startswith("<li>"):
                html_lines.append("</ul>")
            html_lines.append("<br />")
        else:
            html_lines.append(f"<p>{line}</p>")
    if html_lines and html_lines[-1].startswith("<li>"):
        html_lines.append("</ul>")
    return "\n".join(html_lines)


def load_index_data() -> list[dict]:
    index = []
    for md_file in SOURCE_DIR.glob("*.md"):
        if md_file.name == "index.md":
            continue
        content = md_file.read_text(encoding="utf-8")
        title = content.splitlines()[0].lstrip("# ") if content else md_file.stem
        summary_line = next((line for line in content.splitlines() if line.startswith("- ") or line.startswith("## 用途")), "")
        index.append({"title": title, "file": f"{md_file.stem}.html", "summary": summary_line})
    return index


def write_page(title: str, body_html: str, extra_scripts: str = "") -> str:
    return f"""<!doctype html>
<html lang=\"zh-Hant\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title}</title>
  <link rel=\"stylesheet\" href=\"assets/style.css\" />
</head>
<body>
  <header>
    <h1>VB Deep Wiki - PhotoDemon</h1>
    <nav>
      <a href=\"index.html\">Index</a>
    </nav>
  </header>
  <main>
    {body_html}
  </main>
  {extra_scripts}
</body>
</html>"""


def build_site() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    (ASSETS_DIR / "style.css").write_text(
        """
body { font-family: Arial, sans-serif; margin: 0; background: #f5f7fb; color: #1f2937; }
header { background: #1f3a8a; color: #fff; padding: 1rem 2rem; }
nav a { color: #fff; margin-right: 1rem; text-decoration: none; }
main { padding: 2rem; }
.card { background: #fff; padding: 1rem; margin-bottom: 1rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
.search { margin-bottom: 1rem; }
input[type=\"search\"] { padding: 0.5rem; width: 100%; max-width: 480px; }
pre { background: #111827; color: #f9fafb; padding: 1rem; border-radius: 6px; overflow: auto; }
""".strip(),
        encoding="utf-8",
    )

    index_data = load_index_data()
    (OUTPUT_DIR / "index.json").write_text(json.dumps(index_data, ensure_ascii=False, indent=2), encoding="utf-8")

    index_cards = "\n".join(
        f"<div class=\"card\"><h3>{item['title']}</h3><p>{item['summary']}</p><a href=\"{item['file']}\">Read more</a></div>"
        for item in index_data
    )
    index_html = f"""
<div class=\"search\">
  <input type=\"search\" id=\"search\" placeholder=\"搜尋模組...\" />
</div>
<div id=\"results\">
  {index_cards}
</div>
"""

    script = """
<script>
fetch('index.json')
  .then(res => res.json())
  .then(data => {
    const input = document.getElementById('search');
    const results = document.getElementById('results');
    const render = items => {
      results.innerHTML = items.map(item => `
        <div class="card">
          <h3>${item.title}</h3>
          <p>${item.summary || ''}</p>
          <a href="${item.file}">Read more</a>
        </div>
      `).join('');
    };
    render(data);
    input.addEventListener('input', () => {
      const q = input.value.toLowerCase();
      render(data.filter(item => item.title.toLowerCase().includes(q) || (item.summary || '').toLowerCase().includes(q)));
    });
  });
</script>
"""
    (OUTPUT_DIR / "index.html").write_text(write_page("Index", index_html, script), encoding="utf-8")

    for md_file in SOURCE_DIR.glob("*.md"):
        if md_file.name == "index.md":
            continue
        html_body = markdown_to_html(md_file.read_text(encoding="utf-8"))
        page_html = write_page(md_file.stem, f"<div class=\"card\">{html_body}</div>")
        (OUTPUT_DIR / f"{md_file.stem}.html").write_text(page_html, encoding="utf-8")


if __name__ == "__main__":
    build_site()
