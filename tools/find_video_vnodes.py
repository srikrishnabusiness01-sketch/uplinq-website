txt = open('site/_nuxt/BMQH0uFj.js', encoding='utf-8').read()

import re
for m in re.finditer(r'header-video cc-top[^}]+}', txt):
    print(m.group(0))
for m in re.finditer(r'header-video cc-bottom[^}]+}', txt):
    print(m.group(0))
