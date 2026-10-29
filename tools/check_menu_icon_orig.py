txt = open('site/index.html', encoding='utf-8').read()

import re
for m in re.finditer(r'([^{}]*menu-icon[^{}]*\{[^}]+\})', txt):
    print(m.group(0))
