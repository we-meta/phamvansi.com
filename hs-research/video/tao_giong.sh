#!/usr/bin/env bash
# Phương án thay thế: tạo giọng bằng edge-tts (cần mạng tới speech.platform.bing.com). Mặc định dùng tao_giong.py (offline).
# Cần mạng tới speech.platform.bing.com. Đổi giọng: GIONG=vi-VN-NamMinhNeural ./tao_giong.sh
set -euo pipefail
cd "$(dirname "$0")"
GIONG="${GIONG:-vi-VN-HoaiMyNeural}"   # giọng nữ; giọng nam: vi-VN-NamMinhNeural
TOC_DO="${TOC_DO:-+0%}"
python3 -m pip show edge-tts >/dev/null 2>&1 || python3 -m pip install -q edge-tts
for f in audio/canh_*.txt; do
  out="${f%.txt}.mp3"
  echo "-> $out"
  edge-tts --voice "$GIONG" --rate "$TOC_DO" --file "$f" --write-media "$out"
done
python3 build.py --no-frames
