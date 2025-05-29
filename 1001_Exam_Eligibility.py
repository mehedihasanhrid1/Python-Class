cause = str(input("Do you have medical cause? (yes/no): ")).lower()
percentage = int(input("Enter your attendance percentage: "))

if cause == "yes":
    if percentage >= 60:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")
elif cause == "no":
    if percentage >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")
else:
    print("Invalid input!")