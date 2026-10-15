#!/usr/bin/env python3
"""Dựng video giới thiệu khung Hardware Security từ storyboard.json.

Các bước: kiểm tra storyboard -> tách lời đọc/phụ đề -> HTML -> PNG (Playwright)
-> thời lượng (audio thật nếu có, nếu không thì ước tính) -> SRT -> ffmpeg.

Chạy:  python3 build.py            # dựng tất cả
       python3 build.py --no-frames  # dùng lại PNG đã chụp

Audio: đặt audio/canh_XX.mp3 (XX = id cảnh, 2 chữ số) rồi chạy lại.
Cảnh nào thiếu audio sẽ dùng âm thanh im lặng với thời lượng ước tính.
"""
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SLIDES, FRAMES, AUDIO, BUILD = ROOT / "slides", ROOT / "frames", ROOT / "audio", ROOT / "build"
FONT_DIR = SLIDES / "fonts"
FONT_NAME = "Be Vietnam Pro"
W, H, FPS = 1920, 1080, 30
PAUSE = 0.6            # giây nghỉ sau mỗi cảnh
SYL_PER_SEC = 3.6      # tốc độ ước tính khi chưa có audio (âm tiết/giây)
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

MARK = re.compile(r"\[([^\]|]+)\|([^\]]+)\]")


def spoken(t):
    return MARK.sub(lambda m: m.group(2), t)


def shown(t):
    return MARK.sub(lambda m: m.group(1), t)


def esc(t):
    return html.escape(t)


# ---------------------------------------------------------------- HTML
DIR_COLOR = {"of": "var(--of)", "for": "var(--for)", "across": "var(--across)", "ca_ba": "var(--all)"}
CLAIM_CLASS = {"Candidate": "candidate", "Testing": "testing", "Supported": "supported",
               "Rejected": "rejected", "Inconclusive": "inconclusive"}


def r_tieu_de(c):
    sub = "".join(f'<div class="sub">{esc(x)}</div>' for x in c["chu"])
    return f'<h1>{esc(c["tieu_de"])}</h1>{sub}<div class="badge">{esc(c["nhan"])}</div>'


def r_list(c, cls="bul"):
    return f'<ul class="{cls}">' + "".join(f"<li>{esc(x)}</li>" for x in c["chu"]) + "</ul>"


def r_gioi_han(c):
    items = c["chu"]
    out = '<ul class="bul limit"><div class="sep">Giới hạn của bằng chứng</div>'
    out += "".join(f"<li>{esc(x)}</li>" for x in items[:3])
    out += '<div class="sep">Giới hạn của chính tài liệu</div>'
    out += "".join(f'<li class="self">{esc(x)}</li>' for x in items[3:])
    return out + "</ul>"


def r_ba_cot(c):
    cols = "".join(
        f'<div class="card" style="border-top-color:{k["mau"]}"><div class="en" style="color:{k["mau"]}">{esc(k["ten"])}</div>'
        f'<div class="vi">{esc(k["vi"])}</div><div class="q">{esc(k["hoi"])}</div></div>'
        for k in c["hinh"]["cot"])
    return f'<div class="cols3">{cols}</div>'


def r_chuoi_lop(c):
    h = c["hinh"]
    lay = "".join(
        f'<div class="layer{" hl" if code in ("L4", "L5", "L6") else ""}"><span class="code">{code}</span><span class="nm">{esc(nm)}</span></div>'
        for code, nm in h["lop"])
    loops = "".join(f"<div><b>↻</b> {esc(x)}</div>" for x in h["vong"])
    return f'<div class="layers">{lay}</div><div class="loops">{loops}</div><div class="stop">{esc(h["dung"])}</div>'


def ladder(rows):
    return '<div class="ladder">' + "".join(
        f'<div class="step"><span class="code">{a}</span><span class="nm">{esc(b)}</span><span class="ds">{esc(d)}</span></div>'
        for a, b, d in rows) + "</div>"


def r_bac_thang(c):
    return ladder(c["hinh"]["bac"])


def r_bac_thang_ghep(c):
    h = c["hinh"]
    rows = "".join(f"<tr><td>{a}</td><td>{esc(b)}</td></tr>" for a, b in h["ghep"])
    return (f'<div class="twocol">{ladder(h["bac"])}'
            f'<div class="map"><h3>Mức R → mức D thường đi kèm</h3><table>{rows}</table></div></div>')


