with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('class="section-cta"')
if idx == -1:
    idx = c.find('section-cta')
if idx == -1:
    idx = c.find('cta-wrapper')
if idx == -1:
    idx = c.find('section-footer')
print("=== CTA Block snippet ===")
print(c[idx-200:idx+2500])
