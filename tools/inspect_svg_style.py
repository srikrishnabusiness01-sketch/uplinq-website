import re

svgs = [
    'site/_nuxt/service-illustration-strategy.D7qO1f4r.svg',
    'site/_nuxt/home-about-illustration.CNh6-gmc.svg'
]

for s in svgs:
    with open(s, 'r', encoding='utf-8') as f:
        txt = f.read()
    fills = set(re.findall(r'fill="([^"]+)"', txt))
    strokes = set(re.findall(r'stroke="([^"]+)"', txt))
    stroke_widths = set(re.findall(r'stroke-width="([^"]+)"', txt))
    print(f"\n--- {s} ---")
    print("Fills:", fills)
    print("Strokes:", strokes)
    print("Stroke widths:", stroke_widths)
