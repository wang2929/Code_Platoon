from student_registry import Student

def create_student_from_terminal():
    inputs = {
        "name": input("Enter student name: "),
        "age": input("Enter student age or leave blank: "),
        "grade": input("Enter student grade (9th - 12th) or leave blank: ")
    }
    student = Student(**inputs)
    return student

print("\nPlease make a student")
new_student = create_student_from_terminal()
print(new_student)