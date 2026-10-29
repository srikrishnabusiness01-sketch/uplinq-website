with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

terms = ['.menu-button', '.menu-icon', '.page-progress', '.nav-inner', '.nav-logo', '.menu-link']
for t in terms:
    idx = 0
    print(f"=== Searching for {t} ===")
    found = 0
    while idx != -1 and found < 4:
        idx = c.find(t, idx)
        if idx != -1:
            start = max(0, idx - 40)
            end = min(len(c), idx + 100)
            print("  ", c[start:end].replace('\n', ' '))
            idx += len(t)
            found += 1
