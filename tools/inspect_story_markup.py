with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('services-inner cc-stats')
print("=== Story / Stats HTML ===")
print(c[idx:idx+3500])
