const { spawn } = require('child_process');
const http = require('http');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9235;

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

  const evalRes = await send('Runtime.evaluate', {
    expression: `(() => {
      const statsWrapper = document.querySelector('.stats-block_wrapper');
      const statsBlocks = Array.from(document.querySelectorAll('.stats-block')).map((b, i) => ({
        index: i,
        text: b.innerText,
        rect: b.getBoundingClientRect(),
        display: window.getComputedStyle(b).display,
        children: Array.from(b.children).map(c => ({
          className: c.className,
          rect: c.getBoundingClientRect(),
          display: window.getComputedStyle(c).display,
          opacity: window.getComputedStyle(c).opacity
        }))
      }));

      const sketchBlocks = Array.from(document.querySelectorAll('.stats-sketch_block')).map((s, i) => ({
        index: i,
        className: s.className,
        rect: s.getBoundingClientRect(),
        display: window.getComputedStyle(s).display,
        img: s.querySelector('img') ? s.querySelector('img').src : null,
        imgDisplay: s.querySelector('img') ? window.getComputedStyle(s.querySelector('img')).display : null,
        video: s.querySelector('video') ? s.querySelector('video').src : null
      }));

      return JSON.stringify({ statsBlocks, sketchBlocks }, null, 2);
    })()`,
    returnByValue: true
  });

  console.log('Stats evaluation:', evalRes.result.value);

  ws.close();
  chrome.kill();
}

main().catch(console.error);
