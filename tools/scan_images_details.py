import os
import re
import xml.etree.ElementTree as ET
from PIL import Image

def get_image_info(filepath):
    if not os.path.exists(filepath):
        return None
    
    file_size_bytes = os.path.getsize(filepath)
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.svg':
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            width = root.get('width')
            height = root.get('height')
            viewbox = root.get('viewBox')
            
            w, h = None, None
            if width and height:
                w = float(re.sub(r'[^\d.]', '', width))
                h = float(re.sub(r'[^\d.]', '', height))
            elif viewbox:
                parts = [float(p) for p in viewbox.replace(',', ' ').split() if p]
                if len(parts) == 4:
                    w = parts[2]
                    h = parts[3]
            
            if w and h and h > 0:
                ratio = round(w / h, 2)
                return {
                    'width': int(w),
                    'height': int(h),
                    'ratio': f"{w/h:.2f}:1",
                    'simplified_ratio': simplify_ratio(int(w), int(h)),
                    'size_kb': round(file_size_bytes / 1024, 1),
                    'format': 'SVG'
                }
            return {
                'width': 'vector',
                'height': 'vector',
                'ratio': 'scalable',
                'simplified_ratio': 'vector',
                'size_kb': round(file_size_bytes / 1024, 1),
                'format': 'SVG'
            }
        except Exception as e:
            return {
                'width': 'vector',
                'height': 'vector',
                'ratio': 'unknown',
                'simplified_ratio': 'vector',
                'size_kb': round(file_size_bytes / 1024, 1),
                'format': 'SVG'
            }
    else:
        try:
            with Image.open(filepath) as im:
                w, h = im.size
                ratio = round(w / h, 2)
                return {
                    'width': w,
                    'height': h,
                    'ratio': f"{ratio}:1",
                    'simplified_ratio': simplify_ratio(w, h),
                    'size_kb': round(file_size_bytes / 1024, 1),
                    'format': im.format or ext.replace('.', '').upper()
                }
        except Exception as e:
            return {
                'width': 'error',
                'height': 'error',
                'ratio': 'error',
                'simplified_ratio': 'error',
                'size_kb': round(file_size_bytes / 1024, 1),
                'format': ext.replace('.', '').upper(),
                'error': str(e)
            }

def simplify_ratio(w, h):
    from math import gcd
    if not isinstance(w, int) or not isinstance(h, int) or h == 0:
        return ""
    # approximate common ratios
    r = w / h
    if abs(r - 1.0) < 0.05: return "1:1 (Square)"
    if abs(r - 16/9) < 0.05: return "16:9 (Landscape)"
    if abs(r - 4/3) < 0.05: return "4:3 (Landscape)"
    if abs(r - 3/2) < 0.05: return "3:2 (Landscape)"
    if abs(r - 5/4) < 0.05: return "5:4 (Landscape)"
    if abs(r - 21/9) < 0.05: return "21:9 (Ultrawide)"
    if abs(r - 9/16) < 0.05: return "9:16 (Portrait)"
    if abs(r - 3/4) < 0.05: return "3:4 (Portrait)"
    if abs(r - 2/3) < 0.05: return "2:3 (Portrait)"
    if abs(r - 4/5) < 0.05: return "4:5 (Portrait)"
    g = gcd(w, h)
    return f"{w//g}:{h//g}"

