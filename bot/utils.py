from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.methods import SendAnimation, SendMessage, SendPhoto, SendVideo
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    MessageEntity,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from bot.constants import DRAFTS


def check_entities_have_link(e: list[MessageEntity]):
    return [key for key in e if key.type in ["url", "text_link"]]


async def get_state_name(state: FSMContext):
    full_name: str = await state.get_state()
    form, name = full_name.split(":")
    return form, name


async def make_state_message(
    state: FSMContext,
    buttons: list = None,
    inline_buttons: list = None,
    error: str = None,
    done: str = None,
) -> dict | None:
    _, name = await get_state_name(state)
    data = DRAFTS.get(name)

    text = data.get("text")
    if error:
        modify = data.get("mods")["error"][error]
        text = f"<pre>{modify}</pre>\n\n{text}"
    elif done:
        modify = data.get("mods").get("done").format(done)
        text = f"{modify}\n\n{text}"
    msg_data = dict(text=text)

    markup = None
    markup_data = []
    if inline_buttons:
        markup_data = inline_buttons

    if keyboard := data.get("inline_keyboard"):
        markup_data.extend(
            [[InlineKeyboardButton(**btn) for btn in row] for row in keyboard]
        )
        markup = InlineKeyboardBuilder(markup_data).as_markup()
    elif keyboard := data.get("reply_keyboard"):
        markup_data.extend([[KeyboardButton(**btn) for btn in row] for row in keyboard])
        markup = ReplyKeyboardBuilder(markup_data).as_markup()

    if markup:
        msg_data.update(reply_markup=markup)

    return msg_data


async def send_message(data: dict, chat_id) -> Message:
    params = dict(
        chat_id=chat_id,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=data.get("buttons"),
        ),
    )
    text = data.get("text")
    if photo := data.get("photo"):
        msg = await SendPhoto(
            caption=text,
            photo=photo.file_id,
            **params,
        )
    elif video := data.get("video"):
        msg = await SendVideo(
            caption=text,
            video=video.file_id,
            **params,
        )
    elif animation := data.get("animation"):
        msg = await SendAnimation(
            caption=text,
            animation=animation.file_id,
            **params,
        )
    else:
        msg = await SendMessage(
            text=text,
            **params,
        )

    return msg
