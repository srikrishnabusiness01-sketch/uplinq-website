import os
import shutil
from PIL import Image

cards_config = [
    {
        'card_num': 1,
        'step_name': 'Understand',
        'source_file': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921262_5d01ef50.jpg',
        'target_file': r'site\assets\cdn\6a0ec808a39e8bbc34a44724_nlng-thumbnail_compressed.webp',
        'target_w': 3840,
        'target_h': 1600,
        'bg_color': (244, 241, 236),
        'method': 'extend_solid'
    },
    {
        'card_num': 2,
        'step_name': 'Research',
        'source_file': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921269_bcbd917b.jpg',
        'target_file': r'site\assets\cdn\67d7c279e37df6ae8ed39fb9_quidax-cover.webp',
        'target_w': 1300,
        'target_h': 517,
        'bg_color': (36, 156, 180),
        'method': 'extend_solid'
    },
    {
        'card_num': 3,
        'step_name': 'Position',
        'source_file': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921262_d0494391.jpg',
        'target_file': r'site\assets\cdn\673216ce8e2a141a3895f7c1_kele-cover.webp',
        'target_w': 1950,
        'target_h': 779,
        'bg_color': (199, 232, 237),
        'method': 'extend_solid'
    },
    {
        'card_num': 4,
        'step_name': 'Reach',
        'source_file': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921257_9a18ce04.jpg',
        'target_file': r'site\assets\cdn\670fddc84610217f70b0b1bb_autograph-cover.webp',
        'target_w': 1950,
        'target_h': 776,
        'bg_color': (36, 156, 180),
        'method': 'extend_solid'
    },
    {
        'card_num': 5,
        'step_name': 'Grow',
        'source_file': r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921255_a351c4cc.webp',
        'target_file': r'site\assets\cdn\66aa235dc0d81f08040cda27_propel-cover.webp',
        'target_w': 2600,
        'target_h': 1034,
        'method': 'extend_edge'
    }
]

def process_and_deploy_cards():
    os.makedirs('backup_original_images', exist_ok=True)
    
    for c in cards_config:
        print(f"\nProcessing Card {c['card_num']}: {c['step_name']}...")
        if not os.path.exists(c['source_file']):
            print(f"Error: Source file {c['source_file']} not found!")
            continue

        target_ratio = c['target_w'] / c['target_h']

        with Image.open(c['source_file']) as im:
            im = im.convert('RGB')
            orig_w, orig_h = im.size
            
            if c['method'] == 'extend_solid':
                # Extend canvas horizontally so aspect ratio matches exactly
                canvas_w = int(orig_h * target_ratio)
                canvas_h = orig_h
                canvas = Image.new('RGB', (canvas_w, canvas_h), c['bg_color'])
                
                # Center paste
                offset_x = (canvas_w - orig_w) // 2
                canvas.paste(im, (offset_x, 0))

                # Smoothly feather edges if needed
                # Also replicate 1-px column to seamlessly merge any micro texture
                left_col = im.crop((0, 0, 1, orig_h))
                for x in range(offset_x):
                    canvas.paste(left_col, (x, 0))
                right_col = im.crop((orig_w - 1, 0, orig_w, orig_h))
                for x in range(offset_x + orig_w, canvas_w):
                    canvas.paste(right_col, (x, 0))

            elif c['method'] == 'extend_edge':
                canvas_w = int(orig_h * target_ratio)
                canvas_h = orig_h
                canvas = Image.new('RGB', (canvas_w, canvas_h), (252, 252, 252))
                offset_x = (canvas_w - orig_w) // 2
                canvas.paste(im, (offset_x, 0))

                # Replicate edge columns for 100% natural blend
                left_col = im.crop((0, 0, 1, orig_h))
                for x in range(offset_x):
                    canvas.paste(left_col, (x, 0))
                right_col = im.crop((orig_w - 1, 0, orig_w, orig_h))
                for x in range(offset_x + orig_w, canvas_w):
                    canvas.paste(right_col, (x, 0))

            # Resize with Lanczos to exact target dimensions
            final_img = canvas.resize((c['target_w'], c['target_h']), Image.Resampling.LANCZOS)
            
            # Save as high quality WebP
            final_img.save(c['target_file'], 'WEBP', quality=94, method=6)
            print(f"Saved Card {c['card_num']} ({c['step_name']}) -> {c['target_file']} ({c['target_w']}x{c['target_h']} WebP)")

if __name__ == '__main__':
    process_and_deploy_cards()
