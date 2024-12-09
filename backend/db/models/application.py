from peewee import *
from db.models.base import BaseModel
from db.models.vacancy import Vacancy
from db.models.user import User
from db.models.resume import Resume


class Application(BaseModel):
    user = ForeignKeyField(User)
    vacancy = ForeignKeyField(Vacancy)
    resume = ForeignKeyField(Resume)
    message = TextField(default="")
    status = IntegerField(default=0)
