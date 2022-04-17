import asyncio
import logging
import sys

import config
from bot.launcher import setup_bot


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

bot, dp = setup_bot()

asyncio.run(bot.set_webhook(f"{config.WEBHOOK_ADDRESS}{config.WEBHOOK_PATH}"))
