import glob, re

for f in sorted(glob.glob('site/_nuxt/*.js')):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    # Find any phrase like "Let's ..." or "Lets ..."
    matches = re.findall(r"Let(?:'|&#39;|\\')s\s+[A-Za-z]+", txt, re.IGNORECASE)
    if matches:
        print(f"{f}: {set(matches)}")
