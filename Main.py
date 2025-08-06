class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        print(f"[INIT] Employee Created: Name = {self.name}, ID = {self.employee_id}")

    def __del__(self):
        print(f"[DEL] Employee Deleted: Name = {self.name}, ID = {self.employee_id}")


def deleteMethod():
    print("[INFO] Creating Employee Object...")
    emp = Employee("Alex", 101)
    
    print("[INFO] Employee Object Created Successfully.")

    print("[INFO] Deleting Employee Object...")
    del emp

    print("[INFO] Employee Object Deleted.")

deleteMethod()



