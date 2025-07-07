number = int(input("Enter the number: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Division by zero is not allowed.")
elif number % divisor == 0:
    print(f"{number} is divisible by {divisor}.")
else:
    print(f"{number} is not divisible by {divisor}.")
