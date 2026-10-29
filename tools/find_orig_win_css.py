with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'[^{}]*win-img[^{}]*\{[^{}]*\}', css)
for m in matches[:10]:
    print(m)
