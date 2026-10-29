txt = open('site/_nuxt/CKrmhtJt.js', encoding='utf-8').read()

idx = txt.find('_hoisted_8$2')
print(txt[idx-50:idx+600])
