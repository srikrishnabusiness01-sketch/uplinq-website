import re

txt = open('site/_nuxt/BMQH0uFj.js', encoding='utf-8').read()

idx = txt.find("W=()=>{r0.value=!0}")
print(txt[idx-200:idx+200])
