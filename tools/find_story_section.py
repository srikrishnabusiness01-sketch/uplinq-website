txt = open('site/index.html', encoding='utf-8').read()

idx = txt.find('Raising funds')
if idx == -1:
    idx = txt.find('REAL REVENUE')
print(txt[idx-300:idx+1500])
