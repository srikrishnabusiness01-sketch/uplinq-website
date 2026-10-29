with open('site/_nuxt/pK72Md3I.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('footer-socials')
print(js[idx:idx+1200])
