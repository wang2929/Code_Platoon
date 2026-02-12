# runner.py 
from classes.school import School 
from classes.staff import Staff
from classes.student import Student

'''
student_info = {'name':'Tiffany', 'age':'28', 'role':'TA', 'school_id':'U0AAEKX5762', 'password':'xx'}
print(Student(**student_info))
'''

school = School('Ridgemont High') 

#runner.py
#runner.py 

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        school_id = input('Enter the student ID: ')
        student = school.find_student_by_id(school_id)
        print(str(student))
    elif mode == '3':
        student_data = {'role':'student'}
        student_data['name']        = input('Enter student name:\n')
        student_data['age']         = input('Enter student age: \n')
        student_data['school_id']   = input('Enter student school id: \n')
        student_data['password']    = input('Enter student password: \n')
        
        school.add_student(**student_data)
    elif mode == '4':
        school_id = input('Enter the student ID: ')
        school.remove_student_by_id(school_id)
    else:
        break

