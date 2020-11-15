from peewee import (CharField,
                    Model, PostgresqlDatabase)


pg_db = PostgresqlDatabase('movies',
                           user='miyagi',
                           password='miyagi',
                           host='0.0.0.0',
                           port=5444)

class UserAccount(Model):
    name = CharField()

    class Meta:
        database = pg_db


class Complex(Model):
    name = CharField()

    class Meta:
        database = pg_db


pg_db.connect()
pg_db.create_tables([UserAccount])
pg_db.create_tables([Complex])

pg_db.commit()
