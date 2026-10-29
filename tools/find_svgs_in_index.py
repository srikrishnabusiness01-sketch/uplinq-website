txt = open('site/index.html', encoding='utf-8').read()

import re

for m in re.finditer(r'<svg[^>]*>.*?</svg>', txt, re.DOTALL):
    svg = m.group(0)
    # find stroke or path
    print(svg[:150])
