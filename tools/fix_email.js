const fs = require('fs');
const path = require('path');

const SITE_DIR = path.join(__dirname, 'site');

// Create email-decode.min.js
const emailDecodeDir = path.join(SITE_DIR, 'cdn-cgi', 'scripts', '5c5dd728', 'cloudflare-static');
if (!fs.existsSync(emailDecodeDir)) {
  fs.mkdirSync(emailDecodeDir, { recursive: true });
}

const emailDecodeScript = `
(function(){
  function r(e,t){
    var r=e.substr(t,2);
    return parseInt(r,16)
  }
  function n(n,c){
    for(var o="",a=r(n,c),i=c+2;i<n.length;i+=2){
      var l=r(n,i)^a;
      o+=String.fromCharCode(l)
    }
    return decodeURIComponent(escape(o))
  }
  var elements=document.querySelectorAll('[data-cfemail]');
  for(var i=0;i<elements.length;i++){
    try{
      var el=elements[i];
      var enc=el.getAttribute('data-cfemail');
      if(enc){
        el.parentNode.replaceChild(document.createTextNode(n(enc,0)),el);
      }
    }catch(e){}
  }
  var links=document.querySelectorAll('a[href*="/cdn-cgi/l/email-protection"]');
  for(var j=0;j<links.length;j++){
    var a=links[j];
    var h=a.getAttribute('href');
    var hashIndex=h.indexOf('#');
    if(hashIndex!==-1){
      var enc=h.substr(hashIndex+1);
      a.setAttribute('href','mailto:'+n(enc,0));
    }
  }
})();
`;

fs.writeFileSync(path.join(emailDecodeDir, 'email-decode.min.js'), emailDecodeScript.trim());
console.log('Created email-decode.min.js');

// Also update HTML files to replace /cdn-cgi/l/email-protection#... with mailto:hello@wearecheck.co directly
function walkDir(dir) {
  let files = [];
  const list = fs.readdirSync(dir);
  for (const item of list) {
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      files = files.concat(walkDir(full));
    } else if (item.endsWith('.html')) {
      files.push(full);
    }
  }
  return files;
}

const htmlFiles = walkDir(SITE_DIR);
for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');
  content = content.replace(/\/cdn-cgi\/l\/email-protection#[a-zA-Z0-9]+/g, 'mailto:hello@wearecheck.co');
  fs.writeFileSync(file, content, 'utf8');
}
console.log(`Updated ${htmlFiles.length} HTML files.`);
