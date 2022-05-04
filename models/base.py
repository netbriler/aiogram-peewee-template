from peewee import Model

from loader import database


class BaseModel(Model):
    class Meta:
        database = database
