import re

def search_in_file(filepath):
    print(f"=== Searching in {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    terms = [
        'Bonjour',
        'Got a Project',
        'What would you like to do',
        'Branding',
        'Website Design',
        'Mobile App Development',
        'Web App Development',
        'branding',
        'website-design',
        'mobile-app',
        'web-app',
        'NEXT'
    ]
    for term in terms:
        matches = [m.start() for m in re.finditer(re.escape(term), content, re.I)]
        print(f"  Term: '{term}' -> {len(matches)} occurrences")
        for idx in matches:
            snippet = content[max(0, idx-50):min(len(content), idx+80)].replace('\n', ' ')
            print(f"    [{idx}]: {snippet}")

search_in_file('site/_nuxt/B0CwXBEy.js')
search_in_file('site/_nuxt/DSgCRULr.js')
