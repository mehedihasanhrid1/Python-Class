import math

def add(x, y): 
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y): 
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x % y

def power(x, y): 
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of negative number."
    return math.sqrt(x)

def display_menu():
    print("\n--- Advanced Calculator Menu ---")
    print("1. Addition (x + y)")
    print("2. Subtraction (x - y)")
    print("3. Multiplication (x * y)")
    print("4. Division (x / y)")
    print("5. Modulo (x % y)")
    print("6. Power (x ** y)")
    print("7. Square Root (√x)")
    print("0. Quit")


def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        
        if choice == '7':
            x = float(input("Enter first number: "))

        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))
        elif choice == '5':
            print("Result:", modulus(x, y))
        elif choice == '6':
            print("Result:", power(x, y))
        elif choice == '7':
            print("Result:", square_root(x))
        else:
            print("Invalid choice. Please select a valid operation.")


calculator()
