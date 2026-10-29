import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find project card structure in HTML
m = re.findall(r'<div class="project-card"[^>]*>.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
print(f"Project cards found: {len(m)}")
if m:
    print("Sample card HTML snippet:")
    print(m[0][:600])

# Inspect CSS for project-thumbnail, thumbnail-img_block, c-img
css_rules = re.findall(r'(\.(?:project-thumbnail|thumbnail-img_block|c-img)[^{]*\{[^}]*\})', html)
for r in css_rules:
    print("RULE:", r)
