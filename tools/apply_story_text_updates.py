import re

# 1. Update site/index.html
with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacement 1:
# Find target 1 in html
pattern1 = re.compile(r'<div class="stats-text_wrapper" data-horizontal-paragraph data-v-d28b769a>\s*Uplinq began with one clear observation.*?We exist to close that gap\.\s*</div>', re.DOTALL)
match1 = pattern1.search(html)
assert match1, "Match 1 not found in site/index.html"

new_block1_html = '<div class="stats-text_wrapper" data-horizontal-paragraph data-v-d28b769a> We exist to close the gap between a strong product and the right market. </div>'
html = html[:match1.start()] + new_block1_html + html[match1.end():]
print("Updated Target 1 in site/index.html.")

# Replacement 2:
pattern2 = re.compile(r'<div class="stats-text_wrapper" data-horizontal-paragraph data-v-d28b769a>\s*Not a marketing agency\.\s*A strategic growth partner\.\s*</div>', re.DOTALL)
match2 = pattern2.search(html)
assert match2, "Match 2 not found in site/index.html"

new_block2_html = '<div class="stats-text_wrapper" data-horizontal-paragraph data-v-d28b769a> One Goal. Real Revenue. </div>'
html = html[:match2.start()] + new_block2_html + html[match2.end():]
print("Updated Target 2 in site/index.html.")

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update site/_nuxt/BMQH0uFj.js
with open('site/_nuxt/BMQH0uFj.js', 'r', encoding='utf-8') as f:
    js = f.read()

pattern1_js = re.compile(r'class:"stats-text_wrapper","data-horizontal-paragraph":""},\s*" Uplinq began with one clear observation.*?We exist to close that gap\. "\)', re.DOTALL)
match1_js = pattern1_js.search(js)
assert match1_js, "Match 1 not found in site/_nuxt/BMQH0uFj.js"

new_block1_js = 'class:"stats-text_wrapper","data-horizontal-paragraph":""}," We exist to close the gap between a strong product and the right market. ")'
js = js[:match1_js.start()] + new_block1_js + js[match1_js.end():]
print("Updated Target 1 in site/_nuxt/BMQH0uFj.js.")

pattern2_js = re.compile(r'class:"stats-text_wrapper","data-horizontal-paragraph":""},\s*" Not a marketing agency\.\s*A strategic growth partner\. "\)', re.DOTALL)
match2_js = pattern2_js.search(js)
assert match2_js, "Match 2 not found in site/_nuxt/BMQH0uFj.js"

new_block2_js = 'class:"stats-text_wrapper","data-horizontal-paragraph":""}," One Goal. Real Revenue. ")'
js = js[:match2_js.start()] + new_block2_js + js[match2_js.end():]
print("Updated Target 2 in site/_nuxt/BMQH0uFj.js.")

with open('site/_nuxt/BMQH0uFj.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("All text replacements applied successfully!")
