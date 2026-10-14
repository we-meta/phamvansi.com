#!/usr/bin/env python3
"""Synthesize the 22 s soundtrack for the Paper Lab video (numpy only).

Cues follow the scene timeline in scene.html:
  READ 0.6 · EXTRACT 5.4 · BUILD 9.6 · VALIDATE 14.2 · PACKAGE 18.6 · COMPLETE 21.0
Output: audio/music.mp3 (and audio/music.wav) at the repo root.
"""
import os
import subprocess
import numpy as np

SR = 48000
DUR = 22.0
N = int(SR * DUR)
T = np.arange(N) / SR
rng = np.random.default_rng(20261014)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BPM = 120
BEAT = 60 / BPM
STAGES = [0.6, 5.4, 9.6, 14.2, 18.6, 21.0]


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def env_adsr(n, a, d, s, r, sr=SR):
    a, d, r = int(a * sr), int(d * sr), int(r * sr)
    sus = max(0, n - a - d - r)
    e = np.concatenate([
        np.linspace(0, 1, max(a, 1), endpoint=False),
        np.linspace(1, s, max(d, 1), endpoint=False),
        np.full(sus, s),
        np.linspace(s, 0, max(r, 1)),
    ])
    return e[:n] if len(e) >= n else np.pad(e, (0, n - len(e)))


