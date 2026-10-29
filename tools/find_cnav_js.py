txt = open('site/_nuxt/CKrmhtJt.js', encoding='utf-8').read()

import re
idx = txt.find('menu-button')
if idx != -1:
    print("Found menu-button in CKrmhtJt.js:", txt[idx-100:idx+200])
else:
    print("menu-button NOT in CKrmhtJt.js")
    # let's search for c-nav in CKrmhtJt.js
    for m in re.finditer(r'.{0,100}c-nav.{0,100}', txt):
        print("  c-nav:", m.group(0))
