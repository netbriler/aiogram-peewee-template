from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand

from loader import _, bot, i18n
from .default import get_default_commands


def get_admin_commands(lang: str = 'en') -> list[BotCommand]:
    commands = get_default_commands(lang)

    commands.extend([
        BotCommand('/export_users', _('export users to csv', locale=lang)),
        BotCommand('/count_users', _('count users who contacted the bot', locale=lang)),
        BotCommand('/count_active_users', _('count active users (who didn\'t block the bot)', locale=lang)),
    ])

    return commands


async def set_admin_commands(user_id: int, commands_lang: str):
    await bot.set_my_commands(get_admin_commands(commands_lang), scope=BotCommandScopeChat(user_id))
