m = int(input("Enter your marks: "))

if m < 33:
    print("Grade: F")
elif 33 <= m <= 39:
    print("Grade: D")
elif 40 <= m <= 49:
    print("Grade: C")
elif 50 <= m <= 59:
    print("Grade: B")
elif 60 <= m <= 69:
    print("Grade: A-")
elif 70 <= m <= 79:
    print("Grade: A")
elif 80 <= m <= 100:
    print("Grade: A+")
else:
    print("Invalid input!")