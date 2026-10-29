import subprocess
import re

out = subprocess.check_output(['git', 'show', '237283e:site/index.html'], encoding='utf-8')
idx = out.find('nav-inner')
print("Initial commit nav snippet:")
print(out[idx-30:idx+600])
