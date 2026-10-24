const fs = require('fs');
const html = fs.readFileSync('site/index.html', 'utf8');

console.log('--- HEAD SCRIPTS ---');
const scripts = [...html.matchAll(/<script\b[^>]*src=["']([^"']+)["'][^>]*>/gi)].map(m => m[0]);
scripts.forEach(s => console.log(s));

console.log('\n--- HEAD STYLES / LINKS ---');
const links = [...html.matchAll(/<link\b[^>]*href=["']([^"']+)["'][^>]*>/gi)].map(m => m[0]);
links.forEach(l => console.log(l));
