import json
import glob

def apply_removals():
    # -------------------------------------------------------------
    # 1. Remove Menu button from all HTML files
    # -------------------------------------------------------------
    menu_btn_html = '<button class="menu-button"><div>Menu</div><div class="menu-icon"></div></button>'
    html_files = glob.glob('site/**/*.html', recursive=True)
    for hf in html_files:
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()
        if menu_btn_html in content:
            content = content.replace(menu_btn_html, '')
            with open(hf, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Removed menu-button from {hf}")

    # -------------------------------------------------------------
    # 2. Remove Menu button from site/_nuxt/CKrmhtJt.js
    # -------------------------------------------------------------
    with open('site/_nuxt/CKrmhtJt.js', 'r', encoding='utf-8') as f:
        ck = f.read()
    
    old_ck_menu = 'createBaseVNode("button",{class:"menu-button",onClick:d},_hoisted_8$2)'
    new_ck_menu = 'createCommentVNode("v-if",!0)'
    assert old_ck_menu in ck, "old_ck_menu not found in CKrmhtJt.js"
    ck = ck.replace(old_ck_menu, new_ck_menu)
    with open('site/_nuxt/CKrmhtJt.js', 'w', encoding='utf-8') as f:
        f.write(ck)
    print("Updated site/_nuxt/CKrmhtJt.js (menu button replaced with comment)")

    # -------------------------------------------------------------
    # 3. Remove "Our Work" CTA from site/_nuxt/BMQH0uFj.js
    # -------------------------------------------------------------
    with open('site/_nuxt/BMQH0uFj.js', 'r', encoding='utf-8') as f:
        bm = f.read()

    old_bm_cta = 'i("div",z1,[H1,S(x,{"data-tag":"",href:"/work"},{default:X(()=>[M(" Our Work ")]),_:1})])'
    new_bm_cta = 'i("div",z1,[H1])'
    assert old_bm_cta in bm, "old_bm_cta not found in BMQH0uFj.js"
    bm = bm.replace(old_bm_cta, new_bm_cta)
    with open('site/_nuxt/BMQH0uFj.js', 'w', encoding='utf-8') as f:
        f.write(bm)
    print("Updated site/_nuxt/BMQH0uFj.js ('Our Work' CTA removed)")

    # -------------------------------------------------------------
    # 4. Remove "Our Work" CTA and Card Tags from site/index.html
    # -------------------------------------------------------------
    with open('site/index.html', 'r', encoding='utf-8') as f:
        idx_html = f.read()

    # Remove "Our Work" button
    our_work_btn = '<a href="/work" class="c-button w-inline-block" data-tag data-v-d28b769a data-v-50808a10><div class="c-button_inner" data-v-50808a10><div class="button-mask" data-v-50808a10><div class="button-text cc-top" data-button data-v-50808a10><!--[--> Our Work <!--]--></div><div class="button-text cc-bottom" data-button data-v-50808a10><!--[--> Our Work <!--]--></div></div><div class="button-icon" data-v-50808a10></div></div></a>'
    assert our_work_btn in idx_html, "our_work_btn not found in index.html"
    idx_html = idx_html.replace(our_work_btn, '')

    # Remove tags from each of the 5 cards in index.html
    card_tags = [
        '<div class="project-tag_wrapper" data-v-4c6c1c4b><!--[--><div class="project-tag" data-v-4c6c1c4b><div data-v-4c6c1c4b>Discovery</div></div><!--]--></div>',
        '<div class="project-tag_wrapper" data-v-4c6c1c4b><!--[--><div class="project-tag" data-v-4c6c1c4b><div data-v-4c6c1c4b>Market Research</div></div><!--]--></div>',
        '<div class="project-tag_wrapper" data-v-4c6c1c4b><!--[--><div class="project-tag" data-v-4c6c1c4b><div data-v-4c6c1c4b>Positioning</div></div><!--]--></div>',
        '<div class="project-tag_wrapper" data-v-4c6c1c4b><!--[--><div class="project-tag" data-v-4c6c1c4b><div data-v-4c6c1c4b>Outreach</div></div><!--]--></div>',
        '<div class="project-tag_wrapper" data-v-4c6c1c4b><!--[--><div class="project-tag" data-v-4c6c1c4b><div data-v-4c6c1c4b>Growth</div></div><!--]--></div>'
    ]
    empty_tag_wrapper = '<div class="project-tag_wrapper" data-v-4c6c1c4b></div>'
    for ct in card_tags:
        assert ct in idx_html, f"Tag {ct} not found in index.html"
        idx_html = idx_html.replace(ct, empty_tag_wrapper)

    # Update __NUXT_DATA__ in index.html: clear tags for the 5 cards
    s_tag = '<script type="application/json" id="__NUXT_DATA__" data-ssr="true">'
    s_idx = idx_html.find(s_tag)
    e_idx = idx_html.find('</script>', s_idx)
    data = json.loads(idx_html[s_idx+len(s_tag):e_idx])

    # Tag indices:
    # Card 1 (NLNG/Understand): 731
    # Card 2 (Quidax/Research): 23
    # Card 3 (Kele/Position): 264
    # Card 4 (Autograph/Reach): 404
    # Card 5 (Propel/Grow): 471
    for t_idx in [731, 23, 264, 404, 471]:
        data[t_idx] = ""

    new_json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    idx_html = idx_html[:s_idx+len(s_tag)] + new_json_str + idx_html[e_idx:]

    with open('site/index.html', 'w', encoding='utf-8') as f:
        f.write(idx_html)
    print("Updated site/index.html (Our Work button removed, card tags removed, __NUXT_DATA__ tags emptied)")

    # -------------------------------------------------------------
    # 5. Update site/_payload.json: clear tags for the 5 cards
    # -------------------------------------------------------------
    with open('site/_payload.json', 'r', encoding='utf-8') as f:
        pdata = json.load(f)

    for t_idx in [731, 23, 264, 404, 471]:
        pdata[t_idx] = ""

    with open('site/_payload.json', 'w', encoding='utf-8') as f:
        json.dump(pdata, f, separators=(',', ':'), ensure_ascii=False)
    print("Updated site/_payload.json (tags emptied)")

    # -------------------------------------------------------------
    # 6. Update CSS to enforce hiding of menu-button and project-tag_wrapper
    # -------------------------------------------------------------
    css_rule = '\n.menu-button,.c-nav .menu-button,.nav-wrapper .menu-button,.project-tag_wrapper,.projects-cta_wrapper>.c-button{display:none!important;visibility:hidden!important;pointer-events:none!important;}\n'
    
    # Add to site/_nuxt/entry.DzM0mqX9.css
    with open('site/_nuxt/entry.DzM0mqX9.css', 'a', encoding='utf-8') as f:
        f.write(css_rule)
    print("Updated site/_nuxt/entry.DzM0mqX9.css with safety hide rules")

if __name__ == '__main__':
    apply_removals()
