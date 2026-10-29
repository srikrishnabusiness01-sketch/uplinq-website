with open('site/_nuxt/Dl_6lvg3.js', 'r', encoding='utf-8') as f:
    js = f.read()

for w in ['twitter.com', 'linkedin.com', 'facebook.com']:
    idx = js.find(w)
    if idx != -1:
        print(f"--- {w} in Dl_6lvg3.js ---")
        print(js[idx-100:idx+250])
