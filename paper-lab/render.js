#!/usr/bin/env node
// Renders scene.html frame by frame with Playwright and encodes with FFmpeg.
//   node paper-lab/render.js                    -> out/video.mp4
//   node paper-lab/render.js --stills 1,6,12,20 -> out/stills/*.png
"use strict";
const http = require("http");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

function loadPlaywright() {
  try { return require("playwright"); } catch (_) { }
  const { execSync } = require("child_process");
  const root = execSync("npm root -g").toString().trim();
  return require(path.join(root, "playwright"));
}
const { chromium } = loadPlaywright();

const ROOT = path.resolve(__dirname, "..");
const SCENE_DIR = __dirname;
const args = process.argv.slice(2);
const arg = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const OUT = path.resolve(ROOT, arg("--out", "out/video.mp4"));
const AUDIO = path.resolve(ROOT, arg("--audio", "audio/music.mp3"));
const WORKERS = Number(arg("--workers", Math.max(2, require("os").cpus().length)));
const STILLS = arg("--stills", null);

const MIME = { ".html": "text/html", ".js": "text/javascript", ".woff2": "font/woff2" };
function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rsp) => {
      const p = path.join(SCENE_DIR, decodeURIComponent(req.url.split("?")[0]));
      if (!p.startsWith(SCENE_DIR) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { rsp.writeHead(404); return rsp.end(); }
      rsp.writeHead(200, { "Content-Type": MIME[path.extname(p)] || "application/octet-stream" });
      fs.createReadStream(p).pipe(rsp);
    }).listen(0, "127.0.0.1", () => res(srv));
  });
}

async function openPage(browser, url, W, H) {
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  page.on("pageerror", e => console.error("pageerror:", e.message));
  await page.goto(url);
  await page.evaluate(() => window.ready);
  return page;
}
const grab = (page, t, W, H) => page.evaluate(t => window.renderFrame(t), t)
  .then(() => page.screenshot({ type: "png", clip: { x: 0, y: 0, width: W, height: H } }));

(async () => {
  const srv = await serve();
  const url = `http://127.0.0.1:${srv.address().port}/scene.html?render=1`;
  const browser = await chromium.launch({ args: ["--force-color-profile=srgb", "--font-render-hinting=none"] });
  const probe = await openPage(browser, url, 1080, 1350);
  const { W, H, FPS, DUR } = await probe.evaluate(() => window.SCENE);

  if (STILLS) {
    const dir = path.join(path.dirname(OUT), "stills");
    fs.mkdirSync(dir, { recursive: true });
    for (const s of STILLS.split(",").map(Number)) {
      const f = path.join(dir, `t${s.toFixed(2).padStart(5, "0")}.png`);
      fs.writeFileSync(f, await grab(probe, s, W, H));
      console.log("still", f);
    }
    await browser.close(); srv.close(); return;
  }

  const total = Math.round(DUR * FPS);
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  const hasAudio = fs.existsSync(AUDIO);
  const ff = ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "png", "-i", "-"];
  if (hasAudio) ff.push("-i", AUDIO);
  ff.push("-map", "0:v", "-c:v", "libx264", "-preset", "slow", "-crf", "15", "-pix_fmt", "yuv420p",
    "-profile:v", "high", "-tune", "film", "-r", String(FPS), "-movflags", "+faststart");
  if (hasAudio) ff.push("-map", "1:a", "-c:a", "aac", "-b:a", "192k",
    "-af", `apad,afade=t=in:st=0:d=0.5,afade=t=out:st=${DUR - 1.5}:d=1.5`);
  ff.push("-t", String(DUR), OUT);
  console.log(hasAudio ? `audio: ${AUDIO}` : "audio: none (audio/music.mp3 not found)");
  const enc = spawn("ffmpeg", ff, { stdio: ["pipe", "inherit", "inherit"] });
  const encDone = new Promise((res, rej) => enc.on("close", c => c === 0 ? res() : rej(new Error("ffmpeg exit " + c))));

  const pages = [probe];
  for (let i = 1; i < WORKERS; i++) pages.push(await openPage(browser, url, W, H));
  const ready = new Map();
  let next = 0, written = 0;
  const started = Date.now();
  const write = buf => new Promise(res => enc.stdin.write(buf) ? res() : enc.stdin.once("drain", res));
  let flushing = Promise.resolve();
  const flush = () => (flushing = flushing.then(async () => {
    while (ready.has(written)) {
      const b = ready.get(written); ready.delete(written);
      await write(b); written++;
      if (written % 30 === 0) console.log(`frame ${written}/${total}  ${((Date.now() - started) / 1000).toFixed(0)}s`);
    }
  }));
  await Promise.all(pages.map(async page => {
    while (next < total) {
      const i = next++;
      ready.set(i, await grab(page, i / FPS, W, H));
      flush();
      while (ready.size > WORKERS * 4) await flushing;
    }
  }));
  await flush();
  enc.stdin.end();
  await encDone;
  await browser.close(); srv.close();
  console.log(`wrote ${OUT} (${total} frames) in ${((Date.now() - started) / 1000).toFixed(0)}s`);
})().catch(e => { console.error(e); process.exit(1); });
