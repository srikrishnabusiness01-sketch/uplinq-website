import re

txt = open('site/index.html', encoding='utf-8').read()

print("--- BUTTONS WITH C-BUTTON ---")
for m in re.finditer(r'<button[^>]*class=["\'][^"\']*c-button[^>]*>(.*?)</button>', txt, re.DOTALL):
    print(m.group(0))
    print("=" * 50)

print("--- A TAGS WITH C-BUTTON ---")
for m in re.finditer(r'<a[^>]*class=["\'][^"\']*c-button[^>]*>(.*?)</a>', txt, re.DOTALL):
    print(m.group(0))
    print("=" * 50)

print("--- ALL OCCURRENCES OF 'GROW' OR 'DESIGN' OR 'BEGIN' ---")
for word in ['GROW', 'DESIGN', 'BEGIN']:
    for m in re.finditer(rf'.{{0,100}}{word}.{{0,100}}', txt, re.IGNORECASE):
        print(f"[{word}]", m.group(0).strip())
