# your User class goes here
from datetime import datetime
class User(object):
    LAST_POST_ID = 0
    ALL_USERS = []
    
    def __init__(self, name, email="example@email.com"):
        self.name = name
        self.email = email
        self.posts_list = []
        User.ALL_USERS.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.isalpha():
            self._name = value.title()
        else:
            print("Name should be a string. Did not create.")
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if type(value) is str and value[-4:] == ".com" and "@" in value:
            self._email = value
        else:
            print("Invalid email format. User not created.")
    
    def __str__(self):
        return f"My name is {self._name}"
    
    def add_post(self, text: str):
        post_data = {
            "id": User.LAST_POST_ID,
            "msg": text,
            "date": str(datetime.now())
        }
        self.posts_list.append(post_data)
        User.LAST_POST_ID += 1