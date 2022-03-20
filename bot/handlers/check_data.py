from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import config
from bot.channel_post_form import ChannelPostForm
from bot.utils import make_state_message, send_message


async def post_channel(query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await send_message(data, config.TESTING_CHANNEL_ID)
    await state.set_state(ChannelPostForm.done)
    await query.message.answer(**(await make_state_message(state)))
