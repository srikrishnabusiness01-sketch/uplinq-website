from PIL import Image
import os

files = [
    'win-1.4kaXhrsf.jpg',
    'photo-growth-img-1-xrt0cbjpg-t0wMA.jpe',
    'photo-speed-img-jtiybwjpg-t0wMA.jpe',
    'photo-propel-img-bd9nyqjpg-t0wMA.jpe',
    'photo-growth-img-2-wnhqpqjpg-t0wMA.jpe',
    'photo-adidas-b7szujjpg-t0wMA.jpe',
    'photo-thumbnail-1-qyy5fajpg-t0wMA.jpe',
    'photo-thumbnail-2-uk6shujpg-t0wMA.jpe',
    'photo-thumbnail-3-kstjpsjpg-t0wMA.jpe',
    'photo-thumbnail-4-lfg5ygjpg-t0wMA.jpe'
]

for f in files:
    p = os.path.join('backup_original_images', f)
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"{f}: {im.size}, mode={im.mode}")
    else:
        print(f"{f}: NOT FOUND")
