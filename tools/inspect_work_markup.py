with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('id="work"')
if idx == -1:
    idx = c.find('section-projects')
if idx == -1:
    idx = c.find('c-project')
print("=== Work HTML ===")
print(c[idx-100:idx+2500])
