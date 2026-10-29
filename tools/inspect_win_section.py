import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from bs4 import BeautifulSoup
import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find element with "We help them win in"
for tag in soup.find_all(True):
    if tag.string and 'We help them win in' in tag.string:
        print("Found tag:", tag.name, tag.get('class'))
        # find win-wrapper or similar
        parent = tag
        while parent and parent.name != 'body':
            if any('win' in str(c) for c in parent.get('class', [])):
                print("Found win container:", parent.name, parent.get('class'))
                for im in parent.find_all('img'):
                    print("  IMG:", im.get('src'), "classes:", im.get('class'), "parent:", im.parent.name, im.parent.get('class'))
                break
            parent = parent.parent
        break
