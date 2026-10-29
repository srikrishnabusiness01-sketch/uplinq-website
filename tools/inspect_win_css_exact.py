import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

classes = [
    'win-category_wrapper',
    'win-img_wrapper',
    'win-img_block',
    'win-category'
]

for cls in classes:
    print(f"\n=== CSS for .{cls} ===")
    matches = re.findall(rf'(\.{cls}[^{{]*\{{[^}}]*\}})', html)
    for m in matches:
        print(m)
