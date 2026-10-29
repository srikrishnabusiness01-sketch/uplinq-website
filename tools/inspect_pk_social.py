import re

with open('site/_nuxt/pK72Md3I.js', 'r', encoding='utf-8') as f:
    js = f.read()

for url in [
    'https://www.instagram.com/wearecheck_/',
    'https://twitter.com/wearecheck_',
    'https://www.linkedin.com/company/wearecheck/',
    'https://medium.com/@wearecheck'
]:
    idx = js.find(url)
    if idx != -1:
        print(f"\n--- URL: {url} ---")
        print(js[max(0, idx-100):min(len(js), idx+200)])
