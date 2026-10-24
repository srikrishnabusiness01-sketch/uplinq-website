const fs = require('fs');
const path = require('path');

const jsPath = path.join(__dirname, '..', 'site', '_nuxt', 'B0CwXBEy.js');
let code = fs.readFileSync(jsPath, 'utf8');

const target = '.to(".c-loader",{autoAlpha:0,duration:.2,onStart:()=>{I("on-loaded")}},"<+1.2")';
console.log('Includes autoAlpha target:', code.includes(target));

if (code.includes(target)) {
  const replacement = '.to(".c-loader",{autoAlpha:0,duration:.2,onStart:()=>{I("on-loaded")},onComplete:()=>{const el=document.querySelector(".c-loader");if(el){el.style.display="none";el.style.visibility="hidden";el.style.pointerEvents="none";}}},"<+1.2")';
  code = code.replace(target, replacement);
  fs.writeFileSync(jsPath, code, 'utf8');
  console.log('Successfully patched onComplete on .c-loader in B0CwXBEy.js!');
}
