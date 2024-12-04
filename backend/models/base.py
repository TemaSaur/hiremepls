from peewee import *


db = PostgresqlDatabase('postgres', user='postgres',
                        password='postgres', host='0.0.0.0', port=5432)


class BaseModel(Model):
    class Meta:
        database = db
