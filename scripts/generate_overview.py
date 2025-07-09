import os
from collections import defaultdict
from datetime import datetime

# Settings
REPO_NAME = "calox-live-dqm"
ROOT_DIR = "results/html"
OUTPUT_FILE = "docs/overview.html"

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Group HTML entries by RunXXX
grouped_entries = defaultdict(list)
for root, _, files in os.walk(ROOT_DIR):
    for file in sorted(files):
        if file.endswith(".html"):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, ".")  # relative to repo root
            run_path = rel_path.replace("results/html/", "")
            web_path = f"/{REPO_NAME}/{rel_path}"
            run_name = run_path.split("/")[0]  # e.g., Run1005
            mtime = os.path.getmtime(full_path)
            grouped_entries[run_name].append((web_path, run_path, mtime))

# Generate overview HTML
html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Overview of HTML Files</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
      background-color: #f9f9f9;
    }
    h1 {
      margin-bottom: 20px;
      color: #333;
    }
    details {
      border: 1px solid #ccc;
      border-radius: 5px;
      margin-bottom: 10px;
      padding: 0.5em 1em;
      background-color: #fff;
    }
    summary {
      font-weight: bold;
      font-size: 1.05em;
      cursor: pointer;
      outline: none;
    }
    details details {
      margin-top: 5px;
      background-color: #f4f4f4;
      border-left: 4px solid #007acc;
      padding: 0.5em 1em;
    }
    details details summary {
      font-size: 0.95em;
      color: #005b99;
    }
    ul {
      list-style-type: none;
      padding-left: 1em;
      margin: 0.5em 0;
    }
    li {
      margin: 4px 0;
    }
    a {
      text-decoration: none;
      color: #007acc;
    }
    a:hover {
      text-decoration: underline;
    }
    .timestamp {
      color: #777;
      font-size: 0.85em;
      margin-left: 5px;
    }
  </style>
</head>
<body>
  <h1>CaloX Test Beam DQM Plots</h1>
"""

# Add grouped entries
for run_name in sorted(grouped_entries.keys()):
    html += f'  <details>\n    <summary>{run_name}</summary>\n'
    html += f'    <div style="margin-left: 1em;">\n'

    # Collect and group entries by category
    category_map = defaultdict(list)
    prefix = f"{run_name}/"
    for web_path, run_path, mtime in grouped_entries[run_name]:
        inner_path = run_path[len(prefix):]
        category = inner_path.split(
            "/")[0] if "/" in inner_path else inner_path
        category_map[category].append((web_path, inner_path, mtime))

    for category in sorted(category_map.keys()):
        html += f'      <details>\n        <summary>{category}</summary>\n'
        html += f'        <ul>\n'
        for web_path, inner_path, mtime in sorted(category_map[category], key=lambda tup: tup[1]):
            mtime_str = datetime.fromtimestamp(
                mtime).strftime("%Y-%m-%d %H:%M")
            html += f'          <li><a href="{web_path}" target="_blank">{inner_path}</a>'
            html += f' <span class="timestamp">({mtime_str})</span></li>\n'
        html += f'        </ul>\n'
        html += f'      </details>\n'

    html += f'    </div>\n'
    html += f'  </details>\n'

html += """</body>
</html>
"""

# Write to output file
with open(OUTPUT_FILE, "w") as f:
    f.write(html)
    print(f"Overview generated at {OUTPUT_FILE}")
