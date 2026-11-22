"""Контент-план: 8 Reels для @qorovulbozor_uz (спецификации видео + подписи)."""
from reelkit import RED, GREEN, WHITE

TAGS = "#kompyuterustasi #qorovulbozor #buxoro"
CONTACT = "Kompyuter ta'mirlash, Windows o'rnatish, litsenziya — Green IT, Qorovulbozor\n📞 +998 91 448 23 88\n🌐 green-it-service.uz"

def K(at, v, y=780, until=None):
    d = {"k": "keys", "at": at, "v": v, "y": y}
    if until is not None: d["until"] = until
    return d
def R(at, v, y=1000, until=None):
    d = {"k": "run", "at": at, "v": v, "y": y}
    if until is not None: d["until"] = until
    return d
def P(at, v, y=1000, **kw): return {"k": "pills", "at": at, "v": v, "y": y, **kw}
def T(at, v, y, **kw): return {"k": "text", "at": at, "v": v, "y": y, **kw}

REELS = []

# 1 ─ Kompyuter qotyaptimi?
REELS.append(dict(slug="01_kompyuter_tezlashtirish", dur=24, scenes=[
    dict(type="hook", t0=0, t1=3, l1="KOMPYUTERINGIZ", l2="QOTYAPTIMI?", sub="30 soniyada tezlashtiramiz",
         meter=("Tezlik", 0.18, RED)),
    dict(type="step", t0=3, t1=9, num="1 / 3", h1="Keraksiz fayllarni", h2="o'chiring", items=[
        K(0.4, ["Win", "+", "R"], until=2.6), R(1.1, "%temp%", until=3.6),
        K(3.4, ["Ctrl", "+", "A"]), K(4.3, ["Delete"], y=1010), T(4.6, "Hammasini o'chiring", 1220)]),
    dict(type="step", t0=9, t1=15, num="2 / 3", h1="Avtoyuklashni", h2="o'chiring", items=[
        K(0.4, ["Ctrl", "+", "Shift", "+", "Esc"]),
        P(1.8, [("Avtozagruzka / Startup", "n"), ("Keraksiz dastur", "n"), ("O'chirish / Disable", "g")], y=1040, stagger=0.8)]),
    dict(type="step", t0=15, t1=20, num="3 / 3", h1="Diskni", h2="tozalang", items=[
        K(0.4, ["Win", "+", "R"]), R(1.0, "cleanmgr"), K(2.6, ["Enter"], y=1360), T(3.4, "Disk C ni tanlang  →  OK", 1540)]),
    dict(type="cta", t0=20, meter=("Tezlik", 0.18, 0.95, RED, GREEN)),
], caption=f"""Kompyuter sekin ishlayaptimi? 3 ta usul bilan tezlashtiring 💻

1️⃣ Win + R → %temp% → hammasini o'chiring
2️⃣ Ctrl + Shift + Esc → Avtozagruzka → keraksiz dasturni o'chiring
3️⃣ Win + R → cleanmgr → Disk C → OK

🔖 Saqlab qo'ying — kerak bo'ladi!
Qaysi usul yordam berdi? Izohda yozing 👇

{CONTACT}

#kompyuter #windows {TAGS}"""))

# 2 ─ Litsenziya haqiqiymi?
REELS.append(dict(slug="02_litsenziya_tekshirish", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="WINDOWS'INGIZ", l2="ORIGINALMI?", sub="10 soniyada tekshiring"),
    dict(type="step", t0=3, t1=10, num="1 / 2", h1="Win + R ni bosing", h2="va yozing", items=[
        K(0.4, ["Win", "+", "R"]), R(1.2, "slmgr /xpr"), T(4.0, "Enter ni bosing", 1360)]),
    dict(type="step", t0=10, t1=16, num="2 / 2", h1="Natijaga", h2="qarang", items=[
        P(0.4, [("Permanently activated", "g")], y=820, arrows=False),
        T(0.9, "= ORIGINAL, doimiy", 960, col=GREEN, size=56),
        P(2.0, [("Muddat yoki xato chiqdi", "r")], y=1120, arrows=False),
        T(2.5, "= aktivator (vaqtinchalik)", 1260, col=RED, size=56),
        T(3.6, "Aktivatorlar ko'pincha virus olib keladi", 1440, size=44)]),
    dict(type="cta", t0=16, top="ORIGINAL LITSENZIYA", main="1 yil kafolat bilan", ask="Litsenziya kerakmi?",
         tags="Windows • Office • Antivirus"),
], caption=f"""Windows litsenziyangiz haqiqiymi? 10 soniyada tekshiring 🔍

Win + R → slmgr /xpr → Enter
✅ "Permanently activated" — litsenziya doimiy, original
❌ Muddat yoki xato chiqsa — bu aktivator

Aktivatorlar ko'pincha virus va reklama olib keladi.
Original Windows/Office litsenziya — 1 yil kafolat bilan.

Sizda qaysi natija chiqdi? Izohda yozing 👇

{CONTACT}

#windows #litsenziya {TAGS}"""))

# 3 ─ Noutbukni bunday qilmang
REELS.append(dict(slug="03_noutbuk_xatolar", dur=24, scenes=[
    dict(type="hook", t0=0, t1=3, l1="NOUTBUKNI", l2="BUNDAY QILMANG!", sub="3 ta katta xato"),
    dict(type="step", t0=3, t1=9, num="1 / 3", h1="Yumshoq joyda", h2="ishlatmang", items=[
        P(0.4, [("Ko'rpa, yostiq, divan", "n"), ("Havo kirmaydi → qizib ketadi", "r")], y=820),
        T(2.4, "Qattiq stol yoki podstavka ishlating", 1180)]),
    dict(type="step", t0=9, t1=15, num="2 / 3", h1="Zaryadni nolga", h2="tushirmang", items=[
        P(0.4, [("0% gacha tushirish", "r"), ("20–80% oralig'ida saqlang", "g")], y=820),
        T(2.4, "Batareya uzoqroq xizmat qiladi", 1180)]),
    dict(type="step", t0=15, t1=20, num="3 / 3", h1="Changni", h2="tozalamaslik", items=[
        P(0.4, [("Ventilyator chang bilan to'ladi", "n"), ("Qizish → sekinlashish → buzilish", "r")], y=820),
        T(2.4, "Yilda 1 marta profilaktika qiling", 1180, col=GREEN)]),
    dict(type="cta", t0=20, top="NOUTBUK SOG'LIG'I", main="Saqlab qo'ying — kerak bo'ladi", ask="Profilaktika kerakmi?",
         tags="Tozalash • Termopasta • Ta'mirlash"),
], caption=f"""Noutbukni hech qachon bunday qilmang! ⚠️

1️⃣ Yumshoq joyda (ko'rpa, divan) ishlatish — havo kirmaydi, qizib ketadi
2️⃣ Zaryadni har doim 0% gacha tushirish — batareya tez eskiradi
3️⃣ Changni yillab tozalamaslik — ventilyator ishdan chiqadi

✅ Yilda bir marta profilaktika: tozalash + termopasta

Siz qaysi xatoni qilgansiz? Izohda yozing 👇

{CONTACT}

#noutbuk #kompyuter {TAGS}"""))

# 4 ─ Telefon xotirasi
REELS.append(dict(slug="04_telefon_xotira", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="TELEFON XOTIRASI", l2="TO'LDIMI?", sub="Telegram'ni tozalaymiz",
         meter=("Xotira band", 0.96, RED)),
    dict(type="step", t0=3, t1=10, num="1 / 2", h1="Telegram keshini", h2="tozalang", items=[
        P(0.4, [("Sozlamalar", "n"), ("Ma'lumotlar va xotira", "n"), ("Xotiradan foydalanish", "n"),
                ("Keshni tozalash", "g")], y=780, stagger=0.9)]),
    dict(type="step", t0=10, t1=16, num="2 / 2", h1="Avto-yuklashni", h2="o'chiring", items=[
        P(0.4, [("Ma'lumotlar va xotira", "n"), ("Avtomatik yuklab olish", "n"), ("O'chirish", "g")], y=780, stagger=0.9),
        T(3.4, "Bir necha GB bo'shaydi", 1300, col=GREEN, size=56)]),
    dict(type="cta", t0=16, meter=("Xotira band", 0.96, 0.42, RED, GREEN), ask="Telefon sekinmi?",
         tags="Telefon • Proshivka • Ta'mirlash"),
], caption=f"""Telefon xotirasi to'ldimi? Eng ko'p joyni Telegram egallaydi 📱

1️⃣ Sozlamalar → Ma'lumotlar va xotira → Xotiradan foydalanish → Keshni tozalash
2️⃣ Avtomatik yuklab olishni o'chiring

Bir necha gigabayt bo'shaydi! 🔖 Saqlab qo'ying.
Sizda qancha bo'shadi? Izohda yozing 👇

{CONTACT}

#telefon #telegram {TAGS}"""))

# 5 ─ Internet sekinmi
REELS.append(dict(slug="05_wifi_sekin", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="INTERNETINGIZ", l2="SEKINMI?", sub="3 ta oddiy sabab", meter=("Tezlik", 0.22, RED)),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Routerni", h2="qayta yoqing", items=[
        P(0.4, [("Rozetkadan chiqaring", "n"), ("30 soniya kuting", "n"), ("Qayta yoqing", "g")], y=820, stagger=0.8)]),
    dict(type="step", t0=8.5, t1=13.5, num="2 / 3", h1="Router joyini", h2="o'zgartiring", items=[
        P(0.4, [("Shkaf ichida, polda", "r")], y=820, arrows=False),
        P(1.4, [("Baland va ochiq joyda", "g")], y=980, arrows=False),
        T(2.4, "Devorlar signalni susaytiradi", 1180)]),
    dict(type="step", t0=13.5, t1=18, num="3 / 3", h1="Parolni", h2="almashtiring", items=[
        T(0.4, "Qo'shnilar ulanib olgan bo'lishi mumkin", 820, size=46),
        P(1.4, [("Kuchli parol: 10+ belgi", "g")], y=960, arrows=False)]),
    dict(type="cta", t0=18, meter=("Tezlik", 0.22, 0.9, RED, GREEN), ask="Wi-Fi sozlash kerakmi?",
         tags="Router • Wi-Fi • Tarmoq"),
], caption=f"""Internet sekinmi? 3 ta oddiy sabab 📶

1️⃣ Routerni o'chirib, 30 soniyadan keyin qayta yoqing
2️⃣ Routerni baland va ochiq joyga qo'ying — shkaf ichida va polda emas
3️⃣ Parolni almashtiring — qo'shnilar ulanib olgan bo'lishi mumkin

🔖 Saqlab qo'ying! Qaysi biri yordam berdi? 👇

{CONTACT}

#wifi #internet {TAGS}"""))

