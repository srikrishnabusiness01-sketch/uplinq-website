const fs = require('fs');
const path = require('path');

const jsPath = path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js');
let code = fs.readFileSync(jsPath, 'utf8');

// Speed up initial fonts ready timeout from 1000ms to 150ms
code = code.replace('setTimeout(()=>{f(),G(),E(i.value)},1e3)', 'setTimeout(()=>{f(),G(),E(i.value)},150)');

// Speed up m() exit delay from 1000ms to 250ms
code = code.replace('},1e3)};return U', '},250)};return U');

// Speed up loader-progress_bar scale animation duration from 2 to 0.9s
code = code.replace('scale:c.isMobile?25:15,duration:2,ease:"expo.inOut"', 'scale:c.isMobile?25:15,duration:0.9,ease:"expo.inOut"');

fs.writeFileSync(jsPath, code, 'utf8');
console.log('Optimized loader timing to snappy ~2s in B0CwXBEy.js!');
