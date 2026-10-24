const fs = require('fs');
const path = require('path');
const https = require('https');

const videoUrls = [
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-home-j6akyxwebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-home-r0h6pbmp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-about-us-hlhktpwebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-about-us-atkt4mmp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-work-taxdiywebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-work-kcov6omp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-sevices-x9s6p3webm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-services-lm58hmmp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-blog-vmoxlpwebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-blog-myb1jmmp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-careers-mw0dswwebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-career-ts7lmomp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-show-reel-mc61tcwebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-showreel-iqatg3mp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-year-in-review-l1twkcwebm-t0wMA.webm',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-year-in-review-z8obp1mp4-t0wMA.mp4',
  'https://mdn.check-dc.com/BASE/Checkwebsite/video-check-launch-lmhh5hmp4-t0wMA.mp4'
];

const destDir = path.join(__dirname, 'site', 'assets', 'mdn');
if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

function fetchFile(url) {
  const filename = path.basename(url);
  const destPath = path.join(destDir, filename);
  if (fs.existsSync(destPath) && fs.statSync(destPath).size > 0) {
    console.log(`[Cache] ${filename}`);
    return Promise.resolve();
  }

  return new Promise((resolve) => {
    console.log(`[Downloading] ${filename}`);
    const file = fs.createWriteStream(destPath);
    const req = https.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
      }
    }, (res) => {
      if (res.statusCode !== 200) {
        console.error(`Status ${res.statusCode} for ${filename}`);
        file.close();
        fs.unlink(destPath, () => {});
        return resolve();
      }
      res.pipe(file);
      file.on('finish', () => {
        file.close();
        console.log(`[Finished] ${filename}`);
        resolve();
      });
    });

    req.on('error', (err) => {
      console.error(`Error ${filename}: ${err.message}`);
      file.close();
      fs.unlink(destPath, () => {});
      resolve();
    });

    req.setTimeout(45000, () => {
      req.destroy();
      resolve();
    });
  });
}

async function run() {
  for (const url of videoUrls) {
    await fetchFile(url);
  }
  console.log('All menu videos downloaded!');
}

run();