# 6 ─ 5 ta foydali tugma
def key_step(t0, t1, num, h1, h2, ks):
    return dict(type="step", t0=t0, t1=t1, num=num, h1=h1, h2=h2, items=[K(0.4, ks, y=860)])
REELS.append(dict(slug="06_windows_tugmalar", dur=27, scenes=[
    dict(type="hook", t0=0, t1=3, l1="BU TUGMALARNI", l2="BILASIZMI?", sub="Windows uchun 5 ta sir"),
    key_step(3, 7, "1 / 5", "Ish stoliga", "bir zumda", ["Win", "+", "D"]),
    key_step(7, 11, "2 / 5", "Kompyuterni", "qulflash", ["Win", "+", "L"]),
    key_step(11, 15, "3 / 5", "Ekran rasmini", "olish", ["Win", "+", "Shift", "+", "S"]),
    key_step(15, 19, "4 / 5", "Nusxalar", "tarixi", ["Win", "+", "V"]),
    key_step(19, 23, "5 / 5", "Yopilgan sahifani", "qaytarish", ["Ctrl", "+", "Shift", "+", "T"]),
    dict(type="cta", t0=23, top="5 TA SIR", main="Saqlab qo'ying — kerak bo'ladi", ask="Yana kerakmi?",
         tags="Izohga «YANA» deb yozing"),
], caption=f"""Windows uchun 5 ta foydali tugma ⌨️

1️⃣ Win + D — ish stoliga bir zumda
2️⃣ Win + L — kompyuterni qulflash
3️⃣ Win + Shift + S — ekran rasmini olish
4️⃣ Win + V — nusxalar tarixi
5️⃣ Ctrl + Shift + T — yopilgan sahifani qaytarish

🔖 Saqlab qo'ying! Yana kerak bo'lsa, izohga «YANA» deb yozing 👇

{CONTACT}

#windows #kompyuter {TAGS}"""))

# 7 ─ Rezyume 5 daqiqada
REELS.append(dict(slug="07_rezyume_onlayn", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="REZYUME", l2="5 DAQIQADA", sub="Telefondan, onlayn"),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Saytga", h2="kiring", items=[
        P(0.4, [("green-it-service.uz/resume", "g")], y=860, arrows=False),
        T(1.4, "Havola profilda", 1040)]),
    dict(type="step", t0=8.5, t1=14, num="2 / 3", h1="Ma'lumotlarni", h2="to'ldiring", items=[
        P(0.4, [("F.I.Sh, tug'ilgan sana", "n"), ("Ta'lim va ish joylari", "n"), ("Rasm", "n")],
          y=800, arrows=False, gap=140, stagger=0.6)]),
    dict(type="step", t0=14, t1=18, num="3 / 3", h1="PDF ni", h2="yuklab oling", items=[
        P(0.4, [("Tayyor PDF — chop etishga", "g")], y=860, arrows=False),
        T(1.2, "Ma'lumotnoma (obyektivka) ham bor", 1040),
        T(2.0, "To'lov: Click / Payme", 1130)]),
    dict(type="cta", t0=18, top="ONLAYN XIZMAT", main="Havola profilda", ask="Savol bormi?",
         tags="Rezyume • Obyektivka • Hujjatlar"),
], caption=f"""Rezyume kerakmi? Kompyuter va navbat shart emas — telefondan, onlayn 📄

✍️ Ma'lumotlaringizni to'g'ridan-to'g'ri saytga yozing
⏱ 10 daqiqada tayyor PDF — chop etishga tayyor
📋 Rezyume va ma'lumotnoma (obyektivka) formatlari
💳 To'lov: Click / Payme

👉 green-it-service.uz/resume — havola profilda

Savol bo'lsa — Direct'ga yoki izohga yozing 👇

{CONTACT}

#rezyume #obyektivka #ish #vakansiya {TAGS}"""))

# 8 ─ Virus belgilari
def sym(t0, t1, num, h1, h2, txt):
    return dict(type="step", t0=t0, t1=t1, num=num, h1=h1, h2=h2, items=[P(0.4, [(txt, "r")], y=860, arrows=False)])
REELS.append(dict(slug="08_virus_belgilari", dur=24, scenes=[
    dict(type="hook", t0=0, t1=3, l1="KOMPYUTERDA", l2="VIRUS BORMI?", sub="4 ta belgi"),
    sym(3, 7, "1 / 4", "Reklama oynalari", "o'zi ochiladi", "Brauzer yopiq bo'lsa ham"),
    sym(7, 11, "2 / 4", "Bosh sahifa", "o'zgargan", "Siz o'zgartirmagansiz"),
    sym(11, 15, "3 / 4", "Protsessor", "100% band", "Hech narsa ochilmagan"),
    sym(15, 19, "4 / 4", "Fayllar", "yo'qolyapti", "Yoki nomi o'zgargan"),
    dict(type="cta", t0=19, top="BELGI BORMI?", main="Virusni tozalaymiz", ask="Yordam kerakmi?",
         tags="Antivirus • Tozalash • Windows"),
], caption=f"""Kompyuterda virus bormi? 4 ta belgi 🦠

1️⃣ Reklama oynalari o'zi ochiladi
2️⃣ Brauzer bosh sahifasi o'zgargan
3️⃣ Protsessor sababsiz 100% band
4️⃣ Fayllar yo'qolyapti yoki nomi o'zgargan

Bittasi bo'lsa ham — tekshirtiring. Virusni tozalaymiz, antivirus litsenziyasi bor.
Sizda qaysi belgi bor? 👇

{CONTACT}

#virus #antivirus {TAGS}"""))

# ─── Брендовый стиль владельца (assets/brand): кинематографичный фон в крючке + фирменная концовка ───
HOOK_BG = {
    "01_kompyuter_tezlashtirish": ("clip1.mp4", 0.0),
    "02_litsenziya_tekshirish": ("clip4.mp4", 7.5),
    "03_noutbuk_xatolar": ("clip3.mp4", 0.0),
    "04_telefon_xotira": ("clip5.mp4", 1.0),
    "05_wifi_sekin": ("clip2.mp4", 0.0),
    "06_windows_tugmalar": ("clip2.mp4", 1.8),
    "07_rezyume_onlayn": ("clip4.mp4", 8.5),
    "08_virus_belgilari": ("clip1.mp4", 2.0),
}
OUTRO = {"src": "clip1.mp4", "from": 6.6, "dim": 0.0}   # «LITSENZIYALI DASTURLAR» + телефон, Telegram, WhatsApp
OUTRO_LEN = 3.0
CTA_LEN = 2.4

def brandify(r, hook_bg=None):
    """Крючок поверх размытого брендового клипа, короткий CTA «saqlab qo'ying», затем фирменная концовка."""
    scenes = r["scenes"]
    src, frm = hook_bg or HOOK_BG.get(r["slug"], ("clip1.mp4", 0.0))
    scenes[0]["bg"] = {"src": src, "from": frm, "blur": 14, "dim": 0.55}
    cta = scenes[-1]
    cta["t1"] = cta["t0"] + CTA_LEN
    scenes.append({"type": "clip", "t0": cta["t1"], "t1": cta["t1"] + OUTRO_LEN, "bg": dict(OUTRO)})
    r["dur"] = cta["t1"] + OUTRO_LEN
    return r

for _r in REELS:
    brandify(_r)

