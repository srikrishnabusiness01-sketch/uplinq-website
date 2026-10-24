const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9222;

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}

async function main() {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,900',
    'about:blank'
  ]);

  await sleep(1500);
  const targets = await getJson(`http://127.0.0.1:${PORT}/json`);
  const pageTarget = targets.find(t => t.type === 'page' && !t.url.startsWith('chrome-extension')) || targets[0];
  console.log('Using target URL:', pageTarget.url);

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
  await send('Page.navigate', { url: 'http://localhost:3000/' });

  console.log('Waiting 6 seconds for snappy loader and hero transition...');
  await sleep(6000);

  const res = await send('Runtime.evaluate', {
    expression: `(() => {
      const loader = document.querySelector('.c-loader');
      return JSON.stringify({
        loaderExists: !!loader,
        loaderOpacity: loader ? getComputedStyle(loader).opacity : null,
        loaderDisplay: loader ? getComputedStyle(loader).display : null,
        loaderVisibility: loader ? getComputedStyle(loader).visibility : null,
        h1Text: document.querySelector('h1') ? document.querySelector('h1').innerText : null,
        scrollY: window.scrollY
      });
    })()`,
    returnByValue: true
  });

  console.log('Result at 14s:', res.result.value);

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(__dirname, 'frame_top_hero_14s.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved frame_top_hero_14s.png');

  ws.close();
  chrome.kill();
}

main().catch(console.error);
