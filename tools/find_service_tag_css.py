with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'[^{}]*service-tag[^{}]*\{[^{}]*\}', css)
for m in matches:
    print(m)
print('--- title ---')
matches2 = re.findall(r'[^{}]*service-block_title[^{}]*\{[^{}]*\}', css)
for m in matches2:
    print(m)
