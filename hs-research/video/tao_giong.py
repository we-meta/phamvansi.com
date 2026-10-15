#!/usr/bin/env python3
"""Tạo giọng đọc offline cho từng cảnh bằng Piper (qua sherpa-onnx), rồi dựng lại video.

Mỗi câu được tổng hợp riêng rồi ghép lại, nên biết chính xác câu nào bắt đầu và
kết thúc lúc nào. Mốc này ghi vào audio/canh_XX.json để build.py căn phụ đề.

Chạy:  python3 tao_giong.py               # giọng mặc định, tốc độ 1.0
       python3 tao_giong.py --toc-do 1.1  # đọc nhanh hơn 10%
       python3 tao_giong.py --khong-dung  # chỉ tạo audio, không dựng lại video

Cần: pip install sherpa-onnx soundfile numpy. Model tải từ GitHub Releases của sherpa-onnx.
"""
import argparse
import json
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from build import AUDIO, sentences, spoken  # noqa: E402

GIONG = "vi_VN-vais1000-medium"     # giọng nữ, một người đọc, giấy phép CC BY 4.0
MODEL_URL = f"https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-{GIONG}.tar.bz2"
MODEL_DIR = ROOT / "tts_model" / f"vits-piper-{GIONG}"
LEAD = 0.15        # giây im lặng đầu cảnh
GAP = 0.30         # giây nghỉ giữa hai câu


def ensure_model():
    if (MODEL_DIR / f"{GIONG}.onnx").exists():
        return
    MODEL_DIR.parent.mkdir(exist_ok=True)
    archive = MODEL_DIR.parent / f"{GIONG}.tar.bz2"
    print(f"Tải model {GIONG} ...")
    urllib.request.urlretrieve(MODEL_URL, archive)
    with tarfile.open(archive) as t:
        t.extractall(MODEL_DIR.parent, filter="data")
    archive.unlink()


def load_tts():
    import sherpa_onnx
    vits = sherpa_onnx.OfflineTtsVitsModelConfig(
        model=str(MODEL_DIR / f"{GIONG}.onnx"), tokens=str(MODEL_DIR / "tokens.txt"),
        data_dir=str(MODEL_DIR / "espeak-ng-data"))
    cfg = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(vits=vits, num_threads=4))
    return sherpa_onnx.OfflineTts(cfg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--toc-do", type=float, default=1.0, help="hệ số tốc độ đọc (1.0 = mặc định)")
    ap.add_argument("--khong-dung", action="store_true", help="không chạy build.py sau khi tạo audio")
    args = ap.parse_args()

    ensure_model()
    tts = load_tts()
    AUDIO.mkdir(exist_ok=True)
    scenes = json.loads((ROOT / "storyboard.json").read_text(encoding="utf-8"))["canh"]

    for c in scenes:
        parts, spans, t, sr = [], [], LEAD, None
        for sent in sentences(c["loi_doc"]):
            a = tts.generate(spoken(sent), sid=0, speed=args.toc_do)
            sr = a.sample_rate
            x = np.asarray(a.samples, dtype=np.float32)
            spans.append([round(t, 3), round(t + len(x) / sr, 3)])
            parts += [x, np.zeros(int(GAP * sr), dtype=np.float32)]
            t += len(x) / sr + GAP
        audio = np.concatenate([np.zeros(int(LEAD * sr), dtype=np.float32), *parts[:-1]])
        wav = AUDIO / f"canh_{c['id']:02d}.wav"
        sf.write(wav, audio, sr)
        mp3 = wav.with_suffix(".mp3")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "128k", str(mp3)],
                       check=True)
        wav.unlink()
        (AUDIO / f"canh_{c['id']:02d}.json").write_text(json.dumps(
            {"giong": GIONG, "toc_do": args.toc_do, "loi_doc": c["loi_doc"], "cau": spans},
            ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  cảnh {c['id']:2d}: {len(audio) / sr:5.1f}s, {len(spans)} câu")

    if not args.khong_dung:
        subprocess.run([sys.executable, str(ROOT / "build.py"), "--no-frames"], check=True)


if __name__ == "__main__":
    main()
