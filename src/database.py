from peewee import *
import env
database = MySQLDatabase(database=env._DATABASE, user=env._USER, password=env._PASSWORD,host=env._HOST)

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    id= IntegerField()
    username = CharField()
    password=CharField()
    
    class Meta:
        db_table = 'users'
