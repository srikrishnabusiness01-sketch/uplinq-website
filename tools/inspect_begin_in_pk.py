txt = open('site/_nuxt/pK72Md3I.js', encoding='utf-8').read()

idx = txt.find("Let's Begin")
print(txt[idx-100:idx+100])
