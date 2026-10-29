with open('site/_nuxt/BMQH0uFj.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = [m.group(0) for m in re.finditer(r'.{0,60}header-video_block.{0,100}', js)]
for m in matches:
    print(m)
