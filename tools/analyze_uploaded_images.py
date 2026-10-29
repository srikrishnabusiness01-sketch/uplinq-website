import os
from PIL import Image

uploaded = [
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921255_a351c4cc.webp',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921257_9a18ce04.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921262_5d01ef50.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921262_d0494391.jpg',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921269_bcbd917b.jpg'
]

for idx, path in enumerate(uploaded):
    if os.path.exists(path):
        with Image.open(path) as im:
            w, h = im.size
            ratio = round(w / h, 2)
            print(f"Image {idx+1}: {os.path.basename(path)}")
            print(f"  Dimensions: {w}x{h} px | Ratio: {ratio}:1 ({w}:{h}) | Format: {im.format} | Mode: {im.mode}")
    else:
        print(f"Image {idx+1}: NOT FOUND at {path}")
