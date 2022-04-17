from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.channel_post_form import ChannelPostForm
from bot.constants import BUTTON_PRESETS, ERRORS, MAX_TEXT_LENGTH
from bot.utils import make_state_message, send_message


async def get_text(message: Message, state: FSMContext):
    has_media = (await state.get_data()).get("has_media")
    if has_media and len(message.text) >= MAX_TEXT_LENGTH:
        await message.answer(
            **(await make_state_message(state, error=ERRORS.TEXT_TOO_LONG))
        )
        return

    await state.update_data(dict(text=message.text))
    await state.set_state(ChannelPostForm.check_data)

    buttons = [[InlineKeyboardButton(**btn) for btn in row] for row in BUTTON_PRESETS]
    await state.update_data(buttons=buttons)
    data = await state.get_data()

    await send_message(data, message.chat.id)

    await message.answer(**(await make_state_message(state)))


async def wrong_text(message: Message, state: FSMContext):
    await message.answer(**(await make_state_message(state, error=ERRORS.NOT_TEXT)))
