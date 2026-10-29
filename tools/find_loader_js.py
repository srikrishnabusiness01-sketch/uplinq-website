with open('site/_nuxt/B0CwXBEy.js', 'r', encoding='utf-8') as f:
    js = f.read()

words = ['Reimagine', 'RETHINK', 'LOADING CHECK', 'LOADING STRATEGY']
for w in words:
    idx = js.find(w)
    if idx != -1:
        print(f"Found '{w}' at {idx}:")
        print(js[max(0, idx - 100):min(len(js), idx + 200)])
        print("-" * 50)
