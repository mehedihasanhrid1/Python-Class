from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._available = True

    @abstractmethod
    def display_info(self):
        pass

    def is_available(self):
        return self._available

    def borrow(self):
        if self._available:
            self._available = False
            print(f"'{self._title}' has been borrowed.")
        else:
            print(f"'{self._title}' is not available.")

    def return_item(self):
        self._available = True
        print(f"'{self._title}' has been returned.")

# Inheritance and Encapsulation
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self._pages = pages

    def display_info(self):
        print(f"Book: {self._title} by {self._author}, Pages: {self._pages}, Available: {self._available}")

class DVD(LibraryItem):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self._duration = duration

    def display_info(self):
        print(f"DVD: {self._title} by {self._author}, Duration: {self._duration} mins, Available: {self._available}")

# Polymorphism
def show_library_items(items):
    for item in items:
        item.display_info()

# User class with encapsulation
class User:
    def __init__(self, name):
        self.__name = name
        self.__borrowed_items = []

    def borrow_item(self, item):
        if item.is_available():
            item.borrow()
            self.__borrowed_items.append(item)
        else:
            print(f"{self.__name} cannot borrow '{item._title}'.")

    def return_item(self, item):
        if item in self.__borrowed_items:
            item.return_item()
            self.__borrowed_items.remove(item)
        else:
            print(f"{self.__name} did not borrow '{item._title}'.")

    def show_borrowed(self):
        print(f"{self.__name} has borrowed:")
        for item in self.__borrowed_items:
            print(f"  - {item._title}")

if __name__ == "__main__":
    # Create library items
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("Python Programming", "John Doe", 500)
    dvd1 = DVD("Inception", "Christopher Nolan", 148)

    library_items = [book1, book2, dvd1]

    # Show all items
    print("Library Inventory:")
    show_library_items(library_items)
    print()

    # Create users
    alice = User("Alice")
    bob = User("Bob")

    # Borrow and return items
    alice.borrow_item(book1)
    bob.borrow_item(book1)  # Already borrowed
    bob.borrow_item(dvd1)
    print()

    alice.show_borrowed()
    bob.show_borrowed()
    print()

    # Return items
    alice.return_item(book1)
    bob.borrow_item(book1)
    print()

    show_library_items(library_items)
        