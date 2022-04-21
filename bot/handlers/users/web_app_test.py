import time

from aiogram.types import Message, ContentTypes, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, MenuButtonWebApp

from loader import dp, bot
from models import User


@dp.message_handler(commands=['web_app_test'])
async def _web_app_init(message: Message, user: User):
    web_app_uri = 'https://aiogram-sqlalchemy-template.vercel.app/web_app_echo.html?time=' + str(time.time())

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('Menu', web_app=WebAppInfo(url=web_app_uri + '&keyboard_button=1'))
    )

    await message.answer('Web app test', reply_markup=markup)
    await bot.set_chat_menu_button(message.chat.id, MenuButtonWebApp(text='Menu', web_app=WebAppInfo(url=web_app_uri)))


@dp.message_handler(content_types=[ContentTypes.WEB_APP_DATA])
async def _web_app(message: Message, user: User):
    text = f'Button text: {message.web_app_data.button_text}\n\n' \
           f'Data:\n<pre>{message.web_app_data.data}</pre>'

    await message.answer(text)
