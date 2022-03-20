from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, Message

from bot.channel_post_form import ChannelPostForm
from bot.constants import BUTTON_PRESETS, ERRORS, MAX_TEXT_LENGTH
from bot.utils import make_state_message


async def get_text(message: Message, state: FSMContext):
    has_media = (await state.get_data()).get("has_media")
    if has_media and len(message.text) >= MAX_TEXT_LENGTH:
        await message.answer(**(await make_state_message(state, error=ERRORS.TEXT_TOO_LONG)))
        return

    await state.set_state(ChannelPostForm.add_buttons)
    await state.update_data(dict(text=message.text))
    btn_list = [
        [InlineKeyboardButton(text=BUTTON_PRESETS[btn].get("text"), callback_data=btn)]
        for btn in BUTTON_PRESETS.keys()
    ]
    await message.answer(**(await make_state_message(state, inline_buttons=btn_list)))
    await state.update_data(dict(buttons=[]))


async def wrong_text(message: Message, state: FSMContext):
    await message.answer(**(await make_state_message(state, error=ERRORS.NOT_TEXT)))
