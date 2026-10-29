from PIL import Image

im = Image.open(r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793256921255_a351c4cc.webp')
rgb = im.convert('RGB')
w, h = rgb.size

top_content_y = h
for y in range(h):
    for x in range(w):
        p = rgb.getpixel((x, y))
        # check if not white/near-white
        if p[0] < 240 or p[1] < 240 or p[2] < 240:
            top_content_y = min(top_content_y, y)
            break
    if top_content_y < h:
        break

print('Top content starts at y =', top_content_y)
