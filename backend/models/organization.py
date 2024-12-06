from peewee import *
from models.base import BaseModel


class Organization(BaseModel):
    title = TextField()
    description = TextField()
