import glob

for fpath in glob.glob('site/**', recursive=True):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        if '<button class="menu-button"><div>Menu</div><div class="menu-icon"></div></button>' in c:
            print("Found exact menu-button in HTML:", fpath)
        elif 'class="menu-button"' in c and 'Menu' in c:
            print("Found menu-button in:", fpath)
    except:
        pass
