from classes.staff import Staff
from classes.student import Student
import csv, os.path
class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
        

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        student_var = Student(**student_data)
        self.students.append(student_var) 
        headers = ["name", "age", "password", "role", "school_id"]
        with open('data/students.csv', mode ='w') as x:
            new_csv = csv.DictWriter(x, headers)
            new_csv.writeheader()
            for i in self.students:
                new_csv.writerow(i.__dict__)

                


    

