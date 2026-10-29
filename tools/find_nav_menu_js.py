import glob, re

for f in glob.glob('site/_nuxt/*.js'):
    txt = open(f, encoding='utf-8').read()
    if 'menu-button' in txt or 'menu-icon' in txt:
        print(f"Found in {f}")
        for m in re.finditer(r'.{0,100}menu-button.{0,100}', txt):
            print("  ", m.group(0))
