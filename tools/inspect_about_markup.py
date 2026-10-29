with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('id="about-us"')
if idx == -1:
    idx = c.find('about-us')
print("About section snippet:")
print(c[idx:idx+2000])
