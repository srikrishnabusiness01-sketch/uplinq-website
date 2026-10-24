const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js'), 'utf8');

let p = 15000;
while ((p = code.indexOf('Te', p)) !== -1) {
  console.log('Te found at', p, ':', code.substring(Math.max(0, p - 30), Math.min(code.length, p + 70)));
  p += 2;
}
