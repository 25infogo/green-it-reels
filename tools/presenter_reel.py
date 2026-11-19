"""
Ролик с ведущим: говорящий портрет (SadTalker) в фирменной рамке + плашки шагов + субтитры + фирменная концовка.
python3 presenter_reel.py <presenter.mp4> <voice.wav> <plan.json> <out.mp4>
plan.json: {"title": "...", "segments": [{"t0":0,"t1":7.6,"sub":"...","pills":[["текст","g|n|w"]]}], "music": true}
"""
import json, subprocess, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import reelkit as rk
from reelkit import W, H, FPS, text_c, pill, FB, FBo, FM, GREEN, WHITE, MUTED, ease_out, prog

pres, voice, plan_p, out = sys.argv[1:5]
plan = json.load(open(plan_p))
dur_voice = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice]))
OUTRO = 3.0
DUR = dur_voice + 0.6 + OUTRO
PS = 700; PX = (W - PS) // 2; PY = 250            # окно ведущего

def reader(src, size, start=0.0):
    return subprocess.Popen(["ffmpeg", "-loglevel", "error", "-ss", str(start), "-i", src, "-vf",
        f"scale={size[0]}:{size[1]}:force_original_aspect_ratio=increase:flags=lanczos,crop={size[0]}:{size[1]},fps={FPS}",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)

rk.BG = rk.make_bg()
mask = Image.new("L", (PS, PS), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, PS, PS], 60, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).rounded_rectangle([PX - 14, PY - 14, PX + PS + 14, PY + PS + 14], 72, fill=(56, 200, 255, 120))
glow = glow.filter(ImageFilter.GaussianBlur(26))

pr = reader(pres, (PS, PS)); last = None
outro = reader(os.path.join(rk.ASSETS, "clip1.mp4"), (W, H), 6.6)
enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
    "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", out + ".v.mp4"],
    stdin=subprocess.PIPE)

for i in range(int(DUR * FPS)):
    t = i / FPS
    if t >= DUR - OUTRO:
        buf = outro.stdout.read(W * H * 3)
        enc.stdin.write(buf if len(buf) == W * H * 3 else last_frame); continue
    img = rk.BG.copy().convert("RGBA")
    img.alpha_composite(glow)
    buf = pr.stdout.read(PS * PS * 3)
    if len(buf) == PS * PS * 3: last = Image.frombuffer("RGB", (PS, PS), buf)
    if last is not None:
        img.paste(last, (PX, PY), mask)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([PX, PY, PX + PS, PY + PS], 60, outline=GREEN + (255,), width=5)
    # плашка с именем
    pill(img, PY + PS - 40, plan.get("name", "Muhammad • Green IT"), "g", 40, 1.0, FB)
    # заголовок сверху
    text_c(img, 120, plan["title"], FB, 66, WHITE, ease_out(prog(t, 0, 0.4)))
    for seg in plan["segments"]:
        if seg["t0"] <= t < seg["t1"]:
            a = ease_out(prog(t, seg["t0"], seg["t0"] + 0.3))
            y = PY + PS + 90
            for j, (txt, kind) in enumerate(seg.get("pills", [])):
                aa = ease_out(prog(t, seg["t0"] + 0.25 * j, seg["t0"] + 0.25 * j + 0.3))
                pill(img, y + j * 120, txt, kind, 50, aa)
            # субтитры
            text_c(img, 1500, seg["sub"], FBo, 46, WHITE, a)
    d.rectangle([0, 0, W, 12], fill=(20, 32, 48)); d.rectangle([0, 0, W * t / DUR, 12], fill=GREEN)
    last_frame = img.convert("RGB").tobytes()
    enc.stdin.write(last_frame)
enc.stdin.close(); enc.wait(); pr.kill(); outro.kill()

# звук: голос + тихая музыка
subprocess.run(["python3", "beat.py", out + ".m.wav", f"{DUR:.2f}", f"{DUR-OUTRO-0.25:.2f}"], check=True, capture_output=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out + ".v.mp4", "-i", out + ".m.wav", "-i", voice,
    "-filter_complex", "[1:a]volume=0.22[m];[2:a]aresample=44100,aformat=channel_layouts=mono,volume=1.6[v];"
    "[m][v]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]",
    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
os.remove(out + ".v.mp4"); os.remove(out + ".m.wav")
print("ok", out, f"{DUR:.1f}s")
