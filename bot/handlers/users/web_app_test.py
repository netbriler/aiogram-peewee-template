import time

from aiogram.types import Message, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, \
    MenuButtonWebApp

from loader import dp, bot
from models import User


@dp.message_handler(commands=['web_app_test'])
async def _web_app_init(message: Message, user: User):
    web_app_uri = 'https://aiogram-sqlalchemy-template.vercel.app/web_app_echo.html?time=' + str(time.time())

    web_app = WebAppInfo(url=web_app_uri)

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Menu', web_app=web_app)
    )

    await message.answer(web_app_uri)
    await message.answer('Web app test', reply_markup=markup)
    await bot.set_chat_menu_button(message.chat.id, MenuButtonWebApp(text='Menu', web_app=web_app))


@dp.message_handler(content_types=[ContentTypes.WEB_APP_DATA])
async def _web_app(message: Message, user: User):
    await message.answer(message.web_app_data)
