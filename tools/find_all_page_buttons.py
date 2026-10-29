import glob, re

for f in sorted(glob.glob('site/**/*.html', recursive=True)):
    txt = open(f, encoding='utf-8').read()
    print(f"=== {f} ===")
    for m in re.finditer(r'<button[^>]*class=["\'][^"\']*c-button[^>]*>.*?</button>', txt, re.DOTALL):
        btn = m.group(0)
        # extract text inside button
        texts = re.findall(r'<!--\[-->\s*(.*?)\s*<!--]-->', btn)
        print("  Button texts:", texts)
