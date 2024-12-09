"""Peewee migrations -- 003_implement_schema.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.run(func, *args, **kwargs)           # Run python function with the given args
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.add_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)
    > migrator.add_constraint(model, name, sql)
    > migrator.drop_index(model, *col_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.drop_constraints(model, *constraints)

"""

from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator


with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your migrations here."""
    
    @migrator.create_model
    class Vacancy(pw.Model):
        id = pw.AutoField()
        title = pw.TextField()
        organization = pw.ForeignKeyField(column_name='organization_id', field='id', model=migrator.orm['organization'])
        description = pw.TextField(default='')
        pay = pw.IntegerField(default=0)
        worktime = pw.TextField(default='')

        class Meta:
            table_name = "vacancy"

    @migrator.create_model
    class Resume(pw.Model):
        id = pw.AutoField()
        filename = pw.CharField(max_length=255)
        filedata = pw.BlobField()

        class Meta:
            table_name = "resume"

    @migrator.create_model
    class Application(pw.Model):
        id = pw.AutoField()
        user = pw.ForeignKeyField(column_name='user_id', field='id', model=migrator.orm['users'])
        vacancy = pw.ForeignKeyField(column_name='vacancy_id', field='id', model=migrator.orm['vacancy'])
        resume = pw.ForeignKeyField(column_name='resume_id', field='id', model=migrator.orm['resume'])
        message = pw.TextField(default='')
        status = pw.IntegerField(default=0)

        class Meta:
            table_name = "application"


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
    migrator.remove_model('vacancy')

    migrator.remove_model('resume')

    migrator.remove_model('application')
