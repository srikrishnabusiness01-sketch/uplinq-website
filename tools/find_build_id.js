const fs = require('fs');
const path = require('path');

const code = fs.readFileSync(path.join(__dirname, '..', 'site', 'index.html'), 'utf8');

const matches = [...code.matchAll(/buildId["']?\s*:\s*["']([^"']+)["']/g)].map(m => m[1]);
console.log('buildId in index.html:', matches);

const code2 = fs.readFileSync(path.join(__dirname, '..', 'site', '_nuxt', 'CKrmhtJt.js'), 'utf8');
const matches2 = [...code2.matchAll(/buildId["']?\s*:\s*["']([^"']+)["']/g)].map(m => m[1]);
console.log('buildId in CKrmhtJt.js:', matches2);

// Check window.__NUXT__ in index.html
const nuxtConfigMatch = code.match(/window\.__NUXT__\.config\s*=\s*(\{[\s\S]*?\});/);
if (nuxtConfigMatch) {
  console.log('window.__NUXT__.config:\n', nuxtConfigMatch[1]);
}
