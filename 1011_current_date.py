from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

print("Current Date:", get_current_date())
print("Current Time:", get_current_time())