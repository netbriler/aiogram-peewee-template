from aiogram import executor

from loader import dp, bot, config
from models.base import create_async_database
from utils.misc.logging import logger


async def on_startup(dispatcher):
    logger.info('Bot startup')

    bot['session'] = await create_async_database()

    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'Бот успешно запущен')


if __name__ == '__main__':
    from bot.middlewares import setup_middleware
    from bot import filters, handlers

    setup_middleware(dp)

    executor.start_polling(dp, on_startup=on_startup)
