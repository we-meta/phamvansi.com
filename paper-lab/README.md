# Paper Lab — motion graphics

22 s, 1080×1350, 30 fps. `scene.html` vẽ toàn bộ bằng Canvas; mọi chuyển động là hàm của thời gian `t`
(`window.renderFrame(t)`), nên mỗi khung render ra đều giống hệt nhau.

- Xem trước: mở `scene.html` qua một web server tĩnh (ví dụ `npx serve paper-lab`).
- Chụp vài khung: `node paper-lab/render.js --stills 1,6,12,20` → `out/stills/`.
- Xuất video: `node paper-lab/render.js` → `out/video.mp4` (Playwright + FFmpeg).
  Nếu có `audio/music.mp3`, file sẽ được ghép làm nhạc nền (fade in/out, cắt đúng 22 s).

- Nhạc nền: `python3 paper-lab/make_music.py` tổng hợp `audio/music.mp3` (chỉ cần numpy), khớp các mốc READ 0,6 s · EXTRACT 5,4 s · BUILD 9,6 s · VALIDATE 14,2 s · PACKAGE 18,6 s · COMPLETE 21 s.

Font: JetBrains Mono (SIL OFL, xem `fonts/OFL.txt`).
