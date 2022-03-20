from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

from bot.channel_post_form import ChannelPostForm
from bot.constants import BUTTON_PRESETS, ERRORS
from bot.utils import make_state_message, send_message


async def get_buttons_from_entities(message: Message, state: FSMContext):
    btn_data = None
    for e in message.entities:
        if e.type == "url":
            url = message.text[e.offset : e.offset + e.length]
            text = message.text.replace(url, "").strip()
            if not text:
                text = "ССЫЛКА"
        elif e.type == "text_link":
            url = e.url
            text = message.text[e.offset : e.offset + e.length]
        else:
            continue
        btn_data = {
            "text": text,
            "url": url,
        }

    btn_list = [
        [InlineKeyboardButton(text=BUTTON_PRESETS[btn].get("text"), callback_data=btn)]
        for btn in BUTTON_PRESETS.keys()
    ]
    # btn_list.append([KeyboardButton(text="Далее", callback_data="continue")])

    buttons = (await state.get_data()).get("buttons")
    btn = InlineKeyboardButton(**btn_data)
    buttons.append([btn])
    await state.update_data(dict(buttons=buttons))
    btn_text = f"<a href='{url}'>{text}</a>"
    await message.answer(
        **(await make_state_message(state, inline_buttons=btn_list, done=btn_text))
    )


async def wrong_buttons(message: Message, state: FSMContext):

    await message.answer(**(await make_state_message(state, error=ERRORS.NOT_LINK)))


async def buttons_done(query: CallbackQuery, state: FSMContext):
    await query.answer()

    data = await state.get_data()
    await send_message(data, query.message.chat.id)

    await state.set_state(ChannelPostForm.check_data)
    await query.message.answer(**(await make_state_message(state)))


async def get_buttons_from_query(query: CallbackQuery, state: FSMContext):

    await query.answer()
    buttons = (await state.get_data()).get("buttons")
    if btn_data := BUTTON_PRESETS.get(query.data):
        btn = InlineKeyboardButton(**btn_data)
        buttons.append([btn])
        await state.update_data(dict(buttons=buttons))
        btn_list = [
            [
                InlineKeyboardButton(
                    text=BUTTON_PRESETS[btn].get("text"), callback_data=btn
                )
            ]
            for btn in BUTTON_PRESETS.keys()
        ]
        await query.message.answer(
            **(
                await make_state_message(
                    state, inline_buttons=btn_list, done=btn_data.get("text")
                )
            )
        )
    await query.answer(
        "Наберите сообщение со ссылкой и описанием,"
        "либо нажмите одну из готовых кнопок!"
    )
