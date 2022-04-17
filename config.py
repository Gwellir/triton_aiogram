import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent
# load ENV
dotenv_file = BASE_DIR / ".env"
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

DEBUG = bool(int(os.getenv("DEBUG")))

if DEBUG:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_TEST")
    CHANNEL_ID = os.getenv("TESTING_CHANNEL_ID")
else:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHANNEL_ID = os.getenv("LIVE_CHANNEL_ID")

DEV_TG_ID = os.getenv("DEV_TG_ID")

ALLOWED_USERS = []

WEBHOOK_ADDRESS = os.getenv("WEBHOOK_ADDRESS")
WEBHOOK_PORT = int(os.getenv("WEBHOOK_PORT"))
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")

USE_PROXY = os.getenv("USE_PROXY")