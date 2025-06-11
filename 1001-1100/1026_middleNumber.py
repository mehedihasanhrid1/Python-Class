n = int(input("Enter a number: "))

s = str(n)

if len(s) % 2 == 0:
    m = len(s) // 2
    d = (s[m - 1], s[m])
else:
    m = len(s) // 2
    d = s[m]  
    
print(f"The middle digit(s) of the number is/are: {d}")

