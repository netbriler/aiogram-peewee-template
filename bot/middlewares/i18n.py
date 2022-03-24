"""
- Собираем все текста с проекта
pybabel extract --input-dirs=. -o data/locales/bot.pot --project=bot

- Создаем файлы с переводами на разные языки
pybabel init -i data/locales/bot.pot -d data/locales -D bot -l en
pybabel init -i data/locales/bot.pot -d data/locales -D bot -l ru
pybabel init -i data/locales/bot.pot -d data/locales -D bot -l uk

- После того как все текста переведены, нужно скомпилировать все переводы
pybabel compile -d data/locales -D bot --statistics

pybabel update -i data/locales/bot.pot -d data/locales -D bot

"""

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import Message

from data.config import I18N_DOMAIN, LOCALES_DIR


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: list[Message, dict[str]]):
        *_, data = args
        user = data['user']

        return user.language

    def set_user_locale(self, locale: str):
        self.ctx_locale.set(locale)

    async def trigger(self, action, args):
        if 'update' not in action and 'error' not in action and action.startswith('process'):
            locale = await self.get_user_locale(action, args)
            self.set_user_locale(locale)
            return True


i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
