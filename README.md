# green-it-reels

Reels для Instagram [@qorovulbozor_uz](https://www.instagram.com/qorovulbozor_uz/) — Green IT Serves, Qorovulbozor.

- `2026-11/` — готовые ролики (1080×1920, MP4) и подписи к ним (`.txt`). Публикуются по расписанию через Metricool.
- `tools/` — генератор роликов: `specs.py` (контент-план и тексты), `reelkit.py` (анимация), `beat.py` (фоновая музыка), `build_all.py` (сборка).

Сборка: `pip install pillow numpy` и ffmpeg, затем `python3 build_all.py` в папке `tools/`.
