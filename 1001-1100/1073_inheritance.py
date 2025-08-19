class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_role(self):
        return "Employee"

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def get_role(self):
        return "Manager"

    def calculate_salary(self):
        return self.base_salary + (self.team_size * 5000)

class Developer(Employee):
    def __init__(self, name, base_salary, skills):
        super().__init__(name, base_salary)
        self.skills = skills

    def get_role(self):
        return "Developer"

    def calculate_salary(self):
        return self.base_salary + (len(self.skills) * 800)

employees = [
    Manager("Amina Rahman", 90000, 6),
    Developer("Rafi Sarker", 60000, ["Python", "Django"])
]


for emp in employees:
    print(f"{emp.get_role()} - {emp.name} - Salary: {emp.calculate_salary()} Taka")


name_query = "Rafi"
found = [e for e in employees if name_query.lower() in e.name.lower()]
print("\nSearch Result:", found[0].name if found else "Not found")


employees = [e for e in employees if e.name != "Amina Rahman"]
print("\nRemaining Employees:", [e.name for e in employees])
