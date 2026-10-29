from PIL import Image

for i in [1, 2, 3, 4]:
    p = f'site/assets/mdn/photo-thumbnail-{i}-*.jpe'
    import glob
    matches = glob.glob(f'site/assets/mdn/photo-thumbnail-{i}-*')
    for m in matches:
        with Image.open(m) as im:
            # Check average color / sample pixels
            print(m, im.size, im.mode)
            colors = im.getcolors(maxcolors=1000)
            print("  Sample color:", im.getpixel((10, 10)))
