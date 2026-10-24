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

  await sleep(10000);

  const res = await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.elementFromPoint(720, 450);
      const topEl = el ? {
        tagName: el.tagName,
        className: el.className,
        id: el.id,
        opacity: getComputedStyle(el).opacity,
        visibility: getComputedStyle(el).visibility,
        backgroundColor: getComputedStyle(el).backgroundColor,
        width: el.offsetWidth,
        height: el.offsetHeight,
        outerHTMLPreview: el.outerHTML.substring(0, 300)
      } : null;

      const header = document.querySelector('.section-header');
      const headerInfo = header ? {
        opacity: getComputedStyle(header).opacity,
        visibility: getComputedStyle(header).visibility,
        display: getComputedStyle(header).display,
        color: getComputedStyle(header).color,
        backgroundColor: getComputedStyle(header).backgroundColor,
        height: header.offsetHeight
      } : 'no header';

      return JSON.stringify({ topEl, headerInfo });
    })()`,
    returnByValue: true
  });

  console.log('Element at point (720, 450):', res.result.value);

  ws.close();
  chrome.kill();
}

main().catch(console.error);
