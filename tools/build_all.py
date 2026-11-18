import subprocess, sys
from reelkit import render
from specs import REELS
only = sys.argv[1:]
for r in REELS:
    if only and r["slug"] not in only: continue
    wh = ",".join(f"{s['t0']-0.25:.2f}" for s in r["scenes"][1:])
    wav = f"out/{r['slug']}.wav"
    subprocess.run(["python3", "beat.py", wav, str(r["dur"]), wh], check=True, capture_output=True)
    render(r, f"out/{r['slug']}.mp4", wav)
    open(f"out/{r['slug']}.txt", "w").write(r["caption"])
    print("ok", r["slug"], flush=True)
