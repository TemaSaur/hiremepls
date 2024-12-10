import inspect
from db.models import *
import db.models

from peewee import SqliteDatabase

import pytest


def get_models():
    models = []
    for _, obj in globals().items():
        if (inspect.isclass(obj)
                    and issubclass(obj, db.models.BaseModel)
                    and obj is not db.models.BaseModel
                ):
            models.append(obj)
    return models


@pytest.fixture(scope="function", autouse=True)
def use_database():
    db = SqliteDatabase('.test.db')
    models = get_models()
    print(models)
    for model in models:
        model._meta.database = db
        print(model.__name__)
    db.connect()
    db.create_tables(models)
    yield db
    db.drop_tables(models)
    db.close()
