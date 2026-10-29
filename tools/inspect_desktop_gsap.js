const { spawn } = require('child_process');
const http = require('http');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9233;

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
    '--window-size=1440,900',
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

  await send('Page.navigate', { url: 'http://localhost:3000/' });
  await sleep(6000);

  const evalRes = await send('Runtime.evaluate', {
    expression: `(() => {
      const topBlock = document.querySelector('.header-video_block.cc-top');
      const bottomBlock = document.querySelector('.header-video_block.cc-bottom.cc-desktop');
      const topVideo = document.querySelector('.header-video.cc-top');
      return JSON.stringify({
        topBlock: {
          style: topBlock ? topBlock.getAttribute('style') : null,
          rect: topBlock ? topBlock.getBoundingClientRect() : null,
          computedDisplay: topBlock ? window.getComputedStyle(topBlock).display : null,
          computedWidth: topBlock ? window.getComputedStyle(topBlock).width : null,
          computedMaxWidth: topBlock ? window.getComputedStyle(topBlock).maxWidth : null
        },
        bottomBlock: {
          style: bottomBlock ? bottomBlock.getAttribute('style') : null,
          rect: bottomBlock ? bottomBlock.getBoundingClientRect() : null,
          computedWidth: bottomBlock ? window.getComputedStyle(bottomBlock).width : null
        },
        topVideo: {
          src: topVideo ? topVideo.src : null,
          paused: topVideo ? topVideo.paused : null,
          readyState: topVideo ? topVideo.readyState : null,
          videoWidth: topVideo ? topVideo.videoWidth : null
        }
      }, null, 2);
    })()`,
    returnByValue: true
  });

  console.log('Desktop Hero State:', evalRes.result.value);

  ws.close();
  chrome.kill();
}

main().catch(console.error);
