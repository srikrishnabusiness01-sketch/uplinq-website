with open('site/_nuxt/CKrmhtJt.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('menu-button')
while idx != -1:
    print(f"Found at {idx}: {c[max(0, idx-50):min(len(c), idx+150)]}")
    idx = c.find('menu-button', idx+1)
