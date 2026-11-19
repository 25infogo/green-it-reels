# green-it-reels

Reels для Instagram [@qorovulbozor_uz](https://www.instagram.com/qorovulbozor_uz/) — Green IT Serves, Qorovulbozor.

- `2026-11/` — готовые ролики (1080×1920, MP4) и подписи к ним (`.txt`). Публикуются по расписанию через Metricool.
- `tools/` — генератор роликов: `specs.py` (контент-план и тексты), `reelkit.py` (анимация), `beat.py` (фоновая музыка), `build_all.py` (сборка).

Сборка: `pip install pillow numpy` и ffmpeg, затем `python3 build_all.py` в папке `tools/`.

Озвучка (v3, `2026-11/v3/`): узбекский голос Navoiy TTS (aisha-org/navoiy-tts, Apache-2.0, на базе CosyVoice2-0.5B), стиль «mehribon / warm», один голос для всех роликов.
Дикторский текст — `VOICE` в `tools/specs.py`; длительности сцен подгоняются под речь функцией `apply_voice`.
Сборка: синтезировать фразы в папку (`<slug>__<i>.wav`, `SAVE.wav`, `OUTRO.wav`, 24 кГц), затем `python3 build_voice.py <папка_с_фразами> ../2026-11/v3` в `tools/`.
Музыка `beat.py` под голосом: 0.20 во время речи, 0.32 без речи; итог нормализуется до ≈ −16 LUFS, true peak −1.5 dBTP.
