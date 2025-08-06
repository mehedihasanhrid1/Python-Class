import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 120 

        self.root.configure(bg="#ad9bea")

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            bdt_price = price * self.exchange_rate
            label = ttk.Label(frame, text=f"{item} (৳{bdt_price}):", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 1, columnspan=3, padx=10, pady=10)

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        symbol = "৳"
        rate = self.exchange_rate
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()
