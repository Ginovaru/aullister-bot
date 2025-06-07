import requests

BOT_TOKEN = "123456789:ABCdefGHI_jklMNOpqrSTUvwxYZ"
CHAT_ID = "7720244170"

def send_notification(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    print(response.text)

send_notification("✅ Notifica di test: il bot funziona!")
