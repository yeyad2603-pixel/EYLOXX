/**
 * EYLOX — Static File Server
 * Run:  node serve.js
 * Then open: http://localhost:3000
 *
 * No npm install needed — uses Node.js built-in modules only.
 */

'use strict';

const http = require('http');
const fs   = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT       = 3000;
const ROOT_DIR   = path.join(__dirname, 'Eylox WEB html');   // primary: HTML/CSS/JS files
const ASSETS_DIR = path.join(__dirname);                      // fallback: root assets (MUSIC, images…)

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css':  'text/css',
  '.js':   'application/javascript',
  '.json': 'application/json',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif':  'image/gif',
  '.svg':  'image/svg+xml',
  '.ico':  'image/x-icon',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2':'font/woff2',
  '.ttf':  'font/ttf',
  '.mp3':  'audio/mpeg',
  '.mp4':  'audio/mp4',   // all mp4 on this server are audio-only background tracks
  '.m4a':  'audio/mp4',
  '.wav':  'audio/wav',
  '.ogg':  'audio/ogg',
};

const server = http.createServer((req, res) => {
  /* Strip query string */
  let urlPath = req.url.split('?')[0].split('#')[0];

  /* Root → landing page */
  if (urlPath === '/' || urlPath === '') {
    res.writeHead(302, { Location: '/landing.html' });
    res.end();
    return;
  }

  /* Decode URI */
  try { urlPath = decodeURIComponent(urlPath); } catch {}

  /* Map to file */
  const filePath = path.join(ROOT_DIR, urlPath);

  /* Security: block directory traversal outside allowed roots */
  const assetPath = path.join(ASSETS_DIR, urlPath);
  if (!filePath.startsWith(ROOT_DIR) && !assetPath.startsWith(ASSETS_DIR)) {
    res.writeHead(403); res.end('Forbidden');
    return;
  }

  fs.stat(filePath, (err, stat) => {
    if (!err && stat.isFile()) { serve(filePath, res, req); return; }

    /* Try appending .html */
    const withHtml = filePath + '.html';
    fs.stat(withHtml, (err2, stat2) => {
      if (!err2 && stat2.isFile()) { serve(withHtml, res, req); return; }

      /* Fallback: look in root EYLOX directory (covers MUSIC/, images at root, etc.) */
      fs.stat(assetPath, (err3, stat3) => {
        if (!err3 && stat3.isFile()) { serve(assetPath, res, req); return; }
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 — File not found: ' + urlPath);
      });
    });
  });
});

function serve(filePath, res, req) {
  const ext      = path.extname(filePath).toLowerCase();
  const mime     = MIME[ext] || 'application/octet-stream';
  const isAudio  = mime.startsWith('audio/');

  fs.stat(filePath, (err, stat) => {
    if (err) { res.writeHead(500); res.end('Server error'); return; }

    const total     = stat.size;
    const rangeHdr  = req && req.headers && req.headers['range'];

    /* ── Range request (needed for audio seek / progressive loading) ── */
    if (isAudio && rangeHdr) {
      const [startStr, endStr] = rangeHdr.replace(/bytes=/, '').split('-');
      const start = parseInt(startStr, 10);
      const end   = endStr ? parseInt(endStr, 10) : total - 1;
      const chunk = end - start + 1;

      res.writeHead(206, {
        'Content-Range':  `bytes ${start}-${end}/${total}`,
        'Accept-Ranges':  'bytes',
        'Content-Length': chunk,
        'Content-Type':   mime,
        'Cache-Control':  'no-cache',
        'Access-Control-Allow-Origin': '*',
      });
      fs.createReadStream(filePath, { start, end })
        .on('error', () => res.end())
        .pipe(res);
      return;
    }

    /* ── Full file ── */
    const headers = {
      'Content-Type':   mime,
      'Content-Length': total,
      'Cache-Control':  'no-cache',
      'Access-Control-Allow-Origin': '*',
    };
    if (isAudio) headers['Accept-Ranges'] = 'bytes';

    const stream = fs.createReadStream(filePath);
    stream.on('error', () => { res.writeHead(500); res.end('Server error'); });
    res.writeHead(200, headers);
    stream.pipe(res);
  });
}

server.listen(PORT, '127.0.0.1', () => {
  const url = `http://localhost:${PORT}`;

  console.log('');
  console.log('  ╔═══════════════════════════════════╗');
  console.log('  ║  🎮  EYLOX  —  Local Server       ║');
  console.log('  ╠═══════════════════════════════════╣');
  console.log(`  ║  ✅  Running at  ${url}   ║`);
  console.log('  ║  🌐  Opening browser now…         ║');
  console.log('  ║  🛑  Press Ctrl+C to stop         ║');
  console.log('  ╚═══════════════════════════════════╝');
  console.log('');

  /* Auto-open in default browser */
  const open = process.platform === 'win32'  ? `start "" "${url}"`
             : process.platform === 'darwin' ? `open "${url}"`
             : `xdg-open "${url}"`;
  exec(open, err => { if (err) console.log(`  Open manually: ${url}`); });
});

server.on('error', err => {
  if (err.code === 'EADDRINUSE') {
    console.error(`\n  ❌  Port ${PORT} is already in use.`);
    console.error(`  Try: http://localhost:${PORT}  — it may already be running.\n`);
  } else {
    console.error('\n  ❌  Server error:', err.message, '\n');
  }
  process.exit(1);
});