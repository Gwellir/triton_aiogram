import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

import config
from bot.router import add_handlers


async def main():
    bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()

    dp = Dispatcher(storage)

    form_router = Router()
    add_handlers(form_router)
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
