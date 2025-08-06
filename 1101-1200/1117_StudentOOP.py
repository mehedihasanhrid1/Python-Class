class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove_student_by_id(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def update_student_grade(self, student_id, new_grade):
        student = self.find_student_by_id(student_id)
        if student:
            student.grade = new_grade

student1 = Student(1, "Alice", 17, "A")
student2 = Student(2, "Bob", 16, "B")
student3 = Student(3, "Charlie", 18, "A")
student4 = Student(4, "Diana", 17, "C")
student5 = Student(5, "Ethan", 16, "B")


manager = StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)
manager.add_student(student4)
manager.add_student(student5)

manager.display_students()

print(manager.find_student_by_id(3))

manager.remove_student_by_id(2)
manager.display_students()

manager.update_student_grade(4, "B+")
manager.display_students()