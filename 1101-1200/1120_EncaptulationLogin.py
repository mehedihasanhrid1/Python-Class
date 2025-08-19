class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def get_username(self):
        return self.__username
    def verify_password(self, password):
        return self.__password == password


class SignUp(User):
    def __init__(self):
        self.registered_users = {} 

    def create_account(self, username, password):
        if username in self.registered_users:
            return "Username already exists!"
        if len(password) < 4:
            return "Password must be at least 4 characters long."
        
        new_user = User(username, password)
        self.registered_users[username] = new_user
        return "Account created successfully!"


class Login(SignUp):  
    def authenticate(self, username, password):
        if username not in self.registered_users:
            return "No account found with this username."
        
        user = self.registered_users[username]
        if user.verify_password(password):
            return f"Welcome back, {user.get_username()}!"
        else:
            return "Incorrect password."

if __name__ == "__main__":
    system = Login()

    while True:
        print("\n===== LOGIN SYSTEM =====")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            print(system.create_account(uname, pwd))

        elif choice == "2":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            print(system.authenticate(uname, pwd))

        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


