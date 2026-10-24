const fs = require('fs');
const html = fs.readFileSync('site/index.html', 'utf8');

const pos = html.indexOf('class="section-header"');
console.log(html.substring(pos, pos + 3000));
