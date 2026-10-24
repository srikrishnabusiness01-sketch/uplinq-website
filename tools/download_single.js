const fs = require('fs');
const path = require('path');
const https = require('https');

const url = 'https://mdn.check-dc.com/t0wMA/01jpje9v8msdwfydsa5s4h635q/video-quidax-brand-announcement-video-minmp4-t0wMA.mp4';
const dest = path.join(__dirname, 'site', 'assets', 'mdn', 'video-quidax-brand-announcement-video-minmp4-t0wMA.mp4');

function download(attempt = 1) {
  console.log(`Downloading (attempt ${attempt})...`);
  const file = fs.createWriteStream(dest);
  const req = https.get(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
  }, (res) => {
    if (res.statusCode !== 200) {
      console.error('Status:', res.statusCode);
      return;
    }
    res.pipe(file);
    file.on('finish', () => {
      file.close();
      const stats = fs.statSync(dest);
      console.log(`Success! File size: ${(stats.size / (1024*1024)).toFixed(2)} MB`);
    });
  });

  req.on('error', (err) => {
    fs.unlink(dest, () => {});
    console.error('Download error:', err.message);
    if (attempt < 5) {
      setTimeout(() => download(attempt + 1), 2000);
    }
  });

  req.setTimeout(60000, () => {
    req.destroy(new Error('Timeout'));
  });
}

download();
