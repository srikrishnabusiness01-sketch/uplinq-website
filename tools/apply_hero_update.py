import re

def update_index_html():
    with open('site/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Headline line 1: Re -> FROM
    old_h1_line1 = '<div class="relative-block header-re" data-v-d28b769a><h1 class="heading-h1" data-v-d28b769a>Re</h1></div>'
    new_h1_line1 = '<div class="relative-block header-re" data-v-d28b769a><h1 class="heading-h1" data-v-d28b769a>FROM</h1></div>'
    assert old_h1_line1 in html, "old_h1_line1 not found"
    html = html.replace(old_h1_line1, new_h1_line1)

    # 2. Headline line 2: think -> PRODUCT
    old_h1_line2 = '<div class="relative-block header-think" data-v-d28b769a><h1 class="heading-h1" data-v-d28b769a>think</h1><div class="header-tag cc-digital" data-v-d28b769a>Strategy</div></div>'
    new_h1_line2 = '<div class="relative-block header-think" data-v-d28b769a><h1 class="heading-h1" data-v-d28b769a>PRODUCT</h1><div class="header-tag cc-digital" data-v-d28b769a>Strategy</div></div>'
    assert old_h1_line2 in html, "old_h1_line2 not found"
    html = html.replace(old_h1_line2, new_h1_line2)

    # 3. Headline line 3 & Sticker 2: Everything / Technology -> TO REVENUE / GROWTH
    old_h1_line3 = '<div class="relative-block header-subtext" data-v-d28b769a><h1 class="heading-h1" data-v-d28b769a>Everything</h1><div class="header-tag cc-strategy cc-yellow" data-v-d28b769a>Technology</div></div>'
    new_h1_line3 = '<div class="relative-block header-subtext" data-v-d28b769a><h1 class="heading-h1" data-v-d28b769a>TO REVENUE</h1><div class="header-tag cc-strategy cc-yellow" data-v-d28b769a>GROWTH</div></div>'
    assert old_h1_line3 in html, "old_h1_line3 not found"
    html = html.replace(old_h1_line3, new_h1_line3)

    # 4. Body text
    old_body = '<div class="header-text_wrapper" data-v-d28b769a><p data-v-d28b769a> We use technology to create undeniably brilliant work for companies with taste. </p></div>'
    new_body = '<div class="header-text_wrapper" data-v-d28b769a><p data-v-d28b769a> We help businesses turn strong products into well-positioned, market-ready, and growth-driven companies. </p></div>'
    assert old_body in html, "old_body not found"
    html = html.replace(old_body, new_body)

    # 5. Button text: Let&#39;s Build -> Let&#39;s Grow
    old_btn = '<div class="button-mask" data-v-50808a10><div class="button-text cc-top" data-button data-v-50808a10><!--[--> Let&#39;s Build <!--]--></div><div class="button-text cc-bottom" data-button data-v-50808a10><!--[--> Let&#39;s Build <!--]--></div></div>'
    new_btn = '<div class="button-mask" data-v-50808a10><div class="button-text cc-top" data-button data-v-50808a10><!--[--> Let&#39;s Grow <!--]--></div><div class="button-text cc-bottom" data-button data-v-50808a10><!--[--> Let&#39;s Grow <!--]--></div></div>'
    assert old_btn in html, "old_btn not found"
    html = html.replace(old_btn, new_btn)

    with open('site/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated site/index.html")

def update_js_bundle():
    with open('site/_nuxt/BMQH0uFj.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # 1. Line 1: "Re"
    old_js_line1 = 'i("div",{class:"relative-block header-re"},[i("h1",{class:"heading-h1"},"Re")],-1)'
    new_js_line1 = 'i("div",{class:"relative-block header-re"},[i("h1",{class:"heading-h1"},"FROM")],-1)'
    assert old_js_line1 in js, "old_js_line1 not found"
    js = js.replace(old_js_line1, new_js_line1)

    # 2. Line 2: "think"
    old_js_line2 = 'i("div",{class:"relative-block header-think"},[i("h1",{class:"heading-h1"},"think"),i("div",{class:"header-tag cc-digital"},"Strategy")],-1)'
    new_js_line2 = 'i("div",{class:"relative-block header-think"},[i("h1",{class:"heading-h1"},"PRODUCT"),i("div",{class:"header-tag cc-digital"},"Strategy")],-1)'
    assert old_js_line2 in js, "old_js_line2 not found"
    js = js.replace(old_js_line2, new_js_line2)

    # 3. Line 3 & Sticker 2: "Everything", "Technology" -> "TO REVENUE", "GROWTH"
    old_js_line3 = 'i("div",{class:"relative-block header-subtext"},[i("h1",{class:"heading-h1"},"Everything"),i("div",{class:"header-tag cc-strategy cc-yellow"},"Technology")],-1)'
    new_js_line3 = 'i("div",{class:"relative-block header-subtext"},[i("h1",{class:"heading-h1"},"TO REVENUE"),i("div",{class:"header-tag cc-strategy cc-yellow"},"GROWTH")],-1)'
    assert old_js_line3 in js, "old_js_line3 not found"
    js = js.replace(old_js_line3, new_js_line3)

    # 4. Body text
    old_js_body = 'i("p",null," We use technology to create undeniably brilliant work for companies with taste. ")'
    new_js_body = 'i("p",null," We help businesses turn strong products into well-positioned, market-ready, and growth-driven companies. ")'
    assert old_js_body in js, "old_js_body not found"
    js = js.replace(old_js_body, new_js_body)

    # 5. Button text
    old_js_btn = "M(\" Let's Build \")"
    new_js_btn = "M(\" Let's Grow \")"
    assert old_js_btn in js, "old_js_btn not found"
    js = js.replace(old_js_btn, new_js_btn)

    with open('site/_nuxt/BMQH0uFj.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Successfully updated site/_nuxt/BMQH0uFj.js")

if __name__ == '__main__':
    update_index_html()
    update_js_bundle()