# ─── Озвучка (v3): узбекский дикторский текст по сценам, голос Navoiy TTS (mehribon / warm) ───
# Порядок фраз = порядок сцен: hook, step…, cta, clip. Символы и команды записаны словами для произношения.
OUTRO_VO = "Green IT, Qorovulbozor. Raqam ekranda."
SAVE = "Saqlab qo'ying, kerak bo'ladi!"
VOICE = {
    "01_kompyuter_tezlashtirish": [
        "Kompyuteringiz qotyaptimi? O'ttiz soniyada tezlashtiramiz.",
        "Birinchi usul: keraksiz fayllarni o'chiring. Win va R ni bosing, persent temp persent deb yozing. "
        "Kontrol va A ni bosib, hammasini o'chiring.",
        "Ikkinchi usul: avtoyuklashni o'chiring. Kontrol, Shift va Esk tugmalarini bosing, "
        "avtozagruzka bo'limida keraksiz dasturni o'chirib qo'ying.",
        "Uchinchi usul: diskni tozalang. Win va R, klin em ge er deb yozing va Enter ni bosing. "
        "Disk C ni tanlab, okey bosing.",
        SAVE, OUTRO_VO],
    "02_litsenziya_tekshirish": [
        "Vindousingiz originalmi? O'n soniyada tekshiring.",
        "Win va R ni bosing va yozing: es el em ge er, slesh, iks pe er. Keyin Enter ni bosing.",
        "Natijaga qarang. Doimiy faollashgan deb chiqsa, litsenziya original. "
        "Muddat yoki xato chiqsa, bu aktivator. Aktivatorlar ko'pincha virus olib keladi.",
        "Original litsenziya, bir yil kafolat bilan. Saqlab qo'ying!",
        OUTRO_VO],
    "03_noutbuk_xatolar": [
        "Noutbukni bunday qilmang! Uchta katta xato.",
        "Birinchi xato: yumshoq joyda ishlatish. Ko'rpa yoki divanda havo kirmaydi, noutbuk qizib ketadi. "
        "Qattiq stol yoki podstavka ishlating.",
        "Ikkinchi xato: zaryadni nolga tushirish. Yigirmadan sakson foizgacha oraliqda saqlang, "
        "batareya uzoqroq xizmat qiladi.",
        "Uchinchi xato: changni tozalamaslik. Ventilyator chang bilan to'ladi, noutbuk qiziydi va sekinlashadi. "
        "Yilda bir marta profilaktika qiling.",
        SAVE, OUTRO_VO],
    "04_telefon_xotira": [
        "Telefon xotirasi to'ldimi? Telegramni tozalaymiz.",
        "Telegram keshini tozalang. Sozlamalar, ma'lumotlar va xotira, xotiradan foydalanish, "
        "keyin keshni tozalash tugmasini bosing.",
        "Endi avtomatik yuklab olishni o'chiring. Bir necha gigabayt joy bo'shaydi.",
        SAVE, OUTRO_VO],
    "05_wifi_sekin": [
        "Internetingiz sekinmi? Uchta oddiy sabab.",
        "Birinchi: routerni qayta yoqing. Rozetkadan chiqaring, o'ttiz soniya kuting va qayta yoqing.",
        "Ikkinchi: router joyini o'zgartiring. Shkaf ichida yoki polda emas, baland va ochiq joyga qo'ying. "
        "Devorlar signalni susaytiradi.",
        "Uchinchi: parolni almashtiring. Qo'shnilar ulanib olgan bo'lishi mumkin. "
        "Kamida o'nta belgidan iborat kuchli parol qo'ying.",
        SAVE, OUTRO_VO],
    "06_windows_tugmalar": [
        "Bu tugmalarni bilasizmi? Vindous uchun beshta sir.",
        "Win va De: ish stoliga bir zumda.",
        "Win va El: kompyuterni qulflash.",
        "Win, Shift va Es: ekran rasmini olish.",
        "Win va Ve: nusxalar tarixi.",
        "Kontrol, Shift va Te: yopilgan sahifani qaytarish.",
        "Saqlab qo'ying! Yana kerak bo'lsa, izohga yana deb yozing.",
        OUTRO_VO],
    "07_rezyume_onlayn": [
        "Rezyume besh daqiqada. Telefondan, onlayn.",
        "Birinchi: saytga kiring. Havola profilimizda.",
        "Ikkinchi: ma'lumotlarni to'ldiring. Ism va familiya, tug'ilgan sana, ta'lim, ish joylari va rasm.",
        "Uchinchi: tayyor pe de ef faylni yuklab oling. Obyektivka ham bor. To'lov Klik yoki Peymi orqali.",
        "Havola profilda. Saqlab qo'ying!",
        OUTRO_VO],
    "08_virus_belgilari": [
        "Kompyuterda virus bormi? To'rtta belgi.",
        "Birinchi belgi: reklama oynalari o'zi ochiladi, brauzer yopiq bo'lsa ham.",
        "Ikkinchi belgi: bosh sahifa o'zgargan, siz esa uni o'zgartirmagansiz.",
        "Uchinchi belgi: protsessor yuz foiz band, hech narsa ochilmagan bo'lsa ham.",
        "To'rtinchi belgi: fayllar yo'qolyapti yoki nomi o'zgargan.",
        "Belgi bormi? Virusni tozalaymiz. Saqlab qo'ying!",
        OUTRO_VO],
}
VO_PAD = 0.4     # запас после фразы, с
VO_LEAD = 0.15   # задержка начала фразы от начала сцены, с

def apply_voice(r, vo_durs, pad=VO_PAD, lead=VO_LEAD):
    """Длительность сцены = max(исходная, фраза + lead + pad); t0/t1 и dur пересчитываются,
    времена появления элементов шага растягиваются пропорционально, чтобы надписи шли за речью.
    vo_durs — длительности фраз по сценам (None/0 — без голоса). Возвращает старты фраз (с)."""
    t = 0.0; starts = []
    for s, d in zip(r["scenes"], vo_durs):
        orig = s["t1"] - s["t0"]
        p_ = 0.1 if s["type"] == "clip" else pad   # концовка: клип владельца длится 10 с (с 6.6 с — максимум 3.4 с)
        new = max(orig, d + lead + p_) if d else orig
        k = new / orig
        if k > 1 and s["type"] == "step":
            for it in s["items"]:
                it["at"] = round(it["at"] * k, 2)
                if "until" in it: it["until"] = round(it["until"] * k, 2)
        s["t0"], s["t1"] = round(t, 3), round(t + new, 3)
        starts.append(s["t0"] + lead if d else None)
        t += new
    r["dur"] = round(t, 3)
    return starts

# ─── Серия про резюме (v3, ноябрь 2026): «пишете прямо на сайте — PDF за 10 минут» ───
RESUME_URL = "green-it-service.uz/resume"
RESUME_CTA = "Havola profilda. Saqlab qo'ying!"
RESUME_REELS = []

RESUME_REELS.append(dict(slug="09_rezyume_xatolar", dur=24, scenes=[
    dict(type="hook", t0=0, t1=3, l1="REZYUMENGIZNI", l2="O'QISHMAYAPTIMI?", sub="3 ta katta xato"),
    dict(type="step", t0=3, t1=7.5, num="1 / 3", h1="Rasm yo'q", h2="yoki sifatsiz", items=[
        P(0.4, [("Selfi, qorong'i rasm", "r")], y=820, arrows=False),
        P(1.4, [("Toza fon, rasmiy kiyim", "g")], y=980, arrows=False)]),
    dict(type="step", t0=7.5, t1=12, num="2 / 3", h1="Ish joylari", h2="yozilmagan", items=[
        P(0.4, [("Faqat ism va telefon", "r")], y=820, arrows=False),
        P(1.4, [("Ta'lim + ish joylari + ko'nikmalar", "g")], y=980, arrows=False)]),
    dict(type="step", t0=12, t1=16.5, num="3 / 3", h1="Tartibsiz", h2="format", items=[
        P(0.4, [("Har xil shrift, siljigan jadval", "r")], y=820, arrows=False),
        P(1.4, [("Tayyor PDF shablon", "g")], y=980, arrows=False)]),
    dict(type="step", t0=16.5, t1=21, num="YECHIM", h1="Saytga yozing —", h2="10 daqiqada PDF", items=[
        P(0.4, [(RESUME_URL, "g")], y=860, arrows=False), T(1.4, "Havola profilda", 1040)]),
    dict(type="cta", t0=21, top="REZYUME ONLAYN", main="10 daqiqada tayyor PDF", ask="Havola profilda",
         tags="Rezyume • Obyektivka • PDF"),
], caption=f"""Rezyumengizni o'qishmayaptimi? 3 ta katta xato ❌

1️⃣ Rasm yo'q yoki sifatsiz — selfi emas, toza fonda rasmiy rasm
2️⃣ Ish joylari yozilmagan — ta'lim, tajriba, ko'nikmalar bo'lishi shart
3️⃣ Tartibsiz format — har xil shrift, siljigan jadval

✅ Yechim: ma'lumotlarni to'g'ridan-to'g'ri saytga yozing — 10 daqiqada tayyor PDF
👉 {RESUME_URL} (havola profilda)
💳 To'lov: Click / Payme

🔖 Saqlab qo'ying! Savol bo'lsa — Direct'ga yozing 👇

{CONTACT}

#rezyume #ish #vakansiya {TAGS}"""))

RESUME_REELS.append(dict(slug="10_obyektivka_onlayn", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="OBYEKTIVKA", l2="KERAKMI?", sub="Telefondan, 10 daqiqada"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Saytga", h2="kiring", items=[
        P(0.4, [(RESUME_URL, "g")], y=860, arrows=False), T(1.4, "Havola profilda", 1040)]),
    dict(type="step", t0=8, t1=13.5, num="2 / 3", h1="Ma'lumotlarni", h2="yozing", items=[
        P(0.4, [("F.I.Sh, tug'ilgan sana", "n"), ("Ma'lumoti, mutaxassisligi", "n"), ("Ish faoliyati", "n")],
          y=800, arrows=False, gap=140, stagger=0.6)]),
    dict(type="step", t0=13.5, t1=18, num="3 / 3", h1="10 daqiqada", h2="tayyor PDF", items=[
        P(0.4, [("Obyektivka — chop etishga tayyor", "g")], y=860, arrows=False),
        T(1.4, "To'lov: Click / Payme", 1040)]),
    dict(type="cta", t0=18, top="OBYEKTIVKA ONLAYN", main="10 daqiqada tayyor PDF", ask="Havola profilda",
         tags="Obyektivka • Rezyume • Hujjatlar"),
], caption=f"""Obyektivka (ma'lumotnoma) kerakmi? Telefondan, 10 daqiqada 📋

1️⃣ {RESUME_URL} saytiga kiring (havola profilda)
2️⃣ Ma'lumotlaringizni to'g'ridan-to'g'ri saytga yozing
3️⃣ 10 daqiqada tayyor PDF — chop etishga tayyor

Kompyuter markaziga borish va navbat kutish shart emas.
💳 To'lov: Click / Payme

🔖 Saqlab qo'ying! Savol bo'lsa — Direct'ga yozing 👇

{CONTACT}

#obyektivka #malumotnoma #rezyume {TAGS}"""))

RESUME_REELS.append(dict(slug="11_rezyume_telefondan", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="KOMPYUTER", l2="SHART EMAS!", sub="Rezyume — telefondan"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Navbat kutish", h2="kerak emas", items=[
        P(0.4, [("Kompyuter markaziga borish", "r")], y=820, arrows=False),
        P(1.4, [("Uyda, telefondan yozish", "g")], y=980, arrows=False)]),
    dict(type="step", t0=8, t1=13, num="2 / 3", h1="To'g'ridan-to'g'ri", h2="saytga yozing", items=[
        P(0.4, [(RESUME_URL, "g")], y=860, arrows=False), T(1.4, "Havola profilda", 1040)]),
    dict(type="step", t0=13, t1=18, num="3 / 3", h1="10 daqiqada", h2="tayyor PDF", items=[
        P(0.4, [("Rezyume", "n"), ("Obyektivka", "n")], y=820, arrows=False, gap=140, stagger=0.6),
        T(1.8, "To'lov: Click / Payme", 1140)]),
    dict(type="cta", t0=18, top="ONLAYN XIZMAT", main="10 daqiqada tayyor PDF", ask="Havola profilda",
         tags="Rezyume • Obyektivka • PDF"),
], caption=f"""Rezyume uchun kompyuter shart emas — hammasi telefondan 📱

✍️ Ma'lumotlaringizni to'g'ridan-to'g'ri saytga yozasiz
⏱ 10 daqiqada tayyor PDF
📋 Rezyume va obyektivka formatlari
💳 To'lov: Click / Payme

👉 {RESUME_URL} — havola profilda

Ish qidirayotgan do'stingizga yuboring 👇

{CONTACT}

#rezyume #obyektivka #ish {TAGS}"""))

