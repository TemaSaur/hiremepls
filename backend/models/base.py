from peewee import *
import random


db = PostgresqlDatabase('postgres', user='postgres',
                        password='postgres', host='0.0.0.0', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


def SlugField():
    return CharField(
        max_length=8,
        unique=True,
        default=lambda: "".join(
            random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            for _ in range(8))
    )
