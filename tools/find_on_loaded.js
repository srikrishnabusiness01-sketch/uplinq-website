const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, '..', 'site', '_nuxt');
const files = fs.readdirSync(dir).filter(f => f.endsWith('.js'));

for (const f of files) {
  const code = fs.readFileSync(path.join(dir, f), 'utf8');
  if (code.includes('on-loaded') || code.includes('onLoaded')) {
    console.log('Found on-loaded in:', f);
    let pos = 0;
    while ((pos = code.indexOf('on-loaded', pos)) !== -1) {
      console.log('Snippet:', code.substring(Math.max(0, pos - 150), Math.min(code.length, pos + 250)));
      pos += 10;
    }
  }
}
