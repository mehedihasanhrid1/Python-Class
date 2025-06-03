n = int(input("Enter a number: "))

temp = n
s = 0

while temp > 0:
    digit = temp % 10
    s += digit ** 3
    temp //= 10
    
if s == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")    