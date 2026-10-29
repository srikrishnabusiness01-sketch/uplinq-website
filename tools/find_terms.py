with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for term in ['help them win', 'STRATEGY', 'GROWTH', 'win']:
    idx = html.find(term)
    print(f"Term '{term}': idx={idx}")
    if idx != -1:
        print(html[idx-100:idx+200])
