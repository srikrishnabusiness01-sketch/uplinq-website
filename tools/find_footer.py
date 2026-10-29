with open('site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<footer')
if idx != -1:
    print("Before footer:")
    print(c[idx-1500:idx+1500])
else:
    print("No <footer found!")
