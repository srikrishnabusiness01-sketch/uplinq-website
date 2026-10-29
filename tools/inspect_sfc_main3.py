txt = open('site/_nuxt/CKrmhtJt.js', encoding='utf-8').read()

idx = txt.find('_sfc_main$3=defineComponent')
print(txt[idx:idx+1200])
