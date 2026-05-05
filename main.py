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
