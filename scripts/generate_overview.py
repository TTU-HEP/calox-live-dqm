import os

ROOT_DIR = "results/html"
OUTPUT_FILE = "docs/overview.html"
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

html_entries = []

for root, dirs, files in os.walk(ROOT_DIR):
    for file in sorted(files):
        if file.endswith(".html"):
            full_path = os.path.join(root, file)
            # make path relative to GitHub Pages root
            rel_path = os.path.relpath(full_path, "docs")
            html_entries.append(rel_path)

# Create HTML
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
  <h1>Available HTML Reports</h1>
  <ul>
"""

for path in sorted(html_entries):
    html += f'    <li><a href="../{path}" target="_blank">{path}</a></li>\n'

html += """  </ul>
</body>
</html>
"""

with open(OUTPUT_FILE, "w") as f:
    f.write(html)
