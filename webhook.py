import logging

from aiogram.utils.executor import start_webhook

from loader import dp, bot, config
from utils.db.base import create_async_database
from utils.misc.logging import logger

logging.basicConfig(level=logging.INFO)

# webhook settings
WEBHOOK_HOST = config.WEBHOOK_HOST
WEBHOOK_PATH = config.WEBHOOK_PATH
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8000


async def on_startup(dp):
    logger.info('Bot startup')
    logger.info(f'{WEBHOOK_URL=}')

    await bot.set_webhook(WEBHOOK_URL)

    bot['session'] = await create_async_database()

    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'Бот успешно запущен')


async def on_shutdown(dp):
    logger.warning('Shutting down..')

    await bot.delete_webhook()

    await dp.storage.close()
    await dp.storage.wait_closed()

    logger.warning('Bye!')


if __name__ == '__main__':
    from middlewares import setup_middleware
    import filters
    import handlers

    setup_middleware(dp)

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
