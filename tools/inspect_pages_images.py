import os
import re
from PIL import Image
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def get_img_dims(local_path):
    if not os.path.exists(local_path):
        return None
    ext = os.path.splitext(local_path)[1].lower()
    size_kb = round(os.path.getsize(local_path) / 1024, 1)
    if ext == '.svg':
        try:
            tree = ET.parse(local_path)
            root = tree.getroot()
            w = root.get('width')
            h = root.get('height')
            vb = root.get('viewBox')
            if w and h:
                w_val = float(re.sub(r'[^\d.]', '', w))
                h_val = float(re.sub(r'[^\d.]', '', h))
            elif vb:
                parts = [float(p) for p in vb.replace(',', ' ').split() if p]
                w_val, h_val = parts[2], parts[3]
            else:
                return {'w': 'vector', 'h': 'vector', 'ratio': 'vector', 'kb': size_kb, 'fmt': 'SVG'}
            ratio = round(w_val / h_val, 2)
            return {'w': int(w_val), 'h': int(h_val), 'ratio': f"{ratio}:1", 'kb': size_kb, 'fmt': 'SVG'}
        except:
            return {'w': 'vector', 'h': 'vector', 'ratio': 'vector', 'kb': size_kb, 'fmt': 'SVG'}
    else:
        try:
            with Image.open(local_path) as im:
                w, h = im.size
                ratio = round(w / h, 2)
                return {'w': w, 'h': h, 'ratio': f"{ratio}:1", 'kb': size_kb, 'fmt': im.format or ext.upper()}
        except Exception as e:
            return {'error': str(e), 'kb': size_kb, 'fmt': ext.upper()}

pages = {
    'Home (index.html)': 'site/index.html',
    'About (about/index.html)': 'site/about/index.html',
    'Services (services/index.html)': 'site/services/index.html',
    'Work (work/index.html)': 'site/work/index.html',
}

for page_name, page_path in pages.items():
    print(f"\n=======================================================")
    print(f"PAGE: {page_name}")
    print(f"=======================================================")
    with open(page_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    seen = set()
    for img in soup.find_all('img'):
        src = img.get('src')
        if not src or src in seen:
            continue
        seen.add(src)
        
        # Resolve local path
        clean_src = src.split('?')[0]
        if clean_src.startswith('/'):
            local_path = os.path.join('site', clean_src.lstrip('/'))
        else:
            local_path = os.path.join('site', clean_src)
        
        info = get_img_dims(local_path)
        p_cls = img.parent.get('class', []) if img.parent else []
        print(f"SRC: {src}")
        print(f"  Parent: {img.parent.name if img.parent else ''}.{p_cls} | Alt: {img.get('alt', '')}")
        if info:
            print(f"  Dims: {info.get('w')}x{info.get('h')} | Ratio: {info.get('ratio')} | Size: {info.get('kb')} KB | Fmt: {info.get('fmt')}")
        else:
            print(f"  Dims: NOT FOUND at {local_path}")
