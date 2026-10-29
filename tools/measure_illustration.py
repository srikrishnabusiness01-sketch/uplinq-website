from PIL import Image

# Let's extract frame from site/assets/mdn/video-website-loop-ucoly5mp4-t0wMA.mp4
# Or use tools/sample_frame_3s.jpg (which is 720x720)
im = Image.open('tools/sample_frame_3s.jpg')
w, h = im.size

# Find bounds of computer vs boy
# Computer is on the left, boy is on the right
# Let's find horizontal center of computer and horizontal center of boy
non_white = []
for y in range(h):
    for x in range(w):
        r, g, b = im.getpixel((x, y))[:3]
        if r < 240 or g < 240 or b < 240:
            non_white.append((x, y))

min_x = min(p[0] for p in non_white)
max_x = max(p[0] for p in non_white)
min_y = min(p[1] for p in non_white)
max_y = max(p[1] for p in non_white)

print(f"Total non-white bounds in 720x720: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
print(f"Width: {max_x - min_x}, Height: {max_y - min_y}")
print(f"Center: x = {(min_x + max_x)/2}, y = {(min_y + max_y)/2}")
