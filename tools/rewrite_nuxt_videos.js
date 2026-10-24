const fs = require('fs');
const path = require('path');

const SITE_DIR = path.join(__dirname, 'site');

function walkDir(dir) {
  let files = [];
  const list = fs.readdirSync(dir);
  for (const item of list) {
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      files = files.concat(walkDir(full));
    } else if (item.endsWith('.js') || item.endsWith('.html') || item.endsWith('.css')) {
      files.push(full);
    }
  }
  return files;
}

const files = walkDir(SITE_DIR);
let count = 0;

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  // Replace https://mdn.check-dc.com/.../filename with /assets/mdn/filename
  content = content.replace(/https:\/\/mdn\.check-dc\.com\/[^"'\s\)]+\/([a-zA-Z0-9_.-]+\.(?:webm|mp4|jpe|jpg|jpeg|png|gif|svg|webp|js|css))/g, '/assets/mdn/$1');

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    count++;
  }
}

console.log(`Updated ${count} files with local MDN asset URLs.`);
