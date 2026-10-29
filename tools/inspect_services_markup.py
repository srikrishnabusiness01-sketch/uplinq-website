with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('id="services"')
print("=== Services HTML ===")
print(c[idx:idx+2500])
