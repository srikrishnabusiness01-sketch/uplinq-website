import glob
import re

html_files = glob.glob('site/**/*.html', recursive=True)

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    mailtos = re.findall(r'href=["\'](mailto:[^"\']+)["\']', content)
    if mailtos:
        print(hf, mailtos)
