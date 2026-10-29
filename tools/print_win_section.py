with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = 185124
print(html[idx-300:idx+1500])
