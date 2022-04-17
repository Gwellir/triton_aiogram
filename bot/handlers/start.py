from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.channel_post_form import ChannelPostForm
from bot.utils import make_state_message


async def dialog_start(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(ChannelPostForm.get_media)
    await query.answer()
    await query.message.answer(**(await make_state_message(state)))
