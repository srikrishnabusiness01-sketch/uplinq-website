import glob
from bs4 import BeautifulSoup

html_files = glob.glob('site/**/*.html', recursive=True)

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    socials = soup.find_all(class_='social-link')
    print(f"{hf}: {len(socials)} social links")
