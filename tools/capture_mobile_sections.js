const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9223;
const ARTIFACT_DIR = "C:\\Users\\Asus\\.gemini\\antigravity\\brain\\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb";

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

async function main() {
  console.log('Launching Headless Chrome for Mobile Inspection...');
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
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
    console.error('Could not connect to Chrome CDP on port ' + PORT);
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

  console.log('Waiting for loader completion...');
  await sleep(5000);

  // 1. Hero Screenshot
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'mobile_1_hero.png'), Buffer.from(shot1.data, 'base64'));
  console.log('Captured mobile_1_hero.png');

  // 2. Services Section
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.section.is--services') || document.querySelector('.services-block') || document.querySelector('.service-block_item');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      else window.scrollTo(0, 1100);
    })()`
  });
  await sleep(1000);
  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'mobile_2_services.png'), Buffer.from(shot2.data, 'base64'));
  console.log('Captured mobile_2_services.png');

  // Scroll a bit more within services
  await send('Runtime.evaluate', { expression: `window.scrollBy(0, 500);` });
  await sleep(1000);
  const shot2b = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'mobile_2b_services.png'), Buffer.from(shot2b.data, 'base64'));
  console.log('Captured mobile_2b_services.png');

  // 3. Impact Words Section (.is--win)
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.section.is--win') || document.querySelector('.win-title_wrapper');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      else window.scrollTo(0, 2200);
    })()`
  });
  await sleep(1000);
  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'mobile_3_impact.png'), Buffer.from(shot3.data, 'base64'));
  console.log('Captured mobile_3_impact.png');

  // 4. Company Story Section (.is--stats)
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.section.is--stats') || document.querySelector('.stats-block_wrapper');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      else window.scrollTo(0, 3100);
    })()`
  });
  await sleep(1000);
  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'mobile_4_story.png'), Buffer.from(shot4.data, 'base64'));
  console.log('Captured mobile_4_story.png');

  // 5. Test Click on LET'S GROW button
  console.log('Testing "LET\'S GROW" click to trigger Contact Form...');
  await send('Runtime.evaluate', {
    expression: `(() => {
      window.scrollTo(0, 0);
      const btn = Array.from(document.querySelectorAll('.c-button, button')).find(b => b.innerText.includes("LET'S GROW") || b.innerText.includes("LETS GROW"));
      if (btn) btn.click();
    })()`
  });
  await sleep(1500);
  const shot5 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'mobile_5_modal.png'), Buffer.from(shot5.data, 'base64'));
  console.log('Captured mobile_5_modal.png');

  ws.close();
  chrome.kill();
  console.log('Mobile inspection completed successfully!');
}

main().catch(err => {
  console.error('Mobile inspection failed:', err);
  process.exit(1);
});
