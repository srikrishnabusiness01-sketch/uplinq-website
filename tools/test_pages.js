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

  const pagesToTest = [
    { url: 'http://localhost:3000/work', name: 'frame_page_work.png' },
    { url: 'http://localhost:3000/case/nlng', name: 'frame_page_nlng.png' },
    { url: 'http://localhost:3000/work/quidax', name: 'frame_page_quidax.png' }
  ];

  for (const p of pagesToTest) {
    console.log(`Navigating to ${p.url}...`);
    await send('Page.navigate', { url: p.url });
    await sleep(4000);
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(path.join(__dirname, p.name), Buffer.from(shot.data, 'base64'));
    console.log(`Saved ${p.name}`);
  }

  ws.close();
  chrome.kill();
  console.log('All page frame tests done!');
}

main().catch(console.error);
