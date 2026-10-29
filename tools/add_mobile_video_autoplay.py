# 1. Update index.html
html_path = 'site/index.html'
html_txt = open(html_path, encoding='utf-8').read()

target1 = '<video class="header-video_mobile" loop muted playsinline'
rep1 = '<video class="header-video_mobile" autoplay loop muted playsinline'

if target1 in html_txt:
    html_txt = html_txt.replace(target1, rep1)
    open(html_path, 'w', encoding='utf-8').write(html_txt)
    print("SUCCESS: Added autoplay to header-video_mobile in site/index.html!")
else:
    print("target1 not found in index.html (may already have autoplay)")

# 2. Update BMQH0uFj.js
js_path = 'site/_nuxt/BMQH0uFj.js'
js_txt = open(js_path, encoding='utf-8').read()

target2 = 'class:"header-video_mobile",loop:"",muted:"",playsinline:""'
rep2 = 'class:"header-video_mobile",autoplay:"",loop:"",muted:"",playsinline:""'

if target2 in js_txt:
    js_txt = js_txt.replace(target2, rep2)
    open(js_path, 'w', encoding='utf-8').write(js_txt)
    print("SUCCESS: Added autoplay to header-video_mobile in site/_nuxt/BMQH0uFj.js!")
else:
    print("target2 not found in BMQH0uFj.js (may already have autoplay)")
