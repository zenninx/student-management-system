class Student:
    def __init__(self, student_id, name, age, course, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "grade": self.grade
        }

    def display(self):
        print("----------------------------")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")
