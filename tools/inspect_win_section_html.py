txt = open('site/index.html', encoding='utf-8').read()

import re

idx = txt.find('We help them win in')
print(txt[idx-300:idx+2500])
