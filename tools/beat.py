"""Простой фоновый бит 100 BPM + «вжух» на сменах сцен. Всё синтезируется, без чужой музыки."""
import numpy as np, wave, sys
np.random.seed(7)
SR = 44100
DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 24.0
BPM = int(sys.argv[4]) if len(sys.argv) > 4 else 100
WH = [float(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 and sys.argv[3] else [2.75, 8.75, 14.75, 19.75]
n = int(SR * DUR); out = np.zeros(n)
beat = 60 / BPM
t = np.arange(n) / SR

def add(sig, at, gain=1.0):
    i = int(at * SR); j = min(n, i + len(sig))
    if i < n: out[i:j] += sig[: j - i] * gain

def kick():
    d = 0.35; tt = np.arange(int(SR * d)) / SR
    f = 120 * np.exp(-tt * 18) + 45
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
def snare():
    d = 0.2; tt = np.arange(int(SR * d)) / SR
    return (np.random.randn(len(tt)) * 0.6 + np.sin(2 * np.pi * 190 * tt) * 0.4) * np.exp(-tt * 22)
def hat():
    d = 0.05; tt = np.arange(int(SR * d)) / SR
    x = np.random.randn(len(tt)); x = np.diff(np.concatenate([[0], x]))
    return x * np.exp(-tt * 70)
def whoosh():
    d = 0.6; tt = np.arange(int(SR * d)) / SR
    x = np.random.randn(len(tt))
    k = np.ones(40) / 40; x = np.convolve(x, k, mode="same")
    env = np.sin(np.pi * tt / d) ** 2
    return x * env * 3

# пэд: Am – F – C – G по 2 такта
chords = [[220, 261.6, 329.6], [174.6, 220, 261.6], [130.8, 196, 261.6], [196, 246.9, 293.7]]
bar = beat * 4
for k in range(int(DUR / (bar * 2)) + 1):
    ch = chords[k % 4]; st = k * bar * 2; d = bar * 2
    tt = np.arange(int(SR * d)) / SR
    pad = sum(np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2 * tt) for f in ch)
    env = np.minimum(1, tt / 0.4) * np.minimum(1, (d - tt) / 0.4)
    add(pad * env, st, 0.035)

nb = int(DUR / beat)
for b in range(nb):
    at = b * beat
    if at < 0.4: continue
    if b % 4 in (0, 2): add(kick(), at, 0.9)
    if b % 4 in (1, 3): add(snare(), at, 0.25)
    add(hat(), at + beat / 2, 0.18); add(hat(), at, 0.1)
for at in WH:
    add(whoosh(), at, 0.35)

out /= np.max(np.abs(out)) * 1.15
fade = int(SR * 1.0); out[-fade:] *= np.linspace(1, 0, fade)
pcm = (out * 32767).astype(np.int16)
with wave.open(sys.argv[1] if len(sys.argv) > 1 else "beat.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("ok")
