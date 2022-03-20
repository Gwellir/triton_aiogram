from aiogram.dispatcher.filters.state import State, StatesGroup


class ChannelPostForm(StatesGroup):
    start = State()
    welcome = State()
    get_media = State()
    get_text = State()
    add_buttons = State()
    check_data = State()
    done = State()
