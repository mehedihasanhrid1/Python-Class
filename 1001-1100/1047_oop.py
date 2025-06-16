class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}'.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"  - {book.title}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member '{member.name}'.")

    def list_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(f"  - {book}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

if __name__ == "__main__":
    library = Library("City Library")

    library.add_book(Book("1984", "George Orwell", "1234567890"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "2345678901"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "3456789012"))


    alice = Member("Alice", 1)
    bob = Member("Bob", 2)
    library.add_member(alice)
    library.add_member(bob)

   
    library.list_books()

    book = library.find_book_by_title("1984")
    if book:
        alice.borrow_book(book)
    alice.list_borrowed_books()
    library.list_books()

    alice.return_book(book)
    alice.list_borrowed_books()
    library.list_books()