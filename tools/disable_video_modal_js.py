with open('site/_nuxt/BMQH0uFj.js', 'r', encoding='utf-8') as f:
    js = f.read()

target1 = 'T=()=>{R.value=!0}'
assert js.count(target1) == 1, f"Expected 1 occurrence of '{target1}', found {js.count(target1)}"
js = js.replace(target1, 'T=()=>{}')

target2 = 'C(R)?(E(),U(t,{key:0,onOnClose:k[0]||(k[0]=n=>R.value=!1)})):G0("",!0)'
assert js.count(target2) == 1, f"Expected 1 occurrence of '{target2}', found {js.count(target2)}"
js = js.replace(target2, 'G0("",!0)')

with open('site/_nuxt/BMQH0uFj.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated site/_nuxt/BMQH0uFj.js successfully.")
