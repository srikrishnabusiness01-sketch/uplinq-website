const fs = require('fs');
const path = require('path');

const jsPath = path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js');
let code = fs.readFileSync(jsPath, 'utf8');

const target = 'if(u.style.width="100%",a.value&&h.name==="index")return p.value=100,m();if(h.name!=="index")return p.value=100,m()';
console.log('Includes exact target:', code.includes(target));

if (code.includes(target)) {
  const replacement = 'if(u.style.width="100%")return p.value=100,m();';
  code = code.replace(target, replacement);
  fs.writeFileSync(jsPath, code, 'utf8');
  console.log('Successfully patched loader dismissal in B0CwXBEy.js!');
} else {
  // Find substring
  const pos = code.indexOf('u.style.width="100%"');
  console.log('Snippet around width 100%:', code.substring(pos, pos + 150));
}
