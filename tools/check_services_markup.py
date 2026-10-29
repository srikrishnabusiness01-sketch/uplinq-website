with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('DEFINING')
if idx != -1:
    print(html[idx-200:idx+400])
else:
    print("DEFINING not found")
