from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from services.users import get_user


class Admin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def check(self, message: Message):
        if 'database_user' not in message:
            message['database_user'] = get_user(message.from_user.id)
        user = message['database_user']

        if not user:
            return False

        return user.is_admin == self.is_admin
