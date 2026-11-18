"""
reelkit — шаблон анимированных Reels (1080x1920, 30 fps) для @qorovulbozor_uz.
Ролик описывается спецификацией (список сцен), кадры рисует Pillow, кодирует ffmpeg.
Сцены: hook / step / cta. Элементы шага: keys, run, pills, text, meter.
"""
import subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
FB = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FBo = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FM = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
FMONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
_fc = {}
def font(p, s):
    s = int(s); k = (p, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(p, s)
    return _fc[k]

GREEN = (56, 200, 255)   # фирменный неоново-голубой из роликов владельца
GOLD = (255, 196, 46); RED = (239, 68, 68); WHITE = (255, 255, 255)
MUTED = (165, 185, 205); KEYBG = (22, 34, 50); DARK = (4, 14, 26)
PILL = {"n": ((26, 42, 62), WHITE), "g": (GREEN, DARK), "r": (RED, WHITE), "w": (WHITE, (10, 30, 18))}
MAXW = 960

def make_bg():
    y = np.linspace(0, 1, H)[:, None]
    top = np.array([5, 9, 16]); bot = np.array([8, 24, 42])
    g = (top + (bot - top) * y)[:, None, :].repeat(W, axis=1).reshape(H, W, 3)
    img = Image.fromarray(g.astype(np.uint8)).convert("RGBA")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    for x in range(0, W, 90): od.line([(x, 0), (x, H)], fill=(255, 255, 255, 10))
    for yy in range(0, H, 90): od.line([(0, yy), (W, yy)], fill=(255, 255, 255, 10))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.15, H * 0.30, W * 0.85, H * 0.62], fill=(56, 200, 255, 38))
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    return Image.alpha_composite(Image.alpha_composite(img, ov), glow).convert("RGB")
BG = None

def clamp(v, a=0.0, b=1.0): return max(a, min(b, v))
def ease_out(t): t = clamp(t); return 1 - (1 - t) ** 3
def ease_back(t):
    t = clamp(t); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2
def prog(t, a, b): return clamp((t - a) / (b - a)) if b > a else float(t >= a)

def fit(path, size, s, maxw=MAXW):
    f = font(path, size)
    while f.getlength(s) > maxw and size > 20:
        size -= 2; f = font(path, size)
    return f

def text_c(img, y, s, path, size, fill=WHITE, alpha=1.0, dy=0):
    if alpha <= 0: return
    f = fit(path, size, s)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    w = d.textlength(s, font=f)
    d.text(((W - w) / 2, y + dy + (size - f.size) / 2), s, font=f, fill=fill + (int(255 * alpha),))
    img.alpha_composite(layer)

