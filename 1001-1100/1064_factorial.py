def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    

n = int(input("Enter a valid integer: "))

if n < 0:
    print("Factorial is invalid for negative number.")
else:
    print(f"The factoiral of {n} is = {factorial(n)}")        