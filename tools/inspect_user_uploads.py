from PIL import Image
import os

images = [
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258912056_22e56e2f.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258912057_1cbbbe86.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925177_73418da6.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925179_556bc037.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925184_d3b5bc62.jpg'
]

for idx, p in enumerate(images):
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"User Upload {idx+1}: {p}")
            print(f"  Size: {im.size}, Format: {im.format}")
    else:
        print(f"User Upload {idx+1}: NOT FOUND")
