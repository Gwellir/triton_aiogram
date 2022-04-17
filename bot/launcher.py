from aiogram import Bot, Dispatcher, Router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from bot.router import add_handlers
import config


def setup_bot():
    kwargs = {}
    if config.USE_PROXY:
        kwargs["session"] = AiohttpSession(proxy=config.USE_PROXY)

    bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode="HTML", **kwargs)
    storage = MemoryStorage()
    dp = Dispatcher(storage)

    form_router = Router()
    add_handlers(form_router)
    dp.include_router(form_router)

    return bot, dp
