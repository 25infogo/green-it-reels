# Озвучка Navoiy TTS на CPU (как делались ролики v3)

1. `bash tools/tts/setup.sh` — ставит torch (PyPI), CosyVoice @ 074ca6d, CosyVoice2-0.5B @ eec1ae6, чекпойнт emotion_600h_joint.pt (SHA-256 ced40fe6…), зависимости и патч от зацикливания; всё в /home/claude/tts. ~10 мин.
2. `cd /home/claude/tts && bash drive.sh <slug> [<slug> …]` — синтез фраз из `VOICE` (specs.py) в /home/claude/tts/vo: голос «mehribon», референс zero_shot_prompt.wav, seed 2026; уже готовые фразы пропускаются.
   Процесс синтеза иногда убивается средой (SIGKILL) или зависает — поэтому drive.sh запускает отдельный процесс на каждый ролик с повторами и укладывается в ~9 минут; запускать в переднем плане, не в фоне (фоновые процессы снимаются по окончании вызова).
3. `cd tools && python3 build_voice.py /home/claude/tts/vo <папка_вывода> <slug …>` — сборка (≈40 с на ролик).
Скорость: ~6× медленнее реального времени, ≈3–4 мин на ролик.
