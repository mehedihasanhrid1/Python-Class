class Employee:
    def __init__(self, emp_id, name, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def set_work_hours(self, hours):
        self.hours_worked = hours

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def display_info(self):
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Type          : {self.get_employee_type()}")
        print(f"Hours Worked  : {self.hours_worked}")
        print(f"Hourly Rate   : {self.hourly_rate} Taka")
        print(f"Total Salary  : {self.calculate_salary()} Taka\n")

    def get_employee_type(self):
        return "General Employee"

class RegularEmployee(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        if self.hours_worked > 160:
            bonus = 0.10 * base_salary  
            return base_salary + bonus
        return base_salary

    def calculate_overtime_bonus(self):
        if self.hours_worked > 160:
            bonus = 0.10 * (self.hours_worked * self.hourly_rate)
            print(f"[NOTE] Overtime Bonus: {bonus:.2f} Taka")
        else:
            print("[NOTE] No Overtime Bonus")

    def get_employee_type(self):
        return "Regular Employee"


class TemporaryEmployee(Employee):
    def check_max_hours(self):
        if self.hours_worked > 120:
            print("[Warning] Temporary employee exceeded 120 working hours!")
            print()
        else:
            print("[NOTE] Working hours within the permitted limit.")
            print()
    def get_employee_type(self):
        return "Temporary Employee"
if __name__ == "__main__":
    emp1 = RegularEmployee(emp_id=301, name="Mahmudullah Riyad", hourly_rate=300)
    emp2 = TemporaryEmployee(emp_id=302, name="Soumya Sarkar", hourly_rate=200)
    emp3 = RegularEmployee(emp_id=303, name="Tamim Iqbal", hourly_rate=320)
    emp1.set_work_hours(170)  
    emp2.set_work_hours(130) 
    emp3.set_work_hours(150) 
    employees = [emp1, emp2, emp3]
    for emp in employees:
        emp.display_info()
        if isinstance(emp, RegularEmployee):
            emp.calculate_overtime_bonus()
            print()
        elif isinstance(emp, TemporaryEmployee):
            emp.check_max_hours()