def pill(img, y, s, kind="n", size=50, alpha=1.0, path=FBo, pad=(34, 16)):
    if alpha <= 0: return
    bg, fg = PILL[kind]
    f = fit(path, size, s, MAXW - 2 * pad[0])
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    w = d.textlength(s, font=f); h = f.size; cx = W / 2
    d.rounded_rectangle([cx - w / 2 - pad[0], y, cx + w / 2 + pad[0], y + h + pad[1] * 2],
                        radius=(h + pad[1] * 2) // 2, fill=bg + (int(255 * alpha),))
    d.text((cx - w / 2, y + pad[1] - f.size * 0.08), s, font=f, fill=fg + (int(255 * alpha),))
    img.alpha_composite(layer)

def keys(img, y, labels, t0, t, gap=22):
    f = font(FBo, 58); fp = font(FBo, 54)
    items = []
    for lb in labels:
        if lb == "+": items.append(("+", fp.getlength("+") + 10, True))
        else: items.append((lb, max(150, f.getlength(lb) + 70), False))
    total = sum(w for _, w, _ in items) + gap * (len(items) - 1)
    sc_all = min(1.0, MAXW / total)
    x = (W - total * sc_all) / 2
    for i, (lb, w, plus) in enumerate(items):
        w *= sc_all
        p = ease_back(prog(t, t0 + i * 0.15, t0 + i * 0.15 + 0.35))
        a = prog(t, t0 + i * 0.15, t0 + i * 0.15 + 0.2)
        if a > 0:
            layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
            sc = (0.6 + 0.4 * p) * sc_all
            if plus:
                d.text((x, y + 40), "+", font=fp, fill=MUTED + (int(255 * a),))
            else:
                hh = 130 * sc; ww = w * (0.6 + 0.4 * p); cx = x + w / 2; cy = y + 65
                d.rounded_rectangle([cx - ww / 2, cy - hh / 2 + 10, cx + ww / 2, cy + hh / 2 + 10], 24,
                                    fill=(8, 14, 24, int(255 * a)))
                d.rounded_rectangle([cx - ww / 2, cy - hh / 2, cx + ww / 2, cy + hh / 2], 24,
                                    fill=KEYBG + (int(255 * a),), outline=GREEN + (int(255 * a),), width=4)
                fs = font(FBo, max(10, 58 * sc))
                tw = d.textlength(lb, font=fs)
                d.text((cx - tw / 2, cy - fs.size * 0.62), lb, font=fs, fill=WHITE + (int(255 * a),))
            img.alpha_composite(layer)
        x += w + gap * sc_all

def run_box(img, y, typed, t0, t, title="Ishga tushirish  (Win + R)"):
    a = ease_out(prog(t, t0, t0 + 0.3))
    if a <= 0: return
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    x0, x1 = 140, W - 140; dy = (1 - a) * 40; A = int(255 * a)
    d.rounded_rectangle([x0, y + dy, x1, y + 300 + dy], 22, fill=(243, 245, 244, A))
    d.rounded_rectangle([x0, y + dy, x1, y + 80 + dy], 22, fill=(225, 230, 228, A))
    d.rectangle([x0, y + 50 + dy, x1, y + 80 + dy], fill=(225, 230, 228, A))
    d.text((x0 + 34, y + 20 + dy), title, font=font(FM, 36), fill=(40, 50, 45, A))
    d.rounded_rectangle([x0 + 34, y + 130 + dy, x1 - 34, y + 240 + dy], 12,
                        fill=(255, 255, 255, A), outline=(30, 120, 200, A), width=4)
    fm = font(FMONO, 56)
    n = int(len(typed) * prog(t, t0 + 0.35, t0 + 0.35 + 0.08 * len(typed)))
    s = typed[:n]
    d.text((x0 + 62, y + 158 + dy), s, font=fm, fill=(20, 25, 22, A))
    if int(t * 2.5) % 2 == 0:
        cx = x0 + 66 + d.textlength(s, font=fm)
        d.rectangle([cx, y + 152 + dy, cx + 5, y + 222 + dy], fill=(20, 25, 22, A))
    img.alpha_composite(layer)

def meter(img, y, level, color, label, alpha):
    if alpha <= 0: return
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    x0, x1 = 180, W - 180; A = int(255 * alpha)
    d.text((x0, y - 70), label, font=font(FBo, 44), fill=MUTED + (A,))
    pct = f"{int(level * 100)}%"
    d.text((x1 - d.textlength(pct, font=font(FB, 44)), y - 70), pct, font=font(FB, 44), fill=color + (A,))
    d.rounded_rectangle([x0, y, x1, y + 44], 22, fill=(255, 255, 255, int(30 * alpha)))
    d.rounded_rectangle([x0, y, x0 + max(44, (x1 - x0) * level), y + 44], 22, fill=color + (A,))
    img.alpha_composite(layer)

def lerp_col(a, b, p): return tuple(int(a[i] + (b[i] - a[i]) * p) for i in range(3))

# ---------- сцены ----------
def scene_hook(img, t, s):
    t0, t1 = s["t0"], s["t1"]; lt = t - t0
    a_out = 1 - prog(t, t1 - 0.4, t1)
    shake = math.sin(lt * 40) * 6 * (1 - prog(lt, 0, 0.6))
    text_c(img, 560 + shake, s["l1"], FB, 104, WHITE, ease_out(prog(lt, 0, 0.25)) * a_out)
    text_c(img, 690, s["l2"], FB, 124, RED, ease_out(prog(lt, 0.15, 0.45)) * a_out,
           (1 - ease_back(prog(lt, 0.15, 0.5))) * 80)
    if s.get("sub"):
        pill(img, 910, s["sub"], "w", 50, ease_out(prog(lt, 0.7, 1.0)) * a_out)
    if s.get("meter"):
        lb, lvl, col = s["meter"]
        meter(img, 1250, lvl + 0.03 * math.sin(lt * 8), col, lb, ease_out(prog(lt, 1.0, 1.3)) * a_out)

def scene_step(img, t, s):
    t0, t1 = s["t0"], s["t1"]
    a_in = ease_out(prog(t, t0, t0 + 0.35)); a_out = 1 - prog(t, t1 - 0.25, t1); a = a_in * a_out
    if s.get("num"):
        pill(img, 330 + (1 - a_in) * 30, s["num"], "g", 44, a, FB)
    text_c(img, 470, s["h1"], FB, 84, WHITE, a, (1 - a_in) * 40)
    if s.get("h2"): text_c(img, 570, s["h2"], FB, 84, GREEN, a, (1 - a_in) * 50)
    for it in s["items"]:
        kind, at = it["k"], t0 + it["at"]
        until = t0 + it["until"] if "until" in it else t1
        if t < at or t >= until: continue
        y = it["y"]
        if kind == "keys": keys(img, y, it["v"], at, t)
        elif kind == "run": run_box(img, y, it["v"], at, t)
        elif kind == "text":
            text_c(img, y, it["v"], FM, it.get("size", 48), it.get("col", MUTED), ease_out(prog(t, at, at + 0.3)) * a_out)
        elif kind == "pills":
            gap = it.get("gap", 150); arrows = it.get("arrows", True)
            for i, (txt, pk) in enumerate(it["v"]):
                ts = at + i * it.get("stagger", 0.7)
                aa = ease_out(prog(t, ts, ts + 0.3)) * a_out
                pill(img, y + i * gap + (1 - ease_out(prog(t, ts, ts + 0.3))) * 30, txt, pk, it.get("size", 52), aa)
                if arrows and i < len(it["v"]) - 1 and aa > 0:
                    text_c(img, y + i * gap + 92, "↓", FB, 44, MUTED, aa)

def scene_cta(img, t, s):
    t0 = s["t0"]; lt = t - t0
    y = 380
    text_c(img, y, s.get("top", "NATIJA"), FB, 70, MUTED, ease_out(prog(lt, 0, 0.3)))
    if s.get("meter"):
        lb, l0, l1, c0, c1 = s["meter"]; p = ease_out(prog(lt, 0.2, 1.4))
        meter(img, 560, l0 + (l1 - l0) * p, lerp_col(c0, c1, p), lb, ease_out(prog(lt, 0.1, 0.4)))
        y = 720
    else:
        y = 520
    pill(img, y, s.get("main", "Saqlab qo'ying — kerak bo'ladi"), "g", 50, ease_out(prog(lt, 1.2, 1.5)))
    text_c(img, y + 200, s.get("ask", "Yordam kerakmi?"), FB, 80, WHITE, ease_out(prog(lt, 1.8, 2.1)))
    text_c(img, y + 310, "Green IT • Qorovulbozor", FBo, 58, GREEN, ease_out(prog(lt, 2.1, 2.4)))
    text_c(img, y + 410, "+998 91 448 23 88", FB, 70, WHITE, ease_out(prog(lt, 2.4, 2.7)))
    text_c(img, y + 530, s.get("tags", "Ta'mirlash • Windows • Litsenziya"), FM, 44, MUTED, ease_out(prog(lt, 2.7, 3.0)))

def scene_clip(img, t, s):
    """Чистый фрагмент брендового ролика (без наложений), например финал с контактами."""
    pass

SCENES = {"hook": scene_hook, "step": scene_step, "cta": scene_cta, "clip": scene_clip}

# ---------- фоновые видеоклипы (брендовые ролики владельца) ----------
import os
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "brand")

