with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('stats-sketch_block')
while idx != -1:
    print(html[idx-50:idx+300])
    print('---')
    idx = html.find('stats-sketch_block', idx + 1)
