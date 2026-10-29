import re

txt = open('site/index.html', encoding='utf-8').read()

# Let's find all sections and check if there are buttons or links in them
for m in re.finditer(r'<section[^>]*>(.*?)</section>', txt, re.DOTALL):
    sec = m.group(0)
    has_btn = 'button' in sec or 'c-button' in sec
    # print section class and has_btn
    cls = re.search(r'class="([^"]*)"', sec)
    print(cls.group(1) if cls else 'no class', 'has_btn:', has_btn)
    if has_btn:
        btns = re.findall(r'<button[^>]*>.*?</button>', sec, re.DOTALL)
        for b in btns:
            print("   ", b[:100])
