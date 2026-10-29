import re

txt = open('site/_nuxt/BMQH0uFj.js', encoding='utf-8').read()

# Search for definition of W = ...
for m in re.finditer(r'(?:const|let|var)\s+W\s*=[^;,]+[;,]', txt):
    print("Found:", m.group(0))
for m in re.finditer(r'W\s*=\s*\(\)\s*=>[^;,]+[;,]', txt):
    print("Found W function:", m.group(0))
