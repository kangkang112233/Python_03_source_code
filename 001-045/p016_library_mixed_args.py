class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, *categories, year=None, **details):
        book = {
            "title": title,
            "author": author,
            "categories": categories,
            "year": year,
            "details": details,
        }
        self.books.append(book)
        print(f"Added book: {book}")

    def list_books(self):
        for book in self.books:
            print(book)


# Create an instance of Library
library = Library()

# Add books with various arguments
library.add_book(
    "1984",
    "George Orwell",
    "Dystopian",
    "Political Fiction",
    year=1949,
    publisher="Secker & Warburg",
)
library.add_book(
    "To Kill a Mockingbird",
    "Harper Lee",
    "Southern Gothic",
    year=1960,
    awards=["Pulitzer Prize"],
)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

# List all books
library.list_books()
