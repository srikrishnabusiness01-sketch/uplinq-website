with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.group(0) for m in re.finditer(r'.{0,100}defining.{0,200}', html, re.IGNORECASE)]
for m in matches[:3]:
    print(m)
    print('---')
