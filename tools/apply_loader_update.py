import os

def update_content(text):
    # Step 1: Replace original targets with unique tokens
    t1 = ' LOADING ENGINEERING LOADING ENGINEERING LOADING ENGINEERING LOADING ENGINEERING LOADING ENGINEERING '
    t2 = 'LOADING CHECK LOADING CHECK LOADING CHECK LOADING CHECK LOADING CHECK'
    t3 = ' LOADING STRATEGY LOADING STRATEGY LOADING STRATEGY LOADING STRATEGY LOADING STRATEGY '
    t4 = 'LOADING MOTION LOADING MOTION LOADING MOTION LOADING MOTION LOADING'
    t5 = 'LOADING BRANDS LOADING BRANDS LOADING BRANDS LOADING BRANDS LOADING BRANDS'
    t6 = 'LOADING DIGITAL LOADING DIGITAL LOADING DIGITAL LOADING DIGITAL LOADING DIGITAL'
    t7 = 'LOADING LOADING LOADING LOADING LOADING LOADING LOADING LOADING LOADING LOADING'
    tc = '<div class="loading-text">Reimagine</div>'

    text = text.replace(t1, '###TOKEN_R1###')
    text = text.replace(t2, '###TOKEN_R2###')
    text = text.replace(t3, '###TOKEN_R3###')
    text = text.replace(t4, '###TOKEN_R4###')
    text = text.replace(t5, '###TOKEN_R5###')
    text = text.replace(t6, '###TOKEN_R6###')
    text = text.replace(t7, '###TOKEN_R7###')
    text = text.replace(tc, '###TOKEN_CENTER###')

    # Also in JS if present:
    # v.to(u,{text:"Redefine"}),v.to(u,{text:"Reinvent"},">+2"),v.to(u,{text:"Reimagine"},">+2")
    # -> v.to(u,{text:"UPLINQ"})
    # to(u,{text:"Rethink"}) -> to(u,{text:"UPLINQ"})
    text = text.replace('{text:"Rethink"}', '{text:"UPLINQ"}')
    text = text.replace('{text:"Redefine"}', '{text:"UPLINQ"}')
    text = text.replace('{text:"Reinvent"}', '{text:"UPLINQ"}')
    text = text.replace('{text:"Reimagine"}', '{text:"UPLINQ"}')

    # Step 2: Replace tokens with user content
    r1 = ' LOADING STRATEGY LOADING STRATEGY LOADING STRATEGY LOADING STRATEGY LOADING STRATEGY '
    r2 = 'LOADING RESEARCH LOADING RESEARCH LOADING RESEARCH LOADING RESEARCH LOADING RESEARCH'
    r3 = ' LOADING UPLINQ LOADING UPLINQ LOADING UPLINQ LOADING UPLINQ LOADING UPLINQ '
    r4 = 'LOADING POSITIONING LOADING POSITIONING LOADING POSITIONING LOADING POSITIONING LOADING POSITIONING'
    r5 = 'LOADING LEAD GENERATION LOADING LEAD GENERATION LOADING LEAD GENERATION LOADING LEAD GENERATION LOADING LEAD GENERATION'
    r6 = 'LOADING AUTOMATION LOADING AUTOMATION LOADING AUTOMATION LOADING AUTOMATION LOADING AUTOMATION'
    r7 = 'LOADING GROWTH LOADING GROWTH LOADING GROWTH LOADING GROWTH LOADING GROWTH'
    rc = '<div class="loading-text">UPLINQ</div>'

    text = text.replace('###TOKEN_R1###', r1)
    text = text.replace('###TOKEN_R2###', r2)
    text = text.replace('###TOKEN_R3###', r3)
    text = text.replace('###TOKEN_R4###', r4)
    text = text.replace('###TOKEN_R5###', r5)
    text = text.replace('###TOKEN_R6###', r6)
    text = text.replace('###TOKEN_R7###', r7)
    text = text.replace('###TOKEN_CENTER###', rc)

    return text

site_dir = r"site"

# Update HTML files
html_count = 0
for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f == "index.html":
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8") as fp:
                content = fp.read()
            new_content = update_content(content)
            if new_content != content:
                with open(p, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                html_count += 1
                print("Updated HTML:", p)

# Update B0CwXBEy.js
js_file = os.path.join(site_dir, "_nuxt", "B0CwXBEy.js")
if os.path.exists(js_file):
    with open(js_file, "r", encoding="utf-8") as fp:
        content = fp.read()
    new_content = update_content(content)
    if new_content != content:
        with open(js_file, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        print("Updated JS:", js_file)

print(f"Update complete! {html_count} HTML files and JS bundle updated.")
