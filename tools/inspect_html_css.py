import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

classes = [
    'thumbnail-img_block',
    'win-img_block',
    'stats-sketch_block',
    'about-sketch_block',
    'service-block_sketch',
    'header-video_block',
    'c-img',
    'project-thumbnail'
]

for cls in classes:
    matches = re.findall(rf'(\.{cls}[^{{]*\{{[^}}]*\}})', html)
    print(f"=== CSS FOR .{cls} ===")
    for m in matches[:5]:
        print(m)
