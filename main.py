from database import get_connection
from urllib.parse import urlparse
from analyzer import yuksek_etkilesim_mi, haber_hash
from feeds import FEEDS
import feedparser

def haberleri_cek():
    conn = get_connection()
    c = conn.cursor()

    for kaynak, feed_url in FEEDS.items():
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            baslik = entry.title
            ozet = entry.get("summary", "")
            link = entry.link
            h = haber_hash(baslik, link)

            try:
                c.execute("""
                INSERT INTO haberler (baslik, ozet, link, kaynak, yayinci, hash)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (baslik, ozet, link, kaynak, yayinci, h))

            except:
                pass  # aynı haber → geç

    conn.commit()
    conn.close()

if __name__ == "__main__":
    haberleri_cek()
