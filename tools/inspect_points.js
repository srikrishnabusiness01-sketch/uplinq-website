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
  await send('Page.navigate', { url: 'http://localhost:3000/' });

  await sleep(6000);

  const res = await send('Runtime.evaluate', {
    expression: `(() => {
      const points = [
        [100, 100],
        [720, 100],
        [720, 400],
        [720, 800]
      ];
      return points.map(([x, y]) => {
        const el = document.elementFromPoint(x, y);
        if (!el) return { point: [x,y], el: null };
        const cs = getComputedStyle(el);
        return {
          point: [x,y],
          tag: el.tagName,
          class: el.className,
          bg: cs.backgroundColor,
          color: cs.color,
          op: cs.opacity,
          vis: cs.visibility,
          zIndex: cs.zIndex,
          outerHtml: el.outerHTML.substring(0, 100)
        };
      });
    })()`,
    returnByValue: true
  });

  console.log('Elements at points:', JSON.stringify(res.result.value, null, 2));

  ws.close();
  chrome.kill();
}

main().catch(console.error);
