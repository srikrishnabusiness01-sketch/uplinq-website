import os
from PIL import Image

uploaded = [
    ('Image 1 (Team)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921255_a351c4cc.webp'),
    ('Image 2 (Handshake)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921257_9a18ce04.jpg'),
    ('Image 3 (Magnifying Glass)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921262_5d01ef50.jpg'),
    ('Image 4 (Book Stairs)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921262_d0494391.jpg'),
    ('Image 5 (Binoculars)', r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921269_bcbd917b.jpg')
]

for name, path in uploaded:
    with Image.open(path) as im:
        rgb = im.convert('RGB')
        w, h = im.size
        # Sample corners and edge centers
        top_left = rgb.getpixel((5, 5))
        top_right = rgb.getpixel((w - 6, 5))
        bottom_left = rgb.getpixel((5, h - 6))
        bottom_right = rgb.getpixel((w - 6, h - 6))
        left_mid = rgb.getpixel((5, h // 2))
        right_mid = rgb.getpixel((w - 6, h // 2))
        print(f"\n--- {name} ({w}x{h}) ---")
        print(f"Top-Left: {top_left} | Top-Right: {top_right}")
        print(f"Left-Mid: {left_mid} | Right-Mid: {right_mid}")
        print(f"Bottom-Left: {bottom_left} | Bottom-Right: {bottom_right}")
