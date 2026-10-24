const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9222;

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

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
  console.log('Launching Headless Chrome...');
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
      if (targets && targets.length > 0) {
        connected = true;
        break;
      }
    } catch (e) {}
  }

  if (!connected) {
    console.error('Could not connect to Chrome CDP on port ' + PORT);
    chrome.kill();
    process.exit(1);
  }

  const pageTarget = targets.find(t => t.type === 'page') || targets[0];
  console.log('Connecting to Page target WS:', pageTarget.webSocketDebuggerUrl);

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

  const consoleLogs = [];
  const networkErrors = [];
  const exceptions = [];

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && pending.has(data.id)) {
      const p = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) p.reject(data.error);
      else p.resolve(data.result);
      return;
    }

    if (data.method === 'Runtime.consoleAPICalled') {
      const args = data.params.args.map(a => a.value || a.description || JSON.stringify(a)).join(' ');
      consoleLogs.push(`[${data.params.type}] ${args}`);
    } else if (data.method === 'Runtime.exceptionThrown') {
      const desc = data.params.exceptionDetails.exception?.description || data.params.exceptionDetails.text;
      exceptions.push(desc);
    } else if (data.method === 'Network.loadingFailed') {
      networkErrors.push(`${data.params.errorText}: ${data.params.type} (requestId: ${data.params.requestId})`);
    } else if (data.method === 'Network.responseReceived') {
      const status = data.params.response.status;
      if (status >= 400) {
        networkErrors.push(`HTTP ${status} on ${data.params.response.url}`);
      }
    }
  };

  await new Promise((resolve) => ws.onopen = resolve);
  console.log('WebSocket connected. Enabling domains...');

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Network.enable');

  console.log('Navigating to http://localhost:3000/ ...');
  await send('Page.navigate', { url: 'http://localhost:3000/' });

  console.log('Waiting 8 seconds for page load and loader exit animation...');
  await sleep(8000);

  // Capture screenshot 1: Top frame
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(__dirname, 'frame_top.png'), Buffer.from(shot1.data, 'base64'));
  console.log('Saved frame_top.png');

  // Scroll down 800px
  await send('Runtime.evaluate', { expression: 'window.scrollBy(0, 800);' });
  await sleep(1000);
  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(__dirname, 'frame_scroll_1.png'), Buffer.from(shot2.data, 'base64'));
  console.log('Saved frame_scroll_1.png');

  // Scroll down another 1200px
  await send('Runtime.evaluate', { expression: 'window.scrollBy(0, 1200);' });
  await sleep(1000);
  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(__dirname, 'frame_scroll_2.png'), Buffer.from(shot3.data, 'base64'));
  console.log('Saved frame_scroll_2.png');

  // Check document title, innerText sample, loader visibility
  const evalResult = await send('Runtime.evaluate', {
    expression: `JSON.stringify({
      title: document.title,
      loaderDisplay: window.getComputedStyle(document.querySelector('.c-loader') || document.body).display,
      loaderOpacity: window.getComputedStyle(document.querySelector('.c-loader') || document.body).opacity,
      mainWrapperDisplay: window.getComputedStyle(document.querySelector('.main-wrapper') || document.body).display,
      bodyTextSnippet: document.body.innerText.substring(0, 500)
    })`
  });

  console.log('\n=== DOM STATE ===');
  console.log(evalResult.result.value);

  console.log('\n=== RUNTIME EXCEPTIONS (' + exceptions.length + ') ===');
  exceptions.forEach(e => console.log('EXCEPTION:', e));

  console.log('\n=== NETWORK ERRORS (' + networkErrors.length + ') ===');
  networkErrors.forEach(n => console.log('NETWORK:', n));

  console.log('\n=== CONSOLE LOGS (' + consoleLogs.length + ') ===');
  consoleLogs.forEach(c => console.log('CONSOLE:', c));

  ws.close();
  chrome.kill();
  console.log('\nDone diagnosis!');
}

main().catch(err => {
  console.error('Fatal CDP error:', err);
  process.exit(1);
});
