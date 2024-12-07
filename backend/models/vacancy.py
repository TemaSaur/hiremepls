from peewee import *
from models.base import BaseModel, SlugField
from models.organization import Organization


class Vacancy(BaseModel):
    title = TextField()
    organization = ForeignKeyField(Organization)
    description = TextField(default="")
    pay = IntegerField(default=0)
    worktime = TextField(default="")
    slug = SlugField()
