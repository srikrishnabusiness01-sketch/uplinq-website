with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('We help them win in')
print("=== Impact Words HTML ===")
print(c[idx-100:idx+2500])
