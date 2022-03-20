from aiogram import F, Router

from bot.channel_post_form import ChannelPostForm
from bot.constants import QUERIES
from bot.handlers.add_buttons import (
    buttons_done,
    get_buttons_from_entities,
    get_buttons_from_query,
    wrong_buttons,
)
from bot.handlers.check_data import post_channel
from bot.handlers.common import any_message, callback_process
from bot.handlers.get_media import get_media, pass_media, wrong_media
from bot.handlers.get_text import get_text, wrong_text
from bot.handlers.start import dialog_start
from bot.utils import check_entities_have_link


def add_handlers(router: Router) -> Router:
    router.callback_query.register(dialog_start, F.data == QUERIES.RESTART)

    router.message.register(
        get_media, ChannelPostForm.get_media, F.photo | F.video | F.animation
    )
    router.callback_query.register(
        pass_media, ChannelPostForm.get_media, F.data == QUERIES.CONTINUE
    )
    router.message.register(wrong_media, ChannelPostForm.get_media)

    router.message.register(get_text, ChannelPostForm.get_text, F.text)
    router.message.register(wrong_text, ChannelPostForm.get_text)

    router.message.register(
        get_buttons_from_entities,
        ChannelPostForm.add_buttons,
        F.entities,
        F.entities.func(check_entities_have_link),
    )
    router.message.register(wrong_buttons, ChannelPostForm.add_buttons)
    router.callback_query.register(
        buttons_done, ChannelPostForm.add_buttons, F.data == QUERIES.CONTINUE
    )
    router.callback_query.register(get_buttons_from_query, ChannelPostForm.add_buttons)

    router.callback_query.register(
        post_channel, ChannelPostForm.check_data, F.data == QUERIES.FINALIZE
    )

    router.message.register(any_message)
    router.callback_query.register(callback_process)

    return router
