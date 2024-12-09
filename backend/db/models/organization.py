from peewee import *
from db.models.base import BaseModel, SlugField


class Organization(BaseModel):
    title = TextField()
    description = TextField()
    slug = SlugField()
