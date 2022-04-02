from aiogram import Dispatcher
from aiogram import executor

from bot.commands import set_default_commands
from loader import dp, bot, config
from models.base import create_async_database
from utils.misc.logging import logger


async def on_startup(dispatcher: Dispatcher):
    logger.info('Bot startup')

    bot['session'] = await create_async_database()

    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'bot started')

    await set_default_commands()


async def on_shutdown(dispatcher: Dispatcher):
    logger.warning('Shutting down..')

    await dp.storage.close()
    await dp.storage.wait_closed()

    await dp.bot.get('session').close()

    logger.warning('Bye!')


if __name__ == '__main__':
    from bot.middlewares import setup_middleware
    from bot import filters, handlers

    setup_middleware(dp)

    executor.start_polling(dp, on_startup=on_startup)
