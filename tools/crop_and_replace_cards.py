import os
import shutil
from PIL import Image

cards = [
    {
        'name': 'Card 1 (Understand)',
        'gen': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\card1_understand_1793252891346.jpg',
        'target': r'site\assets\cdn\6a0ec808a39e8bbc34a44724_nlng-thumbnail_compressed.webp',
        'target_w': 3840,
        'target_h': 1600,
        'target_ratio': 3840 / 1600
    },
    {
        'name': 'Card 2 (Research)',
        'gen': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\card2_research_1793252949809.jpg',
        'target': r'site\assets\cdn\67d7c279e37df6ae8ed39fb9_quidax-cover.webp',
        'target_w': 1300,
        'target_h': 517,
        'target_ratio': 1300 / 517
    },
    {
        'name': 'Card 3 (Position)',
        'gen': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\card3_position_1793252956418.jpg',
        'target': r'site\assets\cdn\673216ce8e2a141a3895f7c1_kele-cover.webp',
        'target_w': 1950,
        'target_h': 779,
        'target_ratio': 1950 / 779
    },
    {
        'name': 'Card 4 (Reach)',
        'gen': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\card4_reach_1793252960069.jpg',
        'target': r'site\assets\cdn\670fddc84610217f70b0b1bb_autograph-cover.webp',
        'target_w': 1950,
        'target_h': 776,
        'target_ratio': 1950 / 776
    },
    {
        'name': 'Card 5 (Grow)',
        'gen': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\card5_grow_1793252971462.jpg',
        'target': r'site\assets\cdn\66aa235dc0d81f08040cda27_propel-cover.webp',
        'target_w': 2600,
        'target_h': 1034,
        'target_ratio': 2600 / 1034
    }
]

os.makedirs('backup_original_images', exist_ok=True)

def process_and_replace():
    for c in cards:
        print(f"\nProcessing {c['name']}...")
        if not os.path.exists(c['gen']):
            print(f"Error: Generated image {c['gen']} not found!")
            continue
        
        # Backup original
        backup_path = os.path.join('backup_original_images', os.path.basename(c['target']))
        if os.path.exists(c['target']) and not os.path.exists(backup_path):
            shutil.copy2(c['target'], backup_path)
            print(f"Backed up original to {backup_path}")

        # Open and crop
        with Image.open(c['gen']) as im:
            orig_w, orig_h = im.size
            current_ratio = orig_w / orig_h
            target_ratio = c['target_ratio']
            
            # If current ratio is narrower than target, crop height
            if current_ratio < target_ratio:
                new_h = int(orig_w / target_ratio)
                top = (orig_h - new_h) // 2
                bottom = top + new_h
                cropped = im.crop((0, top, orig_w, bottom))
            else:
                new_w = int(orig_h * target_ratio)
                left = (orig_w - new_w) // 2
                right = left + new_w
                cropped = im.crop((left, 0, right, orig_h))
            
            # Resize with Lanczos
            resized = cropped.resize((c['target_w'], c['target_h']), Image.Resampling.LANCZOS)
            
            # Save as WebP
            resized.save(c['target'], 'WEBP', quality=92, method=6)
            print(f"Saved {c['name']} to {c['target']} ({c['target_w']}x{c['target_h']})")

if __name__ == '__main__':
    process_and_replace()