# Now let's list every image on the homepage and across the site
homepage_images = [
    # Hero / Header
    {
        'section': 'Hero Section (Mobile Poster)',
        'element': 'Video poster fallback / Mobile preview',
        'rel_path': 'site/assets/mdn/photo-video-thumbnail-gfb5anjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-video-thumbnail-gfb5anjpg-t0wMA.jpe'
    },
    # Sketch Section (About)
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Sketch 1: Plan/Understand illustration',
        'rel_path': 'site/_nuxt/home-about-illustration.CNh6-gmc.svg',
        'url': '/_nuxt/home-about-illustration.CNh6-gmc.svg'
    },
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Divider 1: Slant line',
        'rel_path': 'site/_nuxt/home-about-slant.BK8NVZZL.svg',
        'url': '/_nuxt/home-about-slant.BK8NVZZL.svg'
    },
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Sketch 2: Design/Position illustration',
        'rel_path': 'site/_nuxt/home-about-illustration-2.CBM_FEvc.svg',
        'url': '/_nuxt/home-about-illustration-2.CBM_FEvc.svg'
    },
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Divider 2: Slant line 2',
        'rel_path': 'site/_nuxt/home-about-slant-2.BY4DzBxE.svg',
        'url': '/_nuxt/home-about-slant-2.BY4DzBxE.svg'
    },
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Sketch 3: Code/Build illustration',
        'rel_path': 'site/_nuxt/home-about-illustration-3.mEgxrqTy.svg',
        'url': '/_nuxt/home-about-illustration-3.mEgxrqTy.svg'
    },
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Divider 3: Slant line 3',
        'rel_path': 'site/_nuxt/home-about-slant-3.CQaeGBYA.svg',
        'url': '/_nuxt/home-about-slant-3.CQaeGBYA.svg'
    },
    {
        'section': 'About Section ("Together, we turn")',
        'element': 'Sketch 4: Launch/Ship illustration',
        'rel_path': 'site/_nuxt/home-about-illustration-4.B3s7jbUm.svg',
        'url': '/_nuxt/home-about-illustration-4.B3s7jbUm.svg'
    },
    # Services 3 Blocks
    {
        'section': 'Services Section (3 Blocks)',
        'element': 'Block 1: Strategy sketch',
        'rel_path': 'site/_nuxt/service-illustration-strategy.D7qO1f4r.svg',
        'url': '/_nuxt/service-illustration-strategy.D7qO1f4r.svg'
    },
    {
        'section': 'Services Section (3 Blocks)',
        'element': 'Block 2: Growth sketch (formerly Digital)',
        'rel_path': 'site/_nuxt/service-illustration-digital.WtCOjdL4.svg',
        'url': '/_nuxt/service-illustration-digital.WtCOjdL4.svg'
    },
    {
        'section': 'Services Section (3 Blocks)',
        'element': 'Block 3: AI sketch (formerly Brand)',
        'rel_path': 'site/_nuxt/service-illustration-brand.Dw0Et53h.svg',
        'url': '/_nuxt/service-illustration-brand.Dw0Et53h.svg'
    },
    # Impact Hover Gallery (Win in Strategy, Revenue, Growth)
    {
        'section': 'Impact Words Gallery ("Win In")',
        'element': 'Win image 1 (Top Left): Neon abstract shape / growth visual',
        'rel_path': 'site/assets/mdn/photo-growth-img-1-xrt0cbjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-growth-img-1-xrt0cbjpg-t0wMA.jpe'
    },
    {
        'section': 'Impact Words Gallery ("Win In")',
        'element': 'Win image 2 (Top Center): Speed / motion kinetic visual',
        'rel_path': 'site/assets/mdn/photo-speed-img-jtiybwjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-speed-img-jtiybwjpg-t0wMA.jpe'
    },
    {
        'section': 'Impact Words Gallery ("Win In")',
        'element': 'Win image 3 (Top Right): Growth graph / geometric artwork',
        'rel_path': 'site/assets/mdn/photo-growth-img-2-wnhqpqjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-growth-img-2-wnhqpqjpg-t0wMA.jpe'
    },
    {
        'section': 'Impact Words Gallery ("Win In")',
        'element': 'Win image 4 (Bottom Left): Modern brand / typography showcase',
        'rel_path': 'site/_nuxt/win-1.4kaXhrsf.jpg',
        'url': '/_nuxt/win-1.4kaXhrsf.jpg'
    },
    {
        'section': 'Impact Words Gallery ("Win In")',
        'element': 'Win image 5 (Bottom Center): Product / mobile dashboard UI',
        'rel_path': 'site/assets/mdn/photo-propel-img-bd9nyqjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-propel-img-bd9nyqjpg-t0wMA.jpe'
    },
    {
        'section': 'Impact Words Gallery ("Win In")',
        'element': 'Win image 6 (Bottom Right): High impact aesthetic visual',
        'rel_path': 'site/assets/mdn/photo-adidas-b7szujjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-adidas-b7szujjpg-t0wMA.jpe'
    },
    # Company Story (Stats right panel)
    {
        'section': 'Company Story (Right Panel Rotating Cards)',
        'element': 'Story Visual 1: Globe / International market visual',
        'rel_path': 'site/assets/mdn/photo-thumbnail-1-qyy5fajpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-thumbnail-1-qyy5fajpg-t0wMA.jpe'
    },
    {
        'section': 'Company Story (Right Panel Rotating Cards)',
        'element': 'Story Visual 2: B2B Growth / revenue metric graphic',
        'rel_path': 'site/assets/mdn/photo-thumbnail-2-uk6shujpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-thumbnail-2-uk6shujpg-t0wMA.jpe'
    },
    {
        'section': 'Company Story (Right Panel Rotating Cards)',
        'element': 'Story Visual 3: Town / enterprise ecosystem building',
        'rel_path': 'site/assets/mdn/photo-thumbnail-3-kstjpsjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-thumbnail-3-kstjpsjpg-t0wMA.jpe'
    },
    {
        'section': 'Company Story (Right Panel Rotating Cards)',
        'element': 'Story Visual 4: Customer connection / handshake/globe visual',
        'rel_path': 'site/assets/mdn/photo-thumbnail-4-lfg5ygjpg-t0wMA.jpe',
        'url': '/assets/mdn/photo-thumbnail-4-lfg5ygjpg-t0wMA.jpe'
    },
    # How We Work (5 Cards)
    {
        'section': 'How We Work (Card 1: Understand)',
        'element': 'Card 1 Cover Thumbnail',
        'rel_path': 'site/assets/cdn/6a0ec808a39e8bbc34a44724_nlng-thumbnail_compressed.webp',
        'url': '/assets/cdn/6a0ec808a39e8bbc34a44724_nlng-thumbnail_compressed.webp'
    },
    {
        'section': 'How We Work (Card 2: Research)',
        'element': 'Card 2 Cover Thumbnail',
        'rel_path': 'site/assets/cdn/67d7c279e37df6ae8ed39fb9_quidax-cover.webp',
        'url': '/assets/cdn/67d7c279e37df6ae8ed39fb9_quidax-cover.webp'
    },
    {
        'section': 'How We Work (Card 3: Position)',
        'element': 'Card 3 Cover Thumbnail',
        'rel_path': 'site/assets/cdn/673216ce8e2a141a3895f7c1_kele-cover.webp',
        'url': '/assets/cdn/673216ce8e2a141a3895f7c1_kele-cover.webp'
    },
    {
        'section': 'How We Work (Card 4: Reach)',
        'element': 'Card 4 Cover Thumbnail',
        'rel_path': 'site/assets/cdn/670fddc84610217f70b0b1bb_autograph-cover.webp',
        'url': '/assets/cdn/670fddc84610217f70b0b1bb_autograph-cover.webp'
    },
    {
        'section': 'How We Work (Card 5: Grow)',
        'element': 'Card 5 Cover Thumbnail',
        'rel_path': 'site/assets/cdn/66aa235dc0d81f08040cda27_propel-cover.webp',
        'url': '/assets/cdn/66aa235dc0d81f08040cda27_propel-cover.webp'
    }
]

print("Scanning images...")
for item in homepage_images:
    info = get_image_info(item['rel_path'])
    item['info'] = info
    print(f"\n--- {item['section']} : {item['element']} ---")
    print(f"Path: {item['rel_path']}")
    if info:
        print(f"Dimensions: {info['width']} x {info['height']} px | Ratio: {info['ratio']} ({info['simplified_ratio']}) | Size: {info['size_kb']} KB | Format: {info['format']}")
    else:
        print("FILE NOT FOUND!")