def r_luoi_nhanh(c):
    legend = ('<div class="legend"><span style="--c:var(--of)">Security of hardware</span>'
              '<span style="--c:var(--for)">Hardware for security</span>'
              '<span style="--c:var(--across)">Across HW/SW</span>'
              '<span style="--c:var(--all)">Cả ba hướng</span></div>')
    cells = "".join(
        f'<div class="br{" hl" if code in ("HS-06", "HS-13") else ""}" style="--c:{DIR_COLOR[d]}"><div class="code">{code}</div><div class="nm">{esc(nm)}</div></div>'
        for code, nm, d in c["hinh"]["nhanh"])
    return legend + f'<div class="grid16">{cells}</div>'


def r_luoi_truc(c):
    h = c["hinh"]
    cells = "".join(f'<div class="ax"><span class="code">{a}</span><span class="nm">{esc(b)}</span></div>' for a, b in h["truc"])
    return f'<div class="grid10">{cells}</div><ul class="bul">' + "".join(f"<li>{esc(x)}</li>" for x in h["ghi"]) + "</ul>"


def r_dong_thoi_gian(c):
    h = c["hinh"]
    phase = ["#2A6F97"] * 2 + ["#0F7B6C"] * 3 + ["#7A3E9D"] * 3 + ["#B5651D"] * 4
    phases = ('<div class="phases"><span style="--c:#2A6F97">Định khung</span><span style="--c:#0F7B6C">Tìm và đọc</span>'
              '<span style="--c:#7A3E9D">Bằng chứng</span><span style="--c:#B5651D">Tổng hợp và dừng</span></div>')
    cells = "".join(
        f'<div class="pt"><div class="ph" style="--c:{phase[i]}"></div><span class="code">{a}</span><span class="nm">{esc(b)}</span></div>'
        for i, (a, b) in enumerate(h["buoc"]))
    return phases + f'<div class="timeline">{cells}</div><div class="note">{esc(h["ghi"])}</div>'


