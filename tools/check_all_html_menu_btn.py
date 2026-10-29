import glob

for p in glob.glob('site/**/*.html', recursive=True):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'class="menu-button"' in c:
        print(f"Present in {p}")
    else:
        print(f"NOT present in {p}")