HOOK_BG.update({"09_rezyume_xatolar": ("clip4.mp4", 8.5), "10_obyektivka_onlayn": ("clip5.mp4", 1.0),
                "11_rezyume_telefondan": ("clip5.mp4", 0.0)})
for _r in RESUME_REELS:
    brandify(_r)
REELS.extend(RESUME_REELS)

VOICE.update({
    "09_rezyume_xatolar": [
        "Rezyumengizni o'qishmayaptimi? Uchta katta xato bor.",
        "Birinchi xato: rasm yo'q yoki sifatsiz. Selfi emas, toza fonda rasmiy rasm qo'ying.",
        "Ikkinchi xato: ish joylari yozilmagan. Ta'lim, ish tajribasi va ko'nikmalarni albatta yozing.",
        "Uchinchi xato: tartibsiz format. Har xil shrift va siljigan jadval yomon taassurot qoldiradi.",
        "Yechim: ma'lumotlarni to'g'ridan-to'g'ri saytga yozing. O'n daqiqada tayyor pe de ef olasiz.",
        RESUME_CTA, OUTRO_VO],
    "10_obyektivka_onlayn": [
        "Obyektivka kerakmi? Telefondan, o'n daqiqada.",
        "Birinchi: saytga kiring. Havola profilimizda.",
        "Ikkinchi: ma'lumotlaringizni to'g'ridan-to'g'ri saytga yozing. Ism, tug'ilgan sana, ma'lumotingiz va ish faoliyatingiz.",
        "Uchinchi: o'n daqiqada tayyor pe de ef ni yuklab oling va chop eting. To'lov Klik yoki Peymi orqali.",
        RESUME_CTA, OUTRO_VO],
    "11_rezyume_telefondan": [
        "Rezyume uchun kompyuter shart emas! Hammasi telefondan.",
        "Kompyuter markaziga borish va navbat kutish kerak emas. Uyda, telefondan yozasiz.",
        "Ma'lumotlarni to'g'ridan-to'g'ri saytga yozing. Havola profilimizda.",
        "O'n daqiqada tayyor pe de ef. Rezyume ham, obyektivka ham bor. To'lov Klik yoki Peymi orqali.",
        "Havola profilda. Do'stlaringizga ham yuboring!",
        OUTRO_VO],
})

# ─── Серия по категориям услуг (v3, 27.11–04.12.2026): принтеры, телефоны, сети/удалённая помощь, Windows/Office ───
SERVICE_REELS = []

SERVICE_REELS.append(dict(slug="12_printer_chop_etmayapti", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="PRINTER", l2="CHOP ETMAYAPTIMI?", sub="3 ta tekshiruv"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Ulanishni", h2="tekshiring", items=[
        P(0.4, [("Kabel yoki Wi-Fi ulanganmi?", "n"), ("Qog'oz bormi, qopqoq yopiqmi?", "n")],
          y=820, arrows=False, gap=150, stagger=0.8)]),
    dict(type="step", t0=8, t1=14, num="2 / 3", h1="Navbatni", h2="tozalang", items=[
        P(0.4, [("Sozlamalar", "n"), ("Printerlar va skanerlar", "n"), ("Navbatni ochish", "n"),
                ("Hammasini bekor qilish", "g")], y=780, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Printerni", h2="qayta yoqing", items=[
        P(0.4, [("O'chiring, 30 soniya kuting", "n"), ("Qayta yoqing", "g")], y=820, stagger=0.8),
        T(2.4, "Keyin yana chop etib ko'ring", 1180)]),
    dict(type="cta", t0=19, top="PRINTER USTASI", main="Saqlab qo'ying — kerak bo'ladi", ask="Yordam bermadimi?",
         tags="Printer • Ta'mirlash • Kartrij"),
], caption=f"""Printer chop etmayaptimi? Ustaga borishdan oldin 3 ta tekshiruv 🖨

1️⃣ Kabel yoki Wi-Fi ulanganmi, qog'oz bormi, qopqoq yopiqmi
2️⃣ Sozlamalar → Printerlar va skanerlar → Navbatni ochish → Hammasini bekor qilish
3️⃣ Printerni o'chiring, 30 soniyadan keyin qayta yoqing

🔖 Saqlab qo'ying! Yordam bermasa — printerni o'rnatamiz va ta'mirlaymiz.
Sizda qanday printer? Izohda yozing 👇

{CONTACT}

#printer #kartrij {TAGS}"""))

SERVICE_REELS.append(dict(slug="13_kartrij_tejash", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="KARTRIJ", l2="TEZ TUGAYAPTIMI?", sub="3 ta tejash usuli",
         meter=("Kartrij", 0.15, RED)),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Tejamkor", h2="rejimni yoqing", items=[
        P(0.4, [("Chop etish sozlamalari", "n"), ("Qoralama / Draft", "g")], y=820, stagger=0.8),
        T(2.4, "Hujjatlar uchun yetarli", 1180)]),
    dict(type="step", t0=8, t1=13, num="2 / 3", h1="Faqat kerakli", h2="sahifalarni", items=[
        P(0.4, [("Avval ko'rib chiqing", "n"), ("Sahifalar: 1-3", "g")], y=820, stagger=0.8)]),
    dict(type="step", t0=13, t1=18, num="3 / 3", h1="Siyoh qurib", h2="qolmasin", items=[
        P(0.4, [("Siyohli printer", "n")], y=820, arrows=False),
        T(1.2, "Haftada 1 sahifa chop eting", 980, col=GREEN, size=56)]),
    dict(type="cta", t0=18, meter=("Kartrij", 0.15, 0.95, RED, GREEN), ask="Kartrij to'ldirish kerakmi?",
         tags="Kartrij • Printer • Ta'mirlash"),
], caption=f"""Kartrij tez tugayaptimi? 3 ta tejash usuli 🖨

1️⃣ Chop etish sozlamalarida «Qoralama / Draft» rejimini yoqing — hujjatlar uchun yetarli
2️⃣ Avval ko'rib chiqing va faqat kerakli sahifalarni chop eting
3️⃣ Siyohli printerda haftada kamida 1 sahifa chop eting — siyoh qurib qolmaydi

🔖 Saqlab qo'ying! Kartrijni to'ldiramiz, printerni ta'mirlaymiz.
Siz qaysi usulni bilmagansiz? Izohda yozing 👇

{CONTACT}

#kartrij #printer {TAGS}"""))

SERVICE_REELS.append(dict(slug="14_telefon_reklama", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="TELEFONDA", l2="REKLAMA CHIQAVERADIMI?", sub="Android: 3 ta qadam"),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Shubhali ilovani", h2="o'chiring", items=[
        P(0.4, [("Sozlamalar", "n"), ("Ilovalar", "n"), ("Notanish ilova → O'chirish", "g")], y=800, stagger=0.8),
        T(3.0, "Reklama boshlangan kuni o'rnatilgan ilova", 1300)]),
    dict(type="step", t0=8.5, t1=14, num="2 / 3", h1="Sayt bildirish-", h2="nomalarini o'chiring", items=[
        P(0.4, [("Chrome", "n"), ("Sozlamalar → Bildirishnomalar", "n"), ("Saytlarni o'chirish", "g")],
          y=800, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Play Protect", h2="tekshiruvi", items=[
        P(0.4, [("Play Market → Profil", "n"), ("Play Protect", "n"), ("Tekshirish", "g")], y=800, stagger=0.8)]),
    dict(type="cta", t0=19, top="TOZA TELEFON", main="Saqlab qo'ying — kerak bo'ladi", ask="Reklama ketmadimi?",
         tags="Tozalash • Proshivka • Dasturlar"),
], caption=f"""Telefonda reklama o'zi chiqaveradimi? Android uchun 3 ta qadam 📱

1️⃣ Sozlamalar → Ilovalar → reklama boshlangan paytda o'rnatilgan notanish ilovani o'chiring
2️⃣ Chrome → Sozlamalar → Bildirishnomalar → saytlar bildirishnomasini o'chiring
3️⃣ Play Market → Profil → Play Protect → Tekshirish

🔖 Saqlab qo'ying! Reklama ketmasa — telefonni viruslardan tozalaymiz, kerak bo'lsa proshivka qilamiz.
Sizda qanday telefon? Izohda yozing 👇

{CONTACT}

#telefon #android {TAGS}"""))

SERVICE_REELS.append(dict(slug="15_telefon_sekin", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="TELEFONINGIZ", l2="SEKINLASHDIMI?", sub="3 ta oddiy qadam",
         meter=("Tezlik", 0.2, RED)),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Tizimni", h2="yangilang", items=[
        P(0.4, [("Sozlamalar", "n"), ("Tizim yangilanishi", "n"), ("Yangilash", "g")], y=800, stagger=0.8)]),
    dict(type="step", t0=8.5, t1=13.5, num="2 / 3", h1="Keraksiz", h2="ilovalarni o'chiring", items=[
        P(0.4, [("Oylab ochilmagan ilovalar", "r")], y=820, arrows=False),
        T(1.4, "Ular fonda xotira va batareyani yeydi", 980, size=46)]),
    dict(type="step", t0=13.5, t1=18, num="3 / 3", h1="Haftada bir", h2="qayta yoqing", items=[
        P(0.4, [("Qayta ishga tushirish", "g")], y=860, arrows=False),
        T(1.4, "Xotira tozalanadi, telefon yengillashadi", 1020, size=46)]),
    dict(type="cta", t0=18, meter=("Tezlik", 0.2, 0.9, RED, GREEN), ask="Yordam bermadimi?",
         tags="Proshivka • Dasturlar • Tozalash"),
], caption=f"""Telefoningiz sekinlashdimi? 3 ta oddiy qadam 📱

1️⃣ Sozlamalar → Tizim yangilanishi → Yangilash
2️⃣ Oylab ochilmagan ilovalarni o'chiring — ular fonda xotira va batareyani yeydi
3️⃣ Haftada bir marta telefonni qayta ishga tushiring

🔖 Saqlab qo'ying! Yordam bermasa — dasturini qayta o'rnatamiz (proshivka).
Telefoningiz necha yillik? Izohda yozing 👇

{CONTACT}

#telefon #proshivka {TAGS}"""))

