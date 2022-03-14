from aiogram.types import ReplyKeyboardMarkup


def get_default_markup(user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    if user.is_admin:
        markup.add('Экспорт пользователей 📁')
        markup.add('Количество пользователей 👥')
        markup.add('Количество активных пользователей 👥')

    return markup
