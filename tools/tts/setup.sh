set -x
cd /home/claude/tts
for f in uztts/__init__.py uztts/normalize.py emotions_40h.json; do mkdir -p $(dirname $f); curl -sfL https://huggingface.co/aisha-org/navoiy-tts/raw/main/$f -o $f; done
pip install --break-system-packages -q torch torchaudio huggingface_hub==0.36.2 transformers==4.51.3 soundfile 2>&1 | tail -3
(git clone -q https://github.com/FunAudioLLM/CosyVoice.git && cd CosyVoice && git checkout -q 074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc && git submodule update --init --recursive -q) 2>&1 | tail -3
python3 -c "
from huggingface_hub import snapshot_download, hf_hub_download
p=snapshot_download('FunAudioLLM/CosyVoice2-0.5B', revision='eec1ae6c79877dbd9379285cf8789c9e0879293d', local_dir='CosyVoice2-0.5B'); print(p)
print(hf_hub_download('aisha-org/navoiy-tts','emotion_600h_joint.pt', local_dir='.'))
"
sha256sum emotion_600h_joint.pt
echo SETUP_DONE
# зависимости CosyVoice (CPU)
pip install --break-system-packages -q conformer==0.3.2 diffusers==0.29.0 HyperPyYAML inflect librosa lightning omegaconf openai-whisper pyworld x-transformers==2.11.24 wetext hydra-core modelscope rich gdown wget pyarrow matplotlib
# защита от зацикливания LLM: лимит токенов и выход при длинной тишине
python3 - <<'PY'
p='/home/claude/tts/CosyVoice/cosyvoice/cli/model.py'; s=open(p).read()
old="""            for i in token_generator:
                if i in self.silent_tokens:
                    cur_silent_token_num += 1
                    if cur_silent_token_num > max_silent_token_num:
                        continue"""
new="""            _n = 0
            for i in token_generator:
                _n += 1
                if _n > getattr(self, 'max_tok', 10 ** 9):
                    print('CAP_HIT', _n, flush=True); break
                if i in self.silent_tokens:
                    cur_silent_token_num += 1
                    if cur_silent_token_num > 60:
                        print('SILENT_LOOP', flush=True); break
                    if cur_silent_token_num > max_silent_token_num:
                        continue"""
if old in s: open(p,'w').write(s.replace(old,new))
PY
cp /home/claude/green-it-reels/tools/tts/synth.py /home/claude/green-it-reels/tools/tts/drive.sh /home/claude/tts/
