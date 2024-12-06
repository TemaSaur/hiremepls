from .user import User
from .base import db


def create_tables():
    db.create_tables([User])
