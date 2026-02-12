import csv
import pandas as pd
from classes.person import Person
# student.py
class Student(Person):
    students_list = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.school_id = kwargs['school_id']
        
    @classmethod
    def all_students(cls):
        with open('data/students.csv') as csvfile:
            student_reader = csv.DictReader(csvfile)
            for row in student_reader:
                cls.students_list.append(Student(**row))
        return cls.students_list
    
    @classmethod
    def add_student(cls, **kwargs):
        fieldnames = ['name', 'age', 'role', 'school_id', 'password']
        with open('data/students.csv', mode='a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(kwargs)
    
    @classmethod
    def remove_student(cls, student_id):
        df = pd.read_csv('data/students.csv')
        df = df.drop(df.query(f"school_id=={student_id}").index)
        print(df)
        df.to_csv('data/students.csv', index=False)
        
    
    def __str__(self):
        return f"{self.name} {self.school_id}"