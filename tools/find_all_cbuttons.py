with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'c-button', c)]
for m in matches:
    print(c[m-50:m+200].replace('\n', ' '))
    print('='*50)
