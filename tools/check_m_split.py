with open('site/_nuxt/CB5bwoBe.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('split')
while idx != -1:
    print(c[max(0, idx-20):min(len(c), idx+100)])
    idx = c.find('split', idx+1)
