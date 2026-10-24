const fs = require('fs');
const path = require('path');

const SITE_DIR = path.join(__dirname, '..', 'site');

function walkDir(dir) {
  let files = [];
  const list = fs.readdirSync(dir);
  for (const item of list) {
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      files = files.concat(walkDir(full));
    } else {
      files.push(full);
    }
  }
  return files;
}

const allFiles = walkDir(SITE_DIR);
const htmlFiles = allFiles.filter(f => f.endsWith('.html'));

console.log(`Found ${htmlFiles.length} HTML files:`);
htmlFiles.forEach(f => console.log('  ', path.relative(SITE_DIR, f)));

let missingAssets = new Set();
let foundAssets = new Set();

for (const htmlFile of htmlFiles) {
  const content = fs.readFileSync(htmlFile, 'utf8');

  // Check src and href
  const matches = [...content.matchAll(/(?:src|href)=["']([^"'#?]+)["']/gi)].map(m => m[1]);
  for (const m of matches) {
    if (m.startsWith('http://') || m.startsWith('https://') || m.startsWith('mailto:') || m.startsWith('data:') || m.startsWith('javascript:')) {
      continue;
    }
    // Relative to site root
    let cleanPath = m.startsWith('/') ? m.slice(1) : m;
    // If it's a page link like "work" or "about", it's an internal route
    if (!cleanPath.includes('.') && cleanPath !== '') {
      const pagePath = path.join(SITE_DIR, cleanPath, 'index.html');
      if (!fs.existsSync(pagePath)) {
        missingAssets.add(`Route: ${m} in ${path.relative(SITE_DIR, htmlFile)}`);
      } else {
        foundAssets.add(`Route: ${m}`);
      }
      continue;
    }
    const assetPath = path.join(SITE_DIR, cleanPath);
    if (!fs.existsSync(assetPath)) {
      missingAssets.add(`Asset: ${m} in ${path.relative(SITE_DIR, htmlFile)}`);
    } else {
      foundAssets.add(`Asset: ${m}`);
    }
  }
}

console.log(`\nVerified ${foundAssets.size} valid local links/assets.`);
console.log(`Missing assets: ${missingAssets.size}`);
if (missingAssets.size > 0) {
  console.log('List of missing:');
  missingAssets.forEach(m => console.log('  ', m));
}
