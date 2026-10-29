import json
import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Check menu-button
menu_matches = re.findall(r'<button[^>]*class="[^"]*menu-button[^"]*"[^>]*>.*?</button>', text)
print(f"menu-button in index.html: {len(menu_matches)}")

# 2. Check Our Work
our_work_matches = re.findall(r'Our\s+Work', text)
print(f"Our Work in index.html: {len(our_work_matches)}")

# 3. Check project tags
tag_matches = re.findall(r'<div class="project-tag"[^>]*>.*?</div>', text)
print(f"project-tag elements in index.html: {len(tag_matches)}")

# 4. Check project-tag_wrapper contents
wrappers = re.findall(r'<div class="project-tag_wrapper"[^>]*>.*?</div>', text)
print(f"project-tag_wrapper count: {len(wrappers)}")
for i, w in enumerate(wrappers):
    print(f"Wrapper {i}: {w}")
