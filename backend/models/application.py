from peewee import *
from models.base import BaseModel
from models.vacancy import Vacancy
from models.user import User
from models.resume import Resume


class Application(BaseModel):
    user = ForeignKeyField(User)
    vacancy = ForeignKeyField(Vacancy)
    resume = ForeignKeyField(Resume)
    message = TextField(default="")
    status = IntegerField(default=0)
