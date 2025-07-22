class Product:
	def __init__(self, name, price, stock):
		self.__name = name
		self.__price = price
		self.__stock = stock

	def get_name(self):
		return self.__name

	def get_price(self):
		return self.__price

	def get_stock(self):
		return self.__stock

	def set_price(self, price):
		if price > 0:
			self.__price = price

	def set_stock(self, stock):
		if stock >= 0:
			self.__stock = stock

	def reduce_stock(self, quantity):
		if 0 < quantity <= self.__stock:
			self.__stock -= quantity
			return True
		return False


class Customer:
	def __init__(self, name):
		self.__name = name
		self.__cart = []

	def get_name(self):
		return self.__name

	def add_to_cart(self, product, quantity):
		self.__cart.append((product, quantity))

	def get_cart(self):
		return self.__cart

	def clear_cart(self):
		self.__cart = []


class Sale:
	def __init__(self, customer):
		self.__customer = customer
		self.__items = []
		self.__total = 0

	def process_sale(self):
		for product, quantity in self.__customer.get_cart():
			if product.reduce_stock(quantity):
				self.__items.append((product, quantity))
				self.__total += product.get_price() * quantity
			else:
				print(f"Not enough stock for {product.get_name()}")
		self.__customer.clear_cart()

	def get_total(self):
		return self.__total

	def get_items(self):
		return self.__items

	def print_receipt(self):
		print(f"Receipt for {self.__customer.get_name()}:")
		for product, quantity in self.__items:
			print(f"{product.get_name()} x{quantity} @ {product.get_price()} each")
		print(f"Total: {self.__total}")



if __name__ == "__main__":
	p1 = Product("Laptop", 1200, 10)
	p2 = Product("Mouse", 25, 50)
	customer = Customer("Alice")
	customer.add_to_cart(p1, 1)
	customer.add_to_cart(p2, 2)
	sale = Sale(customer)
	sale.process_sale()
	sale.print_receipt()