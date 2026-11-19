"""Stories 1080x1920 (JPG) про онлайн-резюме: фирменный фон, крупный заголовок, адрес сайта, «Havola profilda».
usage: python3 stories.py OUT_DIR
"""
import os, sys
from PIL import Image, ImageDraw
from reelkit import make_bg, text_c, pill, FB, FBo, FM, GREEN, GOLD, RED, WHITE, MUTED, W, H

URL = "green-it-service.uz/resume"
STORIES = [
    ("01", ["REZYUME", "10 DAQIQADA"], "Telefondan, onlayn", ["Ma'lumotlarni saytga yozing", "Tayyor PDF — chop etishga tayyor"]),
    ("02", ["OBYEKTIVKA", "KERAKMI?"], "Navbat kutmasdan", ["Saytda to'ldiring", "10 daqiqada tayyor PDF"]),
    ("03", ["KOMPYUTER", "SHART EMAS"], "Hammasi telefondan", ["Kompyuter markaziga bormang", "Uyda, 10 daqiqada"]),
    ("04", ["ISH", "QIDIRYAPSIZMI?"], "Avval — chiroyli rezyume", ["Ta'lim, tajriba, rasm", "Tayyor PDF shablon"]),
    ("05", ["REZYUME", "VA OBYEKTIVKA"], "Bitta saytda", ["Ikkala format ham bor", "To'lov: Click / Payme"]),
    ("06", ["10 DAQIQA —", "TAYYOR PDF"], "Hech qayerga bormasdan", ["Ma'lumotlarni yozing", "PDF ni yuklab oling"]),
    ("07", ["DO'STINGIZGA", "YUBORING"], "Ish qidirayotganlarga kerak", ["Rezyume telefondan", "10 daqiqada tayyor PDF"]),
]

def story(lines, sub, points):
    img = make_bg().convert("RGBA")
    text_c(img, 300, "GREEN IT • QOROVULBOZOR", FBo, 46, GREEN)
    text_c(img, 520, lines[0], FB, 120, WHITE)
    text_c(img, 660, lines[1], FB, 120, GOLD)
    pill(img, 860, sub, "w", 52)
    for i, p in enumerate(points):
        pill(img, 1040 + i * 130, p, "n", 50)
    pill(img, 1340, URL, "g", 54)
    text_c(img, 1460, "Havola profilda  ↑", FB, 64, WHITE)
    text_c(img, 1640, "+998 91 448 23 88", FB, 62, WHITE)
    text_c(img, 1730, "Savol bo'lsa — Direct'ga yozing", FM, 44, MUTED)
    return img.convert("RGB")

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for k, lines, sub, points in STORIES:
        story(lines, sub, points).save(os.path.join(out, f"story_rezyume_{k}.jpg"), quality=92)
        print("ok", k)
