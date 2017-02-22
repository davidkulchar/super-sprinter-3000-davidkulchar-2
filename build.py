# This script can create the database tables based on your models
from models import BaseModel
from user_story import *

db.connect()
# List the tables here what you want to create...
db.drop_tables([UserStory], safe=True)
db.create_tables([UserStory], safe=True)
#Example_data.create_data()