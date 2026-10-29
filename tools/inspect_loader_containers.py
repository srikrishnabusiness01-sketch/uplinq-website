with open('site/_nuxt/B0CwXBEy.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('loader-scroll_container')
while idx != -1:
    print(idx, js[max(0, idx - 100):min(len(js), idx + 200)])
    print("=" * 60)
    idx = js.find('loader-scroll_container', idx + 25)
