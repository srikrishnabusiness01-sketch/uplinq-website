const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const BASE_URL = 'https://wearecheck.co';
const OUT_DIR = path.join(__dirname, 'site');

const DIRS = {
  root: OUT_DIR,
  nuxt: path.join(OUT_DIR, '_nuxt'),
  fonts: path.join(OUT_DIR, 'assets', 'fonts'),
  mdn: path.join(OUT_DIR, 'assets', 'mdn'),
  cdn: path.join(OUT_DIR, 'assets', 'cdn')
};

for (const d of Object.values(DIRS)) {
  if (!fs.existsSync(d)) {
    fs.mkdirSync(d, { recursive: true });
  }
}

function fetchBuffer(url) {
  return new Promise((resolve, reject) => {
    const client = url.startsWith('https') ? https : http;
    const req = client.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*'
      }
    }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        let redirectUrl = res.headers.location;
        if (!redirectUrl.startsWith('http')) {
          const u = new URL(url);
          redirectUrl = `${u.protocol}//${u.host}${redirectUrl}`;
        }
        return fetchBuffer(redirectUrl).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`Status ${res.statusCode} for ${url}`));
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject);
    req.setTimeout(45000, () => {
      req.destroy();
      reject(new Error(`Timeout for ${url}`));
    });
  });
}

const downloaded = new Set();
const assetMap = new Map(); // original URL -> local relative path

function getFilenameFromUrl(url) {
  try {
    const parsed = new URL(url, BASE_URL);
    let pathname = decodeURIComponent(parsed.pathname);
    return path.basename(pathname) || 'file';
  } catch (e) {
    return path.basename(url.split('?')[0]) || 'file';
  }
}

async function downloadAsset(url, targetFolder, localWebPrefix) {
  if (downloaded.has(url)) {
    return assetMap.get(url);
  }
  downloaded.add(url);

  const filename = getFilenameFromUrl(url);
  const destPath = path.join(targetFolder, filename);
  const localWebPath = localWebPrefix + '/' + filename;
  assetMap.set(url, localWebPath);

  if (fs.existsSync(destPath)) {
    console.log(`[Cache] ${filename}`);
    return localWebPath;
  }

  try {
    console.log(`[Downloading] ${url} -> ${filename}`);
    const buffer = await fetchBuffer(url);
    fs.writeFileSync(destPath, buffer);
    return localWebPath;
  } catch (err) {
    console.error(`[Failed] ${url}: ${err.message}`);
    return url;
  }
}

// Queue system for concurrency control
async function processQueue(items, handler, concurrency = 6) {
  const results = [];
  let index = 0;

  async function worker() {
    while (index < items.length) {
      const i = index++;
      results[i] = await handler(items[i]);
    }
  }

  const workers = Array.from({ length: Math.min(concurrency, items.length) }, () => worker());
  await Promise.all(workers);
  return results;
}

const pages = [
  '/',
  '/about',
  '/services',
  '/blog',
  '/careers',
  '/work',
  '/case/nlng',
  '/work/quidax',
  '/work/kele',
  '/work/autograph',
  '/work/propel',
  '/work/adidas',
  '/work/odla',
  '/work/oui-capital',
  '/work/creyv',
  '/work/nnpcl',
  '/work/cardinal-stone'
];

