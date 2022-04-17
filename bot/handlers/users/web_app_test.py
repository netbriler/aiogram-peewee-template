import time

from aiogram.types import Message, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from loader import dp
from models import User


@dp.message_handler(commands=['web_app_test'])
async def _web_app_init(message: Message, user: User):
    web_app_uri = 'https://htmlpreview.github.io/?https://raw.githubusercontent.com/' \
                  'netbriler/aiogram-sqlalchemy-template/master/web_app_echo.html?time=' + str(time.time())

    web_app = WebAppInfo(url=web_app_uri)

    await bot.set_chat_menu_button(message.chat.id, MenuButtonWebApp(text='Menu', web_app=web_app))

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Menu', web_app=web_app)
    )

    await message.answer(web_app_uri)

    await message.answer('Web app test', reply_markup=markup)


@dp.message_handler(content_types=[ContentTypes.WEB_APP_DATA])
async def _web_app(message: Message, user: User):
    print(message)

    await message.answer(message.web_app_data.data)
