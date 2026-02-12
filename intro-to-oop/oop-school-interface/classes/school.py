from classes.staff import Staff
from classes.student import Student
# school.py
class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def list_students(self):
        for i in range(len(self.students)):
            print(f"{i+1}. {self.students[i]}")
            
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return str(student)
    
    def add_student(self, **kwargs):
        new_student = Student(**kwargs)
        self.students.append(new_student)
        Student.add_student(**kwargs)
        
    def remove_student_by_id(self, student_id):
        Student.remove_student(student_id)
        for i in range(len(self.students)):
            if self.students[i].school_id == student_id:
                self.students = self.students[:i] + self.students[i+1:]
                return