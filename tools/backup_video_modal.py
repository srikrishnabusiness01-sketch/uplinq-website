import os
import shutil

os.makedirs('backup_original_js', exist_ok=True)
os.makedirs('backup_original_images', exist_ok=True)

# 1. Backup BMQH0uFj.js
js_src = 'site/_nuxt/BMQH0uFj.js'
js_bak = 'backup_original_js/BMQH0uFj.js.bak'
if not os.path.exists(js_bak):
    shutil.copy2(js_src, js_bak)
    print(f"Backed up {js_src} to {js_bak}")

# 2. Backup video-check-launch-lmhh5hmp4-t0wMA.mp4
video_src = 'site/assets/mdn/video-check-launch-lmhh5hmp4-t0wMA.mp4'
video_bak = 'backup_original_images/video-check-launch-lmhh5hmp4-t0wMA.mp4'
if os.path.exists(video_src) and not os.path.exists(video_bak):
    shutil.copy2(video_src, video_bak)
    print(f"Backed up {video_src} to {video_bak}")

print("Backups complete.")
