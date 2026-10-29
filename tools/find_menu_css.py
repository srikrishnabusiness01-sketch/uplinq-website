with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
for cls in ['.menu-inner', '.menu-link', '.menu-top', '.menu-link_cta', '.menu-link_flex']:
    matches = [m.start() for m in re.finditer(re.escape(cls), c)]
    print(f"=== {cls} ({len(matches)} occurrences) ===")
    for m in matches[:2]:
        print("  ", c[max(0, m-20):min(len(c), m+150)].replace('\n', ' '))
