import random


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(10000, 99999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return {
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Student Age": self.student_age,

            "Student Number": self.student_number
        }


    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course Name: {course.course_name}, Course Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if self.courses_list else 0


students_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid Input. Please enter a valid number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value")

        student = Student(student_name, student_age, student_number)
        students_list.append(student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                students_list.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                student_details = student.get_student_details()
                print("Student Details:")
                for key, value in student_details.items():
                    print(f"{key}: {value}")
                break
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                student_average = student.get_student_average()
                print(f"Student Average: {student_average}")
                break
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                course = Course(course_name, course_mark)
                student.enroll_course(course)
                print("Course Added Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 6:
        exit()
    else:
        print("Invalid input, please select a valid input.")