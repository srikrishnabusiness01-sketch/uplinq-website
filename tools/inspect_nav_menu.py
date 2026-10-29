with open('site/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = 0
while True:
    idx = h.find('Menu', idx)
    if idx == -1: break
    print(f"Found Menu at {idx}: {h[max(0, idx-50):min(len(h), idx+150)]}")
    idx += len('Menu')
