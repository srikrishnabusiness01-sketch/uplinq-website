with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'heading-h1' in line or 'header-re' in line or 'header-think' in line or 'header-subtext' in line or 'header-inner' in line:
        start = max(0, idx - 5)
        end = min(len(lines), idx + 10)
        print(f"--- Line {idx} ---")
        for i in range(start, end):
            print(f"{i}: {lines[i].strip()}")
