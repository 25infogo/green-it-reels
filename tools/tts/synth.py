import sys, os, random, json, time
sys.path.insert(0, '/home/claude/tts/CosyVoice'); sys.path.insert(0, '/home/claude/tts/CosyVoice/third_party/Matcha-TTS')
sys.path.insert(0, '/home/claude/tts'); sys.path.insert(0, '/home/claude/green-it-reels/tools')
import torch, torchaudio, soundfile as _sf
def _load(p, *a, **k):
    x, sr = _sf.read(p, dtype='float32', always_2d=True); return torch.from_numpy(x.T.copy()), sr
def _save(p, w, sr, *a, **k): _sf.write(p, w.detach().cpu().numpy().T, sr)
torchaudio.load = _load; torchaudio.save = _save
from cosyvoice.cli.cosyvoice import CosyVoice2
from uztts.normalize import normalize
import specs
out = sys.argv[1]; slugs = sys.argv[2:]
os.makedirs(out, exist_ok=True)
emo = [e for e in json.load(open('/home/claude/tts/emotions_40h.json')) if e['uz'] == 'mehribon'][0]
torch.set_num_threads(2)
m = CosyVoice2('/home/claude/tts/CosyVoice2-0.5B', load_jit=False, load_trt=False, fp16=False)
st = torch.load('/home/claude/tts/emotion_600h_joint.pt', map_location='cpu', weights_only=True)
for k in ('state_dict', 'model', 'llm'):
    if isinstance(st, dict) and isinstance(st.get(k), dict): st = st[k]
print(m.model.llm.load_state_dict(st, strict=False), flush=True); m.model.llm.eval()
ref = '/home/claude/tts/CosyVoice/asset/zero_shot_prompt.wav'
jobs = []
for s in slugs:
    for i, t in enumerate(specs.VOICE[s]):
        name = 'OUTRO.wav' if t == specs.OUTRO_VO else ('SAVE.wav' if t == specs.SAVE else f'{s}__{i}.wav')
        jobs.append((name, t))
jobs = list(dict.fromkeys(jobs))
for name, t in jobs:
    p = os.path.join(out, name)
    if os.path.exists(p): continue
    import signal
    def _to(*a): raise TimeoutError()
    signal.signal(signal.SIGALRM, _to)
    ok = False
    for seed in (2026, 2027, 2028, 2029):
        random.seed(seed); torch.manual_seed(seed)
        t0 = time.time(); ch = []
        signal.alarm(int(60 + 12 * len(t.split())))
        m.model.max_tok = int(25 * (0.75 * len(t.split()) + 2))
        try:
            with torch.inference_mode():
                for r in m.inference_instruct2(normalize(t, mode='infer'), emo['instruct'].strip() + '<|endofprompt|>', ref, stream=False):
                    ch.append(r['tts_speech'])
            signal.alarm(0)
        except TimeoutError:
            print(f'TIMEOUT {name} seed {seed}', flush=True); continue
        d = sum(c.shape[1] for c in ch) / 24000
        if d > 0.75 * len(t.split()) + 2: print(f'TOO LONG {name} {d:.1f}s seed {seed}', flush=True); continue
        ok = True; break
    if not ok: print(f'FAILED {name}', flush=True); continue
    a = torch.cat(ch, 1); torchaudio.save(p, a, 24000)
    print(f'{name}\t{a.shape[1]/24000:.2f}s\t{len(t.split())/(a.shape[1]/24000):.2f} w/s\tgen {time.time()-t0:.0f}s seed {seed}', flush=True)
print('SYNTH_DONE')
