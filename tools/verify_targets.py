with open('site/_nuxt/B0CwXBEy.js', 'r', encoding='utf-8') as f:
    b0 = f.read()

targets_b0 = [
    'x(" Bonjour, "),e("br"),x(" Got a Project? ")',
    'e("p",{class:"form-subtext"},"What would you like to do?")',
    'Su=F(()=>e("span",{class:"checkbox-label w-form-label",for:"branding"}," Branding ",-1))',
    '$u=F(()=>e("span",{class:"checkbox-label w-form-label",for:"website-design"}," Website Design ",-1))',
    'Pu=F(()=>e("span",{class:"checkbox-label w-form-label",for:"mobile-app"}," Mobile App Development ",-1))',
    'Yu=F(()=>e("span",{class:"checkbox-label w-form-label",for:"web-app"}," Web App Development ",-1))',
    'name:"branding",type:"checkbox",value:"Branding"}',
    'name:"website-design",type:"checkbox",value:"Website Design"}',
    'name:"mobile-app",type:"checkbox",value:"Mobile App Development"}',
    'name:"web-app",type:"checkbox",value:"Web App Development"}'
]

print("=== Targets in B0CwXBEy.js ===")
for t in targets_b0:
    count = b0.count(t)
    print(f"Target '{t[:40]}...': count = {count}")
    assert count == 1, f"Expected 1 occurrence of {t}, found {count}"

with open('site/_nuxt/DSgCRULr.js', 'r', encoding='utf-8') as f:
    ds = f.read()

targets_ds = [
    'n(" Bonjour, "),e("br"),n(" Got a Project? ")',
    'e("p",{class:"form-subtext"},"What would you like to do?")',
    'ne=c(()=>e("span",{class:"checkbox-label w-form-label",for:"branding"}," Branding ",-1))',
    've=c(()=>e("span",{class:"checkbox-label w-form-label",for:"website-design"}," Website Design ",-1))',
    'ue=c(()=>e("span",{class:"checkbox-label w-form-label",for:"mobile-app"}," Mobile App Development ",-1))',
    'ge=c(()=>e("span",{class:"checkbox-label w-form-label",for:"web-app"}," Web App Development ",-1))',
    'name:"branding",type:"checkbox",value:"Branding"}',
    'name:"website-design",type:"checkbox",value:"Website Design"}',
    'name:"mobile-app",type:"checkbox",value:"Mobile App Development"}',
    'name:"web-app",type:"checkbox",value:"Web App Development"}'
]

print("=== Targets in DSgCRULr.js ===")
for t in targets_ds:
    count = ds.count(t)
    print(f"Target '{t[:40]}...': count = {count}")
    assert count == 1, f"Expected 1 occurrence of {t}, found {count}"

print("All targets verified successfully!")
