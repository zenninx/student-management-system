import json
import os


FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(student):
    students = load_students()
    students.append(student)
    save_students(students)


def delete_student(student_id):

    students = load_students()

    students = [
        student for student in students
        if student["student_id"] != student_id
    ]

    save_students(students)


def update_student(updated_student):

    students = load_students()

    for student in students:
        if student["student_id"] == updated_student["student_id"]:
            student.update(updated_student)

    save_students(students)
