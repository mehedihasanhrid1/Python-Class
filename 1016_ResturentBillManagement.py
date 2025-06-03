TAX_RATE = 0.10

menu = {
    "Burger": 150.00,
    "Fries": 175.00,
    "Soda": 60.00,
    "Salad": 120.00,
    "Pizza": 500.00,
    "Ice Cream": 150.00,
    "Coffee": 200.00,
    "Tea": 55.00,
    "Juice": 90.00,
    "Pasta": 250.00,
    "Sandwich": 200.00,
    "Water": 20.00
}

order = {}

def show_menu():
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: Rs. {price:.2f}")
 
def take_order():
    while True:
        item = input("\nEnter the item you want to order (or 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        if item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not found in the menu. Please try again.")  
            
def calculate_total():
    total = 0.0
    for item, quantity in order.items():
        total += menu[item] * quantity
    tax = total * TAX_RATE
    total_with_tax = total + tax
    return total, tax, total_with_tax   

def print_bill():
    print("\n--- Bill Summary ---")
    total, tax, total_with_tax = calculate_total()
    for item, quantity in order.items():
        print(f"{item} x {quantity} = Rs. {menu[item] * quantity:.2f}")
    print(f"Subtotal: Rs. {total:.2f}")
    print(f"Tax (10%): Rs. {tax:.2f}")
    print(f"Total Amount: Rs. {total_with_tax:.2f}")  


if __name__ == "__main__":
    show_menu()
    take_order()
    print_bill()
    print("\nThank you for dining with us!")
    