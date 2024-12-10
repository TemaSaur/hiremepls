from peewee import *
from db.models.base import BaseModel, SlugField


class Resume(BaseModel):
    filename = CharField(max_length=255)
    filedata = BlobField()
    slug = SlugField()
