import os

html_root = "results/html"
overview_file = os.path.join(html_root, "overview.html")

# Collect all .html files (recursively) under home/html/, excluding overview.html
entries = []
for root, dirs, files in os.walk(html_root):
    for f in files:
        if f.endswith(".html") and f != "overview.html":
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, html_root)
            entries.append(f'<li><a href="{rel_path}">{rel_path}</a></li>')

# Build HTML content
html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Overview of All HTML Files</title>
  <style>
    body {{ font-family: sans-serif; padding: 20px; }}
    h1 {{ margin-bottom: 20px; }}
    ul {{ list-style-type: none; padding: 0; }}
    li {{ margin: 8px 0; }}
  </style>
</head>
<body>
  <h1>Overview of All HTML Files</h1>
  <ul>
    {''.join(entries)}
  </ul>
</body>
</html>
"""

# Save the overview file
with open(overview_file, "w") as f:
    f.write(html_content)

print(f"✅ Generated: {overview_file}")
