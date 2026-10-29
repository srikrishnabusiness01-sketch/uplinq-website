with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('id="welcome"')
print("=== Hero HTML ===")
print(c[idx:idx+2500])

print("\n=== Header CSS ===")
for cls in ['.header-inner', '.header-title_wrapper', '.header-tag', '.header-video_block', '.header-subtext']:
    for m in re.finditer(re.escape(cls), c):
        start = max(0, m.start() - 20)
        end = min(len(c), m.start() + 150)
        print(f"[{cls}]:", c[start:end].replace('\n', ' '))
        break
