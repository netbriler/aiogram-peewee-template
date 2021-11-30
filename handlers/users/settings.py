from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from keyboards.inline import get_language_inline_markup
from loader import dp, _
from services.users import edit_user_language


@dp.callback_query_handler(Regexp('^lang_(\w\w)$'))
async def change_language(callback_query: CallbackQuery, regexp: Regexp):
    session = callback_query.bot.get('session')
    language = regexp.group(1)

    await edit_user_language(session, callback_query.from_user.id, language)

    await callback_query.message.answer(_('Язык успешно изменен \n'
                                          'Нажми /help чтобы узнать чем я могу тебе помочь', locale=language))
    await callback_query.message.delete()


@dp.message_handler(commands='lang')
async def bot_start(message: Message):
    text = _('Выбери свой язык').format(full_name=message.from_user.full_name)

    await message.answer(text, reply_markup=get_language_inline_markup())
