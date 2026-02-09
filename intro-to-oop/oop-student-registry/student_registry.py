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
        if isinstance(value, str) and len(value) > 3 and value.isalpha():
            self._name = value.title()
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 11 and value <= 18:
            self._age = value
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if isinstance(value, str) and value[-2:] == "th" and value[:-2].isdigit():
            grade_int = int(value[:-2])
            if grade_int >= 9 and grade_int <= 12:
                self._grade = value
        elif isinstance(value, str) and value.isdigit() and value >= 9 and value <= 12:
            self._grade = value + "th"
    
    def __str__(self):
        return f"Student name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    def advance(self, years_advance = 1):
        grade_int = int(self._grade[:-2])
        advance_grade = str(grade_int + years_advance) + "th"
        return f"{self._name} has advanced to the {advance_grade} grade"
    
    def study(self, value):
        if isinstance(value, str):
            return f"{self._name} is studying {value.title()}"

'''
def create_student_from_terminal():
    inputs = {
        "name": input("Enter student name: "),
        "age": input("Enter student age or leave blank: "),
        "grade": input("Enter student grade (9th - 12th) or leave blank: ")
    }
    student = Student(**inputs)
    return student

registry = []
while True:
    print("\nPlease make a student")
    new_student = create_student_from_terminal()
    registry.append(new_student)
'''