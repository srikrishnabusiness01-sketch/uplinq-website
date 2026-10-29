import re
from bs4 import BeautifulSoup

with open('site/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='project-card')
print(f"cards count: {len(cards)}")

# Search for the cards by title text
for title in ['Understand', 'Research', 'Position', 'Reach', 'Grow']:
    elem = soup.find(lambda e: e.name in ['div', 'h2', 'h3'] and title in e.get_text())
    print(f"\n--- Found '{title}' ---")
    if elem:
        # find closest parent project container
        curr = elem
        for _ in range(6):
            if curr and 'project' in ' '.join(curr.get('class', [])):
                print(f"Parent project tag: {curr.name}.{curr.get('class')}")
                # find img inside
                imgs = curr.find_all('img')
                for im in imgs:
                    print("  IMG:", im.get('src'), "classes:", im.get('class'))
                break
            if curr:
                curr = curr.parent
