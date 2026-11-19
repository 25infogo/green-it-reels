"""Сборка v3: ролики с узбекской озвучкой (Navoiy TTS) + фоновая музыка beat.py под голосом.
usage: python3 build_voice.py VO_DIR OUT_DIR [slug ...]
VO_DIR содержит <slug>__<i>.wav (фраза сцены i), SAVE.wav (мини-призыв), OUTRO.wav (концовка).
"""
import os, subprocess, sys, wave
import numpy as np, soundfile as sf
from reelkit import render
from specs import REELS, VOICE, SAVE, OUTRO_VO, RESUME_CTA, apply_voice

SR = 44100
MUSIC_SPEECH, MUSIC_FREE = 0.20, 0.32   # громкость музыки во время речи / без речи
VOICE_RMS = 0.11                        # целевой RMS речи (≈ −19 dBFS), голос = 1.0 относительно этой нормы

def vo_path(vo, slug, i, text):
    if text == SAVE: return os.path.join(vo, "SAVE.wav")
    if text == OUTRO_VO: return os.path.join(vo, "OUTRO.wav")
    if text == RESUME_CTA: return os.path.join(vo, "RESUME_CTA.wav")
    return os.path.join(vo, f"{slug}__{i}.wav")

def load(path):
    x, sr = sf.read(path, dtype="float32", always_2d=True); x = x.mean(axis=1)
    if sr != SR:
        n = int(round(len(x) * SR / sr)); x = np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x)
    # срезаем тишину по краям (порог −45 dBFS), чтобы фраза начиналась вовремя
    nz = np.where(np.abs(x) > 10 ** (-45 / 20))[0]
    if len(nz): x = x[max(0, nz[0] - int(0.03 * SR)): nz[-1] + int(0.08 * SR)]
    rms = np.sqrt(np.mean(x ** 2)) + 1e-9
    return x * (VOICE_RMS / rms)

def smooth(env, ms=180):
    k = int(SR * ms / 1000); ker = np.ones(k) / k
    return np.convolve(env, ker, mode="same")

def build(r, vo, out_dir):
    slug = r["slug"]
    voices = [load(vo_path(vo, slug, i, t)) if t else None for i, t in enumerate(VOICE[slug])]
    starts = apply_voice(r, [len(v) / SR if v is not None else 0 for v in voices])
    n = int(round(r["dur"] * SR))
    vtrack = np.zeros(n); speech = np.zeros(n)
    for v, st in zip(voices, starts):
        if v is None: continue
        i = int(st * SR); j = min(n, i + len(v)); vtrack[i:j] += v[: j - i]; speech[i:j] = 1
    wh = ",".join(f"{s['t0'] - 0.25:.2f}" for s in r["scenes"][1:])
    mpath = os.path.join(out_dir, f"{slug}.music.wav")
    subprocess.run(["python3", "beat.py", mpath, f"{r['dur']:.3f}", wh], check=True, capture_output=True)
    m, _ = sf.read(mpath, dtype="float32"); m = np.pad(m, (0, max(0, n - len(m))))[:n]
    gain = MUSIC_FREE + (MUSIC_SPEECH - MUSIC_FREE) * np.clip(smooth(speech), 0, 1)
    mix = vtrack * 1.0 + m * gain
    peak = np.max(np.abs(mix))
    if peak > 0.95: mix *= 0.95 / peak          # без клиппинга
    wpath = os.path.join(out_dir, f"{slug}.wav")
    with wave.open(wpath, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())
    # громкость для Reels: ≈ −16 LUFS, true peak −1.5 dBTP (баланс голос/музыка сохраняется)
    npath = os.path.join(out_dir, f"{slug}.norm.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wpath, "-af",
                    f"loudnorm=I=-16:TP=-1.5:LRA=11,aresample={SR}", "-ar", str(SR), npath], check=True)
    os.replace(npath, wpath)
    render(r, os.path.join(out_dir, f"{slug}.mp4"), wpath)
    open(os.path.join(out_dir, f"{slug}.txt"), "w").write(r["caption"])
    os.remove(mpath); os.remove(wpath)
    return dict(slug=slug, dur=r["dur"], peak=round(float(min(peak, 0.95)), 3),
                scenes=[(s["type"], s["t0"], s["t1"]) for s in r["scenes"]])

if __name__ == "__main__":
    vo, out_dir = sys.argv[1], sys.argv[2]; only = sys.argv[3:]
    os.makedirs(out_dir, exist_ok=True)
    for r in REELS:
        if only and r["slug"] not in only: continue
        print(build(r, vo, out_dir), flush=True)
