const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9237;
const ARTIFACT_DIR = "C:\\Users\\Asus\\.gemini\\antigravity\\brain\\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb";

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
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
      if (targets && targets.length > 0) { connected = true; break; }
    } catch (e) {}
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

  await new Promise(r => ws.onopen = r);
  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });

  await send('Page.navigate', { url: 'http://localhost:3000/' });
  await sleep(4000);

  // 1. Hero / Nav
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'fix_1_nav_no_menu.png'), Buffer.from(shot1.data, 'base64'));
  console.log('Saved fix_1_nav_no_menu.png');

  // 2. Services Section
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.section.is--services') || document.querySelector('.service-block_item');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await sleep(1000);
  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'fix_2_services_no_menu.png'), Buffer.from(shot2.data, 'base64'));
  console.log('Saved fix_2_services_no_menu.png');

  // 3. Impact Words ("We help them win in STRATEGY REVENUE GROWTH")
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.win-category_wrapper') || document.querySelector('.win-text_wrapper');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await sleep(1000);
  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'fix_3_impact_no_images.png'), Buffer.from(shot3.data, 'base64'));
  console.log('Saved fix_3_impact_no_images.png');

  // 4. Company Story
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = Array.from(document.querySelectorAll('.stats-block')).find(b => b.innerText.includes('WE EXIST TO CLOSE'));
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await sleep(1000);
  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'fix_4_company_story.png'), Buffer.from(shot4.data, 'base64'));
  console.log('Saved fix_4_company_story.png');

  ws.close();
  chrome.kill();
  console.log('Verification finished successfully!');
}

main().catch(console.error);
