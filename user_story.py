from models import *

class UserStory(BaseModel):
    title = TextField()
    story_text = TextField()
    acceptance_criteria = TextField()
    buisness_value = IntegerField()
    estimation = FloatField()
    status = CharField()
