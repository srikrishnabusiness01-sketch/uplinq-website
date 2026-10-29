import glob
import re
from bs4 import BeautifulSoup

social_domains = [
    'twitter.com', 'x.com', 'instagram.com', 'linkedin.com',
    'dribbble.com', 'behance.net', 'youtube.com', 'facebook.com',
    'tiktok.com', 'github.com', 'medium.com'
]

print("=== SEARCHING HTML FILES ===")
html_files = glob.glob('site/**/*.html', recursive=True)
found_links = {}

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.find_all('a'):
        href = a.get('href', '')
        for d in social_domains:
            if d in href:
                text = a.get_text(strip=True)
                key = (href, text)
                if key not in found_links:
                    found_links[key] = []
                found_links[key].append(hf)

print(f"Found {len(found_links)} unique social media links in HTML files:")
for (href, text), pages in found_links.items():
    print(f"HREF: '{href}' | Text: '{text}' | Pages: {len(pages)}")

print("\n=== SEARCHING JS FILES ===")
js_files = glob.glob('site/**/*.js', recursive=True)
found_js = {}
for jf in js_files:
    with open(jf, 'r', encoding='utf-8') as f:
        content = f.read()
    for d in social_domains:
        matches = re.findall(rf'https?://[^\s"\'<>]*{d}[^\s"\'<>]*', content)
        for m in matches:
            if m not in found_js:
                found_js[m] = []
            found_js[m].append(jf)

print(f"Found {len(found_js)} unique social links in JS files:")
for m, files in found_js.items():
    print(f"LINK: '{m}' in {files}")

print("\n=== SEARCHING _payload.json ===")
if glob.glob('site/_payload.json'):
    with open('site/_payload.json', 'r', encoding='utf-8') as f:
        p_content = f.read()
    for d in social_domains:
        matches = re.findall(rf'https?://[^\s"\'<>]*{d}[^\s"\'<>]*', p_content)
        for m in matches:
            print(f"PAYLOAD: '{m}'")
