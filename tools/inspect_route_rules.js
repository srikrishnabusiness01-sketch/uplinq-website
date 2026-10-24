const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'CKrmhtJt.js'), 'utf8');

const pos = code.indexOf('_sortRoutesMap');
if (pos !== -1) {
  console.log('Found _sortRoutesMap at:', pos);
  console.log(code.substring(Math.max(0, pos - 500), Math.min(code.length, pos + 1000)));
} else {
  console.log('_sortRoutesMap not found directly');
  // Search for getRouteRules
  const p2 = code.indexOf('getRouteRules');
  console.log('getRouteRules at:', p2);
  console.log(code.substring(Math.max(0, p2 - 500), Math.min(code.length, p2 + 1000)));
}
