const fs = require('fs');
const path = require('path');

function walk(dir) {
  let files = [];
  for (const item of fs.readdirSync(dir)) {
    const p = path.join(dir, item);
    if (fs.statSync(p).isDirectory()) files = files.concat(walk(p));
    else files.push(p);
  }
  return files;
}

const allFiles = walk('site');
const assetImages = new Set();

for (const f of allFiles) {
  if (f.endsWith('.js') || f.endsWith('.css') || f.endsWith('.html')) {
    const text = fs.readFileSync(f, 'utf8');
    const matches = [...text.matchAll(/\/assets\/images\/[a-zA-Z0-9_.-]+/g)].map(m => m[0]);
    matches.forEach(m => assetImages.add(m));
  }
}

console.log('Found /assets/images/ references count:', assetImages.size);
assetImages.forEach(a => console.log('  ', a));
