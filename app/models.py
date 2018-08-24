from peewee import CharField, Model, MySQLDatabase
from app import app

MYSQL_DB = 'together'
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = ''

db = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    username = CharField()
    password = CharField()
    token = CharField()