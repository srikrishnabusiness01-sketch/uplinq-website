import os
import re
import json
from bs4 import BeautifulSoup
from PIL import Image

def analyze_index_images():
    with open('site/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    print("=== IMG TAGS ON HOMEPAGE ===")
    img_list = []
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt')
        classes = img.get('class', [])
        parent = img.parent
        p_classes = parent.get('class', []) if parent else []
        p_name = parent.name if parent else ''
        img_list.append({
            'src': src,
            'alt': alt,
            'classes': classes,
            'parent': f"{p_name}.{' '.join(p_classes)}"
        })
        print(f"SRC: {src} | Parent: {p_name}.{p_classes} | Alt: {alt}")

    # Also check video tags
    print("\n=== VIDEO TAGS ON HOMEPAGE ===")
    for v in soup.find_all('video'):
        poster = v.get('poster')
        src = v.get('src')
        sources = [s.get('src') for s in v.find_all('source')]
        print(f"VIDEO src: {src} | poster: {poster} | sources: {sources} | parent: {v.parent.get('class')}")

    # Also check background images in style attributes or inline styles
    print("\n=== INLINE STYLE BACKGROUND IMAGES ===")
    for tag in soup.find_all(style=re.compile(r'url\(')):
        print(f"Tag: {tag.name}.{tag.get('class')} | Style: {tag['style']}")

    # Let's inspect the 5 project cards specifically!
    print("\n=== PROJECT CARDS IN HOMEPAGE ===")
    cards = soup.find_all('div', class_='project-card')
    print(f"Found {len(cards)} project-cards")
    for i, c in enumerate(cards):
        title = c.find(class_='project-card_title')
        title_text = title.get_text(strip=True) if title else "No title"
        imgs = c.find_all('img')
        vids = c.find_all('video')
        img_srcs = [im.get('src') for im in imgs]
        vid_srcs = [vd.get('src') or [s.get('src') for s in vd.find_all('source')] for vd in vids]
        print(f"Card {i+1}: '{title_text}' | Images: {img_srcs} | Videos: {vid_srcs}")

    # Let's check __NUXT_DATA__ for image assets used on the homepage
    s_tag = '<script type="application/json" id="__NUXT_DATA__" data-ssr="true">'
    s_idx = html.find(s_tag)
    if s_idx != -1:
        e_idx = html.find('</script>', s_idx)
        data = json.loads(html[s_idx+len(s_tag):e_idx])
        print("\n=== IMAGES IN __NUXT_DATA__ ===")
        cdn_images = set()
        for item in data:
            if isinstance(item, str) and ('/assets/' in item or item.endswith(('.webp', '.jpg', '.png', '.gif', '.svg'))):
                cdn_images.add(item)
        for img in sorted(cdn_images):
            print(f"NUXT DATA: {img}")

if __name__ == '__main__':
    analyze_index_images()
