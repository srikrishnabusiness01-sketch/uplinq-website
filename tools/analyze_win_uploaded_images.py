import os
from PIL import Image

uploaded = [
    ('Image 1 (Megaphones)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258912056_22e56e2f.jpg'),
    ('Image 2 (Pen/Notepad)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258912057_1cbbbe86.jpg'),
    ('Image 3 (Team High-Five)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925177_73418da6.jpg'),
    ('Image 4 (Man at Laptop)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925179_556bc037.jpg'),
    ('Image 5 (Content/Layout)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925184_d3b5bc62.jpg')
]

for name, path in uploaded:
    with Image.open(path) as im:
        w, h = im.size
        ratio = round(w / h, 2)
        print(f"{name}:")
        print(f"  Dimensions: {w}x{h} px | Ratio: {ratio}:1 ({w}:{h}) | Format: {im.format} | Mode: {im.mode}")
