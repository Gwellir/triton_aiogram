from aiogram import F, Router

from bot.channel_post_form import ChannelPostForm
from bot.constants import QUERIES
from bot.handlers.check_data import post_channel
from bot.handlers.common import any_message, callback_process, on_post
from bot.handlers.get_media import get_media, pass_media, wrong_media
from bot.handlers.get_text import get_text, wrong_text
from bot.handlers.start import dialog_start
from config import ALLOWED_USERS


def add_handlers(router: Router) -> Router:

    router.message.register(
        get_media, ChannelPostForm.get_media, F.photo | F.video | F.animation
    )
    router.callback_query.register(
        pass_media, ChannelPostForm.get_media, F.data == QUERIES.CONTINUE
    )
    router.message.register(wrong_media, ChannelPostForm.get_media)

    router.message.register(get_text, ChannelPostForm.get_text, F.text)
    router.message.register(wrong_text, ChannelPostForm.get_text)

    router.callback_query.register(
        post_channel, ChannelPostForm.check_data, F.data == QUERIES.FINALIZE
    )

    if ALLOWED_USERS:
        router.callback_query.register(
            dialog_start,
            F.data == QUERIES.RESTART | F.from_user.username.in_(ALLOWED_USERS),
        )
        router.message.register(any_message, F.from_user.username.in_(ALLOWED_USERS))
    else:
        router.callback_query.register(dialog_start, F.data == QUERIES.RESTART)
        router.message.register(any_message)
    router.callback_query.register(callback_process)

    router.channel_post.register(on_post)

    return router
