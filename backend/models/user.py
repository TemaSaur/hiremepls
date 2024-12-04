from peewee import *
from models.base import BaseModel


class User(BaseModel):
    email = TextField(unique=True)

    class Meta:
        table_name = 'users'
