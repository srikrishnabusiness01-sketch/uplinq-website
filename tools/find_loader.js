const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, '..', 'site', '_nuxt');
const files = fs.readdirSync(dir).filter(f => f.endsWith('.js'));

for (const f of files) {
  const code = fs.readFileSync(path.join(dir, f), 'utf8');
  if (code.includes('c-loader') || code.includes('loader-fill') || code.includes('loading-percent')) {
    console.log('Loader logic found in:', f);
    const pos = code.indexOf('c-loader');
    console.log(code.substring(Math.max(0, pos - 200), Math.min(code.length, pos + 500)));
  }
}
