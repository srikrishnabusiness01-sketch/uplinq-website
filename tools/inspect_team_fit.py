from PIL import Image

im1 = Image.open(r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921255_a351c4cc.webp')
w, h = im1.size
print('Image 1 size:', w, h)

# Target ratio = 2.514:1
# Option 1: Crop height
crop_h = int(w / 2.514)
print('Cropped height would be:', crop_h, 'cutting', h - crop_h, 'px total')

# Option 2: Extend canvas width
ext_w = int(h * 2.514)
print('Extended width would be:', ext_w, 'adding', ext_w - w, 'px total')
