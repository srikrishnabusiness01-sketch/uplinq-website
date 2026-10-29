import subprocess
import re

out = subprocess.check_output(['git', 'show', '237283e:site/index.html'], encoding='utf-8')
matches = [m.start() for m in re.finditer(r'<nav', out)]
for m in matches:
    print(out[m:m+600])
