const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js'), 'utf8');

console.log(code.substring(37500, 39500));
