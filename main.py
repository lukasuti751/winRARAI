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
