txt1 = open('site/index.html', encoding='utf-8').read()
txt2 = open('site/_nuxt/entry.DzM0mqX9.css', encoding='utf-8').read()

import re
print("=== index.html win- rules ===")
for m in re.finditer(r'([^{}]*\.win-[^{}]*\{[^}]+\})', txt1):
    print(m.group(0))

print("\n=== entry.DzM0mqX9.css win- rules ===")
for m in re.finditer(r'([^{}]*\.win-[^{}]*\{[^}]+\})', txt2):
    print(m.group(0))
