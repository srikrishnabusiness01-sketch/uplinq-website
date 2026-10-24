const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'CKrmhtJt.js'), 'utf8');

let pos = 0;
while ((pos = code.indexOf('on-loaded', pos)) !== -1) {
  console.log('CKrmhtJt.js snippet around', pos, ':');
  console.log(code.substring(Math.max(0, pos - 200), Math.min(code.length, pos + 300)));
  pos += 10;
}
