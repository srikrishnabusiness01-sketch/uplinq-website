import os
import shutil

# 1. Backups
os.makedirs('backup_original_js', exist_ok=True)
for fname in ['B0CwXBEy.js', 'DSgCRULr.js']:
    src = os.path.join('site', '_nuxt', fname)
    dst = os.path.join('backup_original_js', fname)
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"Backed up {fname} to backup_original_js/")

# 2. Update site/_nuxt/B0CwXBEy.js
with open('site/_nuxt/B0CwXBEy.js', 'r', encoding='utf-8') as f:
    b0 = f.read()

replacements_b0 = [
    (
        'x(" Bonjour, "),e("br"),x(" Got a Project? ")',
        'x(" Hello, "),e("br"),x(" Got a Product? ")'
    ),
    (
        'e("p",{class:"form-subtext"},"What would you like to do?")',
        'e("p",{class:"form-subtext"},"What are you looking for?")'
    ),
    (
        'Su=F(()=>e("span",{class:"checkbox-label w-form-label",for:"branding"}," Branding ",-1))',
        'Su=F(()=>e("span",{class:"checkbox-label w-form-label",for:"branding"}," Strategy & Positioning ",-1))'
    ),
    (
        '$u=F(()=>e("span",{class:"checkbox-label w-form-label",for:"website-design"}," Website Design ",-1))',
        '$u=F(()=>e("span",{class:"checkbox-label w-form-label",for:"website-design"}," Lead Generation & Outreach ",-1))'
    ),
    (
        'Pu=F(()=>e("span",{class:"checkbox-label w-form-label",for:"mobile-app"}," Mobile App Development ",-1))',
        'Pu=F(()=>e("span",{class:"checkbox-label w-form-label",for:"mobile-app"}," Digital Presence & Brand ",-1))'
    ),
    (
        'Yu=F(()=>e("span",{class:"checkbox-label w-form-label",for:"web-app"}," Web App Development ",-1))',
        'Yu=F(()=>e("span",{class:"checkbox-label w-form-label",for:"web-app"}," AI & Automation ",-1))'
    ),
    (
        'name:"branding",type:"checkbox",value:"Branding"}',
        'name:"branding",type:"checkbox",value:"Strategy & Positioning"}'
    ),
    (
        'name:"website-design",type:"checkbox",value:"Website Design"}',
        'name:"website-design",type:"checkbox",value:"Lead Generation & Outreach"}'
    ),
    (
        'name:"mobile-app",type:"checkbox",value:"Mobile App Development"}',
        'name:"mobile-app",type:"checkbox",value:"Digital Presence & Brand"}'
    ),
    (
        'name:"web-app",type:"checkbox",value:"Web App Development"}',
        'name:"web-app",type:"checkbox",value:"AI & Automation"}'
    )
]

for old, new in replacements_b0:
    assert b0.count(old) == 1, f"B0CwXBEy: Expected 1 occurrence of '{old}', found {b0.count(old)}"
    b0 = b0.replace(old, new)

with open('site/_nuxt/B0CwXBEy.js', 'w', encoding='utf-8') as f:
    f.write(b0)
print("Updated site/_nuxt/B0CwXBEy.js successfully.")

# 3. Update site/_nuxt/DSgCRULr.js
with open('site/_nuxt/DSgCRULr.js', 'r', encoding='utf-8') as f:
    ds = f.read()

replacements_ds = [
    (
        'n(" Bonjour, "),e("br"),n(" Got a Project? ")',
        'n(" Hello, "),e("br"),n(" Got a Product? ")'
    ),
    (
        'e("p",{class:"form-subtext"},"What would you like to do?")',
        'e("p",{class:"form-subtext"},"What are you looking for?")'
    ),
    (
        'ne=c(()=>e("span",{class:"checkbox-label w-form-label",for:"branding"}," Branding ",-1))',
        'ne=c(()=>e("span",{class:"checkbox-label w-form-label",for:"branding"}," Strategy & Positioning ",-1))'
    ),
    (
        've=c(()=>e("span",{class:"checkbox-label w-form-label",for:"website-design"}," Website Design ",-1))',
        've=c(()=>e("span",{class:"checkbox-label w-form-label",for:"website-design"}," Lead Generation & Outreach ",-1))'
    ),
    (
        'ue=c(()=>e("span",{class:"checkbox-label w-form-label",for:"mobile-app"}," Mobile App Development ",-1))',
        'ue=c(()=>e("span",{class:"checkbox-label w-form-label",for:"mobile-app"}," Digital Presence & Brand ",-1))'
    ),
    (
        'ge=c(()=>e("span",{class:"checkbox-label w-form-label",for:"web-app"}," Web App Development ",-1))',
        'ge=c(()=>e("span",{class:"checkbox-label w-form-label",for:"web-app"}," AI & Automation ",-1))'
    ),
    (
        'name:"branding",type:"checkbox",value:"Branding"}',
        'name:"branding",type:"checkbox",value:"Strategy & Positioning"}'
    ),
    (
        'name:"website-design",type:"checkbox",value:"Website Design"}',
        'name:"website-design",type:"checkbox",value:"Lead Generation & Outreach"}'
    ),
    (
        'name:"mobile-app",type:"checkbox",value:"Mobile App Development"}',
        'name:"mobile-app",type:"checkbox",value:"Digital Presence & Brand"}'
    ),
    (
        'name:"web-app",type:"checkbox",value:"Web App Development"}',
        'name:"web-app",type:"checkbox",value:"AI & Automation"}'
    )
]

for old, new in replacements_ds:
    assert ds.count(old) == 1, f"DSgCRULr: Expected 1 occurrence of '{old}', found {ds.count(old)}"
    ds = ds.replace(old, new)

with open('site/_nuxt/DSgCRULr.js', 'w', encoding='utf-8') as f:
    f.write(ds)
print("Updated site/_nuxt/DSgCRULr.js successfully.")
