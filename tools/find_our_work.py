with open('site/_nuxt/BMQH0uFj.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Our Work')
if idx != -1:
    print("Found 'Our Work' in BMQH0uFj.js at", idx)
    print(c[max(0, idx-100):min(len(c), idx+200)])
else:
    print("'Our Work' not found in BMQH0uFj.js")
