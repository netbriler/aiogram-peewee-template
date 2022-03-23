from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery

from services.users import get_or_create_user


class UsersMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict[str]):
        if 'channel_post' in message or message.chat.type != 'private':
            raise CancelHandler()

        await message.answer_chat_action('typing')

        user = message.from_user

        session = data['session'] = message.bot.get('session')
        data['user'] = await get_or_create_user(session, user.id, user.full_name, user.username, user.language_code)

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        user = callback_query.from_user

        session = data['session'] = callback_query.bot.get('session')
        data['user'] = await get_or_create_user(session, user.id, user.full_name, user.username, user.language_code)

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        user = inline_query.from_user

        session = data['session'] = inline_query.bot.get('session')
        data['user'] = await get_or_create_user(session, user.id, user.full_name, user.username, user.language_code)
