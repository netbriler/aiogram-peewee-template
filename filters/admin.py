from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from services.users import get_user


class Admin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin, *args, **kwargs):
        self.is_admin = is_admin

    async def check(self, message):
        session = message.bot.get('session')
        user = await get_user(session, message.from_user.id)

        if not user:
            return False

        return user.is_admin