with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
idx = html.find('is--win')
if idx != -1:
    print(html[idx-50:idx+1500])
else:
    print('is--win not found')
