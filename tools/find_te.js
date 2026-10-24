const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js'), 'utf8');

// Find where Te is instantiated or used in template
let p = 0;
while ((p = code.indexOf('Te', p)) !== -1) {
  const snippet = code.substring(Math.max(0, p - 50), Math.min(code.length, p + 100));
  if (snippet.includes('createVNode') || snippet.includes('resolveComponent') || snippet.includes('setup') || snippet.includes('Loader') || snippet.includes('"on-loaded"')) {
    console.log('Snippet at', p, ':\n', snippet);
  }
  p += 2;
}
