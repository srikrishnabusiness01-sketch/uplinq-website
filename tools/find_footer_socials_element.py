with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('class="footer-socials"')
if idx != -1:
    print(html[idx-50:idx+1500])
else:
    print("class=\"footer-socials\" not found in HTML text")
