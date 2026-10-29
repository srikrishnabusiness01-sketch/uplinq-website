with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('footer-socials')
if idx != -1:
    print(html[idx:idx+1500])
