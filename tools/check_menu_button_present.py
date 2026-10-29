with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('class="menu-button" in index.html?', 'class="menu-button"' in c)
