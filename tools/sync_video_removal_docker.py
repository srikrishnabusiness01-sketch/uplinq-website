import subprocess

files_to_sync = [
    ('site/_nuxt/BMQH0uFj.js', '/usr/share/nginx/html/_nuxt/BMQH0uFj.js'),
    ('site/_nuxt/entry.DzM0mqX9.css', '/usr/share/nginx/html/_nuxt/entry.DzM0mqX9.css'),
    ('site/assets/mdn/video-check-launch-lmhh5hmp4-t0wMA.mp4', '/usr/share/nginx/html/assets/mdn/video-check-launch-lmhh5hmp4-t0wMA.mp4')
]

for src, dst in files_to_sync:
    cmd = ['docker', 'cp', src, f'wearecheck_website:{dst}']
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Copied {src} -> {dst}")
    else:
        print(f"Failed {src}: {res.stderr}")

print("Docker sync completed.")
