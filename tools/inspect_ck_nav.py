txt = open('site/_nuxt/CKrmhtJt.js', encoding='utf-8').read()

idx = txt.find('nav-logo w-inline-block w--current')
print(txt[idx-50:idx+350])
