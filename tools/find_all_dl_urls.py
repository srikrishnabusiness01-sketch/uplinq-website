with open('site/_nuxt/Dl_6lvg3.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'href=[\'\"](https?://[^\'\"]+)[\'\"]', js)
print("All URLs in Dl_6lvg3.js:")
for m in matches:
    print(" ", m)
