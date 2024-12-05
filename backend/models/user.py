from peewee import *
from models.base import BaseModel


class User(BaseModel):
    email = TextField(unique=True)
    password_hash = CharField(max_length=60)
    full_name = TextField()
    course = IntegerField(null=True)

    class Meta:
        table_name = 'users'
