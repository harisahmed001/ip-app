from peewee import *
from utils.config import *
import datetime

# Initializing the connection
mysqlSqlConnection = MySQLDatabase(MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=int(MYSQL_PORT))

# Model to create table on start
class BaseModel(Model):
    class Meta:
        database = mysqlSqlConnection

class Ip(BaseModel):
    ip_address = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)

# Connecting the DB
mysqlSqlConnection.connect()
# Creating tables in the DB
mysqlSqlConnection.create_tables([Ip])