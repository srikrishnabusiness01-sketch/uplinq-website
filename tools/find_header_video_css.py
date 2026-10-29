import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'(\.header-video[^{]*\{[^}]*\})', html)
for m in matches:
    print(m)