class ClipReader:
    """Последовательно отдаёт кадры клипа 1080x1920 @30fps через ffmpeg (зацикливает при нехватке)."""
    def __init__(self, src, start=0.0):
        self.src, self.start = src, start; self.p = None; self._open(start)
    def _open(self, start):
        if self.p: self.p.kill()
        self.p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-ss", str(start), "-i", self.src, "-vf",
            "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    def next(self):
        buf = self.p.stdout.read(W * H * 3)
        if len(buf) < W * H * 3:
            self._open(self.start); buf = self.p.stdout.read(W * H * 3)
        return Image.frombuffer("RGB", (W, H), buf)
    def close(self):
        if self.p: self.p.kill()

_readers = {}
def clip_frame(s, t, sequential=True):
    bg = s["bg"]; src = bg["src"] if os.path.isabs(bg["src"]) else os.path.join(ASSETS, bg["src"])
    key = id(s)
    if not sequential:
        r = ClipReader(src, bg.get("from", 0) + (t - s["t0"])); im = r.next(); r.close()
    else:
        if key not in _readers: _readers[key] = ClipReader(src, bg.get("from", 0) + (t - s["t0"]))
        im = _readers[key].next()
    if bg.get("blur"):
        im = im.resize((W // 4, H // 4)).filter(ImageFilter.GaussianBlur(bg["blur"] / 4)).resize((W, H), Image.BILINEAR)
    dim = bg.get("dim", 0.45)
    if dim > 0:
        im = Image.blend(im, Image.new("RGB", (W, H), (4, 8, 16)), dim)
    return im
SEQUENTIAL = True

def frame(spec, t):
    base = BG
    for s in spec["scenes"]:
        if s.get("bg") and s["t0"] <= t < s.get("t1", spec["dur"] + 1):
            base = clip_frame(s, t, SEQUENTIAL)
    img = base.copy().convert("RGBA")
    for s in spec["scenes"]:
        if s["t0"] <= t < s.get("t1", spec["dur"] + 1):
            SCENES[s["type"]](img, t, s)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=(20, 32, 48)); d.rectangle([0, 0, W * clamp(t / spec["dur"]), 12], fill=GREEN)
    return img.convert("RGB")

def render(spec, out, audio=None):
    global BG
    if BG is None: BG = make_bg()
    n = int(spec["dur"] * FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    if audio: cmd += ["-i", audio, "-c:a", "aac", "-b:a", "160k", "-shortest"]
    cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(frame(spec, i / FPS).tobytes())
    p.stdin.close(); p.wait()
    for r in _readers.values(): r.close()
    _readers.clear()

def preview(spec, times, out):
    global BG, SEQUENTIAL
    SEQUENTIAL = False
    if BG is None: BG = make_bg()
    ims = [frame(spec, t).resize((270, 480)) for t in times]
    sheet = Image.new("RGB", (270 * len(ims), 480))
    for i, im in enumerate(ims): sheet.paste(im, (i * 270, 0))
    sheet.save(out)
