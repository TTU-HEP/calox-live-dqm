import os

# Settings
REPO_NAME = "calox-live-dqm"
ROOT_DIR = "results/html"
OUTPUT_FILE = "docs/overview.html"

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Collect HTML file paths
html_entries = []
for root, _, files in os.walk(ROOT_DIR):
    for file in sorted(files):
        if file.endswith(".html"):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, ".")  # relative to repo root
            run_path = rel_path.replace("results/html/", "")
            web_path = f"/{REPO_NAME}/{rel_path}"
            html_entries.append((web_path, run_path))

# Generate overview HTML
html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Overview of HTML Files</title>
  <style>
    body { font-family: sans-serif; padding: 20px; }
    h1 { margin-bottom: 20px; }
    ul { list-style-type: none; padding: 0; }
    li { margin: 8px 0; }
    a { text-decoration: none; color: #007acc; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>CaloX Test Beam DQM Plots</h1>
  <ul>
"""

for web_path, run_path in sorted(html_entries):
    html += f'    <li><a href="{web_path}" target="_blank">{run_path}</a></li>\n'

html += """  </ul>
</body>
</html>
"""

with open(OUTPUT_FILE, "w") as f:
    f.write(html)
    print(f"Overview generated at {OUTPUT_FILE}")
