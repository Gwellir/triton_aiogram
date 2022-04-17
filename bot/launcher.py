from aiogram import Bot, Dispatcher, Router
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from bot.router import add_handlers
import config


def setup_bot():
    bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(storage)

    form_router = Router()
    add_handlers(form_router)
    dp.include_router(form_router)

    return bot, dp
