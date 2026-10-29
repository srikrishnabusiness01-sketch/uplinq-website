with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('video-website-loop')
while idx != -1:
    print(html[idx-100:idx+250])
    idx = html.find('video-website-loop', idx+1)
