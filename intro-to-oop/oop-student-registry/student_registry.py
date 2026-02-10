class Student:
    def __init__(self, name, age=13, grade="12th"):
        self.name = name
        self.age = age
        self.grade = grade
        self.subject = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.isalpha() and len(value) > 3:
            self._name = value.title()
        elif not hasattr(self, 'name'):
            self._name = "Anonymous"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and 11 <= value <= 18:
            self._age = value
        elif not hasattr(self, 'age'):
            self._age = 13
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if isinstance(value, str) and value[-2:] == "th" and value[:-2].isdigit():
            grade_int = int(value[:-2])
            if grade_int >= 9 and grade_int <= 12:
                self._grade = value
        elif isinstance(value, str) and value.isdigit() and 9 <= value <= 12:
            self._grade = value + "th"
        elif not hasattr(self, 'grade'):
            self._grade = "12th"
    
    def __str__(self):
        return f"Student name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    def advance(self, years_advance = 1):
        grade_int = int(self._grade[:-2])
        advance_grade = str(grade_int + years_advance) + "th"
        return f"{self._name} has advanced to the {advance_grade} grade"
    
    def study(self, value):
        if isinstance(value, str):
            return f"{self._name} is studying {value.title()}"
