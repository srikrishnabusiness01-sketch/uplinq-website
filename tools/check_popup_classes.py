import glob, re

for f in glob.glob('site/_nuxt/*.js'):
    txt = open(f, encoding='utf-8').read()
    if 'c-popup' in txt or 'popup-overlay' in txt:
        print(f"=== {f} has popup classes ===")
        for m in re.finditer(r'.{0,100}(?:c-popup|popup-overlay).{0,100}', txt):
            print("  ", m.group(0))
