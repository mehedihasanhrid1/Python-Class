# class Operation():
#     def __init__(self):
#         self.s = ""

#     def get(self):
#         self.s = input("Enter a string or sentence: ")
    
#     def output(self):
#         print("Result is:",self.s.upper())
        
# a = Operation()
# a.get()
# a.output()       

class Employee:
    def __init__(self):
        print("Employe created")
    def __del__(self):
        print("Employee deleted")

def Data():
    print("Making employee data")
    d = Employee()
    print("Function executed")
    return d

print("Starting the system")
a = Data()
print("End the system!")
