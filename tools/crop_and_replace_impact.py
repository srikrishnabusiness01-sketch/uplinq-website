import os
import shutil
from PIL import Image

artifact_dir = r"C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb"

impact_images = [
    {
        'name': 'Impact 1 (Strategy Top-Left)',
        'gen': os.path.join(artifact_dir, 'impact_img1_strategy_1793253133136.jpg'),
        'target': r'site\assets\mdn\photo-growth-img-1-xrt0cbjpg-t0wMA.jpe',
        'target_w': 947,
        'target_h': 648
    },
    {
        'name': 'Impact 2 (Revenue Top-Center)',
        'gen': os.path.join(artifact_dir, 'impact_img2_revenue_1793253138840.jpg'),
        'target': r'site\assets\mdn\photo-speed-img-jtiybwjpg-t0wMA.jpe',
        'target_w': 1920,
        'target_h': 1406
    },
    {
        'name': 'Impact 3 (Growth Top-Right)',
        'gen': os.path.join(artifact_dir, 'impact_img3_growth_1793253145701.jpg'),
        'target': r'site\assets\mdn\photo-growth-img-2-wnhqpqjpg-t0wMA.jpe',
        'target_w': 968,
        'target_h': 662
    },
    {
        'name': 'Impact 4 (Strategy Bottom-Left)',
        'gen': os.path.join(artifact_dir, 'impact_img4_strategy_1793253153783.jpg'),
        'target': r'site\_nuxt\win-1.4kaXhrsf.jpg',
        'target_w': 1176,
        'target_h': 804
    },
    {
        'name': 'Impact 5 (Revenue Bottom-Center)',
        'gen': os.path.join(artifact_dir, 'impact_img5_revenue_1793253154179.jpg'),
        'target': r'site\assets\mdn\photo-propel-img-bd9nyqjpg-t0wMA.jpe',
        'target_w': 900,
        'target_h': 616
    },
    {
        'name': 'Impact 6 (Growth Bottom-Right)',
        'gen': os.path.join(artifact_dir, 'impact_img6_growth_1793253159183.jpg'),
        'target': r'site\assets\mdn\photo-adidas-b7szujjpg-t0wMA.jpe',
        'target_w': 1145,
        'target_h': 764
    }
]

os.makedirs('backup_original_images', exist_ok=True)

def process_impact_images():
    for item in impact_images:
        print(f"\nProcessing {item['name']}...")
        if not os.path.exists(item['gen']):
            print(f"Error: Not found: {item['gen']}")
            continue

        backup_path = os.path.join('backup_original_images', os.path.basename(item['target']))
        if os.path.exists(item['target']) and not os.path.exists(backup_path):
            shutil.copy2(item['target'], backup_path)
            print(f"Backed up to {backup_path}")

        target_ratio = item['target_w'] / item['target_h']
        with Image.open(item['gen']) as im:
            orig_w, orig_h = im.size
            current_ratio = orig_w / orig_h
            if current_ratio < target_ratio:
                new_h = int(orig_w / target_ratio)
                top = (orig_h - new_h) // 2
                cropped = im.crop((0, top, orig_w, top + new_h))
            else:
                new_w = int(orig_h * target_ratio)
                left = (orig_w - new_w) // 2
                cropped = im.crop((left, 0, left + new_w, orig_h))

            resized = cropped.resize((item['target_w'], item['target_h']), Image.Resampling.LANCZOS)
            
            # Save in matching format (JPEG)
            resized.save(item['target'], 'JPEG', quality=92)
            print(f"Saved {item['name']} to {item['target']} ({item['target_w']}x{item['target_h']})")

if __name__ == '__main__':
    process_impact_images()
