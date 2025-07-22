num = int(input("Enter a number: "))
digits = [int(d) for d in str(abs(num))]
n = len(digits)
if n == 0:
    print("No middle digit exist.")
if n % 2 == 1:    
    result = digits[n // 2]
else:
    mid1 = digits[n // 2 - 1]
    mid2 = digits[n // 2]
    result = mid1 * mid2

print("Product of middle digit(s):", result)