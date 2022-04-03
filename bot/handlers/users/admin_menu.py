import csv

from aiogram.types import Message, InputFile
from sqlalchemy.ext.asyncio import AsyncSession

from loader import dp, bot, config, _
from services.users import count_users, get_users


@dp.message_handler(i18n_text='Export users 📁', is_admin=True)
@dp.message_handler(commands=['export_users'], is_admin=True)
async def _export_users(message: Message, session: AsyncSession):
    count = await count_users(session)

    file_path = config.DIR / 'users.csv'
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(['id', 'name', 'username', 'language', 'created_at'])

        for user in await get_users(session):
            writer.writerow([user.id, user.name, user.username, user.language, user.created_at])

    text_file = InputFile(file_path, filename='users.csv')
    await message.answer_document(text_file, caption=_('Total users: {count}').format(count=count))


@dp.message_handler(i18n_text='Count users 👥', is_admin=True)
@dp.message_handler(commands=['count_users'], is_admin=True)
async def _users_count(message: Message, session: AsyncSession):
    count = await count_users(session)

    await message.answer(_('Total users: {count}').format(count=count))


@dp.message_handler(i18n_text='Count active users 👥', is_admin=True)
@dp.message_handler(commands=['count_active_users'], is_admin=True)
async def _active_users_count(message: Message, session: AsyncSession):
    users = await get_users(session)

    count = 0
    for user in users:
        try:
            if await bot.send_chat_action(user.id, 'typing'):
                count += 1
        except Exception:
            pass

    await message.answer(_('Active users: {count}').format(count=count))