SERVICE_REELS.append(dict(slug="16_wifi_himoya", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="WI-FI ROUTERINGIZ", l2="HIMOYALANGANMI?", sub="3 ta muhim sozlama"),
    dict(type="step", t0=3, t1=9, num="1 / 3", h1="Router parolini", h2="almashtiring", items=[
        P(0.4, [("Brauzerda: 192.168.0.1 yoki 192.168.1.1", "n")], y=820, arrows=False),
        P(1.6, [("admin / admin", "r")], y=980, arrows=False),
        T(2.6, "Standart parolni albatta almashtiring", 1160)]),
    dict(type="step", t0=9, t1=14, num="2 / 3", h1="Shifrlashni", h2="tanlang", items=[
        P(0.4, [("WPA2 yoki WPA3", "g")], y=860, arrows=False),
        T(1.4, "Ochiq tarmoq yoki WEP — xavfli", 1020, col=RED, size=50)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="WPS ni", h2="o'chiring", items=[
        P(0.4, [("WPS: O'chirish", "g")], y=860, arrows=False),
        T(1.4, "Begonalar tugma orqali ulana olmaydi", 1020, size=46)]),
    dict(type="cta", t0=19, top="TARMOQ XAVFSIZLIGI", main="Saqlab qo'ying — kerak bo'ladi", ask="Sozlash kerakmi?",
         tags="Router • Wi-Fi • Xavfsizlik"),
], caption=f"""Wi-Fi routeringiz himoyalanganmi? 3 ta muhim sozlama 🔐

1️⃣ Brauzerda 192.168.0.1 yoki 192.168.1.1 ni oching — standart «admin» parolini almashtiring
2️⃣ Shifrlash: WPA2 yoki WPA3 (ochiq tarmoq va WEP xavfli)
3️⃣ WPS ni o'chiring — begonalar tugma orqali ulana olmaydi

🔖 Saqlab qo'ying! Routerni sozlaymiz, tarmoqni himoyalaymiz.
Routeringiz parolini oxirgi marta qachon almashtirgansiz? 👇

{CONTACT}

#wifi #xavfsizlik {TAGS}"""))

SERVICE_REELS.append(dict(slug="17_masofaviy_yordam", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="USTAGA BORISH", l2="SHART EMAS!", sub="Masofaviy yordam"),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Bizga", h2="yozing", items=[
        P(0.4, [("Telefon yoki Telegram", "g")], y=860, arrows=False),
        T(1.4, "Muammoni qisqacha tushuntiring", 1020)]),
    dict(type="step", t0=8.5, t1=14, num="2 / 3", h1="Kompyuterga", h2="masofadan ulanamiz", items=[
        P(0.4, [("Windows va dasturlar o'rnatish", "n"), ("Xatolarni tuzatish", "n"), ("Sozlash", "n")],
          y=800, arrows=False, gap=140, stagger=0.6)]),
    dict(type="step", t0=14, t1=19, num="QOIDA", h1="Xavfsizlik", h2="birinchi o'rinda", items=[
        P(0.4, [("Faqat o'zingiz chaqirgan ustaga", "g")], y=820, arrows=False),
        P(1.6, [("Notanish «bank xodimi»ga — YO'Q", "r")], y=980, arrows=False),
        T(2.8, "Ish tugagach ulanishni uzing", 1160)]),
    dict(type="cta", t0=19, top="MASOFAVIY YORDAM", main="Uydan chiqmasdan", ask="Yordam kerakmi?",
         tags="Windows • Dasturlar • Sozlash"),
], caption=f"""Kompyuter muammosi? Ustaga borish shart emas — masofaviy yordam 💻

1️⃣ Bizga qo'ng'iroq qiling yoki Telegram'da yozing
2️⃣ Kompyuteringizga masofadan ulanamiz: Windows va dasturlar o'rnatish, xatolarni tuzatish, sozlash
3️⃣ Xavfsizlik qoidasi: kompyuterga faqat o'zingiz chaqirgan ustani ulang. Notanish «bank xodimi» yoki «texnik yordam» so'rasa — ruxsat bermang. Ish tugagach ulanishni uzing.

🔖 Saqlab qo'ying! Savol bo'lsa — Direct'ga yozing 👇

{CONTACT}

#masofaviyyordam #kompyuter {TAGS}"""))

SERVICE_REELS.append(dict(slug="18_windows_himoya", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="ANTIVIRUS", l2="YOQILGANMI?", sub="Windows'da 1 daqiqada tekshiring"),
    dict(type="step", t0=3, t1=9, num="1 / 3", h1="Windows Security", h2="ni oching", items=[
        K(0.4, ["Win", "+", "I"], until=2.4),
        P(1.6, [("Maxfiylik va xavfsizlik", "n"), ("Windows Security", "g")], y=1000, stagger=0.8)]),
    dict(type="step", t0=9, t1=14, num="2 / 3", h1="Tez tekshiruvni", h2="ishga tushiring", items=[
        P(0.4, [("Viruslardan himoya", "n"), ("Tez tekshiruv / Quick scan", "g")], y=820, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Yangilanishlarni", h2="o'rnating", items=[
        P(0.4, [("Windows Update", "n"), ("Yangilanishlarni tekshirish", "g")], y=820, stagger=0.8),
        T(2.4, "Himoya faqat yangilangan tizimda ishlaydi", 1180, size=44)]),
    dict(type="cta", t0=19, top="ORIGINAL ANTIVIRUS", main="1 yil kafolat bilan", ask="Himoya kerakmi?",
         tags="Antivirus • Windows • Litsenziya"),
], caption=f"""Kompyuteringizda antivirus yoqilganmi? 1 daqiqada tekshiring 🛡

1️⃣ Win + I → Maxfiylik va xavfsizlik → Windows Security
2️⃣ Viruslardan himoya → Tez tekshiruv (Quick scan)
3️⃣ Windows Update → Yangilanishlarni tekshirish — himoya faqat yangilangan tizimda to'liq ishlaydi

🔖 Saqlab qo'ying! Original Windows va antivirus litsenziyasi — 1 yil kafolat bilan.
Tekshiruv nima ko'rsatdi? Izohda yozing 👇

{CONTACT}

#antivirus #windows {TAGS}"""))

SERVICE_REELS.append(dict(slug="19_word_tiklash", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="WORD FAYL", l2="SAQLANMAY QOLDIMI?", sub="Qaytarish mumkin!"),
    dict(type="step", t0=3, t1=9.5, num="1 / 2", h1="Saqlanmagan", h2="hujjatni tiklang", items=[
        P(0.4, [("Fayl → Ma'lumotlar", "n"), ("Hujjatni boshqarish", "n"), ("Saqlanmagan hujjatlarni tiklash", "g")],
          y=800, stagger=0.9)]),
    dict(type="step", t0=9.5, t1=15.5, num="2 / 2", h1="Avtosaqlashni", h2="sozlang", items=[
        P(0.4, [("Fayl → Parametrlar → Saqlash", "n"), ("Har 1 daqiqada avtosaqlash", "g")], y=820, stagger=0.9),
        T(2.6, "Endi ish yo'qolmaydi", 1180, col=GREEN, size=56)]),
    dict(type="cta", t0=15.5, top="OFFICE O'RNATISH", main="Original litsenziya", ask="Office kerakmi?",
         tags="Word • Excel • Office"),
], caption=f"""Word fayl saqlanmay yopilib qoldimi? Uni qaytarish mumkin 📝

1️⃣ Word → Fayl → Ma'lumotlar → Hujjatni boshqarish → Saqlanmagan hujjatlarni tiklash
2️⃣ Fayl → Parametrlar → Saqlash → «Har 1 daqiqada avtosaqlash» ni yoqing

🔖 Saqlab qo'ying — bir kun albatta kerak bo'ladi!
Office o'rnatish va original litsenziya — 1 yil kafolat bilan.
Sizda shunday bo'lganmi? Izohda yozing 👇

{CONTACT}

#word #office {TAGS}"""))

HOOK_BG.update({"12_printer_chop_etmayapti": ("clip6.mp4", 0.0), "13_kartrij_tejash": ("clip6.mp4", 2.0),
                "14_telefon_reklama": ("clip5.mp4", 0.0), "15_telefon_sekin": ("clip5.mp4", 1.0),
                "16_wifi_himoya": ("clip2.mp4", 0.0), "17_masofaviy_yordam": ("clip2.mp4", 7.5),
                "18_windows_himoya": ("clip3.mp4", 0.0), "19_word_tiklash": ("clip4.mp4", 7.5)})
for _r in SERVICE_REELS:
    brandify(_r)
REELS.extend(SERVICE_REELS)

