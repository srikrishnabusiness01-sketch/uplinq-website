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

  await sleep(1000);
  const targets = await getJson(`http://127.0.0.1:${PORT}/json`);
  const ws = new WebSocket(targets[0].webSocketDebuggerUrl);

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

  console.log('Waiting 12 seconds for loader to completely dismiss...');
  await sleep(12000);

  const evalState = await send('Runtime.evaluate', {
    expression: `({
      loaderOpacity: getComputedStyle(document.querySelector('.c-loader')).opacity,
      loaderVisibility: getComputedStyle(document.querySelector('.c-loader')).visibility,
      loaderDisplay: getComputedStyle(document.querySelector('.c-loader')).display,
      loaderPointerEvents: getComputedStyle(document.querySelector('.c-loader')).pointerEvents,
      loaderZIndex: getComputedStyle(document.querySelector('.c-loader')).zIndex,
      headerTitle: document.querySelector('.header-title_wrapper') ? document.querySelector('.header-title_wrapper').innerText : 'no header title'
    })`,
    returnByValue: true
  });
  console.log('DOM state at 12s:', JSON.stringify(evalState.result.value));

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(__dirname, 'frame_top_12s.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved frame_top_12s.png');

  ws.close();
  chrome.kill();
}

main().catch(console.error);
