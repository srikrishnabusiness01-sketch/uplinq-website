import glob, re

for f in sorted(glob.glob('site/_nuxt/*.js')):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    if 'c-popup' in txt or 'contact' in txt.lower():
        # Let's search for what opens the popup or modal
        for keyword in ['contact', 'popup', 'modal', 'openModal', 'isOpen', 'isContact', '$scontact']:
            if keyword in txt:
                print(f"{f} has {keyword}")
