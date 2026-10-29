import xml.etree.ElementTree as ET

svgs = [
    'site/_nuxt/home-about-illustration.CNh6-gmc.svg',
    'site/_nuxt/home-about-illustration-2.CBM_FEvc.svg',
    'site/_nuxt/home-about-illustration-3.mEgxrqTy.svg',
    'site/_nuxt/home-about-illustration-4.B3s7jbUm.svg',
    'site/_nuxt/service-illustration-strategy.D7qO1f4r.svg',
    'site/_nuxt/service-illustration-digital.WtCOjdL4.svg',
    'site/_nuxt/service-illustration-brand.Dw0Et53h.svg'
]

for s in svgs:
    print(f"\n=== SVG: {s} ===")
    try:
        with open(s, 'r', encoding='utf-8') as f:
            txt = f.read()
        print(f"Length: {len(txt)} chars")
        # print first 300 chars
        print(txt[:300].replace('\n', ' '))
    except Exception as e:
        print(f"Error: {e}")
