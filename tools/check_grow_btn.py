import re

txt = open('site/_nuxt/BMQH0uFj.js', encoding='utf-8').read()

# Find Let's Grow
idx = txt.find("Let's Grow")
print("=== BMQH0uFj.js around Let's Grow ===")
print(txt[idx-300:idx+300])
