from models.base import db
from models.user import User


def migrate():
    with db:
        db.create_tables([User])
