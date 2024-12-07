from peewee import *
from models.base import BaseModel, SlugField


class Organization(BaseModel):
    title = TextField()
    description = TextField()
    slug = SlugField()
