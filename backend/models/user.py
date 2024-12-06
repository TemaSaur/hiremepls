from peewee import *
from models.base import BaseModel


class User(BaseModel):
    email = CharField(max_length=255, unique=True, index=True)
    password_hash = CharField(max_length=60)
    full_name = TextField()
    course = IntegerField(default=0)

    class Meta:
        table_name = 'users'
        indexes = (
            (("email",), True),
        )
