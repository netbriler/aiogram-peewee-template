"""
- Собираем все текста с проекта
pybabel extract --input-dirs=. -o data/locales/bot.pot --project=bot

- Создаем файлы с переводами на разные языки
pybabel init -i data/locales/bot.pot -d locales -D bot -l en
pybabel init -i data/locales/bot.pot -d locales -D bot -l ru
pybabel init -i data/locales/bot.pot -d locales -D bot -l uk

- После того как все текста переведены, нужно скомпилировать все переводы
pybabel compile -d locales -D bot
"""

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data.config import I18N_DOMAIN, LOCALES_DIR
from services.users import get_or_create_user


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action, args):
        current_telegram_user = types.User.get_current()

        user = await get_or_create_user(args[0].bot.get('session'), current_telegram_user.id,
                                        current_telegram_user.full_name, current_telegram_user.username,
                                        current_telegram_user.language_code)

        return user.language


i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
