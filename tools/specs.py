"""Контент-план: 8 Reels для @qorovulbozor_uz (спецификации видео + подписи)."""
from reelkit import RED, GREEN, WHITE

TAGS = "#kompyuterustasi #qorovulbozor #buxoro"
CONTACT = "Kompyuter ta'mirlash, Windows o'rnatish, litsenziya — Green IT, Qorovulbozor\n📞 +998 91 448 23 88"

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
], caption=f"""Rezyume 5 daqiqada — telefondan, onlayn 📄

1️⃣ green-it-service.uz/resume saytiga kiring (havola profilda)
2️⃣ Ma'lumotlaringizni to'ldiring
3️⃣ Tayyor PDF ni yuklab oling — chop etishga tayyor

Ma'lumotnoma (obyektivka) formati ham bor. To'lov: Click / Payme.
Savol bo'lsa — izohda yozing 👇

{CONTACT}

#rezyume #obyektivka {TAGS}"""))

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
