from aiogram.types import Message

from bot.keyboards.default import get_default_markup
from loader import dp, _
from models import User


@dp.message_handler(state='*')
async def _default_menu(message: Message, user: User):
    await message.answer(_('Выберите действие в меню 👇'), reply_markup=get_default_markup(user))
