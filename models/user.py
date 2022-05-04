from datetime import datetime

from peewee import IntegerField, CharField, BooleanField, DateTimeField

from .base import BaseModel, database


class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    username = CharField(default=None)
    language = CharField(default='en')

    is_admin = BooleanField(default=False)

    created_at = DateTimeField(default=lambda: datetime.utcnow())

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    class Meta:
        table_name = 'users'
