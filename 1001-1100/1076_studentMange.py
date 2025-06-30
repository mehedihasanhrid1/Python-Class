students = {}

def display_menu():
    print("\n================= Student Management System ================")
    print("1. Add students")
    print("2. Display all students")
    
def add_students():
    studentId = input("Enter student id: ")
    if studentId in students:
        print("\nStudent already exits.")
        return
    name = input("Enter student name: ")   
    age = int(input("Enter student age: "))
    grade = int(input("Enter students grade: "))   
    try:
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("\nInvalid marks input.")
        return
    students[studentId] = {
        "name": name,
        "age": age,
        "grade": grade,
        "marks": marks
    }
    print("\nStudents updates successfully!")
 
def display_students():
    if not students:
        print("\nNo records to display.")
        return
    print("\nAll student records:")
    
    for sid, info in students.items():
        print(f"\nStudent Id: {sid}")
        for key,value in info.items():
            print(f"{key.capitalize()}: {value}")
 
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_students()
        elif choice == "2":
            display_students()
        else:
            print("Invalid Choice! Please enter a number between 1 to 2.")


if __name__ == "__main__":
    main()    