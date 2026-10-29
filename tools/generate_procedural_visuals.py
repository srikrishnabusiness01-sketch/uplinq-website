import os
import math
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.makedirs('backup_original_images', exist_ok=True)

# -------------------------------------------------------------------
# Visual 2: "One Goal: Real Revenue" (3024 x 1249)
# -------------------------------------------------------------------
def render_visual2_real_revenue():
    W, H = 3024, 1249
    target = r'site\assets\mdn\photo-thumbnail-2-uk6shujpg-t0wMA.jpe'
    backup = r'backup_original_images\photo-thumbnail-2-uk6shujpg-t0wMA.jpe'
    if os.path.exists(target) and not os.path.exists(backup):
        shutil.copy2(target, backup)

    # Base dark gradient
    base = Image.new('RGB', (W, H), '#080B10')
    draw = ImageDraw.Draw(base)
    
    for y in range(H):
        ratio = y / H
        r = int(7 + ratio * 8)
        g = int(10 + ratio * 12)
        b = int(16 + ratio * 20)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Add subtle background grid lines
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=(20, 30, 45, 40), width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=(20, 30, 45, 40), width=1)

    # Glow Layer for Typography
    glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    font_path = r'site\assets\fonts\MangoGrotesque-Black.ttf'
    font_size = 460
    font = ImageFont.truetype(font_path, font_size)

    text = "REAL REVENUE"
    bbox = font.getbbox(text)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (W - text_w) // 2
    text_y = (H - text_h) // 2 - 40

    # Draw cyan glow beneath
    for r in range(40, 5, -5):
        glow_draw.text((text_x, text_y), text, font=font, fill=(0, 228, 255, 18))
    for r in range(20, 2, -3):
        glow_draw.text((text_x, text_y), text, font=font, fill=(169, 220, 30, 25))

    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(18))
    base.paste(Image.blend(base, glow_layer.convert('RGB'), 0.5), (0, 0))

    # Main text drawing
    draw = ImageDraw.Draw(base)
    # Deep shadow
    draw.text((text_x + 8, text_y + 12), text, font=font, fill=(5, 8, 14))
    # Titanium body
    draw.text((text_x, text_y), text, font=font, fill=(215, 225, 235))
    # Cyan edge highlight on top
    draw.text((text_x - 2, text_y - 2), text, font=font, fill=(0, 228, 255))
    draw.text((text_x, text_y), text, font=font, fill=(230, 238, 245))

    # Draw pipeline conduits beneath
    pipe_y = text_y + text_h + 90
    draw.line([(0, pipe_y), (W, pipe_y)], fill=(30, 50, 75), width=3)
    draw.line([(0, pipe_y + 16), (W, pipe_y + 16)], fill=(15, 25, 40), width=2)
    
    # Glowing packets on pipeline
    for px in [W*0.15, W*0.35, W*0.5, W*0.68, W*0.85]:
        draw.ellipse([(px - 30, pipe_y - 6), (px + 30, pipe_y + 6)], fill=(0, 228, 255))
        draw.ellipse([(px - 15, pipe_y - 3), (px + 15, pipe_y + 3)], fill=(255, 255, 255))

    # Sub-caption in PolySans
    poly_font = ImageFont.truetype(r'site\assets\fonts\PolySansTrial-Bulky.otf', 38)
    sub = "SCALABLE B2B PIPELINES  ·  REPEATABLE GROWTH  ·  REAL REVENUE"
    s_bbox = poly_font.getbbox(sub)
    s_w = s_bbox[2] - s_bbox[0]
    draw.text(((W - s_w) // 2, pipe_y + 55), sub, font=poly_font, fill=(160, 180, 205))

    base.save(target, 'JPEG', quality=94)
    print("Rendered Visual 2 to", target)


# -------------------------------------------------------------------
# Visual 3: B2B Ecosystem (3022 x 1249)
# -------------------------------------------------------------------
def render_visual3_ecosystem():
    W, H = 3022, 1249
    target = r'site\assets\mdn\photo-thumbnail-3-kstjpsjpg-t0wMA.jpe'
    backup = r'backup_original_images\photo-thumbnail-3-kstjpsjpg-t0wMA.jpe'
    if os.path.exists(target) and not os.path.exists(backup):
        shutil.copy2(target, backup)

    base = Image.new('RGB', (W, H), '#07090E')
    draw = ImageDraw.Draw(base)

    # Isometric grid lines
    cx, cy = W // 2, H // 2
    for i in range(-25, 26):
        x1 = cx + i * 120 - 1800
        y1 = cy - i * 60 + 900
        x2 = cx + i * 120 + 1800
        y2 = cy - i * 60 - 900
        draw.line([(x1, y1), (x2, y2)], fill=(18, 28, 42), width=1)
        
        x3 = cx + i * 120 - 1800
        y3 = cy + i * 60 - 900
        x4 = cx + i * 120 + 1800
        y4 = cy + i * 60 + 900
        draw.line([(x3, y3), (x4, y4)], fill=(18, 28, 42), width=1)

    # Modular enterprise blocks floating in grid
    blocks = [
        (-4, -1, "STARTUPS", (169, 220, 30)),
        (-1, -2, "SAAS PLATFORMS", (0, 228, 255)),
        (2, -1, "ENTERPRISE", (99, 102, 241)),
        (0, 1, "UPLINQ CORE", (255, 255, 255)),
        (-3, 2, "OUTREACH CRM", (169, 220, 30)),
        (3, 1, "REVENUE ENGINE", (0, 228, 255)),
        (1, 3, "MARKET DEMAND", (99, 102, 241))
    ]

    font = ImageFont.truetype(r'site\assets\fonts\PolySansTrial-Bulky.otf', 26)

    for gx, gy, label, col in blocks:
        # Isometric project
        bx = cx + (gx - gy) * 180
        by = cy + (gx + gy) * 90

        # Draw 3D block
        bw, bh, bdepth = 140, 70, 50
        # Top face
        top_pts = [
            (bx, by - bdepth - bh//2),
            (bx + bw//2, by - bdepth),
            (bx, by - bdepth + bh//2),
            (bx - bw//2, by - bdepth)
        ]
        draw.polygon(top_pts, fill=(col[0]//4, col[1]//4, col[2]//4), outline=col, width=2)
        # Left face
        left_pts = [
            (bx - bw//2, by - bdepth),
            (bx, by - bdepth + bh//2),
            (bx, by + bh//2),
            (bx - bw//2, by)
        ]
        draw.polygon(left_pts, fill=(15, 22, 32), outline=col, width=2)
        # Right face
        right_pts = [
            (bx, by - bdepth + bh//2),
            (bx + bw//2, by - bdepth),
            (bx + bw//2, by),
            (bx, by + bh//2)
        ]
        draw.polygon(right_pts, fill=(22, 32, 48), outline=col, width=2)

        # Label above block
        l_bbox = font.getbbox(label)
        l_w = l_bbox[2] - l_bbox[0]
        draw.text((bx - l_w//2, by - bdepth - bh//2 - 38), label, font=font, fill=(220, 235, 245))

        # Connecting luminous channel to center
        draw.line([(bx, by), (cx, cy + 90)], fill=(col[0]//2, col[1]//2, col[2]//2), width=2)
        draw.ellipse([(bx - 6, by - 6), (bx + 6, by + 6)], fill=col)

    base.save(target, 'JPEG', quality=94)
    print("Rendered Visual 3 to", target)


# -------------------------------------------------------------------
# Visual 4: Product-to-Market Connection (3022 x 1248)
# -------------------------------------------------------------------
def render_visual4_connection():
    W, H = 3022, 1248
    target = r'site\assets\mdn\photo-thumbnail-4-lfg5ygjpg-t0wMA.jpe'
    backup = r'backup_original_images\photo-thumbnail-4-lfg5ygjpg-t0wMA.jpe'
    if os.path.exists(target) and not os.path.exists(backup):
        shutil.copy2(target, backup)

    base = Image.new('RGB', (W, H), '#06080D')
    draw = ImageDraw.Draw(base)

    # Soft dark gradient and radial glow at center
    cx, cy = W // 2, H // 2
    for r in range(600, 0, -20):
        alpha = int((1 - r / 600) * 40)
        draw.ellipse([(cx - r, cy - r//2), (cx + r, cy + r//2)], fill=(0, alpha, int(alpha * 1.5)))

    # Two interlocking precision blocks
    # Left Block: "PRODUCT" (Navy Titanium)
    pw, ph = 420, 320
    px = cx - 220
    py = cy
    draw.polygon([(px - pw, py - ph//2), (px, py - ph//2), (px, py + ph//2), (px - pw, py + ph//2)],
                 fill=(18, 28, 45), outline=(99, 102, 241), width=3)
    
    # Right Block: "MARKET" (Cyan / Lime Energy)
    mx = cx + 220
    my = cy
    draw.polygon([(mx, my - ph//2), (mx + pw, my - ph//2), (mx + pw, my + ph//2), (mx, my + ph//2)],
                 fill=(10, 35, 45), outline=(0, 228, 255), width=3)

    # Magnetic snap seam at center
    draw.line([(cx, cy - ph//2 - 50), (cx, cy + ph//2 + 50)], fill=(0, 228, 255), width=4)
    for r in range(80, 0, -10):
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(169, 220, 30, int(150 * (1 - r/80))))

    # Labels
    font = ImageFont.truetype(r'site\assets\fonts\MangoGrotesque-Bold.ttf', 120)
    draw.text((px - pw + 50, py - 60), "STRONG PRODUCT", font=font, fill=(180, 200, 225))
    draw.text((mx + 50, py - 60), "RIGHT MARKET", font=font, fill=(0, 228, 255))

    sub_font = ImageFont.truetype(r'site\assets\fonts\PolySansTrial-Bulky.otf', 32)
    sub = "THE MOMENT OF PERFECT PRODUCT-MARKET FIT"
    sb = sub_font.getbbox(sub)
    draw.text(((W - (sb[2]-sb[0]))//2, cy + ph//2 + 90), sub, font=sub_font, fill=(160, 185, 210))

    base.save(target, 'JPEG', quality=94)
    print("Rendered Visual 4 to", target)


# -------------------------------------------------------------------
# Hero Mobile Poster (3024 x 1594)
# -------------------------------------------------------------------
def render_hero_mobile_poster():
    W, H = 3024, 1594
    target = r'site\assets\mdn\photo-video-thumbnail-gfb5anjpg-t0wMA.jpe'
    backup = r'backup_original_images\photo-video-thumbnail-gfb5anjpg-t0wMA.jpe'
    if os.path.exists(target) and not os.path.exists(backup):
        shutil.copy2(target, backup)

    # Use Card 1 / Card 5 high-res generated asset as base composite
    card1_path = r'site\assets\cdn\6a0ec808a39e8bbc34a44724_nlng-thumbnail_compressed.webp'
    if os.path.exists(card1_path):
        with Image.open(card1_path) as im:
            # Resize / crop to 3024 x 1594
            cw, ch = im.size
            ratio = W / H
            new_h = int(cw / ratio)
            top = max(0, (ch - new_h) // 2)
            cropped = im.crop((0, top, cw, top + new_h))
            base = cropped.resize((W, H), Image.Resampling.LANCZOS)
    else:
        base = Image.new('RGB', (W, H), '#080B10')

    # Apply dark cinematic overlay
    overlay = Image.new('RGBA', (W, H), (8, 12, 18, 120))
    base = Image.alpha_composite(base.convert('RGBA'), overlay).convert('RGB')
    
    base.save(target, 'JPEG', quality=92)
    print("Rendered Hero Mobile Poster to", target)

if __name__ == '__main__':
    render_visual2_real_revenue()
    render_visual3_ecosystem()
    render_visual4_connection()
    render_hero_mobile_poster()
