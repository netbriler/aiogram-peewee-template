from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from aiogram.types import Message

from bot.keyboards.inline import get_language_inline_markup
from loader import dp, _
from models import User


@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    text = _('Привет, {full_name}!\n'
             'Выберите свой язык').format(full_name=user.name)

    await message.answer(text, reply_markup=get_language_inline_markup())


@dp.message_handler(i18n_text='Помощь 🆘', is_admin=True, state='*')
@dp.message_handler(CommandHelp())
async def _help(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAIBR2IvSpW_RM-rKHtq0JtMQeiZ93tAAAIoAAOPC94R1Or-ytaZqY8jBA')
