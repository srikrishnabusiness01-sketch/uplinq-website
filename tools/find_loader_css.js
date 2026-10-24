const fs = require('fs');
const path = require('path');

const files = ['site/index.html', 'site/_nuxt/default.-CLknPkJ.css', 'site/_nuxt/entry.DzM0mqX9.css'];
for (const f of files) {
  if (fs.existsSync(f)) {
    const text = fs.readFileSync(f, 'utf8');
    const matches = [...text.matchAll(/(?:\.c-loader|\.loader-progress_bar)[^{]*\{[^}]+\}/g)].map(m => m[0]);
    if (matches.length) {
      console.log('Matches in', f, ':');
      matches.forEach(m => console.log('  ', m));
    }
  }
}
