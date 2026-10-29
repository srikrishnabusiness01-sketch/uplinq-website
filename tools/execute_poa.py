import os
import re

def update_css():
    css_path = 'site/_nuxt/entry.DzM0mqX9.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Update service-block_title and service-tag
    old_service_title = """  .service-block_title {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    gap: 10px !important;
    margin: 0 0 12px 0 !important;
    position: relative !important;
  }

  .service-block_title .heading-h2 {
    font-size: clamp(28px, 8vw, 36px) !important;
    line-height: 1 !important;
    margin: 0 !important;
  }

  .service-tag {
    font-size: 13px !important;
    padding: 3px 8px !important;
    border-radius: 4px !important;
  }"""

    new_service_title = """  .service-block_title {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    gap: 8px 12px !important;
    margin: 0 0 16px 0 !important;
    position: relative !important;
  }

  .service-block_title .heading-h2 {
    display: inline-block !important;
    font-size: clamp(28px, 8vw, 36px) !important;
    line-height: 1 !important;
    margin: 0 !important;
  }

  .service-tag {
    position: relative !important;
    inset: auto !important;
    top: auto !important;
    right: auto !important;
    bottom: auto !important;
    left: auto !important;
    display: inline-flex !important;
    align-items: center !important;
    margin: 0 !important;
    font-size: 13px !important;
    line-height: 16px !important;
    padding: 4px 10px !important;
    border-radius: 4px !important;
    transform: rotate(-5deg) !important;
    z-index: 2 !important;
  }"""

    assert old_service_title in css, "old_service_title not found in css"
    css = css.replace(old_service_title, new_service_title)
    print("1. Updated service-block_title and service-tag in CSS.")

    # 2. Update win-img_container for Choice A (Show custom images cleanly below typography)
    old_win_hide = """  /* Hide colliding top container */
  .win-img_container.cc-top {
    display: none !important;
  }

  /* Hide all win images and containers on mobile (Impact words text only) */
  .win-img_container,
  .win-img_container.cc-top,
  .win-img_container.cc-bottom,
  .win-img_wrapper,
  .win-img_wrapper.cc-top,
  .win-img_wrapper.cc-bottom,
  .win-img_block,
  .win-img_block.cc-top,
  .win-img_block.cc-bottom {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    height: 0 !important;
    max-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
  }"""

    new_win_show = """  /* Hide colliding top container on mobile */
  .win-img_container.cc-top {
    display: none !important;
  }

  /* Choice A: Show custom win images cleanly below the typography on mobile */
  .win-img_container.cc-bottom {
    position: relative !important;
    display: block !important;
    width: 100% !important;
    max-width: 340px !important;
    height: auto !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    margin: 28px auto 0 !important;
    padding: 0 !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    overflow: visible !important;
  }

  .win-img_wrapper.cc-bottom {
    position: relative !important;
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 10px !important;
    width: 100% !important;
    height: auto !important;
    inset: auto !important;
    visibility: visible !important;
    opacity: 1 !important;
  }

  .win-img_block.cc-bottom,
  .win-img_block.cc-bottom.cc-one,
  .win-img_block.cc-bottom.cc-two,
  .win-img_block.cc-bottom.cc-three {
    position: relative !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    transform: none !important;
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 4 / 3 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
  }

  .win-img_block.cc-bottom img {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
  }"""

    assert old_win_hide in css, "old_win_hide not found in css"
    css = css.replace(old_win_hide, new_win_show)
    print("2. Updated win-img_container to Choice A in CSS.")

    # 3. Update Company Story Section in CSS
    old_story_css = """  /* --- 7. COMPANY STORY SECTION (Fixes illustration cutoffs & text alignment) --- */
  /* Left paragraph and right stat block stack vertically */
  /* Globe/map illustration scales down */
  .services-inner.cc-stats,
  .stats-block_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
    gap: 28px !important;
  }

  .stats-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 0 20px 0 !important;
    padding: 0 !important;
  }

  .stats-block_flex,
  .stats-block_flex.cc-align-top,
  .stats-block_flex.cc-align-bottom {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    min-height: auto !important;
    padding: 0 !important;
    margin: 0 0 16px 0 !important;
    gap: 10px !important;
  }

  .stats-text_wrapper {
    font-size: clamp(20px, 5.5vw, 24px) !important;
    line-height: 1.3 !important;
    text-align: center !important;
    width: 100% !important;
    margin: 0 auto 10px !important;
  }

  .stats-figure {
    font-family: var(--title) !important;
    font-size: clamp(48px, 14vw, 68px) !important;
    line-height: 1 !important;
    text-align: center !important;
    margin: 0 auto !important;
    justify-content: center !important;
  }

  .stats-details_text,
  .stats-details_text.cc-last {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    font-size: 18px !important;
    line-height: 1.2 !important;
    margin: 4px auto !important;
    width: 100% !important;
  }

  .stats-sketch_block,
  .stats-sketch_block.cc-globe,
  .stats-sketch_block.cc-town {
    display: block !important;
    position: relative !important;
    width: 100% !important;
    max-width: 300px !important;
    height: auto !important;
    max-height: none !important;
    aspect-ratio: 16 / 10 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    margin: 16px auto !important;
    padding: 0 !important;
    inset: auto !important;
  }

  .stats-sketch_block img,
  .stats-sketch_block video {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    display: block !important;
  }

  .stats-details_block.cc-country {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    margin: 10px 0 !important;
  }"""

    new_story_css = """  /* --- 7. COMPANY STORY SECTION (Natural vertical flow on mobile) --- */
  .services-container,
  .services-inner.cc-stats,
  .stats-block_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    height: auto !important;
    min-height: auto !important;
    overflow: visible !important;
    padding: 0 !important;
    margin: 0 !important;
    gap: 40px !important;
    transform: none !important;
  }

  .services-inner.cc-stats {
    padding: 48px 16px 64px !important;
    background-color: var(--white) !important;
  }

  .stats-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    min-height: auto !important;
    margin: 0 0 24px 0 !important;
    padding: 0 !important;
  }

  .stats-block_flex,
  .stats-block_flex.cc-align-top,
  .stats-block_flex.cc-align-bottom {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    min-height: auto !important;
    padding: 0 !important;
    margin: 0 0 16px 0 !important;
    gap: 12px !important;
  }

  .stats-text_wrapper {
    font-size: clamp(18px, 5vw, 22px) !important;
    line-height: 1.4 !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 340px !important;
    margin: 0 auto 10px !important;
  }

  .stats-subtext_wrapper,
  .stats-subtext_wrapper.cc-country,
  .stats-subtext_wrapper.cc-impact,
  .stats-subtext_wrapper.cc-amount {
    font-size: 15px !important;
    line-height: 1.4 !important;
    text-align: center !important;
    margin: 0 auto 8px !important;
    max-width: 320px !important;
  }

  .stats-figure {
    font-family: var(--title) !important;
    font-size: clamp(48px, 14vw, 68px) !important;
    line-height: 1 !important;
    text-align: center !important;
    margin: 0 auto !important;
    justify-content: center !important;
  }

  .stats-details_text,
  .stats-details_text.cc-last {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    font-size: 18px !important;
    line-height: 1.2 !important;
    margin: 4px auto !important;
    width: 100% !important;
  }

  .stats-sketch_block,
  .stats-sketch_block.cc-globe,
  .stats-sketch_block.cc-town {
    display: block !important;
    position: relative !important;
    width: 100% !important;
    max-width: 290px !important;
    height: auto !important;
    max-height: none !important;
    aspect-ratio: 16 / 10 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    margin: 16px auto !important;
    padding: 0 !important;
    inset: auto !important;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08) !important;
    visibility: visible !important;
    opacity: 1 !important;
  }

  .stats-sketch_block > img,
  .stats-sketch_block img {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }

  .stats-sketch_block video {
    display: none !important;
  }

  .stats-sketch {
    display: none !important;
  }

  .stats-details_block.cc-country {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 14px !important;
    margin: 10px auto !important;
  }"""

    assert old_story_css in css, "old_story_css not found in css"
    css = css.replace(old_story_css, new_story_css)
    print("3. Updated Company Story Section in CSS.")

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Saved site/_nuxt/entry.DzM0mqX9.css successfully.")

def update_story_text():
    old_p = " We exist to close the gap between a strong product and the right market. "
    new_p = " Uplinq began with one clear observation \u2014 many companies have strong products or services, but struggle to find the right market, position themselves effectively, and reach the customers who truly need them. We exist to close that gap. "

    # Update index.html
    html_path = 'site/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    if old_p in html:
        html = html.replace(old_p, new_p, 1) # replace first occurrence (story section)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated opening story text in site/index.html.")
    else:
        print("Warning: old_p not found in site/index.html")

    # Update BMQH0uFj.js
    js_path = 'site/_nuxt/BMQH0uFj.js'
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    if old_p in js:
        js = js.replace(old_p, new_p, 1)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js)
        print("Updated opening story text in site/_nuxt/BMQH0uFj.js.")
    else:
        print("Warning: old_p not found in site/_nuxt/BMQH0uFj.js")

if __name__ == '__main__':
    update_css()
    update_story_text()
