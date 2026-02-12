import csv
from classes.person import Person
# staff.py
class Staff(Person):
    staff_list = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = kwargs['employee_id']
        
    @classmethod
    def all_staff(cls):
        with open('data/staff.csv') as csvfile:
            student_reader = csv.DictReader(csvfile)
            for row in student_reader:
                cls.staff_list.append(Staff(**row))
        return cls.staff_list