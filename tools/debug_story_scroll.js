const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9236;
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

  // Scroll to the exact position of "WE EXIST TO CLOSE THE GAP"
  await send('Runtime.evaluate', {
    expression: `(() => {
      const b = Array.from(document.querySelectorAll('.stats-block')).find(el => el.innerText.includes('WE EXIST TO CLOSE'));
      if (b) b.scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await sleep(1000);

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'debug_story_scroll.png'), Buffer.from(shot.data, 'base64'));

  // Also inspect computed styles of the sketch block and img
  const info = await send('Runtime.evaluate', {
    expression: `(() => {
      const block = document.querySelector('.stats-block');
      const sketch = block ? block.querySelector('.stats-sketch_block') : null;
      const img = sketch ? sketch.querySelector('img') : null;
      const video = sketch ? sketch.querySelector('video') : null;
      return JSON.stringify({
        sketchRect: sketch ? sketch.getBoundingClientRect() : null,
        sketchDisplay: sketch ? window.getComputedStyle(sketch).display : null,
        sketchHeight: sketch ? window.getComputedStyle(sketch).height : null,
        sketchWidth: sketch ? window.getComputedStyle(sketch).width : null,
        sketchBg: sketch ? window.getComputedStyle(sketch).backgroundColor : null,
        imgRect: img ? img.getBoundingClientRect() : null,
        imgDisplay: img ? window.getComputedStyle(img).display : null,
        imgOpacity: img ? window.getComputedStyle(img).opacity : null,
        imgVisibility: img ? window.getComputedStyle(img).visibility : null,
        videoRect: video ? video.getBoundingClientRect() : null,
        videoDisplay: video ? window.getComputedStyle(video).display : null
      }, null, 2);
    })()`
  });

  console.log('Sketch element info:', info.result.value);

  ws.close();
  chrome.kill();
}

main().catch(console.error);
