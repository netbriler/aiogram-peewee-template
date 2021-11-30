from aiogram import executor

from loader import dp, bot, config
from utils.db.base import create_async_database
from utils.misc.logging import logger


async def on_startup(dispatcher):
    logger.info('Bot startup')

    bot['session'] = await create_async_database()

    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'Бот успешно запущен')


if __name__ == '__main__':
    from middlewares import setup_middleware
    import filters
    import handlers

    setup_middleware(dp)

    executor.start_polling(dp, on_startup=on_startup)
