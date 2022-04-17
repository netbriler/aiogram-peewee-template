from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, InlineQuery, CallbackQuery, WebAppData

from utils.misc.logging import logger


class LoggingMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict[str]):
        if message.content_type == 'text':
            logger.debug(f'Received message [ID:{message.message_id}] from user [ID:{message.from_user.id}] '
                         f'in chat [ID:{message.chat.id}] text "{message.text}"')
        elif message.content_type == 'web_app_data':
            logger.debug(f'Received web app data [ID:{message.message_id}] from user [ID:{message.from_user.id}] '
                         f'in chat [ID:{message.chat.id}] data "{message.web_app_data}"')

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        logger.debug(f'Received callback query [data:"{callback_query.data}"] '
                     f'from user [ID:{callback_query.from_user.id}] '
                     f'for message [ID:{callback_query.message.message_id}] '
                     f'in chat [ID:{callback_query.message.chat.id}]')

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        logger.debug(f'Received inline query [query:{inline_query.query}] from user [ID:{inline_query.from_user.id}]')
