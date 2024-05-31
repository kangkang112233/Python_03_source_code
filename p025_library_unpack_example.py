class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year=None, publisher=None):
        book = {"title": title, "author": author, "year": year, "publisher": publisher}
        self.books.append(book)
        print(
            f"Added book: Title='{title}', Author='{author}', Year='{year}', "
            f"Publisher='{publisher}'"
        )

    def list_books(self):
        for book in self.books:
            print(
                f"Title='{book['title']}', Author='{book['author']}', "
                f"Year='{book['year']}', Publisher='{book['publisher']}'"
            )

    def unpack_books(self):
        # Unpack book details into separate variables
        for book in self.books:
            title, author, year, publisher = book.values()
            print(
                f"Unpacked: Title='{title}', Author='{author}', Year='{year}', "
                f"Publisher='{publisher}'"
            )


# Create an instance of Library
library = Library()

# Add books
library.add_book("1984", "George Orwell", 1949, "Secker & Warburg")
library.add_book("To Kill a Mockingbird", "Harper Lee", 1960, "J.B. Lippincott & Co.")
library.add_book(
    "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Charles Scribner's Sons"
)

# List all books
library.list_books()

# Unpack and display book details
library.unpack_books()
