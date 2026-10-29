with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
rules = [
    'c-nav',
    'nav-inner',
    'nav-logo',
    'page-progress',
    'page-section',
    'menu-button',
    'menu-icon',
    'menu-wrapper',
    'menu-inner',
    'menu-link'
]

for r in rules:
    matches = re.findall(rf'([^{{}}]*\.{r}[^{{}}]*\{{[^}}]*\}})', c)
    print(f"=== Rule .{r} ({len(matches)} occurrences) ===")
    for m in matches[:3]:
        print("  ", m.strip().replace('\n', ' '))
