with open('site/_nuxt/pK72Md3I.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('https://www.instagram.com/wearecheck_/')
print(js[idx-300:idx+800])
