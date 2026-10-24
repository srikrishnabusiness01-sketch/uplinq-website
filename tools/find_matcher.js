const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'CKrmhtJt.js'), 'utf8');

const pos = code.indexOf('createMatcherFromExport');
console.log('Calls to createMatcherFromExport:');
let p = 0;
while ((p = code.indexOf('createMatcherFromExport', p)) !== -1) {
  console.log('Position:', p);
  console.log(code.substring(Math.max(0, p - 300), Math.min(code.length, p + 500)));
  p += 20;
}
