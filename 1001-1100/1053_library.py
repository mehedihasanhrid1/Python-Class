class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' by {author} added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book}")

    def borrow_book(self, book_number):
        if 1 <= book_number <= len(self.books):
            book = self.books[book_number - 1]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid book number.")

    def return_book(self, book_number):
        if 1 <= book_number <= len(self.books):
            book = self.books[book_number - 1]
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned '{book.title}'.")
            else:
                print("Book was not borrowed.")
        else:
            print("Invalid book number.")

    def search_books(self, keyword):
        found = False
        for idx, book in enumerate(self.books, 1):
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(f"{idx}. {book}")
                found = True
        if not found:
            print("No books found matching your search.")

    def remove_book(self, book_number):
        if 1 <= book_number <= len(self.books):
            removed = self.books.pop(book_number - 1)
            print(f"Removed '{removed.title}' by {removed.author}.")
        else:
            print("Invalid book number.")

def main():
    library = Library()
    initial_books = [
        ("To Kill a Mockingbird", "Harper Lee"),
        ("1984", "George Orwell"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("Pride and Prejudice", "Jane Austen"),
        ("The Catcher in the Rye", "J.D. Salinger"),
        ("The Hobbit", "J.R.R. Tolkien"),
        ("Moby Dick", "Herman Melville"),
        ("War and Peace", "Leo Tolstoy"),
        ("The Odyssey", "Homer"),
        ("Crime and Punishment", "Fyodor Dostoevsky"),
    ]
    
    for title, author in initial_books:
        library.add_book(title, author)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Remove Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            library.list_books()
            try:
                book_number = int(input("Enter the number of the book to borrow: "))
                library.borrow_book(book_number)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            library.list_books()
            try:
                book_number = int(input("Enter the number of the book to return: "))
                library.return_book(book_number)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            keyword = input("Enter title or author to search: ")
            library.search_books(keyword)
        elif choice == '6':
            library.list_books()
            try:
                book_number = int(input("Enter the number of the book to remove: "))
                library.remove_book(book_number)
            except ValueError:
                print("Invalid input.")
        elif choice == '7':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
