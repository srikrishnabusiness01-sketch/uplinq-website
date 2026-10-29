import os
import shutil

# Step A: Restore original win images
restores = [
    ('backup_original_images/win-1.4kaXhrsf.jpg', 'site/_nuxt/win-1.4kaXhrsf.jpg'),
    ('backup_original_images/photo-growth-img-1-xrt0cbjpg-t0wMA.jpe', 'site/assets/mdn/photo-growth-img-1-xrt0cbjpg-t0wMA.jpe'),
    ('backup_original_images/photo-speed-img-jtiybwjpg-t0wMA.jpe', 'site/assets/mdn/photo-speed-img-jtiybwjpg-t0wMA.jpe'),
    ('backup_original_images/photo-propel-img-bd9nyqjpg-t0wMA.jpe', 'site/assets/mdn/photo-propel-img-bd9nyqjpg-t0wMA.jpe'),
    ('backup_original_images/photo-growth-img-2-wnhqpqjpg-t0wMA.jpe', 'site/assets/mdn/photo-growth-img-2-wnhqpqjpg-t0wMA.jpe'),
    ('backup_original_images/photo-adidas-b7szujjpg-t0wMA.jpe', 'site/assets/mdn/photo-adidas-b7szujjpg-t0wMA.jpe'),
]

for src, dst in restores:
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Restored {src} -> {dst}")
    else:
        print(f"Warning: backup {src} not found!")

# Step B: Update site/_nuxt/entry.DzM0mqX9.css
with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Hide menu-button globally (both desktop and mobile)
old_menu_rule = """/* Desktop-only overrides: Keep menu-button hidden on desktop & Fix hero video slices */
@media screen and (min-width: 768px) {
  .menu-button,
  .c-nav .menu-button,
  .nav-wrapper .menu-button {
    display: none !important;
    visibility: hidden !important;
    pointer-events: none !important;
  }"""

new_menu_rule = """/* Global Menu Button Removal (Hidden on both Desktop and Mobile per user instruction) */
.menu-button,
.c-nav .menu-button,
.nav-wrapper .menu-button {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
  opacity: 0 !important;
}

/* Desktop-only overrides: Fix hero video slices */
@media screen and (min-width: 768px) {"""

if old_menu_rule in css:
    css = css.replace(old_menu_rule, new_menu_rule)
    print("Updated menu-button to be hidden globally.")
else:
    print("Warning: old_menu_rule pattern not found, prepending global menu hide.")
    css = ".menu-button, .c-nav .menu-button, .nav-wrapper .menu-button { display: none !important; visibility: hidden !important; opacity: 0 !important; pointer-events: none !important; }\n" + css

# 2. In mobile rules, ensure .menu-button is hidden in .c-nav and .nav-inner
css = css.replace('.menu-button,\n  .c-nav .menu-button,\n  .nav-wrapper .menu-button {\n    display: flex !important;',
                  '.menu-button,\n  .c-nav .menu-button,\n  .nav-wrapper .menu-button {\n    display: none !important;\n    visibility: hidden !important;\n    opacity: 0 !important;')

# 3. Completely hide .win-img_container and all win images on mobile
old_win_imgs = """  /* Clean 2x2 grid container below the text */
  .win-img_container.cc-bottom {
    position: relative !important;
    width: 100% !important;
    max-width: 320px !important;
    height: auto !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    margin: 24px auto 0 !important;
    display: block !important;
    align-self: center !important;
  }

  .win-img_wrapper.cc-bottom {
    position: relative !important;
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
    width: 100% !important;
    height: auto !important;
    inset: auto !important;
  }

  .win-img_block,
  .win-img_block.cc-bottom,
  .win-img_block.cc-one,
  .win-img_block.cc-two,
  .win-img_block.cc-three {
    position: relative !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    transform: none !important;
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 4 / 3 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
  }

  .win-img_block img {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
  }"""

new_win_imgs = """  /* Hide all win images and containers on mobile (Impact words text only) */
  .win-img_container,
  .win-img_container.cc-top,
  .win-img_container.cc-bottom,
  .win-img_wrapper,
  .win-img_wrapper.cc-top,
  .win-img_wrapper.cc-bottom,
  .win-img_block,
  .win-img_block.cc-top,
  .win-img_block.cc-bottom {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    height: 0 !important;
    max-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
  }"""

if old_win_imgs in css:
    css = css.replace(old_win_imgs, new_win_imgs)
    print("Replaced win images with complete hiding rule on mobile.")
else:
    print("Warning: old_win_imgs pattern not found exactly in css, appending hide rule.")
    css = css.replace("/* --- 7. COMPANY STORY SECTION", new_win_imgs + "\n\n  /* --- 7. COMPANY STORY SECTION")

# 4. In Company Story section: ensure thumbnail images are visible and not hidden by GSAP autoAlpha
old_story_imgs = """.stats-sketch_block > img,
  .stats-sketch_block img {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
  }"""

new_story_imgs = """.stats-sketch_block > img,
  .stats-sketch_block img {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
  }"""

if old_story_imgs in css:
    css = css.replace(old_story_imgs, new_story_imgs)
    print("Ensured stats-sketch_block images have opacity 1 and visibility visible.")

with open('site/_nuxt/entry.DzM0mqX9.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates applied successfully.")
