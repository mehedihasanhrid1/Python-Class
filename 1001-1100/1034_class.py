class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def display_info(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}")

    def add_mark(self, subject, mark):
        self.marks[subject] = mark
        print(f"Added mark for {subject}: {mark}")

    def get_average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def display_marks(self):
        if not self.marks:
            print("No marks available.")
        else:
            for subject, mark in self.marks.items():
                print(f"{subject}: {mark}")


s = Student("Alice", 101)

s.display_info()
s.add_mark("Math", 90)
s.add_mark("Bangla", 96)
s.add_mark("Science", 85)
s.display_marks()
print(f"Average Marks: {s.get_average()}")