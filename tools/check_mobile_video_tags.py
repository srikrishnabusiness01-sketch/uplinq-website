txt1 = open('site/index.html', encoding='utf-8').read()
txt2 = open('site/_nuxt/BMQH0uFj.js', encoding='utf-8').read()

import re
print("index.html header-video_mobile:")
for m in re.finditer(r'<video[^>]+header-video_mobile[^>]*>', txt1):
    print(m.group(0))

print("\nBMQH0uFj.js header-video_mobile:")
for m in re.finditer(r'header-video_mobile[^}]+}', txt2):
    print(m.group(0))
