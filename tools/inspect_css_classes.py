import re

with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    css = f.read()

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
    matches = re.findall(rf'(\.{cls}[^{{]*\{{[^}}]*\}})', css)
    print(f"=== CSS FOR .{cls} ===")
    for m in matches[:5]:
        print(m)
