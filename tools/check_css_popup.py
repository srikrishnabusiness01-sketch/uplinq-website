txt = open('site/_nuxt/entry.DzM0mqX9.css', encoding='utf-8').read()

import re
for cls in ['c-popup', 'popup-overlay', 'popup-wrapper', 'contact-form', 'c-button']:
    print(f"=== {cls} in CSS ===")
    for m in re.finditer(rf'([^{{}}]*{cls}[^{{}}]*\{{[^}}]+\}})', txt):
        print(m.group(0)[:120])
