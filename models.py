from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
#with open('.../user.txt', 'r') as myfile:
 #   data = myfile.read()
db = PostgresqlDatabase("davidkulchar", user="davidkulchar")


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db