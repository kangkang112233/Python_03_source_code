class Library:
    def __init__(self):
        self.books = []

    # Method with default argument values
    def add_book(self, title, author, year=None):
        book = {"title": title, "author": author, "year": year}
        self.books.append(book)
        print(f"Added book: {book}")

    def list_books(self):
        for book in self.books:
            print(book)


# Create an instance of Library
library = Library()

# Add books with and without the 'year' argument
library.add_book("1984", "George Orwell", 1949)
library.add_book("To Kill a Mockingbird", "Harper Lee")

# List all books
library.list_books()
