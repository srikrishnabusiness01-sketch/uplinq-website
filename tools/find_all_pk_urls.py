with open('site/_nuxt/pK72Md3I.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'href=[\'\"](https?://[^\'\"]+)[\'\"]', js)
print("All URLs in pK72Md3I.js:")
for m in matches:
    print(" ", m)
