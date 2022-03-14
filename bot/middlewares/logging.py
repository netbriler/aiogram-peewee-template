from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, InlineQuery, CallbackQuery

from utils.misc.logging import logger


class LoggingMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        if message.content_type == 'text':
            logger.debug(f'Received message [ID:{message.message_id}] from user [{message.from_user.id}] '
                         f'text "{message.text}"')

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict):
        logger.debug(f'Received inline query [query:{inline_query.query}] from user [ID:{inline_query.from_user.id}]')

    @staticmethod
    async def on_pre_process_callback_query(callback_query: CallbackQuery, data: dict):
        logger.debug(f'Received callback query [data:"{callback_query.data}"] '
                     f'from user [ID:{callback_query.from_user.id}] '
                     f'for message [ID:{callback_query.message.message_id}] '
                     f'in chat [ID:{callback_query.message.chat.id}]')