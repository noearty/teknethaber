from database import get_connection
import asyncio
import sqlite3
from telegram import Bot
import time

TOKEN="8466804470:AAFSU53zU-4jdQAAr8V2O8uz3MUEWclHpEc"
CHAT_ID="@teknethaber"

bot = Bot(token=TOKEN)

async def gonderilecek_haber_var_mi():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT id, baslik, ozet, link
        FROM haberler
        WHERE gonderildi = 0
        LIMIT 1
    """)

    haber = c.fetchone()

    if haber:
        haber_id, baslik, ozet, link = haber

        mesaj = f"📰 *{baslik}*\n\n{ozet}\n\n🔗 {link}"

        await bot.send_message(
            chat_id=CHAT_ID,
            text=mesaj,
            parse_mode="Markdown"
        )

        c.execute("UPDATE haberler SET gonderildi = 1 WHERE id = ?", (haber_id,))
        conn.commit()

        print("✅ Haber gönderildi")
    else:
        print("⏳ Gönderilecek haber yok")

    conn.close()

async def main_loop():
    print("🤖 Telegram bot başlatıldı...")
    while True:
        await gonderilecek_haber_var_mi()
        await asyncio.sleep(300)  # 5 dakika

if __name__ == "__main__":
    asyncio.run(main_loop())
