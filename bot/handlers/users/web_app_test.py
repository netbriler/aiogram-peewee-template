import time

from aiogram.dispatcher.filters import RegexpCommandsFilter
from aiogram.types import Message, ContentTypes, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, MenuButtonWebApp

from loader import dp, bot
from models import User


@dp.message_handler(RegexpCommandsFilter(regexp_commands=['web_app_test(\shttps:(.*))?']))
async def _web_app_init(message: Message, regexp_command):
    web_app_uri = regexp_command.group(1).strip() if regexp_command.group(1) \
        else 'https://aiogram-peewee-template.vercel.app/web_app_echo.html'
    web_app_uri += '?time=' + str(time.time())

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
