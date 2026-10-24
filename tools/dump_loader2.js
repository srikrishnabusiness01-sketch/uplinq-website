const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js'), 'utf8');

const pos = code.indexOf('class:"c-loader"');
console.log('Loader setup code:');
console.log(code.substring(pos + 3000, pos + 7000));
