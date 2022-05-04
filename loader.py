from aiogram import Bot, Dispatcher, types
from peewee import SqliteDatabase, PostgresqlDatabase

from bot.middlewares.i18n import i18n
from data import config
from utils.telegram_test_server import TELEGRAM_TEST

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

if config.TELEGRAM_TEST_SERVER:
    bot.server = TELEGRAM_TEST

if config.REDIS_HOST and config.REDIS_PORT:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2

    storage = RedisStorage2(config.REDIS_HOST, config.REDIS_PORT, db=config.REDIS_DB)
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

    storage = MemoryStorage()

if config.DB_USER and config.DB_PASSWORD and config.DB_HOST and config.DB_PORT and config.DB_NAME:
    database = PostgresqlDatabase(config.DB_NAME, user=config.DB_USER, password=config.DB_PASSWORD,
                                  host=config.DB_HOST, port=config.DB_PORT)
else:
    database = SqliteDatabase(f'{config.DIR}/database.sqlite3')

dp = Dispatcher(bot, storage=storage, run_tasks_by_default=True)

_ = i18n.gettext
