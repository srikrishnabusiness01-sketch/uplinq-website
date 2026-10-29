txt1 = open('site/index.html', encoding='utf-8').read()
txt2 = open('site/_nuxt/entry.DzM0mqX9.css', encoding='utf-8').read()

import re
print("=== index.html service-block styles ===")
for m in re.finditer(r'([^{}]*service-block[^{}]*\{[^}]+\})', txt1):
    print(m.group(0))

print("\n=== entry.DzM0mqX9.css service-block styles ===")
for m in re.finditer(r'([^{}]*service-block[^{}]*\{[^}]+\})', txt2):
    print(m.group(0))
