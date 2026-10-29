import glob
from bs4 import BeautifulSoup

html_files = glob.glob('site/**/*.html', recursive=True)

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    socials = soup.find_all(class_='social-link')
    links = [(s.get('href'), s.get_text(strip=True)) for s in socials]
    print(f"{hf}: {len(links)} social links:")
    for l in links:
        print(f"  {l[1]}: {l[0]}")
    break # Just show first
