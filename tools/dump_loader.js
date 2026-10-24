const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js'), 'utf8');

const pos = code.indexOf('class:"c-loader"');
console.log('Loader component code:');
console.log(code.substring(pos, pos + 3500));
