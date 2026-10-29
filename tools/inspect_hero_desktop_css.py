with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
rules = [
    r'\.header-title_wrapper[^{]*\{[^}]*\}',
    r'\.header-video_block[^{]*\{[^}]*\}',
    r'\.header-video[^{]*\{[^}]*\}',
    r'\.relative-block\.header-re[^{]*\{[^}]*\}',
    r'\.relative-block\.header-think[^{]*\{[^}]*\}',
    r'\.relative-block\.header-subtext[^{]*\{[^}]*\}',
]

for r in rules:
    print(f"=== Rule pattern: {r} ===")
    matches = re.findall(r, c)
    for m in matches:
        print(" ", m.strip().replace('\n', ' '))
