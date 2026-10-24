const fs = require('fs');
const path = require('path');
const https = require('https');

const BASE_URL = 'https://wearecheck.co';
const SITE_DIR = path.join(__dirname, '..', 'site');

function fetchBuffer(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return fetchBuffer(res.headers.location).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`HTTP ${res.statusCode} for ${url}`));
      }
      const chunks = [];
      res.on('data', d => chunks.push(d));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    }).on('error', reject);
  });
}

async function saveFile(remoteUrl, localRelPath) {
  const dest = path.join(SITE_DIR, localRelPath);
  const dir = path.dirname(dest);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  try {
    const buf = await fetchBuffer(remoteUrl);
    fs.writeFileSync(dest, buf);
    console.log(`[Downloaded] ${localRelPath} (${buf.length} bytes)`);
  } catch (e) {
    console.error(`[Failed] ${localRelPath}: ${e.message}`);
  }
}

const svgs = [
  "open.svg",
  "menu-icon-white.svg",
  "arrow-right.svg",
  "arrow-right-black.svg",
  "arrow-left-black.svg",
  "arrow-right-angled.svg",
  "mailbox-illustration.svg",
  "horizontal-line-sketch.svg",
  "line-sketch.svg",
  "blog-shapes.svg",
  "search-icon.svg",
  "paginate-shape.svg",
  "services-header-sketch.svg",
  "close-icon.svg",
  "content-table-line.svg",
  "yellow-shape.svg",
  "green-shape.svg",
  "divider-line-horizontal.svg",
  "twirl-sketch-1.svg",
  "twirl-sketch-2.svg",
  "twirl-sketch-3.svg",
  "squiggle.svg",
  "plane.svg",
  "curved-line.svg",
  "error-line-1.svg",
  "error-line-2.svg",
  "error-line-3.svg",
  "error-line-4.svg"
];

const payloads = [
  "/_payload.json",
  "/about/_payload.json",
  "/services/_payload.json",
  "/careers/_payload.json",
  "/work/_payload.json",
  "/case/nlng/_payload.json",
  "/work/quidax/_payload.json",
  "/work/kele/_payload.json",
  "/work/autograph/_payload.json",
  "/work/propel/_payload.json"
];

async function main() {
  console.log('=== Step 1: Downloading Nuxt Builds Meta ===');
  await saveFile(`${BASE_URL}/_nuxt/builds/latest.json`, '_nuxt/builds/latest.json');
  await saveFile(`${BASE_URL}/_nuxt/builds/meta/db5acbb2-7a77-4559-af4b-384e021cb4e4.json`, '_nuxt/builds/meta/db5acbb2-7a77-4559-af4b-384e021cb4e4.json');

  console.log('=== Step 2: Downloading Nuxt Payloads ===');
  for (const p of payloads) {
    await saveFile(`${BASE_URL}${p}`, p.replace(/^\//, ''));
  }

  console.log('=== Step 3: Downloading /assets/images/ SVGs ===');
  for (const s of svgs) {
    await saveFile(`${BASE_URL}/assets/images/${s}`, `assets/images/${s}`);
  }

  console.log('=== Step 4: Hardening CKrmhtJt.js ===');
  const jsPath = path.join(SITE_DIR, '_nuxt', 'CKrmhtJt.js');
  let js = fs.readFileSync(jsPath, 'utf8');

  // Harden _sortRoutesMap
  const oldSort = 'function _sortRoutesMap(e){return[...e.entries()].sort((t,r)=>t[0].length-r[0].length)}';
  const newSort = 'function _sortRoutesMap(e){if(!e||typeof e.entries!=="function")return[];return[...e.entries()].sort((t,r)=>t[0].length-r[0].length)}';
  if (js.includes(oldSort)) {
    js = js.replace(oldSort, newSort);
    console.log('Patched _sortRoutesMap in CKrmhtJt.js');
  }

  // Harden _matchRoutes table defaults
  const oldMatch = 'function _matchRoutes(e,t,r){r!==!0&&e.endsWith("/")&&(e=e.slice(0,-1)||"/");const a=[];';
  const newMatch = 'function _matchRoutes(e,t,r){if(!t)return[];t.wildcard=t.wildcard||new Map();t.dynamic=t.dynamic||new Map();t.static=t.static||new Map();r!==!0&&e.endsWith("/")&&(e=e.slice(0,-1)||"/");const a=[];';
  if (js.includes(oldMatch)) {
    js = js.replace(oldMatch, newMatch);
    console.log('Patched _matchRoutes in CKrmhtJt.js');
  }

  fs.writeFileSync(jsPath, js, 'utf8');
  console.log('Done downloading and hardening!');
}

main().catch(console.error);
