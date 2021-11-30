from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_language_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('🇺🇸 English', callback_data='lang_en'))
    markup.add(InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_ru'))
    markup.add(InlineKeyboardButton('🇺🇦 Українська', callback_data='lang_uk'))

    return markup
