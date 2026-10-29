js_path = 'site/_nuxt/CKrmhtJt.js'
js_txt = open(js_path, encoding='utf-8').read()

target = '{default:withCtx(()=>[_hoisted_5$2]),_:1}),createCommentVNode("v-if",!0),'
replacement = '{default:withCtx(()=>[_hoisted_5$2]),_:1}),createBaseVNode("button",{class:"menu-button",onClick:d},_hoisted_8$2),'

if target in js_txt:
    js_txt = js_txt.replace(target, replacement, 1)
    open(js_path, 'w', encoding='utf-8').write(js_txt)
    print("SUCCESS: Menu button restored in CKrmhtJt.js!")
else:
    print("ERROR: Target not found in CKrmhtJt.js")