async function main() {
  console.log('=== Step 1: Downloading HTML Pages ===');
  const pageHtmls = new Map();

  for (const pagePath of pages) {
    const pageUrl = pagePath === '/' ? BASE_URL : `${BASE_URL}${pagePath}`;
    try {
      console.log(`Fetching page: ${pagePath} (${pageUrl})`);
      const buf = await fetchBuffer(pageUrl);
      pageHtmls.set(pagePath, buf.toString('utf8'));
    } catch (e) {
      console.error(`Error fetching page ${pagePath}:`, e.message);
    }
  }

  console.log(`Downloaded ${pageHtmls.size} pages.`);

  console.log('=== Step 2: Collecting all assets from HTML ===');
  const nuxtAssets = new Set();
  const fontAssets = new Set();
  const mdnAssets = new Set();
  const cdnAssets = new Set();
  const otherAssets = new Set(['/favicon.png', '/webclip.png']);

  for (const [pagePath, html] of pageHtmls.entries()) {
    // Fonts
    const fontMatches = [...html.matchAll(/url\(([^)]+\.(?:ttf|otf|woff2?))\)/gi)].map(m => m[1].replace(/['"]/g, ''));
    fontMatches.forEach(f => fontAssets.add(f));

    // Nuxt assets
    const nuxtMatches = [...html.matchAll(/["'](\/_nuxt\/[^"']+)["']/gi)].map(m => m[1]);
    nuxtMatches.forEach(n => nuxtAssets.add(n));

    // MDN assets
    const mdnMatches = [...html.matchAll(/["'](https:\/\/mdn\.check-dc\.com\/[^"']+)["']/gi)].map(m => m[1]);
    mdnMatches.forEach(m => mdnAssets.add(m));

    // CDN assets
    const cdnMatches = [...html.matchAll(/["'](https:\/\/cdn\.prod\.website-files\.com\/[^"']+)["']/gi)].map(m => m[1]);
    cdnMatches.forEach(c => cdnAssets.add(c));
  }

  console.log(`Found:`);
  console.log(`  Fonts: ${fontAssets.size}`);
  console.log(`  Nuxt assets: ${nuxtAssets.size}`);
  console.log(`  MDN assets: ${mdnAssets.size}`);
  console.log(`  CDN assets: ${cdnAssets.size}`);

  console.log('=== Step 3: Downloading Fonts ===');
  await processQueue(Array.from(fontAssets), async (fontRelPath) => {
    const fullUrl = fontRelPath.startsWith('http') ? fontRelPath : `${BASE_URL}${fontRelPath.startsWith('/') ? '' : '/'}${fontRelPath}`;
    await downloadAsset(fullUrl, DIRS.fonts, '/assets/fonts');
  }, 4);

  console.log('=== Step 4: Downloading MDN Assets (GSAP Plugins, Videos, Images) ===');
  await processQueue(Array.from(mdnAssets), async (url) => {
    await downloadAsset(url, DIRS.mdn, '/assets/mdn');
  }, 4);

  console.log('=== Step 5: Downloading CDN Assets (Webflow Images/Gifs) ===');
  await processQueue(Array.from(cdnAssets), async (url) => {
    await downloadAsset(url, DIRS.cdn, '/assets/cdn');
  }, 4);

  console.log('=== Step 6: Downloading Favicon and Webclip ===');
  for (const a of otherAssets) {
    try {
      const fullUrl = `${BASE_URL}${a}`;
      const buf = await fetchBuffer(fullUrl);
      fs.writeFileSync(path.join(DIRS.root, path.basename(a)), buf);
    } catch (e) {
      console.log('Could not fetch ' + a);
    }
  }

  console.log('=== Step 7: Downloading Nuxt Assets & Crawling JS/CSS imports ===');
  const crawledNuxt = new Set();
  const nuxtQueue = Array.from(nuxtAssets);

  while (nuxtQueue.length > 0) {
    const currentBatch = nuxtQueue.splice(0, 10);
    await processQueue(currentBatch, async (item) => {
      if (crawledNuxt.has(item)) return;
      crawledNuxt.add(item);

      const filename = path.basename(item.split('?')[0]);
      const destPath = path.join(DIRS.nuxt, filename);
      const fullUrl = item.startsWith('http') ? item : `${BASE_URL}${item}`;

      if (!fs.existsSync(destPath)) {
        try {
          console.log(`[Nuxt] Downloading ${filename}`);
          const buf = await fetchBuffer(fullUrl);
          fs.writeFileSync(destPath, buf);

          // If JS or CSS, inspect for more chunks
          if (filename.endsWith('.js') || filename.endsWith('.css')) {
            const content = buf.toString('utf8');
            const subMatches = [...content.matchAll(/["']([a-zA-Z0-9_-]+\.(?:js|css|svg|png|jpg|webp))["']/g)].map(m => m[1]);
            for (const sub of subMatches) {
              if (sub.length > 5 && !crawledNuxt.has('/_nuxt/' + sub)) {
                // Test if it exists
                nuxtQueue.push('/_nuxt/' + sub);
              }
            }
          }
        } catch (e) {
          console.error(`[Nuxt fail] ${filename}: ${e.message}`);
        }
      }
    }, 4);
  }

  console.log('=== Step 8: Rewriting Assets and Writing Page HTMLs ===');
  for (const [pagePath, rawHtml] of pageHtmls.entries()) {
    let html = rawHtml;

    // Replace mdn and cdn URLs
    for (const [origUrl, localUrl] of assetMap.entries()) {
      html = html.split(origUrl).join(localUrl);
    }

    // Determine target file path
    let targetFilePath;
    if (pagePath === '/') {
      targetFilePath = path.join(DIRS.root, 'index.html');
    } else {
      const pageDir = path.join(DIRS.root, pagePath.replace(/^\//, ''));
      if (!fs.existsSync(pageDir)) {
        fs.mkdirSync(pageDir, { recursive: true });
      }
      targetFilePath = path.join(pageDir, 'index.html');
    }

    fs.writeFileSync(targetFilePath, html, 'utf8');
    console.log(`Saved page: ${pagePath} -> ${targetFilePath}`);
  }

  console.log('=== Step 9: Rewriting CSS files to use local assets ===');
  const cssFiles = fs.readdirSync(DIRS.nuxt).filter(f => f.endsWith('.css'));
  for (const f of cssFiles) {
    const filePath = path.join(DIRS.nuxt, f);
    let css = fs.readFileSync(filePath, 'utf8');
    for (const [origUrl, localUrl] of assetMap.entries()) {
      css = css.split(origUrl).join(localUrl);
    }
    fs.writeFileSync(filePath, css, 'utf8');
  }

  console.log('Done! All assets and pages cloned successfully.');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
