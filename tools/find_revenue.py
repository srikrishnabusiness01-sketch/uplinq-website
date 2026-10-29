with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('REVENUE')
while idx != -1:
    print(f"--- Found at {idx} ---")
    print(html[idx-100:idx+200])
    idx = html.find('REVENUE', idx + 1)
