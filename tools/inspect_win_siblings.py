import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from bs4 import BeautifulSoup

with open('site/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

wt = soup.find('div', class_='win-text_wrapper')
if wt:
    section = wt.parent
    print("Section container:", section.name, section.get('class'))
    for im in section.find_all('img'):
        print(f"SRC: {im.get('src')} | classes: {im.get('class')} | parent: {im.parent.name}.{im.parent.get('class')}")
