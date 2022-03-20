from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.channel_post_form import ChannelPostForm
from bot.utils import make_state_message


async def callback_process(query: CallbackQuery, state: FSMContext):
    await query.answer()


async def any_message(message: Message, state: FSMContext):
    await state.set_state(ChannelPostForm.start)
    await message.answer(**(await make_state_message(state)))
