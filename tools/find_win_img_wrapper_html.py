import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# search for win-img_wrapper in HTML markup
idx = html.find('win-img_wrapper')
if idx != -1:
    print(html[idx-100:idx+400])
