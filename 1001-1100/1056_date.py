import datetime
import calendar

def print_menu():
    print("\nDate & Calendar Utility")
    print("1. Show today's date")
    print("2. Calculate days between two dates")
    print("3. Show calendar for a month")
    print("4. Show current time of Dhaka")
    print("5. Show weekdays")
    print("6. Exit")

def show_today():
    today = datetime.date.today()
    print(f"Today's date: {today}")

def days_between():
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")
    try:
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d").date()
        diff = abs((date2 - date1).days)
        print(f"Days between: {diff}")
    except ValueError:
        print("Invalid date format.")

def show_weekday():
    d = input("Enter a date (YYYY-MM-DD): ")
    try:
        date_obj = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        print(f"{d} is a {date_obj.strftime('%A')}")
    except ValueError:
        print("Invalid date format.")
        

def show_month_calendar():
    try:
        year = int(input("Enter year (e.g. 2024): "))
        month = int(input("Enter month (1-12): "))
        print(calendar.month(year, month))
    except Exception:
        print("Invalid input.")

def show_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    print(f"Current time in Dhaka: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            show_today()
        elif choice == '2':
            days_between()
        elif choice == '3':
            show_month_calendar()
        elif choice == '4':
            show_time()
        elif choice == '5':
            show_weekday()           
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()