import time
import random
import requests

# === CONFIG ===
TELEGRAM_TOKEN = '6674038496:AAH1Qki_dOsWR7xS1-bkKzFDa6JIVCrRLy0'
CHAT_ID = '7720244170'

# Messaggi base
greetings = [
    "Buongiorno, scarafaggio. Cosa devi combinare oggi?",
    "Alzati, parassita. Elenca le tue pseudo-attività giornaliere.",
    "Ancora vivo? Bene. Allora dimmi cosa pensi di realizzare oggi (spoiler: poco)."
]

insults_if_silent = [
    "Silenzio stampa? Tipico dei mediocri.",
    "Il nulla cosmico è più loquace di te.",
    "Neanche una risposta? Già stanco dalla vita?"
]

judgment_replies = [
    "Wow, puntiamo in alto oggi... per un bradipo sedato.",
    "Interessante. Ma non basta a salvarti dalla mediocrità.",
    "Apprezzo l'impegno, ma resta un fallimento annunciato.",
    "Almeno ci provi. È già qualcosa. Pochissimo, ma qualcosa."
]

# === FUNZIONI ===
def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

# === LOOP ===
while True:
    msg = random.choice(greetings)
    send_message(msg)

    time.sleep(1200)  # 20 minuti
    send_message(random.choice(insults_if_silent))
    time.sleep(86400 - 1200)  # 24h - 20min
