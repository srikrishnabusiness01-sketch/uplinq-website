txt = open('site/_nuxt/entry.DzM0mqX9.css', encoding='utf-8').read()

idx = txt.find('@media screen and (max-width: 767.98px)')
print(txt[idx+10500:idx+15000])
