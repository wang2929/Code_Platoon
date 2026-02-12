class Person():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.role = kwargs['role']
        self.password = kwargs['password']
