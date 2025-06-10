def display_menu(menu):
    print("----- Menu -----")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print("----------------")

def take_order(menu):
    order = {}
    while True:
        item = input("Enter item name to order (or 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        if item in menu:
            qty = int(input(f"Enter quantity for {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not found in menu.")
    return order

def calculate_bill(order, menu, tax_rate, tip_percent):
    subtotal = sum(menu[item] * qty for item, qty in order.items())
    tax = subtotal * tax_rate
    tip = (subtotal * tip_percent)/100
    total = subtotal + tax + tip
    return subtotal, tax, tip, total

def print_bill(order, menu, subtotal, tax, tip, total, printed=[False]):
    if printed[0]:
        return
    printed[0] = True
    print("\n----- Bill -----")
    for item, qty in order.items():
        print(f"{item} x {qty} = ${menu[item]*qty:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    print("----------------")

def main():
    menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Salad": 4.99,
        "Soda": 1.99,
        "Fries": 2.99,
        "Water":0.89
    }
    tax_rate = 0.07  # 7% tax
    display_menu(menu)
    order = take_order(menu)
    if not order:
        print("No items ordered.")
        return
    tip_percent = float(input("Enter tip percentage (e.g. 15 for 15%): "))
    subtotal, tax, tip, total = calculate_bill(order, menu, tax_rate, tip_percent)
    print_bill(order, menu, subtotal, tax, tip, total)

if __name__ == "__main__":
    main()