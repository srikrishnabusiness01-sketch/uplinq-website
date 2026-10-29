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
        rgb = im.convert('RGB')
        w, h = rgb.size
        top_col = rgb.getpixel((w//2, 2))
        bot_col = rgb.getpixel((w//2, h - 3))
        left_col = rgb.getpixel((2, h//2))
        right_col = rgb.getpixel((w - 3, h//2))
        print(f"\n--- {name} ({w}x{h}) ---")
        print(f"Top: {top_col} | Bottom: {bot_col}")
        print(f"Left: {left_col} | Right: {right_col}")
