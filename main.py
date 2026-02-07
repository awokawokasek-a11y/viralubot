from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "ubot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    print("🔥 Ubot starting...")
    app.run()
