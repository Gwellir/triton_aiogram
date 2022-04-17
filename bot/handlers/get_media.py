from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.channel_post_form import ChannelPostForm
from bot.constants import ERRORS
from bot.utils import make_state_message


async def get_media(message: Message, state: FSMContext):
    await state.set_state(ChannelPostForm.get_text)
    await state.update_data(dict(has_media=True))
    if not (media_data := (await state.get_data()).get("media")):
        media_data = []
    if message.photo:
        media_data.append(message.photo[-1])
    elif message.video:
        media_data.append(message.video)
    elif message.animation:
        media_data.append(message.animation)

    await state.update_data(media=media_data)

    await message.answer(**(await make_state_message(state)))


async def pass_media(query: CallbackQuery, state: FSMContext):
    await state.set_state(ChannelPostForm.get_text)
    await query.message.answer(**(await make_state_message(state)))


async def wrong_media(message: Message, state: FSMContext):
    await message.answer(**(await make_state_message(state, error=ERRORS.NOT_MEDIA)))