VOICE.update({
    "12_printer_chop_etmayapti": [
        "Printer chop etmayaptimi? Ustaga borishdan oldin uchta tekshiruv.",
        "Birinchi: ulanishni tekshiring. Kabel yoki Vay-Fay ulanganmi, qog'oz bormi, qopqoq yopiqmi?",
        "Ikkinchi: navbatni tozalang. Sozlamalar, printerlar va skanerlar, navbatni ochish, "
        "keyin hammasini bekor qiling.",
        "Uchinchi: printerni o'chiring, o'ttiz soniya kuting va qayta yoqing. Keyin yana chop etib ko'ring.",
        "Saqlab qo'ying! Yordam bermasa, printerni ta'mirlaymiz.",
        OUTRO_VO],
    "13_kartrij_tejash": [
        "Kartrij tez tugayaptimi? Uchta tejash usuli.",
        "Birinchi: tejamkor rejimni yoqing. Chop etish sozlamalarida qoralama rejimini tanlang, hujjatlar uchun yetarli.",
        "Ikkinchi: avval ko'rib chiqing va faqat kerakli sahifalarni chop eting.",
        "Uchinchi: siyohli printerda haftada kamida bitta sahifa chop eting, shunda siyoh qurib qolmaydi.",
        "Saqlab qo'ying! Kartrijni to'ldiramiz.",
        OUTRO_VO],
    "14_telefon_reklama": [
        "Telefonda reklama o'zi chiqaveradimi? Uchta qadam.",
        "Birinchi: shubhali ilovani o'chiring. Sozlamalar, ilovalar. Reklama boshlangan paytda o'rnatilgan "
        "notanish ilovani o'chiring.",
        "Ikkinchi: Xrom sozlamalarida bildirishnomalar bo'limiga kiring va saytlar bildirishnomasini o'chiring.",
        "Uchinchi: Pley Marketda profilni bosing, Pley Protekt bo'limida tekshirish tugmasini bosing.",
        "Saqlab qo'ying! Reklama ketmasa, telefonni tozalaymiz.",
        OUTRO_VO],
    "15_telefon_sekin": [
        "Telefoningiz sekinlashdimi? Uchta oddiy qadam.",
        "Birinchi: tizimni yangilang. Sozlamalar, tizim yangilanishi, yangilash.",
        "Ikkinchi: oylab ochilmagan ilovalarni o'chiring. Ular fonda xotira va batareyani yeydi.",
        "Uchinchi: haftada bir marta telefonni qayta ishga tushiring.",
        "Saqlab qo'ying! Yordam bermasa, proshivka qilamiz.",
        OUTRO_VO],
    "16_wifi_himoya": [
        "Vay-Fay routeringiz himoyalanganmi? Uchta muhim sozlama.",
        "Birinchi: router parolini almashtiring. Brauzerda router manzilini oching. "
        "Standart admin parolini albatta almashtiring.",
        "Ikkinchi: shifrlash turini ve pe a ikki yoki ve pe a uch qilib tanlang. Ochiq tarmoq xavfli.",
        "Uchinchi: ve pe es funksiyasini o'chiring. Begonalar tugma orqali ulana olmaydi.",
        "Saqlab qo'ying! Routerni sozlab beramiz.",
        OUTRO_VO],
    "17_masofaviy_yordam": [
        "Kompyuter muammosi? Ustaga borish shart emas.",
        "Bizga qo'ng'iroq qiling yoki Telegramda yozing, muammoni qisqacha tushuntiring.",
        "Kompyuteringizga masofadan ulanamiz. Vindous va dasturlar o'rnatamiz, xatolarni tuzatamiz.",
        "Muhim qoida: faqat o'zingiz chaqirgan ustaga ruxsat bering. Notanish bank xodimiga ruxsat bermang. "
        "Ish tugagach ulanishni uzing.",
        "Uydan chiqmasdan yordam. Saqlab qo'ying!",
        OUTRO_VO],
    "18_windows_himoya": [
        "Antivirus yoqilganmi? Bir daqiqada tekshiring.",
        "Win va I tugmalarini bosing. Maxfiylik va xavfsizlik, keyin Vindous Sekyuriti bo'limini oching.",
        "Viruslardan himoya bo'limida tez tekshiruvni ishga tushiring.",
        "Vindous Apdeyt bo'limida yangilanishlarni tekshiring. Himoya faqat yangilangan tizimda to'liq ishlaydi.",
        "Original antivirus, bir yil kafolat bilan. Saqlab qo'ying!",
        OUTRO_VO],
    "19_word_tiklash": [
        "Vord fayl saqlanmay yopilib qoldimi? Uni qaytarish mumkin!",
        "Fayl, ma'lumotlar, hujjatni boshqarish, keyin saqlanmagan hujjatlarni tiklash tugmasini bosing.",
        "Endi avtosaqlashni sozlang. Fayl, parametrlar, saqlash. Har bir daqiqada avtosaqlashni yoqing. "
        "Endi ish yo'qolmaydi.",
        "Ofis o'rnatamiz, original litsenziya. Saqlab qo'ying!",
        OUTRO_VO],
})

# ─── Ежедневная серия (10 роликов в день), выпуск 23.11.2026 ───
DAILY_REELS = []

DAILY_REELS.append(dict(slug="20_parol_qoidalari", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="PAROLINGIZ", l2="KUCHLIMI?", sub="3 ta oddiy qoida"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Kamida", h2="12 ta belgi", items=[
        P(0.4, [("123456, ism, tug'ilgan yil", "r")], y=820, arrows=False),
        P(1.4, [("Uzun ibora + raqam + belgi", "g")], y=980, arrows=False)]),
    dict(type="step", t0=8, t1=13, num="2 / 3", h1="Har bir saytga", h2="boshqa parol", items=[
        T(0.4, "Bitta parol o'g'irlansa — hammasi ochiladi", 840, size=46),
        P(1.6, [("Telegram ≠ Pochta ≠ Bank", "g")], y=1000, arrows=False)]),
    dict(type="step", t0=13, t1=18, num="3 / 3", h1="Ikki bosqichli", h2="himoyani yoqing", items=[
        P(0.4, [("Parol + SMS yoki kod", "g")], y=860, arrows=False),
        T(1.4, "Parolni bilsa ham kira olmaydi", 1020)]),
    dict(type="cta", t0=18, top="XAVFSIZLIK", main="Saqlab qo'ying — kerak bo'ladi", ask="Parolingiz qanday?",
         tags="Xavfsizlik • Sozlash • Himoya"),
], caption=f"""Parolingiz kuchlimi? 3 ta oddiy qoida 🔐

1️⃣ Kamida 12 ta belgi: 123456, ism yoki tug'ilgan yil emas — uzun ibora + raqam + belgi
2️⃣ Har bir saytga boshqa parol: bittasi o'g'irlansa, hammasi ochilib qolmaydi
3️⃣ Ikki bosqichli himoyani yoqing: parolni bilsa ham kira olmaydi

🔖 Saqlab qo'ying! Parolingizni oxirgi marta qachon almashtirgansiz? 👇

{CONTACT}

#parol #xavfsizlik {TAGS}"""))

DAILY_REELS.append(dict(slug="21_telegram_himoya", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="TELEGRAMINGIZNI", l2="O'G'IRLASHMASIN!", sub="3 ta sozlama"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Kodni hech kimga", h2="bermang", items=[
        P(0.4, [("Telegram kodi faqat siz uchun", "g")], y=820, arrows=False),
        P(1.6, [("«Kodni ayting» — firibgar", "r")], y=980, arrows=False)]),
    dict(type="step", t0=8, t1=14, num="2 / 3", h1="Ikki bosqichli", h2="parol qo'ying", items=[
        P(0.4, [("Sozlamalar", "n"), ("Maxfiylik va xavfsizlik", "n"), ("Ikki bosqichli tekshiruv", "g")],
          y=800, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Begona qurilmalarni", h2="chiqarib yuboring", items=[
        P(0.4, [("Sozlamalar → Qurilmalar", "n"), ("Boshqa seanslarni tugatish", "g")], y=820, stagger=0.8)]),
    dict(type="cta", t0=19, top="TELEGRAM HIMOYASI", main="Saqlab qo'ying — kerak bo'ladi", ask="Yordam kerakmi?",
         tags="Telefon • Xavfsizlik • Sozlash"),
], caption=f"""Telegram akkauntingizni o'g'irlashmasin! 3 ta sozlama 🔐

1️⃣ Telegram kodini hech kimga bermang — «adashib yubordim, kodni ayting» deganlar firibgar
2️⃣ Sozlamalar → Maxfiylik va xavfsizlik → Ikki bosqichli tekshiruv — qo'shimcha parol qo'ying
3️⃣ Sozlamalar → Qurilmalar → begona qurilma bo'lsa, «Boshqa seanslarni tugatish»

🔖 Saqlab qo'ying va yaqinlaringizga yuboring 👇

{CONTACT}

#telegram #xavfsizlik {TAGS}"""))

DAILY_REELS.append(dict(slug="22_fleshka_yorliq", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="FLESHKADAGI FAYLLAR", l2="YORLIQQA AYLANDIMI?", sub="Bu virus — fayllar joyida"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Yorliqlarni", h2="ochmang", items=[
        P(0.4, [("Yorliqni bosish = virusni ishga tushirish", "r")], y=860, arrows=False)]),
    dict(type="step", t0=8, t1=14, num="2 / 3", h1="Yashirin fayllarni", h2="ko'rsating", items=[
        P(0.4, [("Provodnik", "n"), ("Ko'rinish", "n"), ("Yashirin elementlar ✓", "g")], y=800, stagger=0.8),
        T(3.0, "Fayllaringiz yashiringan, o'chmagan", 1300, col=GREEN, size=48)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Antivirus bilan", h2="tekshiring", items=[
        P(0.4, [("Fleshka → o'ng tugma", "n"), ("Viruslarga tekshirish", "g")], y=820, stagger=0.8)]),
    dict(type="cta", t0=19, top="FAYLLARNI QUTQARAMIZ", main="Saqlab qo'ying — kerak bo'ladi", ask="Yordam kerakmi?",
         tags="Antivirus • Fleshka • Tozalash"),
], caption=f"""Fleshkadagi fayllar yorliqqa aylandimi? Bu virus — fayllaringiz o'chmagan 💾

1️⃣ Yorliqlarni ochmang — har bosishda virus ishga tushadi
2️⃣ Provodnik → Ko'rinish → «Yashirin elementlar» belgisini qo'ying — fayllaringiz ko'rinadi
3️⃣ Fleshkani antivirus bilan tekshiring (o'ng tugma → Viruslarga tekshirish)

🔖 Saqlab qo'ying! O'zingiz uddalay olmasangiz — fayllarni qutqarib, virusni tozalaymiz.
Sizda shunday bo'lganmi? 👇

{CONTACT}

#fleshka #virus {TAGS}"""))

