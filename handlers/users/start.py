from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from keyboards.inline import get_language_inline_markup
from loader import dp, _


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    text = _('Привет, {full_name}!\n'
             'Выбери свой язык').format(full_name=message.from_user.full_name)

    await message.answer(text, reply_markup=get_language_inline_markup())


@dp.message_handler()
async def all(message: Message):
    print(message.html_text)
    await message.answer(message.html_text)
