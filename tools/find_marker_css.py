txt = open('site/_nuxt/entry.DzM0mqX9.css', encoding='utf-8').read()

marker = '/* ============================================================\n   MOBILE RESPONSIVE STYLES (Screen sizes below 768px)'
if marker not in txt:
    marker = 'MOBILE RESPONSIVE STYLES'

idx = txt.find(marker)
print("Found marker at:", idx)
print("Before marker:", repr(txt[idx-100:idx]))
print("End of file from marker:", len(txt[idx:]))
