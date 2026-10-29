with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s = html.find('class="c-loader"')
e = html.find('page-wrapper')
print(html[s-10:e-10])
