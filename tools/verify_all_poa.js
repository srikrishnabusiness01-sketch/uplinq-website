const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9255;
const ARTIFACT_DIR = "C:\\Users\\Asus\\.gemini\\antigravity\\brain\\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb";
const USER_DATA = path.join(os.tmpdir(), 'chrome_cdp_' + Date.now());

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); } catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

async function runMobileCapture() {
  console.log('Launching Headless Chrome for Mobile Verification with user-data-dir...');
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    `--user-data-dir=${USER_DATA}`,
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    '--window-size=375,812',
    'about:blank'
  ]);

  let connected = false;
  let targets = null;
  for (let i = 0; i < 30; i++) {
    await sleep(300);
    try {
      targets = await getJson(`http://127.0.0.1:${PORT}/json`);
      if (targets && targets.length > 0) {
        connected = true;
        break;
      }
    } catch (e) {}
  }

  if (!connected) {
    console.error('Could not connect to Chrome on port ' + PORT);
    chrome.kill();
    process.exit(1);
  }

  const pageTarget = targets.find(t => t.type === 'page') || targets[0];
  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
  let id = 1;
  const pending = new Map();

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const msgId = id++;
      pending.set(msgId, { resolve, reject });
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && pending.has(data.id)) {
      const p = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) p.reject(data.error);
      else p.resolve(data.result);
    }
  };

  await new Promise((resolve) => ws.onopen = resolve);

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });

  console.log('Navigating to http://localhost:3000/ ...');
  await send('Page.navigate', { url: 'http://localhost:3000/' });
  await sleep(4500);

  // 1. Services Card 1: Defining & Strategy
  console.log('Capturing Services cards...');
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelectorAll('.service-block_title')[0];
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      else window.scrollTo(0, 1000);
    })()`
  });
  await sleep(800);
  let shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_service1_defining.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_service1_defining.png');

  // 2. Services Card 2: Reaching & Growth
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelectorAll('.service-block_title')[1];
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      else window.scrollBy(0, 450);
    })()`
  });
  await sleep(800);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_service2_reaching.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_service2_reaching.png');

  // 3. Services Card 3: Automating & AI
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelectorAll('.service-block_title')[2];
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      else window.scrollBy(0, 450);
    })()`
  });
  await sleep(800);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_service3_automating.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_service3_automating.png');

  // 4. "We help them win in" with Custom Images below words
  console.log('Capturing "We help them win in" section...');
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.win-category_wrapper') || document.querySelector('.section.is--win');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      else window.scrollTo(0, 2400);
    })()`
  });
  await sleep(1000);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_win_custom_images.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_win_custom_images.png');

  // 5. Company Story Section - Block 1 & 2
  console.log('Capturing Story section...');
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelectorAll('.stats-block')[0];
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      else window.scrollTo(0, 3200);
    })()`
  });
  await sleep(1000);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_story_block1.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_story_block1.png');

  // Scroll to Story Block 2
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelectorAll('.stats-block')[1];
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      else window.scrollBy(0, 600);
    })()`
  });
  await sleep(1000);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_story_block2.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_story_block2.png');

  // Scroll to Story Block 3 & 4
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelectorAll('.stats-block')[3];
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      else window.scrollBy(0, 600);
    })()`
  });
  await sleep(1000);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_mobile_story_block4.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_mobile_story_block4.png');

  // Desktop View
  console.log('Switching to Desktop View...');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await sleep(500);

  // Scroll to "We help them win in" on desktop
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.win-category_wrapper');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await sleep(1000);
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'verify_desktop_win_section.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved verify_desktop_win_section.png');

  ws.close();
  chrome.kill();
  try { fs.rmSync(USER_DATA, { recursive: true, force: true }); } catch (e) {}
  console.log('All verifications captured successfully!');
}

runMobileCapture().catch(err => {
  console.error('Verification error:', err);
  process.exit(1);
});
