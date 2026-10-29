import glob

for fpath in glob.glob('site/_nuxt/*.js'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'menu-button' in c and 'Menu' in c:
        print("Found in JS:", fpath)
