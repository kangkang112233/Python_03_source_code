import contextlib
import datetime


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = author
        print(
            f"{datetime.datetime.now()}: Book added - Title: '{title}', "
            f"Author: '{author}'"
        )

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print
            (f"{datetime.datetime.now()}: Book removed - Title: '{title}'")
        else:
            print(
                f"{datetime.datetime.now()}: Attempted to remove non-existent "
                f"book - Title: '{title}'"
            )

    def list_books(self):
        print(f"{datetime.datetime.now()}: Listing all books")
        for title, author in self.books.items():
            print(f"Title: '{title}', Author: '{author}'")


# Create an instance of Library
library = Library()

# Create a log file to capture the operations
log_file = "library_operations.log"
with open(log_file, "w") as f:
    with contextlib.redirect_stdout(f):
        # Perform some operations
        library.add_book("1984", "George Orwell")
        library.add_book("To Kill a Mockingbird", "Harper Lee")
        library.list_books()
        library.remove_book("1984")
        library.list_books()
        library.remove_book("The Great Gatsby")
        # Attempt to remove a non-existent book

# Display the content of the log file
with open(log_file, "r") as f:
    print(f.read())