DAILY_REELS.append(dict(slug="23_noutbuk_batareya", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="NOUTBUK ZARYADI", l2="TEZ TUGAYAPTIMI?", sub="3 ta sozlama",
         meter=("Batareya", 0.18, RED)),
    dict(type="step", t0=3, t1=9, num="1 / 3", h1="Energiya tejash", h2="rejimi", items=[
        K(0.4, ["Win", "+", "I"], until=2.4),
        P(1.6, [("Tizim → Quvvat va batareya", "n"), ("Energiya tejash", "g")], y=1000, stagger=0.8)]),
    dict(type="step", t0=9, t1=14, num="2 / 3", h1="Ekran yorqinligini", h2="kamaytiring", items=[
        P(0.4, [("100% → 50–60%", "g")], y=860, arrows=False),
        T(1.4, "Ekran eng ko'p quvvat yeydi", 1020)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Fondagi dasturlarni", h2="yoping", items=[
        K(0.4, ["Ctrl", "+", "Shift", "+", "Esc"], until=2.4),
        P(1.6, [("Keraksiz dastur → Vazifani tugatish", "g")], y=1000, arrows=False)]),
    dict(type="cta", t0=19, meter=("Batareya", 0.18, 0.85, RED, GREEN), ask="Batareya almashtirish kerakmi?",
         tags="Noutbuk • Batareya • Ta'mirlash"),
], caption=f"""Noutbuk zaryadi tez tugayaptimi? 3 ta sozlama 🔋

1️⃣ Win + I → Tizim → Quvvat va batareya → Energiya tejash
2️⃣ Ekran yorqinligini 50–60% ga tushiring — ekran eng ko'p quvvat yeydi
3️⃣ Ctrl + Shift + Esc → keraksiz dasturlarni «Vazifani tugatish»

🔖 Saqlab qo'ying! Yordam bermasa — batareyani tekshiramiz va almashtiramiz.
Noutbukingiz necha soat ishlaydi? 👇

{CONTACT}

#noutbuk #batareya {TAGS}"""))

DAILY_REELS.append(dict(slug="24_kompyuter_ovoz", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="KOMPYUTERDA", l2="OVOZ YO'QMI?", sub="3 ta tekshiruv"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Ovoz belgisini", h2="tekshiring", items=[
        P(0.4, [("Pastki o'ng burchakdagi belgi", "n"), ("O'chirilgan emasmi?", "g")], y=820, stagger=0.8)]),
    dict(type="step", t0=8, t1=14, num="2 / 3", h1="To'g'ri qurilmani", h2="tanlang", items=[
        P(0.4, [("Sozlamalar → Tizim → Ovoz", "n"), ("Chiqish: Karnay / Naushnik", "g")], y=820, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Avtomatik", h2="tuzatish", items=[
        P(0.4, [("Ovoz belgisi → o'ng tugma", "n"), ("Ovoz muammolarini aniqlash", "g")], y=820, stagger=0.8)]),
    dict(type="cta", t0=19, top="OVOZ QAYTDI?", main="Saqlab qo'ying — kerak bo'ladi", ask="Yordam kerakmi?",
         tags="Drayver • Windows • Ta'mirlash"),
], caption=f"""Kompyuterda ovoz yo'qmi? Ustaga borishdan oldin 3 ta tekshiruv 🔈

1️⃣ Pastki o'ng burchakdagi ovoz belgisi — o'chirilgan emasmi
2️⃣ Sozlamalar → Tizim → Ovoz → chiqish qurilmasini to'g'ri tanlang (karnay yoki naushnik)
3️⃣ Ovoz belgisi → o'ng tugma → «Ovoz muammolarini aniqlash»

🔖 Saqlab qo'ying! Yordam bermasa — drayverni o'rnatamiz va sozlaymiz.
Qaysi biri yordam berdi? 👇

{CONTACT}

#kompyuter #windows {TAGS}"""))

DAILY_REELS.append(dict(slug="25_excel_tugmalar", dur=24, scenes=[
    dict(type="hook", t0=0, t1=3, l1="EXCEL'DA", l2="TEZ ISHLANG!", sub="5 ta foydali tugma"),
    key_step(3, 7, "1 / 5", "Ustunlar", "yig'indisi", ["Alt", "+", "="]),
    key_step(7, 11, "2 / 5", "Bugungi", "sana", ["Ctrl", "+", ";"]),
    key_step(11, 15, "3 / 5", "Filtr", "qo'yish", ["Ctrl", "+", "Shift", "+", "L"]),
    key_step(15, 19, "4 / 5", "Jadval oxiriga", "sakrash", ["Ctrl", "+", "↓"]),
    key_step(19, 23, "5 / 5", "Oxirgi amalni", "takrorlash", ["F4"]),
    dict(type="cta", t0=23, top="EXCEL SIRLARI", main="Saqlab qo'ying — kerak bo'ladi", ask="Yana kerakmi?",
         tags="Izohga «EXCEL» deb yozing"),
], caption=f"""Excel'da tez ishlang: 5 ta foydali tugma 📊

1️⃣ Alt + = — ustun yig'indisi (avtosumma)
2️⃣ Ctrl + ; — bugungi sana
3️⃣ Ctrl + Shift + L — filtr qo'yish
4️⃣ Ctrl + ↓ — jadval oxiriga sakrash
5️⃣ F4 — oxirgi amalni takrorlash

🔖 Saqlab qo'ying! Yana kerak bo'lsa, izohga «EXCEL» deb yozing 👇
Office o'rnatish va original litsenziya — 1 yil kafolat bilan.

{CONTACT}

#excel #office {TAGS}"""))

DAILY_REELS.append(dict(slug="26_sms_kod_firibgar", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="SMS KODINI", l2="SO'RASHDIMI?", sub="Bu firibgar!"),
    dict(type="step", t0=3, t1=8, num="1 / 3", h1="Bank kod", h2="so'ramaydi", items=[
        P(0.4, [("«Bank xodimi»: kodni ayting", "r")], y=820, arrows=False),
        P(1.6, [("Bankka o'zingiz qo'ng'iroq qiling", "g")], y=980, arrows=False)]),
    dict(type="step", t0=8, t1=13, num="2 / 3", h1="Havolalarni", h2="tekshiring", items=[
        P(0.4, [("«Yutuq», «bonus», «karta bloklandi»", "r")], y=820, arrows=False),
        T(1.6, "Notanish havolaga karta ma'lumotini kiritmang", 980, size=44)]),
    dict(type="step", t0=13, t1=18, num="3 / 3", h1="Kod — faqat", h2="o'zingiz uchun", items=[
        P(0.4, [("Click, Payme, bank, Telegram", "n")], y=820, arrows=False),
        T(1.4, "Hech kimga aytmang", 980, col=GREEN, size=56)]),
    dict(type="cta", t0=18, top="EHTIYOT BO'LING", main="Yaqinlaringizga yuboring", ask="Sizga ham yozishganmi?",
         tags="Xavfsizlik • Telefon • Himoya"),
], caption=f"""SMS kodini so'rashdimi? Bu firibgar! ⚠️

1️⃣ Bank hech qachon SMS kodni so'ramaydi — «bank xodimi» qo'ng'iroq qilsa, telefonni qo'ying va bankka o'zingiz qo'ng'iroq qiling
2️⃣ «Yutuq», «bonus», «karta bloklandi» degan havolalarga karta ma'lumotini kiritmang
3️⃣ Click, Payme, bank va Telegram kodlari — faqat siz uchun, hech kimga aytmang

🔖 Saqlab qo'ying va ota-onangizga yuboring 👇
Sizga ham shunday yozishganmi?

{CONTACT}

#firibgarlik #xavfsizlik {TAGS}"""))

DAILY_REELS.append(dict(slug="27_telefon_skaner", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="SKANER", l2="SHART EMAS!", sub="Hujjatni telefonda skanerlang"),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Android:", h2="Google Disk", items=[
        P(0.4, [("Google Disk", "n"), ("+ tugmasi", "n"), ("Skanerlash", "g")], y=800, stagger=0.8)]),
    dict(type="step", t0=8.5, t1=14, num="2 / 3", h1="iPhone:", h2="Zametki", items=[
        P(0.4, [("Zametki (Notes)", "n"), ("Kamera belgisi", "n"), ("Hujjatlarni skanerlash", "g")], y=800, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Tayyor", h2="PDF", items=[
        P(0.4, [("Chetlarini to'g'rilang → Saqlash", "g")], y=860, arrows=False),
        T(1.4, "Telegram yoki pochtaga yuboring", 1020)]),
    dict(type="cta", t0=19, top="HUJJATLAR ONLAYN", main="Rezyume — havola profilda", ask="Saqlab qo'ying!",
         tags="Skaner • PDF • Rezyume"),
], caption=f"""Skaner shart emas — hujjatni telefonda skanerlang 📄

1️⃣ Android: Google Disk → «+» → Skanerlash
2️⃣ iPhone: Zametki (Notes) → kamera belgisi → Hujjatlarni skanerlash
3️⃣ Chetlarini to'g'rilang → Saqlash — tayyor PDF ni Telegram yoki pochtaga yuboring

🔖 Saqlab qo'ying! Rezyume va obyektivka ham telefondan — {RESUME_URL} (havola profilda)

{CONTACT}

#skaner #pdf {TAGS}"""))

HOOK_BG.update({"20_parol_qoidalari": ("clip2.mp4", 0.0), "21_telegram_himoya": ("clip5.mp4", 0.0),
                "22_fleshka_yorliq": ("clip1.mp4", 2.0), "23_noutbuk_batareya": ("clip3.mp4", 0.0),
                "24_kompyuter_ovoz": ("clip1.mp4", 0.0), "25_excel_tugmalar": ("clip4.mp4", 7.5),
                "26_sms_kod_firibgar": ("clip5.mp4", 1.0), "27_telefon_skaner": ("clip5.mp4", 0.5)})
for _r in DAILY_REELS:
    brandify(_r)
REELS.extend(DAILY_REELS)

