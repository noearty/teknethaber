import hashlib

ONEMLI_KELIMELER = [
    "son dakika", "açıklama", "karar", "savaş", "operasyon",
    "israil", "gazze", "rusya", "ukrayna",
    "erdoğan", "bakan", "meclis", "yasa",
    "ekonomi", "dolar", "enflasyon", "faiz",
    "deprem", "afet", "öldü", "yaralı"
]

CLICKBAIT_KELIMELER = [
    "şok", "inanılmaz", "bunu kimse beklemiyordu",
    "bakın ne oldu", "görenler şaştı"
]

def yuksek_etkilesim_mi(baslik, ozet):
    metin = (baslik + " " + ozet).lower()
    puan = 0

    for k in ONEMLI_KELIMELER:
        if k in metin:
            puan += 2

    for k in CLICKBAIT_KELIMELER:
        if k in metin:
            puan -= 3

    if len(baslik) > 120:
        puan -= 1

    return puan >= 3


def haber_hash(baslik, link):
    veri = (baslik + link).encode("utf-8")
    return hashlib.sha256(veri).hexdigest()
