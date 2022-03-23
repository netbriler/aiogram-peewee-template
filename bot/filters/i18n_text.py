from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from loader import i18n, _


class I18nText(BoundFilter):
    key = 'i18n_text'

    def __init__(self, i18n_text):
        self.i18n_text = i18n_text

    async def check(self, message):
        if not isinstance(message, Message):
            return False

        available = [self.i18n_text]
        for locale in i18n.available_locales:
            available.append(_(self.i18n_text, locale=locale))

        return message.text in available
