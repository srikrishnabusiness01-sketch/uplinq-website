const { spawn } = require('child_process');
const http = require('http');

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

  console.log('Sampling DOM every 1 second for 10 seconds...');
  for (let s = 1; s <= 10; s++) {
    await sleep(1000);
    const res = await send('Runtime.evaluate', {
      expression: `({
        second: ${s},
        loaderOpacity: (document.querySelector('.c-loader') ? getComputedStyle(document.querySelector('.c-loader')).opacity : 'none'),
        loaderVisibility: (document.querySelector('.c-loader') ? getComputedStyle(document.querySelector('.c-loader')).visibility : 'none'),
        loaderDisplay: (document.querySelector('.c-loader') ? getComputedStyle(document.querySelector('.c-loader')).display : 'none'),
        mainWrapperOpacity: (document.querySelector('.main-wrapper') ? getComputedStyle(document.querySelector('.main-wrapper')).opacity : 'none'),
        mainWrapperVisibility: (document.querySelector('.main-wrapper') ? getComputedStyle(document.querySelector('.main-wrapper')).visibility : 'none'),
        headerOpacity: (document.querySelector('.section-header') ? getComputedStyle(document.querySelector('.section-header')).opacity : 'none'),
        loadingText: (document.querySelector('.loading-text') ? document.querySelector('.loading-text').innerText : '')
      })`,
      returnByValue: true
    });
    console.log(JSON.stringify(res.result.value));
  }

  ws.close();
  chrome.kill();
}

main().catch(console.error);
