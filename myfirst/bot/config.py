from dotenv import load_dotenv
import os

load_dotenv(".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SEND_TO_ID = os.getenv("SEND_TO_ID")