def r_thang_trang_thai(c):
    h = c["hinh"]
    chips = "".join(
        f'<div class="chip {CLAIM_CLASS[en].lower()}" style="background:var(--{CLAIM_CLASS[en]})"><span class="en">{en}</span><span class="vi">{esc(vi)}</span></div>'
        for en, vi in h["claim"])
    rows = "".join(f'<div class="row"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in h["dong"])
    return f'<div class="sub-h">Trạng thái claim (mệnh đề)</div><div class="chips">{chips}</div><div class="rows">{rows}</div>'


def r_hai_cot(c):
    h = c["hinh"]
    f = "".join(f'<div class="fd">{esc(x)}</div>' for x in h["truong"])
    vs = "".join(f'<div class="l">{esc(a)}</div><div class="r">{esc(b)}</div>' for a, b in h["ket"])
    return f'<div class="sub-h">So khớp năm trường của hai kết quả</div><div class="fields">{f}</div><div class="vs">{vs}</div>'


def r_thang_bac(c):
    h = c["hinh"]
    return ladder(h["bac"]) + f'<div class="note" style="margin-top:32px">{esc(h["ghi"])}</div>'


def r_bang_gap(c):
    h = c["hinh"]
    cells = "".join(f'<div class="gp"><span class="en">{esc(a)}</span><span class="vi">{esc(b)}</span></div>' for a, b in h["gap"])
    return f'<div class="grid8">{cells}</div><div class="note">{esc(h["ghi"])}</div>'


def r_the_ket_luan(c):
    h = c["hinh"]
    cells = "".join(f'<div class="dir"><span class="en">{esc(a)}</span><span class="q">{esc(b)}</span></div>' for a, b in h["huong"])
    return (f'<div class="grid4">{cells}</div><div class="next">{esc(h["vong"])}</div>'
            '<div class="small-note">Hướng đề xuất; mức khả thi phụ thuộc tool, dữ liệu, thời gian và cộng tác viên.</div>')


def r_nguon(c):
    cells = "".join(f'<div><span class="code">{a}</span>{esc(b)}</div>' for a, b in c["hinh"]["nguon"])
    return f'<div class="src4">{cells}</div>'


RENDER = {
    "tieu_de": r_tieu_de, "danh_sach": r_list, "danh_sach_gioi_han": r_gioi_han, "ba_cot": r_ba_cot,
    "chuoi_lop": r_chuoi_lop, "bac_thang": r_bac_thang, "bac_thang_ghep": r_bac_thang_ghep,
    "luoi_nhanh": r_luoi_nhanh, "luoi_truc": r_luoi_truc, "dong_thoi_gian": r_dong_thoi_gian,
    "thang_trang_thai": r_thang_trang_thai, "hai_cot_doi_chieu": r_hai_cot, "thang_bac": r_thang_bac,
    "bang_gap": r_bang_gap, "the_ket_luan": r_the_ket_luan, "danh_sach_nguon": r_nguon,
}


def slide_html(c, total):
    is_title = c["kieu_hinh"] == "tieu_de"
    head = "" if is_title else f'<div class="kicker">Cảnh {c["id"]} / {total}</div><h1>{esc(c["tieu_de"])}</h1>'
    gloss = f'<div class="small-note">{esc(c["chu_thich"])}</div>' if c.get("chu_thich") else ""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8">
<link rel="stylesheet" href="style.css"><title>Cảnh {c['id']}</title></head>
<body><div class="slide{' title' if is_title else ''}">{head}<div class="body">{RENDER[c['kieu_hinh']](c)}{gloss}</div>
<div class="footer"><span class="src">Nguồn: tài liệu khung, {esc(c['nguon'])}</span><span>Khung đề xuất · không phải kết quả nghiên cứu</span></div>
</div></body></html>"""


# ---------------------------------------------------------------- kiểm tra
def validate(scenes):
    problems = []
    for c in scenes:
        if len(c["chu"]) > 6:
            problems.append(f"cảnh {c['id']}: {len(c['chu'])} dòng chữ (>6)")
        for line in c["chu"]:
            if len(line) > 60:
                problems.append(f"cảnh {c['id']}: dòng dài {len(line)} ký tự: {line}")
        if c["kieu_hinh"] not in RENDER:
            problems.append(f"cảnh {c['id']}: kiểu hình lạ {c['kieu_hinh']}")
    return problems


# ---------------------------------------------------------------- thời lượng, phụ đề
def probe_duration(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def estimate(text):
    syl = len(re.findall(r"\w+", spoken(text)))
    return syl / SYL_PER_SEC


def sentences(text):
    """Tách câu trên văn bản còn cú pháp [hiển thị|đọc]; tao_giong.py dùng cùng cách tách."""
    return re.split(r"(?<=[.?!])\s+", text.strip())


def wrap_cues(sentence, maxlen=42):
    """Chia một câu (dạng hiển thị) thành khung phụ đề <= 2 dòng x ~42 ký tự."""
    words, lines, cur = sentence.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > maxlen:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return ["\n".join(lines[i:i + 2]) for i in range(0, len(lines), 2)]


def ts(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def sentence_spans(c, speech):
    """Mốc (bắt đầu, kết thúc) của từng câu trong cảnh.

    Có audio/canh_XX.json (do tao_giong.py ghi) thì dùng mốc thật; nếu không thì chia
    thời lượng nói theo số ký tự của từng câu."""
    sents = sentences(c["loi_doc"])
    meta = AUDIO / f"canh_{c['id']:02d}.json"
    if meta.exists() and timing_ok(meta, c):
        return [(s, a, e) for s, (a, e) in zip(sents, json.loads(meta.read_text())["cau"])]
    weights = [len(shown(s)) for s in sents]
    out, t = [], 0.0
    for s, w in zip(sents, weights):
        d = speech * w / sum(weights)
        out.append((s, t, t + d))
        t += d
    return out


def timing_ok(meta, c):
    m = json.loads(meta.read_text())
    return m.get("loi_doc") == c["loi_doc"] and len(m["cau"]) == len(sentences(c["loi_doc"]))


def build_srt(scenes, timing):
    out, n, start = [], 1, 0.0
    for c in scenes:
        for sent, a, e in sentence_spans(c, timing[c["id"]]["speech"]):
            cues = wrap_cues(shown(sent))
            weights = [len(x.replace("\n", " ")) for x in cues]
            t = start + a
            for cue, w in zip(cues, weights):
                d = (e - a) * w / sum(weights)
                out.append(f"{n}\n{ts(t)} --> {ts(t + d - 0.05)}\n{cue}\n")
                n += 1
                t += d
        start += timing[c["id"]]["dur"]
    return "\n".join(out)


# ---------------------------------------------------------------- ffmpeg
def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def render_scene(c, t, out):
    dur = t["dur"]
    frames = int(round(dur * FPS))
    png = FRAMES / f"canh_{c['id']:02d}.png"
    vf = (f"scale={W*2}:{H*2},zoompan=z='1+0.03*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={frames}:s={W}x{H}:fps={FPS},fade=t=in:st=0:d=0.3,fade=t=out:st={dur-0.3:.3f}:d=0.3,format=yuv420p")
    if t["audio"]:
        ain = ["-i", str(t["audio"])]
        af = f"apad=whole_dur={dur:.3f},afade=t=in:st=0:d=0.3,afade=t=out:st={dur-0.3:.3f}:d=0.3"
    else:
        ain = ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        af = "anull"
    run(["ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-i", str(png), *ain,
         "-filter_complex", f"[0:v]{vf}[v];[1:a]{af},aresample=48000,aformat=channel_layouts=stereo[a]",
         "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-tune", "stillimage", "-c:a", "aac", "-b:a", "160k", str(out)])


def write_kich_ban(sb, timing):
    L = [f"# Kịch bản: {sb['tieu_de_video']}", "",
         f"Nguồn: {sb['nguon_chinh']}.", "",
         "## Giả định",
         "- Báo cáo kết quả (`07_synthesis/bao_cao_ket_qua.md`) chưa có, nên video giới thiệu **tài liệu khung**, "
         "không trình bày kết quả nghiên cứu. Mọi cảnh có nhãn \"Khung đề xuất · không phải kết quả nghiên cứu\".",
         "- Giọng đọc: Piper `vi_VN-vais1000-medium` (giọng nữ tổng hợp, CC BY 4.0) chạy offline qua sherpa-onnx, "
         "tạo bằng `tao_giong.py`. Cảnh nào thiếu audio thì dùng thời lượng ước tính (số âm tiết / "
         f"{SYL_PER_SEC}) và âm thanh im lặng. Mỗi cảnh = thời lượng audio + {PAUSE} giây nghỉ.",
         "- Cấu trúc 16 cảnh được điều chỉnh từ mẫu `kieu=day-du` cho nội dung khung; mục tiêu 5 phút.", ""]
    total = 0
    for c in sb["canh"]:
        t = timing[c["id"]]
        total += t["dur"]
        L += [f"## Cảnh {c['id']}: {c['tieu_de']}", "",
              f"- Kiểu hình: `{c['kieu_hinh']}` · Nguồn: {c['nguon']} · Thời lượng: {t['dur']:.1f} s "
              f"({'audio thật' if t['audio'] else 'ước tính'})"]
        if c["chu"]:
            L += ["- Chữ trên màn hình:"] + [f"  - {x}" for x in c["chu"]]
        if c.get("chu_thich"):
            L += [f"- Chú thích thuật ngữ: {c['chu_thich']}"]
        L += ["", "**Lời đọc (phụ đề):**", "", shown(c["loi_doc"]), "",
              "**Văn bản đưa vào TTS:**", "", spoken(c["loi_doc"]), ""]
    L += [f"**Tổng thời lượng:** {total:.1f} s ({total/60:.2f} phút)", ""]
    (ROOT / "kich_ban.md").write_text("\n".join(L), encoding="utf-8")


def contact_sheet(scenes, timing):
    """Trích khung giữa mỗi cảnh từ video có phụ đề, ghép thành kiem_tra_khung.png."""
    tmp = BUILD / "tmp"
    tmp.mkdir(exist_ok=True)
    start = 0.0
    for c in scenes:
        mid = start + timing[c["id"]]["dur"] / 2
        run(["ffmpeg", "-y", "-ss", f"{mid:.2f}", "-i", str(ROOT / "video_ket_qua_phude.mp4"),
             "-frames:v", "1", "-vf", "scale=640:360", str(tmp / f"k_{c['id']:02d}.png")])
        start += timing[c["id"]]["dur"]
    run(["ffmpeg", "-y", "-pattern_type", "glob", "-i", str(tmp / "k_*.png"),
         "-vf", "tile=4x4:padding=8:color=white", "-frames:v", "1", str(ROOT / "kiem_tra_khung.png")])


def main():
    sb = json.loads((ROOT / "storyboard.json").read_text(encoding="utf-8"))
    scenes = sb["canh"]
    problems = validate(scenes)
    if problems:
        sys.exit("Storyboard chưa hợp lệ:\n  " + "\n  ".join(problems))

    for d in (FRAMES, AUDIO, BUILD):
        d.mkdir(exist_ok=True)

    # Văn bản cho TTS, mỗi cảnh một file
    for c in scenes:
        (AUDIO / f"canh_{c['id']:02d}.txt").write_text(spoken(c["loi_doc"]) + "\n", encoding="utf-8")

    # HTML + PNG
    for c in scenes:
        (SLIDES / f"canh_{c['id']:02d}.html").write_text(slide_html(c, len(scenes)), encoding="utf-8")
    if "--no-frames" not in sys.argv:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=CHROMIUM if Path(CHROMIUM).exists() else None)
            pg = b.new_page(viewport={"width": W, "height": H})
            for c in scenes:
                pg.goto((SLIDES / f"canh_{c['id']:02d}.html").as_uri())
                pg.evaluate("document.fonts.ready")
                over = pg.evaluate("""() => [...document.querySelectorAll('.slide *')].filter(e => {
                    const r = e.getBoundingClientRect(); const inBody = e.closest('.body');
                    return r.right > 1824 || (inBody && r.bottom > 852) || e.scrollWidth > e.clientWidth + 2;
                }).map(e => e.className || e.tagName).slice(0, 5)""")
                if over:
                    print(f"  ! cảnh {c['id']}: phần tử có thể tràn: {over}")
                pg.screenshot(path=str(FRAMES / f"canh_{c['id']:02d}.png"))
            b.close()

    # Thời lượng
    timing = {}
    for c in scenes:
        mp3 = AUDIO / f"canh_{c['id']:02d}.mp3"
        if mp3.exists() and mp3.stat().st_size > 0:
            speech, src = probe_duration(mp3), mp3
        else:
            speech, src = estimate(c["loi_doc"]), None
        timing[c["id"]] = {"speech": speech, "dur": round(speech + PAUSE, 3), "audio": src}
    has_audio = all(t["audio"] for t in timing.values())
    any_audio = any(t["audio"] for t in timing.values())

    (ROOT / "phu_de.srt").write_text(build_srt(scenes, timing), encoding="utf-8")
    (BUILD / "thoi_luong.json").write_text(json.dumps(
        {c["id"]: {"dur": timing[c["id"]]["dur"], "audio_that": bool(timing[c["id"]]["audio"])} for c in scenes},
        ensure_ascii=False, indent=1), encoding="utf-8")

    # Từng cảnh
    parts = []
    for c in scenes:
        out = BUILD / f"canh_{c['id']:02d}.mp4"
        render_scene(c, timing[c["id"]], out)
        parts.append(out)
        print(f"  cảnh {c['id']:2d}: {timing[c['id']]['dur']:6.2f}s {'audio' if timing[c['id']]['audio'] else 'im lặng (ước tính)'}")
    (BUILD / "concat.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
    joined = BUILD / "ghep.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(BUILD / "concat.txt"), "-c", "copy", str(joined)])

    # Chuẩn hóa âm lượng khi có audio thật
    a_args = ["-c:a", "copy"]
    if any_audio:
        a_args = ["-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-ar", "48000"]

    srt = ROOT / "phu_de.srt"
    run(["ffmpeg", "-y", "-i", str(joined), "-i", str(srt), "-map", "0:v", "-map", "0:a", "-map", "1:s",
         "-c:v", "copy", *a_args, "-c:s", "mov_text", "-metadata:s:s:0", "language=vie",
         "-metadata:s:a:0", "language=vie", "-movflags", "+faststart", str(ROOT / "video_ket_qua.mp4")])

    style = (f"FontName={FONT_NAME},FontSize=13,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,"
             "BorderStyle=3,Outline=1,Shadow=0,MarginV=26,Alignment=2")
    srt_esc = str(srt).replace(":", r"\:")
    run(["ffmpeg", "-y", "-i", str(joined), "-vf",
         f"subtitles='{srt_esc}':fontsdir='{FONT_DIR}':force_style='{style}'",
         "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-tune", "stillimage", *a_args, "-movflags", "+faststart",
         str(ROOT / "video_ket_qua_phude.mp4")])

    write_kich_ban(sb, timing)
    contact_sheet(scenes, timing)
    total = sum(t["dur"] for t in timing.values())
    print(f"Tổng thời lượng: {total:.1f}s ({total/60:.2f} phút). Audio thật: "
          f"{'đủ' if has_audio else ('một phần' if any_audio else 'chưa có')}")
    shutil.rmtree(BUILD / "tmp", ignore_errors=True)


if __name__ == "__main__":
    main()
