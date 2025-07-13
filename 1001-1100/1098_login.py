print("Login App")
username = input("Enter your username: ")

if username == "ayaz":
    password = input("Enter your password: ")
    if password == "ayaz123":
        print("Login Successfull!")
    else:
        print("Incorrect password!")
else:
    print("Invalid username!")