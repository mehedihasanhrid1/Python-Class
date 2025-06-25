def calculate_bill(subtotal,tip_percent,tax_percent):
        tip_amount = subtotal * (tip_percent / 100)
        tax_amount = subtotal * (tax_percent / 100)
        total = subtotal + tip_amount + tax_amount

        print("\n--- Restaurant Bill ---")
        print(f"Subtotal:   ${subtotal:0.2f}")
        print(f"Tip ({tip_percent}%):   ${tip_amount:0.2f}")
        print(f"Tax ({tax_percent}%):   ${tax_amount:0.2f}")
        print(f"Total:      ${total:0.2f}")


total = float(input("Enter the subtotal amount: $"))
tip= float(input("Enter tip percentage: "))
tax = 8

calculate_bill(total,tip,tax)