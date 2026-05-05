from pathlib import Path
import json
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "winRARAI" / "index.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

rng = random.Random(0xBADC0DE ^ 0xACE0FACE)

rows = []
for i in range(520):
    rows.append(
        {
            "id": i,
            "name": f"facet_archive_{i:04d}.volt",
            "size": rng.randint(1024, 999_999),
            "crc": hex(rng.randint(0, 0xFFFFFFFF)),
            "tip": f"Lesson shard {i}: trace cohort pacing before opening public drills.",
        }
    )

rows_json = json.dumps(rows)

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>winRARAI — VoltTrace archive tutor</title>
  <style>
"""

# large CSS block ~400 lines
css_lines = [
    ":root {",
    "  --bg: #c0c0c0;",
    "  --panel: #d4d0c8;",
    "  --hi: #000080;",
    "  --accent: #7a1c1c;",
    "  --txt: #000000;",
    "  --border: #808080;",
    "  --inner: #ffffff;",
    "}",
    "* { box-sizing: border-box; }",
    "body { margin: 0; font-family: Tahoma, Arial, sans-serif; background: var(--bg); color: var(--txt); }",
    ".titlebar { display: flex; align-items: center; background: linear-gradient(90deg,#000080,#1084d0); color: #fff; padding: 4px 8px; font-size: 13px; }",
    ".titlebar .ico { width: 16px; height: 16px; margin-right: 6px; background: #fff3; border: 1px solid #fff8; }",
    ".toolbar { display: flex; gap: 4px; padding: 4px; background: var(--panel); border-bottom: 1px solid var(--border); flex-wrap: wrap; }",
    ".toolbar button { font-size: 11px; padding: 2px 8px; border: 1px solid #404040; background: var(--panel); cursor: pointer; }",
    ".toolbar button:active { border-style: inset; }",
    ".layout { display: grid; grid-template-columns: 220px 1fr 280px; min-height: calc(100vh - 52px); }",
    ".tree { background: var(--inner); border-right: 1px solid var(--border); padding: 8px; overflow: auto; font-size: 12px; }",
    ".main { padding: 8px; overflow: auto; }",
    ".side { background: var(--inner); border-left: 1px solid var(--border); padding: 8px; font-size: 12px; overflow: auto; }",
    ".status { border-top: 1px solid var(--border); padding: 4px 8px; font-size: 11px; background: var(--panel); }",
    "table.files { width: 100%; border-collapse: collapse; font-size: 12px; }",
    "table.files th, table.files td { border: 1px solid var(--border); padding: 4px 6px; }",
    "table.files th { background: var(--panel); text-align: left; }",
    "tr.sel { background: #00008022; }",
    ".meter { height: 18px; border: 1px inset #808080; background: #fff; margin: 8px 0; }",
    ".meter > i { display: block; height: 100%; background: #000080; width: 0%; transition: width .4s; }",
    ".card { border: 1px solid var(--border); padding: 8px; margin-bottom: 8px; background: #fafafa; }",
    "input, select { font-size: 12px; }",
    "h2 { margin: 8px 0; font-size: 14px; }",
    ".tag { display: inline-block; padding: 1px 6px; background: #ffffcc; border: 1px solid #999; margin: 2px; font-size: 10px; }",
]

for z in range(380):
    css_lines.append(f".z{z} {{ margin: {(z % 5) + 1}px; padding: {(z % 3)}px; }}")

css_lines.append("  </style>")
# fix - last line should close style not have spaces wrong
css_lines[-1] = "}"

# rebuild css properly
css_core = "\n".join(css_lines[:26])
css_extra = "\n".join(f".z{z}{{margin:{(z%5)+1}px}}" for z in range(380))
full_css = ":root {\n  --bg: #c0c0c0;\n  --panel: #d4d0c8;\n  --hi: #000080;\n  --accent: #7a1c1c;\n  --txt: #000000;\n  --border: #808080;\n  --inner: #ffffff;\n}\n"
full_css += "*{box-sizing:border-box}\nbody{margin:0;font-family:Tahoma,Arial,sans-serif;background:var(--bg);color:var(--txt)}\n"
full_css += ".titlebar{display:flex;align-items:center;background:linear-gradient(90deg,#000080,#1084d0);color:#fff;padding:4px 8px;font-size:13px}\n"
full_css += ".titlebar .ico{width:16px;height:16px;margin-right:6px;background:#fff3;border:1px solid #fff8}\n"
full_css += ".toolbar{display:flex;gap:4px;padding:4px;background:var(--panel);border-bottom:1px solid var(--border);flex-wrap:wrap}\n"
full_css += ".toolbar button{font-size:11px;padding:2px 8px;border:1px solid #404040;background:var(--panel);cursor:pointer}\n"
full_css += ".layout{display:grid;grid-template-columns:220px 1fr 280px;min-height:calc(100vh - 52px)}\n"
full_css += ".tree,.main,.side{font-size:12px}\n.tree{background:var(--inner);border-right:1px solid var(--border);padding:8px;overflow:auto}\n"
full_css += ".main{padding:8px;overflow:auto}\n.side{background:var(--inner);border-left:1px solid var(--border);padding:8px;overflow:auto}\n"
full_css += ".status{border-top:1px solid var(--border);padding:4px 8px;font-size:11px;background:var(--panel)}\n"
full_css += "table.files{width:100%;border-collapse:collapse}table.files th,table.files td{border:1px solid var(--border);padding:4px 6px}\n"
full_css += "table.files th{background:var(--panel);text-align:left}tr.sel{background:#00008022}\n"
full_css += ".meter{height:18px;border:1px inset #808080;background:#fff;margin:8px 0}\n.meter>i{display:block;height:100%;background:#000080;width:0%;transition:width .4s}\n"
full_css += ".card{border:1px solid var(--border);padding:8px;margin-bottom:8px;background:#fafafa}\n"
full_css += css_extra + "\n"

html_mid = (
    "</head>\n<body>\n"
    '<div class="titlebar"><span class="ico"></span> winRARAI — VoltTrace / explos_dos archive tutor</div>\n'
    '<div class="toolbar" id="tb"></div>\n'
    '<div class="layout">\n'
    '  <div class="tree" id="tree"></div>\n'
    '  <div class="main">\n'
    '    <h2>Archive listing</h2>\n'
    '    <div class="meter"><i id="meter"></i></div>\n'
    '    <table class="files" id="ft"><thead><tr><th>Name</th><th>Size</th><th>CRC32</th></tr></thead><tbody></tbody></table>\n'
    "  </div>\n"
    '  <div class="side" id="side"></div>\n'
    "</div>\n"
    '<div class="status" id="st">Ready — pedagogical UI only; no on-chain writes from this page.</div>\n'
