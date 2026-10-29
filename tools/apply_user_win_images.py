import os
import shutil
from PIL import Image

TARGET_RATIO = 1.465

win_slots = [
    {
        'name': 'STRATEGY Top-Right (Pen/Notepad)',
        'src': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258912057_1cbbbe86.jpg',
        'target': r'site\assets\mdn\photo-growth-img-1-xrt0cbjpg-t0wMA.jpe',
        'target_w': 947,
        'target_h': 648
    },
    {
        'name': 'STRATEGY Bottom-Left (Megaphones)',
        'src': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258912056_22e56e2f.jpg',
        'target': r'site\_nuxt\win-1.4kaXhrsf.jpg',
        'target_w': 1176,
        'target_h': 804
    },
    {
        'name': 'REVENUE Top-Right (Man at Laptop)',
        'src': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925179_556bc037.jpg',
        'target': r'site\assets\mdn\photo-speed-img-jtiybwjpg-t0wMA.jpe',
        'target_w': 1176,
        'target_h': 804
    },
    {
        'name': 'REVENUE Bottom-Left (Woman Content/Layout)',
        'src': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925184_d3b5bc62.jpg',
        'target': r'site\assets\mdn\photo-propel-img-bd9nyqjpg-t0wMA.jpe',
        'target_w': 900,
        'target_h': 616
    },
    {
        'name': 'GROWTH Top-Right (Team High-Five)',
        'src': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925177_73418da6.jpg',
        'target': r'site\assets\mdn\photo-growth-img-2-wnhqpqjpg-t0wMA.jpe',
        'target_w': 968,
        'target_h': 662
    },
    {
        'name': 'GROWTH Bottom-Left (Team High-Five)',
        'src': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793258925177_73418da6.jpg',
        'target': r'site\assets\mdn\photo-adidas-b7szujjpg-t0wMA.jpe',
        'target_w': 1145,
        'target_h': 764
    }
]

def process_and_replace_win_images():
    for item in win_slots:
        print(f"\nProcessing {item['name']}...")
        if not os.path.exists(item['src']):
            print(f"Error: {item['src']} not found!")
            continue

        target_ratio = item['target_w'] / item['target_h']

        with Image.open(item['src']) as im:
            im = im.convert('RGB')
            w, h = im.size

            # Extend height to match 3:2 target ratio without cropping width
            canvas_h = int(w / target_ratio)
            pad_y = (canvas_h - h) // 2

            canvas = Image.new('RGB', (w, canvas_h))
            canvas.paste(im, (0, pad_y))

            # Replicate top row upwards
            top_row = im.crop((0, 0, w, 1))
            for y in range(pad_y):
                canvas.paste(top_row, (0, y))

            # Replicate bottom row downwards
            bot_row = im.crop((0, h - 1, w, h))
            for y in range(pad_y + h, canvas_h):
                canvas.paste(bot_row, (0, y))

            # Resize with Lanczos to exact target dimensions
            final_img = canvas.resize((item['target_w'], item['target_h']), Image.Resampling.LANCZOS)

            # Save in matching format (JPEG)
            final_img.save(item['target'], 'JPEG', quality=94)
            print(f"Saved {item['name']} -> {item['target']} ({item['target_w']}x{item['target_h']})")

if __name__ == '__main__':
    process_and_replace_win_images()
