cause = input("Did you have medical reason? (Yes/No): ").lower()

if cause == "yes":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 60:
        print("You are eligible for exam.")
    else:
        print("You are not eligible for exam.")

elif cause == "no":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 75:
        print("You are eligible for exam.")
    else:
        print("You are not eligible for exam.")

else:
    print("Invalid input!")