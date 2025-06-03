class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"My name is {self.name}. I am {self.age} years old. I read in class {self.grade}")

student1 = student("Alice", 20, 6)

student1.display_info()
