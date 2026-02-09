# your User class goes here
class User(object):
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("Called setter")
        if isinstance(value, str) and value.isalpha():
            self._name = value.title()
        else:
            raise ValueError("Name must be string")
    
    def __str__(self):
        return f"My name is {self._name}"
    
def create_user():
    name = input("Enter name: ")
    return User(name)

test_user = create_user()
print(test_user)
