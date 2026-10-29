with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    css = f.read()

rule_to_add = """
/* Disable and remove 1-minute showreel video modal and play buttons */
.play-btn,
.play-btn.cc-mobile,
.video-cta,
.c-popup,
.popup-overlay,
.c-video {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
  opacity: 0 !important;
}
"""

if '.c-popup' not in css:
    css = rule_to_add + "\n" + css
    with open('site/_nuxt/entry.DzM0mqX9.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated site/_nuxt/entry.DzM0mqX9.css with video popup removal styles.")
else:
    print("Rules already present.")
