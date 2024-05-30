class Library:
    def __init__(self):
        self.books = []

    # Method with positional-only arguments
    def add_book(self, title, author, /, *, year=None, publisher=None):
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


# Create an instance of Library
library = Library()

# Add books with positional-only arguments
library.add_book("1984", "George Orwell", year=1949, publisher="Secker & Warburg")
library.add_book("To Kill a Mockingbird", "Harper Lee", year=1960)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

# List all books
library.list_books()
