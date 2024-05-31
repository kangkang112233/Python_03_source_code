# Example to demonstrate unpacking dictionary items in a Library Management System


class Library:
    def __init__(self):
        self.books = {}

    # Method to add a book with a unique identifier
    def add_book(self, book_id, title, author, year=None, publisher=None):
        self.books[book_id] = {
            "title": title,
            "author": author,
            "year": year,
            "publisher": publisher,
        }
        print(
            f"Added book: ID='{book_id}', Title='{title}', Author='{author}', "
            f"Year='{year}', Publisher='{publisher}'"
        )

    # Method to list all books
    def list_books(self):
        for book_id, details in self.books.items():
            print(
                f"ID='{book_id}', Title='{details['title']}', Author='{details['author']}', "
                f"Year='{details['year']}', Publisher='{details['publisher']}'"
            )

    # Method to demonstrate unpacking dictionary items
    def unpack_books(self):
        for book_id, (title, author, year, publisher) in self.books.items():
            print(
                f"Unpacked: ID='{book_id}', Title='{title}', Author='{author}', "
                f"Year='{year}', Publisher='{publisher}'"
            )


# Create an instance of Library
library = Library()

# Add books to the library
library.add_book(1, "1984", "George Orwell", 1949, "Secker & Warburg")
library.add_book(
    2, "To Kill a Mockingbird", "Harper Lee", 1960, "J.B. Lippincott & Co."
)
library.add_book(
    3, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Charles Scribner's Sons"
)

# List all books
library.list_books()

# Unpack and display book details
library.unpack_books()
