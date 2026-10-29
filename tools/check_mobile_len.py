txt = open('site/_nuxt/entry.DzM0mqX9.css', encoding='utf-8').read()

idx = txt.find('@media screen and (max-width: 767.98px)')
print("Mobile block starts at:", idx)
print("Total length of file:", len(txt))
print("Mobile block content length:", len(txt) - idx)
