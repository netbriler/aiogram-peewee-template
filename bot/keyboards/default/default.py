from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from loader import _


def get_default_markup(user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    markup.add(_('Помощь 🆘'))

    if user.is_admin:
        markup.add(_('Экспорт пользователей 📁'))
        markup.add(_('Количество пользователей 👥'))
        markup.add(_('Количество активных пользователей 👥'))

    if len(markup.keyboard) < 1:
        return ReplyKeyboardRemove()

    return markup
