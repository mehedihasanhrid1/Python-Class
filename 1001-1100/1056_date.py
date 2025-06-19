import datetime
import calendar

def print_menu():
    print("\nDate & Calendar Utility")
    print("1. Show today's date")
    print("2. Calculate days between two dates")
    print("3. Show calendar for a month")
    print("4. Find weekday of a date")
    print("5. Show current time in GMT+6")
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

def show_month_calendar():
    try:
        year = int(input("Enter year (e.g. 2024): "))
        month = int(input("Enter month (1-12): "))
        print(calendar.month(year, month))
    except Exception:
        print("Invalid input.")
        
def find_weekday():
    d = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        print(f"Weekday: {calendar.day_name[date.weekday()]}")
    except Exception:
        print("Invalid date format.")

def show_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    print(f"Current time in GMT+6: {now.strftime('%Y-%m-%d %H:%M:%S')}")

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
            find_weekday()
        elif choice == '5':
            show_time()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()