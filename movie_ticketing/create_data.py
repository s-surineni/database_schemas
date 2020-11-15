from models import UserAccount, Complex
from peewee import (PostgresqlDatabase)



def create_users():
     UserAccount.create(name='Tony')
     UserAccount.create(name='Bruce')


def create_complex():
     Complex.create(name='Prasads')
     Complex.create(name='PVR')



pg_db = PostgresqlDatabase('movies',
                           user='miyagi',
                           password='miyagi',
                           host='0.0.0.0',
                           port=5444)
pg_db.connect()
create_users()
create_complex()
pg_db.commit()
