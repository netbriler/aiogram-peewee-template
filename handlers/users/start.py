from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from keyboards.inline import get_language_inline_markup
from loader import dp, _
from models import User


@dp.message_handler(CommandStart())
async def bot_start(message: Message, user: User):
    text = _('Привет, {full_name}!\n'
             'Выбери свой язык').format(full_name=user.name)

    await message.answer(text, reply_markup=get_language_inline_markup())