VOICE.update({
    "20_parol_qoidalari": [
        "Parolingiz kuchlimi? Uchta oddiy qoida.",
        "Birinchi: kamida o'n ikkita belgi. Bir, ikki, uch yoki ismingiz emas. Uzun ibora, raqam va belgi qo'shing.",
        "Ikkinchi: har bir saytga boshqa parol qo'ying. Bittasi o'g'irlansa, hammasi ochilib qolmaydi.",
        "Uchinchi: ikki bosqichli himoyani yoqing. Parolni bilsa ham, kira olmaydi.",
        SAVE, OUTRO_VO],
    "21_telegram_himoya": [
        "Telegramingizni o'g'irlashmasin! Uchta sozlama.",
        "Birinchi: kodni hech kimga bermang. Adashib yubordim, kodni ayting, deganlar firibgar.",
        "Ikkinchi: sozlamalar, maxfiylik va xavfsizlik, ikki bosqichli tekshiruv. Qo'shimcha parol qo'ying.",
        "Uchinchi: sozlamalar, qurilmalar. Begona qurilma bo'lsa, boshqa seanslarni tugating.",
        "Saqlab qo'ying va yaqinlaringizga yuboring!",
        OUTRO_VO],
    "22_fleshka_yorliq": [
        "Fleshkadagi fayllar yorliqqa aylandimi? Bu virus, fayllaringiz joyida.",
        "Birinchi: yorliqlarni ochmang. Har bosishda virus ishga tushadi.",
        "Ikkinchi: provodnikda ko'rinish bo'limiga kiring va yashirin elementlarni yoqing. Fayllaringiz ko'rinadi.",
        "Uchinchi: fleshkani antivirus bilan tekshiring.",
        "Uddalay olmasangiz, fayllarni qutqaramiz. Saqlab qo'ying!",
        OUTRO_VO],
    "23_noutbuk_batareya": [
        "Noutbuk zaryadi tez tugayaptimi? Uchta sozlama.",
        "Birinchi: Win va I ni bosing. Tizim, quvvat va batareya, energiya tejash rejimini yoqing.",
        "Ikkinchi: ekran yorqinligini ellik, oltmish foizga tushiring. Ekran eng ko'p quvvat yeydi.",
        "Uchinchi: Kontrol, Shift va Esk ni bosing va keraksiz dasturlarni yoping.",
        "Saqlab qo'ying! Kerak bo'lsa, batareyani almashtiramiz.",
        OUTRO_VO],
    "24_kompyuter_ovoz": [
        "Kompyuterda ovoz yo'qmi? Uchta tekshiruv.",
        "Birinchi: pastki o'ng burchakdagi ovoz belgisini tekshiring. O'chirilgan emasmi?",
        "Ikkinchi: sozlamalar, tizim, ovoz. Chiqish qurilmasini to'g'ri tanlang, karnay yoki naushnik.",
        "Uchinchi: ovoz belgisini o'ng tugma bilan bosing va ovoz muammolarini aniqlashni tanlang.",
        "Saqlab qo'ying! Yordam bermasa, drayverni o'rnatamiz.",
        OUTRO_VO],
    "25_excel_tugmalar": [
        "Eksel'da tez ishlang! Beshta foydali tugma.",
        "Alt va teng: ustun yig'indisi.",
        "Kontrol va nuqtali vergul: bugungi sana.",
        "Kontrol, Shift va El: filtr qo'yish.",
        "Kontrol va pastga strelka: jadval oxiriga sakrash.",
        "Ef to'rt: oxirgi amalni takrorlash.",
        "Saqlab qo'ying! Yana kerak bo'lsa, izohga Eksel deb yozing.",
        OUTRO_VO],
    "26_sms_kod_firibgar": [
        "SMS kodini so'rashdimi? Bu firibgar!",
        "Bank hech qachon kod so'ramaydi. Bank xodimi qo'ng'iroq qilsa, telefonni qo'ying va bankka o'zingiz qo'ng'iroq qiling.",
        "Yutuq, bonus yoki karta bloklandi degan havolalarga karta ma'lumotini kiritmang.",
        "Klik, Peymi, bank va Telegram kodlari faqat siz uchun. Hech kimga aytmang.",
        "Saqlab qo'ying va yaqinlaringizga yuboring!",
        OUTRO_VO],
    "27_telefon_skaner": [
        "Skaner shart emas! Hujjatni telefonda skanerlang.",
        "Androidda: Gugl Disk, plyus tugmasi, keyin skanerlash.",
        "Ayfonda: zametki ilovasi, kamera belgisi, hujjatlarni skanerlash.",
        "Chetlarini to'g'rilang va saqlang. Tayyor pe de ef ni Telegram yoki pochtaga yuboring.",
        "Rezyume ham telefondan. Havola profilda!",
        OUTRO_VO],
})

# ─── Замены 22.11: вместо 21_telegram_himoya (23.11 14:30) и 14_telefon_reklama (29.11 19:00) ───
SWAP_REELS = []
SWAP_REELS.append(dict(slug="28_wifi_qr", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="WI-FI PAROLINI", l2="UNUTDINGIZMI?", sub="Telefondan QR bilan ulashing"),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Android:", h2="Wi-Fi sozlamalari", items=[
        P(0.4, [("Sozlamalar → Wi-Fi", "n"), ("Ulangan tarmoq", "n"), ("Ulashish → QR kod", "g")], y=800, stagger=0.8)]),
    dict(type="step", t0=8.5, t1=14, num="2 / 3", h1="Mehmon telefoni", h2="QR ni skanerlaydi", items=[
        P(0.4, [("Kamera → QR kod", "g")], y=860, arrows=False),
        T(1.4, "Parolni aytish shart emas", 1020)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="iPhone'da", h2="ham bor", items=[
        P(0.4, [("Sozlamalar → Wi-Fi → (i)", "n"), ("Parol — Face ID bilan", "g")], y=820, stagger=0.8)]),
    dict(type="cta", t0=19, top="WI-FI SOZLASH", main="Saqlab qo'ying — kerak bo'ladi", ask="Router sozlash kerakmi?",
         tags="Router • Wi-Fi • Tarmoq"),
], caption=f"""Wi-Fi parolini unutdingizmi? Telefondan QR kod bilan ulashing 📶

1️⃣ Android: Sozlamalar → Wi-Fi → ulangan tarmoq → Ulashish — QR kod va parol chiqadi
2️⃣ Mehmon telefoni kamerasi bilan QR ni skanerlaydi — parolni aytish shart emas
3️⃣ iPhone: Sozlamalar → Wi-Fi → (i) → Parol — Face ID bilan ko'rinadi

🔖 Saqlab qo'ying! Routerni sozlab beramiz.
Siz bu usulni bilarmidingiz? 👇

{CONTACT}

#wifi #telefon {TAGS}"""))

SWAP_REELS.append(dict(slug="29_telefon_batareya", dur=22, scenes=[
    dict(type="hook", t0=0, t1=3, l1="TELEFON ZARYADI", l2="TEZ TUGAYAPTIMI?", sub="3 ta sozlama",
         meter=("Batareya", 0.15, RED)),
    dict(type="step", t0=3, t1=8.5, num="1 / 3", h1="Kim ko'p yeyotganini", h2="ko'ring", items=[
        P(0.4, [("Sozlamalar", "n"), ("Batareya", "n"), ("Ilovalar bo'yicha sarf", "g")], y=800, stagger=0.8)]),
    dict(type="step", t0=8.5, t1=14, num="2 / 3", h1="Yorqinlik va", h2="qorong'i rejim", items=[
        P(0.4, [("Avto-yorqinlik: yoqilgan", "g"), ("Qorong'i rejim", "g")], y=820, arrows=False, gap=150, stagger=0.8)]),
    dict(type="step", t0=14, t1=19, num="3 / 3", h1="Keraksiz", h2="joylashuvni o'chiring", items=[
        P(0.4, [("GPS faqat kerak bo'lganda", "g")], y=860, arrows=False),
        T(1.4, "Fonda doim ishlasa — quvvat ketadi", 1020)]),
    dict(type="cta", t0=19, meter=("Batareya", 0.15, 0.85, RED, GREEN), ask="Batareya eskirganmi?",
         tags="Telefon • Dasturlar • Ta'mirlash"),
], caption=f"""Telefon zaryadi tez tugayaptimi? 3 ta sozlama 🔋

1️⃣ Sozlamalar → Batareya — qaysi ilova ko'p quvvat yeyotganini ko'ring
2️⃣ Avto-yorqinlik va qorong'i rejimni yoqing
3️⃣ Joylashuvni (GPS) faqat kerak bo'lganda yoqing — fonda doim ishlasa, quvvat ketadi

🔖 Saqlab qo'ying! Yordam bermasa — telefon dasturini tekshirib, sozlab beramiz.
Telefoningiz necha soat ishlaydi? 👇

{CONTACT}

#telefon #batareya {TAGS}"""))

HOOK_BG.update({"28_wifi_qr": ("clip2.mp4", 0.0), "29_telefon_batareya": ("clip5.mp4", 1.0)})
for _r in SWAP_REELS:
    brandify(_r)
REELS.extend(SWAP_REELS)
VOICE.update({
    "28_wifi_qr": [
        "Vay-Fay parolini unutdingizmi? Telefondan QR kod bilan ulashing.",
        "Androidda: sozlamalar, Vay-Fay, ulangan tarmoq, keyin ulashish. QR kod va parol chiqadi.",
        "Mehmon telefoni kamera bilan QR kodni skanerlaydi. Parolni aytish shart emas.",
        "Ayfonda ham bor: sozlamalar, Vay-Fay, tarmoq yonidagi belgi, parol. Feys ID bilan ko'rinadi.",
        SAVE, OUTRO_VO],
    "29_telefon_batareya": [
        "Telefon zaryadi tez tugayaptimi? Uchta sozlama.",
        "Birinchi: sozlamalar, batareya. Qaysi ilova ko'p quvvat yeyotganini ko'ring.",
        "Ikkinchi: avtomatik yorqinlik va qorong'i rejimni yoqing.",
        "Uchinchi: joylashuvni faqat kerak bo'lganda yoqing. Fonda doim ishlasa, quvvat ketadi.",
        SAVE, OUTRO_VO],
})
