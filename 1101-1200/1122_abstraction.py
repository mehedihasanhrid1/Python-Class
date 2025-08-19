from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.balance} Taka"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Taka deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} Taka withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest:.2f} Taka added.")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, balance=0):
        if account_number in self.accounts:
            print("Account number already exists!")
            return
        account = SavingsAccount(account_number, account_holder, balance)
        self.accounts[account_number] = account
        print(f"Savings Account created for {account_holder}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        for acc in self.accounts.values():
            print(acc)
def main():
    bank = BankSystem()
    while True:
        print("\n===== Savings Account Menu =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Add Interest")
        print("6. Display All Accounts")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            acc_num = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(acc_num, acc_holder, balance)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found!")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter withdraw amount: "))
                account.withdraw(amount)
            else:
                print("Account not found!")
        elif choice == "4":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                print(f"Balance: {account.get_balance()} Taka")
            else:
                print("Account not found!")
        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                account.add_interest()
            else:
                print("Account not found!")
        elif choice == "6":
            bank.display_all_accounts()
        elif choice == "7":
            print("Thank you for using the Savings Account System!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
