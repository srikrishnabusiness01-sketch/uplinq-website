import glob
import re

def remove_social_redirections():
    # Targets to replace in HTML files:
    replacements = [
        ('href="mailto:hello@wearecheck.co"', 'href="#"'),
        ('href="mailto:info@wearecheck.co"', 'href="#"'),
        ('href="https://www.instagram.com/wearecheck_/"', 'href="#"'),
        ('href="https://twitter.com/wearecheck_"', 'href="#"'),
        ('href="https://www.linkedin.com/company/wearecheck/"', 'href="#"'),
        ('href="https://medium.com/@wearecheck"', 'href="#"'),
        ('href="https://open.spotify.com/user/31qsdlftcrlk745coxgyopd3ksly?si=879379c9297a466c"', 'href="#"')
    ]

    html_files = glob.glob('site/**/*.html', recursive=True)
    for hf in html_files:
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()

        updated = content
        count = 0
        for old_href, new_href in replacements:
            if old_href in updated:
                count += updated.count(old_href)
                updated = updated.replace(old_href, new_href)

        if count > 0:
            with open(hf, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Updated {hf}: replaced {count} social link redirections")

    # Update JS bundle: pK72Md3I.js
    pk_path = 'site/_nuxt/pK72Md3I.js'
    if glob.glob(pk_path):
        with open(pk_path, 'r', encoding='utf-8') as f:
            pk = f.read()

        pk_updated = pk
        pk_count = 0
        for old_href, new_href in replacements:
            if old_href in pk_updated:
                pk_count += pk_updated.count(old_href)
                pk_updated = pk_updated.replace(old_href, new_href)

        if pk_count > 0:
            with open(pk_path, 'w', encoding='utf-8') as f:
                f.write(pk_updated)
            print(f"Updated {pk_path}: replaced {pk_count} social link redirections")

    # Also check Dl_6lvg3.js
    dl_path = 'site/_nuxt/Dl_6lvg3.js'
    if glob.glob(dl_path):
        with open(dl_path, 'r', encoding='utf-8') as f:
            dl = f.read()
        
        # Replace share URLs with '#'
        dl_replacements = [
            ('https://twitter.com/intent/tweet?text=', '#'),
            ('https://www.linkedin.com/sharing/share-offsite/?mini=true', '#'),
            ('https://www.facebook.com/sharer/sharer.php?u=', '#')
        ]
        dl_updated = dl
        for old_s, new_s in dl_replacements:
            if old_s in dl_updated:
                dl_updated = re.sub(rf'href:[`\'"][^\'"`]*{re.escape(old_s)}[^\'"`]*[`\'"]', 'href:"#"', dl_updated)
        
        if dl_updated != dl:
            with open(dl_path, 'w', encoding='utf-8') as f:
                f.write(dl_updated)
            print(f"Updated {dl_path}: replaced blog share link redirections")

if __name__ == '__main__':
    remove_social_redirections()
