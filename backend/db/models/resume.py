from peewee import *
from db.models.base import BaseModel


class Resume(BaseModel):
    filename = CharField(max_length=255)
    filedata = BlobField()
