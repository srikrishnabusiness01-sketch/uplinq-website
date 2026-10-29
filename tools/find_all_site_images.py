import glob
from bs4 import BeautifulSoup
import re

html_files = glob.glob('site/**/*.html', recursive=True)
print(f"Total HTML files: {len(html_files)}")

all_images = {}

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            if src not in all_images:
                all_images[src] = []
            all_images[src].append(hf)

print(f"Total unique img src across all HTML files: {len(all_images)}")
for src, pages in sorted(all_images.items()):
    print(f"\nSRC: {src}")
    print(f"  Pages ({len(pages)}): {pages[:3]}{'...' if len(pages)>3 else ''}")
