with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('contact-form')
while idx != -1:
    print("Contact form match at", idx, ":")
    print(c[max(0, idx-50):min(len(c), idx+250)].replace('\n', ' '))
    idx = c.find('contact-form', idx+1)
    if idx > 120000:
        break
