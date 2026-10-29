txt = open('site/index.html', encoding='utf-8').read()

import re

print("=== 1. NAV & MENU BUTTON ===")
nav_match = re.search(r'<nav[^>]*>.*?</nav>', txt, re.DOTALL)
if nav_match:
    print(nav_match.group(0)[:500])
else:
    # find .c-nav
    idx = txt.find('class="c-nav"')
    print(txt[idx-50:idx+600])

print("\n=== 2. HERO VIDEO BLOCK MOBILE ===")
idx = txt.find('header-video_block cc-mobile')
print(txt[idx-50:idx+700])

print("\n=== 3. SERVICES BLOCKS (DEFINING, REACHING, AUTOMATING) ===")
idx = txt.find('section-services')
print(txt[idx:idx+2500])
