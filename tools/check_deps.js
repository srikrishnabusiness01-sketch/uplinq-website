const fs = require('fs');
const path = require('path');

const deps = [
  "Bng0Y5Qc.js",
  "pK72Md3I.js",
  "CUHQ75Kx.js",
  "useText.LSRUOlx9.css",
  "GWfF2dPz.js",
  "about.DBtAqrtP.css",
  "CSa3K16w.js",
  "CB5bwoBe.js",
  "BRNoKpZr.js",
  "CTv0N32m.js",
  "DvDH6DOc.js",
  "B16is_2b.js",
  "careers.BH39NcD2.css",
  "BUNzQeiZ.js",
  "Dw6j1lKB.js",
  "ContentLoader.CEL3A0Ie.css",
  "C88u2vV_.js",
  "swiper.BkhtZMPQ.css",
  "_slug_.CvRIJPsF.css",
  "DSgCRULr.js",
  "C6wqUHeU.js",
  "contact.4hqApv5O.css",
  "BMQH0uFj.js",
  "DfGQTBJ8.js",
  "useWorkItems.C3Iyg7EB.css",
  "D89ZAvpF.js",
  "index.CL5g6JNe.css",
  "DY_CZq6x.js",
  "services.C32MMqyw.css",
  "Dl_6lvg3.js",
  "C_DdlpMG.js",
  "Bq5zHFFt.js",
  "_slug_.CYrd78P_.css",
  "C7RDNTEG.js",
  "index.Dbun9GLX.css",
  "C41ihraj.js",
  "_slug_.cRKi73VL.css",
  "DNL1_x1j.js",
  "CKnKRuIZ.js",
  "CIWXCq25.js",
  "B0CwXBEy.js",
  "default.-CLknPkJ.css"
];

const dir = path.join(__dirname, '..', 'site', '_nuxt');
const missing = deps.filter(f => !fs.existsSync(path.join(dir, f)));
console.log('Checked', deps.length, 'deps.');
console.log('Missing deps count:', missing.length);
if (missing.length) console.log('Missing:', missing);
else console.log('ALL DEPS EXIST!');
