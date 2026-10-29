import re

# 1. Update site/_nuxt/entry.DzM0mqX9.css
with open('site/_nuxt/entry.DzM0mqX9.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .heading-h1 block with comprehensive rule that includes opacity and transform
old_h1 = """.heading-h1 {
    font-size: clamp(34px, 11vw, 54px) !important;
    line-height: 0.95 !important;
    letter-spacing: -0.02em !important;
    text-align: center !important;
    width: 100% !important;
    word-break: normal !important;
    overflow-wrap: normal !important;
  }"""

new_h1 = """.heading-h1,
  .header-re > h1,
  .header-think > h1,
  .header-subtext > h1,
  h1.heading-h1,
  .relative-block > h1,
  .header-title_wrapper h1 {
    font-size: clamp(34px, 11vw, 54px) !important;
    line-height: 0.95 !important;
    letter-spacing: -0.02em !important;
    text-align: center !important;
    width: 100% !important;
    word-break: normal !important;
    overflow-wrap: normal !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
    display: block !important;
  }"""

if old_h1 in css:
    css = css.replace(old_h1, new_h1)
    print("Replaced .heading-h1 in entry.DzM0mqX9.css")
else:
    print("Could not find exact old_h1 in entry.DzM0mqX9.css")

# Also add crown-sketch removal and win top-wrapper removal to entry.DzM0mqX9.css
additions = """
  /* Crown sketch removal and win section fixes */
  .crown-sketch,
  .crown-sketch.cc-small,
  div[class*="crown-sketch"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }

  .win-img_wrapper.cc-top,
  .win-img_block.cc-top {
    display: none !important;
    visibility: hidden !important;
  }

  .win-container,
  .win-category_wrapper {
    height: auto !important;
    min-height: auto !important;
  }
"""

if "/* Crown sketch removal and win section fixes */" not in css:
    # Insert right before /* --- 7. COMPANY STORY SECTION
    target = "/* --- 7. COMPANY STORY SECTION"
    if target in css:
        css = css.replace(target, additions + "\n  " + target)
        print("Added crown-sketch and win fixes to entry.DzM0mqX9.css")

with open('site/_nuxt/entry.DzM0mqX9.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update site/_nuxt/index.CL5g6JNe.css
with open('site/_nuxt/index.CL5g6JNe.css', 'r', encoding='utf-8') as f:
    index_css = f.read()

# Make sure c-button.home has opacity: 1 and visibility: visible on mobile
index_css = index_css.replace('.c-button.home[data-v-d28b769a]{display:block;opacity:0;visibility:hidden}',
                              '.c-button.home[data-v-d28b769a]{display:block;opacity:1;visibility:visible}')

# Add mobile overrides to index.CL5g6JNe.css if not present
index_mobile_patch = "@media screen and (max-width:767px){.header-subtext>h1[data-v-d28b769a],.header-re>h1[data-v-d28b769a],.header-think>h1[data-v-d28b769a]{opacity:1!important;transform:none!important}.header-tag.cc-digital[data-v-d28b769a],.header-tag.cc-strategy[data-v-d28b769a],.header-tag.cc-branding[data-v-d28b769a]{opacity:1!important}.crown-sketch[data-v-d28b769a]{display:none!important}.win-img_wrapper.cc-top[data-v-d28b769a]{display:none!important}}"

if ".header-subtext>h1[data-v-d28b769a]{opacity:1" not in index_css:
    index_css += "\n" + index_mobile_patch
    print("Appended mobile patch to index.CL5g6JNe.css")

with open('site/_nuxt/index.CL5g6JNe.css', 'w', encoding='utf-8') as f:
    f.write(index_css)

print("Finished refining mobile CSS.")
