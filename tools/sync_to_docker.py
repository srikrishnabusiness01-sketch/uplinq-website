import subprocess
import glob
import os

files_to_copy = [
    ('site/_nuxt/entry.DzM0mqX9.css', '/usr/share/nginx/html/_nuxt/entry.DzM0mqX9.css'),
    ('site/_nuxt/BMQH0uFj.js', '/usr/share/nginx/html/_nuxt/BMQH0uFj.js'),
    ('site/_nuxt/CKrmhtJt.js', '/usr/share/nginx/html/_nuxt/CKrmhtJt.js'),
    ('site/_nuxt/win-1.4kaXhrsf.jpg', '/usr/share/nginx/html/_nuxt/win-1.4kaXhrsf.jpg'),
    ('site/index.html', '/usr/share/nginx/html/index.html'),
    ('site/about/index.html', '/usr/share/nginx/html/about/index.html'),
    ('site/careers/index.html', '/usr/share/nginx/html/careers/index.html'),
    ('site/case/nlng/index.html', '/usr/share/nginx/html/case/nlng/index.html'),
    ('site/services/index.html', '/usr/share/nginx/html/services/index.html'),
    ('site/work/index.html', '/usr/share/nginx/html/work/index.html'),
    ('site/work/autograph/index.html', '/usr/share/nginx/html/work/autograph/index.html'),
    ('site/work/kele/index.html', '/usr/share/nginx/html/work/kele/index.html'),
    ('site/work/propel/index.html', '/usr/share/nginx/html/work/propel/index.html'),
    ('site/work/quidax/index.html', '/usr/share/nginx/html/work/quidax/index.html'),
]

# Add all win mdn images
for f in glob.glob('site/assets/mdn/*photo*'):
    f_dst = f.replace('\\', '/').replace('site/', '/usr/share/nginx/html/')
    files_to_copy.append((f, f_dst))

for src, dst in files_to_copy:
    cmd = ['docker', 'cp', src, f'wearecheck_website:{dst}']
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Copied {src} -> {dst}")
    else:
        print(f"Failed {src}: {res.stderr}")

# Reload nginx
res = subprocess.run(['docker', 'exec', 'wearecheck_website', 'nginx', '-s', 'reload'], capture_output=True, text=True)
print("Nginx reload:", res.stdout, res.stderr)
print("Docker sync completed.")
