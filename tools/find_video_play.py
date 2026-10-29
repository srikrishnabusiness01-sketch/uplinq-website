import re

txt = open('site/_nuxt/BMQH0uFj.js', encoding='utf-8').read()

for m in re.finditer(r'.{0,100}\.play\(.{0,100}', txt):
    print("Found .play():", m.group(0))
