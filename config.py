import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent
# load ENV
dotenv_file = BASE_DIR / ".env"
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TESTING_CHANNEL_ID = os.getenv("TESTING_CHANNEL_ID")

DEV_TG_ID = os.getenv("DEV_TG_ID")

ALLOWED_USERS = []
