import re

txt = open('site/_nuxt/pK72Md3I.js', encoding='utf-8').read()

for m in re.finditer(r'.{0,100}contact.{0,100}', txt):
    print(m.group(0))
