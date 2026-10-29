with open('site/_nuxt/CB5bwoBe.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('splitWordsByCommas')
if idx != -1:
    print(c[idx:idx+300])
else:
    # search across all nuxt files
    import glob
    for p in glob.glob('site/_nuxt/*.js'):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            t = f.read()
        if 'splitWordsByCommas' in t:
            print("Found in", p)
            i = t.find('splitWordsByCommas')
            print(t[i:i+300])