def fft_filter(x, lo=None, hi=None):
    """Brick-ish band filter with soft edges, done in the frequency domain."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.ones_like(f)
    if hi is not None:
        g *= 1 / (1 + (f / hi) ** 4)
    if lo is not None:
        g *= 1 / (1 + (lo / np.maximum(f, 1e-3)) ** 4)
    return np.fft.irfft(X * g, len(x))


def add(buf, sig, t0, pan=0.0, gain=1.0):
    i0 = int(t0 * SR)
    if i0 >= N:
        return
    sig = sig[: N - i0]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[0, i0:i0 + len(sig)] += sig * gain * l
    buf[1, i0:i0 + len(sig)] += sig * gain * r


mix = np.zeros((2, N))

# ---------------- pad: one chord per stage ----------------
CHORDS = [  # D minor journey: Dm  Bbmaj7  F  C  Dm(add9)
    (0.0, [50, 57, 62, 65, 69]),
    (5.4, [46, 53, 57, 62, 69]),
    (9.6, [41, 53, 57, 60, 65]),
    (14.2, [48, 55, 60, 64, 67]),
    (18.6, [50, 57, 62, 64, 65, 69]),
]
for k, (t0, notes) in enumerate(CHORDS):
    t1 = CHORDS[k + 1][0] if k + 1 < len(CHORDS) else DUR
    n = int((t1 - t0 + 1.6) * SR)
    tt = np.arange(n) / SR
    e = env_adsr(n, 1.2 if k == 0 else 0.6, 0.5, 0.85, 1.6)
    for j, m in enumerate(notes):
        for det, pan in ((-0.07, -0.6), (0.07, 0.6)):
            f = midi(m + det)
            # soft saw: few decaying harmonics, slow tremolo
            s = sum(np.sin(2 * np.pi * f * h * tt + rng.uniform(0, 6)) / h ** 1.6 for h in range(1, 6))
            s *= 1 + 0.15 * np.sin(2 * np.pi * (0.13 + 0.05 * j) * tt)
            add(mix, s * e, t0, pan * (0.4 + 0.1 * j), 0.022)

# ---------------- sub bass pulses from EXTRACT on ----------------
ROOTS = {5.4: 34, 9.6: 29, 14.2: 36, 18.6: 38}
t = 5.4
while t < 21.0:
    root = [v for k, v in ROOTS.items() if t >= k][-1]
    n = int(0.45 * SR)
    tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * midi(root) * tt) + 0.25 * np.sin(2 * np.pi * midi(root + 12) * tt)
    add(mix, s * np.exp(-tt * 6) * np.minimum(1, tt * 200), t, 0, 0.12)
    t += BEAT

# ---------------- soft kick from BUILD on ----------------
t = 9.6
while t < 21.0:
    n = int(0.35 * SR)
    tt = np.arange(n) / SR
    f = 48 + 90 * np.exp(-tt * 30)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
    add(mix, s, t, 0, 0.42 if t >= 14.2 else 0.3)
    t += BEAT

# ---------------- data ticks: 16ths, density grows by stage ----------------
DENS = [0.35, 0.55, 0.7, 0.85, 0.9]
t = 0.6
step = BEAT / 4
i = 0
while t < 21.0:
    st = max(k for k in range(5) if t >= STAGES[k])
    if rng.random() < DENS[st] or i % 4 == 2:
        n = int(0.04 * SR)
        tt = np.arange(n) / SR
        s = rng.standard_normal(n) * np.exp(-tt * (160 if i % 4 else 90))
        add(mix, s, t + rng.normal(0, 0.002), rng.uniform(-0.8, 0.8), 0.05 * (1.4 if i % 4 == 2 else rng.uniform(0.4, 1)))
    t += step
    i += 1

# ---------------- arpeggio blips from BUILD ----------------
ARP = {9.6: [65, 69, 72, 77], 14.2: [67, 72, 76, 79], 18.6: [69, 74, 76, 77, 81]}
t = 9.6
i = 0
while t < 21.0:
    notes = [v for k, v in ARP.items() if t >= k][-1]
    m = notes[(i * 3 + (i // 4)) % len(notes)]
    n = int(0.3 * SR)
    tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * midi(m) * tt) + 0.3 * np.sin(2 * np.pi * midi(m) * 2 * tt) * np.exp(-tt * 30)
    add(mix, s * np.exp(-tt * 14) * np.minimum(1, tt * 400), t, 0.5 * np.sin(i * 0.7), 0.05)
    t += BEAT / 2 if t < 14.2 else BEAT / 4
    i += 1

# ---------------- "page pulled" bleeps, synced to the callouts ----------------
for k in range(24):
    t0 = 1.6 + k * 0.82
    if t0 > 21:
        break
    m = 84 + [0, 3, 7, 10, 5][k % 5]
    n = int(0.12 * SR)
    tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * midi(m) * tt) * np.exp(-tt * 35)
    s += 0.6 * np.sin(2 * np.pi * midi(m + 12) * tt) * np.exp(-tt * 50) * (tt > 0.05)
    add(mix, s, t0, [-0.7, 0.5, -0.3, 0.8][k % 4], 0.035)

# ---------------- risers into each stage change ----------------
for t1 in STAGES[1:5]:
    L = 1.6
    n = int(L * SR)
    tt = np.arange(n) / SR
    noise = rng.standard_normal(n)
    # sweep: blend from a low band to a high band of filtered noise
    lowb, highb = fft_filter(noise, lo=300, hi=1500), fft_filter(noise, lo=2500, hi=9000)
    u = tt / L
    s = (lowb * (1 - u) + highb * u) * u ** 2.2
    s += 0.25 * np.sin(2 * np.pi * np.cumsum(200 + 1600 * u ** 2) / SR) * u ** 3
    add(mix, s, t1 - L, 0, 0.09)
    # little impact on the downbeat
    n2 = int(0.9 * SR)
    t2 = np.arange(n2) / SR
    hit = fft_filter(rng.standard_normal(n2), hi=3000) * np.exp(-t2 * 7) * 0.5
    hit += np.sin(2 * np.pi * np.cumsum(40 + 60 * np.exp(-t2 * 20)) / SR) * np.exp(-t2 * 5)
    add(mix, hit, t1, 0, 0.22)

# ---------------- final: PACKAGE COMPLETE ----------------
n = int(1.6 * SR)
tt = np.arange(n) / SR
boom = np.sin(2 * np.pi * np.cumsum(34 + 50 * np.exp(-tt * 12)) / SR) * np.exp(-tt * 2.2)
add(mix, boom, 21.0, 0, 0.55)
for j, m in enumerate([74, 77, 81, 86, 88]):
    s = np.sin(2 * np.pi * midi(m) * tt) * np.exp(-tt * 1.8) * np.minimum(1, tt * 60)
    add(mix, s, 21.0 + j * 0.04, (j - 2) * 0.35, 0.05)

# ---------------- space: stereo FFT convolution reverb ----------------
def reverb(x, seconds=2.2, seed=0):
    r = np.random.default_rng(seed)
    n = int(seconds * SR)
    ir = r.standard_normal(n) * np.exp(-np.arange(n) / SR * 3.2)
    ir = fft_filter(ir, hi=6000)
    ir /= np.sqrt((ir ** 2).sum())
    L = len(x) + n
    y = np.fft.irfft(np.fft.rfft(x, L) * np.fft.rfft(ir, L), L)
    return y[: len(x)]

wet = np.stack([reverb(mix[0], seed=1), reverb(mix[1], seed=2)])
out = mix + 0.35 * wet

# keep the sub tidy, tame harsh highs
out = np.stack([fft_filter(c, lo=28, hi=14000) for c in out])

# master fades + soft limiter
fade = np.minimum(1, T / 0.6) * np.minimum(1, np.maximum(0, (DUR - T) / 0.9))
out *= fade
out /= np.max(np.abs(out)) + 1e-9
out = np.tanh(out * 1.6) / np.tanh(1.6) * 0.89

os.makedirs(os.path.join(ROOT, "audio"), exist_ok=True)
wav = os.path.join(ROOT, "audio", "music.wav")
mp3 = os.path.join(ROOT, "audio", "music.mp3")
pcm = (out.T * 32767).astype("<i2").tobytes()
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(SR), "-ac", "2", "-i", "-", wav], input=pcm, check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "libmp3lame", "-b:a", "256k", mp3], check=True)
print("wrote", mp3)
