from peewee import *
from utils.config import *
import datetime

mysqlSqlConnection = MySQLDatabase(MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=int(MYSQL_PORT))

class BaseModel(Model):
    class Meta:
        database = mysqlSqlConnection

class Ip(BaseModel):
    ip_address = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)

mysqlSqlConnection.connect()
mysqlSqlConnection.create_tables([Ip])